# Novelty-aware baselines: the fair control

*Runs 2026-10-13 13:25 to 14:27 EDT on the user's Mac, local only, $0 of API
credit. Every number is surrogate-level (CHGNet relaxation, Materials Project
hull, MEGNet HSE gap): candidates for validation, not discoveries.*

## Why this run

The original baselines check each candidate against Materials Project but
relax it either way. The agent is told not to spend relaxations on known
compositions, and a known composition can never be a hit. So part of the
agent's lead in the 2026-10-12 rerun could be that handicap rather than better
choices. The original baselines also left 13–34 of their 100 relaxations
unspent: they stop after 10 batches per iteration.

The `-novel` variants (src/athanor/baselines.py) change exactly those two
things: they skip compositions Materials Project already has before relaxing,
and may draw up to 50 batches per iteration so the skips do not leave budget
unspent. Same mission, seeds 0–7, 5 iterations × 20 relaxations, both scoring
fixes, same filters, scorer and hit rule. The Sonnet arm is the 2026-10-12
no-surrogate arm, unchanged (its critic failed open; see
results/2026-10-12-fixed-prototypes/analysis.md).

## Result (PV mission)

| arm | n | relaxations per run | hits per run, mean ± SD (range) | hits per 100 relaxations | distinct hits |
|---|---|---|---|---|---|
| random | 8 | 75 (60–87) | 0.6 ± 1.2 (0–3) | 0.9 ± 1.7 | 4 |
| random-novel | 8 | 100 | 0.9 ± 1.1 (0–3) | 0.9 ± 1.1 | 4 |
| similarity | 8 | 66 (56–76) | 0.9 ± 0.4 (0–1) | 1.3 ± 0.6 | 1 |
| similarity-novel | 8 | 98 (94–100) | 2.0 ± 0.0 (2–2) | 2.0 ± 0.1 | 2 |
| bayesopt | 8 | 87 (80–95) | 0.6 ± 0.7 (0–2) | 0.7 ± 0.8 | 4 |
| bayesopt-novel | 8 | 100 | 0.6 ± 0.5 (0–1) | 0.6 ± 0.5 | 3 |
| Sonnet 5.5 agent | 5 | 96 (92–98) | 5.4 ± 1.5 (3–7) | 5.6 ± 1.6 | 13 |

Exact permutation tests, two-sided (arms-pv-summary.md):

| comparison | hits per run | hits per 100 relaxations | head-to-head, per run |
|---|---|---|---|
| Sonnet vs similarity-novel | p = 0.0008 | p = 0.0008 | 40 of 40 won |
| Sonnet vs random-novel | p = 0.0016 | p = 0.0008 | 39 won, 1 tie |
| Sonnet vs bayesopt-novel | p = 0.0008 | p = 0.0008 | 40 of 40 won |
| similarity-novel vs similarity | p = 0.0002 | p = 0.0002 | |
| random-novel vs random | p = 0.81 | p = 1.0 | |
| bayesopt-novel vs bayesopt | p = 1.0 | p = 0.70 | |

## What it means

- **The handicap was real for the strongest baseline.** Similarity more than
  doubles (0.9 → 2.0 hits per run) once it skips known compositions and spends
  its budget. Random and Bayesian optimisation do not change.
- **The agent still beats every baseline,** now at equal spend (96 vs 98–100
  relaxations). Its lead over the best baseline is about 2.7× (5.4 vs 2.0 per
  run, 5.6 vs 2.0 per 100 relaxations), down from about 6× against the
  original baselines. Roughly half of the original gap was the handicap.
- **Every Sonnet run beat every similarity-novel run.** Similarity-novel finds
  the same two compositions in every run (CuSnS₂ and MnZn(CuS₂)₂); the agent
  found 13 distinct ones in 5 runs.
- These comparisons supersede the original-baseline ones as the fair control
  for agent-vs-baseline claims. The original arms stay as recorded.

## Caveats

- Sonnet arm: n = 5, critic effectively off, hits concentrated in a few
  families (see the 2026-10-12 analysis). Not rerun here.
- The runs used uncommitted code (`run_config.json` records
  `3dc1c1c…-dirty`); the exact code is in
  [code-at-launch.diff](code-at-launch.diff).
- No new structure or novelty audit was needed: every hit composition here
  (CuSnS₂, MnZn(CuS₂)₂, MnCd(CuS₂)₂, MnGa(CuS₂)₂, Cu₂AgAsS₄) was also a hit
  for an October baseline, so the audits in
  results/2026-10-12-fixed-prototypes/ already cover them.

## Reproduce

```bash
scripts/run_novelty_baselines.sh
uv run python scripts/aggregate_ablation.py results/2026-10-13-novelty-baselines/arms-pv.json
```
