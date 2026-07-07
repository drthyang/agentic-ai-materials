"""OpenAI-compatible chat backend — covers Ollama, LM Studio, vLLM, etc.

Talks to POST {base_url}/chat/completions with httpx (already a transitive
dependency). Local models emit malformed tool arguments occasionally; parse
failures are captured on the ToolCall rather than raised, so the loop can
bounce the error back to the model for a retry.
"""

from __future__ import annotations

import json
import uuid

import httpx

from matdiscover.llm.base import LLMBackend, LLMResponse, ToolCall, ToolSpec


class OpenAICompatBackend(LLMBackend):
    name = "openai-compat"

    def __init__(
        self,
        model: str,
        base_url: str = "http://localhost:11434/v1",
        api_key: str = "ollama",  # Ollama ignores it but the endpoint wants a header
        timeout_s: float = 300.0,
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

        resp = self._client.post("/chat/completions", json=payload)
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
