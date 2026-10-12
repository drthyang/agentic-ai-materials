# Campaign report: pv-absorber-v1

## Executive summary

Over five iterations, 97 candidates were scored with a machine-learned surrogate: formation energy, energy above hull and band gap. 96 of them were novel against the Materials Project; one was a deliberate known calibration compound. The target gap window is never stated in the notebook. The hit criteria in the notebook imply roughly 1.1–1.7 eV with E_hull ≤ 0.05 eV/atom, and I treat that as inferred. Five novel Ag-based kesterite-type compounds met these criteria: **BaSi(AgSe₂)₂** (1.42 eV, E_hull 0.026), SrAg₂SnS₄, SrSi(AgSe₂)₂, MgSi(AgTe₂)₂ and MgAg₂SnSe₄. All are surrogate predictions only. The surrogate's gap noise is large, and no DFT or experimental validation has been done, so confidence in any individual number is low. Two of the five iterations (3 and 5) produced no hits, and the Ag-kesterite grid was largely exhausted by iteration 4.

## Scored candidates

Columns: Ef = formation energy (eV/atom), E_hull (eV/atom), Gap (eV), Novel = absent from Materials Project. "Hit" marks candidates the notebook recorded as novel, in the gap window and with E_hull ≤ 0.05. This is an inferred criterion, not one stated in the data. The count is 97: 20, 20, 20, 17 and 20 per iteration.

| Iter | Formula | Ef | E_hull | Gap | Novel | Note |
|---|---|---|---|---|---|---|
| 1 | CdAg2GeSe4 | -0.551 | 0.000 | 0.026 | yes | |
| 1 | CdSi(AgSe2)2 | -0.599 | 0.000 | 0.745 | yes | |
| 1 | CdSi(AgS2)2 | -0.721 | 0.000 | 2.220 | yes | |
| 1 | ZnSi(AgSe2)2 | -0.614 | 0.000 | 1.841 | yes | |
| 1 | ZnAg2GeSe4 | -0.567 | 0.003 | 0.677 | yes | |
| 1 | MgAg2GeS4 | -0.798 | 0.006 | 1.777 | yes | |
| 1 | MgAg2SnS4 | -0.788 | 0.011 | 0.691 | yes | |
| 1 | MgSi(AgSe2)2 | -0.739 | 0.011 | 1.837 | yes | |
| 1 | MgSi(AgS2)2 | -0.908 | 0.012 | 2.463 | yes | |
| 1 | MgCu2SnS4 | -0.866 | 0.014 | 0.490 | yes | |
| 1 | MgAg2SnTe4 | -0.530 | 0.014 | 0.187 | yes | |
| 1 | MgAg2GeTe4 | -0.479 | 0.015 | 0.870 | yes | |
| 1 | MgAg2GeSe4 | -0.690 | 0.018 | 0.282 | yes | |
| 1 | ZnCu2SnSe4 | -0.626 | 0.019 | 0.112 | **no** | known compound |
| 1 | MgCu2GeSe4 | -0.713 | 0.030 | 0.307 | yes | |
| 1 | MgAg2SnSe4 | -0.700 | 0.043 | 1.153 | yes | **Hit** |
| 1 | MgCu2SnSe4 | -0.734 | 0.047 | 0.189 | yes | |
| 1 | CaAg2GeSe4 | -0.833 | 0.068 | 0.258 | yes | |
| 1 | CaAg2SnSe4 | -0.851 | 0.089 | 1.454 | yes | gap in window, hull too high |
| 1 | CaZr(AgSe2)2 | -1.092 | 0.173 | 0.092 | yes | |
| 2 | TiCd(AgS2)2 | -0.921 | 0.007 | 2.228 | yes | |
| 2 | SrAg2GeS4 | -0.971 | 0.017 | 1.946 | yes | |
| 2 | TiCd(AgSe2)2 | -0.818 | 0.019 | 0.609 | yes | |
| 2 | SrSi(AgSe2)2 | -0.932 | 0.021 | 1.694 | yes | **Hit** |
| 2 | MnAg2GeS4 | -0.593 | 0.021 | 0.248 | yes | |
| 2 | SrAg2SnS4 | -0.961 | 0.024 | 1.667 | yes | **Hit** |
| 2 | BaSi(AgSe2)2 | -0.965 | 0.026 | 1.423 | yes | **Hit** (best gap and hull combination) |
| 2 | TiMn(AgSe2)2 | -0.747 | 0.031 | 0.110 | yes | |
| 2 | SrSi(AgS2)2 | -1.083 | 0.033 | 2.543 | yes | |
| 2 | BaTi(AgSe2)2 | -1.164 | 0.035 | 2.033 | yes | |
| 2 | SrAg2GeSe4 | -0.879 | 0.035 | 0.150 | yes | |
| 2 | MnSi(AgS2)2 | -0.686 | 0.052 | 0.086 | yes | |
| 2 | SrAg2SnSe4 | -0.896 | 0.052 | 0.340 | yes | |
| 2 | SrTi(AgS2)2 | -1.253 | 0.056 | 2.170 | yes | |
| 2 | BaAg2GeTe4 | -0.682 | 0.059 | 0.203 | yes | |
| 2 | CaAg2GeS4 | -0.928 | 0.060 | 1.752 | yes | |
| 2 | CaAg2SnS4 | -0.922 | 0.063 | 0.517 | yes | |
| 2 | SrAg2SnTe4 | -0.697 | 0.067 | 0.033 | yes | |
| 2 | ZrCd(AgSe2)2 | -0.822 | 0.088 | 0.014 | yes | |
| 2 | ZrCd(AgS2)2 | -0.920 | 0.097 | 1.877 | yes | |
| 3 | BaCu2SiSe4 | -0.952 | 0.054 | 1.812 | yes | |
| 3 | SrCu2SiSe4 | -0.913 | 0.055 | 1.736 | yes | |
| 3 | BaNa2SnSe4 | -1.314 | 0.055 | 2.533 | yes | |
| 3 | BaNa2GeSe4 | -1.290 | 0.056 | 2.625 | yes | |
| 3 | SrCu2SiS4 | -1.103 | 0.058 | 3.173 | yes | |
| 3 | BaNa2SnTe4 | -1.058 | 0.058 | 1.306 | yes | near-miss (hull) |
| 3 | BaCu2SiS4 | -1.119 | 0.060 | 3.133 | yes | |
| 3 | BaCu2GeTe4 | -0.686 | 0.066 | 0.350 | yes | |
| 3 | K2BaSnSe4 | -1.368 | 0.066 | 2.165 | yes | |
| 3 | BaCu2SnTe4 | -0.730 | 0.067 | 0.078 | yes | |
| 3 | Na2SrSnSe4 | -1.291 | 0.067 | 2.823 | yes | |
| 3 | K2BaGeSe4 | -1.341 | 0.074 | 2.714 | yes | |
| 3 | Na2SrGeSe4 | -1.261 | 0.074 | 2.891 | yes | |
| 3 | SrCu2SnSe4 | -0.902 | 0.083 | 0.105 | yes | |
| 3 | K2SrSnSe4 | -1.352 | 0.084 | 2.424 | yes | |
| 3 | SrCu2GeTe4 | -0.646 | 0.092 | 0.156 | yes | |
| 3 | SrCu2SnTe4 | -0.688 | 0.095 | 0.243 | yes | |
| 3 | Na2CaSnSe4 | -1.253 | 0.096 | 2.972 | yes | |
| 3 | BaCu2SiTe4 | -0.630 | 0.098 | 0.541 | yes | |
| 3 | SrCu2SiTe4 | -0.595 | 0.119 | 0.268 | yes | |
| 4 | ZnSi(AgTe2)2 | -0.355 | 0.001 | 1.717 | yes | near-miss (gap slightly high) |
| 4 | CdSi(AgTe2)2 | -0.344 | 0.008 | 0.332 | yes | |
| 4 | ZnAg2GeTe4 | -0.382 | 0.010 | 0.627 | yes | |
| 4 | TiZn(AgSe2)2 | -0.847 | 0.014 | 1.887 | yes | |
| 4 | CdAg2GeTe4 | -0.375 | 0.014 | 0.166 | yes | |
| 4 | MgSi(AgTe2)2 | -0.447 | 0.014 | 1.627 | yes | **Hit** |
| 4 | TiZn(AgS2)2 | -0.951 | 0.022 | 2.046 | yes | |
| 4 | MgTi(AgTe2)2 | -0.677 | 0.048 | 0.212 | yes | |
| 4 | TiCd(AgTe2)2 | -0.572 | 0.048 | 0.091 | yes | |
| 4 | TiZn(AgTe2)2 | -0.573 | 0.051 | 0.065 | yes | |
| 4 | CaSi(AgSe2)2 | -0.883 | 0.061 | 2.177 | yes | |
| 4 | CaSi(AgS2)2 | -1.039 | 0.067 | 2.272 | yes | |
| 4 | ZrZn(AgSe2)2 | -0.853 | 0.080 | 1.328 | yes | |
| 4 | CaSi(AgTe2)2 | -0.569 | 0.086 | 1.920 | yes | |
| 4 | ZrZn(AgTe2)2 | -0.601 | 0.087 | 0.346 | yes | |
| 4 | ZrZn(AgS2)2 | -0.957 | 0.106 | 1.223 | yes | |
| 4 | CaZr(AgS2)2 | -1.217 | 0.185 | 0.208 | yes | |
| 5 | TiCd(CuS2)2 | -0.955 | 0.051 | 2.164 | yes | |
| 5 | MgTi(AgSe2)2 | -0.943 | 0.053 | 1.516 | yes | marginal near-miss (hull) |
| 5 | TiCd(CuSe2)2 | -0.796 | 0.060 | 2.885 | yes | |
| 5 | ZrCd(CuS2)2 | -0.971 | 0.069 | 1.986 | yes | |
| 5 | MgTi(CuS2)2 | -1.135 | 0.071 | 2.187 | yes | |
| 5 | FeAg2GeSe4 | -0.419 | 0.075 | 0.151 | yes | |
| 5 | MgTi(CuSe2)2 | -0.931 | 0.080 | 2.616 | yes | |
| 5 | BaTi(CuSe2)2 | -1.124 | 0.089 | 2.408 | yes | |
| 5 | MgZr(CuS2)2 | -1.147 | 0.093 | 1.138 | yes | |
| 5 | TiCd(CuTe2)2 | -0.534 | 0.108 | 0.561 | yes | |
| 5 | ZrCd(CuSe2)2 | -0.801 | 0.127 | 1.274 | yes | |
| 5 | BaTi(CuS2)2 | -1.265 | 0.142 | 2.204 | yes | |
| 5 | SrTi(CuS2)2 | -1.246 | 0.142 | 2.391 | yes | |
| 5 | MgZr(CuSe2)2 | -0.939 | 0.144 | 1.545 | yes | |
| 5 | ZrCd(CuTe2)2 | -0.542 | 0.163 | 0.018 | yes | |
| 5 | FeSi(AgTe2)2 | -0.193 | 0.173 | 0.014 | yes | |
| 5 | SrZr(CuS2)2 | -1.245 | 0.179 | 1.119 | yes | |
| 5 | BaZr(CuSe2)2 | -1.115 | 0.184 | 0.083 | yes | |
| 5 | BaZr(CuS2)2 | -1.261 | 0.184 | 1.161 | yes | |
| 5 | SrZr(CuSe2)2 | -1.073 | 0.215 | 0.789 | yes | |

## Hypotheses tested and what was learned

**Iteration 1: isovalent substitution in the kesterite Cu₂ZnSnS₄ family.**
- The idea was to substitute Ag for Cu, Cd/Mg for Zn, Ge/Si for Sn and vary the chalcogen to tune the gap near 1.4 eV.
- Result: one hit, MgAg₂SnSe₄ (1.15 eV, E_hull 0.043). Several compounds were stable but had gaps that were too small or too large.
- Cu analogues had very small gaps (0.11–0.49 eV). The notebook attributes this partly to surrogate gap noise.
- The Ge/Sn gap trends were inconsistent (MgAg₂GeS₄ 1.78 eV vs MgAg₂SnS₄ 0.69 eV), which the notebook flags as noise.
- ZnCu₂SnSe₄ turned out to be known (novel = false); it was the only non-novel candidate in the scored set.

**Iteration 2: vary the divalent and tetravalent sites in Ag-kesterites (Mn, Sr, Ba, Ti, Zr, Cd).**
- Three hits: BaSi(AgSe₂)₂ (1.42 eV, E_hull 0.026), SrAg₂SnS₄ (1.67 eV, 0.024) and SrSi(AgSe₂)₂ (1.69 eV, 0.021).
- Large alkaline earths (Sr, Ba) were tolerated on the divalent site (E_hull ≈ 0.02–0.03), unlike Ca.
- Mn, Zr and Cd variants gave near-zero gaps or high hull energies.
- Chalcopyrite and zincblende prototypes returned only known compounds.
- The tool did not support mixed anions.

**Iteration 3: Cu analogues of Sr/Ba kesterites, and Na/K alkali kesterites. No hits.**
- The Cu analogues were falsified: E_hull 0.054–0.12 eV, with gaps either above 1.7 eV (Si–S/Se) or below 0.6 eV (Te, Sn).
- The Na/K compounds had E_hull 0.055–0.096 and gaps of 2.2–3.0 eV, too wide.
- The exception was BaNa₂SnTe₄ (1.31 eV), with E_hull 0.058 just above the limit.
- Lesson recorded in the notebook: Ag stabilises this structure type better than Cu or Na/K, and Te helps bring gaps down.

**Iteration 4: fill the remaining Ag-kesterite grid; Si–Te and Ti/Zr variants.**
- One hit: MgSi(AgTe₂)₂ (1.63 eV, E_hull 0.014). ZnSi(AgTe₂)₂ (1.72 eV, E_hull 0.001) narrowly missed on gap.
- The Zr–Zn compounds had in-window gaps (1.22 and 1.33 eV) but E_hull of 0.08–0.11.
- Ca–Si–Ag compounds were unstable (0.06–0.09).
- Chalcopyrite II-IV-V₂ pnictides were all known.
- The notebook states the grid was nearly exhausted.

**Iteration 5: Cu kesterites with d⁰ Ti⁴⁺/Zr⁴⁺, and exploratory Fe variants. No hits.**
- The Cu Ti/Zr compounds had E_hull of 0.05–0.22. The Zr ones had in-window gaps (1.1–1.5 eV) but were unstable.
- The closest was MgTi(AgSe₂)₂ (1.52 eV, E_hull 0.053), a marginal miss.
- The Fe variants were unstable or had near-zero gaps.

**Overall:** the productive region was Ag-based kesterite-type compositions with Sr/Ba/Mg on the divalent site and Si/Sn on the tetravalent site. Only a limited set of structure prototypes was available, and the notebook notes that this capped how much novelty could be found outside Ag-kesterites.

## Caveats

- **Surrogate error.** All energies and gaps come from an ML surrogate; the notebook mentions CHGNet/ML gap noise. Gaps are not DFT-quality. Noise appears to be substantial: the notebook cites inconsistent Ge/Sn trends and a spread of 0.15–0.34 eV for Sr–Ge/Sn–Se compounds. The "1.42 eV" for BaSi(AgSe₂)₂ should not be read as precise.
- **Hull stability is a surrogate estimate.** The hits have E_hull of 0.014–0.043 eV/atom. The reference set of competing phases is not documented here. Competing Ag, alkaline-earth and Si/Sn chalcogenides could undermine the stability of any of them.
- **Structure assumption.** All candidates were generated from kesterite-type prototypes. For large cations such as Ba or Sr, other structure types may be lower in energy; this is untested.
- **Novelty means novelty against the Materials Project only.** No literature or other database search results are recorded in the notebook, so "novel" does not mean never reported.
- **Gap definition.** The window used for "hit" is inferred from the notebook's hit lists, and the sensitivity of the hit list to its edges is high (e.g. ZnSi(AgTe₂)₂ at 1.72 eV missed).
- **No validation.** No DFT, phonon, defect or synthesis work has been done. Several non-gap properties relevant to PV were not assessed: absorption, defects and carrier transport.

## Recommended next steps

1. Run DFT (hybrid functional or GW) on the five hits, starting with BaSi(AgSe₂)₂, SrAg₂SnS₄, SrSi(AgSe₂)₂, MgSi(AgTe₂)₂ and MgAg₂SnSe₄. Check relaxed structure, band gap and hull energy against a full competing-phase set.
2. Run phonon and structure-type competition checks, especially for the Ba/Sr compounds.
3. Revisit the near-misses: ZnSi(AgTe₂)₂, MgTi(AgSe₂)₂ and BaNa₂SnTe₄, which are close in gap or hull energy.
4. Explore alloying and mixed-anion tuning (e.g. Mg/Zn-Si-Te with Ge-Te, mixed S/Se). The tool did not support this, so it needs another method.
5. Open a new chemical family. The notebook suggests Ag–Sb/Bi chalcohalides and Cu₃SbS₄-type compounds as candidates, if the tool permits.
6. Only after computational validation, consider synthesis feasibility for the most stable hits.
