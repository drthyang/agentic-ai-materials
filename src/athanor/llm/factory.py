"""Backend selection from mission config."""

from __future__ import annotations

from athanor.config import CriticConfig, LLMConfig
from athanor.llm.base import LLMBackend


def make_backend(cfg: LLMConfig, critic: CriticConfig | None = None) -> LLMBackend:
    """The backend for one role. Pass ``critic`` when building the critic: an
    Ollama critic then talks to /api/chat with a bounded context window (see
    ollama_native.py) instead of the OpenAI-compatible endpoint."""
    if critic is not None and cfg.backend == "ollama":
        from athanor.llm.ollama_native import OllamaNativeBackend

        return OllamaNativeBackend(
            model=cfg.model, base_url=cfg.base_url, num_ctx=critic.num_ctx,
            timeout_s=cfg.timeout_s, min_reply_seconds=critic.min_reply_seconds)
    if cfg.backend in ("ollama", "openai-compat"):
        from athanor.llm.openai_compat import OpenAICompatBackend

        return OpenAICompatBackend(
            model=cfg.model, base_url=cfg.base_url, timeout_s=cfg.timeout_s
        )
    if cfg.backend == "anthropic":
        from athanor.llm.anthropic_backend import AnthropicBackend

        return AnthropicBackend(model=cfg.model, effort=cfg.effort,
                                max_cost_usd=cfg.max_cost_usd)
    raise ValueError(f"unknown llm backend: {cfg.backend!r} "
                     "(expected 'ollama', 'openai-compat', or 'anthropic')")
