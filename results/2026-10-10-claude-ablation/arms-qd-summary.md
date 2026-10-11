## Per-arm summary

| arm | n | hits/100 relax: mean ± sd [95% bootstrap CI] | median (min–max) | hits/run: mean ± sd (min–max) | relaxations/run: mean (min–max) |
|---|---|---|---|---|---|
| random | 5 | 4.9 ± 2.2 [3.2, 6.6] | 4.9 (2.0–7.5) | 2.8 ± 1.3 (1–4) | 56.2 (51–63) |
| similarity | 5 | 7.7 ± 1.5 [6.3, 8.6] | 8.1 (5.0–8.9) | 3.8 ± 1.1 (2–5) | 48.8 (40–62) |
| bayesopt | 5 | 5.4 ± 4.0 [3.2, 9.0] | 3.9 (3.1–12.5) | 3.8 ± 2.9 (2–9) | 69.4 (65–77) |
| agent qwen3:32b, no surrogate (July) | 1 | 66.7 ± — — | 66.7 (66.7–66.7) | 2.0 ± — (2–2) | 3.0 (3–3) |
| agent Sonnet 5.5, no surrogate | 3 | 11.7 ± 4.7 [6.3, 14.5] | 14.3 (6.3–14.5) | 9.0 ± 2.6 (6–11) | 80.3 (69–95) |

Structure-robust hits per run (hits whose composition is still a hit when re-scored in a correct bulk cell; structure-audit.csv):

| arm | n | robust hits/run: mean ± sd (min–max) |
|---|---|---|
| random | 5 | 0.8 ± 0.8 (0–2) |
| similarity | 5 | 1.4 ± 0.9 (0–2) |
| bayesopt | 5 | 1.2 ± 2.2 (0–5) |
| agent qwen3:32b, no surrogate (July) | 1 | 0.0 ± — (0–0) |
| agent Sonnet 5.5, no surrogate | 3 | 2.3 ± 1.2 (1–3) |

## Per-run values

| arm | run | relax | hits | hits/100 | best \|Δgap\| | novel frac | critic vetoes | API $ | cache-read share | hit formulas |
|---|---|---|---|---|---|---|---|---|---|---|
| random | 20261011-064821-seed8-qd-base | 51 | 1 | 2.0 | 0.009 | 0.65 | — | — | — | BaCa(CuS2)2 |
| random | 20261011-065502-seed9-qd-base | 53 | 2 | 3.8 | 0.044 | 0.60 | — | — | — | Cu2SnSeS4 MgCu2SnS4 |
| random | 20261011-070033-seed10-qd-base | 61 | 3 | 4.9 | 0.044 | 0.59 | — | — | — | Cu2SnGeS4 Cu2SnSeS4 SrZn(CuS2)2 |
| random | 20261011-070733-seed11-qd-base | 63 | 4 | 6.3 | 0.009 | 0.67 | — | — | — | Cu2SnSeS4 InI2Cl SrZnSe2 Zn3SnO4 |
| random | 20261011-071438-seed12-qd-base | 53 | 4 | 7.5 | 0.025 | 0.72 | — | — | — | Cu2SiSnS4 Cu2TeS5 MgCu2SnS4 ZnCu2SeS4 |
| similarity | 20261011-064821-seed8-qd-base | 62 | 5 | 8.1 | 0.044 | 0.69 | — | — | — | Cu2SiSnS4 Cu2SnGeS4 Cu2SnSeS4 ZnCu2SeS4 ZnSn3S4 |
| similarity | 20261011-065502-seed9-qd-base | 40 | 2 | 5.0 | 0.108 | 0.55 | — | — | — | Cu2SnGeS4 ZnSn3S4 |
| similarity | 20261011-070033-seed10-qd-base | 47 | 4 | 8.5 | 0.044 | 0.60 | — | — | — | Cu2SiSnS4 Cu2SnGeS4 Cu2SnSeS4 ZnCu2SeS4 |
| similarity | 20261011-070733-seed11-qd-base | 50 | 4 | 8.0 | 0.044 | 0.64 | — | — | — | Cu2SiSnS4 Cu2SnGeS4 Cu2SnSeS4 ZnSn3S4 |
| similarity | 20261011-071438-seed12-qd-base | 45 | 4 | 8.9 | 0.108 | 0.60 | — | — | — | Cu2SiSnS4 Cu2SnGeS4 ZnCu2SeS4 ZnSn3S4 |
| bayesopt | 20261011-064821-seed8-qd-base | 65 | 2 | 3.1 | 0.139 | 0.57 | — | — | — | CuAg2SnS4 CuAgI2 |
| bayesopt | 20261011-065502-seed9-qd-base | 65 | 2 | 3.1 | 0.025 | 0.52 | — | — | — | Cu2SnGeS4 SrZn(CuS2)2 |
| bayesopt | 20261011-070033-seed10-qd-base | 77 | 3 | 3.9 | 0.108 | 0.60 | — | — | — | Cu2SnCl4O Cu2SnTeI4 SrZn(CuS2)2 |
| bayesopt | 20261011-070733-seed11-qd-base | 68 | 3 | 4.4 | 0.044 | 0.63 | — | — | — | Cu2SnSeS4 PSe2Cl SrZn(CuS2)2 |
| bayesopt | 20261011-071438-seed12-qd-base | 72 | 9 | 12.5 | 0.021 | 0.54 | — | — | — | BaCa(CuS2)2 BaMg(CuS2)2 BaZn(CuS2)2 Cu2SnGeS4 MgCu2SnS4 ZnAg2SeS4 ZnAg2TeS4 ZnGe2SeS4 ZnGe2TeS4 |
| agent qwen3:32b, no surrogate (July) | 20260708-131929-seed8 | 3 | 2 | 66.7 | 0.507 | 1.00 | 0 | — | — | MgAg2GeS4 MgAg2GeSe4 |
| agent Sonnet 5.5, no surrogate | 20261011-072045-seed41-qd-sonnet-nosurr | 69 | 10 | 14.5 | 0.021 | 1.00 | 10 | 0.72 | 0.83 | AlGa(AgS2)2 Cu2AgPSe4 Cu2SnGeS4 CuAg2PS4 CuAg2PSe4 MgAg2GeS4 MgAg2GeSe4 MgAg2SnS4 MgCu2SnS4 SrAg2GeS4 |
| agent Sonnet 5.5, no surrogate | 20261011-074126-seed42-qd-sonnet-nosurr | 95 | 6 | 6.3 | 0.019 | 1.00 | 9 | 0.68 | 0.81 | Ba2InCuS4 CaZn3S4 MgAg2GeS4 MgAg2GeSe4 MgAg2SnS4 MgCu2SnS4 |
| agent Sonnet 5.5, no surrogate | 20261011-080331-seed43-qd-sonnet-nosurr | 77 | 11 | 14.3 | 0.003 | 0.99 | 7 | 0.83 | 0.83 | AlGa(AgS2)2 BaSnO2 Cu2AgPSe4 CuAg2PS4 CuAg2PSe4 MgAg2GeS4 MgAg2GeSe4 MgAg2SnS4 MgCu2SnS4 SrAg2GeS4 SrSnS2 |

## Comparisons (one-sided exact permutation test on the mean; P(A>B) = probability of superiority over all run pairs)

| A | B | metric | mean A | mean B | P(A>B) | p (A > B) |
|---|---|---|---|---|---|---|
| agent Sonnet 5.5, no surrogate | similarity | hits_per_100_relaxations | 11.70 | 7.69 | 0.73 | 0.0893 |
| agent Sonnet 5.5, no surrogate | similarity | hits | 9.00 | 3.80 | 1.00 | 0.0179 |
| agent Sonnet 5.5, no surrogate | similarity | relaxations | 80.33 | 48.80 | 1.00 | 0.0179 |
| agent Sonnet 5.5, no surrogate | similarity | robust_hits | 2.33 | 1.40 | 0.77 | 0.1964 |
| agent Sonnet 5.5, no surrogate | bayesopt | hits_per_100_relaxations | 11.70 | 5.39 | 0.93 | 0.0357 |
| agent Sonnet 5.5, no surrogate | bayesopt | hits | 9.00 | 3.80 | 0.93 | 0.0357 |
| agent Sonnet 5.5, no surrogate | bayesopt | relaxations | 80.33 | 69.40 | 0.83 | 0.0893 |
| agent Sonnet 5.5, no surrogate | bayesopt | robust_hits | 2.33 | 1.20 | 0.77 | 0.2500 |

## Critic audit (vetoes checked against relaxations of the same composition in any other run of this study)

| arm | vetoes | vetoed compositions relaxed elsewhere | of those, hits |
|---|---|---|---|
| agent Sonnet 5.5, no surrogate | 26 | 13 | 1 |
