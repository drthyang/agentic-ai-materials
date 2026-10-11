# Campaign report: pv-absorber-v1

## Executive summary

Over five iterations I screened about 94 novel kesterite-type quaternary chalcogenides with CHGNet relaxations and a surrogate HSE-fidelity band-gap model. The goal was a gap of 1.1–1.7 eV (centred near 1.4 eV) with a low energy above hull (E_hull ≤ 0.05 eV/atom). By my strict count, 20 novel compounds meet both criteria. One more, SrCu2SnSe4, narrowly misses at E_hull = 0.0504. The best-looking compounds are K2MnGeSe4 (1.44 eV, E_hull 0.000), K2CaGeTe4 (1.42 eV, 0.019), K2MgSnTe4 (1.33 eV, 0.000), K2MgGeTe4 (1.50 eV, 0.000), Na2CdSnTe4 (1.37 eV, 0.032) and CdAg2GeSe4 (1.28 eV, 0.000). **Confidence is low to moderate.** Every number comes from ML surrogates with no DFT, phonon or experimental check, and the Mn compounds and large-cation members have specific reasons for extra doubt (see Caveats).

## Scored candidates

Window = gap 1.1–1.7 eV, E_hull ≤ 0.05 eV/atom and novel in the Materials Project (MP). E_f is the formation energy in eV/atom, E_hull is in eV/atom and the gap is in eV. A ✓ marks window hits. All entries are novel except CdAg2SnSe4, which MP flagged as known. It was evaluated by mistake and is not a discovery.

### Iteration 1 (Ag/Cu kesterites, 14 scored)
| Formula | E_f | E_hull | Gap | Window |
|---|---|---|---|---|
| CdAg2GeSe4 | -0.657 | 0.000 | 1.279 | ✓ |
| ZnAg2GeSe4 | -0.681 | 0.000 | 1.119 | ✓ |
| MgAg2SnS4 | -1.177 | 0.002 | 1.871 | |
| CdAg2GeTe4 | -0.326 | 0.017 | 0.481 | |
| MgAg2GeS4 | -1.165 | 0.017 | 1.893 | |
| MgAg2GeSe4 | -0.797 | 0.020 | 1.856 | |
| CdAg2SnTe4 | -0.366 | 0.027 | 0.412 | |
| ZnAg2GeTe4 | -0.318 | 0.028 | 1.171 | ✓ |
| ZnAg2SnTe4 | -0.358 | 0.039 | 0.596 | |
| MgCu2SnSe4 | -0.819 | 0.071 | 1.383 | |
| CdSi(AgSe2)2 | -0.568 | 0.130 | 1.714 | |
| MgCu2GeSe4 | -0.717 | 0.136 | 1.102 | |
| MgSi(AgSe2)2 | -0.715 | 0.145 | 2.348 | |
| CdSi(AgS2)2 | -0.937 | 0.152 | 2.751 | |

### Iteration 2 (Zr/Ti/Mn/Ca Cu-selenides and alkali kesterites, 20 scored)
| Formula | E_f | E_hull | Gap | Window |
|---|---|---|---|---|
| ZrCd(CuSe2)2 | -1.141 | 0.000 | 0.146 | |
| MgZr(CuSe2)2 | -1.276 | 0.000 | 0.190 | |
| CaZr(CuSe2)2 | -1.491 | 0.000 | 0.040 | |
| SrZr(CuSe2)2 | -1.496 | 0.000 | 0.078 | |
| BaZr(CuSe2)2 | -1.453 | 0.000 | 0.104 | |
| CdAg2SnSe4 (known in MP) | -0.700 | 0.000 | 1.262 | n/a |
| K2CdGeSe4 | -1.169 | 0.000 | 2.409 | |
| K2CdSnTe4 | -0.899 | 0.000 | 0.864 | |
| Na2ZnSnSe4 | -1.121 | 0.007 | 2.292 | |
| Na2CdSnSe4 | -1.085 | 0.019 | 1.957 | |
| Na2ZnSnTe4 | -0.712 | 0.023 | 2.053 | |
| Na2CdSnTe4 | -0.699 | 0.032 | 1.367 | ✓ |
| MnCu2GeSe4 | -0.531 | 0.104 | 0.931 | |
| CaCu2GeSe4 | -0.928 | 0.121 | 1.198 | |
| BaTi(CuSe2)2 | -0.962 | 0.361 | 2.680 | |
| SrTi(CuSe2)2 | -0.900 | 0.425 | 2.583 | |
| MgTi(CuSe2)2 | -0.677 | 0.443 | 2.706 | |
| TiMn(CuSe2)2 | -0.437 | 0.465 | 2.454 | |
| TiCd(CuSe2)2 | -0.487 | 0.479 | 2.805 | |
| CaTi(CuSe2)2 | -0.829 | 0.488 | 2.617 | |

### Iteration 3 (alkali-Mg tellurides/selenides and alkaline-earth Ag/Cu kesterites, 20 scored)
| Formula | E_f | E_hull | Gap | Window |
|---|---|---|---|---|
| K2MgSnTe4 | -0.977 | 0.000 | 1.329 | ✓ |
| K2MgGeTe4 | -0.948 | 0.000 | 1.499 | ✓ |
| SrAg2SnSe4 | -1.059 | 0.000 | 1.701 | (just outside) |
| BaAg2GeTe4 | -0.704 | 0.000 | 0.705 | |
| BaCu2SnTe4 | -0.750 | 0.001 | 0.395 | |
| SrAg2GeSe4 | -1.021 | 0.003 | 1.687 | ✓ |
| BaAg2SnTe4 | -0.746 | 0.007 | 0.516 | |
| SrAg2GeTe4 | -0.651 | 0.016 | 0.155 | |
| SrAg2SnTe4 | -0.689 | 0.029 | 0.100 | |
| K2MgSnSe4 | -1.311 | 0.030 | 2.536 | |
| K2MgGeSe4 | -1.288 | 0.034 | 2.497 | |
| Na2MgGeTe4 | -0.759 | 0.047 | 1.136 | ✓ |
| SrCu2SnSe4 | -1.045 | 0.0504 | 1.109 | (borderline, hull just over) |
| CaAg2SnSe4 | -0.998 | 0.051 | 1.816 | |
| Na2MgGeSe4 | -1.186 | 0.055 | 2.448 | |
| Na2MgSnSe4 | -1.209 | 0.055 | 2.156 | |
| Na2MgSnTe4 | -0.782 | 0.055 | 1.932 | |
| CaAg2GeSe4 | -0.949 | 0.062 | 1.679 | |
| CaAg2SnTe4 | -0.625 | 0.072 | 0.062 | |
| CaCu2SnSe4 | -0.979 | 0.108 | 0.944 | |

### Iteration 4 (K/Na-II-IV tellurides, 20 scored)
| Formula | E_f | E_hull | Gap | Window |
|---|---|---|---|---|
| K2ZnSiTe4 | -0.802 | 0.000 | 2.069 | |
| K2CdSiTe4 | -0.798 | 0.000 | 1.235 | ✓ |
| K2BaGeTe4 | -1.187 | 0.000 | 1.566 | ✓ |
| Na2CaGeTe4 | -1.098 | 0.000 | 1.731 | |
| Na2CaSiTe4 | -1.026 | 0.000 | 2.047 | |
| K2MgSiTe4 | -0.868 | 0.005 | 1.692 | ✓ |
| K2SrSnTe4 | -1.128 | 0.012 | 1.199 | ✓ |
| K2SrGeTe4 | -1.087 | 0.013 | 1.216 | ✓ |
| K2CaGeTe4 | -1.059 | 0.019 | 1.421 | ✓ |
| K2CaSnTe4 | -1.085 | 0.033 | 1.118 | ✓ |
| BaNa2GeTe4 | -0.978 | 0.063 | 1.759 | |
| BaNa2SnTe4 | -1.004 | 0.066 | 1.704 | |
| Na2ZnSiTe4 | -0.615 | 0.094 | 2.791 | |
| K2CaSiTe4 | -0.972 | 0.098 | 1.455 | |
| K2SrSiTe4 | -0.987 | 0.105 | 1.875 | |
| Na2CdSiTe4 | -0.600 | 0.105 | 1.796 | |
| Na2SrGeTe4 | -0.913 | 0.113 | 1.692 | |
| Na2SrSnTe4 | -0.933 | 0.124 | 1.725 | |
| Na2MgSiTe4 | -0.677 | 0.134 | 2.155 | |
| Na2CaSnTe4 | -0.865 | 0.169 | 1.458 | |

### Iteration 5 (Mn-containing alkali chalcogenides and others, 20 scored)
| Formula | E_f | E_hull | Gap | Window |
|---|---|---|---|---|
| K2MnGeSe4 | -1.142 | 0.000 | 1.443 | ✓ |
| K2MnSnTe4 | -0.932 | 0.000 | 0.646 | |
| Na2MnSnSe4 | -1.074 | 0.000 | 1.115 | ✓ |
| Na2CaSnSe4 | -1.477 | 0.000 | 2.633 | |
| Na2CaGeSe4 | -1.438 | 0.000 | 2.794 | |
| K2MnGeTe4 | -0.709 | 0.002 | 1.0996 | (just below 1.1) |
| Na2MnGeSe4 | -1.035 | 0.008 | 1.646 | ✓ |
| K2CdSiSe4 | -1.099 | 0.009 | 2.686 | |
| K2MgSiSe4 | -1.224 | 0.022 | 2.874 | |
| K2ZnSiSe4 | -1.135 | 0.036 | 2.950 | |
| K2MnSiSe4 | -1.073 | 0.040 | 1.675 | ✓ |
| Na2MnGeTe4 | -0.588 | 0.043 | 1.088 | |
| K2MnSiTe4 | -0.694 | 0.045 | 1.455 | ✓ |
| Na2MnSnTe4 | -0.618 | 0.046 | 0.947 | |
| SrSi(AgTe2)2 | -0.561 | 0.077 | 1.508 | |
| Na2SrSnSe4 | -1.369 | 0.099 | 1.745 | |
| CaSi(AgTe2)2 | -0.493 | 0.122 | 1.247 | |
| SrSi(AgSe2)2 | -0.933 | 0.130 | 2.071 | |
| Na2MnSiSe4 | -0.956 | 0.151 | 1.561 | |
| Na2MnSiTe4 | -0.506 | 0.165 | 2.035 | |

Proposed versus scored per iteration: iteration 1 proposed 27 and scored 14. Iteration 2 proposed 72, filtered out 19 and scored 20. Iterations 3, 4 and 5 proposed 41, 24 and 31, and scored 20 each.

**Discrepancy with the notebook:** the iteration 5 reflection says "~25 novel window hits". Applying the criteria above to the scored data gives 20 strict hits (3, 1, 4, 7 and 5 across iterations 1–5). The notebook figure appears to be loose.

## Hypotheses tested and what was learned

1. **Iteration 1: isoelectronic substitution in the I2-II-IV-VI4 kesterite (Cu→Ag, Zn→Cd/Mg, Sn→Ge/Si, S→Se/Te).**
   - Ag-Ge-Se kesterites with Zn or Cd were hits, and ZnAg2GeTe4 was a hit too.
   - Mg-Ag sulfides and Mg-Ag-Ge-Se gave gaps of 1.86–1.89 eV, which is too wide.
   - Ag tellurides mostly gave gaps of 0.4–0.6 eV, which is too low.
   - Si variants were unstable (E_hull 0.13–0.15).
   - Cu-Mg-Sn/Ge selenides had gaps in the window but E_hull of 0.071 and 0.136.
2. **Iteration 2: Cu2-II-IV-Se4 with Zr/Ti/Mn/Ca, and alkali-for-Cu kesterites.**
   - **Na2CdSnTe4** (1.37 eV, E_hull 0.032) was the only new window hit.
   - Alkali kesterites were generally stable, but most had gaps of 1.96–2.41 eV, apart from K2CdSnTe4 at 0.86 eV.
   - Ti analogues were strongly unstable (E_hull 0.36–0.49).
   - **The Zr analogues have E_hull = 0 but gaps of only 0.04–0.19 eV.** I regard these as not credible, since Zr⁴⁺ (d⁰) selenides should have wider gaps. They are probably model artefacts or a different structure type.
   - The chalcopyrite and zincblende prototypes mostly returned compounds already in MP, so they yielded nothing new.
3. **Iteration 3: neighbours of Na2CdSnTe4 (alkali-Mg tellurides) and alkaline-earth Ag/Cu kesterites.**
   - K2MgSnTe4 and K2MgGeTe4 are stable (E_hull 0) with gaps of 1.33 and 1.50 eV.
   - SrAg2GeSe4 (1.69 eV) sits at the upper edge of the window, and SrAg2SnSe4 (1.701 eV) falls just outside it.
   - Mg-alkali selenides were too wide (2.2–2.5 eV).
   - Sr/Ba Ag tellurides were stable but had gaps of 0.1–0.7 eV.
   - Ca-based Ag/Cu compounds were unstable (E_hull 0.05–0.11).
4. **Iteration 4: K/Na-II-IV tellurides, with II = Mg/Zn/Cd/Ca/Sr/Ba and IV = Si/Ge/Sn.**
   - Seven window hits, the most productive batch: K2CaGeTe4, K2CdSiTe4, K2BaGeTe4, K2SrSnTe4, K2SrGeTe4, K2CaSnTe4 and K2MgSiTe4.
   - K stabilises large II cations (Ca/Sr/Ba), while Na prefers smaller ones. Most Na compounds with large II cations or with Si were unstable.
5. **Iteration 5: Mn on the II site and other K/Na substitutions.**
   - Five hits: K2MnGeSe4, Na2MnGeSe4, Na2MnSnSe4, K2MnSiSe4 and K2MnSiTe4.
   - K2MnGeTe4 (1.0996 eV) and Na2MnGeTe4 are just below the window.
   - K2(Zn,Cd,Mg)SiSe4 and Na2Ca(Sn,Ge)Se4 gave gaps of 2.6–2.95 eV, too wide.

**Rough trends from the data:** Te lowers the gap by about 1 eV relative to Se. Sn gives lower gaps than Ge, and Cd lower than Zn. Mn lowers the gap relative to Mg or Zn. K stabilises more compositions than Na.

## Caveats

- **Surrogate error.** E_hull comes from CHGNet relaxations measured against known MP competing phases only. Band gaps come from an ML model at HSE fidelity. Both have unquantified error bars, and the 1.1–1.7 eV window and the 0.05 eV/atom hull cutoff are narrower than plausible model errors. Several results sit on the boundary: SrAg2SnSe4 at 1.701 eV, K2MnGeTe4 at 1.0996 eV and SrCu2SnSe4 at E_hull 0.0504.
- **Structure assumption.** All candidates were generated by substitution on kesterite-type prototypes. Large-II members (K2CaGeTe4, K2SrGeTe4, K2BaGeTe4 and similar) probably have a different true ground-state structure. A hull of 0 or near 0 relative to known phases does not show they are stable in the kesterite arrangement, or that undiscovered competing phases are absent.
- **Mn compounds.** The gaps are from a non-magnetic treatment. Mn d–d states and magnetic ordering are not captured, so the K2MnGeSe4 gap in particular is unreliable.
- **Zr and Ti Cu-selenides.** The Zr results (near-zero gaps with E_hull 0) are likely artefacts and should not be treated as candidates.
- **No other validation.** There is no DFT confirmation, no phonon or dynamic-stability check, no defect, doping or absorption analysis, and no synthesis feasibility assessment. Tellurides and alkali-containing chalcogenides are also likely to be air- or moisture-sensitive, which was not assessed.

## Recommended next steps

1. Run spin-polarised DFT with HSE (or GW) on the top candidates to confirm gaps. These are K2MnGeSe4 (check AFM versus FM), K2CaGeTe4, K2MgSnTe4, K2MgGeTe4, Na2CdSnTe4, CdAg2GeSe4, ZnAg2GeSe4 and K2BaGeTe4.
2. Recompute the hull with a wider set of competing phases and alternative structure types. For the large-II K compounds, check against K2BaSnTe4-type structures and the known K-Ge-Se, K-Ge-Te and K-Mn-Ge phases.
3. Run phonon stability calculations, and calculate optical absorption and effective masses for the DFT-confirmed survivors.
4. Drop the Zr and Ti Cu-selenides unless an independent calculation supports them.
5. Consider alloying studies around the boundary cases, such as Sr(Ag,Cu)2(Sn,Ge)Se4 and K2(Mn,Mg)GeSe4/Te4. The aim is to move boundary compounds into the window, but any alloy results would need the same validation.
6. Assess the synthesis route and air stability for the K- and Na-containing tellurides before investing in experiments.
