# Campaign report: pv-absorber-v1

## Executive summary

The campaign ran 5 iterations and scored 89 candidates. All of them were flagged novel against the Materials Project (MP). The target was a band gap of about 1.1–1.7 eV (aiming near 1.4 eV) with energy above hull ≤ 0.05 eV/atom. By these criteria 14 candidates were hits, but I trust only a subset of them. These are the non-magnetic, chemically plausible ones: **CdAg2GeSe4** (1.28 eV, hull 0.0), **ZnAg2GeSe4** (1.12 eV, hull 0.0), **KBiTe2** (1.30 eV, hull 0.003), **K2ZnSnTe4** (1.57 eV, hull 0.0) and **Na2CdSnTe4** (1.37 eV, hull 0.032). Every number is a surrogate-model prediction (CHGNet relaxation plus an HSE-fidelity gap model). Nothing has been checked with DFT or experiment. Several hits come from forcing a kesterite or chalcopyrite prototype onto chemistries that probably adopt other structures, and several others involve Mn, Ti or Zr. Treat all hits as hypotheses, not discoveries.

## Scored candidates

Ef is the formation energy in eV/atom, hull is the energy above hull in eV/atom, and gap is in eV. All entries converged and are novel versus MP. Hit = gap 1.1–1.7 eV and hull ≤ 0.05 eV/atom.

### Iteration 1 (Ag2-II-IV-VI4 kesterite-type)

| Formula | Ef | Hull | Gap | Hit |
|---|---|---|---|---|
| CdAg2GeSe4 | -0.657 | 0.000 | 1.279 | ✔ |
| ZnAg2GeSe4 | -0.681 | 0.000 | 1.119 | ✔ |
| MgAg2SnS4 | -1.177 | 0.002 | 1.871 | |
| MgAg2SnSe4 | -0.838 | 0.016 | 1.588 | ✔ |
| CdAg2GeTe4 | -0.326 | 0.017 | 0.481 | |
| MgAg2GeS4 | -1.165 | 0.017 | 1.893 | |
| MgAg2GeSe4 | -0.797 | 0.020 | 1.856 | |
| MgAg2GeTe4 | -0.423 | 0.025 | 1.490 | ✔ |
| ZnAg2GeTe4 | -0.318 | 0.028 | 1.171 | ✔ |
| ZnAg2SnTe4 | -0.358 | 0.039 | 0.596 | |
| CaAg2GeTe4 | -0.587 | 0.058 | 0.240 | |
| CaAg2GeSe4 | -0.949 | 0.062 | 1.679 | |
| CdSi(AgTe2)2 | -0.230 | 0.083 | 1.055 | |
| MgSi(AgTe2)2 | -0.331 | 0.087 | 1.802 | |
| CaSi(AgTe2)2 | -0.493 | 0.122 | 1.247 | |
| CdSi(AgSe2)2 | -0.568 | 0.130 | 1.714 | |
| MgSi(AgSe2)2 | -0.715 | 0.145 | 2.348 | |
| CaSi(AgSe2)2 | -0.867 | 0.187 | 2.510 | |

### Iteration 2 (Cu variants, Ti/Zr quaternaries, alkali I-III-VI2)

| Formula | Ef | Hull | Gap | Hit |
|---|---|---|---|---|
| ZrZn(AgS2)2 | -1.543 | 0.000 | 0.193 | |
| ZrZn(AgSe2)2 | -1.183 | 0.000 | 0.653 | |
| ZrZn(CuS2)2 | -1.556 | 0.000 | 0.296 | |
| ZrZn(CuSe2)2 | -1.188 | 0.000 | 0.205 | |
| TiZn(AgS2)2 | -1.547 | 0.000 | 1.554 | ✔ (suspect) |
| TiZn(CuS2)2 | -1.574 | 0.000 | 2.660 | |
| NaGaS2 | -1.810 | 0.000 | 3.827 | |
| TiMn(AgS2)2 | -1.513 | 0.000 | 1.480 | ✔ (suspect, Mn) |
| NaGaSe2 | -1.169 | 0.017 | 2.202 | |
| MgCu2SnS4 | -1.239 | 0.020 | 2.174 | |
| SrCu2SnSe4 | -1.045 | 0.050 | 1.109 | borderline (hull 0.0504) |
| MgCu2SnSe4 | -0.819 | 0.071 | 1.383 | |
| MnCu2GeSe4 | -0.531 | 0.104 | 0.931 | |
| MgCu2GeSe4 | -0.717 | 0.136 | 1.102 | |
| TiCd(AgS2)2 | -0.957 | 0.351 | 2.400 | |
| TiZn(AgSe2)2 | -0.617 | 0.353 | 2.229 | |
| MgTi(AgS2)2 | -1.143 | 0.364 | 1.948 | |
| TiZn(CuSe2)2 | -0.573 | 0.412 | 2.835 | |

### Iteration 3 (Ag2 kesterite remainder, pnictide chalcopyrites, alkali I-III/V-VI2)

| Formula | Ef | Hull | Gap | Hit |
|---|---|---|---|---|
| KGaSe2 | -1.275 | 0.000 | 2.177 | |
| KSbTe2 | -0.741 | 0.000 | 0.547 | |
| KBiTe2 | -0.736 | 0.003 | 1.296 | ✔ |
| CdAg2SnTe4 | -0.366 | 0.027 | 0.412 | |
| MgAg2SnTe4 | -0.461 | 0.038 | 1.172 | ✔ (marginal) |
| CaGeSb2 | -0.422 | 0.122 | 0.008 | |
| MgSnSb2 | -0.112 | 0.123 | 0.009 | |
| CdGeSb2 | 0.078 | 0.172 | 0.315 | |
| MgGeSb2 | -0.054 | 0.177 | 0.006 | |
| ZnGeSb2 | 0.110 | 0.199 | 0.229 | |
| CaSnAs2 | -0.463 | 0.215 | 0.027 | |
| CaGeAs2 | -0.455 | 0.220 | 0.653 | |
| SrSiAs2 | -0.464 | 0.242 | 1.735 | |
| CdSiSb2 | 0.171 | 0.251 | 0.548 | |
| ZnSiSb2 | 0.206 | 0.281 | 1.201 | |
| CaSiSb2 | -0.230 | 0.300 | 0.017 | |
| CaSiAs2 | -0.401 | 0.302 | 1.857 | |

### Iteration 4 (alkali A2-II-IV-VI4, A = Na, K)

| Formula | Ef | Hull | Gap | Hit |
|---|---|---|---|---|
| K2ZnSnSe4 | -1.222 | 0.000 | 2.265 | |
| K2ZnGeSe4 | -1.197 | 0.000 | 2.488 | |
| K2ZnSnTe4 | -1.001 | 0.000 | 1.573 | ✔ |
| K2CdSnTe4 | -0.899 | 0.000 | 0.864 | |
| K2ZnGeTe4 | -0.902 | 0.000 | 1.896 | |
| K2TiZnTe4 | -1.177 | 0.000 | 0.009 | |
| Na2ZnSnSe4 | -1.121 | 0.007 | 2.292 | |
| Na2ZnGeSe4 | -1.094 | 0.011 | 2.480 | |
| Na2ZnGeTe4 | -0.690 | 0.015 | 2.419 | |
| Na2CdSnSe4 | -1.085 | 0.019 | 1.957 | |
| Na2CdGeTe4 | -0.680 | 0.021 | 1.739 | |
| Na2ZnSnTe4 | -0.712 | 0.023 | 2.053 | |
| Na2CdGeSe4 | -1.052 | 0.029 | 2.413 | |
| Na2CdSnTe4 | -0.699 | 0.032 | 1.367 | ✔ |
| Na2MgGeSe4 | -1.186 | 0.055 | 2.448 | |
| Na2MgSnSe4 | -1.209 | 0.055 | 2.156 | |
| Na2MgSnTe4 | -0.782 | 0.055 | 1.932 | |
| BaNa2SnSe4 | -1.421 | 0.058 | 1.932 | |
| BaNa2SnTe4 | -1.004 | 0.066 | 1.704 | |
| Na2SrSnTe4 | -0.933 | 0.124 | 1.725 | |

### Iteration 5 (alkali Cd/Mn/Fe/Ti/Zr variants)

| Formula | Ef | Hull | Gap | Hit |
|---|---|---|---|---|
| K2CdGeTe4 | -0.863 | 0.000 | 0.884 | |
| K2CdGeSe4 | -1.169 | 0.000 | 2.409 | |
| K2MnSnTe4 | -0.932 | 0.000 | 0.646 | |
| Na2MnSnSe4 | -1.074 | 0.000 | 1.115 | ✔ (Mn, suspect) |
| Na2ZrMnTe4 | -1.001 | 0.000 | 1.493 | ✔ (suspect) |
| K2TiCdTe4 | -1.135 | 0.000 | -0.002 | |
| K2ZrCdTe4 | -1.237 | 0.000 | 2.124 | |
| Na2TiFeTe4 | -0.961 | 0.000 | 0.005 | |
| Na2ZrFeTe4 | -0.949 | 0.000 | 0.063 | |
| Na2MnGeSe4 | -1.035 | 0.008 | 1.646 | ✔ (Mn, suspect) |
| Na2FeSnSe4 | -1.011 | 0.036 | 0.808 | |
| Na2MnGeTe4 | -0.588 | 0.043 | 1.088 | near miss (gap just under 1.1) |
| Na2MnSnTe4 | -0.618 | 0.046 | 0.947 | |
| Na2FeGeTe4 | -0.576 | 0.079 | 0.012 | |
| Na2FeSnTe4 | -0.608 | 0.080 | 0.126 | |
| Na2TiMnTe4 | -0.493 | 0.333 | 0.004 | |

## Hypotheses tested and what was learned

**Iteration 1: Ag2-II-IV-VI4 kesterite-type (Zn/Cd/Mg/Ca, Si/Ge/Sn, S/Se/Te).**
- The hypothesis held. Ge and Sn selenides and tellurides gave stable gaps of about 1.1–1.6 eV.
- Si analogs were unstable (hull 0.08–0.19) and Ca analogs were unstable.
- The Mg sulfides were stable but had gaps of about 1.87–1.89 eV, too wide.
- CdAg2GeTe4 (0.48 eV) and ZnAg2SnTe4 (0.60 eV) had gaps that were too small.
- Chalcopyrite Ag variants were all already known, so they were not evaluated.
- Two relaxations went unspent.

**Iteration 2: Cu/mixed variants, Ti/Zr quaternaries, alkali I-III-VI2.**
- The Cu-variant hypothesis was mostly falsified. The Cu-Mg analogs were marginally unstable (MgCu2SnSe4 hull 0.071) or too wide in gap (MgCu2SnS4 at 2.17 eV).
- NaGaSe2 and NaGaS2 were too wide-gap.
- TiZn(AgS2)2 and TiMn(AgS2)2 landed in the window with hull 0.0. I flagged these as suspect for two reasons. Ti4+ prefers octahedral coordination, and the kesterite prototype forces tetrahedral. Hull 0.0 may also reflect sparse competing phases in MP.
- The Zr analogs had gaps of 0.19–0.65 eV, and the Ti-Se and Cd/Mg-Ti analogs were unstable (hull 0.35–0.41).
- Two relaxations went unspent.

**Iteration 3: remaining Ag2 kesterite members, II-IV-V2 pnictide chalcopyrites, alkali I-III-VI2.**
- The Ag2 kesterite family was exhausted, with only MgAg2SnTe4 (a marginal hit) and CdAg2SnTe4 (a miss) still novel.
- The pnictide hypothesis was clearly falsified. All the Sb/As chalcopyrites were unstable (hull 0.12–0.30) and mostly had the wrong gap. ZnSiSb2 had a 1.2 eV gap but a hull of 0.28.
- KGaSe2 was too wide (2.18 eV) and KSbTe2 too narrow (0.55 eV).
- KBiTe2 was a hit (1.30 eV, hull 0.003). It was forced into the chalcopyrite prototype, and its true ground state is probably layered or rocksalt-ordered.
- Three relaxations went unspent.

**Iteration 4: alkali A2-II-IV-VI4.**
- The Bi/Sb I-V-VI2 chalcopyrite relabelings were all reported as already considered, and the zincblende prototype only returned binaries. I therefore switched to alkali kesterite-type compounds.
- K2ZnSnTe4 (1.57 eV, hull 0.0) and Na2CdSnTe4 (1.37 eV, hull 0.032) were hits.
- The selenides were stable but too wide (about 1.96–2.49 eV).
- The Mg, Ba and Sr analogs had hull 0.055–0.12.
- Replacing Zn with Cd lowered the gap by about 0.7 eV in both K2SnTe4 and Na2SnTe4.
- K2TiZnTe4 came out metallic (gap about 0).

**Iteration 5: alkali Cd/Mn/Fe/Ti/Zr extensions.**
- The hypothesis held only partly. Cd with K, Ge and Te overshoots to 0.88 eV.
- Na2MnSnSe4 (1.115 eV, hull 0.0) and Na2MnGeSe4 (1.646 eV, hull 0.008) fell in the window. Mn magnetism makes their gaps unreliable.
- Na2ZrMnTe4 (1.49 eV, hull 0.0) also fell in the window, but Zr4+ in a tetrahedral site and the Mn make it suspect.
- The Fe and Ti analogs were metallic or small-gap.
- Four relaxations went unspent.

**Cross-cutting trends (from the data):**
- Te and Sn lower the gap, and Si destabilizes the structure.
- The Ge and Sn selenides and tellurides of the Ag2 kesterite family are the most robust window hits.
- Hull 0.0 values for Ti/Zr quaternaries should not be trusted.

## Caveats

- **Surrogate error.** Stability comes from CHGNet relaxations and hull energies against the MP reference set. Gaps come from an HSE-fidelity predictor. Neither has been validated, and the error bars are uncertain and could easily be a few tenths of an eV on gaps.
- **Prototype forcing.** Only three prototypes (chalcopyrite, kesterite, zincblende) were available. The kesterite-type structure was imposed on large-alkali and Ti/Zr compounds, and KBiTe2 was placed in a chalcopyrite-type cell. Real ground states are probably different. For the Ag2 compounds, wurtzstannite-type polymorphs are one example. For alkali tellurostannates the real structures may be non-tetrahedral. A wrong polymorph could change the gap and the hull.
- **Sparse competing phases.** Hull 0.0 for K, Ti and Zr quaternaries may reflect missing competing phases in MP rather than true stability.
- **Magnetic systems.** Gaps for Mn- and Fe-containing compounds (Na2MnSnSe4, Na2MnGeSe4, TiMn(AgS2)2 and others) are unreliable. The notebook notes uncertainty about the spin treatment.
- **Novelty.** "Novel" means absent from MP only. I did not check the broader literature or other databases, and no literature results are recorded in the notebook.
- **Window definition.** The 1.1–1.7 eV, hull ≤ 0.05 eV/atom window is the screening rule used here. It is not a device-level criterion, and effects such as absorption character and defect tolerance were not assessed.

## Recommended next steps

1. Run spin-polarized, hybrid-functional DFT (HSE) on the five trusted candidates: CdAg2GeSe4, ZnAg2GeSe4, KBiTe2, K2ZnSnTe4 and Na2CdSnTe4. Add MgAg2SnTe4 and MgAg2GeTe4 as lower-priority checks.
2. Check competing polymorphs for each candidate, including wurtzstannite-type for the Ag2 compounds and layered or rocksalt-ordered for KBiTe2. Rebuild the convex hulls with a more complete phase set.
3. Check phonon stability and computed absorption.
4. Treat the Ti/Zr/Mn/Fe compounds as low priority. That means TiZn(AgS2)2, TiMn(AgS2)2, Na2ZrMnTe4, Na2MnSnSe4 and Na2MnGeSe4. Revisit them only with proper site preference and magnetic treatment.
5. Fine-tune toward 1.4 eV with mixed-anion or mixed-cation alloys. Examples are ZnAg2GeSe4 with S, and Zn/Cd or Na/K mixes in A2MSnTe4. The current prototype tool does not support these, so this needs a workaround.
6. If any candidate survives the DFT checks, assess synthesis feasibility, with the Ag-based selenides first.
