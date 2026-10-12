# Campaign report: pv-absorber-v1

## Executive summary

Over five iterations, 98 novel (absent from Materials Project) kesterite-type compounds were scored for photovoltaic-absorber suitability. The working window was a band gap of 1.1–1.7 eV with e_hull ≤ 0.05 eV/atom. Six candidates met both criteria: MgAg2SnSe4, MgSi(AgTe2)2, SrAg2SnS4, NiAg2SiSe4, BaAg2SiSe4 and SrAg2SiSe4. The best result is **BaAg2SiSe4**, with a predicted gap of 1.42 eV and e_hull of 0.026 eV/atom. Confidence is low to moderate. All values are surrogate-model estimates with no DFT or experimental validation, several hits sit at the edge of the window, and the notebook itself warns that the kesterite prototype may not be the true ground-state structure for Ba and Sr. The campaign was a single-prototype study, and no candidate has been checked beyond the screening model.

## Scored candidates

All 98 candidates are flagged novel and converged. E_f is formation energy per atom (eV), E_hull is energy above hull (eV/atom), and Gap is the band gap (eV). "Hit" means gap in 1.1–1.7 eV and E_hull ≤ 0.05. Values are rounded to three decimals.

### Iteration 1 (20 scored)
| Formula | E_f | E_hull | Gap | Hit |
|---|---|---|---|---|
| CdAg2GeSe4 | -0.551 | 0.000 | 0.026 | |
| CdSi(AgSe2)2 | -0.599 | 0.000 | 0.745 | |
| CdSi(AgS2)2 | -0.721 | 0.000 | 2.220 | |
| ZnSi(AgSe2)2 | -0.614 | 0.000 | 1.841 | |
| ZnSi(AgTe2)2 | -0.355 | 0.001 | 1.717 | |
| ZnAg2GeSe4 | -0.567 | 0.003 | 0.677 | |
| MgAg2GeS4 | -0.798 | 0.006 | 1.777 | |
| CdSi(AgTe2)2 | -0.344 | 0.008 | 0.332 | |
| MgAg2SnS4 | -0.788 | 0.011 | 0.691 | |
| MgSi(AgSe2)2 | -0.739 | 0.011 | 1.837 | |
| MgCu2SnS4 | -0.866 | 0.014 | 0.490 | |
| MgSi(AgTe2)2 | -0.447 | 0.014 | 1.627 | **Yes** |
| CdAg2SnTe4 | -0.425 | 0.015 | 0.031 | |
| MgAg2GeTe4 | -0.479 | 0.015 | 0.870 | |
| MgAg2GeSe4 | -0.690 | 0.018 | 0.282 | |
| ZnAg2SnTe4 | -0.424 | 0.019 | 0.438 | |
| MgCu2GeSe4 | -0.713 | 0.030 | 0.307 | |
| MgCu2SiTe4 | -0.461 | 0.034 | 0.245 | |
| MgAg2SnSe4 | -0.700 | 0.043 | 1.153 | **Yes** |
| MgCu2SnSe4 | -0.734 | 0.047 | 0.189 | |

### Iteration 2 (20 scored)
| Formula | E_f | E_hull | Gap | Hit |
|---|---|---|---|---|
| SrAg2GeS4 | -0.971 | 0.017 | 1.946 | |
| SrAg2SnS4 | -0.961 | 0.024 | 1.667 | **Yes** |
| SrAg2GeSe4 | -0.879 | 0.035 | 0.150 | |
| SrAg2SnSe4 | -0.896 | 0.052 | 0.340 | |
| SrCu2SiSe4 | -0.913 | 0.055 | 1.736 | |
| SrCu2SiS4 | -1.103 | 0.058 | 3.173 | |
| CaAg2GeS4 | -0.928 | 0.060 | 1.752 | |
| CaAg2SnS4 | -0.922 | 0.063 | 0.517 | |
| CaAg2GeSe4 | -0.833 | 0.068 | 0.258 | |
| SrCu2SnSe4 | -0.902 | 0.083 | 0.105 | |
| CaCu2SiS4 | -1.066 | 0.089 | 3.311 | |
| CaCu2SnS4 | -0.976 | 0.089 | 2.199 | |
| CaAg2SnSe4 | -0.851 | 0.089 | 1.454 | (gap only) |
| CaCu2GeS4 | -0.966 | 0.090 | 2.625 | |
| MgZr(CuS2)2 | -1.147 | 0.093 | 1.138 | (gap only) |
| CaCu2SnSe4 | -0.860 | 0.117 | 0.212 | |
| MgZr(CuSe2)2 | -0.939 | 0.144 | 1.545 | (gap only) |
| SrZr(CuS2)2 | -1.245 | 0.179 | 1.119 | (gap only) |
| CaZr(CuS2)2 | -1.227 | 0.197 | 0.909 | |
| SrZr(CuSe2)2 | -1.073 | 0.215 | 0.789 | |

### Iteration 3 (20 scored; 53 proposed, 27 filtered out)
| Formula | E_f | E_hull | Gap | Hit |
|---|---|---|---|---|
| TiCd(AgS2)2 | -0.921 | 0.007 | 2.228 | |
| TiZn(AgSe2)2 | -0.847 | 0.014 | 1.887 | |
| TiCd(AgSe2)2 | -0.818 | 0.019 | 0.609 | |
| BaTi(AgSe2)2 | -1.164 | 0.035 | 2.033 | |
| MgTi(AgS2)2 | -1.088 | 0.040 | 1.785 | |
| BaTi(AgS2)2 | -1.280 | 0.049 | 2.245 | |
| MgTi(AgSe2)2 | -0.943 | 0.053 | 1.516 | (near miss: gap OK, hull slightly high) |
| BaAg2GeTe4 | -0.682 | 0.059 | 0.203 | |
| BaAg2SnTe4 | -0.724 | 0.068 | 0.230 | |
| SrTi(AgSe2)2 | -1.129 | 0.071 | 2.326 | |
| CaAg2SnTe4 | -0.660 | 0.081 | 0.046 | |
| CaAg2GeTe4 | -0.607 | 0.083 | 0.868 | |
| ZrCd(AgSe2)2 | -0.822 | 0.088 | 0.014 | |
| ZrCd(AgS2)2 | -0.920 | 0.097 | 1.877 | |
| BaZr(AgSe2)2 | -1.174 | 0.110 | 0.136 | |
| MgZr(AgSe2)2 | -0.950 | 0.119 | 0.116 | |
| MgZr(AgS2)2 | -1.083 | 0.134 | 0.230 | |
| BaZr(AgS2)2 | -1.273 | 0.144 | 0.379 | |
| CaZr(AgSe2)2 | -1.092 | 0.173 | 0.092 | |
| CaZr(AgS2)2 | -1.217 | 0.185 | 0.208 | |

### Iteration 4 (20 scored)
| Formula | E_f | E_hull | Gap | Hit |
|---|---|---|---|---|
| MnAg2GeS4 | -0.593 | 0.021 | 0.248 | |
| TiMn(AgSe2)2 | -0.747 | 0.031 | 0.110 | |
| NiAg2GeSe4 | -0.443 | 0.031 | 0.308 | |
| NiAg2GeS4 | -0.507 | 0.033 | 2.453 | |
| NiAg2SnS4 | -0.514 | 0.034 | 1.769 | |
| SiNi(AgSe2)2 | -0.484 | 0.036 | 1.632 | **Yes** |
| NiAg2SnSe4 | -0.463 | 0.049 | 0.638 | |
| TiZn(AgTe2)2 | -0.573 | 0.051 | 0.065 | |
| MnSi(AgS2)2 | -0.686 | 0.052 | 0.086 | |
| TiNi(AgS2)2 | -0.824 | 0.053 | 2.293 | |
| TiMn(AgTe2)2 | -0.470 | 0.065 | 0.169 | |
| TiNi(AgSe2)2 | -0.695 | 0.072 | 1.483 | (gap only) |
| TiNi(AgTe2)2 | -0.487 | 0.084 | 0.002 | |
| TiMn(AgS2)2 | -0.872 | 0.092 | 1.392 | (gap only) |
| TiCo(AgS2)2 | -0.786 | 0.117 | 1.723 | |
| TiCo(AgSe2)2 | -0.651 | 0.127 | 1.124 | (gap only) |
| TiCo(AgTe2)2 | -0.437 | 0.133 | 0.002 | |
| TiFe(AgS2)2 | -0.785 | 0.171 | 0.977 | |
| TiFe(AgSe2)2 | -0.631 | 0.173 | 0.334 | |
| TiFe(AgTe2)2 | -0.385 | 0.179 | 0.009 | |

### Iteration 5 (18 scored)
| Formula | E_f | E_hull | Gap | Hit |
|---|---|---|---|---|
| Cu2NiGeS4 | -0.602 | 0.010 | 0.486 | |
| Cu2SiNiSe4 | -0.523 | 0.014 | 0.235 | |
| SrSi(AgSe2)2 | -0.932 | 0.021 | 1.694 | **Yes** (edge) |
| Cu2NiGeSe4 | -0.486 | 0.023 | 0.894 | |
| BaSi(AgSe2)2 | -0.965 | 0.026 | 1.423 | **Yes** |
| BaSi(AgS2)2 | -1.106 | 0.029 | 2.565 | |
| SrSi(AgS2)2 | -1.083 | 0.033 | 2.543 | |
| BaCu2SiSe4 | -0.952 | 0.054 | 1.812 | |
| CoCu2SiSe4 | -0.485 | 0.055 | 0.229 | |
| BaCu2SiS4 | -1.119 | 0.060 | 3.133 | |
| CaSi(AgSe2)2 | -0.883 | 0.061 | 2.177 | |
| CaSi(AgS2)2 | -1.039 | 0.067 | 2.272 | |
| CoAg2SnS4 | -0.504 | 0.069 | 0.477 | |
| CoAg2GeSe4 | -0.416 | 0.073 | 0.153 | |
| CoAg2SnSe4 | -0.441 | 0.074 | 0.231 | |
| CoSi(AgSe2)2 | -0.455 | 0.076 | 0.757 | |
| CoAg2GeS4 | -0.491 | 0.078 | 0.598 | |
| CoSi(AgS2)2 | -0.578 | 0.103 | 1.893 | |

### The six hits, ranked by gap proximity to 1.4 eV
| Formula | Gap (eV) | E_hull (eV/atom) | Comment |
|---|---|---|---|
| BaAg2SiSe4 | 1.423 | 0.026 | Best overall result |
| MgAg2SnSe4 | 1.153 | 0.043 | Near lower edge of gap window; highest hull energy among hits |
| MgSi(AgTe2)2 | 1.627 | 0.014 | Near upper edge |
| NiAg2SiSe4 | 1.632 | 0.036 | Near upper edge |
| SrAg2SnS4 | 1.667 | 0.024 | Near upper edge |
| SrAg2SiSe4 | 1.694 | 0.021 | Within 0.006 eV of the upper limit |

## Hypotheses tested and what was learned

**Iteration 1: isoelectronic substitution in I2-II-IV-VI4 kesterites.** The proposal varied Ag/Cu, Zn/Cd/Mg, Sn/Ge/Si and S/Se/Te.
- All 20 candidates came out near-stable (e_hull ≤ 0.047).
- Two hits: MgAg2SnSe4 and MgSi(AgTe2)2.
- Si and S raised the gap. Cu, Te and Sn lowered it.
- CdAg2GeSe4 has a gap of about 0 eV. The notebook attributes this to a likely model artefact or metallic behaviour.
- The hypothesis partially held.

**Iteration 2: large A-site cations (Ca, Sr) with Ag and Cu, plus Zr on the B-site.**
- One hit: SrAg2SnS4, at the upper edge of the window.
- CaAg2SnSe4 has an in-window gap (1.454 eV) but is unstable (e_hull 0.089).
- All Ca/Sr-Cu kesterites had e_hull of 0.055–0.12, and the Zr-Cu compounds had 0.09–0.21.
- Sr stabilised the Ag kesterites best.
- The zincblende-derived and chalcopyrite attempts were not usable for novelty. The notebook says the zincblende prototype returned only known binaries. Chalcopyrite substitution returned mostly known compounds, and the two novel ones (NaGaS2, NaAlS2) were not evaluated.

**Iteration 3: Ag-Te with Ca/Ba, and Ti or Zr on the group-IV site with Ag.**
- No hits.
- Ag-Te compounds with Ca/Ba had e_hull of 0.059–0.083 and small gaps.
- Zr-Ag compounds were all unstable (e_hull 0.088–0.185).
- The Ti-Ag family was stable and its gap tuned with the A-site: for Ti-Se, Cd gave 0.61, Mg 1.52 and Zn 1.89 eV.
- MgTi(AgSe2)2 was a near miss (1.516 eV, e_hull 0.053).

**Iteration 4: transition-metal A-sites (Mn, Fe, Co, Ni) with Ti and with group-14 B-sites.**
- One new hit: NiAg2SiSe4.
- Ni2+ stabilised Ag kesterites well (e_hull about 0.03–0.05).
- Fe and Co Ti compounds were unstable (e_hull 0.11–0.18). The Ti-Te compounds had gaps of about 0 eV.
- Mn gaps were low. The notebook suspects a magnetic or PBE-type artefact, which was not tested.
- Te consistently collapsed the gap.

**Iteration 5: Ni/Co/Cu A-sites and large alkaline-earth Ag-Si-chalcogenides.**
- Two new hits: BaAg2SiSe4 and SrAg2SiSe4.
- The notebook concludes that a large A-site cation combined with the small Si B-site and Ag is the best-performing combination in this campaign.
- The Co-Ag kesterites were all unstable (e_hull 0.069–0.103).
- Ca-Si-Ag and Ba/Cu-Si compounds fell outside the stability threshold.
- The Ni-Cu compounds were stable but had low gaps.

**Overall:** iterations 2 and 3 had little or no success. The campaign recovered by changing the A-site and B-site chemistry. Sulfides generally have gaps that are too wide (2.2–2.6 eV for Ba/Sr-Si-S). Selenides of Ba/Sr/Ni with Si land in the window. Te and Cd-Se compounds tend to have gaps that are too small.

## Caveats

- **Surrogate-model uncertainty.** Gaps and hull energies are ML-surrogate predictions, not DFT or experimental values. No error bars were computed. The notebook describes the gaps as model estimates, and several results are suspicious (gaps near 0 eV for Cd-Ge-Se, Ti-Te and Zr compounds; Mn and Co gaps that look artefactual). Neither the gap nor the stability prediction should be taken at face value for the transition-metal compounds.
- **Window edges.** Four of the six hits (SrAg2SiSe4, SrAg2SnS4, NiAg2SiSe4, MgSi(AgTe2)2) are within 0.08 eV of the upper limit, and MgAg2SnSe4 is within 0.06 eV of the lower limit. Modest model error would remove them from the window.
- **Structure assumption.** All candidates are kesterite-type substitutions. The notebook notes that Ba and Sr analogs may adopt other structure types in reality. This applies directly to the top candidate, so its true e_hull could differ substantially, and competing phases were not explored.
- **Hull reference.** E_hull values are relative to the database used here. Many e_hull ≈ 0.000 values are probably competing-phase artefacts of an incomplete reference set, not evidence of stability. This is my interpretation and was not checked in the campaign.
- **Mixed-anion and mixed-cation tuning.** Single-site substitution could not reach intermediate compositions, so the 1.4 eV target was approached only by whichever endpoint happened to land near it.
- **Properties not assessed.** Absorption coefficient, direct versus indirect gap, defect tolerance, carrier properties and toxicity or cost were not evaluated. The notebook's gap labels do not say whether gaps are direct. Notebook-flagged sticking points for transition-metal compounds are magnetism and PBE-type gap errors.
- **Novelty.** "Novel" means absent from Materials Project only, and no literature check of the final hits is recorded in the notebook. Some may exist in other databases or the literature.

## Recommended next steps

1. **Validate the top candidates with DFT.** Start with BaAg2SiSe4, SrAg2SiSe4, SrAg2SnS4, NiAg2SiSe4, MgAg2SnSe4 and MgSi(AgTe2)2. Use hybrid-functional or GW gaps and a full competing-phase hull. Check dynamical stability and direct versus indirect character.
2. **Test alternative structure types for Ba/Sr.** Compare against the structure types adopted by related Ba/Sr chalcogenides before spending synthesis effort on the kesterite polymorph.
3. **Explore mixed-site compositions** such as Ba/Sr mixing or S/Se mixing around BaAg2SiSe4, SrAg2SnS4 and SrAg2SiSe4. This would fine-tune the gap toward 1.4 eV, which single-site substitution cannot do.
4. **Revisit the artefact-prone families only with better methods.** Mn/Fe/Co and the Ti-Te and Zr compounds need spin-polarised or hybrid treatment before their predictions can be trusted.
5. **Look beyond kesterites for novelty.** The zincblende and chalcopyrite approaches returned almost entirely known compounds. Other families (for example Cu-Sb-S types or Na/K-In/Ga chalcogenides, suggested in the iteration 1–2 reflections) were not tried.
6. **Experimental feasibility.** If DFT supports the Ba-Si-Ag-Se family, assess phase competition with binaries and ternaries in the Ba-Ag-Si-Se system, and the practicality of Ag-based absorbers, before any synthesis attempt.
