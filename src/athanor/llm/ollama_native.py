"""Ollama's native chat API, for the critic.

Ollama's OpenAI-compatible endpoint (/v1/chat/completions) cannot set the
context window, so a model loads with its default: for gemma4:26b that is
262,144 tokens. On 2026-10-12 that window, on a Mac also running an LM Studio
model, exhausted unified GPU memory; the runner broke and answered every
critic request with HTTP 200 in 15-37 ms and no usable content, and ten
campaigns ran without a critic. /api/chat takes ``options.num_ctx``, so the
model is loaded with a window sized for a review instead.

The window is fixed per backend rather than sized per prompt: Ollama reloads a
model whenever num_ctx changes, so a per-call size would reload it between
reviews. A prompt that would not fit is refused before it is sent.
"""

from __future__ import annotations

import logging
import time

import httpx

from athanor.llm.base import LLMBackend, LLMResponse, ToolSpec

log = logging.getLogger("athanor.llm")

# rough upper bound for chat text: at least 1 token per 3 characters
_CHARS_PER_TOKEN = 3
_REPLY_BUDGET_TOKENS = 2048


class PromptTooLong(ValueError):
    """The prompt would not fit in the configured context window."""


class OllamaNativeBackend(LLMBackend):
    name = "ollama"

    def __init__(
        self,
        model: str,
        base_url: str = "http://localhost:11434",
        num_ctx: int = 16384,
        timeout_s: float = 600.0,
        min_reply_seconds: float = 0.2,
        transport: httpx.BaseTransport | None = None,
    ):
        self.model = model
        # accept the OpenAI-style base URL the mission config carries
        self.base_url = base_url.rstrip("/").removesuffix("/v1")
        self.num_ctx = num_ctx
        # a 26B model cannot read a review prompt and write verdicts faster
        # than this; a quicker reply means a broken runner, not a review
        self.min_reply_seconds = min_reply_seconds
        self.last_latency_s: float | None = None
        self._client = httpx.Client(base_url=self.base_url, timeout=timeout_s,
                                    transport=transport)

    def chat(self, system: str, messages: list[dict], tools: list[ToolSpec]) -> LLMResponse:
        if tools:
            raise NotImplementedError("OllamaNativeBackend serves tool-free calls (the critic)")
        wire = [{"role": "system", "content": system}] + [
            {"role": m["role"], "content": m["content"]} for m in messages]
        est = sum(len(m["content"]) for m in wire) // _CHARS_PER_TOKEN + _REPLY_BUDGET_TOKENS
        if est > self.num_ctx:
            raise PromptTooLong(f"prompt needs ~{est} tokens; num_ctx is {self.num_ctx}")
        payload = {"model": self.model, "messages": wire, "stream": False,
                   "options": {"num_ctx": self.num_ctx}}
        t0 = time.monotonic()
        resp = self._client.post("/api/chat", json=payload)
        self.last_latency_s = time.monotonic() - t0
        resp.raise_for_status()
        body = resp.json()
        text = (body.get("message") or {}).get("content") or ""
        log.debug("ollama /api/chat %s: %.2fs, %d chars, done_reason=%s", self.model,
                  self.last_latency_s, len(text), body.get("done_reason"))
        return LLMResponse(text=text)
