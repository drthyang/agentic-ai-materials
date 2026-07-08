# Replication analysis: the aligned agent's advantage is real

*2026-07-08. Two replicate runs (seeds 6, 7) of the objective-aligned agent
(qwen3:32b + gemma4:26b critic, hardened backend), identical protocol to
benchmark 2. Note on "seeds": the seed drives the baselines' RNG; agent
variation across runs comes from LLM sampling randomness. Three independent
aligned-agent runs now exist (benchmark 2 + these two).*

## Aggregate: hits per 100 relaxations

| strategy | runs | values | mean ± std |
|---|---|---|---|
| random | 8 | 0.00, 1.67, 1.23, 3.95, 1.61, 1.27, 0.00, 1.32 | 1.38 ± 1.15 |
| similarity | 8 | 1.72, 2.70, 2.90, 2.82, 3.57, 3.28, 3.12, 3.95 | 3.01 ± 0.62 |
| **agent (aligned)** | 3 | 57.1, 22.2, 16.7 | **32.0 ± 17.9** |

**Complete separation: the agent's worst run (16.7) is 4.2× the best
baseline observation ever recorded (similarity's 3.95).** With 3 agent runs
all ranking above all 8 similarity runs, the exact one-sided rank
probability under the null is 1/C(11,3) = 1/165 ≈ **p = 0.006**. Pooled
alternative (robust to small denominators): 8 hits in 28 agent relaxations
= 28.6/100 vs similarity's 24 hits in 796 ≈ 3.0/100.

The efficiency claim is now statistically defensible. The *magnitude* is
noisy (17.9 std on 3 runs) — more replicates would tighten it, but the
direction no longer depends on any single run.

## The convergence result (arguably the bigger finding)

Three independent runs, three different sampling trajectories — **all three
converged on the same chemical family**: Ag₂(II)(IV)(VI)₄ silver kesterites.

| compound | found in run(s) | hull (eV/atom) | gap (eV) |
|---|---|---|---|
| CdAg₂GeSe₄ | seed 0 **and** seed 7 | 0.000 | 1.28 |
| ZnAg₂GeSe₄ | seed 6 | 0.000 | 1.12 |
| MgAg₂GeTe₄ | seed 0 **and** seed 7 | 0.025 | 1.49 |
| ZnAg₂GeTe₄ | seed 6 | 0.028 | 1.17 |
| MgAg₂SnSe₄ | seed 0 | 0.016 | 1.59 |
| MgAg₂SnTe₄ | seed 0 | 0.038 | 1.17 |

Two members sit exactly on the convex hull; the family reproduces across
runs including *different* members each time — this is a coherent stable
composition plateau, not cherry-picking. (Novelty caveats per the
benchmark-2 audit: CdAg₂GeSe₄ recently synthesized; Ag₂ZnGeSe₄ likely known
from the Parasyuk-school literature; the Mg tellurides remain
candidate-novel pending ICSD/OQMD.)

Honest failures reproduced too: each run still has 1–2 iterations that spend
nothing (seed 7 burned iteration 3 on wildly unstable Ti quaternaries,
hull ≈ 0.44 — creative, wrong, and correctly measured as wrong), and budget
usage stays low (7–12 of 100). The efficiency numbers are *high despite*
this, not because of it.

## Engineering note

Both replicates ran start-to-finish on the hardened backend (retries +
crash guard + 600s timeout) after the first attempt at these same
replicates was killed by a single 300s read-timeout. The failure cost one
night; the fix is tested and permanent.

## Status of the overall study

| claim | status |
|---|---|
| Aligned local agent beats chemistry-informed enumeration on hit efficiency | **Supported** (3/3 runs, p ≈ 0.006, complete separation) |
| Objective alignment, not capability, was the binding constraint | Supported (same model 0 → 57 via prompt change; benchmark 1 vs 2) |
| The loop finds real chemistry | Supported (on-hull members synthesized/DFT-validated externally) |
| Genuinely novel candidates | Two Mg tellurides pending ICSD/OQMD audit |
| Model-capability effect (Claude vs local) | Not yet run (needs ANTHROPIC_API_KEY) |

Remaining before a preprint draft: ICSD/OQMD manual check of MgAg₂GeTe₄ and
MgAg₂SnTe₄; optionally 2–3 more agent replicates to tighten the mean; the
Claude capability run if the capability axis is wanted in v1.
