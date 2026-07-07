# matdiscover — Agentic AI for Materials Discovery

A closed-loop "AI materials scientist": an agent that proposes candidate
materials, screens them with physics-grounded surrogate models (CHGNet
relaxation, convex-hull stability, MEGNet band gaps), reflects on results in a
lab notebook, and iterates.

Default mission: find novel, near-stable semiconductor compositions with a band
gap near 1.4 eV (photovoltaic absorber candidates). Missions are configured in
[config/mission.yaml](config/mission.yaml) — see [PLAN.md](PLAN.md) for the full
build plan.

## Setup

```bash
uv sync --extra dev
export MP_API_KEY=...        # free key from https://materialsproject.org/api
export ANTHROPIC_API_KEY=... # for the agent loop (Phase 2+)
```

## Usage

```bash
# Run a discovery campaign (default: local qwen3:32b via Ollama)
uv run matdiscover run --iterations 3

# Use Claude instead of a local model
uv run matdiscover run --backend anthropic --model claude-sonnet-5

# Phase 1 pipeline without any agent (sanity check)
uv run python scripts/smoke_pipeline.py

# Run tests
uv run pytest
```

The LLM backend is pluggable (`llm:` section in mission.yaml): `ollama` /
`openai-compat` for local models, `anthropic` for Claude. The architecture is
identical either way — the agent's memory is the lab notebook, its actions are
the physics tools, and all budgets are enforced in code.

## Layout

- `src/matdiscover/tools/` — deterministic tool layer (MP search, candidate
  generation, SMACT filters, CHGNet/MEGNet scoring)
- `src/matdiscover/db.py`, `notebook.py` — campaign persistence
- `config/mission.yaml` — the discovery mission (target, chemistry, budget)
- `scripts/` — standalone pipeline scripts
