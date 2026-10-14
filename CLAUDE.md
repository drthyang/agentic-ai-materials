# Athanor — agent onboarding

Closed-loop "AI materials scientist." Read PLAN.md for the full build plan.
Status: Phases 0–4 complete (tool layer; agent loop with pluggable LLM
backend, local-first via Ollama/qwen3:32b; baselines + metrics + benchmark;
critic + literature tool + live dashboard).
**Remaining:** ROADMAP.md is the source of truth for next steps (benchmark
matrix, rediscovery run, mission gallery in config/missions/, then
magnetism/active-learning, then new-surrogate work).

## Commands

```bash
uv run pytest                              # 155 tests, all should pass
uv run athanor check                   # env/key status
uv run athanor run --iterations 1      # discovery campaign (needs Ollama up)
uv run athanor benchmark --skip-agent  # baselines only (no LLM needed)
uv run athanor benchmark               # full agent-vs-baselines comparison
uv run python scripts/smoke_pipeline.py    # end-to-end pipeline, no agent
uv run athanor dashboard               # live view at localhost:8517
uv run athanor export-pages            # static recorded-campaign site -> docs/
```

## Phase 4 (critic, literature, dashboard)

- `agent/critic.py` — independent reviewer with skeptical persona, fresh
  context per review. Gates evaluate_candidates INSIDE the tool: vetoes cost
  zero relaxation budget, recorded as filtered_out rows. Fails OPEN (parse
  failure/exception => approve all): a flaky critic may only save compute,
  never block science. Disabled via critic.enabled in mission.yaml; tests in
  test_agent.py disable it to keep scripted backends exact.
- `tools/literature.py` — Crossref search (free, no key), disk-cached in
  data/lit_cache/; registered as search_literature agent tool.
- `dashboard.py` — "Mission Control": stdlib http.server serving a static
  shell (`src/athanor/web/` — vanilla JS + CSS in the MATERIA workbench
  design language, IBM Plex bundled) plus `/api/snapshot` and
  `/api/benchmark` JSON read fresh per request from DB + notebook + mission
  config. Client renders the discovery-loop funnel, SVG gap-vs-hull map,
  event feed, top candidates, and notebook; auto-refresh 10s. Read-only by
  design (config-over-code applies to the UI) and still zero new
  dependencies — no node, no build step. Hit/rediscovery flags come from
  `metrics.row_flags`, the single source of the hit rule.

## Architecture

- `src/athanor/tools/` — deterministic tools the agent will call:
  `candidates.py` (prototype substitution), `filters.py` (SMACT + mission
  chemistry, run BEFORE any compute), `mp_search.py` (Materials Project +
  novelty, disk-cached in data/mp_cache/), `scoring.py` (CHGNet relax →
  formation energy → hull; MEGNet band gap)
- `src/athanor/db.py` — SQLite record of every candidate; `notebook.py` —
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
- Anthropic backend: assistant turns carry `provider_content` (raw blocks,
  thinking included) that is replayed verbatim — Claude requires it before
  tool results; tools+system and the turn tail are prompt-cached; usage is
  priced per call and `llm.max_cost_usd` is a hard stop. Missions pin
  `critic.backend: ollama`, and the loop refuses a non-Claude critic model
  on the anthropic backend (it would 404 and fail open silently).
- Ablation arms are benchmark flags, not mission edits (`--backend/--model/
  --effort`, `--no-surrogate`, `--no-critic`, `--baselines none`, `--tag`,
  `--ledger/--spend-cap-usd`); each run dir records run_config.json,
  metrics.json, agent_stats.json, usage.json. Aggregate with
  `scripts/aggregate_ablation.py <spec.json>`.

## Phase 3 (benchmark & evaluation)

- `baselines.py` — random + greedy-similarity + BayesOpt searchers; identical
  budget, filters, scorer, and DB schema as the agent. Only candidate choice
  differs. The BO machinery (GP, `featurize_composition`, `mission_utility`)
  is also the agent's `rank_by_surrogate` tool — keep them shared, or the
  LLM-vs-LLM+BO comparison stops being controlled. Toggle via `acquisition:`
  in mission.yaml. Each baseline has a `-novel` variant (`--baselines
  random-novel,similarity-novel,bayesopt-novel`) that skips Materials
  Project compositions before relaxing, as the agent is told to; the
  originals relax known compositions too. Only the original three run by
  default, so past commands reproduce.
- `metrics.py` — shared hit definition (converged + on-target gap + near-hull +
  not confirmed-known); `benchmark.py` orchestrates same-relaxation-cap comparison into
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
- Prototypes are conventional cells built from their space groups
  (chalcopyrite I-42d and kesterite I-4 at 16 atoms, zinc blende F-43m at
  8). Before 2026-10-12 the first two were 8-atom P2 half-cells with a ~7 Å
  empty slab and most benchmark hits depended on it;
  `tests/test_prototypes.py` pins space group, stoichiometry, tetrahedral
  coordination and the absence of vacuum. Runs record `prototype_cells` in
  run_config.json.
- pymatgen's `reduced_formula` ordering is canonical-but-surprising
  (e.g. "GaCuSe2"); compare `Composition` objects, not strings.

## Conventions

- Naming: the project is **Athanor** (renamed from matdiscover 2026-07).
  Keep the "formerly matdiscover" notes in README/WALKTHROUGH and the
  `matdiscover` CLI alias — external references still cite the old name; do
  not purge them until the user says those references are updated. Do not rename
  the GitHub repo without asking, for the same reason.
- uv + Python 3.11 (pinned); `uv sync --extra dev` to set up
- Commit style: imperative subject, body explains the "why". No trailers.
- Attribution: every commit in this repo is authored solely by
  `Tsung-Han Yang <tsung-han_yang@alumni.brown.edu>` — no `Co-Authored-By`,
  no `Claude-Session`. `.claude/settings.json` enforces this two ways:
  `attribution` blanks the trailers, and a `SessionStart` hook sets the
  repo-local git identity (`.git/config` is not checked in, so a fresh
  clone or container would otherwise fall back to whatever the environment
  defaults to). Do not re-add the trailers.
