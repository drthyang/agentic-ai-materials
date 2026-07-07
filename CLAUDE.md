# matdiscover — agent onboarding

Closed-loop "AI materials scientist." Read PLAN.md for the full build plan.
Status: Phases 0–3 complete (tool layer; agent loop with pluggable LLM
backend, local-first via Ollama/qwen3:32b; baselines + metrics + benchmark).
**Next: Phase 4** — critic agent, literature agent, dashboard, per PLAN.md.

## Commands

```bash
uv run pytest                              # 39 tests, all should pass
uv run matdiscover check                   # env/key status
uv run matdiscover run --iterations 1      # discovery campaign (needs Ollama up)
uv run matdiscover benchmark --skip-agent  # baselines only (no LLM needed)
uv run matdiscover benchmark               # full agent-vs-baselines comparison
uv run python scripts/smoke_pipeline.py    # end-to-end pipeline, no agent
```

## Architecture

- `src/matdiscover/tools/` — deterministic tools the agent will call:
  `candidates.py` (prototype substitution), `filters.py` (SMACT + mission
  chemistry, run BEFORE any compute), `mp_search.py` (Materials Project +
  novelty, disk-cached in data/mp_cache/), `scoring.py` (CHGNet relax →
  formation energy → hull; MEGNet band gap)
- `src/matdiscover/db.py` — SQLite record of every candidate; `notebook.py` —
  append-only markdown lab notebook (the agent's cross-iteration memory)
- `config/mission.yaml` — the mission (target windows, element palette,
  compute budgets). Change missions here, never in code.

## Phase 2 architecture (agent loop)

- `llm/` — provider-agnostic backend (`base.py` neutral messages, `openai_compat.py`
  for Ollama/LM Studio/vLLM, `anthropic_backend.py`, `factory.py`). Selected via
  `llm:` in mission.yaml. Default: `ollama` + `qwen3:32b` (user has 64 GB RAM).
- `agent/` — `registry.py` (schema validation, errors returned to the model, never
  raised), `tools.py` (agent-facing tools over the Phase 1 layer; propose fuses
  generate+filter+novelty; evaluate enforces the relaxation budget in code),
  `prompts.py`, `loop.py`.
- Context strategy: each iteration starts a FRESH message list; cross-iteration
  memory is the lab notebook (via read_notebook tool). Keeps prompts small for
  local models and makes the notebook the scientific record.
- Local-model robustness: malformed tool JSON is captured as ToolCall.parse_error
  and bounced back for retry; tool-call budget terminates runaway iterations.

## Phase 3 (benchmark & evaluation)

- `baselines.py` — random + greedy-similarity searchers; identical budget,
  filters, scorer, and DB schema as the agent. Only substitution choice differs.
- `metrics.py` — shared hit definition (converged + on-target gap + near-hull +
  not confirmed-known); `benchmark.py` orchestrates equal-budget comparison into
  data/benchmark/<stamp>/ with markdown table + png plot.
- Rediscovery hold-out: `evaluation.holdout_formulas` in mission.yaml masks
  known materials from MP search + novelty (compared via reduced formula), so
  campaigns can "rediscover" them; metrics count rediscoveries.

## Non-obvious decisions (don't re-derive)

- Band gaps: use **HSE fidelity** (`predict_band_gap` default). PBE fidelity
  collapses chalcogenide gaps to ~0. Fidelity indices verified against Si.
- `MP_API_KEY` unset ⇒ novelty/hull checks skip gracefully and elemental
  references fall back to crude FCC cells (absolute E_form offset; rankings
  still usable). Full pipeline needs the key (free, materialsproject.org/api).
- CHGNet runs on Apple MPS; relaxations are the compute cost driver — respect
  `budget.max_relaxations_per_iteration` from mission.yaml in any agent loop.
- Scoring must never crash a campaign: `relax_and_score` returns a
  `ScoreResult` with `.error` set instead of raising.
- pymatgen's `reduced_formula` ordering is canonical-but-surprising
  (e.g. "GaCuSe2"); compare `Composition` objects, not strings.

## Conventions

- uv + Python 3.11 (pinned); `uv sync --extra dev` to set up
- Commit style: imperative subject, body explains the "why",
  `Co-Authored-By: Claude <noreply@anthropic.com>` trailer
