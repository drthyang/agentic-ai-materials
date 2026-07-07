# matdiscover — agent onboarding

Closed-loop "AI materials scientist." Read PLAN.md for the full build plan.
Status: Phases 0–1 complete (scaffold + deterministic tool layer, verified).
**Next: Phase 2** — wire tools into a Claude-driven hypothesize→propose→screen→
reflect loop (`matdiscover run --iterations N`), per PLAN.md.

## Commands

```bash
uv run pytest                              # 19 tests, all should pass
uv run matdiscover check                   # env/key status
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
