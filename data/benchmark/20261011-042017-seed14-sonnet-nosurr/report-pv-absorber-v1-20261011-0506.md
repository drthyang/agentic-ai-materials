# Campaign report: pv-absorber-v1

## Executive summary

Over five iterations the campaign scored 93 candidates (16, 17, 20, 20 and 20 per iteration) by CHGNet relaxation with a surrogate HSE-fidelity band gap. The target was a gap near 1.4 eV, and the notebook counted a "hit" as hull energy ≤ 0.05 eV/atom with a gap of 1.1–1.7 eV. By that criterion, 18 novel candidates qualified. Six are Ag-based kesterite-type selenides and tellurides (iteration 1). Four are alkali (K/Na) tellurides from iteration 4, and eight are K-based tellurides with alkaline-earth or Cd on the II site from iteration 5. The strongest cases are K2CaGeTe4 (1.42 eV, hull 0.019), K2MgSnTe4 (1.33 eV, hull 0.0) and CdAg2GeSe4 (1.28 eV, hull 0.0). All of these are surrogate-model predictions with no DFT or experimental validation. "Novel" means only that a compound is absent from the Materials Project database. Confidence is therefore moderate at best, especially for the alkali tellurides, whose true ground-state structures may not be the tetrahedral kesterite-like type that was modelled.

## Scored candidates

Columns: Ef = formation energy (eV/atom), Hull = energy above hull (eV/atom), Gap = predicted band gap (eV). Novel = absent from Materials Project. Every candidate listed is novel except the two marked "no" (iteration 2). Hits (hull ≤ 0.05 and gap 1.1–1.7) are marked ★.

### Iteration 1 (Ag/Cu kesterite-type)
| Formula | Ef | Hull | Gap | Note |
|---|---|---|---|---|
| CdAg2GeSe4 | -0.657 | 0.000 | 1.279 | ★ |
| ZnAg2GeSe4 | -0.681 | 0.000 | 1.119 | ★ |
| MgAg2SnS4 | -1.177 | 0.002 | 1.871 | gap too wide |
| MgAg2SnSe4 | -0.838 | 0.016 | 1.588 | ★ |
| CdAg2GeTe4 | -0.326 | 0.017 | 0.481 | gap too low |
| MgAg2GeSe4 | -0.797 | 0.020 | 1.856 | gap too wide |
| MgAg2GeTe4 | -0.423 | 0.025 | 1.490 | ★ |
| CdAg2SnTe4 | -0.366 | 0.027 | 0.412 | gap too low |
| ZnAg2GeTe4 | -0.318 | 0.028 | 1.171 | ★ |
| MgAg2SnTe4 | -0.461 | 0.038 | 1.172 | ★ |
| ZnAg2SnTe4 | -0.358 | 0.039 | 0.596 | gap too low |
| CdSi(AgTe2)2 | -0.230 | 0.083 | 1.055 | unstable |
| MgCu2GeTe4 | -0.372 | 0.101 | 0.895 | unstable |
| CdSi(AgSe2)2 | -0.568 | 0.130 | 1.714 | unstable |
| MgCu2GeSe4 | -0.717 | 0.136 | 1.102 | unstable |
| MgSi(AgSe2)2 | -0.715 | 0.145 | 2.348 | unstable |

### Iteration 2 (d-block Ag2-M-IV-X4 and II-IV-V2 pnictides)
| Formula | Ef | Hull | Gap | Note |
|---|---|---|---|---|
| CoAg2SnSe4 | -0.569 | 0.056 | 0.603 | |
| MgCu2SnSe4 | -0.819 | 0.071 | 1.383 | near-miss on hull |
| FeAg2SnSe4 | -0.579 | 0.072 | -0.003 | metallic |
| CoAg2GeSe4 | -0.524 | 0.075 | 0.809 | |
| FeAg2GeSe4 | -0.525 | 0.078 | 0.018 | metallic |
| MnAg2GeS4 | -0.914 | 0.079 | 2.236 | |
| CoAg2SnS4 | -0.860 | 0.092 | 1.388 | gap OK, unstable |
| CoAg2GeS4 | -0.835 | 0.113 | 1.512 | gap OK, unstable |
| MgSnSb2 | -0.112 | 0.123 | 0.009 | |
| FeAg2GeS4 | -0.851 | 0.135 | 0.013 | metallic |
| CdGeSb2 | 0.078 | 0.172 | 0.315 | |
| MgGeSb2 | -0.054 | 0.177 | 0.006 | |
| ZnGeSb2 | 0.110 | 0.199 | 0.229 | |
| CdSiSb2 | 0.171 | 0.251 | 0.548 | |
| CdSiAs2 | 0.074 | 0.254 | 1.863 | novel = no (known) |
| ZnSiSb2 | 0.206 | 0.281 | 1.201 | unstable |
| MgSiSb2 | 0.164 | 0.381 | 1.487 | novel = no (known) |

### Iteration 3 (Ca/Sr/Ba-Ag/Cu chalcogenides)
| Formula | Ef | Hull | Gap | Note |
|---|---|---|---|---|
| SrAg2SnS4 | -1.369 | 0.000 | 1.720 | just wide |
| SrAg2SnSe4 | -1.059 | 0.000 | 1.701 | 0.001 eV above window |
| BaAg2GeTe4 | -0.704 | 0.000 | 0.705 | gap too low |
| BaAg2SnTe4 | -0.746 | 0.007 | 0.516 | gap too low |
| SrAg2GeS4 | -1.354 | 0.013 | 1.867 | gap too wide |
| MgAg2GeS4 | -1.165 | 0.017 | 1.893 | gap too wide |
| SrAg2SnTe4 | -0.689 | 0.029 | 0.100 | gap too low |
| SrCu2SnSe4 | -1.045 | 0.0504 | 1.109 | borderline: hull marginally above 0.05 |
| CaAg2SnSe4 | -0.998 | 0.051 | 1.816 | |
| CaAg2SnS4 | -1.297 | 0.068 | 2.279 | |
| CaAg2SnTe4 | -0.625 | 0.072 | 0.062 | |
| CaCu2SnS4 | -1.371 | 0.072 | 2.704 | |
| CaAg2GeS4 | -1.273 | 0.094 | 2.158 | |
| CaCu2GeS4 | -1.340 | 0.096 | 2.563 | |
| CaCu2SnSe4 | -0.979 | 0.108 | 0.944 | |
| BaSi(AgSe2)2 | -0.987 | 0.114 | 2.245 | |
| CaCu2GeSe4 | -0.928 | 0.121 | 1.198 | unstable |
| BaTi(AgSe2)2 | -0.997 | 0.312 | 2.397 | |
| SrTi(AgSe2)2 | -0.938 | 0.373 | 2.357 | |
| BaZr(AgSe2)2 | -0.989 | 0.405 | 2.173 | |

### Iteration 4 (Na/K-II-IV-Se/Te)
| Formula | Ef | Hull | Gap | Note |
|---|---|---|---|---|
| K2CdSnTe4 | -0.899 | 0.000 | 0.864 | gap too low |
| K2CdGeSe4 | -1.169 | 0.000 | 2.409 | |
| K2CdGeTe4 | -0.863 | 0.000 | 0.884 | gap too low |
| K2ZnSnSe4 | -1.222 | 0.000 | 2.265 | |
| K2ZnSnTe4 | -1.001 | 0.000 | 1.573 | ★ |
| K2ZnGeTe4 | -0.902 | 0.000 | 1.896 | |
| K2MgSnTe4 | -0.977 | 0.000 | 1.329 | ★ |
| K2ZnGeSe4 | -1.197 | 0.000 | 2.488 | |
| Na2ZnSnSe4 | -1.121 | 0.007 | 2.292 | |
| Na2ZnGeSe4 | -1.094 | 0.011 | 2.480 | |
| Na2ZnGeTe4 | -0.690 | 0.015 | 2.419 | |
| Na2CdSnSe4 | -1.085 | 0.019 | 1.957 | |
| Na2CdGeTe4 | -0.680 | 0.021 | 1.739 | just wide |
| Na2ZnSnTe4 | -0.712 | 0.023 | 2.053 | |
| Na2CdGeSe4 | -1.052 | 0.029 | 2.413 | |
| K2MgSnSe4 | -1.311 | 0.030 | 2.536 | |
| Na2CdSnTe4 | -0.699 | 0.032 | 1.367 | ★ |
| Na2MgGeTe4 | -0.759 | 0.047 | 1.136 | ★ |
| Na2MgSnSe4 | -1.209 | 0.055 | 2.156 | |
| Na2MgSnTe4 | -0.782 | 0.055 | 1.932 | |

### Iteration 5 (K/Na-Te with Ca/Sr/Ba/Si)
| Formula | Ef | Hull | Gap | Note |
|---|---|---|---|---|
| K2BaGeTe4 | -1.187 | 0.000 | 1.566 | ★ |
| Na2CaGeTe4 | -1.098 | 0.000 | 1.731 | just wide |
| K2CdSiTe4 | -0.798 | 0.000 | 1.235 | ★ |
| K2ZnSiTe4 | -0.802 | 0.000 | 2.069 | |
| K2BaSiTe4 | -1.122 | 0.000 | 1.642 | ★ |
| K2MgSiTe4 | -0.868 | 0.005 | 1.692 | ★ (edge) |
| K2SrSnTe4 | -1.128 | 0.012 | 1.199 | ★ |
| K2SrGeTe4 | -1.087 | 0.013 | 1.216 | ★ |
| K2CaGeTe4 | -1.059 | 0.019 | 1.421 | ★ |
| K2CaSnTe4 | -1.084 | 0.033 | 1.118 | ★ |
| BaNa2GeTe4 | -0.978 | 0.063 | 1.759 | |
| BaNa2SnTe4 | -1.004 | 0.066 | 1.704 | |
| Na2ZnSiTe4 | -0.615 | 0.094 | 2.791 | |
| K2CaSiTe4 | -0.972 | 0.098 | 1.455 | unstable |
| K2SrSiTe4 | -0.987 | 0.105 | 1.875 | |
| Na2CdSiTe4 | -0.600 | 0.105 | 1.796 | |
| Na2SrGeTe4 | -0.913 | 0.113 | 1.692 | unstable |
| Na2SrSnTe4 | -0.933 | 0.124 | 1.725 | |
| Na2MgSiTe4 | -0.677 | 0.134 | 2.155 | |
| Na2CaSnTe4 | -0.865 | 0.169 | 1.458 | gap OK, unstable |

## Hypotheses tested and what was learned

**Iteration 1: Ag/Cu kesterites with isoelectronic substitution.**
- The hypothesis was that Ag on the Cu site and Cd/Mg/Zn/Ge/Sn/Se/Te substitutions would give novel kesterites with gaps of about 1.1–1.7 eV.
- It was supported. Six hits came out: CdAg2GeSe4, ZnAg2GeSe4, MgAg2SnSe4, MgAg2GeTe4, ZnAg2GeTe4 and MgAg2SnTe4.
- Si variants were unstable (hull > 0.08). The Cd/Zn-Ag-SnTe4 phases had gaps below 0.6 eV.
- The critic vetoed Ca, Sr and Zr as outside scope. Four relaxations went unspent because no unvetted novel candidates remained in scope.

**Iteration 2: chalcopyrite-type II-IV-V2 pnictides and d-block Ag2-M-IV-X4.**
- The hypothesis was falsified; there were no hits.
- The zincblende prototype returned only known binaries, and the I-III-VI2 chalcopyrite candidates were nearly all known.
- The II-IV-Sb2 antimonides had hull energies of 0.12–0.38 eV/atom and mostly small gaps.
- Mn/Fe/Co on the II site gave hull energies of 0.056–0.135. Fe gave metallic gaps.
- CoAg2SnS4 (1.39 eV) and CoAg2GeS4 (1.51 eV) had suitable gaps but were unstable.
- MgCu2SnSe4 (1.38 eV, hull 0.071) was a near-miss.
- CdSiAs2 and MgSiSb2 turned out to be known compounds (novel = 0), so those relaxations were wasted.

**Iteration 3: larger alkaline-earth cations (Ca/Sr/Ba) in Ag/Cu chalcogenides.**
- It produced no candidate that strictly meets the hit criteria.
- Sr and Ba stabilised the phases. SrAg2SnSe4 (hull 0, 1.701 eV) and SrAg2SnS4 (hull 0, 1.72 eV) sit just above the window.
- SrCu2SnSe4 (hull 0.0504, 1.109 eV) is borderline and fails the 0.05 cutoff by a hair. The notebook called it a marginal hit.
- Ca variants were unstable or had wide gaps.
- The Sr/Ba tellurides were stable but had gaps of 0.06–0.7 eV, which is too low.
- Ti/Zr/Si with Sr/Ba gave hull energies of 0.11–0.41, so they were falsified.
- Cu-Sr/Ba variants beyond SrCu2SnSe4 were not scored. The notebook says they were "already considered (rejected)".

**Iteration 4: alkali (Na/K) on the I site.**
- The hypothesis was supported, with four hits: K2MgSnTe4 (1.33 eV, hull 0), K2ZnSnTe4 (1.57 eV, hull 0), Na2CdSnTe4 (1.37 eV, hull 0.032) and Na2MgGeTe4 (1.14 eV, hull 0.047).
- The Se variants all had gaps near 2 eV or higher (too wide).
- K2Cd-Te had gaps of 0.86–0.88 eV (too low).
- Te was needed to bring the gap into range, and K was generally more stable than Na.
- The notebook notes that K2CdSnSe4 is already in Materials Project, which makes the family plausible.

**Iteration 5: extending the alkali-Te family to Ca/Sr/Ba and Si.**
- The hypothesis was supported for K-based phases, with eight hits (K2CaGeTe4, K2BaGeTe4, K2CdSiTe4, K2BaSiTe4, K2SrSnTe4, K2SrGeTe4, K2CaSnTe4, K2MgSiTe4).
- K2ZnSiTe4 was too wide (2.07 eV), and K2CaSiTe4 and K2SrSiTe4 were unstable (hull ~0.1).
- Na analogues were mostly unstable (hull 0.06–0.17). The exception was Na2CaGeTe4 (hull 0, 1.73 eV), which sits just above the window.

**Overall trends:**
- Te with Ge/Sn is the sweet spot for the alkali phases.
- Large, electropositive cations (K, Sr, Ba) stabilise these chalcogenides.
- d-block II-site cations destabilise them.
- Gap falls steeply along S > Se > Te.

## Caveats

- **Surrogate error.** All numbers come from CHGNet relaxations plus a surrogate HSE-fidelity gap predictor. Neither error bar was quantified in this campaign. Hull values below about 0.05 eV/atom are within the typical uncertainty of such models.
- **Hull reference.** Stability is measured only against competing phases in the database. Unknown quaternary polymorphs could undercut these compounds.
- **Structure assumption.** Candidates were built on kesterite-type prototypes. This is a particular concern for the K2/Na2-II-IV-Te4 phases. The notebook flags that their true ground states may be non-tetrahedral, for example edge-sharing or layered structures. Structure prediction or polymorph screening was not performed.
- **Novelty.** Novelty was checked only against Materials Project. Literature or ICSD coverage was not exhaustively verified.
- **Property scope.** No defect, dopability, absorption, band-alignment, toxicity or air-stability analysis was done. Te-rich alkali compounds are likely to be hygroscopic or air-sensitive, though this was not computed.
- **Edge cases.** SrAg2SnSe4 (1.701 eV) and SrCu2SnSe4 (hull 0.0504) miss the window by about 0.001 eV each, which is well inside the model error. The cutoff is a convention, not a physical boundary.

## Recommended next steps

1. Run DFT (PBE/HSE) relaxations and gap calculations for the top candidates. Start with K2CaGeTe4, K2MgSnTe4, K2BaGeTe4, K2ZnSnTe4, CdAg2GeSe4, ZnAg2GeSe4 and MgAg2SnSe4. Add phonon checks for dynamic stability.
2. Screen competing polymorphs and non-tetrahedral structure types for the K2-AE/Cd-IV-Te4 family. Recompute the hull with those phases included.
3. Test whether Se/Te anion mixing or Sr–Ge/Sn alloying can pull SrAg2SnSe4 and Na2CaGeTe4 into the window. The notebook proposed this but it was not run.
4. Assess air and moisture stability, and the synthetic accessibility of the alkali tellurides, before committing to experiments.
5. Prioritise the Ag-based selenides (CdAg2GeSe4, ZnAg2GeSe4) for synthesis attempts, since they have hull energy 0 and are chemically closer to known absorbers.
