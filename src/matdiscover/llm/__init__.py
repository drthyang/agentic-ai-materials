"""LLM backend abstraction: one neutral interface, pluggable providers."""

from matdiscover.llm.base import LLMBackend, LLMResponse, ToolCall, ToolSpec
from matdiscover.llm.factory import make_backend

__all__ = ["LLMBackend", "LLMResponse", "ToolCall", "ToolSpec", "make_backend"]
