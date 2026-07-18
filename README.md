# Athanor — Agentic AI for Materials Discovery

> An *athanor* is the alchemists' furnace: built to sustain a slow
> transmutation, self-feeding, running unattended. This one has a skeptic
> inside.

*Formerly published as **matdiscover** — the name some external links
still use. Same project, renamed 2026-07; the `matdiscover` CLI command
still works.*

A closed-loop **"AI materials scientist"**: an LLM agent that states chemical
hypotheses, proposes candidate materials, screens them with physics-grounded
surrogate models, reflects on the results in a lab notebook, and iterates —
then writes a research report from ground-truth data. Runs **entirely on
local models** (Ollama) by default; Claude is a one-line config switch.

```
mission config ──▶ [LLM hypothesizes] ──▶ propose ──▶ filter (SMACT, palette)
                        ▲                                    │
                        │                          critic review (2nd LLM)
                   lab notebook                              │
                   + SQLite DB  ◀── evaluate: CHGNet relax ──▶ formation energy
                        ▲                  │                  energy above hull
                        │                  └────────────────▶ band gap (MEGNet)
                   [LLM reflects] ◀───────── results ◀───────┘
```

Why it's interesting: the agent's "experiments" are real physics (ML
interatomic potentials, convex-hull thermodynamics), success is objectively
measurable, and every campaign is benchmarked against **non-LLM baselines at
identical compute** — so "the agent helps" is a claim with a control group.

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
uv run athanor benchmark               # agent vs random vs similarity
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
  `--backend anthropic` for Claude). Hypothesizes, proposes substitutions on
  known prototypes, decides what's worth evaluating.
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

## Results so far

- Full pipeline verified live end-to-end with local models doing real
  hypothesis-driven iterations.
- First screening hit (similarity baseline, 19 relaxations): **CdCuSe2** —
  predicted 1.70 eV gap, 0.003 eV/atom above hull, no Materials Project
  entry. Surrogate-level only; needs DFT validation.
- Headline agent-vs-baseline benchmark: in progress.

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

## Where this is going

See [ROADMAP.md](ROADMAP.md) — short term: finish the benchmark matrix and
rediscovery validation; mid term: magnetism screening and active learning;
long term: the surrogates that quantum-materials searches actually need
(optical, dopability, defects, topology). [PLAN.md](PLAN.md) documents the
original build (phases 0–4, complete).
