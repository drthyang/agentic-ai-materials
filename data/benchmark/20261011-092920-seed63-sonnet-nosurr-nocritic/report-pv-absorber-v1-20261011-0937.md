# Campaign report: pv-absorber-v1

## Executive summary

Over five iterations, 95 candidates were relaxed and scored (CHGNet relaxation, formation energy, energy above hull, and an HSE-fidelity ML band gap). All 95 were novel relative to the Materials Project (MP) database. I counted a candidate as a "hit" if its gap was 1.1–1.7 eV and its E_hull was ≤ 0.05 eV/atom. By that rule 14 compounds qualify, in three families:

- Ag-based kesterite-type Ag₂-II-(Ge/Sn)-(Se/Te)₄ compounds (8 hits).
- Famatinite-type I₃-V-VI₄ selenides and one sulfide (5 hits).
- Ag₂ZnTiS₄ (1 hit).
- KBiTe₂ is also counted among the hits, from the chalcopyrite-type prototype; the family counts above sum to 14 only if it is included (8 + 5 + 1 = 14 includes it under the first group's iteration-3 list: CdAg₂GeSe₄, MgAg₂GeTe₄, MgAg₂SnSe₄, MgAg₂SnTe₄, ZnAg₂GeSe₄, ZnAg₂GeTe₄, SrAg₂GeSe₄, KBiTe₂).

Confidence is low to moderate. Every number comes from a surrogate model, structures were restricted to the prototype lattices, and "novel" means only "absent from MP". No DFT, literature confirmation or synthesis has been done. The strongest candidates are CdAg₂GeSe₄, ZnAg₂GeSe₄, MgAg₂SnSe₄ and CuAg₂AsSe₄. Their gaps are in or near the target window and their E_hull is 0.0 or small.

## Scored candidates

Window hits (gap 1.1–1.7 eV, E_hull ≤ 0.05 eV/atom) are marked ✓. E_f is the formation energy per atom (eV), E_hull is in eV/atom, and the gap is in eV. Values are rounded.

### Iteration 1 (Ag-based kesterite substitutions)
| Formula | E_f | E_hull | Gap | Hit |
|---|---|---|---|---|
| CdAg2GeSe4 | -0.657 | 0.000 | 1.279 | ✓ |
| ZrCd(AgSe2)2 | -1.148 | 0.000 | 0.295 | |
| ZrCd(AgTe2)2 | -0.773 | 0.000 | 0.006 | |
| MgZr(AgTe2)2 | -0.878 | 0.000 | 0.841 | |
| CdAg2GeTe4 | -0.326 | 0.017 | 0.481 | |
| MgAg2GeSe4 | -0.797 | 0.020 | 1.856 | |
| MgAg2GeTe4 | -0.423 | 0.025 | 1.490 | ✓ |
| CaAg2GeTe4 | -0.587 | 0.058 | 0.240 | |
| CaAg2GeSe4 | -0.949 | 0.062 | 1.679 | |
| CdSi(AgTe2)2 | -0.230 | 0.083 | 1.055 | |
| MgSi(AgTe2)2 | -0.331 | 0.087 | 1.802 | |
| CdSi(AgSe2)2 | -0.568 | 0.130 | 1.714 | |
| MgSi(AgSe2)2 | -0.715 | 0.145 | 2.348 | |
| CaSi(AgSe2)2 | -0.867 | 0.187 | 2.510 | |
| MgZr(AgSe2)2 | -0.720 | 0.459 | 1.579 | |
| CaZr(AgSe2)2 | -0.882 | 0.493 | 2.471 | |

### Iteration 2 (Cu/Ag-II-Sn/Ge chalcogenides, Na-Ga/Al sulfides)
| Formula | E_f | E_hull | Gap | Hit |
|---|---|---|---|---|
| SrCu2SnTe4 | -0.751 | 0.000 | 0.867 | |
| BaCu2SnTe4 | -0.754 | 0.000 | 0.143 | |
| NaGaS2 | -1.810 | 0.000 | 3.827 | |
| NaAlS2 | -2.075 | 0.000 | 4.647 | |
| SrAg2SnSe4 | -1.059 | 0.000 | 1.701 | |
| SrAg2SnS4 | -1.369 | 0.000 | 1.720 | |
| MgAg2SnS4 | -1.177 | 0.002 | 1.871 | |
| BaAg2SnTe4 | -0.746 | 0.007 | 0.516 | |
| MgAg2SnSe4 | -0.838 | 0.016 | 1.588 | ✓ |
| MgCu2SnS4 | -1.239 | 0.020 | 2.174 | |
| CdAg2SnTe4 | -0.366 | 0.027 | 0.412 | |
| SrAg2SnTe4 | -0.689 | 0.029 | 0.100 | |
| BaCu2GeTe4 | -0.672 | 0.034 | 0.499 | |
| MgAg2SnTe4 | -0.461 | 0.038 | 1.172 | ✓ |
| SrCu2SnSe4 | -1.045 | 0.0504 | 1.109 | (borderline, just over the hull cutoff) |
| MgCu2SnSe4 | -0.819 | 0.071 | 1.383 | |
| SrCu2GeTe4 | -0.614 | 0.078 | 0.161 | |
| MgCu2GeTe4 | -0.372 | 0.101 | 0.895 | |
| MgCu2SnTe4 | -0.409 | 0.109 | 0.483 | |
| MgCu2GeSe4 | -0.717 | 0.136 | 1.102 | |

### Iteration 3 (Zn/Sr Ag₂-Ge/Sn, Ca/Mn variants, alkali-III/V chalcogenides)
| Formula | E_f | E_hull | Gap | Hit |
|---|---|---|---|---|
| ZnAg2GeSe4 | -0.681 | 0.000 | 1.119 | ✓ |
| KGaSe2 | -1.275 | 0.000 | 2.177 | |
| KSbTe2 | -0.741 | 0.000 | 0.547 | |
| KBiTe2 | -0.736 | 0.003 | 1.296 | ✓ |
| SrAg2GeSe4 | -1.021 | 0.003 | 1.687 | ✓ |
| SrAg2GeS4 | -1.354 | 0.013 | 1.867 | |
| SrAg2GeTe4 | -0.651 | 0.016 | 0.155 | |
| NaGaSe2 | -1.169 | 0.017 | 2.202 | |
| MgAg2GeS4 | -1.165 | 0.017 | 1.893 | |
| ZnAg2GeTe4 | -0.318 | 0.028 | 1.171 | ✓ |
| ZnAg2SnTe4 | -0.358 | 0.039 | 0.596 | |
| CaAg2SnSe4 | -0.998 | 0.051 | 1.816 | |
| CaAg2SnS4 | -1.297 | 0.068 | 2.279 | |
| CaCu2SnS4 | -1.371 | 0.072 | 2.704 | |
| MnAg2GeS4 | -0.914 | 0.079 | 2.236 | |
| CaAg2GeS4 | -1.273 | 0.094 | 2.148 | |
| CaCu2GeS4 | -1.340 | 0.096 | 2.563 | |
| CaCu2SnSe4 | -0.979 | 0.108 | 0.944 | |
| CaCu2GeSe4 | -0.928 | 0.121 | 1.198 | |

### Iteration 4 (famatinite-type I₃-V-VI₄)
| Formula | E_f | E_hull | Gap | Hit |
|---|---|---|---|---|
| Cu2AgSbS4 | -0.855 | 0.000 | 1.738 | |
| CuAg2SbS4 | -0.856 | 0.000 | 1.862 | |
| Ag3SbS4 | -0.856 | 0.000 | 1.791 | |
| Ag3SbSe4 | -0.573 | 0.000 | 1.665 | ✓ |
| Cu2AgSbSe4 | -0.523 | 0.000 | 0.425 | |
| CuAg2SbSe4 | -0.565 | 0.000 | 1.457 | ✓ |
| Cu2AgAsS4 | -0.824 | 0.000 | 1.869 | |
| CuAg2AsS4 | -0.828 | 0.000 | 1.974 | |
| Cu2AgAsSe4 | -0.483 | 0.000 | 0.436 | |
| CuAg2AsSe4 | -0.530 | 0.000 | 1.378 | ✓ |
| Ag3AsSe4 | -0.541 | 0.000 | 1.681 | ✓ |
| CuAg2PSe4 | -0.476 | 0.000 | 2.152 | |
| Cu2AgBiS4 | -0.888 | 0.000 | 1.587 | ✓ |
| CuAg2SbTe4 | -0.279 | 0.000 | 0.314 | |
| Cu3SbTe4 | -0.251 | 0.001 | 0.322 | |
| Cu2AgBiSe4 | -0.531 | 0.009 | 0.957 | |
| CuAg2PS4 | -0.830 | 0.020 | 2.448 | |
| Cu2AgPSe4 | -0.425 | 0.045 | 2.139 | |
| Cu2AgSbTe4 | -0.211 | 0.045 | 0.383 | |
| Cu2AgBiTe4 | -0.217 | 0.073 | 0.441 | |

### Iteration 5 (Ti/Zr-containing Ag₂-II-IV-X₄, Na₂-II-Ge-Se₄)
| Formula | E_f | E_hull | Gap | Hit |
|---|---|---|---|---|
| TiZn(AgS2)2 (Ag₂ZnTiS₄) | -1.547 | 0.000 | 1.554 | ✓ |
| ZrZn(AgSe2)2 | -1.183 | 0.000 | 0.653 | |
| ZrZn(AgS2)2 | -1.543 | 0.000 | 0.193 | |
| MgZr(AgS2)2 | -1.666 | 0.000 | 0.330 | |
| ZrMn(AgSe2)2 | -1.127 | 0.000 | ~0.000 | |
| Na2ZnGeSe4 | -1.094 | 0.011 | 2.480 | |
| Na2CdGeSe4 | -1.052 | 0.029 | 2.413 | |
| Na2MgGeSe4 | -1.186 | 0.055 | 2.448 | |
| TiCd(AgS2)2 | -0.957 | 0.351 | 2.400 | |
| TiZn(AgSe2)2 | -0.617 | 0.353 | 2.229 | |
| TiCd(AgSe2)2 | -0.590 | 0.357 | 2.354 | |
| MgTi(AgS2)2 | -1.143 | 0.364 | 1.948 | |
| Na2TiZnSe4 | -1.009 | 0.367 | 2.989 | |
| SrTi(AgSe2)2 | -0.938 | 0.373 | 2.357 | |
| MgTi(AgSe2)2 | -0.725 | 0.380 | 2.433 | |
| SrTi(AgS2)2 | -1.305 | 0.384 | 1.916 | |
| SrZr(AgS2)2 | -1.354 | 0.424 | 1.758 | |
| SrZr(AgSe2)2 | -0.944 | 0.440 | 2.331 | |
| ZrCd(AgS2)2 | -0.946 | 0.451 | 2.364 | |
| Na2ZrZnSe4 | -0.988 | 0.502 | 2.573 | |

## What was tested and what was learned

Iteration 3 has only observation and reflection entries in the notebook. The hypotheses for that batch appear only as tags in the database.

**Iteration 1: Ag-substituted kesterites (supported).**
- Hypothesis: substituting Zn→Cd/Mg, Sn→Ge/Si, Cu→Ag and mixing anions would tune the gap into 1.1–1.7 eV.
- The `propose_candidates` tool forced Cu→Ag, so no Cu variants were generated.
- Two hits resulted: CdAg₂GeSe₄ (gap 1.28, E_hull 0.0) and MgAg₂GeTe₄ (1.49, 0.025).
- Si-containing compounds were unstable (E_hull 0.083–0.187).
- Zr-containing Cd/Mg tellurides and selenides sat on the hull but had gaps of 0–0.84 eV.
- Ca- and Mg-Zr-selenide variants were unstable.
- Observed trends: Se→Te lowers the gap by roughly 0.8 eV, and Mg→Cd lowers it by roughly 0.6 eV.

**Iteration 2: chalcopyrite and Cu/Ag-Sn kesterites (partly supported).**
- The chalcopyrite proposals were almost all already in MP. Only NaGaS₂ and NaAlS₂ were novel, and both are far too wide-gap (3.8 and 4.6 eV).
- Cu-based kesterites were less stable than their Ag analogues. MgCu₂SnSe₄ has gap 1.38 but E_hull 0.071. SrCu₂SnSe₄ (1.11 eV) sits at E_hull 0.0504, just over the cutoff.
- Ag-Sn compounds gave two hits: MgAg₂SnSe₄ (1.59, 0.016) and MgAg₂SnTe₄ (1.17, 0.038).
- SrAg₂SnSe₄ (1.70) and SrAg₂SnS₄ (1.72) are stable near-misses.
- Ba/Sr/Cd Ag₂SnTe₄ gaps were too low (0.1–0.5 eV).

**Iteration 3: Zn/Sr Ge analogues, Ca/Mn variants, alkali-V/III chalcogenides (supported).**
- Four new hits: ZnAg₂GeSe₄ (1.12, 0.0), ZnAg₂GeTe₄ (1.17, 0.028), SrAg₂GeSe₄ (1.69, 0.003, at the window edge) and KBiTe₂ (1.30, 0.003).
- KBiTe₂ was modelled in a chalcopyrite-type prototype. Its real structure is probably layered or rocksalt-ordered, so this result is unverified.
- Every Ca-containing compound was unstable (E_hull ≥ 0.051 where evaluated), as was MnAg₂GeS₄ (0.079).
- Sulfides were stable but too wide-gap (1.87–1.89 eV for Mg/Sr Ag₂GeS₄).
- KGaSe₂ and NaGaSe₂ were stable but wide (about 2.2 eV).
- The zincblende prototype yielded only binaries and was not useful.

**Iteration 4: famatinite-type I₃-V-VI₄ (supported; most productive new family).**
- The Ag₂-II-IV-X₄ and I-V-VI₂ spaces were reported as exhausted (already known or already considered), so I switched to I₃-V-VI₄.
- Five hits, all selenides except one sulfide: CuAg₂AsSe₄ (1.378, 0.0), CuAg₂SbSe₄ (1.457, 0.0), Cu₂AgBiS₄ (1.587, 0.0), Ag₃SbSe₄ (1.665, 0.0) and Ag₃AsSe₄ (1.681, 0.0).
- Sulfides of Sb/As were stable but too wide (1.74–1.97 eV).
- Phosphides were wide (2.1–2.4 eV). Tellurides were narrow (0.3–0.45 eV).
- Cu-rich selenides Cu₂AgSbSe₄ and Cu₂AgAsSe₄ had gaps of about 0.43 eV, against about 1.4 eV for the single-Cu analogues. The notebook flags this jump as suspicious and possibly surrogate-model noise.
- Ag₃SbSe₄ and Ag₃AsSe₄ in a famatinite structure are probably not true ground states, even though the hull value is 0.

**Iteration 5: Ti/Zr-containing Ag₂-II-IV-X₄ and Na₂-II-Ge-Se₄ (weakly supported, 1 of 20).**
- The only hit was TiZn(AgS₂)₂ (Ag₂ZnTiS₄; 1.554 eV, E_hull 0.0).
- Zr compounds with Zn/Mg/Mn were on the hull but had gaps of 0–0.65 eV.
- Ti/Zr compounds with Cd, Mg and Sr, and the Ti selenides, were unstable (E_hull 0.35–0.50).
- Na₂-II-Ge-Se₄ compounds were near-stable (0.011–0.055) but had gaps of 2.4–2.5 eV.
- Ag₂ZnTiS₄ looks isolated: tetrahedral Ti⁴⁺ is chemically unusual, and its analogues sit at about 0.35 eV above the hull. Treat it with caution.

**Overall:** Ag-containing kesterite-type and famatinite-type chalcogenides are the productive families in this model. Ca fails consistently, as do Si and most Cu-rich variants. Sulfides tend to be too wide-gap and tellurides too narrow-gap, with selenides landing in the window.

## Caveats

- **Surrogate error.** Formation energies and hull distances come from CHGNet and the gaps from an ML model at "HSE fidelity". No error bars were computed. The nonmonotonic gap jump in the Cu/Ag selenides is evidence of noise.
- **Window edges.** SrAg₂SnSe₄ (1.701), SrCu₂SnSe₄ (E_hull 0.0504) and SrAg₂GeSe₄ (1.687) lie within plausible model error of the cutoffs. The hit/non-hit classification is not robust there.
- **Prototype-restricted structures.** Relaxation was confined to the kesterite or chalcopyrite-type frameworks, and true ground states may differ. The notebook flags Ag₃SbSe₄ and Ag₃AsSe₄ (real Ag₃SbS₄ is pyrargyrite-type), KBiTe₂ and Ag₂ZnTiS₄.
- **Novelty is relative to MP only.** The iteration 1 reflection notes that CdAg₂GeSe₄ may resemble a known Ag₂CdGeSe₄ in a different structure. The literature search for Ag₂ZnGeSe₄ returned nothing useful. No systematic literature novelty check was done.
- **Hull reference.** E_hull is measured against the MP hull. Unknown competing phases, and structure types not tried, could change stability.
- **Missing properties.** Nothing was assessed for absorption coefficient, direct versus indirect gap, defect tolerance, toxicity or cost, and no synthesis was attempted.
- **Mixed anions.** The tool could not generate mixed-anion compositions, so anion alloying was not tested.

## Recommended next steps

1. Run DFT validation with a hybrid functional or GW on the top candidates: CdAg₂GeSe₄, ZnAg₂GeSe₄, MgAg₂SnSe₄, MgAg₂GeTe₄, CuAg₂AsSe₄, CuAg₂SbSe₄, Cu₂AgBiS₄ and, with caution, Ag₂ZnTiS₄ and KBiTe₂.
2. Search for lower-energy polymorphs, for example with structure prediction or by testing known structure types such as pyrargyrite or wurtzite-derived ones. Redo the hull with competing binary and ternary phases.
3. Check the literature and ICSD for prior reports of these compositions, such as Ag₂CdGeSe₄ and Ag₂ZnGeSe₄.
4. Probe the gap noise in the Cu/Ag selenide series with a direct calculation of Cu₂AgSbSe₄ and CuAg₂SbSe₄.
5. Tune toward about 1.4 eV with S/Se or Se/Te alloys, for example around the SrAg₂SnSe₄/MgAg₂SnSe₄ edge cases. This needs tooling that supports mixed anions.
6. If a candidate survives validation, assess synthesizability, for example through solid-state reaction conditions and secondary-phase risk.
