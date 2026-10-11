# Campaign report: pv-absorber-v1

## Executive summary

The campaign ran five iterations looking for novel photovoltaic absorbers. The target was a band gap of 1.1–1.7 eV, ideally about 1.4 eV, with energy above hull (Ehull) of 0.05 eV/atom or less. Almost all of the work used the kesterite A₂-II-IV-Q₄ prototype. In total 99 candidates were scored with CHGNet relaxation and a surrogate "HSE-fidelity" band-gap model. 98 of them were novel relative to Materials Project (MP). The one known compound, ZnCu₂SnSe₄, was a deliberate calibration point.

Counting directly from the scored table, **24 novel candidates meet both the gap and the stability criteria**. Most are alkali kesterite tellurides and selenides (K₂- and Na₂-II-IV-Q₄); a smaller group are Ag₂-II-IV-Q₄ kesterites. The candidates closest to 1.4 eV that also sit on or near the hull are:

| Formula | Gap (eV) | Ehull (eV/atom) |
|---|---|---|
| K₂MnGeSe₄ | 1.443 | 0.000 |
| K₂CaGeTe₄ | 1.421 | 0.019 |
| K₂MnSiTe₄ | 1.455 | 0.045 |
| Na₂CdSnTe₄ | 1.367 | 0.032 |
| K₂MgSnTe₄ | 1.329 | 0.000 |

Confidence in these results is moderate to low:
- **Gaps:** the gap model underestimated the gap of the one calibration compound, CZTSe, by about 0.6 eV.
- **Stability:** Ehull was computed only for the kesterite polymorph against MP phases.
- **Validation:** none of these predictions has been checked with DFT or by experiment.

## Scored candidates

"Hit" means novel, Ehull ≤ 0.050 eV/atom and gap between 1.1 and 1.7 eV. Values are from CHGNet relaxation and the surrogate gap model. Formation energy (E_f) and Ehull are in eV/atom; gaps are in eV.

### Iteration 1: Ag/Cu kesterites (19 scored)
| Formula | E_f | Ehull | Gap | Novel | Hit |
|---|---|---|---|---|---|
| ZnAg₂GeSe₄ | -0.681 | 0.000 | 1.119 | yes | ✔ |
| CdAg₂GeSe₄ | -0.657 | 0.000 | 1.279 | yes | ✔ |
| MgAg₂SnS₄ | -1.177 | 0.002 | 1.871 | yes | |
| MgAg₂SnSe₄ | -0.838 | 0.016 | 1.588 | yes | ✔ |
| CdAg₂GeTe₄ | -0.326 | 0.017 | 0.481 | yes | |
| MgAg₂GeS₄ | -1.165 | 0.017 | 1.893 | yes | |
| MgCu₂SnS₄ | -1.239 | 0.020 | 2.174 | yes | |
| MgAg₂GeSe₄ | -0.797 | 0.020 | 1.856 | yes | |
| MgAg₂GeTe₄ | -0.423 | 0.025 | 1.490 | yes | ✔ |
| ZnCu₂SnSe₄ (calibration) | -0.698 | 0.057 | 0.343 | **no** | — |
| MgCu₂SnSe₄ | -0.819 | 0.071 | 1.383 | yes | |
| FeAg₂SnSe₄ | -0.579 | 0.072 | -0.003 (≈0) | yes | |
| FeAg₂GeSe₄ | -0.525 | 0.078 | 0.018 | yes | |
| MnAg₂GeS₄ | -0.914 | 0.079 | 2.236 | yes | |
| MnCu₂GeSe₄ | -0.531 | 0.104 | 0.931 | yes | |
| CdSi(AgSe₂)₂ | -0.568 | 0.130 | 1.714 | yes | |
| FeAg₂GeS₄ | -0.851 | 0.135 | 0.013 | yes | |
| MgCu₂GeSe₄ | -0.717 | 0.136 | 1.102 | yes | |
| ZnSi(AgSe₂)₂ | -0.553 | 0.170 | 1.904 | yes | |

### Iteration 2: Na kesterites, Ag-Sn tellurides, Ti⁴⁺ on the IV site (20 scored)
| Formula | E_f | Ehull | Gap | Novel | Hit |
|---|---|---|---|---|---|
| TiZn(CuS₂)₂ | -1.574 | 0.000 | 2.660 | yes | |
| TiCd(CuS₂)₂ | -1.514 | 0.000 | 2.861 | yes | |
| MgTi(CuS₂)₂ | -1.700 | 0.000 | 2.935 | yes | |
| Na₂ZnSnSe₄ | -1.121 | 0.007 | 2.292 | yes | |
| Na₂ZnGeTe₄ | -0.690 | 0.015 | 2.419 | yes | |
| Na₂CdSnSe₄ | -1.085 | 0.019 | 1.957 | yes | |
| Na₂CdGeTe₄ | -0.680 | 0.021 | 1.739 | yes | |
| Na₂ZnSnTe₄ | -0.712 | 0.023 | 2.053 | yes | |
| CdAg₂SnTe₄ | -0.366 | 0.027 | 0.412 | yes | |
| Na₂CdGeSe₄ | -1.052 | 0.029 | 2.413 | yes | |
| Na₂CdSnTe₄ | -0.699 | 0.032 | 1.367 | yes | ✔ |
| MgAg₂SnTe₄ | -0.461 | 0.038 | 1.172 | yes | ✔ |
| ZnAg₂SnTe₄ | -0.358 | 0.039 | 0.596 | yes | |
| Na₂MgGeTe₄ | -0.759 | 0.047 | 1.136 | yes | ✔ |
| Na₂MgSnTe₄ | -0.782 | 0.055 | 1.932 | yes | |
| MgCu₂GeTe₄ | -0.372 | 0.101 | 0.895 | yes | |
| TiCd(AgS₂)₂ | -0.957 | 0.351 | 2.400 | yes | |
| MgTi(AgS₂)₂ | -1.143 | 0.364 | 1.948 | yes | |
| MgTi(AgSe₂)₂ | -0.725 | 0.380 | 2.433 | yes | |
| TiZn(CuSe₂)₂ | -0.573 | 0.412 | 2.835 | yes | |

### Iteration 3: alkali kesterites with larger II cations, plus Na chalcopyrite (20 scored)
| Formula | E_f | Ehull | Gap | Novel | Hit |
|---|---|---|---|---|---|
| Na₂MnSnSe₄ | -1.074 | 0.000 | 1.115 | yes | ✔ (edge) |
| Na₂CaGeTe₄ | -1.098 | 0.000 | 1.731 | yes | |
| K₂CdSnTe₄ | -0.899 | 0.000 | 0.864 | yes | |
| K₂CdGeTe₄ | -0.863 | 0.000 | 0.884 | yes | |
| K₂MgSnTe₄ | -0.977 | 0.000 | 1.329 | yes | ✔ |
| K₂MgGeTe₄ | -0.948 | 0.000 | 1.499 | yes | ✔ |
| K₂MnSnTe₄ | -0.932 | 0.000 | 0.646 | yes | |
| K₂BaGeTe₄ | -1.187 | 0.000 | 1.566 | yes | ✔ |
| K₂CdGeSe₄ | -1.169 | 0.000 | 2.409 | yes | |
| K₂MnGeTe₄ | -0.709 | 0.002 | 1.0996 | yes | (just below 1.1) |
| Na₂MnGeSe₄ | -1.035 | 0.008 | 1.646 | yes | ✔ |
| K₂SrSnTe₄ | -1.128 | 0.012 | 1.199 | yes | ✔ |
| K₂SrGeTe₄ | -1.087 | 0.013 | 1.216 | yes | ✔ |
| NaGaSe₂ (chalcopyrite) | -1.169 | 0.017 | 2.202 | yes | |
| K₂CaSnTe₄ | -1.085 | 0.033 | 1.118 | yes | ✔ (edge) |
| Na₂MnGeTe₄ | -0.588 | 0.043 | 1.088 | yes | |
| Na₂MnSnTe₄ | -0.618 | 0.046 | 0.947 | yes | |
| Na₂SrGeTe₄ | -0.913 | 0.113 | 1.692 | yes | |
| Na₂SrSnTe₄ | -0.933 | 0.124 | 1.725 | yes | |
| Na₂CaSnTe₄ | -0.865 | 0.169 | 1.458 | yes | |

### Iteration 4: completing the K family; alkaline-earth Ag/Cu kesterites (20 scored)
| Formula | E_f | Ehull | Gap | Novel | Hit |
|---|---|---|---|---|---|
| K₂ZnSnTe₄ | -1.001 | 0.000 | 1.573 | yes | ✔ |
| K₂ZnGeTe₄ | -0.902 | 0.000 | 1.896 | yes | |
| K₂ZnSnSe₄ | -1.222 | 0.000 | 2.265 | yes | |
| BaAg₂GeTe₄ | -0.704 | 0.000 | 0.705 | yes | |
| BaCu₂SnTe₄ | -0.754 | 0.000 | 0.143 | yes | |
| SrCu₂SnTe₄ | -0.751 | 0.000 | 0.866 | yes | |
| K₂MnGeSe₄ | -1.142 | 0.000 | 1.443 | yes | ✔ |
| SrAg₂GeSe₄ | -1.021 | 0.003 | 1.687 | yes | ✔ (edge) |
| BaAg₂SnTe₄ | -0.746 | 0.007 | 0.516 | yes | |
| SrAg₂GeTe₄ | -0.651 | 0.016 | 0.155 | yes | |
| K₂CaGeTe₄ | -1.059 | 0.019 | 1.421 | yes | ✔ |
| SrAg₂SnTe₄ | -0.689 | 0.029 | 0.100 | yes | |
| BaCu₂GeTe₄ | -0.672 | 0.034 | 0.499 | yes | |
| CaAg₂SnSe₄ | -0.998 | 0.051 | 1.816 | yes | |
| CaAg₂GeSe₄ | -0.949 | 0.062 | 1.679 | yes | |
| CaAg₂SnTe₄ | -0.625 | 0.072 | 0.062 | yes | |
| CaCu₂SnS₄ | -1.371 | 0.072 | 2.704 | yes | |
| SrCu₂GeTe₄ | -0.614 | 0.078 | 0.161 | yes | |
| CaCu₂SnSe₄ | -0.979 | 0.108 | 0.944 | yes | |
| CaCu₂GeSe₄ | -0.928 | 0.121 | 1.198 | yes | |

### Iteration 5: Si on the IV site of alkali kesterites; K₂(Fe,Co) selenides (20 scored)
| Formula | E_f | Ehull | Gap | Novel | Hit |
|---|---|---|---|---|---|
| K₂CdSiTe₄ | -0.798 | 0.000 | 1.235 | yes | ✔ |
| K₂ZnSiTe₄ | -0.802 | 0.000 | 2.069 | yes | |
| K₂BaSiTe₄ | -1.122 | 0.000 | 1.642 | yes | ✔ |
| K₂FeSnSe₄ | -1.124 | 0.000 | 0.437 | yes | |
| Na₂CaSiTe₄ | -1.026 | 0.000 | 2.047 | yes | |
| K₂MgSiTe₄ | -0.868 | 0.005 | 1.692 | yes | ✔ (edge) |
| K₂CdSiSe₄ | -1.099 | 0.009 | 2.686 | yes | |
| K₂FeGeSe₄ | -1.083 | 0.010 | 0.632 | yes | |
| K₂CoSnSe₄ | -1.087 | 0.020 | 2.120 | yes | |
| K₂CoGeSe₄ | -1.067 | 0.021 | 2.314 | yes | |
| K₂MnSiSe₄ | -1.073 | 0.040 | 1.675 | yes | ✔ (edge) |
| K₂MnSiTe₄ | -0.694 | 0.045 | 1.455 | yes | ✔ |
| Na₂ZnSiTe₄ | -0.615 | 0.094 | 2.791 | yes | |
| K₂CaSiTe₄ | -0.972 | 0.098 | 1.455 | yes | |
| K₂SrSiTe₄ | -0.987 | 0.105 | 1.875 | yes | |
| Na₂CdSiTe₄ | -0.600 | 0.105 | 1.796 | yes | |
| Na₂MgSiTe₄ | -0.677 | 0.134 | 2.155 | yes | |
| Na₂MnSiSe₄ | -0.956 | 0.151 | 1.561 | yes | |
| Na₂MnSiTe₄ | -0.506 | 0.165 | 2.035 | yes | |
| Na₂SrSiTe₄ | -0.822 | 0.208 | 2.081 | yes | |

**Campaign statistics:**

| Iteration | Proposed | Filtered out | Scored |
|---|---|---|---|
| 1 | 59 | 5 | 19 |
| 2 | 54 | 12 | 20 |
| 3 | 75 | 1 | 20 |
| 4 | 29 | — | 20 |
| 5 | 32 | — | 20 |

The total is 99 scored, of which 98 are novel and 24 are hits. The notebook's final reflection says "~25" hits; the strict count from the table is 24, because K₂MnGeTe₄ (1.0996 eV) falls just below the window.

## Hypotheses tested and what was learned

**Iteration 1: isovalent substitution in I₂-II-IV-VI₄ kesterites (Ag on the I site; Mg, Mn, Fe on the II site).**
- **Supported for Ag:** Ag₂-II-Ge-Se₄ and the Mg-Ag selenide and telluride members were stable and in the window (4 hits).
- **Mg with Cu:** putting Mg on the II site widened the gap but was unstable with Cu in selenides (MgCu₂SnSe₄ 0.071, MgCu₂GeSe₄ 0.136 eV/atom).
- **Fe members:** came out essentially metallic and unstable.
- **Mn members:** unstable (0.08–0.10 eV/atom).
- **Ag-Si-Se members:** unstable (0.13–0.17 eV/atom).
- **Calibration:** CZTSe came out at 0.34 eV against the notebook's experimental reference of about 1.0 eV, so Cu-based gaps from this model are probably underestimated by about 0.6 eV.

**Iteration 2: Na on the I site; Ag-Sn tellurides; Ti⁴⁺ on the IV site.**
- **Pnictides abandoned:** II-IV-As₂ chalcopyrites were all already in MP, and the II-IV-P₂ phosphides failed the SMACT chemistry filter, so this line was dropped.
- **Na kesterites:** all nine were near-stable (Ehull 0.007–0.055 eV/atom). Most gaps were too wide. Cd combined with Te lowered the gap the most, giving Na₂CdSnTe₄ at 1.37 eV.
- **MgAg₂SnTe₄ (1.17 eV):** an in-window hit, which supports the Ag-Mg branch of the hypothesis.
- **Zn/Cd-Ag-Sn tellurides:** gaps too small (0.41–0.60 eV).
- **Ti⁴⁺ hypothesis falsified:** the idea was that empty d0 Ti states would lower the gap. Instead the Cu₂(Zn,Cd,Mg)TiS₄ members were on the hull but had gaps of 2.66–2.94 eV. The Ag-Ti and Se-Ti members were highly unstable (0.35–0.41 eV/atom).
- **Unresolved anomaly:** Na₂MgGeTe₄ (1.14 eV) has a smaller gap than Na₂MgSnTe₄ (1.93 eV), which is the opposite of the usual Ge/Sn trend. It may be a model artefact.

**Iteration 3: I-III-VI₂ chalcopyrites with alkali I cations; alkali kesterites with larger II cations and K on the I site.**
- **Chalcopyrite branch failed on novelty:** almost all of this space is already in MP. The only novel member evaluated, NaGaSe₂, had a 2.20 eV gap.
- **Alkali kesterite branch strongly supported (8 hits):** K accommodated Ca, Sr and Ba (Ehull ≤ 0.033 eV/atom). Na with Ca or Sr in the Sn/Ge tellurides was unstable (0.11–0.17 eV/atom), with one exception: Na₂CaGeTe₄ sat on the hull but its gap (1.73 eV) was just above the window. This supports a size-matching rule.
- **Gap trends:** Mn lowered gaps relative to Mg. Swapping Na for K lowered the gap of the Cd members.

**Iteration 4: completing the K family; alkaline-earth Ag/Cu kesterites.**
- **Two new near-ideal hits:** K₂CaGeTe₄ (1.42 eV) and K₂MnGeSe₄ (1.44 eV), both close to the values predicted beforehand.
- **Zn interpolation wrong:** K₂Zn members did not fall between the Mg and Cd members; K₂ZnSnTe₄ (1.57 eV) has a wider gap than K₂MgSnTe₄ (1.33 eV).
- **Alkaline-earth branch with Ag/Cu mostly failed:** the tellurides had collapsed gaps (0.06–0.87 eV), and Ca on the II site was unstable. The only hit was SrAg₂GeSe₄ at the window edge.

**Iteration 5: Si on the IV site of alkali kesterites; Fe/Co on the II site with K.**
- **Supported for K tellurides (5 hits):** replacing Ge with Si raised the gap by about 0.35 eV for the Cd and Mn tellurides.
- **Falsified for Na:** all Na-Si members were unstable except Na₂CaSiTe₄, whose gap (2.05 eV) was too wide.
- **K with Ca or Sr plus Si:** also unstable (about 0.10 eV/atom).
- **K₂(Fe,Co) selenides:** stable, and Fe opened a gap in the K lattice (unlike the metallic Fe members with Cu/Ag in iteration 1). But the gaps fell outside the window: Fe 0.44–0.63 eV, Co 2.12–2.31 eV.

## Caveats

- **Gap model error:** the one calibration point (ZnCu₂SnSe₄) was underestimated by about 0.6 eV. That was a Cu compound. No Ag, Na or K compound was calibrated, so the error for the hit families is unknown. Treat every gap as uncertain to several tenths of an eV.
- **Stability is incomplete:** Ehull compares only the relaxed kesterite cell with MP phases. Real alkali quaternary chalcogenides often take other structures; for example, the notebook notes that K₂MnSnSe₄ is in MP in a non-kesterite structure. Competing polymorphs were not searched, so "on hull" here does not mean thermodynamically stable.
- **CHGNet is a surrogate:** both the formation energies and Ehull values come from a machine-learned potential, not DFT.
- **Magnetic compounds:** for the Mn, Fe and Co members, it is uncertain how the model handles high-spin states and d–d physics.
- **Possible artefact:** the Na₂MgGeTe₄ / Na₂MgSnTe₄ gap inversion has not been explained.
- **Novelty is only relative to MP:** the literature searches were limited Crossref queries, so absence from MP does not prove a compound has never been reported.
- **Practical issues:** alkali tellurides are likely to be air- and moisture-sensitive. The model also did not determine whether the gaps are direct or indirect, or how strongly the materials absorb light.
- **Hits at the window edges:** several hits lie within 0.02 eV of the gap limits (Na₂MnSnSe₄, K₂CaSnTe₄, SrAg₂GeSe₄, K₂MgSiTe₄, K₂MnSiSe₄) or near the Ehull limit (K₂MnSiTe₄ at 0.045, Na₂MgGeTe₄ at 0.047). Given the error bars above, these should be treated as marginal.

## Recommended next steps

1. **DFT validation of the top hits:** K₂MnGeSe₄, K₂CaGeTe₄, K₂MgSnTe₄, K₂CdSiTe₄, Na₂CdSnTe₄, CdAg₂GeSe₄ and ZnAg₂GeSe₄. This means PBE/PBEsol relaxation and a convex hull, plus a search over competing polymorphs (for example the K₂BaSnTe₄-type and isolated-tetrahedra structures).
2. **HSE06 (or better) band gaps** for the same set, with spin-polarised treatment for the Mn compounds. Determine whether each gap is direct or indirect and compute the optical absorption.
3. **Recalibrate the gap model** on known Ag- and alkali-containing chalcogenides, so the uncertainty for these families is measured rather than inferred from one Cu compound.
4. **Resolve the Na₂MgGeTe₄ / Na₂MgSnTe₄ gap inversion** with a direct DFT calculation.
5. **Consider synthesis** only for the candidates that survive steps 1–2. Prefer those that are on the hull in DFT and have gaps near 1.4 eV, and account for how air-sensitive alkali tellurides and selenides are when handling and processing them.
