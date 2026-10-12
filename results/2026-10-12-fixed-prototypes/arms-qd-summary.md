## Per-arm summary

| arm | n | hits/100 relax: mean ± sd [95% bootstrap CI] | median (min–max) | hits/run: mean ± sd (min–max) | relaxations/run: mean (min–max) |
|---|---|---|---|---|---|
| random | 5 | 0.4 ± 0.8 [0.0, 1.1] | 0.0 (0.0–1.9) | 0.2 ± 0.4 (0–1) | 56.2 (51–63) |
| similarity | 5 | 1.6 ± 0.9 [0.8, 2.1] | 2.0 (0.0–2.2) | 0.8 ± 0.4 (0–1) | 48.8 (40–62) |
| bayesopt | 5 | 0.3 ± 0.6 [0.0, 0.8] | 0.0 (0.0–1.4) | 0.2 ± 0.4 (0–1) | 69.4 (65–77) |

## Per-run values

| arm | run | relax | hits | hits/100 | best \|Δgap\| | novel frac | critic vetoes | critic auto-approved | API $ | ledger status | hit formulas |
|---|---|---|---|---|---|---|---|---|---|---|---|
| random | 20261012-082009-seed8-fx-qd-base | 51 | 0 | 0.0 | 0.071 | 0.65 | — | — | — | — | — |
| random | 20261012-082233-seed9-fx-qd-base | 53 | 0 | 0.0 | 0.047 | 0.60 | — | — | — | — | — |
| random | 20261012-082650-seed10-fx-qd-base | 61 | 0 | 0.0 | 0.201 | 0.59 | — | — | — | — | — |
| random | 20261012-083337-seed11-fx-qd-base | 63 | 0 | 0.0 | 0.075 | 0.67 | — | — | — | — | — |
| random | 20261012-084108-seed12-fx-qd-base | 53 | 1 | 1.9 | 0.182 | 0.72 | — | — | — | — | Cu2SiSnS4 |
| similarity | 20261012-082009-seed8-fx-qd-base | 62 | 1 | 1.6 | 0.145 | 0.69 | — | — | — | — | Cu2SiSnS4 |
| similarity | 20261012-082233-seed9-fx-qd-base | 40 | 0 | 0.0 | 0.236 | 0.55 | — | — | — | — | — |
| similarity | 20261012-082650-seed10-fx-qd-base | 47 | 1 | 2.1 | 0.145 | 0.60 | — | — | — | — | Cu2SiSnS4 |
| similarity | 20261012-083337-seed11-fx-qd-base | 50 | 1 | 2.0 | 0.145 | 0.64 | — | — | — | — | Cu2SiSnS4 |
| similarity | 20261012-084108-seed12-fx-qd-base | 45 | 1 | 2.2 | 0.145 | 0.60 | — | — | — | — | Cu2SiSnS4 |
| bayesopt | 20261012-082009-seed8-fx-qd-base | 65 | 0 | 0.0 | 0.075 | 0.57 | — | — | — | — | — |
| bayesopt | 20261012-082233-seed9-fx-qd-base | 65 | 0 | 0.0 | 0.120 | 0.52 | — | — | — | — | — |
| bayesopt | 20261012-082650-seed10-fx-qd-base | 77 | 0 | 0.0 | 0.145 | 0.61 | — | — | — | — | — |
| bayesopt | 20261012-083337-seed11-fx-qd-base | 68 | 0 | 0.0 | 0.136 | 0.63 | — | — | — | — | — |
| bayesopt | 20261012-084108-seed12-fx-qd-base | 72 | 1 | 1.4 | 0.048 | 0.54 | — | — | — | — | AlCu2AgS4 |

## Comparisons (exact permutation test on the difference in means, two-sided; P(A>B) = probability of superiority over all run pairs)

| A | B | metric | mean A | mean B | P(A>B) | p (two-sided) |
|---|---|---|---|---|---|---|
| similarity | bayesopt | hits_per_100_relaxations | 1.59 | 0.28 | 0.88 | 0.0476 |
| similarity | bayesopt | hits | 0.80 | 0.20 | 0.80 | 0.2063 |
| similarity | bayesopt | relaxations | 48.80 | 69.40 | 0.00 | 0.0079 |
| similarity | random | hits_per_100_relaxations | 1.59 | 0.38 | 0.84 | 0.0873 |
| similarity | random | hits | 0.80 | 0.20 | 0.80 | 0.2063 |
| similarity | random | relaxations | 48.80 | 56.20 | 0.16 | 0.1349 |
| bayesopt | random | hits_per_100_relaxations | 0.28 | 0.38 | 0.48 | 1.0000 |
| bayesopt | random | hits | 0.20 | 0.20 | 0.50 | 1.0000 |
| bayesopt | random | relaxations | 69.40 | 56.20 | 1.00 | 0.0079 |

## Critic audit (vetoes checked against relaxations of the same composition in any other run of this study)

| arm | vetoes | vetoed compositions relaxed elsewhere | of those, hits |
|---|---|---|---|
