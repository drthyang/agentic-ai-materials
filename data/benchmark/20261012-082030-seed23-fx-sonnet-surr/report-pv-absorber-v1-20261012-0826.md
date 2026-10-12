# Campaign report: pv-absorber-v1

## Executive summary

Five iterations scored 100 candidates, 20 per iteration, with a surrogate (CHGNet-based) workflow. The target was a gap near 1.4 eV (the notebook treats roughly 1.1–1.7 eV as the "window") with a small energy above hull (ehull). Four novel compounds fell in that window with ehull ≤ 0.05 eV/atom: **BaAg2SiSe4** (written BaSi(AgSe2)2, gap 1.42 eV, ehull 0.026), **SrAg2SiSe4** (1.69 / 0.021), **SrAg2SnS4** (1.67 / 0.024) and **MgAg2SnSe4** (1.15 / 0.043). BaAg2SiSe4 is the closest to the target. These are surrogate predictions only, with no DFT or experimental confirmation. The notebook also warns that the assumed kesterite-type structure is probably not the true ground state for the Ba/Sr compounds. Treat all four as candidates to check, not as confirmed absorbers.

## Scored candidates

Columns: Ef = formation energy (eV/atom), ehull = energy above hull (eV/atom), Gap = predicted band gap (eV). All entries are flagged novel versus the Materials Project except FeAg2SnS4 (iteration 5), which is marked not novel.

### Iteration 1 (kesterite isoelectronic substitution)

| Formula | Ef | ehull | Gap |
|---|---|---|---|
| CdAg2GeSe4 | -0.551 | 0.000 | 0.03 |
| CdSi(AgSe2)2 | -0.599 | 0.000 | 0.75 |
| ZnSi(AgSe2)2 | -0.614 | 0.000 | 1.84 |
| CdSi(AgS2)2 | -0.721 | 0.000 | 2.22 |
| ZnAg2GeSe4 | -0.567 | 0.003 | 0.68 |
| MgAg2GeS4 | -0.798 | 0.006 | 1.78 |
| ZnAg2GeTe4 | -0.382 | 0.010 | 0.63 |
| MgAg2SnS4 | -0.788 | 0.011 | 0.69 |
| MgSi(AgSe2)2 | -0.739 | 0.011 | 1.84 |
| MgSi(AgS2)2 | -0.908 | 0.012 | 2.46 |
| MgCu2SnS4 | -0.866 | 0.014 | 0.49 |
| CdAg2GeTe4 | -0.375 | 0.014 | 0.17 |
| CdAg2SnTe4 | -0.425 | 0.015 | 0.03 |
| MgCu2GeTe4 | -0.502 | 0.017 | 0.52 |
| MgAg2GeSe4 | -0.690 | 0.018 | 0.28 |
| ZnAg2SnTe4 | -0.424 | 0.019 | 0.44 |
| MgCu2SnTe4 | -0.537 | 0.026 | 0.35 |
| MgCu2GeSe4 | -0.713 | 0.030 | 0.31 |
| **MgAg2SnSe4** | -0.700 | 0.043 | **1.15** |
| MgCu2SnSe4 | -0.734 | 0.047 | 0.19 |

### Iteration 2 (group-4 d0 cations, Ag/Cu kesterite-type, chalcopyrite attempt)

| Formula | Ef | ehull | Gap |
|---|---|---|---|
| NaGaS2 | -1.193 | 0.000 | 4.24 |
| TiZn(AgSe2)2 | -0.847 | 0.014 | 1.89 |
| TiZn(AgS2)2 | -0.951 | 0.022 | 2.05 |
| **SrAg2SnS4** | -0.961 | 0.024 | **1.67** |
| TiMn(AgSe2)2 | -0.747 | 0.031 | 0.11 |
| TiZn(CuSe2)2 | -0.840 | 0.035 | 3.05 |
| MgTi(AgSe2)2 | -0.943 | 0.053 | 1.52 |
| TiZn(CuS2)2 | -0.996 | 0.055 | 2.15 |
| CaAg2SnS4 | -0.922 | 0.063 | 0.52 |
| ZrZn(CuS2)2 | -1.020 | 0.065 | 1.12 |
| CaAg2GeSe4 | -0.833 | 0.068 | 0.26 |
| MgTi(CuS2)2 | -1.135 | 0.071 | 2.19 |
| ZrZn(AgSe2)2 | -0.853 | 0.080 | 1.33 |
| CaAg2SnSe4 | -0.851 | 0.089 | 1.45 |
| TiMn(AgS2)2 | -0.872 | 0.092 | 1.39 |
| ZrZn(CuSe2)2 | -0.849 | 0.098 | 1.63 |
| ZrZn(AgS2)2 | -0.957 | 0.106 | 1.22 |
| TiMn(CuSe2)2 | -0.673 | 0.119 | 2.45 |
| MgZr(AgS2)2 | -1.083 | 0.134 | 0.23 |
| ZrMn(AgS2)2 | -0.883 | 0.159 | 0.02 |

### Iteration 3 (alkaline-earth A-site kesterite-type)

| Formula | Ef | ehull | Gap |
|---|---|---|---|
| **SrSi(AgSe2)2** | -0.932 | 0.021 | **1.69** |
| **BaSi(AgSe2)2** | -0.965 | 0.026 | **1.42** |
| BaSi(AgS2)2 | -1.106 | 0.029 | 2.57 |
| SrSi(AgS2)2 | -1.083 | 0.033 | 2.54 |
| BaTi(AgSe2)2 | -1.164 | 0.035 | 2.03 |
| BaCu2SiSe4 | -0.952 | 0.054 | 1.81 |
| SrCu2SiSe4 | -0.913 | 0.055 | 1.74 |
| SrTi(AgS2)2 | -1.253 | 0.056 | 2.17 |
| SrCu2SiS4 | -1.103 | 0.058 | 3.17 |
| BaCu2SiS4 | -1.119 | 0.060 | 3.13 |
| CaSi(AgSe2)2 | -0.883 | 0.061 | 2.18 |
| CaSi(AgS2)2 | -1.039 | 0.067 | 2.27 |
| SrTi(AgSe2)2 | -1.129 | 0.071 | 2.33 |
| SrCu2SnSe4 | -0.902 | 0.083 | 0.10 |
| CaTi(AgS2)2 | -1.217 | 0.095 | 2.09 |
| CaTi(AgSe2)2 | -1.080 | 0.112 | 2.33 |
| SrTi(CuSe2)2 | -1.075 | 0.140 | 2.51 |
| SrTi(CuS2)2 | -1.246 | 0.142 | 2.39 |
| CaZr(AgSe2)2 | -1.092 | 0.173 | 0.09 |
| CaZr(AgS2)2 | -1.217 | 0.185 | 0.21 |

### Iteration 4 (alkali analogs and Ag–Te neighbors)

| Formula | Ef | ehull | Gap |
|---|---|---|---|
| K2BaSiSe4 | -1.397 | 0.000 | 3.39 |
| K2SrSiSe4 | -1.377 | 0.000 | 3.35 |
| BaNa2SnSe4 | -1.314 | 0.055 | 2.53 |
| BaNa2GeSe4 | -1.290 | 0.056 | 2.62 |
| BaNa2SnTe4 | -1.058 | 0.058 | 1.31 |
| BaAg2GeTe4 | -0.682 | 0.059 | 0.20 |
| K2BaSnSe4 | -1.368 | 0.066 | 2.16 |
| Na2SrSnSe4 | -1.291 | 0.067 | 2.82 |
| SrSi(AgTe2)2 | -0.610 | 0.067 | 1.89 |
| SrAg2GeTe4 | -0.645 | 0.068 | 0.69 |
| BaSi(AgTe2)2 | -0.645 | 0.069 | 2.15 |
| BaNa2SiSe4 | -1.349 | 0.072 | 3.36 |
| K2BaGeSe4 | -1.341 | 0.074 | 2.71 |
| Na2SrGeSe4 | -1.261 | 0.074 | 2.89 |
| Na2SrSiSe4 | -1.322 | 0.078 | 3.41 |
| K2SrSnSe4 | -1.352 | 0.084 | 2.42 |
| BaNa2GeTe4 | -0.992 | 0.095 | 1.83 |
| K2SrGeSe4 | -1.322 | 0.095 | 2.58 |
| BaNa2SiTe4 | -0.954 | 0.136 | 2.64 |
| Na2SrSiTe4 | -0.932 | 0.139 | 2.52 |

### Iteration 5 (open-shell 3d transition metals on the divalent site)

| Formula | Ef | ehull | Gap |
|---|---|---|---|
| MnAg2GeS4 | -0.593 | 0.021 | 0.25 |
| NiAg2GeS4 | -0.507 | 0.033 | 2.45 |
| SiNi(AgS2)2 | -0.606 | 0.049 | 0.41 |
| MnSi(AgS2)2 | -0.686 | 0.052 | 0.09 |
| CoAg2SnS4 | -0.504 | 0.069 | 0.48 |
| CoAg2GeSe4 | -0.416 | 0.073 | 0.15 |
| CoAg2SnSe4 | -0.441 | 0.074 | 0.23 |
| FeAg2GeSe4 | -0.419 | 0.075 | 0.15 |
| CoSi(AgSe2)2 | -0.455 | 0.076 | 0.76 |
| CoAg2GeS4 | -0.491 | 0.078 | 0.60 |
| MnCo(AgSe2)2 | -0.379 | 0.090 | 0.27 |
| FeAg2SnSe4 | -0.447 | 0.095 | 0.06 |
| MnFe(AgSe2)2 | -0.397 | 0.097 | 0.02 |
| CoSi(AgS2)2 | -0.578 | 0.103 | 1.89 |
| FeAg2GeS4 | -0.501 | 0.106 | 0.29 |
| MnNi(AgS2)2 | -0.491 | 0.107 | 0.97 |
| FeSi(AgSe2)2 | -0.448 | 0.109 | 0.01 |
| FeAg2SnS4 (not novel) | -0.516 | 0.112 | 0.36 |
| MnCo(AgS2)2 | -0.482 | 0.141 | 0.01 |
| MnFe(AgS2)2 | -0.489 | 0.188 | 0.02 |

Proposal counts per iteration were 50, 66, 42, 32 and 57. Iterations 2 and 5 filtered out 9 and 29 candidates, respectively. 20 candidates were scored in each iteration.

## Hypotheses tested and what was learned

**Iteration 1: isoelectronic substitution in the Cu2ZnSnS4 kesterite family (Ag for Cu, Cd/Mg for Zn, Si/Ge for Sn, S/Se/Te mixing).** This partly held.
- Nearly all 20 compounds were near-stable (ehull 0–0.047), so stability was easy to get.
- Gap tuning was the hard part, and only MgAg2SnSe4 landed in the window (1.15 eV, ehull 0.043, marginal).
- Observed trends were S > Se > Te for the gap, Si/Ge raising it, Ag raising it relative to Cu, and Cd lowering it, which the notebook calls odd.
- The Te compounds (0.03–0.6 eV) and the Cu–Mg compounds (roughly 0.2–0.5 eV) came out too narrow.

**Iteration 2: group-4 d0 cations (Ti, Zr) and Sr/Ca on the A-site, plus a chalcopyrite attempt.** This partly held.
- The chalcopyrite candidates were nearly all already in the Materials Project, so only NaGaS2 was scored. It was stable but had a 4.24 eV gap, which is useless here.
- Zr lowered the gap relative to Ti by about 0.7 eV but destabilized the compounds (ehull 0.065–0.106 for the Zr–Zn compounds, up to 0.159 for ZrMn(AgS2)2). Ti–Zn–Ag compounds were stable but their gaps were only about 1.9–2.0 eV.
- Sr stabilized the Ag–Sn–S kesterite-type relative to Ca (SrAg2SnS4: 1.667 eV, ehull 0.024; CaAg2SnS4: 0.52 eV, ehull 0.063).

**Iteration 3: larger alkaline-earth A-sites (Ca/Sr/Ba) with Ag/Cu, Si/Ti/Sn/Zr and S/Se.** This held and gave the best result of the campaign.
- For Ag–Si–Se, the gap fell as the A-site grew: Ca 2.18, Sr 1.69, Ba 1.42 eV.
- Ba and Sr also stabilized the compounds. BaSi(AgSe2)2 had ehull 0.026 and SrSi(AgSe2)2 had 0.021.
- The sulfur analogs were stable but too wide (about 2.5 eV).
- Se lowered the gap relative to S by roughly 0.6–1.1 eV depending on the cation set.
- Ca analogs were unstable (ehull 0.061–0.185), and the Cu analogs had ehull above 0.05 with gaps of 1.7–3.2 eV.

**Iteration 4: alkali (Na/K) analogs and Ag–Te neighbors of the Ba/Sr compounds.** This was mostly falsified.
- The stable compounds (K2BaSiSe4, K2SrSiSe4, ehull 0) had gaps of about 3.4 eV, which is too wide.
- The narrow-gap ones were unstable. The only in-window result was BaNa2SnTe4 (1.31 eV, ehull 0.058), just above the 0.05 cutoff.
- Te lowered the gap by about 1 eV but raised ehull by about 0.06–0.1.
- No new in-window near-stable compound was found.

**Iteration 5: Mn/Fe/Co/Ni on the divalent site.** This was falsified.
- None of the 20 compounds were in the window.
- Open-shell cations mostly collapsed the gap to near zero (Fe, Co, Mn–Fe and Mn–Co combinations) and mostly destabilized the structure (ehull up to 0.188).
- The exceptions were near-stable MnAg2GeS4 (0.25 eV, ehull 0.021) and NiAg2GeS4 (2.45 eV, ehull 0.033), but neither is in the window.
- The notebook states that all 20 were novel. The database flags FeAg2SnS4 as not novel, and the notebook does not call it out as a deliberate calibration point.
- The notebook also records that the zincblende prototype yielded only binaries, so it was dropped.

Overall, closed-shell cations (d0, d10, s0) combined with a large Ba or Sr A-site worked. Open-shell 3d metals, Te substitution and the alkali analogs did not produce stable compounds with gaps in the window.

## Caveats

- **Surrogate accuracy.** Gaps are CHGNet-HSE estimates, and ehull comes from a surrogate relaxation. No error bars were quantified in this campaign. The notebook itself notes that the predicted gaps for Cu compounds look low and that open-shell d compounds come out near-metallic. Quantitative gap values, including 1.42 eV for BaAg2SiSe4, should be treated as rough.
- **Structure assumption.** The Ba/Sr compounds were modeled in a kesterite-type prototype. The notebook flags that the real ground state is probably a different structure type, such as a BaAg2GeS4-type, so competing structures may be lower in energy. An ehull of 0.02–0.04 eV/atom means near-stable, not on the hull.
- **Novelty.** Novelty was judged against the Materials Project only. The notebook says the literature search gave nothing specific for the Sr/Ba compounds, so "novel" does not mean never reported in the literature.
- **Gap window.** The target window was never formally defined in the notebook. It was used implicitly as about 1.1–1.7 eV around 1.4 eV.
- **No validation.** Nothing was checked by DFT or synthesis. Trend statements come from small sets of 20 compounds per iteration.

## Recommended next steps

1. Run full DFT (HSE or GW) on BaAg2SiSe4, SrAg2SiSe4, SrAg2SnS4 and MgAg2SnSe4 to confirm the gaps and ehull.
2. Test competing structure types, for example the BaAg2GeS4-type and other Ba–Ag–chalcogenide structures. This should include phonon and decomposition-product checks against the competing ternary and binary phases.
3. If the structures hold up, check absorber-relevant properties such as band edges, optical absorption and defect tolerance, and assess synthesizability.
4. Follow the unexplored ideas the notebook raised, such as Se/Te anion mixing in BaAg2SiSe4, Ba(Si,Ge) mixing, Sr/Ba alloys and Ba(Na,Ag) mixed cations. These were limited by the prototype tool supporting only pure-element site substitutions.
5. Avoid the lines that stalled: open-shell 3d transition metals, Zr and Ca on the A/B sites, and the Na/K selenides.
