# Campaign report: pv-absorber-v1

## Executive summary

Over five iterations the campaign scored 85 kesterite-type compositions. All 85 were flagged novel relative to Materials Project, and the relaxations and gap predictions were run with CHGNet and an HSE-fidelity gap model. The stated target was a PV-type gap, roughly 1.4 eV; the notebook used about 1.1–1.7 eV as its working window. Eleven compositions fall in that window with E_hull ≤ ~0.02 eV/atom. The most promising are CdAg2GeSe4 (1.28 eV, on hull), TiMnAg2S4 (1.48 eV, on hull), TiZnAg2S4 (1.55 eV, on hull) and TiCu2NiS4 (1.60 eV, on hull). Confidence is moderate to low. These are single-method computational predictions with no DFT cross-check or experimental validation, and the Ti/Mn/Ni d-state results are the least trustworthy. The kesterite prototype space accessible to the tool appears largely exhausted, and later iterations produced diminishing returns.

## Scored candidates

Columns: formation energy per atom (E_f, eV), energy above hull (E_hull, eV/atom) and predicted band gap (Eg, eV). Values are rounded. Rows are grouped by iteration in the order recorded in the campaign database.

### Iteration 1 (10 scored)
| Formula | E_f | E_hull | Eg |
|---|---|---|---|
| CdAg2GeSe4 | -0.657 | 0.000 | 1.28 |
| ZnAg2GeSe4 | -0.681 | 0.000 | 1.12 |
| MgAg2SnS4 | -1.177 | 0.002 | 1.87 |
| MgAg2SnSe4 | -0.838 | 0.016 | 1.59 |
| CdAg2GeTe4 | -0.326 | 0.017 | 0.48 |
| MgAg2GeS4 | -1.165 | 0.017 | 1.89 |
| MgCu2SnS4 | -1.239 | 0.020 | 2.17 |
| MgAg2GeSe4 | -0.797 | 0.020 | 1.86 |
| MgCu2SnSe4 | -0.819 | 0.071 | 1.38 |
| MgCu2GeSe4 | -0.717 | 0.136 | 1.10 |

### Iteration 2 (20 scored)
| Formula | E_f | E_hull | Eg |
|---|---|---|---|
| SrAg2SnSe4 | -1.059 | 0.000 | 1.70 |
| SrAg2SnS4 | -1.369 | 0.000 | 1.72 |
| NiAg2SnSe4 | -0.631 | 0.000 | 1.68 |
| NiAg2SnS4 | -0.936 | 0.000 | 1.90 |
| NiAg2GeSe4 | -0.583 | 0.0005 | 1.65 |
| SrAg2GeSe4 | -1.021 | 0.003 | 1.69 |
| NiAg2GeS4 | -0.911 | 0.008 | 1.74 |
| SrAg2GeS4 | -1.354 | 0.013 | 1.87 |
| CaAg2SnSe4 | -0.998 | 0.051 | 1.82 |
| CoAg2SnSe4 | -0.569 | 0.056 | 0.60 |
| CaAg2GeSe4 | -0.949 | 0.062 | 1.68 |
| CaAg2SnS4 | -1.297 | 0.068 | 2.28 |
| FeAg2SnSe4 | -0.579 | 0.072 | ~0.00 |
| CoAg2GeSe4 | -0.524 | 0.075 | 0.81 |
| FeAg2GeSe4 | -0.525 | 0.078 | 0.02 |
| MnAg2GeS4 | -0.914 | 0.079 | 2.24 |
| CoAg2SnS4 | -0.860 | 0.092 | 1.39 |
| CaAg2GeS4 | -1.273 | 0.094 | 2.15 |
| CoAg2GeS4 | -0.835 | 0.113 | 1.51 |
| FeAg2GeS4 | -0.851 | 0.135 | 0.01 |

### Iteration 3 (20 scored)
| Formula | E_f | E_hull | Eg |
|---|---|---|---|
| BaAg2GeTe4 | -0.704 | 0.000 | 0.70 |
| SrCu2SnTe4 | -0.751 | 0.000 | 0.87 |
| BaCu2SnTe4 | -0.754 | 0.000 | 0.14 |
| TiCu2NiS4 | -1.528 | 0.000 | 1.60 |
| BaAg2SnTe4 | -0.746 | 0.007 | 0.52 |
| Cu2NiGeS4 | -0.979 | 0.013 | 1.12 |
| SrAg2GeTe4 | -0.651 | 0.016 | 0.16 |
| CdAg2SnTe4 | -0.366 | 0.027 | 0.41 |
| SrAg2SnTe4 | -0.689 | 0.029 | 0.10 |
| BaCu2GeTe4 | -0.672 | 0.034 | 0.50 |
| NiAg2GeTe4 | -0.281 | 0.036 | 0.13 |
| Cu2NiGeSe4 | -0.577 | 0.041 | 0.25 |
| NiAg2SnTe4 | -0.323 | 0.045 | 0.04 |
| SrCu2SnSe4 | -1.045 | 0.050 | 1.11 |
| Cu2NiSnTe4 | -0.288 | 0.076 | 0.14 |
| SrCu2GeTe4 | -0.614 | 0.078 | 0.16 |
| Cu2SiNiSe4 | -0.479 | 0.167 | 0.19 |
| TiNi(AgSe2)2 | -0.504 | 0.374 | 2.25 |
| TiCu2NiSe4 | -0.496 | 0.390 | 2.15 |
| TiNi(AgS2)2 | -0.815 | 0.441 | 0.07 |

### Iteration 4 (18 scored)
| Formula | E_f | E_hull | Eg |
|---|---|---|---|
| TiCd(CuS2)2 | -1.514 | 0.000 | 2.86 |
| MgTi(CuS2)2 | -1.700 | 0.000 | 2.93 |
| TiMn(CuS2)2 | -1.566 | 0.000 | 2.26 |
| ZrZn(CuS2)2 | -1.556 | 0.000 | 0.30 |
| TiMn(AgS2)2 (TiMnAg2S4) | -1.513 | 0.000 | 1.48 |
| TiZn(AgS2)2 (TiZnAg2S4) | -1.547 | 0.000 | 1.55 |
| ZrZn(AgS2)2 | -1.543 | 0.000 | 0.19 |
| ZrMn(AgS2)2 | -1.502 | 0.000 | 0.18 |
| BaZr(CuS2)2 | -1.598 | 0.226 | 0.07 |
| CaTi(CuS2)2 | -1.517 | 0.252 | 0.99 |
| SrZr(CuS2)2 | -1.548 | 0.256 | 0.36 |
| CaZr(CuS2)2 | -1.498 | 0.305 | 0.31 |
| BaTi(CuS2)2 | -1.454 | 0.332 | 0.22 |
| TiCd(AgS2)2 | -0.957 | 0.351 | 2.40 |
| MgTi(AgS2)2 | -1.143 | 0.364 | 1.95 |
| SrTi(CuS2)2 | -1.380 | 0.387 | 0.14 |
| BaZr(AgSe2)2 | -0.989 | 0.405 | 2.17 |
| SrZr(AgSe2)2 | -0.944 | 0.440 | 2.33 |

### Iteration 5 (17 scored)
| Formula | E_f | E_hull | Eg |
|---|---|---|---|
| ZrMn(AgSe2)2 | -1.127 | 0.000 | ~0.00 |
| ZrCd(AgSe2)2 | -1.148 | 0.000 | 0.30 |
| ZrZn(AgSe2)2 | -1.183 | 0.000 | 0.65 |
| ZrCd(CuSe2)2 | -1.141 | 0.000 | 0.15 |
| ZrZn(CuSe2)2 | -1.188 | 0.000 | 0.21 |
| MgZr(CuSe2)2 | -1.276 | 0.000 | 0.07 |
| MgZr(AgS2)2 | -1.666 | 0.000 | 0.33 |
| TiZn(AgSe2)2 | -0.617 | 0.353 | 2.23 |
| TiCd(AgSe2)2 | -0.590 | 0.357 | 2.35 |
| MgTi(AgSe2)2 | -0.725 | 0.380 | 2.43 |
| TiMn(AgSe2)2 | -0.492 | 0.395 | 2.21 |
| TiZn(CuSe2)2 | -0.573 | 0.412 | 2.84 |
| MgTi(CuSe2)2 | -0.677 | 0.443 | 2.71 |
| ZrCd(AgS2)2 | -0.946 | 0.451 | 2.36 |
| MgZr(AgSe2)2 | -0.720 | 0.459 | 1.58 |
| TiMn(CuSe2)2 | -0.437 | 0.465 | 2.45 |
| TiCd(CuSe2)2 | -0.487 | 0.479 | 2.80 |

### Shortlist: Eg ≈ 1.1–1.7 eV and E_hull ≤ ~0.02 eV/atom
CdAg2GeSe4 (1.28 / 0.000), ZnAg2GeSe4 (1.12 / 0.000), TiMnAg2S4 (1.48 / 0.000), TiZnAg2S4 (1.55 / 0.000), TiCu2NiS4 (1.60 / 0.000), MgAg2SnSe4 (1.59 / 0.016), Cu2NiGeS4 (1.12 / 0.013), NiAg2GeSe4 (1.65 / 0.0005), NiAg2SnSe4 (1.68 / 0.000), SrAg2GeSe4 (1.69 / 0.003) and SrAg2SnSe4 (1.70 / 0.000).

SrAg2SnS4 (1.72 eV) and NiAg2GeS4 (1.74 eV) are stable but sit slightly above the window.

## Hypotheses tested and what was learned

**Iteration 1: Ag/Cd/Zn/Mg/Ge/Sn/Se isoelectronic substitutions in kesterite Cu2ZnSnS4.**
- Hypothesis held. The Ag–Ge–Se compounds are on the hull with gaps of 1.1–1.3 eV.
- S→Se lowers the gap by about 0.3–0.5 eV, and Se→Te lowers it by about 0.8 eV.
- Mg raises the gap relative to Zn/Cd.
- Mg combined with Cu is unstable in the selenides (E_hull 0.07–0.14).
- Si variants were vetoed by the critic for radius mismatch.

**Iteration 2: chalcopyrite, then divalent-site expansion.**
- The chalcopyrite proposals were all already in Materials Project, apart from CuBiTe2, which was not evaluated. The campaign therefore switched to kesterite divalent-site expansion.
- Sr and Ni gave stable Ag chalcogenides with gaps of about 1.65–1.9 eV, at or above the top of the window.
- Fe and Co gave closed or low gaps and were unstable, except CoAg2SnS4 and CoAg2GeS4, which have in-window gaps but E_hull of 0.09–0.11.
- Ca analogues are weakly unstable (E_hull 0.05–0.09).
- MnAg2GeS4 is unstable (E_hull 0.079) with a wide gap (2.24 eV).

**Iteration 3: lower the gap using Ba, Cu and Te.**
- Tellurides were mostly stable or near-stable but have gaps of 0.04–0.87 eV, which is too low.
- Cu2NiGeS4 (1.12 eV, E_hull 0.013) and TiCu2NiS4 (1.60 eV, E_hull 0.000) were new hits.
- SrCu2SnSe4 (1.11 eV, E_hull 0.050) is borderline.
- Ti–Se/Ag versions were very unstable (E_hull 0.37–0.44).
- The zincblende prototype returned only known binaries.
- Zr and Si variants were vetoed for size mismatch.

**Iteration 4: Ti4+/Zr4+ with Cu/Ag sulfides.**
- TiMnAg2S4 (1.48 eV) and TiZnAg2S4 (1.55 eV) are on the hull.
- Ti–Cu sulfides with Cd, Mg or Mn are stable but have wide gaps of 2.3–2.9 eV.
- Zr–Zn/Mn Ag and Cu sulfides are stable but have gaps of about 0.2–0.3 eV.
- Sr, Ba and Ca combined with Ti or Zr and Cu are unstable (E_hull 0.23–0.39).
- Ti–Ag with Cd or Mg is unstable.
- Two candidates were vetoed for charge imbalance. The notebook records about 20 evaluated, but the database holds 18 scored entries; this report uses the database.

**Iteration 5: extend the Ti/Zr chalcogenide hits to selenides and other divalent ions.**
- Hypothesis falsified for the selenides. Zr selenides are on the hull but have gaps of 0–0.65 eV.
- Ti selenides are unstable (E_hull 0.35–0.48).
- MgZr(AgSe2)2 has an in-window gap (1.58 eV) but E_hull of 0.46.
- No new stable in-window hits appeared.
- Two Ba + Ti/Zr + Cu–Se candidates were vetoed for size mismatch.
- The surrogate was uninformative in this region.
- Three relaxations went unspent.

## Caveats

- **Single-method predictions.** All energies come from CHGNet relaxations. Gaps are model-predicted "HSE-fidelity" values. The notebook itself flags the fidelity of CHGNet-based gaps as limited, especially for Ti/Mn/Ni d-states. Gaps near 0 eV for Fe, Co and Zr-based compounds may reflect this limitation.
- **Surrogate model.** The GP surrogate had no data in iteration 1 and was judged uninformative in iterations 3–5. It favoured already-known sulfides and was largely ignored. No surrogate error bars are reported.
- **Hull stability.** E_hull values of 0.00–0.02 eV/atom are within typical ML-potential error. The hull is also drawn from Materials Project only. Competing phases that are missing from the database, or that CHGNet handles poorly, could change the stability conclusions.
- **Novelty claim.** "Novel" means absent from Materials Project only. The literature search found nothing directly on the Ti–Ag–M–S or Sr/Ni–Ag–chalcogenide kesterites, but that search was not exhaustive.
- **Structural assumptions.** All structures are substitutions on prototype lattices. Other polymorphs and cation ordering, and whether the actual ground state is kesterite-type at all, were not examined.
- **Optical properties.** Gap type (direct or indirect) and absorption were not assessed.
- **No experiments.** No synthesis or experimental data exist for any candidate.

## Recommended next steps

1. **Independent DFT.** Run hybrid-functional (HSE) or GW calculations with full relaxation, phonons and a thorough competing-phase hull, on the shortlist. Start with CdAg2GeSe4, ZnAg2GeSe4, TiMnAg2S4, TiZnAg2S4 and TiCu2NiS4. Check the magnetic and d-state treatment for Ti, Mn and Ni, including spin and U settings.
2. **Gap tuning by alloying.** Alloying is not available through the prototype tool and needs a custom workflow. Candidates are Zn/Cd mixing on ZnAg2GeSe4/CdAg2GeSe4, mixed S/Se, and Ni/Zn mixing to move Cu2NiGeS4 (1.12 eV) and TiCu2NiS4 (1.60 eV) toward about 1.4 eV.
3. **Avoid dead ends.** The notebook indicates these lines have stalled: Fe and Co on the divalent site, Ca, Ti–Se, Zr–Se (gaps too low), Te compounds (gaps too low), and Mg + Cu selenides.
4. **Experimental screening.** If DFT confirms the shortlist, attempt synthesis of the on-hull Ag–Ge–Se compounds first. They are the simplest chemistries and have the best stability margins.
