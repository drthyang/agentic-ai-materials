# Campaign report: pv-absorber-v1

## Executive summary

Over 5 iterations I scored 88 candidates, all flagged novel relative to Materials Project. The search centred on kesterite-type quaternary chalcogenides targeting a band gap of about 1.4 eV, with a working window of 1.1–1.7 eV and E_hull ≤ ~0.05 eV/atom. Five candidates met both criteria in the surrogate-model results: **BaSi(AgSe2)2** (gap 1.42 eV, E_hull 0.026), SrSi(AgSe2)2 (1.69, 0.021), SrAg2SnS4 (1.67, 0.024), MgSi(AgTe2)2 (1.63, 0.014) and MgAg2SnSe4 (1.15, 0.043). Confidence is low to moderate. All values come from a machine-learned relaxation and gap predictor (the notebook refers to CHGNet), with no DFT, phonon or experimental validation. The kesterite prototype is also probably not the true ground-state structure for the large-alkaline-earth compounds (Sr, Ba). Iterations 3 and 5 produced no new hits.

## Scored candidates

All 88 candidates are flagged novel vs. Materials Project and converged. E_f is formation energy per atom (eV), E_hull is energy above hull (eV/atom), and Gap is the predicted band gap (eV). Values are rounded.

| Iter | Formula | E_f | E_hull | Gap |
|---|---|---|---|---|
| 1 | CdAg2GeSe4 | -0.551 | 0.000 | 0.026 |
| 1 | CdSi(AgSe2)2 | -0.599 | 0.000 | 0.745 |
| 1 | ZnSi(AgSe2)2 | -0.614 | 0.000 | 1.841 |
| 1 | CdSi(AgS2)2 | -0.721 | 0.000 | 2.220 |
| 1 | ZnAg2GeSe4 | -0.567 | 0.003 | 0.677 |
| 1 | MgAg2GeS4 | -0.798 | 0.006 | 1.777 |
| 1 | CdSi(AgTe2)2 | -0.344 | 0.008 | 0.332 |
| 1 | MgAg2SnS4 | -0.788 | 0.011 | 0.691 |
| 1 | MgSi(AgSe2)2 | -0.739 | 0.011 | 1.837 |
| 1 | CdAg2GeTe4 | -0.375 | 0.014 | 0.166 |
| 1 | **MgSi(AgTe2)2** | -0.447 | 0.014 | **1.627** |
| 1 | MgAg2GeTe4 | -0.479 | 0.015 | 0.870 |
| 1 | MgCu2GeTe4 | -0.502 | 0.017 | 0.520 |
| 1 | MgAg2GeSe4 | -0.690 | 0.018 | 0.282 |
| 1 | MgCu2GeSe4 | -0.713 | 0.030 | 0.307 |
| 1 | MgCu2SiTe4 | -0.461 | 0.034 | 0.245 |
| 1 | **MgAg2SnSe4** | -0.700 | 0.043 | **1.153** |
| 2 | SrAg2GeS4 | -0.971 | 0.017 | 1.946 |
| 2 | **SrAg2SnS4** | -0.961 | 0.024 | **1.667** |
| 2 | SrAg2GeSe4 | -0.879 | 0.035 | 0.150 |
| 2 | SrAg2SnSe4 | -0.896 | 0.052 | 0.340 |
| 2 | SrCu2SiS4 | -1.103 | 0.058 | 3.173 |
| 2 | CaAg2GeS4 | -0.928 | 0.060 | 1.752 |
| 2 | BaCu2SiS4 | -1.119 | 0.060 | 3.133 |
| 2 | CaAg2SnS4 | -0.922 | 0.063 | 0.517 |
| 2 | CaAg2GeSe4 | -0.833 | 0.068 | 0.258 |
| 2 | SrCu2SnSe4 | -0.902 | 0.083 | 0.105 |
| 2 | CaCu2SiS4 | -1.066 | 0.089 | 3.311 |
| 2 | CaCu2SnS4 | -0.976 | 0.089 | 2.199 |
| 2 | CaAg2SnSe4 | -0.851 | 0.089 | 1.454 |
| 2 | CaCu2GeS4 | -0.966 | 0.090 | 2.625 |
| 2 | CaCu2GeSe4 | -0.829 | 0.110 | 0.301 |
| 2 | CaCu2SnSe4 | -0.860 | 0.117 | 0.212 |
| 2 | SrZr(CuS2)2 | -1.245 | 0.179 | 1.119 |
| 2 | BaZr(CuS2)2 | -1.261 | 0.184 | 1.161 |
| 2 | CaZr(CuS2)2 | -1.227 | 0.197 | 0.909 |
| 2 | CaZr(CuSe2)2 | -1.035 | 0.244 | 1.309 |
| 3 | TiCd(AgS2)2 | -0.921 | 0.007 | 2.228 |
| 3 | CdAg2SnTe4 | -0.425 | 0.015 | 0.031 |
| 3 | TiCd(AgSe2)2 | -0.818 | 0.019 | 0.609 |
| 3 | MnAg2GeS4 | -0.593 | 0.021 | 0.248 |
| 3 | BaTi(AgSe2)2 | -1.164 | 0.035 | 2.033 |
| 3 | TiCd(AgTe2)2 | -0.572 | 0.048 | 0.091 |
| 3 | BaTi(AgS2)2 | -1.280 | 0.049 | 2.245 |
| 3 | SrTi(AgS2)2 | -1.253 | 0.056 | 2.170 |
| 3 | BaAg2SnTe4 | -0.724 | 0.068 | 0.230 |
| 3 | SrTi(AgSe2)2 | -1.129 | 0.071 | 2.326 |
| 3 | CdSnS2 | -0.756 | 0.075 | 0.479 |
| 3 | ZnSnTe2 | -0.551 | 0.076 | 1.351 |
| 3 | TiMn(AgS2)2 | -0.872 | 0.092 | 1.392 |
| 3 | ZrCd(AgS2)2 | -0.920 | 0.097 | 1.877 |
| 3 | BaTi(AgTe2)2 | -0.871 | 0.109 | 0.076 |
| 3 | BaZr(AgSe2)2 | -1.174 | 0.110 | 0.136 |
| 3 | ZnSnS2 | -0.800 | 0.121 | 0.902 |
| 3 | BaZr(AgS2)2 | -1.273 | 0.144 | 0.379 |
| 3 | SrZr(AgS2)2 | -1.250 | 0.149 | 1.610 |
| 3 | ZrMn(AgS2)2 | -0.883 | 0.159 | 0.017 |
| 4 | TiZn(AgSe2)2 | -0.847 | 0.014 | 1.887 |
| 4 | MgCu2SnS4 | -0.866 | 0.014 | 0.490 |
| 4 | **SrSi(AgSe2)2** | -0.932 | 0.021 | **1.694** |
| 4 | TiZn(AgS2)2 | -0.951 | 0.022 | 2.046 |
| 4 | **BaSi(AgSe2)2** | -0.965 | 0.026 | **1.423** |
| 4 | BaSi(AgS2)2 | -1.106 | 0.029 | 2.565 |
| 4 | SrSi(AgS2)2 | -1.083 | 0.033 | 2.543 |
| 4 | MgTi(AgS2)2 | -1.088 | 0.040 | 1.785 |
| 4 | MgCu2SnSe4 | -0.734 | 0.047 | 0.189 |
| 4 | TiCd(CuS2)2 | -0.955 | 0.051 | 2.164 |
| 4 | MnSi(AgS2)2 | -0.686 | 0.052 | 0.086 |
| 4 | MgTi(AgSe2)2 | -0.943 | 0.053 | 1.516 |
| 4 | TiZn(CuS2)2 | -0.996 | 0.055 | 2.150 |
| 4 | TiCd(CuSe2)2 | -0.796 | 0.060 | 2.885 |
| 4 | CaSi(AgSe2)2 | -0.883 | 0.061 | 2.177 |
| 4 | MgTi(CuS2)2 | -1.135 | 0.071 | 2.187 |
| 4 | MgTi(CuSe2)2 | -0.931 | 0.080 | 2.616 |
| 5 | KGaSe2 | -1.113 | 0.000 | 3.307 |
| 5 | KAlS2 | -1.494 | 0.000 | 3.920 |
| 5 | NaAlS2 | -1.462 | 0.000 | 4.084 |
| 5 | NaGaS2 | -1.193 | 0.000 | 4.245 |
| 5 | NaGaSe2 | -1.059 | 0.006 | 3.083 |
| 5 | Cu2NiGeS4 | -0.602 | 0.010 | 0.486 |
| 5 | Cu2SiNiSe4 | -0.523 | 0.014 | 0.235 |
| 5 | KBiTe2 | -0.735 | 0.050 | 0.564 |
| 5 | KSbTe2 | -0.682 | 0.054 | 0.361 |
| 5 | CoCu2SiSe4 | -0.485 | 0.055 | 0.229 |
| 5 | TiCu2NiS4 | -0.889 | 0.063 | 2.090 |
| 5 | TiCu2NiSe4 | -0.700 | 0.076 | 2.129 |
| 5 | TiCo(CuSe2)2 | -0.648 | 0.129 | 1.565 |
| 5 | TiCo(CuS2)2 | -0.846 | 0.140 | 1.873 |

Bold rows are the five candidates inside the 1.1–1.7 eV gap window with E_hull ≤ ~0.05.

Candidates scored per iteration: 17, 20, 20, 17 and 14. The iteration 5 notebook records 6 relaxations left unspent.

## Hypotheses tested and what was learned

**Iteration 1: isoelectronic kesterite substitution.** The hypothesis was that Zn→Cd/Mg, Sn→Ge/Si, S→Se and Cu→Ag would give stable quaternaries with tunable gaps near 1.4 eV.
- All 17 scored candidates were near-stable (E_hull ≤ 0.043).
- Two landed in the window: MgSi(AgTe2)2 and MgAg2SnSe4.
- The gap trend was noisy. Mg raised the gap, while Sn, Se and Te lowered it.
- Cu–Mg–Ge/Si–Se/Te and Cd–Ag–Ge–Se/Te compounds had gaps below ~0.9 eV.
- The notebook notes that many Cu analogues are already in MP.

**Iteration 2: interpolating between MgAg2SnSe4 and MgAg2GeS4, plus larger alkaline earths.**
- Only SrAg2SnS4 hit (1.67 eV, E_hull 0.024), marginally at the top of the window.
- Ca-containing kesterites and Cu–alkaline-earth kesterites were unstable (E_hull ~0.06–0.12) and often had wide gaps of 2.2–3.3 eV.
- Zr compounds were strongly unstable (E_hull 0.18–0.24).
- The SrAg2GeSe4 gap of 0.15 eV was flagged in the notebook as a likely model artefact.
- The notebook conclusion is that the kesterite prototype is wrong for large alkaline earths, except Sr with Ag.
- Chalcopyrite ternaries proposed in this iteration were already in MP and were skipped.

**Iteration 3: new prototypes and Ti/Zr/Mn variants.** The notebook has no hypothesis entry for this iteration. Its candidate hypothesis strings cover Ag-based kesterites with Mn, Ba, Sr, Ti or Zr, and II-IV-V2/I-V-VI2 chalcopyrites.
- The zincblende prototype returned only binaries, and the pnictide chalcopyrite route was mostly rejected by SMACT filtering. 59 candidates were filtered out.
- No candidate met both the gap window and the stability criterion.
- Ti-based Ag kesterites were stable but had gaps that were too wide (S, ~2.2 eV) or too narrow (Se/Cd, 0.6 eV).
- Zr compounds were again unstable or low-gap, and tellurides had gaps near zero.
- The in-window compounds were unstable: TiMn(AgS2)2, ZnSnTe2 and SrZr(AgS2)2.

**Iteration 4: Cu analogues, plus Si/Ba/Sr–Ag–Se.** The literature search was recorded as "unhelpful".
- The Cu-for-Ag hypothesis was falsified. Cu-Ti kesterites had gaps of 2.1–2.9 eV, so the Ti d-derived conduction band appears to set the gap.
- MgCu2SnS4 and MgCu2SnSe4 had gaps of only 0.2–0.5 eV.
- The productive finding was the Si/Ag/Se series, where the gap falls with alkaline-earth size: CaSi(AgSe2)2 2.18, SrSi(AgSe2)2 1.69, BaSi(AgSe2)2 1.42 eV. The Ca member was unstable (E_hull 0.061).
- BaSi(AgSe2)2 is the best hit of the campaign, with a gap at the ideal ~1.4 eV.
- MgTi(AgSe2)2 (1.52 eV) just missed on stability (E_hull 0.053).

**Iteration 5: refinement and alternative families.**
- Ba/Sr–Ag–(Si,Ge,Sn)–(S,Se) was reported as already exhausted. Candidates were rejected as considered, and the other members do not appear in the scored data.
- Alkali–Al/Ga chalcopyrite-type compounds were stable (E_hull 0–0.006) but wide-gap (3.1–4.2 eV), so not suitable for photovoltaics.
- KSbTe2 and KBiTe2 had gaps of 0.36 and 0.56 eV at E_hull of about 0.05.
- Divalent-TM (Ni, Co) Cu kesterites had gaps of 0.2–0.5 eV. TiCo(CuSe2)2 had a gap of 1.56 eV but E_hull of 0.129.
- No new hits.

## Caveats

- **Surrogate-model error.** Formation energies, hull distances and gaps are ML predictions, not DFT or HSE results. The notebook flags several likely artefacts, such as SrAg2GeSe4 at 0.15 eV and the Mn compounds. Telluride and Se-containing Sr/Ca compounds have erratic gaps. The reliability of the gap predictions, especially against the sharp 1.1–1.7 eV window, is unquantified. Hull distances of 0.02–0.05 eV/atom are within the typical error of such models, so "near-stable" is not a stability guarantee.
- **Structure.** All large-alkaline-earth compounds (Sr, Ba) were evaluated in the kesterite prototype. The notebook states the true ground state is likely a different structure type, and that alternative types were not tested. The candidates' hull energies may therefore be unrepresentative.
- **Novelty.** "Novel" means absent from the Materials Project database only. It does not rule out prior literature reports.
- **Tool limitations.** The workflow could not produce anion or cation mixing (S/Se, Ge/Sn, Sr/Ba), so fine-tuning towards 1.4 eV by interpolation was not possible.
- **Literature.** Beyond a note that the iteration 4 search was unhelpful, the notebook records no literature findings.
- **Gap-window conventions.** The window and stability cutoff are as stated in the notebook; KBiTe2 sits at E_hull 0.0498.

## Recommended next steps

1. Run DFT (PBE for structure, then HSE06 or GW for gaps) on the top five: BaSi(AgSe2)2, SrSi(AgSe2)2, SrAg2SnS4, MgSi(AgTe2)2 and MgAg2SnSe4. Include a spin-orbit check where relevant.
2. For the Sr and Ba compounds, run a structure search over alternative prototypes, since the kesterite assumption is doubtful. Recompute E_hull against competing phases such as binaries and ternary chalcogenides.
3. Check dynamical stability with phonons, and assess defect tolerance and absorption before any synthesis attempt.
4. Prioritise BaSi(AgSe2)2 for synthesis planning if DFT confirms the gap and stability.
5. Enable anion and cation mixing in the workflow (e.g. Sr/Ba, S/Se, Ge/Sn) to tune the gap continuously.
6. Deprioritise Zr, Ca and Cu–Ti kesterites, Ag/Cu tellurides, alkali-III-VI chalcopyrites and divalent-TM Cu kesterites, since these families gave no hits in this campaign.
