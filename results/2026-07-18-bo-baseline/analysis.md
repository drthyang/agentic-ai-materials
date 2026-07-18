# Bayesian-optimization baseline: seeds 0–1

**Runs:** `data/benchmark/20260718-160305-seed0/` and the seed-1 dir —
baselines only, 5 iterations × 20 relaxations, pv-absorber-v1
(gap 1.1–1.7 eV, hull ≤ 0.05 eV/atom). BO strategy introduced in
commit `38f4fbe` (GP + expected improvement over composition features;
utility = −|gap − 1.4| − 10·max(0, hull − 0.05)).

| strategy | seed 0: hits (best \|Δgap\|) | seed 1: hits (best \|Δgap\|) |
|---|---|---|
| random | 0 (0.249) | 1 (0.041) |
| similarity | 1 (0.041) | 2 (0.041) |
| **bayesopt** | **0** (0.095) | **0** (**0.036**) |

Reference bands from earlier seeds (n=8): random 1.38±1.15,
similarity 3.01±0.62; aligned agent (n=3): 32.0±17.9 hits/100 relax.
Random and similarity landed inside their bands both seeds.

## What BO actually found

Its in-window compositions across both seeds, ordered by stability
(`bayesopt.db`):

| seed | formula | gap (eV) | hull (eV/at) | novel? | why not a hit |
|---|---|---|---|---|---|
| 0 | CuCl | 1.30 | 0.000 | no | known, on the hull |
| 0 | MgSb | 1.17 | 0.184 | no | known and unstable |
| 0 | Sr₂ZnSnSe₄ | 1.15 | 0.250 | yes | novel but far from stable |
| 1 | NaAsSe₂ | 1.10 | 0.000 | no | known, on the hull |
| 1 | **AlSb** | **1.49** | **0.000** | no | **the textbook III–V absorber** |
| 1 | CdCu₂SnS₄ | 1.69 | 0.011 | no | known |
| 1 | GaCuSe₂ | 1.21 | 0.099 | no | known (CuGaSe₂) |
| 1 | Zn₃SnSe₄ | 1.36 | 0.128 | yes | novel but unstable |

Seed 1 is the cleaner illustration: BO's best find was **AlSb at
1.49 eV on the hull** — 0.036 eV from the mission's ideal gap, and a
semiconductor known since the 1950s. The optimizer found the textbook
answer, because the textbook answer optimizes the objective it was
given.

## Interpretation (preliminary — two seeds)

1. **The GP works as an optimizer.** Gap targeting improved markedly
   over random (best |gap−ideal| 0.095 vs 0.249): EI is steering toward
   the objective it was given.
2. **It walked straight into the known-materials trap.** Exploiting a
   gap+stability objective converges on chemistry that is stable and
   well-tuned precisely because it is already known (CuCl, literally on
   the hull). Novelty is a database-membership predicate — not a smooth
   function of composition features — so it cannot simply be added to
   the GP's utility. This mirrors benchmark 1, where the naive agent
   also did coherent optimization inside known space and scored zero.
   The aligned agent escapes because it *reasons about* novelty as a
   constraint; encoding the same constraint in an acquisition function
   is genuinely awkward.
3. If this pattern holds across seeds, it sharpens the paper's thesis:
   the hard part of discovery-as-search is not optimization pressure
   but objective alignment — and a language model is currently the
   cheapest place to encode "novel" as a first-class goal.

## Caveats & next steps

- **n=2 seeds, both zero hits with best-in-class gap targeting
  (0.095, 0.036 eV).** Consistent so far; 3+ more seeds would make the
  band citable.
- A fair stronger BO control would add a novelty-aware term (e.g.
  penalize proximity to known compositions in feature space, or filter
  the pool to MP-novel candidates before EI). Worth building — if
  novelty-aware BO still trails the agent, the alignment claim gets
  stronger; if it catches up, that is an important (and honest) result.
- Similarity's single hit at this seed is CdCuSe₂ again — consistent
  with its n=8 band.
