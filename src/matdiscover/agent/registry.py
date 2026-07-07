"""Tool registry: schemas the model sees + safe dispatch of its calls.

Errors never raise out of `execute` — they return an error string the loop
feeds back to the model, so a local model that fumbles a call can retry.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Callable

from matdiscover.llm.base import ToolCall, ToolSpec


@dataclass
class ToolRegistry:
    _tools: dict[str, tuple[ToolSpec, Callable[..., dict]]] = field(default_factory=dict)

    def register(self, spec: ToolSpec, fn: Callable[..., dict]) -> None:
        self._tools[spec.name] = (spec, fn)

    @property
    def specs(self) -> list[ToolSpec]:
        return [spec for spec, _ in self._tools.values()]

    def execute(self, call: ToolCall) -> str:
        """Run one tool call; always returns a JSON string for the model."""
        if call.parse_error:
            return _err(call.parse_error + " — re-send the call with valid JSON arguments")
        if call.name not in self._tools:
            return _err(
                f"unknown tool {call.name!r}; available tools: {sorted(self._tools)}"
            )
        spec, fn = self._tools[call.name]

        required = spec.input_schema.get("required", [])
        missing = [k for k in required if k not in call.arguments]
        if missing:
            return _err(f"missing required arguments {missing} for tool {call.name!r}")
        allowed = set(spec.input_schema.get("properties", {}))
        unknown = [k for k in call.arguments if k not in allowed]
        if unknown:
            return _err(
                f"unknown arguments {unknown} for tool {call.name!r}; "
                f"valid arguments: {sorted(allowed)}"
            )

        try:
            result = fn(**call.arguments)
        except Exception as exc:  # tool bugs/bad values must not kill the campaign
            return _err(f"{type(exc).__name__}: {exc}")
        return json.dumps(result, default=str)


def _err(message: str) -> str:
    return json.dumps({"error": message})
