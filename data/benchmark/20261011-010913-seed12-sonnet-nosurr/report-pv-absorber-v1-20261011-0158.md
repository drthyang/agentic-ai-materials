# Campaign report: pv-absorber-v1

## Executive summary

The campaign ran 5 iterations. It searched kesterite-type (A₂-M-IV-X₄) quaternary chalcogenides for novel photovoltaic absorbers with band gaps near 1.4 eV. It scored 90 novel, converged candidates.

Using the working window of gap 1.1–1.7 eV and E_hull ≤ 0.05 eV/atom, I count 18 candidates inside it. A 19th, SrCu₂SnSe₄, is borderline: its hull energy is 0.0504. The most promising leads are **K₂CaGeTe₄** (1.42 eV, hull 0.019), **K₂MgSnTe₄** (1.33 eV, hull 0.000), **CdAg₂GeSe₄** (1.28 eV, hull 0.000) and **K₂CdSiTe₄** (1.23 eV, hull 0.000).

Confidence is low to moderate. All numbers come from a surrogate pipeline: CHGNet relaxation and an ML band gap at "HSE fidelity". Stability is measured only against phases in the Materials Project, and the kesterite structure was imposed on every composition. For the K/Na tellurides especially, the real ground-state structures probably differ. No DFT or experimental validation has been done.

## Scored candidates

All candidates are novel versus the Materials Project and all converged. E_f is formation energy in eV/atom, hull is E_above_hull in eV/atom, and gap is in eV. Rows are in database order (grouped by iteration). A ✔ marks candidates inside the window (gap 1.1–1.7 eV, hull ≤ 0.05).

### Iteration 1 (18 scored)
| Formula | E_f | Hull | Gap | In window |
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
| MgCu2SnSe4 | -0.819 | 0.071 | 1.383 | |
| MgCu2GeTe4 | -0.372 | 0.101 | 0.895 | |
| MgCu2SnTe4 | -0.409 | 0.109 | 0.483 | |
| MgCu2GeSe4 | -0.717 | 0.136 | 1.102 | |
| ZrCd(AgS2)2 | -0.946 | 0.451 | 2.364 | |

### Iteration 2 (19 scored)
| Formula | E_f | Hull | Gap | In window |
|---|---|---|---|---|
| SrAg2SnSe4 | -1.059 | 0.000 | 1.701 | (just over) |
| BaAg2GeTe4 | -0.704 | 0.000 | 0.705 | |
| ZrZn(AgSe2)2 | -1.183 | 0.000 | 0.653 | |
| ZrZn(AgTe2)2 | -0.781 | 0.000 | 0.071 | |
| SrAg2GeSe4 | -1.021 | 0.003 | 1.687 | ✔ |
| BaAg2SnTe4 | -0.746 | 0.007 | 0.516 | |
| SrAg2GeTe4 | -0.651 | 0.016 | 0.155 | |
| SrAg2SnTe4 | -0.689 | 0.029 | 0.100 | |
| SrCu2SnSe4 | -1.045 | 0.050 | 1.109 | borderline (hull 0.0504) |
| CoAg2SnSe4 | -0.569 | 0.056 | 0.603 | |
| FeAg2SnSe4 | -0.579 | 0.072 | -0.003 | |
| CoAg2GeSe4 | -0.524 | 0.075 | 0.809 | |
| FeAg2GeSe4 | -0.525 | 0.078 | 0.018 | |
| CoAg2GeTe4 | -0.229 | 0.087 | 0.004 | |
| FeAg2GeTe4 | -0.199 | 0.112 | 0.012 | |
| TiZn(AgSe2)2 | -0.617 | 0.353 | 2.229 | |
| TiCd(AgSe2)2 | -0.590 | 0.357 | 2.354 | |
| SrTi(AgSe2)2 | -0.938 | 0.373 | 2.357 | |
| SrZr(AgSe2)2 | -0.944 | 0.440 | 2.331 | |

### Iteration 3 (20 scored)
| Formula | E_f | Hull | Gap | In window |
|---|---|---|---|---|
| K2ZnSnSe4 | -1.222 | 0.000 | 2.265 | |
| K2ZnGeSe4 | -1.197 | 0.000 | 2.488 | |
| K2CdGeSe4 | -1.169 | 0.000 | 2.409 | |
| K2CdSnTe4 | -0.899 | 0.000 | 0.864 | |
| K2ZnSnTe4 | -1.001 | 0.000 | 1.573 | ✔ |
| K2CdGeTe4 | -0.863 | 0.000 | 0.884 | |
| K2MgSnTe4 | -0.977 | 0.000 | 1.329 | ✔ |
| Na2ZnSnSe4 | -1.121 | 0.007 | 2.292 | |
| Na2ZnGeSe4 | -1.094 | 0.011 | 2.480 | |
| Na2ZnGeTe4 | -0.690 | 0.015 | 2.419 | |
| Na2CdSnSe4 | -1.085 | 0.019 | 1.957 | |
| Na2CdGeTe4 | -0.680 | 0.021 | 1.739 | |
| Na2ZnSnTe4 | -0.712 | 0.023 | 2.053 | |
| Na2CdGeSe4 | -1.052 | 0.029 | 2.413 | |
| K2MgSnSe4 | -1.311 | 0.030 | 2.536 | |
| Na2CdSnTe4 | -0.699 | 0.032 | 1.367 | ✔ |
| Na2MgGeTe4 | -0.759 | 0.047 | 1.136 | ✔ |
| Na2MgGeSe4 | -1.186 | 0.055 | 2.448 | |
| Na2MgSnSe4 | -1.209 | 0.055 | 2.156 | |
| Na2MgSnTe4 | -0.782 | 0.055 | 1.932 | |

### Iteration 4 (19 scored)
| Formula | E_f | Hull | Gap | In window |
|---|---|---|---|---|
| K2BaGeTe4 | -1.187 | 0.000 | 1.566 | ✔ |
| K2MnSnTe4 | -0.932 | 0.000 | 0.646 | |
| Na2CaGeTe4 | -1.098 | 0.000 | 1.731 | (just over) |
| K2BaSiTe4 | -1.122 | 0.000 | 1.642 | ✔ |
| K2MnGeTe4 | -0.709 | 0.002 | 1.100 | (1.0995, just under) |
| K2MgSiTe4 | -0.868 | 0.005 | 1.692 | ✔ |
| K2SrSnTe4 | -1.128 | 0.012 | 1.199 | ✔ |
| K2SrGeTe4 | -1.087 | 0.013 | 1.216 | ✔ |
| K2CaGeTe4 | -1.059 | 0.019 | 1.421 | ✔ |
| K2CaSnTe4 | -1.085 | 0.033 | 1.118 | ✔ |
| Na2MnGeTe4 | -0.588 | 0.043 | 1.088 | (just under) |
| Na2MnSnTe4 | -0.618 | 0.046 | 0.947 | |
| BaNa2GeTe4 | -0.978 | 0.063 | 1.759 | |
| BaNa2SnTe4 | -1.004 | 0.066 | 1.704 | |
| K2CaSiTe4 | -0.972 | 0.098 | 1.455 | |
| K2SrSiTe4 | -0.987 | 0.105 | 1.875 | |
| Na2SrGeTe4 | -0.913 | 0.113 | 1.692 | |
| Na2SrSnTe4 | -0.933 | 0.124 | 1.725 | |
| Na2CaSnTe4 | -0.865 | 0.169 | 1.458 | |

### Iteration 5 (14 scored)
| Formula | E_f | Hull | Gap | In window |
|---|---|---|---|---|
| K2ZnSiTe4 | -0.802 | 0.000 | 2.069 | |
| K2CdSiTe4 | -0.798 | 0.000 | 1.235 | ✔ |
| K2BaSnSe4 | -1.627 | 0.000 | 2.723 | |
| K2BaGeSe4 | -1.594 | 0.000 | 2.477 | |
| K2CdSiSe4 | -1.099 | 0.009 | 2.686 | |
| CaAg2SnSe4 | -0.998 | 0.051 | 1.816 | |
| BaSi(AgTe2)2 | -0.617 | 0.056 | 1.265 | (hull too high) |
| CaAg2GeTe4 | -0.587 | 0.058 | 0.240 | |
| CaAg2SnTe4 | -0.625 | 0.072 | 0.062 | |
| ZnSi(AgTe2)2 | -0.222 | 0.095 | 2.036 | |
| BaSi(AgSe2)2 | -0.987 | 0.114 | 2.245 | |
| CaSi(AgTe2)2 | -0.493 | 0.122 | 1.247 | (hull too high) |
| K2CaSnSe4 | -1.410 | 0.127 | 2.648 | |
| ZnSi(AgSe2)2 | -0.553 | 0.170 | 1.904 | |

## Hypotheses tested and what was learned

**Iteration 1: Ag-, Cd-, Mg- and Ge-substituted kesterite (CZTS-derived).**
- The hypothesis was that Cu→Ag, Zn→Cd/Mg, Sn→Ge and S→Se would tune the CZTS gap toward 1.4 eV.
- It held for Ag-based selenides and tellurides. Six candidates landed in the window: CdAg₂GeSe₄, ZnAg₂GeSe₄, MgAg₂SnSe₄, MgAg₂GeTe₄, ZnAg₂GeTe₄ and MgAg₂SnTe₄.
- The Mg sulfides and MgAg₂GeSe₄ were too wide (1.86–1.89 eV). The Cd tellurides were too narrow.
- The Cu–Mg variants were unstable (hull 0.07–0.14).
- The critic vetoed Si and Ca substitutions at the kesterite sites in this iteration.
- Observed gap trends were S > Se > Te for the anion, and Mg > Zn > Cd for the divalent cation.

**Iteration 2: extend the Ag₂-M-IV-Se/Te₄ family to Sr, Ba, Co, Fe, Zr and Ti.**
- The chalcopyrite sweep was skipped because the candidates were mostly already in the Materials Project. NaGaS₂ and NaAlS₂ were novel but were not evaluated.
- Sr pushed the Ag selenide gaps to about 1.7 eV. SrAg₂GeSe₄ is inside the window, and SrAg₂SnSe₄ is just over it.
- The Sr/Ba Ag tellurides were stable but too narrow (0.1–0.7 eV).
- The Co/Fe variants (hull 0.056–0.112, gaps below 0.81 eV) and the Ti variants (hull 0.35–0.44) were rejected. Zr/Zn-based variants were stable but narrow. The hypothesis was falsified for these sites.

**Iteration 3: replace Cu/Ag with Na/K in A₂-M-(Sn/Ge)-(Se/Te)₄.**
- The II-IV-V₂ chalcopyrites were all already known and were skipped.
- Alkali replacement widened the gaps. All selenides were too wide (1.96–2.54 eV), though several were stable.
- Tellurides reached the window: K₂MgSnTe₄ (1.33 eV, hull 0.000), K₂ZnSnTe₄ (1.57 eV, hull 0.000), Na₂CdSnTe₄ (1.37 eV, hull 0.032) and Na₂MgGeTe₄ (1.14 eV, hull 0.047).
- K₂CdSnTe₄ and K₂CdGeTe₄ were too narrow (0.86–0.88 eV).

**Iteration 4: complete the alkali-telluride grid with Ca, Sr, Ba, Mn and Si.**
- A literature search found no prior reports of these quaternaries. This is weak support for novelty, not proof.
- Seven K-based tellurides landed in the window: K₂CaGeTe₄ (1.42 eV, hull 0.019, the closest to 1.4 eV), K₂BaGeTe₄, K₂BaSiTe₄, K₂MgSiTe₄, K₂SrSnTe₄, K₂SrGeTe₄ and K₂CaSnTe₄.
- K stabilises large divalent cations better than Na. The Na–Sr/Ba analogs had hull 0.06–0.12, and Na₂CaSnTe₄ had hull 0.17.
- K₂Ca/SrSiTe₄ had hull of about 0.10. The Mn variants had gaps that were too narrow or at the lower edge.

**Iteration 5: fill the remaining K₂-M-IV-Te₄ grid and test Ag–Si/Ca/Ba analogs.**
- One new hit: K₂CdSiTe₄ (1.235 eV, hull 0.000).
- K₂ZnSiTe₄ is stable but too wide (2.07 eV).
- The Ag–Si and Ag–Ca tellurides had gaps in the window for BaSi(AgTe₂)₂ and CaSi(AgTe₂)₂, but hull 0.056 and 0.122 excluded them. The CaAg₂-Ge/Sn tellurides were narrow and unstable.
- All K₂-AE-IV-Se₄ compounds were too wide (2.5–2.7 eV).
- Six relaxations were left unspent, because the remaining candidates were predicted to be wide-gap selenides.

**Overall.** Te-based alkali kesterite-types and Ag-selenides (with Zn, Cd, Mg or Sr) gave gaps in the window. Selenides in the alkali series were too wide, and 3d-metal and Ti/Zr sites failed.

## Caveats

- **Imposed prototype.** Every candidate was forced into the kesterite prototype. The K₂/Na₂-AE-IV-Te₄ compounds are unlikely to be kesterites in reality. Large Ca/Sr/Ba and alkali ions usually favour other coordination and structure types. A hull of 0.000 means only that no competing phase in the Materials Project is lower in energy. Missing polymorphs or unreported phases could make these compounds unstable.
- **Surrogate errors.** CHGNet energies and ML gaps carry errors that I did not quantify. Gap errors of a few tenths of an eV are plausible, which is comparable to the width of the window. Gaps for magnetic ions (Mn, Fe, Co) are especially unreliable.
- **Novelty.** "Novel" means absent from the Materials Project. Only the iteration 4 literature search was recorded, and it found nothing. Other sources were not checked.
- **Photovoltaic suitability.** No assessment was made of direct versus indirect gap, absorption, defect tolerance, band alignment, or toxicity and cost. Cd and Te raise toxicity and cost concerns, and Ag adds cost.
- **No experimental data.** There are no synthesis or characterisation data for any candidate.

## Recommended next steps

1. **Check polymorphs.** For the top K₂-AE-IV-Te₄ candidates, compute competing structure types and the competing binary and ternary phases. Do this first, because the imposed prototype is the biggest risk.
2. **Run DFT checks.** Relax the structures and compute hybrid-functional (HSE) or GW gaps for the top candidates, plus phonon stability. Start with K₂CaGeTe₄, K₂MgSnTe₄, CdAg₂GeSe₄, K₂CdSiTe₄, K₂BaGeTe₄, K₂SrGeTe₄/K₂SrSnTe₄, K₂ZnSnTe₄, Na₂CdSnTe₄ and ZnAg₂GeSe₄.
3. **Prioritise the Ag selenides.** The Ag–Zn/Cd–Ge–Se compounds (hull 0.000) have more conventional chemistry and a more plausible tetrahedral structure than the alkali tellurides. Check their gaps with higher-level methods.
4. **Try alloys.** Mixed cations (for example Zn/Mg or Cd/Mg) and mixed anions (Se/Te or S/Se) could tune the gap toward 1.4 eV. Mixed anions were not available through the single-substitution tool.
5. **Assess PV figures of merit.** Evaluate whether the gaps are direct, estimate absorption, and screen for defects. Drop members with toxicity or cost problems.
6. **Explore other families.** The kesterite-prototype space looks largely mapped. Other families should be tried, since the chalcopyrite and II-IV-V₂ sweeps turned up almost nothing novel.
