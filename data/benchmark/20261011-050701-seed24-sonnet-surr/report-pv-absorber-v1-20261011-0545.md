# Campaign report: pv-absorber-v1

## Executive summary

The campaign ran 5 iterations and scored 96 kesterite-type chalcogenide candidates. 95 are flagged novel against the Materials Project and one is flagged known. All numbers come from CHGNet relaxation and ML-estimated "HSE-fidelity" band gaps. No explicit DFT or HSE validation and no synthesis were done.

12 candidates fall in the target window (gap 1.1–1.7 eV, E_hull ≤ 0.05 eV/atom). They fall into three families:

- **Ag-based Ge/Sn selenides and tellurides:** CdAg2GeSe4, ZnAg2GeSe4, MgAg2SnSe4, SrAg2GeSe4, NiAg2GeSe4, NiAg2SnSe4, ZnAg2GeTe4 and MgAg2SnTe4.
- **Alkali–Mn selenides:** K2MnGeSe4, Na2MnGeSe4 and Na2MnSnSe4.
- **One alkali–Ni selenide:** Na2NiGeSe4.

CdAg2GeSe4 (1.28 eV, on the hull) is the most credible lead. The open-shell 3d compounds (Mn, Ni) are the least trustworthy, because ML gaps for these ions are doubtful.

The data are limited to a single structure type and a single-site-substitution tool. Several hypotheses failed and are recorded below.

## Scored candidates

Columns: E_f is formation energy (eV/atom), E_hull is energy above hull (eV/atom), and Gap is the ML-estimated band gap (eV). "Window" marks gap 1.1–1.7 eV with E_hull ≤ 0.05. Rows are in database order within each iteration. Gaps are shown to three decimals and values within about 0.001 of the window edges should be treated as borderline.

### Iteration 1 (kesterite substitutions: Ag/Cu, Zn/Cd/Mg, Ge/Sn/Si, S/Se/Te)

| Formula | E_f | E_hull | Gap | Window |
|---|---|---|---|---|
| CdAg2GeSe4 | -0.657 | 0.000 | 1.279 | **yes** |
| ZnAg2GeSe4 | -0.681 | 0.000 | 1.119 | **yes** |
| MgAg2SnS4 | -1.177 | 0.002 | 1.871 | no |
| MgAg2SnSe4 | -0.838 | 0.016 | 1.588 | **yes** |
| CdAg2GeTe4 | -0.326 | 0.017 | 0.481 | no |
| MgAg2GeS4 | -1.165 | 0.017 | 1.893 | no |
| MgCu2SnS4 | -1.239 | 0.020 | 2.174 | no |
| MgAg2GeSe4 | -0.797 | 0.020 | 1.856 | no |
| ZnAg2GeTe4 | -0.318 | 0.028 | 1.171 | **yes** |
| MgAg2SnTe4 | -0.461 | 0.038 | 1.172 | **yes** |
| ZnAg2SnTe4 | -0.358 | 0.039 | 0.596 | no |
| MgCu2SnSe4 | -0.819 | 0.071 | 1.383 | no (hull) |
| ZnSi(AgTe2)2 | -0.222 | 0.095 | 2.036 | no |
| MgCu2GeTe4 | -0.372 | 0.101 | 0.895 | no |
| CdSi(AgSe2)2 | -0.568 | 0.130 | 1.714 | no |
| MgCu2GeSe4 | -0.717 | 0.136 | 1.102 | no (hull) |
| MgSi(AgSe2)2 | -0.715 | 0.145 | 2.348 | no |
| CdSi(AgS2)2 | -0.937 | 0.152 | 2.751 | no |
| ZnSi(AgSe2)2 | -0.553 | 0.170 | 1.904 | no |
| MgCu2GeS4 (known in MP, novel=0) | -1.032 | 0.220 | 2.582 | no |

### Iteration 2 (Ca/Sr/Ba/Ti/Zr A-site and M(IV) variants)

| Formula | E_f | E_hull | Gap | Window |
|---|---|---|---|---|
| ZrCd(AgSe2)2 | -1.148 | 0.000 | 0.295 | no |
| SrAg2SnSe4 | -1.059 | 0.000 | 1.701 | no (just above 1.7) |
| SrAg2GeSe4 | -1.021 | 0.003 | 1.687 | **yes** |
| SrAg2GeS4 | -1.354 | 0.013 | 1.867 | no |
| SrAg2SnTe4 | -0.689 | 0.029 | 0.100 | no |
| CaAg2GeSe4 | -0.949 | 0.062 | 1.679 | no (hull) |
| CaAg2GeS4 | -1.273 | 0.094 | 2.158 | no |
| CaZr(AgS2)2 | -1.487 | 0.294 | 2.734 | no |
| BaTi(AgSe2)2 | -0.997 | 0.312 | 2.397 | no |
| BaTi(AgS2)2 | -1.391 | 0.317 | 1.901 | no |
| TiCd(AgS2)2 | -0.957 | 0.351 | 2.400 | no |
| TiCd(AgSe2)2 | -0.590 | 0.357 | 2.354 | no |
| SrTi(AgSe2)2 | -0.938 | 0.373 | 2.357 | no |
| CaTi(AgS2)2 | -1.315 | 0.376 | 2.317 | no |
| SrTi(AgS2)2 | -1.305 | 0.384 | 1.916 | no |
| BaZr(AgSe2)2 | -0.989 | 0.405 | 2.173 | no |
| CaTi(AgSe2)2 | -0.864 | 0.438 | 2.723 | no |
| SrZr(AgSe2)2 | -0.944 | 0.440 | 2.331 | no |
| ZrCd(AgS2)2 | -0.946 | 0.451 | 2.364 | no |
| CaZr(AgSe2)2 | -0.882 | 0.493 | 2.471 | no |

### Iteration 3 (Sr/Ba tellurides, Cu-based Sr, 3d-metal Ag2-M-(Ge,Sn)-(S,Se)4)

| Formula | E_f | E_hull | Gap | Window |
|---|---|---|---|---|
| BaAg2GeTe4 | -0.704 | 0.000 | 0.705 | no |
| NiAg2SnS4 | -0.936 | 0.000 | 1.897 | no |
| NiAg2SnSe4 | -0.631 | 0.000 | 1.676 | **yes** |
| NiAg2GeSe4 | -0.583 | 0.0005 | 1.648 | **yes** |
| NiAg2GeS4 | -0.911 | 0.008 | 1.744 | no |
| SrAg2GeTe4 | -0.651 | 0.016 | 0.155 | no |
| NiAg2GeTe4 | -0.281 | 0.036 | 0.126 | no |
| Cu2NiGeSe4 | -0.577 | 0.041 | 0.255 | no |
| NiAg2SnTe4 | -0.323 | 0.045 | 0.039 | no |
| SrCu2SnSe4 | -1.045 | 0.050 | 1.109 | no (hull 0.0504, marginal) |
| CoAg2SnSe4 | -0.569 | 0.056 | 0.603 | no |
| FeAg2SnSe4 | -0.579 | 0.072 | -0.003 | no |
| Cu2NiGeTe4 | -0.252 | 0.074 | 0.089 | no |
| CoAg2GeSe4 | -0.524 | 0.075 | 0.809 | no |
| Cu2NiSnTe4 | -0.288 | 0.076 | 0.137 | no |
| FeAg2GeSe4 | -0.525 | 0.078 | 0.018 | no |
| MnAg2GeS4 | -0.914 | 0.079 | 2.236 | no |
| CoAg2SnS4 | -0.860 | 0.092 | 1.387 | no (hull) |
| CoAg2GeS4 | -0.835 | 0.113 | 1.512 | no (hull) |
| FeAg2GeS4 | -0.851 | 0.135 | 0.013 | no |

### Iteration 4 (alkali A2-M-(Ge,Sn)-(S,Se,Te)4; M = Zn, Cd, Mn, Co)

| Formula | E_f | E_hull | Gap | Window |
|---|---|---|---|---|
| Na2MnSnSe4 | -1.074 | 0.000 | 1.115 | **yes** |
| K2CdGeSe4 | -1.169 | 0.000 | 2.409 | no |
| K2ZnSnSe4 | -1.222 | 0.000 | 2.265 | no |
| K2ZnGeSe4 | -1.197 | 0.000 | 2.488 | no |
| K2MnGeSe4 | -1.142 | 0.000 | 1.443 | **yes** |
| K2MnSnS4 | -1.546 | 0.000 | 2.238 | no |
| K2MnGeS4 | -1.530 | 0.000 | 1.875 | no |
| Na2MnSnS4 | -1.449 | 0.000 | 2.141 | no |
| Na2MnGeS4 | -1.437 | 0.000 | 2.083 | no |
| K2MnSnTe4 | -0.932 | 0.000 | 0.646 | no |
| K2MnGeTe4 | -0.709 | 0.002 | 1.100 | no (gap 1.0998, just below 1.1) |
| K2CoGeS4 | -1.462 | 0.006 | 1.845 | no |
| Na2ZnSnSe4 | -1.121 | 0.007 | 2.292 | no |
| Na2MnGeSe4 | -1.035 | 0.008 | 1.646 | **yes** |
| Na2ZnGeSe4 | -1.094 | 0.011 | 2.480 | no |
| Na2CdSnSe4 | -1.085 | 0.019 | 1.957 | no |
| K2CoSnS4 | -1.451 | 0.026 | 2.206 | no |
| Na2CdGeSe4 | -1.052 | 0.029 | 2.413 | no |
| Na2CoSnS4 | -1.362 | 0.040 | 2.287 | no |
| Na2MnSnTe4 | -0.618 | 0.046 | 0.947 | no |

### Iteration 5 (alkali Ni/Co/Fe selenides; Ni/Co tellurides)

| Formula | E_f | E_hull | Gap | Window |
|---|---|---|---|---|
| K2NiGeSe4 | -1.111 | 0.000 | 2.020 | no |
| K2NiSnSe4 | -1.128 | 0.000 | 2.114 | no |
| K2FeSnSe4 | -1.124 | 0.000 | 0.437 | no |
| K2NiGeTe4 | -0.744 | 0.000 | 0.652 | no |
| K2NiSnTe4 | -0.885 | 0.000 | 0.531 | no |
| Na2NiSnSe4 | -1.031 | 0.0004 | 2.060 | no |
| Na2NiGeSe4 | -1.009 | 0.002 | 1.402 | **yes** |
| K2FeGeSe4 | -1.083 | 0.010 | 0.632 | no |
| K2CoSnSe4 | -1.087 | 0.020 | 2.120 | no |
| K2CoGeSe4 | -1.067 | 0.021 | 2.314 | no |
| Na2NiGeTe4 | -0.644 | 0.022 | 0.076 | no |
| Na2NiSnTe4 | -0.665 | 0.029 | 0.613 | no |
| Na2FeSnSe4 | -1.011 | 0.036 | 0.808 | no |
| Na2CoSnSe4 | -0.985 | 0.048 | 1.922 | no |
| Na2FeGeSe4 | -0.971 | 0.057 | 1.325 | no (hull) |
| Na2CoGeSe4 | -0.957 | 0.058 | 2.140 | no |

## Hypotheses tested and what was learned

**Iteration 1: Ag/Cd/Ge/Se kesterite variants.**
- Hypothesis: isoelectronic substitution (Cu→Ag, Zn→Cd/Mg, Sn→Ge/Si, S→Se/Te) keeps the structures near the hull and puts gaps in 1.1–1.7 eV.
- Result: supported. Ag-based Ge/Sn selenides and tellurides were stable with suitable gaps (five window hits, listed in the table).
- Trends: the gap ordering is S > Se > Te, and Mg raises the gap relative to Zn/Cd. Ag consistently stabilised the structures.
- Failures: Si variants were unstable (hull 0.13–0.17). Cu–Mg selenides were also unstable or off-window (MgCu2SnSe4 hull 0.071, MgCu2GeSe4 hull 0.136).

**Iteration 2: larger A-site cations and 4+ M sites.**
- Chalcopyrite Ag–Al/Ga proposals were all already known, so they were skipped.
- Ti/Zr (4+) variants were unstable (hull 0.29–0.49). The exception was ZrCd(AgSe2)2, which is on the hull but has a 0.30 eV gap.
- Sr stabilised the Ag2-A-Ge/Sn-Se4 compounds. SrAg2GeSe4 is a hit at 1.687 eV, near the upper edge, and SrAg2SnSe4 (1.701 eV, hull 0.000) is just outside the window.
- Ca was worse on the hull (CaAg2GeSe4 0.062).

**Iteration 3: tuning gaps down, and 3d-metal M sites.**
- Sr/Ba tellurides were too narrow (SrAg2GeTe4 0.155 eV, BaAg2GeTe4 0.705 eV), so the Te route was ruled out for Sr/Ba.
- The critic vetoed 9 candidates. They were non-kesterite compounds (Sb chalcopyrites, K/Na–Ga/Sb/Bi chalcogenides) that did not match my multi-part hypothesis. The notebook records this as a lesson: state one focused hypothesis per batch. The zincblende prototype also yielded only binaries.
- Cu substitution for Ag, and Se→Te, both closed the gap too far (Cu2NiGeSe4 0.255 eV; Ni tellurides ≤0.13 eV). S→Se was the useful lever.
- The Cu-based Sr hypothesis gave only SrCu2SnSe4 (1.109 eV, hull 0.0504), which misses the hull cutoff by a hair. The Ba–Cu compounds named in the hypothesis do not appear among the scored candidates.
- The Ni–Ag selenides NiAg2GeSe4 and NiAg2SnSe4 are window hits at the upper gap edge. Co and Fe analogues were unstable and/or had gaps that were too narrow.
- Co sulfides had suitable gaps (1.39 and 1.51 eV) but hulls of 0.092 and 0.113.

**Iteration 4: alkali (Na, K) A2-M-(Ge,Sn)-Se4 analogues.**
- Almost everything was near or on the hull.
- Zn and Cd gaps were too wide (1.96–2.49 eV).
- Mn lowered the gap and gave three hits: K2MnGeSe4 (1.443 eV, hull 0.000, the best compound in this family), Na2MnGeSe4 and Na2MnSnSe4.
- S analogues were too wide (1.84–2.29 eV). Mn tellurides were too narrow (0.65–0.95 eV), except K2MnGeTe4 at 1.0998 eV, which falls just below the window.

**Iteration 5: alkali Co/Ni/Fe selenides.**
- The hypothesis that Co²⁺ lowers the gap relative to Mn was falsified. Co selenides had gaps of 1.9–2.3 eV.
- Na2NiGeSe4 (1.402 eV, hull 0.002) is the one hit. The K/Na Ni–Sn analogues and K2NiGeSe4 are about 2.0–2.1 eV, so the Na2NiGeSe4 result is an isolated point, not a trend.
- Na2FeGeSe4 has gap 1.325 eV but hull 0.057, so it fails. Fe selenides are otherwise narrow (0.44–0.81 eV).
- Ni and Co tellurides were too narrow (0.08–0.65 eV).

## Caveats

- **Gap reliability:** all band gaps are ML (HSE-fidelity) estimates on CHGNet-relaxed structures, with no error bars reported. Gaps of 1.10–1.12 eV (ZnAg2GeSe4, Na2MnSnSe4) and 1.65–1.70 eV (SrAg2GeSe4, NiAg2GeSe4, NiAg2SnSe4, Na2MnGeSe4) sit at the window edges. Their classification could flip within plausible model error.
- **Open-shell 3d ions:** the Mn²⁺ (d5, spin state) and tetrahedral Ni²⁺ (d8, which normally prefers square-planar coordination) gaps are suspect. Na2NiGeSe4 and the Ni–Ag selenides are the most suspect. The Co/Fe results are subject to the same concern.
- **Stability scope:** E_hull is computed against the Materials Project reference set. Competing phases outside that set, dynamic (phonon) stability and finite-temperature effects were not assessed.
- **Novelty:** it is judged only against the Materials Project. Literature checks were limited (the notebook reports none found for the iteration 5 family).
- **Absorber metrics not assessed:** no optical absorption, defect tolerance, carrier transport or band alignment was computed. A gap in the window is only a first filter.
- **Tooling:** the tool supports only single-site substitution lists, so mixed-anion and mixed-cation alloys were not explored.
- **Structure type:** all scored candidates are derived from kesterite-type or related structure types. The "stable" label assumes that structure type, and lower-energy structure types were not searched.

## Recommended next steps

1. **Validate the top leads with explicit DFT/HSE.** Start with CdAg2GeSe4 and ZnAg2GeSe4, then MgAg2SnSe4, SrAg2GeSe4, K2MnGeSe4, Na2MnGeSe4 and Na2MnSnSe4. Use DFT+U or hybrid functionals with magnetic ordering for the Mn and Ni compounds (K2MnGeSe4, Na2MnGeSe4, Na2MnSnSe4, Na2NiGeSe4, NiAg2GeSe4, NiAg2SnSe4).
2. **Check competing phases and structure types.** Compute phonons and compare kesterite-type against other known structure types for these compositions, such as the K2ZnSnS4-type or Ag/Cd/Ge selenides in other polymorphs.
3. **Probe the borderline compounds.** Test ZnAg2GeTe4 and MgAg2SnTe4 (hull 0.028 and 0.038, hits only at the lower gap edge) and the near-misses SrAg2SnSe4, SrCu2SnSe4 and K2MnGeTe4.
4. **Explore alloys and the untried families.** Examples are Sr/Cd or Se/Te alloys, which should fine-tune gaps, and the Sb-based II-IV-V2 compounds noted in the notebook (ZnGeSb2, CdGeSb2, MgSnSb2, MgGeSb2), each under its own focused hypothesis.
5. **Search the literature before any synthesis attempt**, then prioritise CdAg2GeSe4 and ZnAg2GeSe4 for synthesis and measurement.
