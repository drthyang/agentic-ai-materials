## Per-arm summary

| arm | n | hits/100 relax: mean ± sd [95% bootstrap CI] | median (min–max) | hits/run: mean ± sd (min–max) | relaxations/run: mean (min–max) |
|---|---|---|---|---|---|
| random | 8 | 0.9 ± 1.7 [0.0, 2.1] | 0.0 (0.0–4.0) | 0.6 ± 1.2 (0–3) | 75.1 (60–87) |
| similarity | 8 | 1.3 ± 0.6 [0.9, 1.6] | 1.4 (0.0–1.8) | 0.9 ± 0.4 (0–1) | 66.1 (56–76) |
| bayesopt | 8 | 0.7 ± 0.8 [0.1, 1.2] | 0.6 (0.0–2.1) | 0.6 ± 0.7 (0–2) | 86.8 (80–95) |
| agent qwen3:32b, no surrogate | 3 | 5.6 ± 9.6 [0.0, 16.7] | 0.0 (0.0–16.7) | 0.3 ± 0.6 (0–1) | 5.7 (4–7) |
| agent Sonnet 5.5, no surrogate (critic failed open) | 5 | 5.6 ± 1.6 [4.3, 6.8] | 6.1 (3.1–7.6) | 5.4 ± 1.5 (3–7) | 96.0 (92–98) |
| agent Sonnet 5.5, + rank_by_surrogate (critic failed open) | 5 | 6.4 ± 3.2 [4.6, 9.3] | 5.2 (4.0–12.1) | 6.2 ± 3.3 (4–12) | 96.4 (88–100) |

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
| agent qwen3:32b, no surrogate | 20261012-033313-seed0-fx-qwen-nosurr | 7 | 0 | 0.0 | 0.208 | 0.29 | 1 | 3 | — | — | — |
| agent qwen3:32b, no surrogate | 20261012-045504-seed6-fx-qwen-nosurr | 6 | 1 | 16.7 | 0.010 | 0.17 | 4 | 0 | — | — | GaCu2SbS4 |
| agent qwen3:32b, no surrogate | 20261012-061403-seed7-fx-qwen-nosurr | 4 | 0 | 0.0 | 0.530 | 1.00 | 2 | 0 | — | — | — |
| agent Sonnet 5.5, no surrogate (critic failed open) | 20261012-072454-seed11-fx-sonnet-nosurr | 96 | 3 | 3.1 | 0.046 | 0.99 | 0 | 96 | 0.63 | critic_failed_open | MgAg2SnSe4 MgSi(AgTe2)2 SiNi(AgSe2)2 |
| agent Sonnet 5.5, no surrogate (critic failed open) | 20261012-073400-seed12-fx-sonnet-nosurr | 98 | 6 | 6.1 | 0.008 | 1.00 | 0 | 98 | 0.51 | critic_failed_open | BaSi(AgSe2)2 MgAg2SnSe4 MgSi(AgTe2)2 SiNi(AgSe2)2 SrAg2SnS4 SrSi(AgSe2)2 |
| agent Sonnet 5.5, no surrogate (critic failed open) | 20261012-074011-seed13-fx-sonnet-nosurr | 92 | 7 | 7.6 | 0.023 | 0.99 | 0 | 92 | 0.55 | critic_failed_open | Ag3SbSe4 BaSi(AgSe2)2 Cu2AgAsS4 CuAg2AsS4 MgAg2SnSe4 SrAg2SnS4 SrSi(AgSe2)2 |
| agent Sonnet 5.5, no surrogate (critic failed open) | 20261012-074752-seed14-fx-sonnet-nosurr | 96 | 5 | 5.2 | 0.023 | 1.00 | 0 | 96 | 0.53 | critic_failed_open | BaSi(AgSe2)2 MgAg2SnSe4 MgSi(AgTe2)2 SrAg2SnS4 SrSi(AgSe2)2 |
| agent Sonnet 5.5, no surrogate (critic failed open) | 20261012-075519-seed15-fx-sonnet-nosurr | 98 | 6 | 6.1 | 0.025 | 1.00 | 0 | 98 | 0.61 | critic_failed_open | K2ZnSnTe4 K2ZrCdTe4 MgAg2SnSe4 MgSi(AgTe2)2 Na2CdSnTe4 Na2ZnGeTe4 |
| agent Sonnet 5.5, + rank_by_surrogate (critic failed open) | 20261012-080505-seed21-fx-sonnet-surr | 98 | 5 | 5.1 | 0.008 | 1.00 | 0 | 98 | 0.64 | critic_failed_open | BaSi(AgSe2)2 MgAg2SnSe4 MgSi(AgTe2)2 SrAg2SnS4 SrSi(AgSe2)2 |
| agent Sonnet 5.5, + rank_by_surrogate (critic failed open) | 20261012-081314-seed22-fx-sonnet-surr | 99 | 12 | 12.1 | 0.024 | 1.00 | 0 | 99 | 0.62 | critic_failed_open | Ag3SbSe4 BaSi(AgSe2)2 Cu2AgAsS4 CuAg2AsS4 CuAg2PSe4 KAg2AsSe4 MgAg2SnSe4 NaAg2AsS4 NaAg2AsSe4 NaCu2SbS4 SrAg2SnS4 SrSi(AgSe2)2 |
| agent Sonnet 5.5, + rank_by_surrogate (critic failed open) | 20261012-082030-seed23-fx-sonnet-surr | 100 | 4 | 4.0 | 0.008 | 0.99 | 0 | 100 | 0.58 | critic_failed_open | BaSi(AgSe2)2 MgAg2SnSe4 SrAg2SnS4 SrSi(AgSe2)2 |
| agent Sonnet 5.5, + rank_by_surrogate (critic failed open) | 20261012-082636-seed24-fx-sonnet-surr | 97 | 5 | 5.2 | 0.023 | 0.99 | 0 | 97 | 0.61 | critic_failed_open | BaSi(AgSe2)2 MgAg2SnSe4 MgSi(AgTe2)2 SrAg2SnS4 SrSi(AgSe2)2 |
| agent Sonnet 5.5, + rank_by_surrogate (critic failed open) | 20261012-083420-seed25-fx-sonnet-surr | 88 | 5 | 5.7 | 0.008 | 1.00 | 0 | 88 | 0.60 | critic_failed_open | BaSi(AgSe2)2 MgAg2SnSe4 MgSi(AgTe2)2 SrAg2SnS4 SrSi(AgSe2)2 |

## Comparisons (exact permutation test on the difference in means, two-sided; P(A>B) = probability of superiority over all run pairs)

| A | B | metric | mean A | mean B | P(A>B) | p (two-sided) |
|---|---|---|---|---|---|---|
| agent Sonnet 5.5, no surrogate (critic failed open) | similarity | hits_per_100_relaxations | 5.64 | 1.31 | 1.00 | 0.0008 |
| agent Sonnet 5.5, no surrogate (critic failed open) | similarity | hits | 5.40 | 0.88 | 1.00 | 0.0008 |
| agent Sonnet 5.5, no surrogate (critic failed open) | similarity | relaxations | 96.00 | 66.12 | 1.00 | 0.0008 |
| agent Sonnet 5.5, no surrogate (critic failed open) | agent qwen3:32b, no surrogate | hits_per_100_relaxations | 5.64 | 5.56 | 0.67 | 0.9643 |
| agent Sonnet 5.5, no surrogate (critic failed open) | agent qwen3:32b, no surrogate | hits | 5.40 | 0.33 | 1.00 | 0.0179 |
| agent Sonnet 5.5, no surrogate (critic failed open) | agent qwen3:32b, no surrogate | relaxations | 96.00 | 5.67 | 1.00 | 0.0179 |
| agent Sonnet 5.5, no surrogate (critic failed open) | agent Sonnet 5.5, + rank_by_surrogate (critic failed open) | hits_per_100_relaxations | 5.64 | 6.41 | 0.60 | 0.7778 |
| agent Sonnet 5.5, no surrogate (critic failed open) | agent Sonnet 5.5, + rank_by_surrogate (critic failed open) | hits | 5.40 | 6.20 | 0.58 | 0.8571 |
| agent Sonnet 5.5, no surrogate (critic failed open) | agent Sonnet 5.5, + rank_by_surrogate (critic failed open) | relaxations | 96.00 | 96.40 | 0.32 | 0.9206 |
| agent Sonnet 5.5, + rank_by_surrogate (critic failed open) | similarity | hits_per_100_relaxations | 6.41 | 1.31 | 1.00 | 0.0008 |
| agent Sonnet 5.5, + rank_by_surrogate (critic failed open) | similarity | hits | 6.20 | 0.88 | 1.00 | 0.0008 |
| agent Sonnet 5.5, + rank_by_surrogate (critic failed open) | similarity | relaxations | 96.40 | 66.12 | 1.00 | 0.0008 |
| agent qwen3:32b, no surrogate | similarity | hits_per_100_relaxations | 5.56 | 1.31 | 0.38 | 0.2727 |
| agent qwen3:32b, no surrogate | similarity | hits | 0.33 | 0.88 | 0.23 | 0.1515 |
| agent qwen3:32b, no surrogate | similarity | relaxations | 5.67 | 66.12 | 0.00 | 0.0061 |
| similarity | bayesopt | hits_per_100_relaxations | 1.31 | 0.70 | 0.80 | 0.1088 |
| similarity | bayesopt | hits | 0.88 | 0.62 | 0.63 | 0.6737 |
| similarity | bayesopt | relaxations | 66.12 | 86.75 | 0.00 | 0.0002 |
| bayesopt | random | hits_per_100_relaxations | 0.70 | 0.90 | 0.56 | 0.8107 |
| bayesopt | random | hits | 0.62 | 0.62 | 0.57 | 1.0000 |
| bayesopt | random | relaxations | 86.75 | 75.12 | 0.91 | 0.0056 |
| similarity | random | hits_per_100_relaxations | 1.31 | 0.90 | 0.70 | 0.4833 |
| similarity | random | hits | 0.88 | 0.62 | 0.70 | 0.7868 |
| similarity | random | relaxations | 66.12 | 75.12 | 0.19 | 0.0584 |

## Critic audit (vetoes checked against relaxations of the same composition in any other run of this study)

| arm | vetoes | vetoed compositions relaxed elsewhere | of those, hits |
|---|---|---|---|
| agent qwen3:32b, no surrogate | 7 | 3 | 0 |
