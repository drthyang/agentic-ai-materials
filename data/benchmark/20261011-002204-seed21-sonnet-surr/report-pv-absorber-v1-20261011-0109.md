# Campaign report: pv-absorber-v1

## Executive summary

Over 5 iterations, 76 compositions were relaxed and scored. 74 of them are novel relative to the Materials Project, and 2 were deliberate known-compound calibrations. The only productive region was the Ag-based kesterite-type family, A²⁺Ag₂(Ge/Sn)(S/Se/Te)₄. Several members came out thermodynamically stable (E_hull ≈ 0) with predicted gaps in the 1.1–1.7 eV window, which the notebook used as the PV target window (the compound labels point to ~1.4 eV as the ideal). The best are CdAg₂GeSe₄ (1.28 eV, E_hull 0.000) and ZnAg₂GeSe₄ (1.12 eV, E_hull 0.000). Other candidates are MgAg₂SnSe₄, MgAg₂GeTe₄, ZnAg₂GeTe₄ and SrAg₂GeSe₄. Confidence is low to moderate. Every number comes from a CHGNet relaxation plus an ML band-gap predictor, with no DFT or experimental validation. No candidate landed exactly at 1.4 eV with E_hull < 0.02 eV/atom. Iteration 5 found no hits, and the novelty filter exhausted most of the reachable prototype space.

## Scored candidates

Columns: E_f = formation energy (eV/atom), E_hull = energy above hull (eV/atom), Gap = predicted band gap (eV). Novel = absent from the Materials Project.

### Iteration 1
| Formula | E_f | E_hull | Gap | Novel |
|---|---|---|---|---|
| CdAg2GeSe4 | -0.657 | 0.000 | 1.28 | yes |
| ZrCd(AgSe2)2 | -1.148 | 0.000 | 0.30 | yes |
| CdAg2SnSe4 | -0.700 | 0.000 | 1.26 | no (calibration) |
| MgAg2SnS4 | -1.177 | 0.002 | 1.87 | yes |
| MgAg2SnSe4 | -0.838 | 0.016 | 1.59 | yes |
| CdAg2GeTe4 | -0.326 | 0.017 | 0.48 | yes |
| MgAg2GeS4 | -1.165 | 0.017 | 1.89 | yes |
| MgAg2GeSe4 | -0.797 | 0.020 | 1.86 | yes |
| MgAg2GeTe4 | -0.423 | 0.025 | 1.49 | yes |
| CaAg2GeTe4 | -0.587 | 0.058 | 0.24 | yes |
| CaAg2GeSe4 | -0.949 | 0.062 | 1.68 | yes |
| CdSi(AgTe2)2 | -0.230 | 0.083 | 1.05 | yes |
| MgSi(AgTe2)2 | -0.331 | 0.087 | 1.80 | yes |
| CdSi(AgSe2)2 | -0.568 | 0.130 | 1.71 | yes |
| MgSi(AgSe2)2 | -0.715 | 0.145 | 2.35 | yes |
| CaSi(AgSe2)2 | -0.867 | 0.187 | 2.51 | yes |

### Iteration 2
| Formula | E_f | E_hull | Gap | Novel |
|---|---|---|---|---|
| ZnAg2GeSe4 | -0.681 | 0.000 | 1.12 | yes |
| ZrCd(CuSe2)2 | -1.141 | 0.000 | 0.15 | yes |
| MgZr(CuSe2)2 | -1.276 | 0.000 | 0.19 | yes |
| ZrZn(CuSe2)2 | -1.188 | 0.000 | 0.21 | yes |
| CaZr(CuSe2)2 | -1.494 | 0.000 | 0.06 | yes |
| MgCu2SnS4 | -1.239 | 0.020 | 2.17 | yes |
| CdAg2SnTe4 | -0.366 | 0.027 | 0.41 | yes |
| ZnAg2GeTe4 | -0.318 | 0.028 | 1.17 | yes |
| MgAg2SnTe4 | -0.461 | 0.038 | 1.17 | yes |
| ZnAg2SnTe4 | -0.358 | 0.039 | 0.60 | yes |
| SrCu2SnSe4 | -1.045 | 0.050 | 1.11 | yes |
| MgCu2SnSe4 | -0.819 | 0.071 | 1.38 | yes |
| CaCu2SnS4 | -1.371 | 0.072 | 2.70 | yes |
| CaCu2GeS4 | -1.340 | 0.096 | 2.56 | yes |
| CaCu2SnSe4 | -0.979 | 0.108 | 0.94 | yes |
| CaCu2GeSe4 | -0.928 | 0.121 | 1.20 | yes |
| MgCu2GeSe4 | -0.717 | 0.136 | 1.10 | yes |
| TiZn(CuSe2)2 | -0.573 | 0.412 | 2.84 | yes |
| MgTi(CuSe2)2 | -0.677 | 0.443 | 2.71 | yes |
| TiCd(CuSe2)2 | -0.487 | 0.479 | 2.80 | yes |

### Iteration 3
| Formula | E_f | E_hull | Gap | Novel |
|---|---|---|---|---|
| SrAg2SnSe4 | -1.059 | 0.000 | 1.70 | yes |
| BaAg2GeTe4 | -0.704 | 0.000 | 0.70 | yes |
| NiAg2SnSe4 | -0.631 | 0.000 | 1.68 | yes |
| NaGaS2 | -1.810 | 0.000 | 3.83 | yes |
| NaAlS2 | -2.075 | 0.000 | 4.65 | yes |
| NiAg2GeSe4 | -0.583 | 0.0005 | 1.65 | yes |
| SrAg2GeSe4 | -1.021 | 0.003 | 1.69 | yes |
| BaAg2SnTe4 | -0.746 | 0.007 | 0.52 | yes |
| SrAg2GeTe4 | -0.651 | 0.016 | 0.16 | yes |
| SrAg2SnTe4 | -0.689 | 0.029 | 0.10 | yes |
| CoAg2SnSe4 | -0.569 | 0.056 | 0.60 | yes |
| FeAg2SnSe4 | -0.579 | 0.072 | 0.00 | yes |
| CoAg2GeSe4 | -0.524 | 0.075 | 0.81 | yes |
| FeAg2GeSe4 | -0.525 | 0.078 | 0.02 | yes |
| FeAg2GeTe4 | -0.199 | 0.112 | 0.01 | yes |
| FeAg2SnTe4 | -0.243 | 0.119 | 0.01 | yes |

### Iteration 4
| Formula | E_f | E_hull | Gap | Novel |
|---|---|---|---|---|
| ZrZn(AgSe2)2 | -1.183 | 0.000 | 0.65 | yes |
| SrAg2SnS4 | -1.369 | 0.000 | 1.72 | yes |
| SrCu2SnTe4 | -0.751 | 0.000 | 0.87 | yes |
| ZrZn(AgTe2)2 | -0.781 | 0.000 | 0.07 | yes |
| BaCu2SnTe4 | -0.750 | 0.001 | 0.39 | yes |
| SrAg2GeS4 | -1.354 | 0.013 | 1.87 | yes |
| BaCu2GeTe4 | -0.672 | 0.034 | 0.50 | yes |
| BaSi(AgTe2)2 | -0.617 | 0.056 | 1.27 | yes |
| SrCu2GeTe4 | -0.614 | 0.078 | 0.16 | yes |
| ZnSi(AgTe2)2 | -0.222 | 0.095 | 2.04 | yes |
| MnCu2GeSe4 | -0.531 | 0.104 | 0.93 | yes |
| BaCu2SiSe4 | -0.950 | 0.166 | 1.93 | yes |
| ZnSi(AgSe2)2 | -0.553 | 0.170 | 1.90 | yes |
| SrCu2SiSe4 | -0.895 | 0.183 | 2.03 | yes |
| Na2ZrZnTe4 | -0.508 | 0.456 | 2.45 | yes |
| Na2ZrCdTe4 | -0.492 | 0.468 | 1.66 | yes |
| Na2MgZrTe4 | -0.581 | 0.485 | 1.95 | yes |
| Na2ZrZnSe4 | -0.988 | 0.502 | 2.57 | yes |
| Na2ZrCdSe4 | -0.929 | 0.537 | 3.03 | yes |
| Na2MgZrSe4 | -1.082 | 0.543 | 2.39 | yes |

### Iteration 5
| Formula | E_f | E_hull | Gap | Novel |
|---|---|---|---|---|
| CdSnS2 | -1.169 | 0.041 | 2.42 | yes |
| ZnSnTe2 | -0.498 | 0.084 | 0.98 | yes |
| ZnSnS2 | -1.178 | 0.122 | 2.53 | yes |
| ZnSnAs2 | -0.040 | 0.230 | 0.37 | no (calibration) |

## Hypotheses tested and what was learned

**Iteration 1: Ag-kesterite substitution.**
- The starting idea was isoelectronic substitution in Cu₂ZnSnS₄ (Zn→Cd/Mg, Sn→Ge/Si, S→Se/Te, Cu→Ag).
- All scored compounds were Ag-type kesterites.
- CdAg₂GeSe₄ (1.28 eV, E_hull 0.0) was the best result.
- MgAg₂GeTe₄ (1.49 eV, E_hull 0.025) and MgAg₂SnSe₄ (1.59 eV, E_hull 0.016) were also in the window and near-stable.
- Si analogues were unstable (E_hull 0.083–0.187).
- Ca analogues were marginal to unstable.
- Mg sulfides were too wide (~1.9 eV).
- The Cd telluride had too small a gap (0.48 eV).
- The known CdAg₂SnSe₄ calibration (1.26 eV, E_hull 0.0) fits the same Ag–Cd–selenide trend.

**Iteration 2: Cu/Ag mixing and Zn/Mg/Cd variants.**
- ZnAg₂GeSe₄ (1.12 eV, E_hull 0.0) was stable and in the window.
- ZnAg₂GeTe₄ (1.17 eV, E_hull 0.028) and MgAg₂SnTe₄ (1.17 eV, E_hull 0.038) were near-stable.
- The Cu versions gave useful gaps but were less stable: MgCu₂SnSe₄ (1.38 eV, E_hull 0.071) and SrCu₂SnSe₄ (1.11 eV, E_hull 0.050).
- Zr-containing compounds were stable (E_hull 0.0) but had gaps of only ~0.06–0.21 eV, so they are dead ends for this target.
- Ti analogues were very unstable (E_hull 0.41–0.48).
- Ca–Cu compounds were unstable, with E_hull 0.072–0.121 for the Sn/Ge compounds.
- The notebook records that the surrogate's top picks (e.g. CaCu₂GeSe₄) were unstable, because its gap-driven expected improvement ignored the hull.

**Iteration 3: chalcopyrite alkali compounds and large or 3d A²⁺ cations.**
- The alkali I-III-VI₂ route was a dead end.
  - Most proposals were already known.
  - NaGaS₂ (3.83 eV) and NaAlS₂ (4.65 eV) are stable but far too wide.
  - K-based variants were vetoed by the critic for size mismatch.
- Sr on the divalent site gave stable selenides with gaps at or just past the upper edge of the window: SrAg₂GeSe₄ (1.69 eV, E_hull 0.003) and SrAg₂SnSe₄ (1.70 eV, E_hull 0.0).
- NiAg₂GeSe₄ and NiAg₂SnSe₄ (1.65 and 1.68 eV, E_hull ≈ 0) look attractive, but the Ni²⁺ gap is likely unreliable and I treat it as suspect.
- Fe and Co analogues were unstable or metallic-like.
- Sr/Ba tellurides had gaps of 0.10–0.70 eV, too small.
- 4 budget units went unspent because only 2 novel candidates passed the critic.

**Iteration 4: S/Se Ag-kesterites with Sr/Ba, plus Na/Zr variants.**
- No new compounds landed inside both the gap and stability windows.
- Sulfides widened the gap as expected: SrAg₂SnS₄ is 1.72 eV with E_hull 0.0, borderline on gap, and SrAg₂GeS₄ is 1.87 eV.
- Na₂Zr(Zn/Cd/Mg)(Se/Te)₄ was very unstable (E_hull 0.46–0.54).
- Sr/Ba Cu tellurides were stable or near-stable but had gaps of 0.39–0.87 eV, too small.
- Si analogues were unstable.
- BaSi(AgTe₂)₂ had a good gap (1.27 eV) but E_hull of 0.056.

**Iteration 5: II-IV-V₂ / II-IV-VI₂ chalcopyrites (zincblende-derived).**
- The hypothesis was falsified in this evaluator.
- The zincblende prototype returned only known binaries.
- Of the 4 scored compounds, CdSnS₂ was near-stable (E_hull 0.041) but too wide (2.42 eV), and the others were unstable.
- The known ZnSnAs₂ calibration gave E_hull 0.23 and a gap of 0.37 eV, which suggests CHGNet is poor for this chemistry.
- The notebook records that the Mn(IV) Ag-kesterites were critic-vetoed as implausible, and that the novelty and SMACT filters removed most of the proposals (112 filtered out, 4 scored).
- Most of the budget went unspent.

**Overall:** the Ag-II-IV-Se₄/Te₄ kesterite-type family is the productive one. The A²⁺ cation sets the gap roughly as Zn/Cd (about 1.1–1.3 eV) < Mg/Sr (about 1.6–1.9 eV) for the selenides. In the tellurides Zn and Mg are the only ones with in-window gaps. Ge versus Sn is a secondary effect.

## Top candidates (novel, E_hull ≤ ~0.03, gap 1.1–1.7 eV)
| Formula | Gap (eV) | E_hull (eV/atom) | Note |
|---|---|---|---|
| CdAg2GeSe4 | 1.28 | 0.000 | best overall |
| ZnAg2GeSe4 | 1.12 | 0.000 | |
| MgAg2SnSe4 | 1.59 | 0.016 | |
| MgAg2GeTe4 | 1.49 | 0.025 | |
| ZnAg2GeTe4 | 1.17 | 0.028 | |
| SrAg2GeSe4 | 1.69 | 0.003 | at the edge of the window |
| NiAg2GeSe4, NiAg2SnSe4 | 1.65, 1.68 | ~0 | gap suspect |

MgAg₂SnTe₄ (1.17 eV, E_hull 0.038) and SrAg₂SnSe₄ (1.70 eV, E_hull 0.0) are borderline. SrAg₂SnS₄ (1.72 eV, E_hull 0.0) is also borderline on gap.

## Caveats

- **Method fidelity.** All values are ML-based. Structures come from CHGNet relaxation, and gaps come from an HSE-fidelity ML predictor. No DFT or experimental data were generated.
- **Hull values.** E_hull depends on the reference phases available in the database and on CHGNet accuracy. The ZnSnAs₂ calibration (E_hull 0.23 eV/atom) shows the evaluator can be badly off for some chemistries.
- **Prototype assumption.** All candidates were assumed to take the kesterite-type structure. The true ground-state polymorph (e.g. a stannite or wurtzite-derived or entirely different Ag-based structure) was not searched. E_hull ≈ 0 may reflect missing competing phases rather than true stability.
- **Gap reliability.** Gaps for 3d-metal compounds (Ni, Fe, Co, Mn) are likely unreliable. Large gap swings across chemically similar compounds, such as the Sr/Ba tellurides, probably reflect structural distortion. The notebook itself flags this.
- **Surrogate.** The GP surrogate had no data in iteration 1. Its expected improvement later favoured gap over stability and produced unstable picks. It was advisory only, and no error bars are quantified.
- **Record-keeping.** The iteration 1 and 5 notebook counts differ slightly from the database. The notebook says 12 evaluated in iteration 1 and 5 in iteration 5, while the database holds 16 and 4 scored rows. I used the database.
- **Absorber suitability.** Nothing was assessed beyond gap and stability. This covers defect tolerance, absorption coefficient, Ag cost, and toxicity (Cd).

## Recommended next steps

1. Run DFT validation (HSE or hybrid gaps, phonons, competing-phase hulls). Start with CdAg₂GeSe₄, ZnAg₂GeSe₄, MgAg₂SnSe₄, MgAg₂GeTe₄ and SrAg₂GeSe₄. Check alternative polymorphs such as stannite and wurtzite-derived structures.
2. Alloy on the divalent site (e.g. Zn/Cd or Cd/Sr mixes) to reach ~1.4 eV. The pure compounds bracket that value, with Zn at 1.12 eV and Cd at 1.28 eV on one side and Mg or Sr at about 1.6–1.7 eV on the other. The generator doesn't enumerate such alloys, so this needs explicit supercell work.
3. Test Se/Te and S/Se mixed-anion variants, which the generator didn't cover.
4. Verify the Ni-containing results with spin-polarized DFT before treating them as hits.
5. Drop the lines that failed: Ti, Zr, Fe/Co, Si, Ca–Cu, Na/Zr, alkali chalcopyrites, and II-IV-V₂ pnictides in this evaluator.
6. If candidates survive DFT, assess synthesizability, e.g. against known Ag–Cd–Ge–Se phases.
