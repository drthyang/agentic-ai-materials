"""Anthropic backend for the campaign loop.

Secondary to the local backend; enables the Claude-vs-local comparison by
flipping `llm.backend` in mission.yaml (or `--backend anthropic`).

Three things matter for running it as an experimental arm rather than a demo:

- **Replay fidelity.** Current Claude models think adaptively, and a tool loop
  must send the assistant turn back unchanged — thinking blocks included —
  before its tool results. The neutral message format can't hold those
  blocks, so the response carries them in `provider_content` and `_to_wire`
  replays them verbatim. Parallel tool results go back in ONE user message.
- **Prompt caching.** Tools + system prompt are identical for every call in a
  campaign, and each turn's history is a prefix of the next, so the system
  block carries a breakpoint and top-level automatic caching marks the tail.
  Verify with `usage.cache_read_input_tokens` (recorded per run).
- **Spend accounting.** Every response's `usage` is accumulated and priced;
  `max_cost_usd` is a hard stop checked before each request, so a runaway
  campaign fails one call past the cap at worst, never silently.
"""

from __future__ import annotations

import json
import logging
from dataclasses import asdict, dataclass, field
from pathlib import Path

from athanor.llm.base import LLMBackend, LLMResponse, ToolCall, ToolSpec

log = logging.getLogger("athanor.llm")

# USD per million tokens: (input, output, cache read, 5-minute cache write).
# Source: https://platform.claude.com/docs/en/about-claude/pricing (checked
# 2026-10-11). Footnote 2 there: "Cache hits and refreshes on Claude Opus 5.5
# and Claude Sonnet 5.5 are priced at 0.05x the base input price" (Fable 5.1:
# 0.025x; the rest 0.1x). 5-minute cache writes are 1.25x base input.
PRICES_PER_MTOK: dict[str, tuple[float, float, float, float]] = {
    "claude-fable-5-1": (10.00, 50.00, 0.25, 12.50),
    "claude-fable-5": (10.00, 50.00, 1.00, 12.50),
    "claude-opus-5-5": (4.00, 20.00, 0.20, 5.00),
    "claude-opus-5": (5.00, 25.00, 0.50, 6.25),
    "claude-opus-4-8": (5.00, 25.00, 0.50, 6.25),
    "claude-opus-4-7": (5.00, 25.00, 0.50, 6.25),
    "claude-opus-4-6": (5.00, 25.00, 0.50, 6.25),
    "claude-sonnet-5-5": (2.00, 10.00, 0.10, 2.50),
    "claude-sonnet-5": (2.00, 10.00, 0.20, 2.50),
    "claude-sonnet-4-6": (3.00, 15.00, 0.30, 3.75),
    # Haiku 5.5 is priced by prompt length; this is the >100k-token tier,
    # the higher of the two, so the spend guard can only over-estimate
    "claude-haiku-5-5": (0.50, 2.50, 0.05, 0.625),
}
# For an unpriced model without a spend cap, cost every component at the
# highest rate on record (a component-wise maximum, so no single rate is
# under-counted). With a cap set, unpriced models are refused outright.
_FALLBACK_PRICE = tuple(max(p[i] for p in PRICES_PER_MTOK.values()) for i in range(4))


class SpendCapExceeded(RuntimeError):
    """Raised before a request once the backend's cost cap has been reached."""


@dataclass
class UsageTotals:
    calls: int = 0
    input_tokens: int = 0
    output_tokens: int = 0
    cache_read_input_tokens: int = 0
    cache_creation_input_tokens: int = 0
    stop_reasons: dict[str, int] = field(default_factory=dict)

    def add(self, usage: object, stop_reason: str | None) -> None:
        self.calls += 1
        self.input_tokens += getattr(usage, "input_tokens", 0) or 0
        self.output_tokens += getattr(usage, "output_tokens", 0) or 0
        self.cache_read_input_tokens += getattr(usage, "cache_read_input_tokens", 0) or 0
        self.cache_creation_input_tokens += (
            getattr(usage, "cache_creation_input_tokens", 0) or 0
        )
        key = stop_reason or "none"
        self.stop_reasons[key] = self.stop_reasons.get(key, 0) + 1

    def cost_usd(self, model: str) -> float:
        p_in, p_out, p_read, p_write = price_for(model)
        return (
            self.input_tokens * p_in
            + self.output_tokens * p_out
            + self.cache_read_input_tokens * p_read
            + self.cache_creation_input_tokens * p_write
        ) / 1e6


def price_for(model: str) -> tuple[float, float, float, float]:
    if model in PRICES_PER_MTOK:
        return PRICES_PER_MTOK[model]
    log.warning("no price on record for %s; costing at the highest known rates", model)
    return _FALLBACK_PRICE


class SpendTracker:
    """One budget for every Claude backend in a campaign (proposer and critic).

    Each attached backend checks the shared total before every request, so
    a hybrid local-proposer + Claude-critic run is capped like any other,
    and flushes its own usage file (``usage.json`` for the proposer,
    ``<role>_usage.json`` otherwise) after every call.
    """

    def __init__(self, cap_usd: float | None = None, usage_dir: Path | None = None):
        self.cap_usd = cap_usd
        self.usage_dir = usage_dir
        self.members: list[tuple[str, AnthropicBackend]] = []

    def attach(self, backend: "AnthropicBackend", role: str) -> None:
        if self.cap_usd is not None and backend.model not in PRICES_PER_MTOK:
            raise ValueError(f"no price on record for {backend.model!r}; refusing to run "
                             "it under a spend cap (add it to PRICES_PER_MTOK)")
        backend.tracker = self
        if self.usage_dir is not None:
            name = "usage.json" if role == "proposer" else f"{role}_usage.json"
            backend.usage_path = Path(self.usage_dir) / name
        self.members.append((role, backend))

    @property
    def spent_usd(self) -> float:
        return sum(b.cost_usd for _, b in self.members)

    def check(self) -> None:
        if self.cap_usd is not None and self.spent_usd >= self.cap_usd:
            raise SpendCapExceeded(
                f"campaign spent ${self.spent_usd:.2f} of the ${self.cap_usd:.2f} cap")


class AnthropicBackend(LLMBackend):
    name = "anthropic"

    def __init__(
        self,
        model: str = "claude-sonnet-5-5",
        max_tokens: int = 16000,
        effort: str | None = None,
        max_cost_usd: float | None = None,
        client: object | None = None,
    ):
        self.model = model
        self.max_tokens = max_tokens
        self.effort = effort
        if max_cost_usd is not None and model not in PRICES_PER_MTOK:
            raise ValueError(f"no price on record for {model!r}; refusing to run it "
                             "under a spend cap (add it to PRICES_PER_MTOK)")
        self.max_cost_usd = max_cost_usd
        self.tracker: SpendTracker | None = None
        self.usage = UsageTotals()
        # when set, usage is flushed here after every call so a killed run
        # still leaves an exact spend record
        self.usage_path: Path | None = None
        if client is None:
            import anthropic

            client = anthropic.Anthropic()
        self._client = client

    # -- accounting ---------------------------------------------------------
    @property
    def cost_usd(self) -> float:
        return self.usage.cost_usd(self.model)

    def usage_summary(self) -> dict:
        return {
            "backend": self.name,
            "model": self.model,
            "effort": self.effort,
            **asdict(self.usage),
            "cost_usd": round(self.cost_usd, 4),
            "max_cost_usd": self.max_cost_usd,
        }

    # -- the call -----------------------------------------------------------
    def chat(self, system: str, messages: list[dict], tools: list[ToolSpec]) -> LLMResponse:
        if self.max_cost_usd is not None and self.cost_usd >= self.max_cost_usd:
            raise SpendCapExceeded(
                f"spent ${self.cost_usd:.2f} of the ${self.max_cost_usd:.2f} cap"
            )
        if self.tracker is not None:
            self.tracker.check()
        kwargs: dict = {
            "model": self.model,
            "max_tokens": self.max_tokens,
            # breakpoint 1: tools + system, identical across the campaign
            "system": [{"type": "text", "text": system,
                        "cache_control": {"type": "ephemeral"}}],
            "messages": self._to_wire_messages(messages),
            # breakpoint 2 (automatic): the tail of the growing tool loop
            "cache_control": {"type": "ephemeral"},
        }
        if tools:
            kwargs["tools"] = [
                {"name": t.name, "description": t.description,
                 "input_schema": t.input_schema}
                for t in tools
            ]
        if self.effort:
            kwargs["output_config"] = {"effort": self.effort}

        response = self._client.messages.create(**kwargs)
        self.usage.add(response.usage, response.stop_reason)
        self._flush_usage()
        u = response.usage
        log.info(
            "anthropic call %d: in=%s cache_read=%s cache_write=%s out=%s stop=%s "
            "| run total $%.3f",
            self.usage.calls, u.input_tokens, getattr(u, "cache_read_input_tokens", 0),
            getattr(u, "cache_creation_input_tokens", 0), u.output_tokens,
            response.stop_reason, self.cost_usd,
        )
        if response.stop_reason in ("refusal", "max_tokens"):
            log.warning("anthropic stop_reason=%s", response.stop_reason)

        text = ""
        tool_calls = []
        blocks = []
        for block in response.content:
            blocks.append(_block_to_dict(block))
            if block.type == "text":
                text += block.text
            elif block.type == "tool_use":
                tool_calls.append(
                    ToolCall(id=block.id, name=block.name, arguments=dict(block.input))
                )
        return LLMResponse(
            text=text, tool_calls=tool_calls,
            provider_content={"backend": self.name, "model": self.model,
                              "blocks": blocks},
        )

    def _flush_usage(self) -> None:
        if self.usage_path is not None:
            self.usage_path.write_text(json.dumps(self.usage_summary(), indent=1))

    # -- wire format ---------------------------------------------------------
    def _to_wire_messages(self, messages: list[dict]) -> list[dict]:
        """Neutral -> Anthropic messages. Consecutive tool results are merged
        into one user turn (the API's contract for parallel tool calls)."""
        out: list[dict] = []
        for m in messages:
            wire = self._to_wire(m)
            if (m["role"] == "tool" and out and out[-1]["role"] == "user"
                    and isinstance(out[-1]["content"], list)
                    and all(b.get("type") == "tool_result" for b in out[-1]["content"])):
                out[-1]["content"].extend(wire["content"])
            else:
                out.append(wire)
        return out

    def _to_wire(self, m: dict) -> dict:
        if m["role"] == "tool":
            return {
                "role": "user",
                "content": [
                    {
                        "type": "tool_result",
                        "tool_use_id": m["tool_call_id"],
                        "content": m["content"],
                    }
                ],
            }
        if m["role"] == "assistant":
            pc = m.get("provider_content")
            if pc and pc.get("backend") == self.name and pc.get("model") == self.model:
                # verbatim replay: thinking blocks must come back unchanged
                return {"role": "assistant", "content": [dict(b) for b in pc["blocks"]]}
            if m.get("tool_calls"):
                content = []
                if m.get("content"):
                    content.append({"type": "text", "text": m["content"]})
                for tc in m["tool_calls"]:
                    content.append(
                        {
                            "type": "tool_use",
                            "id": tc["id"],
                            "name": tc["name"],
                            "input": tc["arguments"],
                        }
                    )
                return {"role": "assistant", "content": content}
        return {"role": m["role"], "content": m["content"]}


def _block_to_dict(block: object) -> dict:
    """SDK content block -> request-shaped dict, dropping null fields."""
    if hasattr(block, "model_dump"):
        return block.model_dump(exclude_none=True)
    return dict(block)  # already a dict (tests)
