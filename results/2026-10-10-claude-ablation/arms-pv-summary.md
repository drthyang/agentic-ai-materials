## Per-arm summary

| arm | n | hits/100 relax: mean ± sd [95% bootstrap CI] | median (min–max) | hits/run: mean ± sd (min–max) | relaxations/run: mean (min–max) |
|---|---|---|---|---|---|
| random | 8 | 1.4 ± 1.2 [0.7, 2.2] | 1.3 (0.0–4.0) | 1.0 ± 0.9 (0–3) | 75.1 (60–87) |
| similarity | 8 | 3.0 ± 0.7 [2.5, 3.4] | 3.0 (1.7–4.0) | 2.0 ± 0.5 (1–3) | 66.1 (56–76) |
| bayesopt | 8 | 1.7 ± 1.6 [0.7, 2.7] | 1.2 (0.0–4.4) | 1.5 ± 1.4 (0–4) | 86.8 (80–95) |
| agent qwen3:32b, no surrogate (July) | 3 | 32.0 ± 21.9 [16.7, 57.1] | 22.2 (16.7–57.1) | 2.7 ± 1.2 (2–4) | 9.3 (7–12) |
| agent qwen3:32b, no surrogate (same day) | 3 | 11.1 ± 19.2 [0.0, 33.3] | 0.0 (0.0–33.3) | 0.3 ± 0.6 (0–1) | 4.7 (3–8) |
| agent qwen3:32b, + rank_by_surrogate (same day) | 1 | 0.0 ± — — | 0.0 (0.0–0.0) | 0.0 ± — (0–0) | 5.0 (5–5) |
| agent Sonnet 5.5, no surrogate | 5 | 18.1 ± 2.2 [16.4, 19.8] | 17.6 (15.7–21.1) | 16.4 ± 2.1 (14–19) | 90.8 (89–93) |
| agent Sonnet 5.5, + rank_by_surrogate | 5 | 12.4 ± 2.1 [10.9, 14.2] | 11.8 (10.0–15.8) | 11.0 ± 2.5 (9–15) | 88.4 (76–96) |
| agent Sonnet 5.5, + surrogate, no critic | 3 | 16.5 ± 3.2 [14.3, 20.2] | 14.9 (14.3–20.2) | 15.0 ± 3.5 (13–19) | 90.7 (87–94) |
| agent Sonnet 5.5, no surrogate, no critic | 3 | 17.4 ± 3.4 [14.7, 21.3] | 16.3 (14.7–21.3) | 16.3 ± 3.2 (14–20) | 93.7 (92–95) |
| agent Opus 5.5, no surrogate | 3 | 18.8 ± 5.5 [13.3, 24.2] | 19.0 (13.3–24.2) | 18.7 ± 5.5 (13–24) | 99.0 (98–100) |

Re-scored with both 2026-10 fixes (rescore-rows.csv; distinct compositions per run): *hull fix* = the run's own cells on the corrected hull; *both fixes* = every evaluated candidate rebuilt in a correct cell and scored on the corrected hull.

| arm | n | raw hits/run | hull fix only | both fixes: mean ± sd (min–max) |
|---|---|---|---|---|
| random | 8 | 1.0 | 0.0 ± 0.0 | 0.6 ± 1.2 (0–3) |
| similarity | 8 | 2.0 | 0.0 ± 0.0 | 0.9 ± 0.4 (0–1) |
| bayesopt | 8 | 1.5 | 0.1 ± 0.4 | 0.6 ± 0.7 (0–2) |
| agent qwen3:32b, no surrogate (July) | 3 | 2.7 | 0.0 ± 0.0 | 0.3 ± 0.6 (0–1) |
| agent qwen3:32b, no surrogate (same day) | 3 | 0.3 | 0.0 ± 0.0 | 0.0 ± 0.0 (0–0) |
| agent qwen3:32b, + rank_by_surrogate (same day) | 1 | 0.0 | 0.0 ± — | 0.0 ± — (0–0) |
| agent Sonnet 5.5, no surrogate | 5 | 16.4 | 0.8 ± 0.4 | 7.4 ± 0.9 (7–9) |
| agent Sonnet 5.5, + rank_by_surrogate | 5 | 11.0 | 0.2 ± 0.4 | 4.6 ± 2.9 (2–9) |
| agent Sonnet 5.5, + surrogate, no critic | 3 | 15.0 | 0.3 ± 0.6 | 6.3 ± 1.5 (5–8) |
| agent Sonnet 5.5, no surrogate, no critic | 3 | 16.3 | 0.0 ± 0.0 | 6.3 ± 0.6 (6–7) |
| agent Opus 5.5, no surrogate | 3 | 18.7 | 0.3 ± 0.6 | 11.0 ± 2.0 (9–13) |

Structure-robust hits per run (hits whose composition is still a hit when re-scored in a correct bulk cell; structure-audit.csv):

| arm | n | robust hits/run: mean ± sd (min–max) |
|---|---|---|
| random | 8 | 0.5 ± 0.8 (0–2) |
| similarity | 8 | 0.9 ± 0.4 (0–1) |
| bayesopt | 8 | 0.2 ± 0.5 (0–1) |
| agent qwen3:32b, no surrogate (July) | 3 | 0.3 ± 0.6 (0–1) |
| agent qwen3:32b, no surrogate (same day) | 3 | 0.0 ± 0.0 (0–0) |
| agent qwen3:32b, + rank_by_surrogate (same day) | 1 | 0.0 ± — (0–0) |
| agent Sonnet 5.5, no surrogate | 5 | 4.4 ± 1.3 (2–5) |
| agent Sonnet 5.5, + rank_by_surrogate | 5 | 3.0 ± 1.4 (1–4) |
| agent Sonnet 5.5, + surrogate, no critic | 3 | 4.3 ± 2.1 (2–6) |
| agent Sonnet 5.5, no surrogate, no critic | 3 | 3.3 ± 2.3 (2–6) |
| agent Opus 5.5, no surrogate | 3 | 4.3 ± 3.2 (2–8) |

## Per-run values

| arm | run | relax | hits | hits/100 | best \|Δgap\| | novel frac | critic vetoes | critic auto-approved | API $ | ledger status | hit formulas |
|---|---|---|---|---|---|---|---|---|---|---|---|
| random | 20260707-231335-seed0 | 80 | 0 | 0.0 | 0.249 | 0.60 | — | — | — | — | — |
| random | 20260707-225531-seed1 | 60 | 1 | 1.7 | 0.041 | 0.57 | — | — | — | — | Cu2SnTeS4 |
| random | 20260707-230040-seed2 | 81 | 1 | 1.2 | 0.186 | 0.58 | — | — | — | — | Cu2TeWS4 |
| random | 20260707-230651-seed3 | 76 | 3 | 4.0 | 0.044 | 0.67 | — | — | — | — | Cu2SnTeS4 CuSnS2 ZnSn(I2Br)2 |
| random | 20260708-002610-seed4 | 62 | 1 | 1.6 | 0.018 | 0.65 | — | — | — | — | CuSnS2 |
| random | 20260708-010930-seed5 | 79 | 1 | 1.3 | 0.014 | 0.66 | — | — | — | — | CaCuSe2 |
| random | 20260708-021219-seed6 | 87 | 0 | 0.0 | 0.043 | 0.66 | — | — | — | — | — |
| random | 20260708-032352-seed7 | 76 | 1 | 1.3 | 0.014 | 0.60 | — | — | — | — | CaCuSe2 |
| similarity | 20260707-231335-seed0 | 58 | 1 | 1.7 | 0.041 | 0.57 | — | — | — | — | CdCuSe2 |
| similarity | 20260707-225531-seed1 | 74 | 2 | 2.7 | 0.041 | 0.49 | — | — | — | — | CdCuSe2 CuSnS2 |
| similarity | 20260707-230040-seed2 | 69 | 2 | 2.9 | 0.041 | 0.56 | — | — | — | — | CdCuSe2 CuSnS2 |
| similarity | 20260707-230651-seed3 | 71 | 2 | 2.8 | 0.041 | 0.47 | — | — | — | — | CdCuSe2 CuSnS2 |
| similarity | 20260708-002610-seed4 | 56 | 2 | 3.6 | 0.041 | 0.50 | — | — | — | — | CdCuSe2 CuSnS2 |
| similarity | 20260708-010930-seed5 | 61 | 2 | 3.3 | 0.041 | 0.51 | — | — | — | — | CdCuSe2 CuSnS2 |
| similarity | 20260708-021219-seed6 | 64 | 2 | 3.1 | 0.041 | 0.56 | — | — | — | — | CdCuSe2 CuSnS2 |
| similarity | 20260708-032352-seed7 | 76 | 3 | 4.0 | 0.041 | 0.54 | — | — | — | — | CdCuSe2 Cu2SnTeS4 CuSnS2 |
| bayesopt | 20260718-160305-seed0 | 80 | 0 | 0.0 | 0.095 | 0.59 | — | — | — | — | — |
| bayesopt | 20260718-161211-seed1 | 83 | 0 | 0.0 | 0.036 | 0.68 | — | — | — | — | — |
| bayesopt | 20261010-224906-seed2-bo-pv | 90 | 4 | 4.4 | 0.093 | 0.64 | — | — | — | — | Ba2NiSnS4 CuAgCl2 MgCd2SnS4 SrCuSe2 |
| bayesopt | 20261010-225555-seed3-bo-pv | 89 | 1 | 1.1 | 0.014 | 0.73 | — | — | — | — | CaCuSe2 |
| bayesopt | 20261010-230610-seed4-bo-pv | 91 | 1 | 1.1 | 0.029 | 0.51 | — | — | — | — | CuSnS2 |
| bayesopt | 20261010-231321-seed5-bo-pv | 84 | 1 | 1.2 | 0.032 | 0.63 | — | — | — | — | SrCuSe2 |
| bayesopt | 20261010-232028-seed6-bo-pv | 95 | 3 | 3.2 | 0.043 | 0.78 | — | — | — | — | CdCuSe2 Cu2SnTeS4 MnCu2AsS4 |
| bayesopt | 20261010-232828-seed7-bo-pv | 82 | 2 | 2.4 | 0.043 | 0.61 | — | — | — | — | CdCuSe2 SrCuSe2 |
| agent qwen3:32b, no surrogate (July) | 20260707-231335-seed0 | 7 | 4 | 57.1 | 0.090 | 1.00 | 3 | — | — | — | CdAg2GeSe4 MgAg2GeTe4 MgAg2SnSe4 MgAg2SnTe4 |
| agent qwen3:32b, no surrogate (July) | 20260708-021219-seed6 | 9 | 2 | 22.2 | 0.229 | 0.56 | 3 | — | — | — | ZnAg2GeSe4 ZnAg2GeTe4 |
| agent qwen3:32b, no surrogate (July) | 20260708-032352-seed7 | 12 | 2 | 16.7 | 0.090 | 0.83 | 1 | — | — | — | CdAg2GeSe4 MgAg2GeTe4 |
| agent qwen3:32b, no surrogate (same day) | 20261011-134359-seed0-qwen-nosurr-oct | 3 | 1 | 33.3 | 0.121 | 0.33 | 3 | 0 | — | — | CdAg2GeSe4 |
| agent qwen3:32b, no surrogate (same day) | 20261011-152517-seed6-qwen-nosurr-oct | 8 | 0 | 0.0 | 0.018 | 0.00 | 0 | 0 | — | — | — |
| agent qwen3:32b, no surrogate (same day) | 20261011-174133-seed7-qwen-nosurr-oct | 3 | 0 | 0.0 | 0.018 | 0.33 | 1 | 0 | — | — | — |
| agent qwen3:32b, + rank_by_surrogate (same day) | 20261011-184906-seed71-qwen-surr-oct | 5 | 0 | 0.0 | 0.115 | 0.00 | 5 | 0 | — | — | — |
| agent Sonnet 5.5, no surrogate | 20261010-233515-seed11-sonnet-nosurr | 91 | 15 | 16.5 | 0.021 | 1.00 | 5 | 0 | 0.62 | ok | CdAg2GeSe4 K2BaGeTe4 K2CaGeTe4 K2CaSnTe4 K2MgSnTe4 K2SrGeTe4 K2SrSnTe4 K2ZnSnTe4 MgAg2GeTe4 MgAg2SnSe4 MgAg2SnTe4 Na2CdSnTe4 SrAg2GeSe4 ZnAg2GeSe4 ZnAg2GeTe4 |
| agent Sonnet 5.5, no surrogate | 20261011-010913-seed12-sonnet-nosurr | 90 | 19 | 21.1 | 0.017 | 1.00 | 6 | 7 | 0.60 | ok | CdAg2GeSe4 K2BaGeTe4 K2BaSiTe4 K2CaGeTe4 K2CaSnTe4 K2CdSiTe4 K2MgSiTe4 K2MgSnTe4 K2SrGeTe4 K2SrSnTe4 K2ZnSnTe4 MgAg2GeTe4 MgAg2SnSe4 MgAg2SnTe4 Na2CdSnTe4 Na2MgGeTe4 SrAg2GeSe4 ZnAg2GeSe4 ZnAg2GeTe4 |
| agent Sonnet 5.5, no surrogate | 20261011-025804-seed13-sonnet-nosurr | 91 | 16 | 17.6 | 0.017 | 0.99 | 7 | 0 | 0.61 | ok | Ag3AsSe4 Ag3SbSe4 CdAg2GeSe4 Cu2NiGeS4 CuAg2AsSe4 CuAg2SbSe4 CuAsS2 KBiTe2 MgAg2GeTe4 MgAg2SnSe4 MgAg2SnTe4 NiAg2GeSe4 NiAg2SnSe4 SrAg2GeSe4 ZnAg2GeSe4 ZnAg2GeTe4 |
| agent Sonnet 5.5, no surrogate | 20261011-042017-seed14-sonnet-nosurr | 93 | 18 | 19.4 | 0.012 | 0.98 | 6 | 0 | 0.59 | ok | CdAg2GeSe4 K2BaGeTe4 K2BaSiTe4 K2CaGeTe4 K2CaSnTe4 K2CdSiTe4 K2MgSiTe4 K2MgSnTe4 K2SrGeTe4 K2SrSnTe4 K2ZnSnTe4 MgAg2GeTe4 MgAg2SnSe4 MgAg2SnTe4 Na2CdSnTe4 Na2MgGeTe4 ZnAg2GeSe4 ZnAg2GeTe4 |
| agent Sonnet 5.5, no surrogate | 20261011-054525-seed15-sonnet-nosurr | 89 | 14 | 15.7 | 0.017 | 1.00 | 0 | 14 | 0.56 | ok | CdAg2GeSe4 K2ZnSnTe4 KBiTe2 MgAg2GeTe4 MgAg2SnSe4 MgAg2SnTe4 Na2CdSnTe4 Na2MnGeSe4 Na2MnSnSe4 Na2ZrMnTe4 TiMn(AgS2)2 TiZn(AgS2)2 ZnAg2GeSe4 ZnAg2GeTe4 |
| agent Sonnet 5.5, + rank_by_surrogate | 20261011-002204-seed21-sonnet-surr | 76 | 9 | 11.8 | 0.017 | 0.97 | 13 | 0 | 0.75 | ok | CdAg2GeSe4 MgAg2GeTe4 MgAg2SnSe4 MgAg2SnTe4 NiAg2GeSe4 NiAg2SnSe4 SrAg2GeSe4 ZnAg2GeSe4 ZnAg2GeTe4 |
| agent Sonnet 5.5, + rank_by_surrogate | 20261011-015902-seed22-sonnet-surr | 95 | 15 | 15.8 | 0.017 | 0.90 | 12 | 20 | 0.92 | ok | CdAg2GeSe4 K2MgGeTe4 K2MgSnTe4 K2ZnSnTe4 KBiTe2 MgAg2GeTe4 MgAg2SnSe4 MgAg2SnTe4 Na2CdSnTe4 Na2MgGeTe4 SrAg2GeSe4 TiMn(AgS2)2 TiZn(AgS2)2 ZnAg2GeSe4 ZnAg2GeTe4 |
| agent Sonnet 5.5, + rank_by_surrogate | 20261011-034118-seed23-sonnet-surr | 85 | 10 | 11.8 | 0.013 | 1.00 | 9 | 0 | 0.67 | ok | CdAg2GeSe4 Cu2NiGeS4 MgAg2SnSe4 NiAg2GeSe4 NiAg2SnSe4 SrAg2GeSe4 TiCu2NiS4 TiMn(AgS2)2 TiZn(AgS2)2 ZnAg2GeSe4 |
| agent Sonnet 5.5, + rank_by_surrogate | 20261011-050701-seed24-sonnet-surr | 96 | 12 | 12.5 | 0.002 | 0.99 | 9 | 0 | 0.66 | ok | CdAg2GeSe4 K2MnGeSe4 MgAg2SnSe4 MgAg2SnTe4 Na2MnGeSe4 Na2MnSnSe4 Na2NiGeSe4 NiAg2GeSe4 NiAg2SnSe4 SrAg2GeSe4 ZnAg2GeSe4 ZnAg2GeTe4 |
| agent Sonnet 5.5, + rank_by_surrogate | 20261011-060541-seed25-sonnet-surr | 90 | 9 | 10.0 | 0.017 | 0.97 | 16 | 0 | 0.76 | ok | CdAg2GeSe4 K2MnGeSe4 MgAg2SnSe4 Na2CdSnTe4 Na2MnGeSe4 Na2MnSnSe4 SrAg2GeSe4 ZnAg2GeSe4 ZnAg2GeTe4 |
| agent Sonnet 5.5, + surrogate, no critic | 20261011-062436-seed31-sonnet-surr-nocritic | 94 | 19 | 20.2 | 0.017 | 0.99 | 0 | 0 | 0.66 | ok | CdAg2GeSe4 K2BaGeTe4 K2BaSiTe4 K2CaGeTe4 K2CaSnTe4 K2CdSiTe4 K2MnSiTe4 K2SrGeTe4 K2SrSnTe4 K2ZnSnTe4 KBiTe2 MgAg2SnSe4 MgAg2SnTe4 Na2CdSnTe4 NiAg2GeSe4 NiAg2SnSe4 SrAg2GeSe4 ZnAg2GeSe4 ZnAg2GeTe4 |
| agent Sonnet 5.5, + surrogate, no critic | 20261011-063221-seed32-sonnet-surr-nocritic | 87 | 13 | 14.9 | 0.033 | 0.98 | 0 | 0 | 0.65 | ok | CdAg2GeSe4 K2AgSbSe4 K2CuSbTe4 KBiTe2 MgAg2GeTe4 MgAg2SnSe4 MgAg2SnTe4 Na2AgSbSe4 Na2AgSbTe4 Na2CdSnTe4 Na2CuSbTe4 SrAg2GeSe4 ZnAg2GeSe4 |
| agent Sonnet 5.5, + surrogate, no critic | 20261011-064005-seed33-sonnet-surr-nocritic | 91 | 13 | 14.3 | 0.017 | 1.00 | 0 | 0 | 0.65 | ok | Ag3AsSe4 Ag3SbSe4 CdAg2GeSe4 Cu2AgBiS4 CuAg2AsSe4 CuAg2SbSe4 KBiTe2 MgAg2GeTe4 MgAg2SnSe4 MgAg2SnTe4 SrAg2GeSe4 ZnAg2GeSe4 ZnAg2GeTe4 |
| agent Sonnet 5.5, no surrogate, no critic | 20261011-091317-seed61-sonnet-nosurr-nocritic | 94 | 20 | 21.3 | 0.017 | 0.99 | 0 | 0 | 0.54 | ok | CdAg2GeSe4 K2BaGeTe4 K2CaGeTe4 K2CaSnTe4 K2CdSiTe4 K2MgGeTe4 K2MgSiTe4 K2MgSnTe4 K2MnGeSe4 K2MnSiSe4 K2MnSiTe4 K2SrGeTe4 K2SrSnTe4 Na2CdSnTe4 Na2MgGeTe4 Na2MnGeSe4 Na2MnSnSe4 SrAg2GeSe4 ZnAg2GeSe4 ZnAg2GeTe4 |
| agent Sonnet 5.5, no surrogate, no critic | 20261011-092102-seed62-sonnet-nosurr-nocritic | 92 | 15 | 16.3 | 0.012 | 0.99 | 0 | 0 | 0.65 | ok | Ag3AsSe4 Ag3SbSe4 CdAg2GeSe4 Cu2NiGeS4 CuAg2AsSe4 CuAg2SbSe4 KBiTe2 MgAg2GeTe4 MgAg2SnSe4 MgAg2SnTe4 NiAg2GeSe4 NiAg2SnSe4 SrAg2GeSe4 ZnAg2GeSe4 ZnAg2GeTe4 |
| agent Sonnet 5.5, no surrogate, no critic | 20261011-092920-seed63-sonnet-nosurr-nocritic | 95 | 14 | 14.7 | 0.017 | 1.00 | 0 | 0 | 0.57 | ok | Ag3AsSe4 Ag3SbSe4 CdAg2GeSe4 Cu2AgBiS4 CuAg2AsSe4 CuAg2SbSe4 KBiTe2 MgAg2GeTe4 MgAg2SnSe4 MgAg2SnTe4 SrAg2GeSe4 TiZn(AgS2)2 ZnAg2GeSe4 ZnAg2GeTe4 |
| agent Opus 5.5, no surrogate | 20261011-082538-seed51-opus-nosurr | 98 | 13 | 13.3 | 0.017 | 0.97 | 14 | 17 | 2.34 | ok | Ag3AsSe4 Ag3SbSe4 CdAg2GeSe4 CuAg2AsSe4 CuAg2SbSe4 KCu2SbSe4 MgAg2GeTe4 MgAg2SnSe4 MgAg2SnTe4 NaCu2SbSe4 TiZn(AgS2)2 ZnAg2GeSe4 ZnAg2GeTe4 |
| agent Opus 5.5, no surrogate | 20261011-085326-seed52-opus-nosurr | 99 | 24 | 24.2 | 0.017 | 0.99 | 9 | 0 | 1.53 | ok | CdAg2GeSe4 K2BaGeTe4 K2BaSiTe4 K2CaGeTe4 K2CaSnTe4 K2CdSiTe4 K2MgGeTe4 K2MgSiTe4 K2MgSnTe4 K2MnGeSe4 K2MnSiSe4 K2MnSiTe4 K2SrGeTe4 K2SrSnTe4 K2ZnSnTe4 MgAg2GeTe4 MgAg2SnSe4 MgAg2SnTe4 Na2CdSnTe4 Na2MgGeTe4 Na2MnGeSe4 Na2MnSnSe4 SrAg2GeSe4 ZnAg2GeSe4 |
| agent Opus 5.5, no surrogate | 20261011-093727-seed53-opus-nosurr | 100 | 19 | 19.0 | 0.012 | 0.99 | 0 | 16 | 1.54 | ok | Ag3AsSe4 Ag3SbSe4 CdAg2GeSe4 Cu2NiGeS4 CuAg2AsSe4 CuAg2SbSe4 K2CuSbTe4 KCu2SbSe4 MgAg2GeTe4 MgAg2SnSe4 MgAg2SnTe4 Na2AgSbTe4 Na2CuSbTe4 NaCu2SbSe4 NiAg2GeSe4 NiAg2SnSe4 TiZn(AgS2)2 ZnAg2GeSe4 ZnAg2GeTe4 |

## Comparisons (exact permutation test on the difference in means, two-sided; P(A>B) = probability of superiority over all run pairs)

| A | B | metric | mean A | mean B | P(A>B) | p (two-sided) |
|---|---|---|---|---|---|---|
| agent Sonnet 5.5, no surrogate | agent qwen3:32b, no surrogate (July) | hits_per_100_relaxations | 18.05 | 32.01 | 0.20 | 0.0893 |
| agent Sonnet 5.5, no surrogate | agent qwen3:32b, no surrogate (July) | hits | 16.40 | 2.67 | 1.00 | 0.0179 |
| agent Sonnet 5.5, no surrogate | agent qwen3:32b, no surrogate (July) | relaxations | 90.80 | 9.33 | 1.00 | 0.0179 |
| agent Sonnet 5.5, no surrogate | agent qwen3:32b, no surrogate (July) | robust_hits | 4.40 | 0.33 | 1.00 | 0.0179 |
| agent Sonnet 5.5, no surrogate | agent qwen3:32b, no surrogate (July) | hits_hullfix | 0.80 | 0.00 | 0.90 | 0.1429 |
| agent Sonnet 5.5, no surrogate | agent qwen3:32b, no surrogate (July) | hits_fixed | 7.40 | 0.33 | 1.00 | 0.0179 |
| agent Sonnet 5.5, no surrogate | agent qwen3:32b, no surrogate (same day) | hits_per_100_relaxations | 18.05 | 11.11 | 0.67 | 0.3571 |
| agent Sonnet 5.5, no surrogate | agent qwen3:32b, no surrogate (same day) | hits | 16.40 | 0.33 | 1.00 | 0.0179 |
| agent Sonnet 5.5, no surrogate | agent qwen3:32b, no surrogate (same day) | relaxations | 90.80 | 4.67 | 1.00 | 0.0179 |
| agent Sonnet 5.5, no surrogate | agent qwen3:32b, no surrogate (same day) | robust_hits | 4.40 | 0.00 | 1.00 | 0.0179 |
| agent Sonnet 5.5, no surrogate | agent qwen3:32b, no surrogate (same day) | hits_hullfix | 0.80 | 0.00 | 0.90 | 0.1429 |
| agent Sonnet 5.5, no surrogate | agent qwen3:32b, no surrogate (same day) | hits_fixed | 7.40 | 0.00 | 1.00 | 0.0179 |
| agent qwen3:32b, no surrogate (July) | agent qwen3:32b, no surrogate (same day) | hits_per_100_relaxations | 32.01 | 11.11 | 0.78 | 0.3000 |
| agent qwen3:32b, no surrogate (July) | agent qwen3:32b, no surrogate (same day) | hits | 2.67 | 0.33 | 1.00 | 0.1000 |
| agent qwen3:32b, no surrogate (July) | agent qwen3:32b, no surrogate (same day) | relaxations | 9.33 | 4.67 | 0.89 | 0.2000 |
| agent qwen3:32b, no surrogate (July) | agent qwen3:32b, no surrogate (same day) | robust_hits | 0.33 | 0.00 | 0.67 | 1.0000 |
| agent qwen3:32b, no surrogate (July) | agent qwen3:32b, no surrogate (same day) | hits_hullfix | 0.00 | 0.00 | 0.50 | 1.0000 |
| agent qwen3:32b, no surrogate (July) | agent qwen3:32b, no surrogate (same day) | hits_fixed | 0.33 | 0.00 | 0.67 | 1.0000 |
| agent qwen3:32b, no surrogate (same day) | similarity | hits_per_100_relaxations | 11.11 | 3.01 | 0.33 | 0.2727 |
| agent qwen3:32b, no surrogate (same day) | similarity | hits | 0.33 | 2.00 | 0.02 | 0.0121 |
| agent qwen3:32b, no surrogate (same day) | similarity | relaxations | 4.67 | 66.12 | 0.00 | 0.0061 |
| agent qwen3:32b, no surrogate (same day) | similarity | robust_hits | 0.00 | 0.88 | 0.06 | 0.0242 |
| agent qwen3:32b, no surrogate (same day) | similarity | hits_hullfix | 0.00 | 0.00 | 0.50 | 1.0000 |
| agent qwen3:32b, no surrogate (same day) | similarity | hits_fixed | 0.00 | 0.88 | 0.06 | 0.0242 |
| agent Sonnet 5.5, no surrogate | agent Sonnet 5.5, + rank_by_surrogate | hits_per_100_relaxations | 18.05 | 12.38 | 0.96 | 0.0159 |
| agent Sonnet 5.5, no surrogate | agent Sonnet 5.5, + rank_by_surrogate | hits | 16.40 | 11.00 | 0.94 | 0.0238 |
| agent Sonnet 5.5, no surrogate | agent Sonnet 5.5, + rank_by_surrogate | relaxations | 90.80 | 88.40 | 0.54 | 0.6429 |
| agent Sonnet 5.5, no surrogate | agent Sonnet 5.5, + rank_by_surrogate | robust_hits | 4.40 | 3.00 | 0.86 | 0.1825 |
| agent Sonnet 5.5, no surrogate | agent Sonnet 5.5, + rank_by_surrogate | hits_hullfix | 0.80 | 0.20 | 0.80 | 0.2063 |
| agent Sonnet 5.5, no surrogate | agent Sonnet 5.5, + rank_by_surrogate | hits_fixed | 7.40 | 4.60 | 0.82 | 0.0952 |
| agent Sonnet 5.5, + surrogate, no critic | agent Sonnet 5.5, + rank_by_surrogate | hits_per_100_relaxations | 16.48 | 12.38 | 0.87 | 0.0714 |
| agent Sonnet 5.5, + surrogate, no critic | agent Sonnet 5.5, + rank_by_surrogate | hits | 15.00 | 11.00 | 0.87 | 0.1071 |
| agent Sonnet 5.5, + surrogate, no critic | agent Sonnet 5.5, + rank_by_surrogate | relaxations | 90.67 | 88.40 | 0.53 | 0.7500 |
| agent Sonnet 5.5, + surrogate, no critic | agent Sonnet 5.5, + rank_by_surrogate | robust_hits | 4.33 | 3.00 | 0.77 | 0.4107 |
| agent Sonnet 5.5, + surrogate, no critic | agent Sonnet 5.5, + rank_by_surrogate | hits_hullfix | 0.33 | 0.20 | 0.57 | 1.0000 |
| agent Sonnet 5.5, + surrogate, no critic | agent Sonnet 5.5, + rank_by_surrogate | hits_fixed | 6.33 | 4.60 | 0.70 | 0.3929 |
| agent Sonnet 5.5, no surrogate, no critic | agent Sonnet 5.5, no surrogate | hits_per_100_relaxations | 17.44 | 18.05 | 0.40 | 0.7321 |
| agent Sonnet 5.5, no surrogate, no critic | agent Sonnet 5.5, no surrogate | hits | 16.33 | 16.40 | 0.47 | 1.0000 |
| agent Sonnet 5.5, no surrogate, no critic | agent Sonnet 5.5, no surrogate | relaxations | 93.67 | 90.80 | 0.93 | 0.0714 |
| agent Sonnet 5.5, no surrogate, no critic | agent Sonnet 5.5, no surrogate | robust_hits | 3.33 | 4.40 | 0.40 | 0.4643 |
| agent Sonnet 5.5, no surrogate, no critic | agent Sonnet 5.5, no surrogate | hits_hullfix | 0.00 | 0.80 | 0.10 | 0.1429 |
| agent Sonnet 5.5, no surrogate, no critic | agent Sonnet 5.5, no surrogate | hits_fixed | 6.33 | 7.40 | 0.13 | 0.2679 |
| agent Sonnet 5.5, no surrogate, no critic | agent Sonnet 5.5, + surrogate, no critic | hits_per_100_relaxations | 17.44 | 16.48 | 0.67 | 0.6000 |
| agent Sonnet 5.5, no surrogate, no critic | agent Sonnet 5.5, + surrogate, no critic | hits | 16.33 | 15.00 | 0.78 | 0.5000 |
| agent Sonnet 5.5, no surrogate, no critic | agent Sonnet 5.5, + surrogate, no critic | relaxations | 93.67 | 90.67 | 0.83 | 0.3000 |
| agent Sonnet 5.5, no surrogate, no critic | agent Sonnet 5.5, + surrogate, no critic | robust_hits | 3.33 | 4.33 | 0.39 | 1.0000 |
| agent Sonnet 5.5, no surrogate, no critic | agent Sonnet 5.5, + surrogate, no critic | hits_hullfix | 0.00 | 0.33 | 0.33 | 1.0000 |
| agent Sonnet 5.5, no surrogate, no critic | agent Sonnet 5.5, + surrogate, no critic | hits_fixed | 6.33 | 6.33 | 0.56 | 1.0000 |
| agent Sonnet 5.5, no surrogate | similarity | hits_per_100_relaxations | 18.05 | 3.01 | 1.00 | 0.0008 |
| agent Sonnet 5.5, no surrogate | similarity | hits | 16.40 | 2.00 | 1.00 | 0.0008 |
| agent Sonnet 5.5, no surrogate | similarity | relaxations | 90.80 | 66.12 | 1.00 | 0.0008 |
| agent Sonnet 5.5, no surrogate | similarity | robust_hits | 4.40 | 0.88 | 1.00 | 0.0008 |
| agent Sonnet 5.5, no surrogate | similarity | hits_hullfix | 0.80 | 0.00 | 0.90 | 0.0070 |
| agent Sonnet 5.5, no surrogate | similarity | hits_fixed | 7.40 | 0.88 | 1.00 | 0.0008 |
| agent Sonnet 5.5, + rank_by_surrogate | similarity | hits_per_100_relaxations | 12.38 | 3.01 | 1.00 | 0.0008 |
| agent Sonnet 5.5, + rank_by_surrogate | similarity | hits | 11.00 | 2.00 | 1.00 | 0.0008 |
| agent Sonnet 5.5, + rank_by_surrogate | similarity | relaxations | 88.40 | 66.12 | 0.99 | 0.0016 |
| agent Sonnet 5.5, + rank_by_surrogate | similarity | robust_hits | 3.00 | 0.88 | 0.91 | 0.0062 |
| agent Sonnet 5.5, + rank_by_surrogate | similarity | hits_hullfix | 0.20 | 0.00 | 0.60 | 0.3846 |
| agent Sonnet 5.5, + rank_by_surrogate | similarity | hits_fixed | 4.60 | 0.88 | 1.00 | 0.0008 |
| agent qwen3:32b, no surrogate (July) | similarity | hits_per_100_relaxations | 32.01 | 3.01 | 1.00 | 0.0061 |
| agent qwen3:32b, no surrogate (July) | similarity | hits | 2.67 | 2.00 | 0.67 | 0.3939 |
| agent qwen3:32b, no surrogate (July) | similarity | relaxations | 9.33 | 66.12 | 0.00 | 0.0061 |
| agent qwen3:32b, no surrogate (July) | similarity | robust_hits | 0.33 | 0.88 | 0.23 | 0.1515 |
| agent qwen3:32b, no surrogate (July) | similarity | hits_hullfix | 0.00 | 0.00 | 0.50 | 1.0000 |
| agent qwen3:32b, no surrogate (July) | similarity | hits_fixed | 0.33 | 0.88 | 0.23 | 0.1515 |
| bayesopt | random | hits_per_100_relaxations | 1.68 | 1.38 | 0.47 | 0.6909 |
| bayesopt | random | hits | 1.50 | 1.00 | 0.59 | 0.5469 |
| bayesopt | random | relaxations | 86.75 | 75.12 | 0.91 | 0.0056 |
| bayesopt | random | robust_hits | 0.25 | 0.50 | 0.42 | 0.7128 |
| bayesopt | random | hits_hullfix | 0.12 | 0.00 | 0.56 | 1.0000 |
| bayesopt | random | hits_fixed | 0.62 | 0.62 | 0.57 | 1.0000 |
| similarity | bayesopt | hits_per_100_relaxations | 3.01 | 1.68 | 0.78 | 0.0454 |
| similarity | bayesopt | hits | 2.00 | 1.50 | 0.67 | 0.4965 |
| similarity | bayesopt | relaxations | 66.12 | 86.75 | 0.00 | 0.0002 |
| similarity | bayesopt | robust_hits | 0.88 | 0.25 | 0.81 | 0.0406 |
| similarity | bayesopt | hits_hullfix | 0.00 | 0.12 | 0.44 | 1.0000 |
| similarity | bayesopt | hits_fixed | 0.88 | 0.62 | 0.63 | 0.6737 |
| agent Opus 5.5, no surrogate | agent Sonnet 5.5, no surrogate | hits_per_100_relaxations | 18.84 | 18.05 | 0.53 | 0.8036 |
| agent Opus 5.5, no surrogate | agent Sonnet 5.5, no surrogate | hits | 18.67 | 16.40 | 0.63 | 0.4821 |
| agent Opus 5.5, no surrogate | agent Sonnet 5.5, no surrogate | relaxations | 99.00 | 90.80 | 1.00 | 0.0179 |
| agent Opus 5.5, no surrogate | agent Sonnet 5.5, no surrogate | robust_hits | 4.33 | 4.40 | 0.43 | 1.0000 |
| agent Opus 5.5, no surrogate | agent Sonnet 5.5, no surrogate | hits_hullfix | 0.33 | 0.80 | 0.27 | 0.4643 |
| agent Opus 5.5, no surrogate | agent Sonnet 5.5, no surrogate | hits_fixed | 11.00 | 7.40 | 0.97 | 0.0357 |

## Critic audit (vetoes checked against relaxations of the same composition in any other run of this study)

| arm | vetoes | vetoed compositions relaxed elsewhere | of those, hits |
|---|---|---|---|
| agent qwen3:32b, no surrogate (July) | 7 | 7 | 0 |
| agent qwen3:32b, no surrogate (same day) | 4 | 3 | 0 |
| agent qwen3:32b, + rank_by_surrogate (same day) | 5 | 2 | 0 |
| agent Sonnet 5.5, no surrogate | 24 | 22 | 2 |
| agent Sonnet 5.5, + rank_by_surrogate | 59 | 41 | 3 |
| agent Opus 5.5, no surrogate | 23 | 10 | 1 |
