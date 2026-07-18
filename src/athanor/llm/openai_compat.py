"""OpenAI-compatible chat backend — covers Ollama, LM Studio, vLLM, etc.

Talks to POST {base_url}/chat/completions with httpx (already a transitive
dependency). Local models emit malformed tool arguments occasionally; parse
failures are captured on the ToolCall rather than raised, so the loop can
bounce the error back to the model for a retry.
"""

from __future__ import annotations

import json
import logging
import time
import uuid

import httpx

from athanor.llm.base import LLMBackend, LLMResponse, ToolCall, ToolSpec

log = logging.getLogger("athanor.llm")


class OpenAICompatBackend(LLMBackend):
    name = "openai-compat"

    # transient failures are retried; a local model swapping in/out of memory
    # can stall well past a normal response time (learned from two dead
    # replicate campaigns on 2026-07-08)
    max_retries = 2
    retry_wait_s = 15.0

    def __init__(
        self,
        model: str,
        base_url: str = "http://localhost:11434/v1",
        api_key: str = "ollama",  # Ollama ignores it but the endpoint wants a header
        timeout_s: float = 600.0,
    ):
        self.model = model
        self.base_url = base_url.rstrip("/")
        self._client = httpx.Client(
            base_url=self.base_url,
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=timeout_s,
        )

    def chat(self, system: str, messages: list[dict], tools: list[ToolSpec]) -> LLMResponse:
        payload = {
            "model": self.model,
            "messages": [{"role": "system", "content": system}]
            + [self._to_wire(m) for m in messages],
        }
        if tools:
            payload["tools"] = [
                {
                    "type": "function",
                    "function": {
                        "name": t.name,
                        "description": t.description,
                        "parameters": t.input_schema,
                    },
                }
                for t in tools
            ]

        resp = self._post_with_retry(payload)
        resp.raise_for_status()
        msg = resp.json()["choices"][0]["message"]

        tool_calls = []
        for tc in msg.get("tool_calls") or []:
            call_id = tc.get("id") or f"call_{uuid.uuid4().hex[:8]}"
            fn = tc.get("function", {})
            raw_args = fn.get("arguments", "{}")
            try:
                args = json.loads(raw_args) if isinstance(raw_args, str) else raw_args
                if not isinstance(args, dict):
                    raise ValueError(f"arguments must be an object, got {type(args).__name__}")
                parse_error = None
            except (json.JSONDecodeError, ValueError) as exc:
                args, parse_error = {}, f"could not parse tool arguments: {exc}"
            tool_calls.append(
                ToolCall(id=call_id, name=fn.get("name", ""), arguments=args,
                         parse_error=parse_error)
            )

        return LLMResponse(text=msg.get("content") or "", tool_calls=tool_calls)

    def _post_with_retry(self, payload: dict) -> httpx.Response:
        last_exc: Exception | None = None
        for attempt in range(self.max_retries + 1):
            try:
                return self._client.post("/chat/completions", json=payload)
            except (httpx.TimeoutException, httpx.ConnectError) as exc:
                last_exc = exc
                if attempt < self.max_retries:
                    log.warning("LLM request failed (%s: %s); retry %d/%d in %.0fs",
                                type(exc).__name__, exc, attempt + 1,
                                self.max_retries, self.retry_wait_s)
                    time.sleep(self.retry_wait_s)
        raise last_exc

    @staticmethod
    def _to_wire(m: dict) -> dict:
        if m["role"] == "tool":
            return {
                "role": "tool",
                "tool_call_id": m["tool_call_id"],
                "content": m["content"],
            }
        if m["role"] == "assistant" and m.get("tool_calls"):
            return {
                "role": "assistant",
                "content": m.get("content") or "",
                "tool_calls": [
                    {
                        "id": tc["id"],
                        "type": "function",
                        "function": {
                            "name": tc["name"],
                            "arguments": json.dumps(tc["arguments"]),
                        },
                    }
                    for tc in m["tool_calls"]
                ],
            }
        return {"role": m["role"], "content": m["content"]}
