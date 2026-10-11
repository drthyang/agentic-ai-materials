# Campaign report: pv-absorber-v1

## Executive summary

The campaign ran 5 iterations and scored 91 candidates. Every candidate was novel relative to the Materials Project (MP). The working target window, as used in the notebook, was a band gap of 1.1–1.7 eV with E_hull ≤ 0.05 eV/atom. By that criterion 13 candidates qualify. They fall into three groups:

- **Ag-based quaternary chalcogenides:** 7 compounds, in the Ag₂–(Cd, Zn, Mg, Sr)–(Ge, Sn)–(Se, Te)₄ family.
- **Famatinite-type I₃–V–VI₄ selenides and a sulfide:** 5 compounds, all with E_hull = 0.
- **One alkali bismuth telluride:** KBiTe₂.

The strongest candidates by this screen are CuAg₂AsSe₄ (1.378 eV, hull 0), CuAg₂SbSe₄ (1.457 eV, hull 0) and CdAg₂GeSe₄ (1.279 eV, hull 0). Confidence is low to moderate. All numbers come from CHGNet relaxations and a surrogate band-gap model, with no DFT or experimental validation. "Novel" means only "absent from MP", and no literature novelty check is recorded in the notebook.

## Scored candidates

Columns: E_f is formation energy in eV/atom. E_hull is energy above hull in eV/atom. Gap is the HSE-fidelity predicted gap in eV. "Hit" means gap 1.1–1.7 eV and E_hull ≤ 0.05. Iteration 4 and 5 formulas are as recorded in the database. All 91 entries converged and are flagged novel.

### Iteration 1 (20 scored)
| Formula | E_f | E_hull | Gap | Hit |
|---|---|---|---|---|
| CdAg2GeSe4 | -0.657 | 0.000 | 1.279 | ✔ |
| ZrCd(AgSe2)2 | -1.148 | 0.000 | 0.295 | |
| ZnAg2GeSe4 | -0.681 | 0.000 | 1.119 | ✔ |
| MgAg2SnS4 | -1.177 | 0.002 | 1.871 | |
| MgAg2SnSe4 | -0.838 | 0.016 | 1.588 | ✔ |
| CdAg2GeTe4 | -0.326 | 0.017 | 0.481 | |
| MgAg2GeS4 | -1.165 | 0.017 | 1.893 | |
| MgAg2GeSe4 | -0.797 | 0.020 | 1.856 | |
| MgAg2GeTe4 | -0.423 | 0.025 | 1.490 | ✔ |
| CdAg2SnTe4 | -0.366 | 0.027 | 0.412 | |
| ZnAg2GeTe4 | -0.318 | 0.028 | 1.171 | ✔ |
| MgAg2SnTe4 | -0.461 | 0.038 | 1.172 | ✔ |
| ZnAg2SnTe4 | -0.358 | 0.039 | 0.596 | |
| CaAg2GeSe4 | -0.949 | 0.062 | 1.679 | |
| CdSi(AgTe2)2 | -0.230 | 0.083 | 1.055 | |
| CdSi(AgSe2)2 | -0.568 | 0.130 | 1.714 | |
| MgSi(AgSe2)2 | -0.715 | 0.145 | 2.348 | |
| CaSi(AgSe2)2 | -0.867 | 0.187 | 2.510 | |
| MgZr(AgSe2)2 | -0.720 | 0.459 | 1.579 | |
| CaZr(AgSe2)2 | -0.882 | 0.493 | 2.471 | |

### Iteration 2 (20 scored)
| Formula | E_f | E_hull | Gap | Hit |
|---|---|---|---|---|
| SrAg2SnSe4 | -1.059 | 0.000 | 1.701 | (just above window) |
| BaAg2GeTe4 | -0.704 | 0.000 | 0.705 | |
| SrCu2SnTe4 | -0.751 | 0.000 | 0.867 | |
| SrAg2GeSe4 | -1.021 | 0.003 | 1.687 | ✔ |
| SrAg2GeTe4 | -0.651 | 0.016 | 0.155 | |
| SrAg2SnTe4 | -0.689 | 0.029 | 0.100 | |
| BaCu2GeTe4 | -0.672 | 0.034 | 0.499 | |
| SrCu2SnSe4 | -1.045 | 0.050 | 1.109 | (borderline; hull 0.0504) |
| CaAg2SnSe4 | -0.998 | 0.051 | 1.816 | |
| MgCu2SnSe4 | -0.819 | 0.071 | 1.383 | |
| CaAg2SnTe4 | -0.625 | 0.072 | 0.062 | |
| SrCu2GeTe4 | -0.614 | 0.078 | 0.161 | |
| MgCu2GeTe4 | -0.372 | 0.101 | 0.895 | |
| MnCu2GeSe4 | -0.531 | 0.104 | 0.931 | |
| CaCu2SnSe4 | -0.979 | 0.108 | 0.944 | |
| MgCu2SnTe4 | -0.409 | 0.109 | 0.483 | |
| CaCu2GeTe4 | -0.554 | 0.116 | 0.034 | |
| CaCu2SnTe4 | -0.595 | 0.120 | 0.024 | |
| CaCu2GeSe4 | -0.928 | 0.121 | 1.198 | |
| MgCu2GeSe4 | -0.717 | 0.136 | 1.102 | |

### Iteration 3 (20 scored, no hits)
| Formula | E_f | E_hull | Gap | Hit |
|---|---|---|---|---|
| K2BaSnSe4 | -1.627 | 0.000 | 2.723 | |
| SrAg2SnS4 | -1.369 | 0.000 | 1.720 | (just above window) |
| K2SrSnSe4 | -1.541 | 0.005 | 2.388 | |
| SrAg2GeS4 | -1.354 | 0.013 | 1.867 | |
| BaNa2SnSe4 | -1.421 | 0.058 | 1.932 | |
| BaNa2GeSe4 | -1.397 | 0.058 | 2.368 | |
| Na2SrSnSe4 | -1.369 | 0.099 | 1.745 | |
| Na2SrGeSe4 | -1.345 | 0.100 | 2.164 | |
| BaTi(AgSe2)2 | -0.997 | 0.312 | 2.397 | |
| Na2SrTiSe4 | -1.371 | 0.346 | 2.808 | |
| K2BaZrSe4 | -1.430 | 0.350 | 2.651 | |
| K2SrZrSe4 | -1.417 | 0.353 | 2.315 | |
| TiZn(AgSe2)2 | -0.617 | 0.353 | 2.229 | |
| K2SrTiSe4 | -1.337 | 0.360 | 2.415 | |
| SrTi(AgSe2)2 | -0.938 | 0.373 | 2.357 | |
| BaZr(AgSe2)2 | -0.989 | 0.405 | 2.173 | |
| BaNa2TiSe4 | -1.305 | 0.409 | 2.840 | |
| BaNa2ZrSe4 | -1.263 | 0.565 | 2.433 | |
| K2BaTiSe4 | -1.120 | 0.575 | 2.897 | |
| Na2SrZrSe4 | -1.199 | 0.631 | 2.483 | |

### Iteration 4 (20 scored)
| Formula | E_f | E_hull | Gap | Hit |
|---|---|---|---|---|
| Ag3SbS4 | -0.856 | 0.000 | 1.791 | |
| Ag3SbSe4 | -0.573 | 0.000 | 1.665 | ✔ |
| Ag3AsSe4 | -0.541 | 0.000 | 1.681 | ✔ |
| Cu2AgSbS4 | -0.855 | 0.000 | 1.738 | |
| Cu2AgSbSe4 | -0.523 | 0.000 | 0.425 | |
| CuAg2SbS4 | -0.856 | 0.000 | 1.862 | |
| CuAg2SbSe4 | -0.565 | 0.000 | 1.457 | ✔ |
| Cu2AgAsS4 | -0.824 | 0.000 | 1.869 | |
| Cu2AgAsSe4 | -0.483 | 0.000 | 0.436 | |
| CuAg2AsS4 | -0.828 | 0.000 | 1.974 | |
| CuAg2AsSe4 | -0.530 | 0.000 | 1.378 | ✔ |
| Cu2AgBiS4 | -0.888 | 0.000 | 1.587 | ✔ |
| Cu2AgBiSe4 | -0.531 | 0.009 | 0.957 | |
| MgCu2SnS4 | -1.239 | 0.020 | 2.174 | |
| CuAg2PS4 | -0.830 | 0.020 | 2.448 | |
| Cu2AgPSe4 | -0.425 | 0.045 | 2.139 | |
| CoAg2SnSe4 | -0.569 | 0.056 | 0.603 | |
| FeAg2SnSe4 | -0.579 | 0.072 | -0.003 | |
| CoAg2GeSe4 | -0.524 | 0.075 | 0.809 | |
| FeAg2GeSe4 | -0.525 | 0.078 | 0.018 | |

### Iteration 5 (11 scored)
| Formula | E_f | E_hull | Gap | Hit |
|---|---|---|---|---|
| KSbTe2 | -0.741 | 0.000 | 0.547 | |
| CuAg2SbTe4 | -0.279 | 0.000 | 0.314 | |
| KGaSe2 | -1.275 | 0.000 | 2.177 | |
| NaGaS2 | -1.810 | 0.000 | 3.827 | |
| KAsS2 | -1.409 | 0.000 | 2.450 | |
| Cu3SbTe4 | -0.251 | 0.001 | 0.322 | |
| KBiTe2 | -0.736 | 0.003 | 1.296 | ✔ |
| NaGaSe2 | -1.169 | 0.017 | 2.202 | |
| CaAg2SnS4 | -1.297 | 0.068 | 2.279 | |
| Cu2AgBiTe4 | -0.217 | 0.073 | 0.442 | |
| CaAg2GeS4 | -1.273 | 0.094 | 2.148 | |

## Hypotheses tested and what was learned

**Iteration 1: kesterite analogs.**
- Hypothesis: cation and anion substitution in Cu₂ZnSnS₄ (Ag for Cu; Cd, Mg for Zn; Ge, Si for Sn; Se/Te for S) keeps the gap in 1.1–1.7 eV and stays near the hull.
- Result: 6 hits. These were CdAg₂GeSe₄, ZnAg₂GeSe₄, MgAg₂GeTe₄, MgAg₂SnSe₄, MgAg₂SnTe₄ and ZnAg₂GeTe₄.
- Si on the IV site was strongly unstable (hull 0.08–0.19). Zr on that site was also unstable for Mg/Ca (hull 0.46–0.49), while ZrCd(AgSe₂)₂ had hull 0 but a 0.30 eV gap.
- Trends: Se→Te lowers the gap by roughly 0.4–0.7 eV, Mg and Ca raise it, and sulfides sit near 1.9 eV (too wide).
- The chalcopyrite prototype returned only already-known compounds, so those proposals were skipped.

**Iteration 2: gap tuning with Cu and larger II-site cations.**
- Result: 1 clear hit, SrAg₂GeSe₄ (1.687 eV, hull 0.003).
- SrAg₂SnSe₄ (1.701 eV, hull 0) sits just above the window. SrCu₂SnSe₄ (1.109 eV, hull 0.0504) sits just outside the hull cutoff.
- Cu analogs with Mg, Ca or Mn on the II site were unstable (hull 0.07–0.14).
- Sr/Ba tellurides were too narrow (0.02–0.9 eV).
- Cu lowers the gap by about 0.6 eV relative to Ag.

**Iteration 3: alkali/alkaline-earth and Ti/Zr variants. Falsified.**
- Zero hits.
- Ti/Zr variants had hull 0.3–0.6 eV/atom.
- K₂BaSnSe₄ and K₂SrSnSe₄ were stable but too wide (2.72 and 2.39 eV).
- SrAg₂SnS₄ (1.72 eV, hull 0) and SrAg₂GeS₄ (1.87 eV, hull 0.013) show little S/Se gap sensitivity in the Sr–Ag series.
- The notebook's own reflection says the wide gaps and Ti/Zr instability should have been anticipated.

**Iteration 4: famatinite-type I₃–V–VI₄.**
- The notebook holds only the reflection for this iteration. The hypotheses recorded in the database describe it as Ag-for-Cu analogs of Cu₃SbSe₄ with Sb/Bi/As/P and S/Se.
- Result: 5 new hits, all with hull 0 (Cu₂AgBiS₄ is the lowest-E_f of them): CuAg₂AsSe₄ (1.378 eV), CuAg₂SbSe₄ (1.457), Cu₂AgBiS₄ (1.587), Ag₃SbSe₄ (1.665) and Ag₃AsSe₄ (1.681).
- Trends: more Ag widens the gap, and selenides are narrower than sulfides. Cu-rich selenides were too narrow (Cu₂AgSbSe₄ 0.43 eV, Cu₂AgAsSe₄ 0.44 eV).
- The P variants were wide (2.1–2.4 eV). The Fe/Co II-site Ag selenides failed (hull 0.056–0.078, gaps ≈0–0.8 eV).
- The zincblende prototype produced only binaries.

**Iteration 5: fill remaining famatinite and I–III–VI₂ neighbors.**
- Only 11 candidates were scored, because many proposals were rejected as already seen (26 filtered out of 56 proposed). The notebook calls the kesterite/famatinite space "nearly exhausted" and says about 9 budget units were wasted.
- One hit: KBiTe₂ (1.296 eV, hull 0.003).
- Te famatinites were too narrow (0.31–0.44 eV). K/Na-Ga-Se₂/S₂ and KAsS₂ were stable but too wide (2.2–3.8 eV). KSbTe₂ was stable but narrow (0.55 eV).

**Overall.** The productive veins were Ag₂-(Cd, Zn, Mg, Sr)-(Ge, Sn)-(Se, Te)₄ and Ag/Cu-(As, Sb, Bi)-chalcogenide famatinites. Alkali, Ti, Zr, Si, Fe/Co and Cu-with-Mg/Ca/Mn variants were unproductive.

## Caveats

- **Level of theory.** Stability comes from CHGNet relaxations and gaps from an HSE-fidelity surrogate. Neither has been checked against explicit DFT in this campaign. A hull of 0.000 may partly reflect an incomplete set of competing phases in the reference hull.
- **Gap accuracy.** Gap errors for ML models are typically a few tenths of an eV, and that is not quantified here. Many hits sit near the window edges, for example 1.665 and 1.681 eV against the 1.7 eV cutoff, and CdAg₂GeSe₄ at 1.28 eV. The window assignment is therefore fragile.
- **Structure assumptions.** Candidates were generated on kesterite or famatinite frames. The notebook notes that some Sr/Ba compounds relaxed to non-kesterite structures, so actual ground-state structures were not mapped.
- **Novelty.** "Novel" means absent from MP only. No literature check of the hits is recorded in the notebook, so some may exist in the literature (for example, alkali bismuth tellurides). The surrogate ranking tool was not recorded as used.
- **Missing properties.** Nothing was assessed beyond gap and hull: no band alignment, defect tolerance, absorption coefficient, toxicity or cost. Ag and Te content and Sb/Bi/As content are practical concerns.
- **Coverage.** The iteration 4 notebook entries are reflection-only, and iteration 5 is thin (11 scored).

## Recommended next steps

1. Validate the top hits with explicit DFT (HSE or GW gaps, phonons, a full competing-phase hull). The priority list is CuAg₂AsSe₄, CuAg₂SbSe₄, CdAg₂GeSe₄, ZnAg₂GeSe₄, KBiTe₂, Cu₂AgBiS₄, Ag₃SbSe₄, Ag₃AsSe₄ and SrAg₂GeSe₄.
2. Run a literature and ICSD novelty check on the hits, since novelty here is only relative to MP.
3. Test structural polymorph competition for the Sr/Ba compounds.
4. Fine-tune gaps in the near-window compounds (SrAg₂SnSe₄ 1.70 eV, SrAg₂SnS₄ 1.72 eV, SrCu₂SnSe₄ 1.11 eV, Cu₂AgSbS₄ 1.74 eV), by mixed anion or Cu/Ag alloying if tooling allows.
5. Expand the alkali/Ag/Cu–Bi/Sb–chalcogenide families around KBiTe₂ (Na/K/Rb, Se/Te mixes), since the kesterite and famatinite spaces appear largely exhausted under the current prototype tooling.
6. If synthesis is considered, start with the stable Se famatinites and the Cd/Zn-Ag-Ge-Se phases.
