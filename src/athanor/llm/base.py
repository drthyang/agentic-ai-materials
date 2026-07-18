"""Neutral LLM interface.

Messages use a provider-agnostic dict format; each backend translates to its
wire format. Neutral message shapes:

    {"role": "user" | "assistant", "content": str}
    {"role": "assistant", "content": str, "tool_calls": [ToolCall-as-dict]}
    {"role": "tool", "tool_call_id": str, "name": str, "content": str}
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass
class ToolSpec:
    """A tool description the model sees. input_schema is standard JSON Schema."""

    name: str
    description: str
    input_schema: dict


@dataclass
class ToolCall:
    id: str
    name: str
    arguments: dict
    # Set when the model emitted unparseable arguments; the loop returns this
    # to the model as an error instead of executing anything.
    parse_error: str | None = None

    def as_dict(self) -> dict:
        return {"id": self.id, "name": self.name, "arguments": self.arguments}


@dataclass
class LLMResponse:
    text: str = ""
    tool_calls: list[ToolCall] = field(default_factory=list)


class LLMBackend(ABC):
    """One chat turn: system prompt + neutral messages + tools -> response."""

    name: str = "abstract"

    @abstractmethod
    def chat(
        self,
        system: str,
        messages: list[dict],
        tools: list[ToolSpec],
    ) -> LLMResponse: ...
