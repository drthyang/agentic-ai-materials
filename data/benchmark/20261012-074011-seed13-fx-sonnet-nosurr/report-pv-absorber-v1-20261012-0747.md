# Campaign report: pv-absorber-v1

## Executive summary

Over five iterations, 92 candidates were relaxed and scored, 91 of them novel against the Materials Project (one known calibration point, CdCu2SnS4). Seven candidates had a surrogate gap in the 1.1–1.7 eV window the notebook used and a computed energy above hull of 0.043 eV/atom or less. The strongest are BaSi(AgSe2)2 (1.42 eV, 0.026 eV/atom), Ag3SbSe4 (1.26 eV, 0.000 eV/atom), CuAg2AsS4 and Cu2AgAsS4 (1.56 and 1.63 eV, about 0.01 eV/atom), and SrAg2SnS4 (1.67 eV, 0.024 eV/atom). Confidence is low to moderate. All values are surrogate-model outputs with no DFT or experimental validation. The notebook itself records that the gaps are noisy and that the kesterite-type hull energies are probably optimistic for some families. The results are best read as a shortlist for DFT follow-up, not as confirmed absorbers.

## Scored candidates

Columns are formation energy per atom (E_f, eV/atom), energy above hull (E_hull, eV/atom), surrogate band gap (eV) and the novelty flag. Every row was converged. The "In window" column marks a gap of 1.1–1.7 eV, the range used in the notebook. A "Yes" does not mean E_hull is low.

### Iteration 1 (17 scored)
| Formula | E_f | E_hull | Gap | Novel | In window |
|---|---|---|---|---|---|
| CdAg2GeSe4 | -0.551 | 0.000 | 0.026 | yes | |
| CdSi(AgSe2)2 | -0.599 | 0.000 | 0.745 | yes | |
| CdCu2SnS4 | -0.686 | 0.000 | 0.598 | **no** (calibration) | |
| ZnSi(AgSe2)2 | -0.614 | 0.000 | 1.841 | yes | |
| CdSi(AgS2)2 | -0.721 | 0.000 | 2.220 | yes | |
| ZnAg2GeSe4 | -0.567 | 0.003 | 0.677 | yes | |
| MgAg2GeS4 | -0.798 | 0.006 | 1.777 | yes | |
| MgAg2SnS4 | -0.788 | 0.011 | 0.691 | yes | |
| MgSi(AgSe2)2 | -0.739 | 0.011 | 1.837 | yes | |
| MgSi(AgS2)2 | -0.908 | 0.012 | 2.463 | yes | |
| MgCu2SnS4 | -0.866 | 0.014 | 0.490 | yes | |
| MgAg2GeSe4 | -0.690 | 0.018 | 0.282 | yes | |
| MgCu2SnTe4 | -0.537 | 0.026 | 0.346 | yes | |
| MgCu2GeSe4 | -0.713 | 0.030 | 0.307 | yes | |
| MgCu2SiTe4 | -0.461 | 0.034 | 0.245 | yes | |
| MgAg2SnSe4 | -0.700 | 0.043 | 1.153 | yes | Yes (marginal hull) |
| MgCu2SnSe4 | -0.734 | 0.047 | 0.189 | yes | |

### Iteration 2 (20 scored)
| Formula | E_f | E_hull | Gap | Novel | In window |
|---|---|---|---|---|---|
| NaGaS2 | -1.193 | 0.000 | 4.245 | yes | |
| NaAlS2 | -1.462 | 0.000 | 4.084 | yes | |
| Ag3SbS4 | -0.372 | 0.000 | 0.152 | yes | |
| Ag3SbSe4 | -0.360 | 0.000 | 1.255 | yes | **Yes** |
| CuAg2SbSe4 | -0.377 | 0.000 | 0.851 | yes | |
| Ag3AsSe4 | -0.319 | 0.000 | 0.211 | yes | |
| Cu2AgPSe4 | -0.363 | 0.000 | 1.934 | yes | |
| CuAg2SbS4 | -0.409 | 0.007 | 0.455 | yes | |
| Cu2AgSbS4 | -0.448 | 0.009 | 0.474 | yes | |
| ZnGeSb2 | -0.127 | 0.009 | 0.239 | yes | |
| Cu2AgAsS4 | -0.412 | 0.010 | 1.627 | yes | **Yes** |
| CuAg2AsS4 | -0.372 | 0.012 | 1.560 | yes | **Yes** |
| CuAg2PS4 | -0.458 | 0.014 | 2.421 | yes | |
| CdGeSb2 | -0.109 | 0.032 | 0.135 | yes | |
| ZnSiSb2 | -0.075 | 0.048 | 0.906 | yes | |
| CuBiTe2 | -0.334 | 0.052 | 1.446 | yes | gap yes, hull marginal |
| CdSiSb2 | -0.071 | 0.057 | 0.200 | yes | |
| MgSnSb2 | -0.231 | 0.079 | 0.035 | yes | |
| MgGeSb2 | -0.181 | 0.081 | 0.058 | yes | |
| CuAsS2 | -0.370 | 0.085 | 0.681 | yes | |

### Iteration 3 (20 scored)
| Formula | E_f | E_hull | Gap | Novel | In window |
|---|---|---|---|---|---|
| SrAg2GeS4 | -0.971 | 0.017 | 1.946 | yes | |
| SrAg2GeSe4 | -0.879 | 0.035 | 0.150 | yes | |
| KSbTe2 | -0.682 | 0.054 | 0.361 | yes | |
| CaAg2GeS4 | -0.928 | 0.060 | 1.752 | yes | |
| CaAg2GeSe4 | -0.833 | 0.068 | 0.258 | yes | |
| BaTi(CuSe2)2 | -1.124 | 0.089 | 2.408 | yes | |
| CaCu2GeS4 | -0.966 | 0.090 | 2.625 | yes | |
| CaCu2GeSe4 | -0.829 | 0.110 | 0.301 | yes | |
| BaZr(AgSe2)2 | -1.174 | 0.110 | 0.136 | yes | |
| KAsS2 | -0.784 | 0.114 | 2.821 | yes | |
| SrZr(AgSe2)2 | -1.138 | 0.135 | 0.117 | yes | |
| SrTi(CuSe2)2 | -1.075 | 0.140 | 2.505 | yes | |
| BaTi(CuS2)2 | -1.265 | 0.142 | 2.204 | yes | |
| BaZr(AgS2)2 | -1.273 | 0.144 | 0.379 | yes | |
| SrZr(AgS2)2 | -1.250 | 0.149 | 1.610 | yes | gap yes, unstable |
| SrZr(CuS2)2 | -1.245 | 0.179 | 1.119 | yes | gap yes, unstable |
| BaZr(CuSe2)2 | -1.115 | 0.184 | 0.083 | yes | |
| BaZr(CuS2)2 | -1.261 | 0.184 | 1.161 | yes | gap yes, unstable |
| SrZr(CuSe2)2 | -1.073 | 0.215 | 0.789 | yes | |
| CaZr(CuSe2)2 | -1.035 | 0.244 | 1.309 | yes | gap yes, unstable |

### Iteration 4 (16 scored)
| Formula | E_f | E_hull | Gap | Novel | In window |
|---|---|---|---|---|---|
| Na2CdGeS4 | -1.061 | 0.005 | 3.406 | yes | |
| Na2CdGeSe4 | -0.961 | 0.010 | 2.438 | yes | |
| Na2CdSnSe4 | -0.983 | 0.011 | 3.142 | yes | |
| SrAg2SnS4 | -0.961 | 0.024 | 1.667 | yes | **Yes** (upper edge) |
| Na2MgSnS4 | -1.222 | 0.031 | 3.278 | yes | |
| Na2MgGeSe4 | -1.088 | 0.042 | 3.034 | yes | |
| Na2MgSnSe4 | -1.110 | 0.044 | 3.001 | yes | |
| BaNa2SnS4 | -1.401 | 0.045 | 3.432 | yes | |
| SrAg2SnSe4 | -0.896 | 0.052 | 0.340 | yes | |
| Na2SrSnS4 | -1.382 | 0.053 | 3.353 | yes | |
| BaNa2SnSe4 | -1.314 | 0.055 | 2.533 | yes | |
| CaAg2SnS4 | -0.922 | 0.063 | 0.517 | yes | |
| Na2SrSnSe4 | -1.291 | 0.067 | 2.823 | yes | |
| Na2CaSnS4 | -1.353 | 0.084 | 3.351 | yes | |
| CaAg2SnSe4 | -0.851 | 0.089 | 1.454 | yes | gap yes, unstable |
| Na2CaSnSe4 | -1.253 | 0.096 | 2.972 | yes | |

### Iteration 5 (19 scored)
| Formula | E_f | E_hull | Gap | Novel | In window |
|---|---|---|---|---|---|
| SrSi(AgSe2)2 | -0.932 | 0.021 | 1.694 | yes | **Yes** (upper edge) |
| BaSi(AgSe2)2 | -0.965 | 0.026 | 1.423 | yes | **Yes** |
| BaSi(AgS2)2 | -1.106 | 0.029 | 2.565 | yes | |
| SrSi(AgS2)2 | -1.083 | 0.033 | 2.543 | yes | |
| BaCu2SiSe4 | -0.952 | 0.054 | 1.812 | yes | |
| SrCu2SiSe4 | -0.913 | 0.055 | 1.736 | yes | |
| SrCu2SiS4 | -1.103 | 0.058 | 3.173 | yes | |
| BaAg2GeTe4 | -0.682 | 0.059 | 0.203 | yes | |
| BaCu2SiS4 | -1.119 | 0.060 | 3.133 | yes | |
| CaSi(AgSe2)2 | -0.883 | 0.061 | 2.177 | yes | |
| SrAg2SnTe4 | -0.697 | 0.067 | 0.033 | yes | |
| SrSi(AgTe2)2 | -0.610 | 0.067 | 1.894 | yes | |
| SrAg2GeTe4 | -0.645 | 0.068 | 0.690 | yes | |
| BaAg2SnTe4 | -0.724 | 0.068 | 0.230 | yes | |
| BaSi(AgTe2)2 | -0.645 | 0.069 | 2.147 | yes | |
| CaAg2SnTe4 | -0.660 | 0.081 | 0.046 | yes | |
| SrCu2SnSe4 | -0.902 | 0.083 | 0.105 | yes | |
| CaAg2GeTe4 | -0.607 | 0.083 | 0.868 | yes | |
| CaSi(AgTe2)2 | -0.569 | 0.086 | 1.920 | yes | |

### Shortlist: in-window gap and E_hull ≤ 0.043 eV/atom
| Formula | Gap (eV) | E_hull (eV/atom) | Iteration |
|---|---|---|---|
| Ag3SbSe4 | 1.255 | 0.000 | 2 |
| Cu2AgAsS4 | 1.627 | 0.010 | 2 |
| CuAg2AsS4 | 1.560 | 0.012 | 2 |
| SrSi(AgSe2)2 | 1.694 | 0.021 | 5 |
| SrAg2SnS4 | 1.667 | 0.024 | 4 |
| BaSi(AgSe2)2 | 1.423 | 0.026 | 5 |
| MgAg2SnSe4 | 1.153 | 0.043 | 1 |

SrSi(AgSe2)2 and SrAg2SnS4 sit at the upper edge of the window, and MgAg2SnSe4 has a marginal hull value.

## Hypotheses tested and what was learned

**Iteration 1: kesterite (Cu2ZnSnS4-type) isoelectronic substitutions (Zn→Cd/Mg, Sn→Ge/Si, S→Se/Te, Cu→Ag).**
- The substitutions gave many near-hull compounds (E_hull 0–0.047), so the family is energetically accessible on this lattice.
- Gaps rarely landed in the window. Cu, Se and Te variants and Sn/Ge-Cu compounds came out too narrow (about 0.2–0.6 eV). Si and Mg variants and Ag-S compounds came out too wide (1.78–2.46 eV).
- The only in-window result was MgAg2SnSe4 (1.15 eV), which is marginal on stability (0.043 eV/atom).
- Mixed-anion or mixed-cation compounds could not be built, because the tool substitutes whole sites. 3 relaxations went unspent because no novel candidates remained.

**Iteration 2: chalcopyrite I-III-VI2 and II-IV-V2 pnictides, plus I3-V-VI4 and I-V-VI2 compounds.**
- The antimonide chalcopyrites had gaps of 0.04–0.9 eV and E_hull of 0.01–0.08, so they were too narrow.
- 29 proposals were filtered out before scoring, and the notebook records that the phosphide ones were filtered by SMACT.
- NaGaS2 and NaAlS2 are on the hull but have gaps above 4 eV.
- The I3-V-VI4 compounds on the kesterite lattice gave three in-window, near-stable hits: Ag3SbSe4, CuAg2AsS4 and Cu2AgAsS4.
- Gaps are non-monotonic across chemically similar compounds (Ag3SbS4 at 0.15 eV against Ag3SbSe4 at 1.26 eV). The notebook flags this as likely surrogate noise.
- CuBiTe2 has a gap of 1.446 eV but an E_hull of 0.052 eV/atom, which just misses.

**Iteration 3: alkaline-earth + Zr/Ti + Cu/Ag chalcogenides, plus a few I-V-VI2 compounds. The hypothesis was falsified.**
- The family was only partly reached. Per the notebook, the I3-V-VI4 and I-V-VI2 families were mostly "already considered", and only KSbTe2, KBiTe2 and KAsS2 came up as novel, so the campaign pivoted to alkaline-earth/Zr/Ti kesterite-type compounds. The scored KBiTe2 does not appear in the data; only KSbTe2 and KAsS2 were scored.
- All Zr/Ti compounds were unstable on the kesterite lattice (E_hull about 0.09–0.24 eV/atom). Several had in-window gaps (BaZr(CuS2)2 1.16, SrZr(AgS2)2 1.61, CaZr(CuSe2)2 1.31 eV), but these are not credible given the instability.
- SrAg2GeS4 (0.017 eV/atom, 1.95 eV) is stable but too wide.
- SrAg2GeSe4 (0.035 eV/atom, 0.15 eV) is stable but too narrow. The notebook notes the Ag-Ge-Se gaps look suspiciously low.
- No hits.
- The notebook states the literature search returned nothing useful for this iteration.

**Iteration 4: unexplored II-IV-Ag2/Cu2-Q4 members, with Sr/Ba/Mg/Cd/Zn/Na.**
- SrAg2SnS4 (1.667 eV, 0.024 eV/atom) was the one in-window, near-stable hit.
- The Na2-based compounds are stable (E_hull 0.005–0.045 for the best members) but have gaps of roughly 2.4–3.4 eV, so they are too wide.
- The Ca variants were unstable or noisy. CaAg2SnSe4 has a gap of 1.454 eV but an E_hull of 0.089 eV/atom. CaAg2SnS4 has a gap of 0.52 eV.
- 4 relaxations went unspent because only wide-gap candidates remained.

**Iteration 5: neighbours of SrAg2SnS4 (Ba/Sr/Ca, Ag/Cu, Si/Ge/Sn, S/Se/Te).**
- The hypothesis held. BaSi(AgSe2)2 (1.423 eV, 0.026 eV/atom) is the best gap match in the campaign, and SrSi(AgSe2)2 (1.694 eV, 0.021 eV/atom) sits at the window edge.
- The sulfide analogues are stable (E_hull 0.029 and 0.033 eV/atom) but too wide (about 2.55 eV).
- The Cu analogues (E_hull 0.054–0.083 eV/atom) and all Te analogues (E_hull 0.059–0.086 eV/atom) are unstable.
- The Ca member is unstable (0.061 eV/atom) with a gap of 2.18 eV.
- The zincblende proposals were all known or trivial and were not evaluated.

**Overall pattern.** Ag-rich kesterite-type chalcogenides with a large divalent cation (Sr, Ba) or mixed I3-V-VI4 chemistry, in sulfides and selenides, give the best combination of gap and stability in this dataset. Tellurides, Zr/Ti compounds and Ca members were consistently unstable.

## Caveats

- **Surrogate gaps are not DFT-grade.** The notebook refers to the gaps as coming from a surrogate (CHGNet / HSE-surrogate). It flags that some gaps look implausible, such as the non-monotonic Ag3SbS4/Ag3SbSe4 values and the very low Ag-Ge-Se and Ag-Sn-Se gaps. Error bars were not quantified. A gap near the 1.1–1.7 eV window edges could easily move out of it.
- **Hull energies are probably optimistic for the kesterite-type lattice.** Many of these compositions probably adopt other structures in reality. Ba/Sr-Ag-Si-Se compounds likely prefer something like the BaAg2GeS4 type, and the I3-V-VI4 compounds have known enargite and famatinite polymorphs. Low E_hull on the assumed lattice does not show that this lattice is the ground state.
- **Hull energies are small and sit near typical metastability limits.** Several shortlisted values are 0.02–0.04 eV/atom, which is within normal surrogate error.
- **Limited scope.** The tool cannot build mixed-anion or mixed-cation compounds, so alloy-type tuning, which the notebook identifies as the likely route to gaps near 1.4 eV, was not explored.
- **Properties are limited to the surrogate gap and hull.** There is no information on absorption strength, band alignment, direct vs. indirect gap, defect tolerance, or toxicity.
- **No validation of any kind.** No DFT or synthesis was performed.
- **Novelty is only versus the Materials Project database.** It is not an exhaustive literature or ICSD check.

## Recommended next steps

1. Run DFT with a hybrid or GW gap, plus a structure search across competing polymorphs, on the seven shortlisted compounds. Prioritize BaSi(AgSe2)2, Ag3SbSe4, CuAg2AsS4, Cu2AgAsS4 and SrAg2SnS4.
2. Compute phonons and the full competing-phase hull for these, including the known enargite/famatinite and BaAg2GeS4-type polymorphs, to test the lattice assumption.
3. Explore mixed S/Se anion alloys, for example Ba-Si-Ag-(S,Se) or SrAg2Ge(S,Se)4. The notebook notes that the S and Se end-members bracket the window, so alloys could land inside it. This needs a tool or workflow that supports mixed sites.
4. Deprioritize Zr/Ti kesterite-type compounds, Te analogues, Ca analogues and the Na2-based family, which were unstable or too wide-gap in this campaign.
5. Where synthesis is feasible, make the lowest-risk candidates first (Ag3SbSe4 and the CuAg2AsS4 / Cu2AgAsS4 pair, with hull values of 0.000–0.012 eV/atom) and check structure and optical gap experimentally.
