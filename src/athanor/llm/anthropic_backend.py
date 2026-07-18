"""Anthropic backend for the campaign loop.

Secondary to the local backend for now; enables the Claude-vs-local
comparison experiment by flipping `llm.backend` in mission.yaml.
"""

from __future__ import annotations

from athanor.llm.base import LLMBackend, LLMResponse, ToolCall, ToolSpec


class AnthropicBackend(LLMBackend):
    name = "anthropic"

    def __init__(self, model: str = "claude-sonnet-5", max_tokens: int = 16000):
        import anthropic

        self.model = model
        self.max_tokens = max_tokens
        self._client = anthropic.Anthropic()

    def chat(self, system: str, messages: list[dict], tools: list[ToolSpec]) -> LLMResponse:
        response = self._client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            system=system,
            messages=[self._to_wire(m) for m in messages],
            tools=[
                {
                    "name": t.name,
                    "description": t.description,
                    "input_schema": t.input_schema,
                }
                for t in tools
            ],
        )
        text = ""
        tool_calls = []
        for block in response.content:
            if block.type == "text":
                text += block.text
            elif block.type == "tool_use":
                tool_calls.append(
                    ToolCall(id=block.id, name=block.name, arguments=dict(block.input))
                )
        return LLMResponse(text=text, tool_calls=tool_calls)

    @staticmethod
    def _to_wire(m: dict) -> dict:
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
        if m["role"] == "assistant" and m.get("tool_calls"):
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
