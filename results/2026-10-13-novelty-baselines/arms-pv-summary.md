## Per-arm summary

| arm | n | hits/100 relax: mean ± sd [95% bootstrap CI] | median (min–max) | hits/run: mean ± sd (min–max) | relaxations/run: mean (min–max) |
|---|---|---|---|---|---|
| random | 8 | 0.9 ± 1.7 [0.0, 2.1] | 0.0 (0.0–4.0) | 0.6 ± 1.2 (0–3) | 75.1 (60–87) |
| similarity | 8 | 1.3 ± 0.6 [0.9, 1.6] | 1.4 (0.0–1.8) | 0.9 ± 0.4 (0–1) | 66.1 (56–76) |
| bayesopt | 8 | 0.7 ± 0.8 [0.1, 1.2] | 0.6 (0.0–2.1) | 0.6 ± 0.7 (0–2) | 86.8 (80–95) |
| random-novel | 8 | 0.9 ± 1.1 [0.2, 1.6] | 0.5 (0.0–3.0) | 0.9 ± 1.1 (0–3) | 100.0 (100–100) |
| similarity-novel | 8 | 2.0 ± 0.1 [2.0, 2.1] | 2.0 (2.0–2.1) | 2.0 ± 0.0 (2–2) | 97.8 (94–100) |
| bayesopt-novel | 8 | 0.6 ± 0.5 [0.2, 0.9] | 1.0 (0.0–1.0) | 0.6 ± 0.5 (0–1) | 100.0 (100–100) |
| agent Sonnet 5.5 (critic failed open) | 5 | 5.6 ± 1.6 [4.3, 6.8] | 6.1 (3.1–7.6) | 5.4 ± 1.5 (3–7) | 96.0 (92–98) |

## Per-run values

| arm | run | relax | hits | hits/100 | best \|Δgap\| | novel frac | critic vetoes | critic auto-approved | API $ | ledger status | hit formulas |
|---|---|---|---|---|---|---|---|---|---|---|---|
| random | 20261012-071557-seed0-fx-pv-base | 80 | 0 | 0.0 | 0.003 | 0.60 | — | — | — | — | — |
| random | 20261012-071919-seed1-fx-pv-base | 60 | 0 | 0.0 | 0.056 | 0.57 | — | — | — | — | — |
| random | 20261012-072357-seed2-fx-pv-base | 81 | 0 | 0.0 | 0.010 | 0.58 | — | — | — | — | — |
| random | 20261012-073355-seed3-fx-pv-base | 76 | 3 | 4.0 | 0.064 | 0.67 | — | — | — | — | Cu2AgAsS4 CuSnS2 MnCd(CuS2)2 |
| random | 20261012-074144-seed4-fx-pv-base | 62 | 2 | 3.2 | 0.010 | 0.65 | — | — | — | — | CuSnS2 MnZn(CuS2)2 |
| random | 20261012-074955-seed5-fx-pv-base | 79 | 0 | 0.0 | 0.031 | 0.66 | — | — | — | — | — |
| random | 20261012-080002-seed6-fx-pv-base | 87 | 0 | 0.0 | 0.043 | 0.66 | — | — | — | — | — |
| random | 20261012-081157-seed7-fx-pv-base | 76 | 0 | 0.0 | 0.010 | 0.60 | — | — | — | — | — |
| similarity | 20261012-071557-seed0-fx-pv-base | 58 | 0 | 0.0 | 0.010 | 0.57 | — | — | — | — | — |
| similarity | 20261012-071919-seed1-fx-pv-base | 74 | 1 | 1.4 | 0.010 | 0.49 | — | — | — | — | CuSnS2 |
| similarity | 20261012-072357-seed2-fx-pv-base | 69 | 1 | 1.4 | 0.010 | 0.56 | — | — | — | — | CuSnS2 |
| similarity | 20261012-073355-seed3-fx-pv-base | 71 | 1 | 1.4 | 0.010 | 0.47 | — | — | — | — | CuSnS2 |
| similarity | 20261012-074144-seed4-fx-pv-base | 56 | 1 | 1.8 | 0.010 | 0.50 | — | — | — | — | CuSnS2 |
| similarity | 20261012-074955-seed5-fx-pv-base | 61 | 1 | 1.6 | 0.010 | 0.51 | — | — | — | — | CuSnS2 |
| similarity | 20261012-080002-seed6-fx-pv-base | 64 | 1 | 1.6 | 0.010 | 0.56 | — | — | — | — | CuSnS2 |
| similarity | 20261012-081157-seed7-fx-pv-base | 76 | 1 | 1.3 | 0.010 | 0.54 | — | — | — | — | CuSnS2 |
| bayesopt | 20261012-071557-seed0-fx-pv-base | 80 | 0 | 0.0 | 0.095 | 0.59 | — | — | — | — | — |
| bayesopt | 20261012-071919-seed1-fx-pv-base | 83 | 1 | 1.2 | 0.082 | 0.68 | — | — | — | — | MnZn(CuS2)2 |
| bayesopt | 20261012-072357-seed2-fx-pv-base | 90 | 0 | 0.0 | 0.056 | 0.64 | — | — | — | — | — |
| bayesopt | 20261012-073355-seed3-fx-pv-base | 89 | 0 | 0.0 | 0.144 | 0.73 | — | — | — | — | — |
| bayesopt | 20261012-074144-seed4-fx-pv-base | 91 | 1 | 1.1 | 0.010 | 0.51 | — | — | — | — | CuSnS2 |
| bayesopt | 20261012-074955-seed5-fx-pv-base | 84 | 1 | 1.2 | 0.051 | 0.63 | — | — | — | — | MnZn(CuS2)2 |
| bayesopt | 20261012-080002-seed6-fx-pv-base | 95 | 2 | 2.1 | 0.032 | 0.78 | — | — | — | — | Cu2AgAsS4 MnGa(CuS2)2 |
| bayesopt | 20261012-081157-seed7-fx-pv-base | 82 | 0 | 0.0 | 0.010 | 0.61 | — | — | — | — | — |
| random-novel | 20261013-172547-seed0-fx-pv-novel | 100 | 0 | 0.0 | 0.104 | 1.00 | — | — | — | — | — |
| random-novel | 20261013-173502-seed1-fx-pv-novel | 100 | 0 | 0.0 | 0.043 | 1.00 | — | — | — | — | — |
| random-novel | 20261013-174416-seed2-fx-pv-novel | 100 | 0 | 0.0 | 0.032 | 1.00 | — | — | — | — | — |
| random-novel | 20261013-175300-seed3-fx-pv-novel | 100 | 3 | 3.0 | 0.017 | 1.00 | — | — | — | — | Cu2AgAsS4 CuSnS2 MnCd(CuS2)2 |
| random-novel | 20261013-180048-seed4-fx-pv-novel | 100 | 1 | 1.0 | 0.082 | 1.00 | — | — | — | — | CuSnS2 |
| random-novel | 20261013-180729-seed5-fx-pv-novel | 100 | 1 | 1.0 | 0.031 | 1.00 | — | — | — | — | MnZn(CuS2)2 |
| random-novel | 20261013-181410-seed6-fx-pv-novel | 100 | 0 | 0.0 | 0.043 | 1.00 | — | — | — | — | — |
| random-novel | 20261013-182110-seed7-fx-pv-novel | 100 | 2 | 2.0 | 0.076 | 1.00 | — | — | — | — | CuSnS2 MnZn(CuS2)2 |
| similarity-novel | 20261013-172547-seed0-fx-pv-novel | 99 | 2 | 2.0 | 0.082 | 1.00 | — | — | — | — | CuSnS2 MnZn(CuS2)2 |
| similarity-novel | 20261013-173502-seed1-fx-pv-novel | 100 | 2 | 2.0 | 0.032 | 1.00 | — | — | — | — | CuSnS2 MnZn(CuS2)2 |
| similarity-novel | 20261013-174416-seed2-fx-pv-novel | 95 | 2 | 2.1 | 0.032 | 1.00 | — | — | — | — | CuSnS2 MnZn(CuS2)2 |
| similarity-novel | 20261013-175300-seed3-fx-pv-novel | 94 | 2 | 2.1 | 0.082 | 1.00 | — | — | — | — | CuSnS2 MnZn(CuS2)2 |
| similarity-novel | 20261013-180048-seed4-fx-pv-novel | 100 | 2 | 2.0 | 0.032 | 1.00 | — | — | — | — | CuSnS2 MnZn(CuS2)2 |
| similarity-novel | 20261013-180729-seed5-fx-pv-novel | 100 | 2 | 2.0 | 0.032 | 1.00 | — | — | — | — | CuSnS2 MnZn(CuS2)2 |
| similarity-novel | 20261013-181410-seed6-fx-pv-novel | 94 | 2 | 2.1 | 0.032 | 1.00 | — | — | — | — | CuSnS2 MnZn(CuS2)2 |
| similarity-novel | 20261013-182110-seed7-fx-pv-novel | 100 | 2 | 2.0 | 0.032 | 1.00 | — | — | — | — | CuSnS2 MnZn(CuS2)2 |
| bayesopt-novel | 20261013-172547-seed0-fx-pv-novel | 100 | 0 | 0.0 | 0.021 | 1.00 | — | — | — | — | — |
| bayesopt-novel | 20261013-173502-seed1-fx-pv-novel | 100 | 1 | 1.0 | 0.017 | 1.00 | — | — | — | — | MnZn(CuS2)2 |
| bayesopt-novel | 20261013-174416-seed2-fx-pv-novel | 100 | 0 | 0.0 | 0.032 | 1.00 | — | — | — | — | — |
| bayesopt-novel | 20261013-175300-seed3-fx-pv-novel | 100 | 0 | 0.0 | 0.144 | 1.00 | — | — | — | — | — |
| bayesopt-novel | 20261013-180048-seed4-fx-pv-novel | 100 | 1 | 1.0 | 0.021 | 1.00 | — | — | — | — | CuSnS2 |
| bayesopt-novel | 20261013-180729-seed5-fx-pv-novel | 100 | 1 | 1.0 | 0.032 | 1.00 | — | — | — | — | MnZn(CuS2)2 |
| bayesopt-novel | 20261013-181410-seed6-fx-pv-novel | 100 | 1 | 1.0 | 0.032 | 1.00 | — | — | — | — | MnGa(CuS2)2 |
| bayesopt-novel | 20261013-182110-seed7-fx-pv-novel | 100 | 1 | 1.0 | 0.033 | 1.00 | — | — | — | — | MnZn(CuS2)2 |
| agent Sonnet 5.5 (critic failed open) | 20261012-072454-seed11-fx-sonnet-nosurr | 96 | 3 | 3.1 | 0.046 | 0.99 | 0 | 96 | 0.63 | — | MgAg2SnSe4 MgSi(AgTe2)2 SiNi(AgSe2)2 |
| agent Sonnet 5.5 (critic failed open) | 20261012-073400-seed12-fx-sonnet-nosurr | 98 | 6 | 6.1 | 0.008 | 1.00 | 0 | 98 | 0.51 | — | BaSi(AgSe2)2 MgAg2SnSe4 MgSi(AgTe2)2 SiNi(AgSe2)2 SrAg2SnS4 SrSi(AgSe2)2 |
| agent Sonnet 5.5 (critic failed open) | 20261012-074011-seed13-fx-sonnet-nosurr | 92 | 7 | 7.6 | 0.023 | 0.99 | 0 | 92 | 0.55 | — | Ag3SbSe4 BaSi(AgSe2)2 Cu2AgAsS4 CuAg2AsS4 MgAg2SnSe4 SrAg2SnS4 SrSi(AgSe2)2 |
| agent Sonnet 5.5 (critic failed open) | 20261012-074752-seed14-fx-sonnet-nosurr | 96 | 5 | 5.2 | 0.023 | 1.00 | 0 | 96 | 0.53 | — | BaSi(AgSe2)2 MgAg2SnSe4 MgSi(AgTe2)2 SrAg2SnS4 SrSi(AgSe2)2 |
| agent Sonnet 5.5 (critic failed open) | 20261012-075519-seed15-fx-sonnet-nosurr | 98 | 6 | 6.1 | 0.025 | 1.00 | 0 | 98 | 0.61 | — | K2ZnSnTe4 K2ZrCdTe4 MgAg2SnSe4 MgSi(AgTe2)2 Na2CdSnTe4 Na2ZnGeTe4 |

## Comparisons (exact permutation test on the difference in means, two-sided; P(A>B) = probability of superiority over all run pairs)

| A | B | metric | mean A | mean B | P(A>B) | p (two-sided) |
|---|---|---|---|---|---|---|
| agent Sonnet 5.5 (critic failed open) | random-novel | hits_per_100_relaxations | 5.64 | 0.88 | 1.00 | 0.0008 |
| agent Sonnet 5.5 (critic failed open) | random-novel | hits | 5.40 | 0.88 | 0.99 | 0.0016 |
| agent Sonnet 5.5 (critic failed open) | random-novel | relaxations | 96.00 | 100.00 | 0.00 | 0.0008 |
| agent Sonnet 5.5 (critic failed open) | similarity-novel | hits_per_100_relaxations | 5.64 | 2.05 | 1.00 | 0.0008 |
| agent Sonnet 5.5 (critic failed open) | similarity-novel | hits | 5.40 | 2.00 | 1.00 | 0.0008 |
| agent Sonnet 5.5 (critic failed open) | similarity-novel | relaxations | 96.00 | 97.75 | 0.30 | 0.3147 |
| agent Sonnet 5.5 (critic failed open) | bayesopt-novel | hits_per_100_relaxations | 5.64 | 0.62 | 1.00 | 0.0008 |
| agent Sonnet 5.5 (critic failed open) | bayesopt-novel | hits | 5.40 | 0.62 | 1.00 | 0.0008 |
| agent Sonnet 5.5 (critic failed open) | bayesopt-novel | relaxations | 96.00 | 100.00 | 0.00 | 0.0008 |
| random-novel | random | hits_per_100_relaxations | 0.88 | 0.90 | 0.56 | 1.0000 |
| random-novel | random | hits | 0.88 | 0.62 | 0.59 | 0.8107 |
| random-novel | random | relaxations | 100.00 | 75.12 | 1.00 | 0.0002 |
| similarity-novel | similarity | hits_per_100_relaxations | 2.05 | 1.31 | 1.00 | 0.0002 |
| similarity-novel | similarity | hits | 2.00 | 0.88 | 1.00 | 0.0002 |
| similarity-novel | similarity | relaxations | 97.75 | 66.12 | 1.00 | 0.0002 |
| bayesopt-novel | bayesopt | hits_per_100_relaxations | 0.62 | 0.70 | 0.41 | 0.7009 |
| bayesopt-novel | bayesopt | hits | 0.62 | 0.62 | 0.52 | 1.0000 |
| bayesopt-novel | bayesopt | relaxations | 100.00 | 86.75 | 1.00 | 0.0002 |
| similarity-novel | random-novel | hits_per_100_relaxations | 2.05 | 0.88 | 0.84 | 0.0095 |
| similarity-novel | random-novel | hits | 2.00 | 0.88 | 0.81 | 0.0331 |
| similarity-novel | random-novel | relaxations | 97.75 | 100.00 | 0.25 | 0.0769 |
| bayesopt-novel | random-novel | hits_per_100_relaxations | 0.62 | 0.88 | 0.48 | 0.7868 |
| bayesopt-novel | random-novel | hits | 0.62 | 0.88 | 0.48 | 0.7868 |
| bayesopt-novel | random-novel | relaxations | 100.00 | 100.00 | 0.50 | 1.0000 |

## Critic audit (vetoes checked against relaxations of the same composition in any other run of this study)

| arm | vetoes | vetoed compositions relaxed elsewhere | of those, hits |
|---|---|---|---|
