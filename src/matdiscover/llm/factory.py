"""Backend selection from mission config."""

from __future__ import annotations

from matdiscover.config import LLMConfig
from matdiscover.llm.base import LLMBackend


def make_backend(cfg: LLMConfig) -> LLMBackend:
    if cfg.backend in ("ollama", "openai-compat"):
        from matdiscover.llm.openai_compat import OpenAICompatBackend

        return OpenAICompatBackend(
            model=cfg.model, base_url=cfg.base_url, timeout_s=cfg.timeout_s
        )
    if cfg.backend == "anthropic":
        from matdiscover.llm.anthropic_backend import AnthropicBackend

        return AnthropicBackend(model=cfg.model)
    raise ValueError(f"unknown llm backend: {cfg.backend!r} "
                     "(expected 'ollama', 'openai-compat', or 'anthropic')")
