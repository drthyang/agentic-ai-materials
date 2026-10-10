"""Anthropic backend + spend controls — hermetic: a fake client plays the API.

Covers what the Claude ablation arms depend on: verbatim replay of thinking
blocks, one user turn for parallel tool results, prompt-cache breakpoints,
usage pricing, the hard spend stop, the run ledger, and the critic guard.
"""

from __future__ import annotations

import csv
import json
from types import SimpleNamespace

import pytest

from athanor.agent.critic import Critic
from athanor.agent.loop import _run_agent_turn, run_campaign
from athanor.agent.registry import ToolRegistry
from athanor.config import load_mission
from athanor.llm.anthropic_backend import (
    AnthropicBackend,
    SpendCapExceeded,
    UsageTotals,
    price_for,
)
from athanor.llm.base import LLMBackend, LLMResponse, ToolSpec


class FakeBlock(SimpleNamespace):
    def model_dump(self, exclude_none: bool = False) -> dict:
        d = dict(vars(self))
        return {k: v for k, v in d.items() if not (exclude_none and v is None)}


def _usage(inp=100, out=50, read=0, write=0):
    return SimpleNamespace(input_tokens=inp, output_tokens=out,
                           cache_read_input_tokens=read,
                           cache_creation_input_tokens=write)


class FakeMessages:
    def __init__(self, responses):
        self.responses = list(responses)
        self.requests: list[dict] = []

    def create(self, **kwargs):
        self.requests.append(json.loads(json.dumps(kwargs)))  # deep, wire-shaped copy
        return self.responses.pop(0)


def _client(responses):
    return SimpleNamespace(messages=FakeMessages(responses))


def _tool_use_response(*calls, usage=None):
    blocks = [FakeBlock(type="thinking", thinking="", signature="sig-abc")]
    for i, (name, args) in enumerate(calls):
        blocks.append(FakeBlock(type="tool_use", id=f"tu{i}", name=name, input=args,
                                caller=None))
    return SimpleNamespace(content=blocks, usage=usage or _usage(),
                           stop_reason="tool_use")


def _text_response(text, usage=None):
    return SimpleNamespace(content=[FakeBlock(type="text", text=text, citations=None)],
                           usage=usage or _usage(), stop_reason="end_turn")


TOOLS = [ToolSpec("read_notebook", "read it", {"type": "object", "properties": {}})]


# --------------------------------------------------------------------------
# request shape
# --------------------------------------------------------------------------

def test_request_sets_cache_breakpoints_and_effort():
    client = _client([_text_response("hi")])
    be = AnthropicBackend(model="claude-sonnet-5-5", effort="medium", client=client)
    be.chat("SYSTEM", [{"role": "user", "content": "go"}], TOOLS)
    req = client.messages.requests[0]
    assert req["system"] == [{"type": "text", "text": "SYSTEM",
                              "cache_control": {"type": "ephemeral"}}]
    assert req["cache_control"] == {"type": "ephemeral"}
    assert req["output_config"] == {"effort": "medium"}
    assert req["tools"][0]["name"] == "read_notebook"


def test_no_effort_or_tools_keys_when_unset():
    client = _client([_text_response("ok")])
    be = AnthropicBackend(model="claude-sonnet-5-5", client=client)
    be.chat("S", [{"role": "user", "content": "x"}], tools=[])
    req = client.messages.requests[0]
    assert "output_config" not in req and "tools" not in req


def test_thinking_blocks_replayed_verbatim_and_tool_results_merged():
    client = _client([
        _tool_use_response(("read_notebook", {}), ("get_top_candidates", {"limit": 3})),
        _text_response("summary"),
    ])
    be = AnthropicBackend(model="claude-sonnet-5-5", client=client)
    first = be.chat("S", [{"role": "user", "content": "go"}], TOOLS)
    assert [tc.name for tc in first.tool_calls] == ["read_notebook", "get_top_candidates"]
    assert first.provider_content["blocks"][0]["type"] == "thinking"

    history = [
        {"role": "user", "content": "go"},
        {"role": "assistant", "content": first.text,
         "tool_calls": [tc.as_dict() for tc in first.tool_calls],
         "provider_content": first.provider_content},
        {"role": "tool", "tool_call_id": "tu0", "name": "read_notebook", "content": "{}"},
        {"role": "tool", "tool_call_id": "tu1", "name": "get_top_candidates",
         "content": "[]"},
    ]
    be.chat("S", history, TOOLS)
    msgs = client.messages.requests[1]["messages"]
    assert [m["role"] for m in msgs] == ["user", "assistant", "user"]
    # assistant turn goes back exactly as received, thinking signature intact,
    # null fields dropped
    assert msgs[1]["content"][0] == {"type": "thinking", "thinking": "",
                                     "signature": "sig-abc"}
    assert "caller" not in msgs[1]["content"][1]
    # both parallel results in ONE user turn
    assert [b["tool_use_id"] for b in msgs[2]["content"]] == ["tu0", "tu1"]


def test_foreign_provider_content_is_not_replayed():
    be = AnthropicBackend(model="claude-sonnet-5-5", client=_client([]))
    m = {"role": "assistant", "content": "t",
         "tool_calls": [{"id": "c1", "name": "f", "arguments": {}}],
         "provider_content": {"backend": "anthropic", "model": "claude-opus-5-5",
                              "blocks": [{"type": "thinking", "signature": "x"}]}}
    wire = be._to_wire(m)
    assert [b["type"] for b in wire["content"]] == ["text", "tool_use"]


# --------------------------------------------------------------------------
# spend accounting
# --------------------------------------------------------------------------

def test_usage_pricing_sonnet():
    u = UsageTotals()
    u.add(_usage(inp=1_000_000, out=1_000_000, read=1_000_000, write=1_000_000),
          "end_turn")
    # 2 input + 10 output + 0.20 cache read + 2.50 cache write
    assert u.cost_usd("claude-sonnet-5-5") == pytest.approx(14.70)
    assert u.stop_reasons == {"end_turn": 1}


def test_unknown_model_priced_at_highest_known_rate():
    assert price_for("claude-mystery-9") == price_for("claude-opus-5-5")


def test_spend_cap_stops_before_the_next_request(tmp_path):
    expensive = _usage(inp=0, out=200_000)  # $2.00 on Sonnet
    client = _client([_text_response("a", expensive), _text_response("b")])
    be = AnthropicBackend(model="claude-sonnet-5-5", max_cost_usd=1.0, client=client)
    be.usage_path = tmp_path / "usage.json"
    be.chat("S", [{"role": "user", "content": "x"}], TOOLS)
    with pytest.raises(SpendCapExceeded):
        be.chat("S", [{"role": "user", "content": "y"}], TOOLS)
    assert len(client.messages.requests) == 1  # the capped call never went out
    flushed = json.loads(be.usage_path.read_text())
    assert flushed["calls"] == 1 and flushed["cost_usd"] == pytest.approx(2.0)


def test_loop_replays_provider_content_and_counts_tools():
    client = _client([
        _tool_use_response(("read_notebook", {})),
        _text_response("done"),
    ])
    be = AnthropicBackend(model="claude-sonnet-5-5", client=client)
    reg = ToolRegistry()
    reg.register(TOOLS[0], lambda: {"notebook": ""})
    stats: dict = {}
    out = _run_agent_turn(be, reg, kickoff="go", max_tool_calls=5, stats=stats)
    assert out == "done"
    assert stats["tool_calls"] == {"read_notebook": 1}
    replayed = client.messages.requests[1]["messages"][1]["content"]
    assert replayed[0]["type"] == "thinking"


# --------------------------------------------------------------------------
# critic wiring
# --------------------------------------------------------------------------

@pytest.fixture
def cfg(tmp_path, monkeypatch):
    monkeypatch.delenv("MP_API_KEY", raising=False)
    c = load_mission("config/mission.yaml")
    c.paths.db = tmp_path / "c.db"
    c.paths.notebook = tmp_path / "nb.md"
    c.paths.reports = tmp_path / "reports"
    return c


def test_mission_pins_the_critic_to_the_local_backend(cfg):
    assert cfg.critic.backend == "ollama"


def test_critic_on_anthropic_with_a_local_model_name_fails_loudly(cfg):
    cfg.llm.backend = "anthropic"
    cfg.critic.backend = None  # the old default: inherit the proposer's backend
    cfg.critic.model = "gemma4:26b"

    class Never(LLMBackend):
        def chat(self, system, messages, tools):
            raise AssertionError("should not get this far")

    with pytest.raises(ValueError, match="critic.backend"):
        run_campaign(cfg, Never(), iterations=1)


def test_critic_counts_fail_open_reviews(cfg):
    class Broken(LLMBackend):
        def chat(self, system, messages, tools):
            raise ConnectionError("down")

    class Vetoer(LLMBackend):
        def chat(self, system, messages, tools):
            return LLMResponse(text=json.dumps({"verdicts": [
                {"formula": "CuInSe2", "approve": False, "reason": "known"}]}))

    batch = [{"formula": "CuInSe2", "substitution": {}},
             {"formula": "AgInSe2", "substitution": {}}]
    broken = Critic(Broken(), cfg)
    broken.review(batch, "h")
    assert broken.stats["failed_open"] == 1 and broken.stats["approved"] == 2

    vet = Critic(Vetoer(), cfg)
    vet.review(batch, "h")
    assert vet.stats == {"reviews": 1, "candidates": 2, "approved": 1,
                         "vetoed": 1, "failed_open": 0}


# --------------------------------------------------------------------------
# benchmark plumbing: arm overrides, baseline selection, ledger, spend cap
# --------------------------------------------------------------------------

def test_arm_overrides_and_baseline_parsing(cfg):
    from athanor.cli import _parse_baselines, apply_arm_overrides

    args = SimpleNamespace(backend="anthropic", model="claude-sonnet-5-5",
                           effort="medium", max_cost_usd=3.0, critic_backend=None,
                           critic_model=None, no_critic=False, no_surrogate=True)
    apply_arm_overrides(cfg, args)
    assert (cfg.llm.backend, cfg.llm.model, cfg.llm.effort) == (
        "anthropic", "claude-sonnet-5-5", "medium")
    assert cfg.llm.max_cost_usd == 3.0
    assert cfg.acquisition.enabled is False and cfg.critic.enabled is True
    assert cfg.critic.backend == "ollama"  # untouched
    assert _parse_baselines(None) is None
    assert _parse_baselines("none") == []
    assert _parse_baselines("bayesopt") == ["bayesopt"]


def test_ledger_roundtrip(tmp_path):
    from athanor.benchmark import append_ledger, ledger_total_usd

    path = tmp_path / "ledger.csv"
    assert ledger_total_usd(path) == 0.0
    usage = {"backend": "anthropic", "model": "claude-sonnet-5-5", "effort": None,
             "calls": 3, "input_tokens": 10, "cache_creation_input_tokens": 5,
             "cache_read_input_tokens": 7, "output_tokens": 2, "cost_usd": 1.25}
    append_ledger(path, tmp_path / "run1", "pv", usage, "ok")
    append_ledger(path, tmp_path / "run2", "pv", {**usage, "cost_usd": 0.5}, "ok")
    assert ledger_total_usd(path) == pytest.approx(1.75)
    rows = list(csv.DictReader(open(path)))
    assert rows[0]["status"] == "ok" and rows[1]["run_dir"].endswith("run2")
    assert "key" not in open(path).read().lower()


def test_benchmark_refuses_to_start_past_the_spend_cap(cfg, tmp_path, monkeypatch):
    from athanor.benchmark import append_ledger, run_benchmark

    monkeypatch.chdir(tmp_path)
    ledger = tmp_path / "ledger.csv"
    append_ledger(ledger, tmp_path / "r", "pv", {"cost_usd": 39.8}, "ok")
    cfg.llm.backend = "anthropic"
    with pytest.raises(SystemExit, match="spend cap"):
        run_benchmark(cfg, iterations=1, baselines=[], ledger=ledger, spend_cap_usd=40)


def test_agent_only_benchmark_writes_artifacts(cfg, tmp_path, monkeypatch):
    from athanor.benchmark import run_benchmark

    monkeypatch.chdir(tmp_path)
    cfg.critic.enabled = False
    client = _client([_text_response("iteration summary"),
                      _text_response("# report")])
    be = AnthropicBackend(model="claude-sonnet-5-5", client=client)
    monkeypatch.setattr("athanor.llm.make_backend", lambda llm: be)
    cfg.llm.backend = "anthropic"
    ledger = tmp_path / "ledger.csv"
    outdir = run_benchmark(cfg, iterations=1, baselines=[], tag="arm",
                           ledger=ledger, spend_cap_usd=40)
    assert outdir.name.endswith("-seed0-arm")
    snap = json.loads((outdir / "run_config.json").read_text())
    assert snap["baselines"] == [] and snap["mission_config"]["llm"]["backend"] == "anthropic"
    assert json.loads((outdir / "usage.json").read_text())["calls"] == 2
    assert json.loads((outdir / "agent_stats.json").read_text())["aborted_turns"] == 0
    assert be.max_cost_usd == pytest.approx(40 - 0.5)
    assert len(list(csv.DictReader(open(ledger)))) == 1
    metrics = json.loads((outdir / "metrics.json").read_text())
    assert metrics[0]["name"].startswith("agent")
