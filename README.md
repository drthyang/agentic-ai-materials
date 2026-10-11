# Athanor — Agentic AI for Materials Discovery

> An *athanor* is the alchemists' furnace: built to sustain a slow
> transmutation, self-feeding, running unattended. This one has a skeptic
> inside.

*Formerly published as **matdiscover** — the name some external links
still use. Same project, renamed 2026-07; the `matdiscover` CLI command
still works.*

A closed-loop **"AI materials scientist"**. A tool-calling LLM agent states
a chemical hypothesis, proposes a family of candidate materials, lets an
independent critic model veto weak ones before any compute is spent,
screens the survivors with physics-grounded surrogates, records what it
learned in a lab notebook, and iterates, then writes its report from
ground-truth data. Runs **entirely on local models** (Ollama) by default;
Claude is one flag away (`--backend anthropic`).

```
mission config ──▶ [LLM hypothesizes] ──▶ propose ──▶ filter (SMACT, palette)
                        ▲                                    │
                        │       rank_by_surrogate ◀──────────┤ (GP + EI, free)
                        │                          critic review (2nd LLM)
                   lab notebook                              │
                   + SQLite DB  ◀── evaluate: CHGNet relax ──▶ formation energy
                        ▲                  │                  energy above hull
                        │                  └────────────────▶ band gap (MEGNet)
                   [LLM reflects] ◀───────── results ◀───────┘
```

**What the agent works with**

- **A tool-calling proposer with eight tools.** `read_notebook` /
  `write_notebook` (its memory across iterations), `search_literature`
  (Crossref), `search_known_materials` (Materials Project),
  `propose_candidates` (prototype substitution, then charge-balance,
  palette and novelty checks), `evaluate_candidates` (the physics),
  `rank_by_surrogate` and `get_top_candidates`. Budgets live in the tool
  code, so the model cannot talk its way past them.
- **An independent critic.** A second model from a different family
  (default `gemma4:26b`) reviews every batch in a fresh context before it
  is relaxed. Vetoes cost nothing and are recorded with reasons; a broken
  critic fails open, so it can save compute but never block a run.
- **`rank_by_surrogate`.** The Bayesian-optimisation baseline's Gaussian
  process and expected-improvement acquisition, exposed to the agent as a
  free, advisory tool: same features, same utility, so "LLM" vs "LLM + BO"
  is a controlled comparison.
- **Physics-grounded surrogates.** CHGNet structure relaxation and
  formation energy, energy above the Materials Project convex hull, and
  MEGNet band gaps at HSE fidelity, on Apple-GPU.

Why it's interesting: the agent's "experiments" are real physics (ML
interatomic potentials, convex-hull thermodynamics), success is objectively
measurable, and every campaign is benchmarked against **non-LLM baselines under
the same relaxation cap**, so "the agent helps" is a claim with a control group.
That cap equalizes CHGNet relaxations only; it is not matched total compute.
The proposer and critic LLMs' inference cost is not counted, and an agent
may spend less than the cap, so results report both hits per run and hits
per 100 relaxations.

**New here (or catching up)? Read [WALKTHROUGH.md](WALKTHROUGH.md)** — the
whole machine and every experiment so far, in order, in ~15 minutes.

## Quickstart

```bash
uv sync --extra dev
export MP_API_KEY=...        # free key: materialsproject.org/api (or put in .env)
ollama pull qwen3:32b        # the default local scientist (needs ~20 GB RAM)

uv run athanor check                   # verify environment
uv run athanor run --iterations 3     # run a discovery campaign
uv run athanor dashboard               # watch it live at localhost:8517
uv run athanor benchmark               # agent vs random / similarity / BO
uv run athanor export-pages            # bake a static Mission Control into docs/
```

`export-pages` writes a self-contained recorded-campaign site (the same
Mission Control UI, clearly labeled as a recording) that GitHub Pages can
serve from the `docs/` folder — nothing live, nothing local leaks; you
choose which campaign DB to publish (`--latest`, `--db`).

## Missions

The science target is pure config — swap missions without touching code:

| Mission | Target | File |
|---|---|---|
| PV absorber *(default)* | gap 1.1–1.7 eV, near-stable | [config/mission.yaml](config/mission.yaml) |
| QD display emitter | visible gap, **no Cd/Pb/Hg** | [config/missions/qd-emitter.yaml](config/missions/qd-emitter.yaml) |
| Transparent conductor | gap ≥ 3.1 eV oxides (see caveats in file) | [config/missions/tco.yaml](config/missions/tco.yaml) |

Activate one: `cp config/missions/qd-emitter.yaml config/mission.yaml`

## The cast

- **Proposer** — any tool-calling LLM (default `qwen3:32b` via Ollama;
  `--backend anthropic` for Claude, with prompt caching, verbatim replay
  of thinking blocks, and a per-run spend stop plus CSV ledger).
  Hypothesizes, proposes substitutions on known prototypes, decides what's
  worth evaluating.
- **Critic** — an independent second model (default `gemma4:26b`) that
  reviews every batch *before* compute is spent. Vetoes cost zero budget and
  are recorded with reasons. Fails open: a flaky critic can only save
  compute, never block science.
- **The lab** — deterministic Python tools: SMACT charge-balance filters,
  CHGNet relaxation (Apple-GPU accelerated), Materials Project convex-hull
  stability, MEGNet multi-fidelity band gaps (HSE), Crossref literature
  search. Budgets are enforced in code; the models can't talk their way
  around them.
- **The record** — an append-only lab notebook (the agent's cross-iteration
  memory) and a SQLite ledger of every candidate ever considered. Final
  reports are generated from this ground truth injected into the prompt —
  never from the model's recollection.

## Results

Agent vs non-LLM baselines on the PV-absorber mission (gap 1.1–1.7 eV,
≤ 0.05 eV/atom above hull, absent from Materials Project). Every strategy
gets the same cap of 100 CHGNet relaxations per run (5 iterations × 20).
The cap equalises relaxations, not total compute: LLM inference is not
counted and an agent may stop short of the cap, which is why both columns
matter.

| strategy | runs | hits per run, mean ± SD (range) | hits per 100 relaxations | relaxations used |
|---|---|---|---|---|
| random | 8 | 1.0 ± 0.9 (0–3) | 1.4 ± 1.2 | 75 |
| chemistry similarity | 8 | 2.0 ± 0.5 (1–3) | 3.0 ± 0.7 | 66 |
| Bayesian optimisation (GP + EI) | 8 | 1.5 ± 1.4 (0–4) | 1.7 ± 1.6 | 87 |
| agent, qwen3:32b (local) | 3 | 2.7 ± 1.2 (2–4) | 32.0 ± 21.9 | 9 |
| agent, Claude Sonnet 5.5 | 5 | **16.4 ± 2.1** (14–19) | 18.1 ± 2.2 | 91 |
| agent, Sonnet 5.5 + `rank_by_surrogate` | 5 | 11.0 ± 2.5 (9–15) | 12.4 ± 2.1 | 88 |
| agent, Claude Opus 5.5 | 3 | 18.7 ± 5.5 (13–24) | 18.8 ± 5.5 | 99 |

- **Frontier vs local proposer.** Same mission, prompts, tools, critic and
  cap: Sonnet 5.5 turned the cap into about six times as many hits as
  qwen3:32b, every run above every qwen run (exact permutation p = 0.018,
  the floor for 5 vs 3). Per relaxation the local model scores higher
  (not significant) because it used under a tenth of its budget. The qwen
  runs are from July 2026; the write-up lists what that does and does not
  control.
- **Agent vs baselines.** All 19 Claude runs on this mission, in every
  configuration tried, beat all 24 baseline runs on both metrics.
- **Which parts matter.** Giving the agent the BO acquisition function
  *lowered* its hits (11.0 vs 16.4 per run, n = 5 each, p = 0.012); a
  surrogate × critic 2×2 puts the loss in the combination of the two
  (critic vetoes rose 2.5×). The critic on its own changed nothing.
  Opus 5.5 showed no detectable gain over Sonnet at ~2.7× the cost.
- **Replicated baselines.** Bayesian optimisation at n = 8 is
  indistinguishable from random, so an earlier n = 2 reading of "zero
  hits" did not hold up.
- **Second mission, partly.** On the QD-emitter mission Sonnet found
  9.0 ± 2.6 hits per run vs 3.8 ± 1.1 for similarity (n = 3 vs 5), but per
  relaxation the gap is not significant and one BO run beat one Sonnet run.

Full tables, per-run values, the critic audit and the spend ledger
($18.05 of API credit for the whole study) are in
[results/2026-10-10-claude-ablation/analysis.md](results/2026-10-10-claude-ablation/analysis.md).
Hits recur across runs (the agents keep re-finding the Ag₂-kesterite and
alkali-telluride families), so per-run counts are not independent
discoveries, and "absent from Materials Project" is not "new to science".

All predictions carry surrogate error bars (CHGNet ~0.05 eV/atom on hull
distances; MEGNet gaps worse). Outputs are *candidates for validation*, never
"discoveries".

## Layout

- `src/athanor/tools/` — deterministic tool layer (filters, scoring,
  MP search, literature)
- `src/athanor/agent/` — registry, campaign tools, critic, prompts, loop
- `src/athanor/llm/` — provider-agnostic backends (Ollama/OpenAI-compat,
  Anthropic)
- `src/athanor/{baselines,metrics,benchmark,dashboard}.py` — the
  evaluation machinery
- `config/` — missions; `tests/` — hermetic suite (`uv run pytest`, no
  network/GPU needed)

The dashboard UI is specified in [WIREFRAMES.md](WIREFRAMES.md) — SVG
wireframes of every page, card, and state, traced from the shipped
`src/athanor/web/` implementation and drawn in its own tokens.

## Where this is going

See [ROADMAP.md](ROADMAP.md) — short term: finish the benchmark matrix and
rediscovery validation; mid term: magnetism screening and active learning;
long term: the surrogates that quantum-materials searches actually need
(optical, dopability, defects, topology). [PLAN.md](PLAN.md) documents the
original build (phases 0–4, complete).

## License

AGPL-3.0 — see [LICENSE](LICENSE). © 2026 Tsung-Han Yang.

*This project is personal work, developed and maintained in my personal capacity.*
