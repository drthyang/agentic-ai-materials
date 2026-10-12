# Athanor

A closed-loop agent that proposes, critiques, computes and records materials
candidates under a fixed compute budget, and is benchmarked against non-LLM
baselines. *(Formerly published as **matdiscover**; that CLI name still works.)*

## What it does

- **Proposes.** A tool-calling LLM (local `qwen3:32b` via Ollama by default;
  Claude with `--backend anthropic`) states a chemical hypothesis and proposes a
  family of substitutions on known prototype structures, through eight tools
  whose budgets are enforced in code.
- **Critiques.** An independent second model (`gemma4:26b`) reviews every batch
  before compute is spent; vetoes cost nothing and are logged with reasons.
- **Computes.** Charge-balance and novelty filters, then CHGNet relaxation,
  energy above the Materials Project hull, and a MEGNet band gap. A
  `rank_by_surrogate` tool exposes the Bayesian-optimisation baseline's GP to the
  agent.
- **Records.** Every proposal, veto and score goes to SQLite and an append-only
  lab notebook; the final report is written from that record, never from memory.
- **Shows its work.** A read-only dashboard (Mission Control) and a static export
  for GitHub Pages.

## Quick start

```bash
uv sync
export MP_API_KEY=...        # free key from materialsproject.org/api (or .env)
ollama pull qwen3:32b && ollama pull gemma4:26b

uv run athanor check                       # environment
uv run athanor run --iterations 3          # one campaign
uv run athanor benchmark --iterations 5    # agent vs random / similarity / BO
uv run athanor dashboard                   # localhost:8517
uv run pytest                              # hermetic tests
```

Missions are YAML files (`config/mission.yaml`, `config/missions/`); swapping
the science target needs no code change.

## How it is evaluated, and current results

Every strategy gets the same cap of 100 CHGNet relaxations per run (5 iterations
× 20) on the same filters and scorer; a *hit* is a converged candidate in the
mission's band-gap window, within 0.05 eV/atom of the hull, and absent from
Materials Project. The cap matches relaxations, not total compute.

On the PV-absorber mission, with both scoring defects below fixed, Claude
Sonnet 5.5 as proposer found **5.4 ± 1.5 hits per run** (n = 5) against
0.9 ± 0.4 for the best non-LLM baseline (similarity, n = 8; two-sided
p = 0.0008) and 0.3 ± 0.6 for the local qwen3:32b (n = 3; p = 0.018). The
Bayesian-optimisation tool made no detectable difference (p = 0.86). The critic
failed open in those Sonnet runs, so they ran without one.

All results are surrogate-level: candidates for validation, not discoveries.
Details: [results/2026-10-12-fixed-prototypes/analysis.md](results/2026-10-12-fixed-prototypes/analysis.md).

> **Correction (October 2026).** Results published before 2026-10-12 rested on
> two scoring defects: the chalcopyrite and kesterite prototypes were 8-atom
> half-cells, and the convex hull mixed energy scales (uncorrected Materials
> Project vs CHGNet's MP2020-corrected). The July headline (32 hits per 100
> relaxations, complete separation from the baselines) and several October claims
> are withdrawn. Both defects are fixed and the benchmark was rerun; see the
> [rerun](results/2026-10-12-fixed-prototypes/analysis.md) and the
> [audit](results/2026-10-10-claude-ablation/analysis.md).

## Documents

- [WALKTHROUGH.md](WALKTHROUGH.md) — the machine and every experiment, in order
- [results/](results/) — one write-up per experiment, newest first:
  [fixed-prototype rerun](results/2026-10-12-fixed-prototypes/analysis.md),
  [Claude ablation and structure audit](results/2026-10-10-claude-ablation/analysis.md)
- [ROADMAP.md](ROADMAP.md) — what comes next · [PLAN.md](PLAN.md) — the original build
- [WIREFRAMES.md](WIREFRAMES.md) — the dashboard specification
- [paper/draft.md](paper/draft.md) — preprint draft (claims C3–C5 withdrawn)
- [CLAUDE.md](CLAUDE.md) — conventions for coding agents working on the repo

## License

AGPL-3.0 — see [LICENSE](LICENSE). © 2026 Tsung-Han Yang.

*This project is personal work, developed and maintained in my personal capacity.*
