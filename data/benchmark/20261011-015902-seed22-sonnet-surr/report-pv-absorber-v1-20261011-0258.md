# Campaign report: pv-absorber-v1

## Executive summary

The campaign ran 5 iterations and scored 95 compositions with CHGNet relaxation, energy above hull and a predicted HSE-fidelity band gap. Applying the campaign's own screen (novel, E_hull ≤ 0.05 eV/atom, gap 1.1–1.7 eV) to the database gives **15 candidates**. They come from four chemical families: Ag-based selenide and telluride kesterites, a Ti–S–Ag compound, K/Na telluride kesterites, and KBiTe2.

The best of these sit at 1.28–1.37 eV. Na2CdSnTe4 (1.367 eV, E_hull 0.032) is closest to the 1.4 eV target. K2MgSnTe4 (1.329 eV, E_hull 0.000) and KBiTe2 (1.296 eV, E_hull 0.003) come next.

**Confidence is low to moderate.** Everything is computational and unvalidated by DFT or synthesis. The notebook itself records that the CHGNet hull references look patchy, and that several structures (K compounds, KBiTe2, Sr kesterites) are probably not true ground states. The numbers are screening-level only.

## Scored candidates

Columns: iteration, formula, formation energy per atom (eV), E_hull (eV/atom), predicted gap (eV), and novelty vs Materials Project as flagged in the campaign database. All 95 rows converged. Values are rounded.

| It | Formula | E_form | E_hull | Gap | Novel |
|---|---|---|---|---|---|
| 1 | CdAg2GeSe4 | -0.657 | 0.000 | 1.279 | yes |
| 1 | ZnAg2GeSe4 | -0.681 | 0.000 | 1.119 | yes |
| 1 | SrAg2SnSe4 | -1.059 | 0.000 | 1.701 | yes |
| 1 | MgAg2SnS4 | -1.177 | 0.002 | 1.871 | yes |
| 1 | SrAg2GeSe4 | -1.021 | 0.003 | 1.687 | yes |
| 1 | MgAg2SnSe4 | -0.838 | 0.016 | 1.588 | yes |
| 1 | MgAg2GeS4 | -1.165 | 0.017 | 1.893 | yes |
| 1 | MgCu2SnS4 | -1.239 | 0.020 | 2.174 | yes |
| 1 | MgAg2GeSe4 | -0.797 | 0.020 | 1.856 | yes |
| 1 | CaAg2SnSe4 | -0.998 | 0.051 | 1.816 | yes |
| 1 | CaAg2GeSe4 | -0.949 | 0.062 | 1.679 | yes |
| 1 | CaAg2SnS4 | -1.297 | 0.068 | 2.279 | yes |
| 1 | MgCu2SnSe4 | -0.819 | 0.071 | 1.383 | yes |
| 1 | FeAg2SnSe4 | -0.579 | 0.072 | -0.003 | yes |
| 1 | CaCu2SnS4 | -1.371 | 0.072 | 2.704 | yes |
| 1 | MnAg2GeS4 | -0.914 | 0.079 | 2.236 | yes |
| 1 | MnCu2GeSe4 | -0.531 | 0.104 | 0.931 | yes |
| 1 | CaCu2SnSe4 | -0.979 | 0.108 | 0.944 | yes |
| 1 | CaCu2GeSe4 | -0.928 | 0.121 | 1.198 | yes |
| 1 | MgCu2GeSe4 | -0.717 | 0.136 | 1.102 | yes |
| 2 | CdAg2SnSe4 | -0.700 | 0.000 | 1.262 | no |
| 2 | ZnAg2SnSe4 | -0.721 | 0.000 | 1.124 | no |
| 2 | CdAg2SnS4 | -0.995 | 0.000 | 2.146 | no |
| 2 | ZnAg2SnS4 | -1.022 | 0.009 | 2.010 | no |
| 2 | SrAg2GeTe4 | -0.651 | 0.016 | 0.155 | yes |
| 2 | CdAg2GeTe4 | -0.326 | 0.017 | 0.481 | yes |
| 2 | CdAg2GeS4 | -0.974 | 0.025 | 2.211 | no |
| 2 | MgAg2GeTe4 | -0.423 | 0.025 | 1.490 | yes |
| 2 | CdAg2SnTe4 | -0.366 | 0.027 | 0.412 | yes |
| 2 | ZnAg2GeTe4 | -0.318 | 0.028 | 1.171 | yes |
| 2 | SrAg2SnTe4 | -0.689 | 0.029 | 0.100 | yes |
| 2 | ZnAg2GeS4 | -1.000 | 0.037 | 2.308 | no |
| 2 | MgAg2SnTe4 | -0.461 | 0.038 | 1.172 | yes |
| 2 | ZnAg2SnTe4 | -0.358 | 0.039 | 0.596 | yes |
| 2 | ZnCu2SnSe4 | -0.698 | 0.057 | 0.343 | no |
| 2 | ZnCu2GeSe4 | -0.651 | 0.066 | 0.851 | no |
| 2 | CdCu2SnSe4 | -0.638 | 0.093 | 0.283 | no |
| 2 | CdCu2GeSe4 | -0.584 | 0.110 | 0.530 | no |
| 3 | ZrZn(AgSe2)2 | -1.183 | 0.000 | 0.653 | yes |
| 3 | ZrCd(AgSe2)2 | -1.148 | 0.000 | 0.295 | yes |
| 3 | ZrZn(AgS2)2 | -1.543 | 0.000 | 0.193 | yes |
| 3 | TiZn(AgS2)2 | -1.547 | 0.000 | 1.554 | yes |
| 3 | ZrZn(CuSe2)2 | -1.188 | 0.000 | 0.205 | yes |
| 3 | ZrCd(CuSe2)2 | -1.141 | 0.000 | 0.146 | yes |
| 3 | NaGaS2 | -1.810 | 0.000 | 3.827 | yes |
| 3 | NaAlS2 | -2.075 | 0.000 | 4.647 | yes |
| 3 | TiZn(CuS2)2 | -1.574 | 0.000 | 2.660 | yes |
| 3 | ZrZn(CuS2)2 | -1.556 | 0.000 | 0.296 | yes |
| 3 | MgZr(AgS2)2 | -1.666 | 0.000 | 0.330 | yes |
| 3 | TiCd(CuS2)2 | -1.514 | 0.000 | 2.847 | yes |
| 3 | NaGaSe2 | -1.169 | 0.017 | 2.202 | yes |
| 3 | TiCd(AgS2)2 | -0.957 | 0.351 | 2.400 | yes |
| 3 | TiZn(AgSe2)2 | -0.617 | 0.353 | 2.229 | yes |
| 3 | TiCd(AgSe2)2 | -0.590 | 0.357 | 2.354 | yes |
| 3 | MgTi(AgS2)2 | -1.143 | 0.364 | 1.948 | yes |
| 3 | ZrCd(AgS2)2 | -0.946 | 0.451 | 2.364 | yes |
| 3 | MgZr(AgSe2)2 | -0.720 | 0.459 | 1.579 | yes |
| 3 | TiCd(CuSe2)2 | -0.487 | 0.479 | 2.805 | yes |
| 4 | KSbTe2 | -0.741 | 0.000 | 0.547 | yes |
| 4 | KGaSe2 | -1.275 | 0.000 | 2.177 | yes |
| 4 | KBiTe2 | -0.736 | 0.003 | 1.296 | yes |
| 4 | CdSi(AgTe2)2 | -0.230 | 0.083 | 1.055 | yes |
| 4 | MgSi(AgTe2)2 | -0.331 | 0.087 | 1.802 | yes |
| 4 | ZnSi(AgTe2)2 | -0.222 | 0.095 | 2.036 | yes |
| 4 | CaSi(AgTe2)2 | -0.493 | 0.122 | 1.247 | yes |
| 4 | BaSiAs2 | -0.558 | 0.135 | 0.851 | yes |
| 4 | MgGeSb2 | -0.054 | 0.177 | 0.006 | yes |
| 4 | SrGeAs2 | -0.503 | 0.184 | 0.547 | yes |
| 4 | CaSi(AgSe2)2 | -0.867 | 0.187 | 2.510 | yes |
| 4 | CaGeAs2 | -0.455 | 0.220 | 0.652 | yes |
| 4 | SrSiAs2 | -0.464 | 0.242 | 1.735 | yes |
| 4 | CdSiSb2 | 0.171 | 0.251 | 0.548 | yes |
| 4 | ZnSiSb2 | 0.206 | 0.281 | 1.201 | yes |
| 4 | CaSiSb2 | -0.230 | 0.300 | 0.017 | yes |
| 4 | CaSiAs2 | -0.401 | 0.302 | 1.857 | yes |
| 5 | K2MgSnTe4 | -0.977 | 0.000 | 1.329 | yes |
| 5 | K2MgGeTe4 | -0.948 | 0.000 | 1.499 | yes |
| 5 | K2ZnSnTe4 | -1.001 | 0.000 | 1.573 | yes |
| 5 | K2ZnGeTe4 | -0.902 | 0.000 | 1.896 | yes |
| 5 | K2CdGeTe4 | -0.863 | 0.000 | 0.884 | yes |
| 5 | K2CdSnTe4 | -0.899 | 0.000 | 0.864 | yes |
| 5 | TiMn(AgS2)2 | -1.513 | 0.000 | 1.479 | yes |
| 5 | Na2ZnSnSe4 | -1.121 | 0.007 | 2.292 | yes |
| 5 | Na2ZnGeSe4 | -1.094 | 0.011 | 2.480 | yes |
| 5 | Na2ZnGeTe4 | -0.690 | 0.015 | 2.419 | yes |
| 5 | Na2CdSnSe4 | -1.085 | 0.019 | 1.957 | yes |
| 5 | Na2CdGeTe4 | -0.680 | 0.021 | 1.739 | yes |
| 5 | Na2ZnSnTe4 | -0.712 | 0.023 | 2.053 | yes |
| 5 | Na2CdGeSe4 | -1.052 | 0.029 | 2.413 | yes |
| 5 | Na2CdSnTe4 | -0.699 | 0.032 | 1.367 | yes |
| 5 | Na2MgGeTe4 | -0.759 | 0.047 | 1.136 | yes |
| 5 | Na2MgGeSe4 | -1.186 | 0.055 | 2.448 | yes |
| 5 | Na2MgSnSe4 | -1.209 | 0.055 | 2.156 | yes |
| 5 | Na2MgSnTe4 | -0.782 | 0.055 | 1.932 | yes |
| 5 | TiNi(AgS2)2 | -0.815 | 0.441 | 0.075 | yes |

## Hypotheses tested and what was learned

**Iteration 1: Ag/Cu/alkaline-earth/transition-metal kesterites (A2-M-(Ge,Sn)-(S,Se)4).**
- The hypothesis largely held. Ag selenides with Ge or Sn are stable with in-window gaps.
- Four novel hits: CdAg2GeSe4 (1.28 eV), ZnAg2GeSe4 (1.12), MgAg2SnSe4 (1.59, E_hull 0.016) and SrAg2GeSe4 (1.69).
- SrAg2SnSe4 is a near miss at 1.701 eV.
- Mg/Ag sulfides come out near 1.9 eV and MgCu2SnS4 at 2.17 eV, both too wide.
- Ca, Mn and Fe variants and the Cu–Mg–Ge–Se compound are above hull (0.05–0.14 eV/atom). FeAg2SnSe4 has zero gap.
- The critic vetoed 5 malformed Si formulas for charge imbalance.

**Iteration 2: tellurides and more Ag-kesterite members.**
- 18 candidates were scored. The notebook records 8 critic vetoes, mainly Ba kesterites and a Sr sulfide, for size mismatch.
- New novel in-window members are MgAg2GeTe4 (1.49 eV, E_hull 0.025), ZnAg2GeTe4 (1.17, 0.028) and MgAg2SnTe4 (1.17, 0.038).
- Cd and Sr tellurides have gaps of 0.10–0.48 eV, too small.
- Ag–Cd/Zn sulfides are stable but 2.0–2.3 eV, too wide.
- Cu selenides with Zn or Cd are unstable (E_hull 0.06–0.11) with gaps of 0.28–0.85 eV, so Ag is needed.
- **Discrepancy:** the notebook lists CdAg2SnSe4 (1.262 eV) and ZnAg2SnSe4 (1.124 eV) as novel hits. The database flags both as **not novel**, so they are not counted as discoveries here.

**Iteration 3: Ti/Zr on the tetravalent site, plus Na–Ga/Al chalcogenides as controls.**
- The only in-window result is TiZn(AgS2)2, i.e. Ag2ZnTiS4 (E_hull 0.000, 1.554 eV).
- Zr compounds are mostly stable but have gaps of 0.15–0.65 eV, too small. The exceptions are the three Zr compounds with E_hull 0.45–0.46 or above, which are unstable.
- Ti–Cu sulfides are stable but 2.66–2.85 eV, too wide.
- Ti–Ag selenides and Ti–Cd/Mg Ag compounds have E_hull of about 0.35–0.48.
- Na–Ga/Al chalcogenides are wide-gap: NaGaSe2 2.20, NaGaS2 3.83, NaAlS2 4.65 eV.
- Some results are internally inconsistent. For example, ZrCd(AgS2)2 is unstable while ZrZn(AgS2)2 is stable. This suggests uneven hull references.

**Iteration 4: pnictide chalcopyrites, Si-telluride kesterites, K–Sb/Bi/Ga chalcogenides.**
- The one hit is KBiTe2 (E_hull 0.003, 1.296 eV).
- KSbTe2 is stable but has a 0.55 eV gap. KGaSe2 is stable but 2.18 eV.
- Ag–Si–Te/Se kesterites are unstable (E_hull 0.08–0.19). CaSi(AgTe2)2 has a 1.25 eV gap but E_hull 0.122.
- Alkaline-earth and Si/Ge pnictides are strongly unstable (E_hull 0.13–0.30), or have near-zero gaps (MgGeSb2, CaSiSb2).
- This hypothesis was falsified, apart from KBiTe2.

**Iteration 5: alkali (Na/K) A2MBX4 kesterite-type tellurides and selenides, plus Ti–S–Ag extensions.**
- Six in-window hits: K2MgSnTe4 (E_hull 0.000, 1.329 eV), K2MgGeTe4 (0.000, 1.499), K2ZnSnTe4 (0.000, 1.573), Na2CdSnTe4 (0.032, 1.367), Na2MgGeTe4 (0.047, 1.136) and TiMn(AgS2)2 (0.000, 1.479).
- Na selenides are stable but 1.96–2.48 eV.
- K2Cd tellurides are 0.86–0.88 eV, too low.
- K2ZnGeTe4 is 1.90 eV.
- TiNi(AgS2)2 is unstable (E_hull 0.441).

**Overall lessons.**
- Gaps follow the anion: sulfides are about 2.0–2.3 eV, selenides about 1.1–1.3 eV (Zn/Cd), and tellurides range from 0.1 to 1.5 eV depending on the cation.
- Ag is needed for stability over Cu in Ge/Sn selenides.
- Several families were falsified: Ca/Sr/Ba pnictides, Si tellurides, Zr kesterites and Na/K–Ga/Al chalcogenides.
- No compound sits exactly at 1.4 eV with E_hull of about 0. No anion-mixed alloys were tried, because the prototype tool only supports full substitutions.

## Caveats

- **Method limits.**
  - Stabilities come from CHGNet relaxations and an ML-fidelity gap model.
  - Neither was checked against DFT or experiment.
  - The notebook flags that the hull references appear patchy.
  - The campaign's surrogate model (GP expected improvement) was available to rank candidates, but no surrogate error bars are recorded in the notebook, so none are reported here.
- **Structure concerns.**
  - K- and Na-based kesterite-type cells are likely strained. Real ground states probably differ, so E_hull ≈ 0 may be an artifact.
  - KBiTe2 was computed in a chalcopyrite-derived cell, and the real structure is probably layered or NaCl-derived.
  - The Sr kesterites (SrAg2GeSe4, SrAg2SnSe4) may be relaxation artifacts, as the critic suggested for Ba and Sr.
- **Material-specific concerns.**
  - TiZn(AgS2)2 and TiMn(AgS2)2 rely on the Ti–S results, which sit beside inconsistent Ti–Se and Zr results.
  - Mn magnetism makes the TiMn(AgS2)2 gap suspect at this level of theory.
- **Novelty.** Novelty is relative to Materials Project only. The notebook notes that "already considered" formulas in the propose step were not necessarily evaluated. The iteration 2 novelty discrepancy shows the flags should be rechecked before any claim of discovery.
- **Missing records.** The campaign statistics give no filtered-out count for iteration 3.

**Validation the top candidates need:**
- Polymorph and structure search, including layered and other structure types for K/Na compounds and KBiTe2.
- DFT hull checks with competing ternary and binary phases.
- Hybrid-functional (HSE) or GW gaps.
- Phonon stability.
- Defect and absorption calculations, and then synthesis.

## Recommended next steps

1. Run DFT-level structure searches and hull checks for the leading candidates:
   - CdAg2GeSe4
   - ZnAg2GeSe4
   - K2MgSnTe4
   - Na2CdSnTe4
   - KBiTe2
   - TiZn(AgS2)2
2. Tune gaps toward 1.4 eV by alloying: K/Na mixing, Sn/Ge mixing in K2MgTe4-type compounds, and Se/Te mixing in Ag kesterites. This needs tooling that supports partial substitution.
3. Re-verify novelty for the iteration 2 compounds, and check the literature for any experimental reports on the leading candidates.
4. Deprioritize the families falsified in this campaign: Ca/Sr/Ba pnictides, Si-Te kesterites, Zr kesterites, Na/K–Ga/Al chalcogenides, Cu-selenide kesterites, and Fe/Mn/Ni variants.
