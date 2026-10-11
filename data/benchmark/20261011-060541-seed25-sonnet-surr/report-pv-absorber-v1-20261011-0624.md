# Campaign report: pv-absorber-v1

## Executive summary

The campaign ran 5 iterations and scored 90 candidates. The target was a band gap near 1.4 eV (the notebook treats roughly 1.1–1.7 eV as the window) with low energy above hull (Eh). Most work was substitution on the kesterite prototype. Several novel compositions are predicted stable (Eh ≤ ~0.05 eV/atom) with gaps in or near the window. The closest to the target is **K2MnGeSe4** (Eh 0.000, gap 1.44 eV). Other candidates are CdAg2GeSe4 (1.28 eV), Na2CdSnTe4 (1.37 eV, Eh 0.032), ZnAg2GeSe4 and Na2MnSnSe4 (both ~1.12 eV). Confidence is moderate to low. All numbers come from CHGNet relaxation, a surrogate band-gap model and a hull built only from Materials Project, and nothing was checked by DFT or experiment. The Mn-containing gaps in particular may be unreliable (see Caveats). The substitution tool's design space looked largely exhausted by iteration 5, which found no new window hits.

## Scored candidates

Columns: Ef = formation energy (eV/atom), Eh = energy above hull (eV/atom), Eg = predicted band gap (eV). "Novel" means absent from Materials Project. Three entries are known compounds: ZnAg2SnSe4 was a deliberate calibration point, and ZnAg2GeS4 and CdCu2GeS4 were also flagged known. All 90 candidates converged.

### Iteration 1 (Ag/Cu kesterites, Zn/Cd/Mg, Ge/Sn, S/Se/Te)

| Formula | Ef | Eh | Eg | Novel |
|---|---|---|---|---|
| CdAg2GeSe4 | -0.657 | 0.000 | 1.28 | Y |
| ZnAg2GeSe4 | -0.681 | 0.000 | 1.12 | Y |
| ZnAg2SnSe4 | -0.721 | 0.000 | 1.12 | N (calibration) |
| MgAg2SnS4 | -1.177 | 0.002 | 1.87 | Y |
| MgAg2SnSe4 | -0.838 | 0.016 | 1.59 | Y |
| CdAg2GeTe4 | -0.326 | 0.017 | 0.48 | Y |
| MgAg2GeS4 | -1.165 | 0.017 | 1.89 | Y |
| MgCu2SnS4 | -1.239 | 0.020 | 2.17 | Y |
| MgAg2GeSe4 | -0.797 | 0.020 | 1.86 | Y |
| CdAg2SnTe4 | -0.366 | 0.027 | 0.41 | Y |
| ZnAg2GeTe4 | -0.318 | 0.028 | 1.17 | Y |
| ZnAg2SnTe4 | -0.358 | 0.039 | 0.60 | Y |
| MgCu2SnSe4 | -0.819 | 0.071 | 1.38 | Y |
| MgCu2GeSe4 | -0.717 | 0.136 | 1.10 | Y |

### Iteration 2 (Ca/Sr/Ba/Mn on the divalent site; Zr/Ti tetravalent variants)

| Formula | Ef | Eh | Eg | Novel |
|---|---|---|---|---|
| BaAg2GeTe4 | -0.704 | 0.000 | 0.70 | Y |
| SrAg2SnS4 | -1.369 | 0.000 | 1.72 | Y |
| ZrCd(AgSe2)2 | -1.148 | 0.000 | 0.30 | Y |
| SrAg2SnSe4 | -1.059 | 0.000 | 1.70 | Y |
| SrAg2GeSe4 | -1.021 | 0.003 | 1.69 | Y |
| SrAg2GeS4 | -1.354 | 0.013 | 1.87 | Y |
| SrAg2GeTe4 | -0.651 | 0.016 | 0.16 | Y |
| SrAg2SnTe4 | -0.689 | 0.029 | 0.10 | Y |
| SrCu2SnSe4 | -1.045 | 0.050 | 1.11 | Y |
| CaAg2SnSe4 | -0.998 | 0.051 | 1.82 | Y |
| CaAg2GeTe4 | -0.587 | 0.058 | 0.24 | Y |
| CaAg2GeSe4 | -0.949 | 0.062 | 1.68 | Y |
| CaAg2SnS4 | -1.297 | 0.068 | 2.28 | Y |
| CaAg2SnTe4 | -0.625 | 0.072 | 0.06 | Y |
| MnAg2GeS4 | -0.914 | 0.079 | 2.24 | Y |
| CaAg2GeS4 | -1.273 | 0.094 | 2.15 | Y |
| BaZr(AgSe2)2 | -0.989 | 0.405 | 2.17 | Y |
| SrZr(AgSe2)2 | -0.944 | 0.440 | 2.33 | Y |
| ZrCd(AgS2)2 | -0.946 | 0.451 | 2.36 | Y |
| CaZr(AgSe2)2 | -0.882 | 0.493 | 2.47 | Y |

### Iteration 3 (alkali kesterites A2MM'X4)

| Formula | Ef | Eh | Eg | Novel |
|---|---|---|---|---|
| Na2MnSnSe4 | -1.074 | 0.000 | 1.12 | Y |
| K2ZnSnSe4 | -1.222 | 0.000 | 2.26 | Y |
| K2CdGeSe4 | -1.169 | 0.000 | 2.41 | Y |
| K2CdSnTe4 | -0.899 | 0.000 | 0.86 | Y |
| K2CdGeTe4 | -0.863 | 0.000 | 0.88 | Y |
| K2MnGeSe4 | -1.142 | 0.000 | 1.44 | Y |
| Na2ZnSnSe4 | -1.121 | 0.007 | 2.29 | Y |
| Na2MnGeSe4 | -1.035 | 0.008 | 1.65 | Y |
| Na2ZnGeSe4 | -1.094 | 0.011 | 2.48 | Y |
| Na2ZnGeTe4 | -0.690 | 0.015 | 2.42 | Y |
| Na2CdSnSe4 | -1.085 | 0.019 | 1.96 | Y |
| Na2CdGeTe4 | -0.680 | 0.021 | 1.74 | Y |
| Na2ZnSnTe4 | -0.712 | 0.023 | 2.05 | Y |
| Na2CdGeSe4 | -1.052 | 0.029 | 2.41 | Y |
| Na2CdSnTe4 | -0.699 | 0.032 | 1.37 | Y |
| ZnAg2GeS4 | -1.000 | 0.037 | 2.31 | N |
| Na2MnGeTe4 | -0.588 | 0.043 | 1.09 | Y |
| Na2MnSnTe4 | -0.618 | 0.046 | 0.95 | Y |
| Na2MgSnSe4 | -1.209 | 0.055 | 2.16 | Y |
| CdCu2GeS4 | -0.953 | 0.105 | 1.85 | N |

### Iteration 4 (alkali sulfide kesterites with Mn/Fe/Co/Ni)

| Formula | Ef | Eh | Eg | Novel |
|---|---|---|---|---|
| Na2MnGeS4 | -1.435 | 0.000 | 2.15 | Y |
| Na2MnSnS4 | -1.449 | 0.000 | 2.14 | Y |
| K2MnGeS4 | -1.530 | 0.000 | 1.88 | Y |
| K2MnSnS4 | -1.546 | 0.000 | 2.24 | Y |
| K2NiGeSe4 | -1.111 | 0.000 | 2.02 | Y |
| K2NiGeS4 | -1.488 | 0.000 | 1.73 | Y |
| Na2NiGeS4 | -1.387 | 0.000 | 1.76 | Y |
| Na2NiSnS4 | -1.388 | 0.000 | 1.83 | Y |
| K2NiSnS4 | -1.479 | 0.000 | 1.82 | Y |
| K2NiGeTe4 | -0.744 | 0.000 | 0.65 | Y |
| K2FeGeS4 | -1.476 | 0.006 | 1.72 | Y |
| K2CoGeS4 | -1.462 | 0.006 | 1.84 | Y |
| K2FeSnS4 | -1.476 | 0.014 | 2.01 | Y |
| K2CoSnS4 | -1.451 | 0.026 | 2.21 | Y |
| Na2FeGeS4 | -1.395 | 0.033 | 0.10 | Y |
| Na2CoSnS4 | -1.362 | 0.040 | 2.29 | Y |
| Na2FeSnS4 | -1.384 | 0.045 | 0.87 | Y |
| Na2CoGeS4 | -1.359 | 0.055 | 1.29 | Y |

### Iteration 5 (Fe/Co/Mn Ag kesterites; ABX2-type Mn/Co/Fe compounds; Ti/Zr)

| Formula | Ef | Eh | Eg | Novel |
|---|---|---|---|---|
| NaMnS2 | -1.648 | 0.000 | 0.82 | Y |
| KMnS2 | -1.761 | 0.000 | 1.79 | Y |
| MnAgS2 | -1.213 | 0.000 | 0.37 | Y |
| NaCoS2 | -1.479 | 0.000 | 0.01 | Y |
| KCoS2 | -1.564 | 0.000 | 0.64 | Y |
| NaFeTe2 | -0.715 | 0.000 | 0.01 | Y |
| FeAg2SnSe4 | -0.579 | 0.072 | 0.00 | Y |
| CoAg2GeSe4 | -0.524 | 0.075 | 0.81 | Y |
| FeAg2GeSe4 | -0.525 | 0.078 | 0.02 | Y |
| KCoSe2 | -0.882 | 0.085 | 0.23 | Y |
| CoAg2GeTe4 | -0.229 | 0.087 | 0.00 | Y |
| MnAgSe2 | -0.476 | 0.100 | 1.08 | Y |
| FeAg2GeTe4 | -0.199 | 0.112 | 0.01 | Y |
| FeAg2SnTe4 | -0.243 | 0.119 | 0.01 | Y |
| NaFeSe2 | -0.834 | 0.131 | 1.75 | Y |
| FeAg2GeS4 | -0.851 | 0.135 | 0.01 | Y |
| CoAgS2 | -0.631 | 0.305 | 0.01 | Y |
| TiCd(AgSe2)2 | -0.590 | 0.357 | 2.35 | Y |

### Best novel candidates (Eh ≤ ~0.05 eV/atom, gap near 1.1–1.7 eV)

| Formula | Eh | Eg | Comment |
|---|---|---|---|
| K2MnGeSe4 | 0.000 | 1.44 | Closest to 1.4 eV; Mn-containing |
| CdAg2GeSe4 | 0.000 | 1.28 | |
| Na2CdSnTe4 | 0.032 | 1.37 | Slightly above hull |
| ZnAg2GeSe4 | 0.000 | 1.12 | |
| Na2MnSnSe4 | 0.000 | 1.12 | Mn-containing |
| ZnAg2GeTe4 | 0.028 | 1.17 | |
| MgAg2SnSe4 | 0.016 | 1.59 | |
| Na2MnGeSe4 | 0.008 | 1.65 | Mn-containing |
| SrAg2GeSe4 | 0.003 | 1.69 | Upper edge of window |
| SrAg2SnSe4 | 0.000 | 1.70 | Just outside window |
| SrCu2SnSe4 | 0.050 | 1.11 | Borderline on both stability and gap |

## Hypotheses tested and what was learned

**Iteration 1: Ag/Cd/Mg isoelectronic kesterites.** This largely held. Ag selenide kesterites are predicted stable with gaps of 1.1–1.6 eV. Mg sulfides and Mg-Ge selenides were too wide (1.86–1.89 eV). Tellurides were mostly below 0.6 eV, except the Zn/Ge telluride at 1.17 eV. Cu-Mg variants were marginal: MgCu2SnSe4 had gap 1.38 eV but Eh 0.071, and MgCu2GeSe4 had Eh 0.136. Si variants were vetoed by the critic for size mismatch.

**Iteration 2: larger divalent cations (Ca/Sr/Ba/Mn) and Zr/Ti on the tetravalent site.** This partly held.
- Sr fits the kesterite site (SrAg2GeSe4 and SrAg2SnSe4 have Eh ≤ 0.003), but their gaps are 1.69–1.70 eV, at or just above the window edge.
- Ca is too small: Eh rises to 0.05–0.09.
- Zr/Ti kesterite-type variants are unstable (Eh 0.36–0.49), except ZrCd(AgSe2)2 (Eh 0, gap 0.30 eV).
- Sr/Ba tellurides are stable but have gaps of only 0.1–0.7 eV.
- SrCu2SnSe4 (gap 1.11 eV, Eh 0.050) suggests Cu lowers the gap relative to Ag.

**Iteration 3: pivot to alkali kesterites (Na/K for Cu/Ag).** This was the most productive pivot.
- The Mn-on-divalent-site members gave window or near-window gaps: K2MnGeSe4 (1.44 eV), Na2MnGeSe4 (1.65 eV) and Na2MnSnSe4 (1.12 eV).
- Na2CdSnTe4 also fell in the window (1.37 eV, Eh 0.032).
- Zn/Cd/Mg selenides were too wide (~1.96–2.5 eV).
- K tellurides were too narrow (0.86–0.88 eV).
- The notebook attributes the lowered Mn gaps to Mn d states. This is an interpretation and was not tested.
- Ag/Cu kesterite space was reported as "already considered" by the proposal tool, and Ba variants were vetoed for size mismatch.

**Iteration 4: sulfides with Mn/Fe/Co/Ni.** This was mostly falsified. Nearly all 18 compounds were stable (Eh ≤ ~0.045 for most), but gaps were mostly 1.7–2.3 eV. The only in-window sulfide was Na2CoGeS4 (1.29 eV), which has Eh 0.055. K2FeGeS4 (1.72 eV) and K2NiGeS4 (1.73 eV) sit just above the window. The Na2Fe sulfides had gaps of 0.10 and 0.87 eV. No new stable window hit came from this iteration.

**Iteration 5: Fe/Co Ag kesterites and ABX2-type Mn/Co/Fe compounds.** This was falsified.
- Fe/Co Ag kesterites are unstable (Eh 0.07–0.135) and essentially metallic (gap ≈ 0), except CoAg2GeSe4 (0.81 eV, Eh 0.075).
- The ABX2-type compounds that came out stable have gaps outside the window: NaCoS2 (0.01 eV), KCoS2 (0.64 eV), MnAgS2 (0.37 eV), NaMnS2 (0.82 eV), NaFeTe2 (0.01 eV) and KMnS2 (1.79 eV).
- Se analogues of alkali Fe/Co/Ni/Mn kesterites were blocked by the "already considered" filter, and the zincblende prototype gave no novel candidates.

**Overall lesson:** Cd and Mn on the divalent site, combined with Ag or alkali on the monovalent site, gave the window gaps. Fe/Co/Ni gave gaps that were too narrow or too wide. S/Se/Te anion choice is a strong gap lever, but with discrete substitutions it tends to overshoot the window.

## Caveats

- **Computational level.** All values come from CHGNet relaxations with a surrogate "HSE-fidelity" band-gap predictor. No DFT, hybrid-functional or phonon calculations were run, and no synthesis was attempted. The gap model's error bars were not quantified in this campaign. Errors of several tenths of an eV would change which candidates sit in the window.
- **Hull.** Stability is judged only against Materials Project phases, so Eh ≈ 0 means "not beaten by known MP competitors". Unknown competing phases could make a candidate unstable. "Novel" likewise means only "absent from MP". The literature was not systematically checked for each candidate.
- **Mn compounds.** K2MnGeSe4, Na2MnGeSe4 and Na2MnSnSe4 contain magnetic Mn. The notebook flags that gaps may be unreliable if magnetism is not treated properly. Spin state and magnetic ordering were not verified.
- **Surrogate.** The Gaussian-process surrogate had no data in iteration 1, and its advice (e.g. favouring tellurides in iteration 4) was not borne out. It was advisory and played a minor role.
- **Scope.** The window width and the Eh ≤ ~0.05 criterion were used loosely. Several "near misses" (Eh 0.05–0.055 or gaps 1.7–1.8 eV) are borderline. No quantities relevant to photovoltaic performance beyond gap and Eh were assessed (absorption, defects, band alignment, carrier transport, toxicity or cost; Cd-containing hits would face toxicity concerns).
- **Record-keeping.** Iteration 4 reflected on Se analogues whose details were "unrecorded". Candidate properties above come from the campaign database, which is the authoritative source.

## Recommended next steps

1. Re-compute the top candidates with DFT (HSE or a hybrid functional, with spin polarisation for the Mn compounds) and a full competing-phase hull, including binary and ternary phases not in MP. Prioritise K2MnGeSe4, CdAg2GeSe4, ZnAg2GeSe4, Na2MnSnSe4, Na2CdSnTe4 and MgAg2SnSe4.
2. Check phonon/dynamical stability and the kesterite versus alternative polymorph energetics for these compositions.
3. Test gap tuning by mixing rather than endmember substitution, since discrete substitutions overshoot the window. Examples are Sr(Ag,Cu)2SnSe4, S/Se mixing in the Mn alkali kesterites, and Cd/Zn or Cd/Mg mixing on the divalent site. The prototype tool cannot express these directly, so they would need custom structure generation.
4. Screen the literature for each hit before any synthesis attempt, and assess synthetic accessibility. Prefer the non-toxic hits, such as the Mn and Zn compounds, over the Cd-containing ones.
