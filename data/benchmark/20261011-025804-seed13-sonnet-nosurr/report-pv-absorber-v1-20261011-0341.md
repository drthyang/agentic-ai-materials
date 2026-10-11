# Campaign report: pv-absorber-v1

## Executive summary

The campaign ran five iterations and relaxed 91 candidates (20, 18, 15, 18 and 20 per iteration). The target was PV-absorber-like compounds with a band gap of about 1.1–1.7 eV and a low energy above the hull. The most useful result is the Ag-based, kesterite-type selenides and tellurides with Ge or Sn on the IV site, and the Ag-rich Sb/As selenide famatinite-type compounds. Their gaps fall in the target window with computed E_hull of 0–0.04 eV/atom. The best novel candidates are CdAg2GeSe4 (E_hull 0.000, gap 1.28 eV), ZnAg2GeSe4 (0.000, 1.12), CuAg2AsSe4 (0.000, 1.38), CuAg2SbSe4 (0.000, 1.46) and MgAg2GeTe4 (0.025, 1.49). All numbers come from a CHGNet-relaxed, ML band-gap surrogate with no DFT or experimental validation. Confidence is moderate for the main-group Ag chalcogenides and low for the Ni-containing and I–V–VI2 hits.

## Scored candidates

Columns: iteration, formula, formation energy (eV/atom), E_above_hull (eV/atom), band gap (eV, surrogate "HSE-fidelity"), and novelty versus Materials Project. All entries converged. Only ZnAg2SnSe4 was flagged as already known. It was run as a deliberate calibration point.

| Iter | Formula | E_form | E_hull | Gap (eV) | Novel |
|---|---|---|---|---|---|
| 1 | CdAg2GeSe4 | -0.657 | 0.000 | 1.28 | yes |
| 1 | ZnAg2SnSe4 (calibration) | -0.721 | 0.000 | 1.12 | no |
| 1 | ZnAg2GeSe4 | -0.681 | 0.000 | 1.12 | yes |
| 1 | SrAg2SnSe4 | -1.059 | 0.000 | 1.70 | yes |
| 1 | MgAg2SnS4 | -1.177 | 0.002 | 1.87 | yes |
| 1 | SrAg2GeSe4 | -1.021 | 0.003 | 1.69 | yes |
| 1 | MgAg2SnSe4 | -0.838 | 0.016 | 1.59 | yes |
| 1 | MgAg2GeS4 | -1.165 | 0.017 | 1.89 | yes |
| 1 | MgAg2GeSe4 | -0.797 | 0.020 | 1.86 | yes |
| 1 | ZnAg2SnTe4 | -0.358 | 0.039 | 0.60 | yes |
| 1 | CaAg2SnSe4 | -0.998 | 0.051 | 1.82 | yes |
| 1 | CaAg2GeSe4 | -0.949 | 0.062 | 1.68 | yes |
| 1 | CaAg2SnS4 | -1.297 | 0.068 | 2.28 | yes |
| 1 | CaAg2GeS4 | -1.273 | 0.094 | 2.15 | yes |
| 1 | MgCu2GeTe4 | -0.372 | 0.101 | 0.90 | yes |
| 1 | CdSi(AgSe2)2 | -0.568 | 0.130 | 1.71 | yes |
| 1 | MgCu2GeSe4 | -0.717 | 0.136 | 1.10 | yes |
| 1 | MgSi(AgSe2)2 | -0.715 | 0.145 | 2.35 | yes |
| 1 | CdSi(AgS2)2 | -0.937 | 0.152 | 2.75 | yes |
| 1 | MgSi(AgS2)2 | -1.132 | 0.167 | 2.54 | yes |
| 2 | ZrCd(AgSe2)2 | -1.148 | 0.000 | 0.30 | yes |
| 2 | ZrMn(AgSe2)2 | -1.127 | 0.000 | 0.00 | yes |
| 2 | ZrZn(AgSe2)2 | -1.183 | 0.000 | 0.65 | yes |
| 2 | SrCu2SnTe4 | -0.751 | 0.000 | 0.87 | yes |
| 2 | SrAg2GeTe4 | -0.651 | 0.016 | 0.16 | yes |
| 2 | CdAg2GeTe4 | -0.326 | 0.017 | 0.48 | yes |
| 2 | MgAg2GeTe4 | -0.423 | 0.025 | 1.49 | yes |
| 2 | CdAg2SnTe4 | -0.366 | 0.027 | 0.41 | yes |
| 2 | ZnAg2GeTe4 | -0.318 | 0.028 | 1.17 | yes |
| 2 | SrAg2SnTe4 | -0.689 | 0.029 | 0.10 | yes |
| 2 | MgAg2SnTe4 | -0.461 | 0.038 | 1.17 | yes |
| 2 | SrCu2SnSe4 | -1.045 | 0.050 | 1.11 | yes |
| 2 | MgCu2SnSe4 | -0.819 | 0.071 | 1.38 | yes |
| 2 | SrCu2GeTe4 | -0.614 | 0.078 | 0.16 | yes |
| 2 | MgCu2SnTe4 | -0.409 | 0.109 | 0.48 | yes |
| 2 | TiZn(AgSe2)2 | -0.617 | 0.353 | 2.23 | yes |
| 2 | TiCd(AgSe2)2 | -0.590 | 0.357 | 2.35 | yes |
| 2 | TiMn(AgSe2)2 | -0.492 | 0.395 | 2.21 | yes |
| 3 | Cu2AgSbS4 | -0.855 | 0.000 | 1.74 | yes |
| 3 | Cu2AgSbSe4 | -0.523 | 0.000 | 0.43 | yes |
| 3 | Cu2AgAsS4 | -0.824 | 0.000 | 1.87 | yes |
| 3 | Cu2AgAsSe4 | -0.483 | 0.000 | 0.44 | yes |
| 3 | CuAg2SbS4 | -0.856 | 0.000 | 1.86 | yes |
| 3 | CuAg2SbSe4 | -0.565 | 0.000 | 1.46 | yes |
| 3 | CuAg2AsS4 | -0.828 | 0.000 | 1.97 | yes |
| 3 | CuAg2AsSe4 | -0.530 | 0.000 | 1.38 | yes |
| 3 | Ag3SbS4 | -0.856 | 0.000 | 1.79 | yes |
| 3 | Ag3SbSe4 | -0.573 | 0.000 | 1.67 | yes |
| 3 | Ag3AsSe4 | -0.541 | 0.000 | 1.68 | yes |
| 3 | NaAg2SbS4 | -1.069 | 0.000 | 2.21 | yes |
| 3 | NaAg2SbSe4 | -0.778 | 0.000 | 1.90 | yes |
| 3 | NaAg2AsS4 | -1.045 | 0.000 | 2.17 | yes |
| 3 | NaAg2AsSe4 | -0.747 | 0.000 | 1.92 | yes |
| 4 | NiAg2SnSe4 | -0.631 | 0.000 | 1.68 | yes |
| 4 | NiAg2SnS4 | -0.936 | 0.000 | 1.90 | yes |
| 4 | NiAg2GeSe4 | -0.583 | 0.0005 | 1.65 | yes |
| 4 | NiAg2GeS4 | -0.911 | 0.008 | 1.74 | yes |
| 4 | Cu2NiGeS4 | -0.979 | 0.013 | 1.12 | yes |
| 4 | NiAg2GeTe4 | -0.281 | 0.036 | 0.13 | yes |
| 4 | Cu2NiGeSe4 | -0.577 | 0.041 | 0.25 | yes |
| 4 | NiAg2SnTe4 | -0.323 | 0.045 | 0.04 | yes |
| 4 | CoAg2SnSe4 | -0.569 | 0.056 | 0.60 | yes |
| 4 | FeAg2SnSe4 | -0.579 | 0.072 | ~0.00 | yes |
| 4 | Cu2NiGeTe4 | -0.252 | 0.074 | 0.09 | yes |
| 4 | CoAg2GeSe4 | -0.524 | 0.075 | 0.81 | yes |
| 4 | Cu2NiSnTe4 | -0.288 | 0.076 | 0.14 | yes |
| 4 | FeAg2GeSe4 | -0.525 | 0.078 | 0.02 | yes |
| 4 | CoAg2GeTe4 | -0.229 | 0.087 | 0.00 | yes |
| 4 | MnCu2GeSe4 | -0.531 | 0.104 | 0.93 | yes |
| 4 | FeAg2GeTe4 | -0.199 | 0.112 | 0.01 | yes |
| 4 | FeAg2SnTe4 | -0.243 | 0.119 | 0.01 | yes |
| 5 | CuAsS2 | -0.868 | 0.000 | 1.46 | yes |
| 5 | KSbTe2 | -0.741 | 0.000 | 0.55 | yes |
| 5 | KAsS2 | -1.409 | 0.000 | 2.45 | yes |
| 5 | CuAg2PSe4 | -0.476 | 0.000 | 2.15 | yes |
| 5 | CuAg2SbTe4 | -0.279 | 0.000 | 0.31 | yes |
| 5 | Cu3SbTe4 | -0.251 | 0.001 | 0.32 | yes |
| 5 | KBiTe2 | -0.736 | 0.003 | 1.30 | yes |
| 5 | Cu2AgPSe4 | -0.425 | 0.045 | 2.14 | yes |
| 5 | Cu2AgSbTe4 | -0.211 | 0.045 | 0.38 | yes |
| 5 | CuBiTe2 | -0.247 | 0.093 | 0.63 | yes |
| 5 | CaSnSb2 | -0.431 | 0.118 | 0.01 | yes |
| 5 | MgSnSb2 | -0.112 | 0.123 | 0.01 | yes |
| 5 | MgGeSb2 | -0.054 | 0.177 | 0.01 | yes |
| 5 | SrGeAs2 | -0.503 | 0.184 | 0.55 | yes |
| 5 | SrSnAs2 | -0.535 | 0.184 | 0.05 | yes |
| 5 | CaSnAs2 | -0.463 | 0.215 | 0.03 | yes |
| 5 | CaGeAs2 | -0.455 | 0.220 | 0.65 | yes |
| 5 | SrSiAs2 | -0.464 | 0.242 | 1.73 | yes |
| 5 | MgZrAs2 | -0.643 | 0.251 | 0.04 | yes |
| 5 | CaSiAs2 | -0.401 | 0.302 | 1.86 | yes |

### Candidates in or near the target window (gap about 1.1–1.7 eV, E_hull ≤ about 0.05 eV/atom)

- **Main-group Ag kesterite-type selenides:**
  - CdAg2GeSe4 (1.28 eV), ZnAg2GeSe4 (1.12) and MgAg2SnSe4 (1.59, E_hull 0.016).
  - SrAg2GeSe4 (1.69) and SrAg2SnSe4 (1.70) sit at the upper edge of the window.
- **Ag tellurides:** MgAg2GeTe4 (1.49, E_hull 0.025), ZnAg2GeTe4 (1.17, 0.028) and MgAg2SnTe4 (1.17, 0.038).
- **Famatinite-type I3–V–VI4:** CuAg2AsSe4 (1.38) and CuAg2SbSe4 (1.46). Ag3SbSe4 (1.67) and Ag3AsSe4 (1.68) are at the edge. All four have E_hull 0.000.
- **Ni-containing (low confidence):** NiAg2GeSe4 (1.65), NiAg2SnSe4 (1.68) and Cu2NiGeS4 (1.12, E_hull 0.013).
- **I–V–VI2 in a chalcopyrite cell (low to moderate confidence):** CuAsS2 (1.46, E_hull 0.000) and KBiTe2 (1.30, E_hull 0.003).
- **Borderline:** SrCu2SnSe4 (1.11 eV, E_hull 0.050).

## Hypotheses tested and what was learned

The notebook has hypothesis entries for iterations 1, 3 and 4. Iterations 2 and 5 have only observation and reflection entries.

**Iteration 1: isoelectronic kesterite substitution** (Ag for Cu; Cd, Mg, Ca or Sr for Zn; Ge or Si for Sn; S, Se or Te for the chalcogen).
- Supported for Ag selenides with Ge or Sn and Zn, Cd, Mg or Sr (the novel hits listed above).
- Si-containing Ag kesterites failed (E_hull 0.13–0.17), as did Ca analogs (0.05–0.09). Cu–Mg–Ge–Se and Cu–Mg–Ge–Te also failed (E_hull 0.10–0.14).
- Sulfides had gaps that were too wide and tellurides too narrow, so Se was the sweet spot.
- The critic vetoed MgCu2SiTe4 for size mismatch.
- The notebook says 21 compounds were evaluated, but the database holds 20 for this iteration.

**Iteration 2: Zr and Ti on the IV site, Ba on the A site, and Ag tellurides.**
- Zr compounds had E_hull 0.000 but gaps of 0–0.65 eV, so they are too narrow.
- Ti compounds were unstable (E_hull above 0.35).
- Ba was vetoed for size mismatch.
- The small-cation Ag tellurides gave hits: MgAg2GeTe4, ZnAg2GeTe4 and MgAg2SnTe4.
- Cd and Sr tellurides had gaps of 0.1–0.5 eV. The notebook states these trends:
  - Ge gives wider gaps than Sn.
  - For the A-site cation, Mg > Zn > Cd > Sr.
- Two relaxations went unspent.

**Iteration 3: Cu/Ag/Na I3–V–VI4 famatinite-type compounds with Sb or As.**
- Supported for the Ag-rich selenides. All 15 evaluated had E_hull 0.000, which is suspicious: the notebook suggests the Materials Project hull may lack competing Ag–Sb–Se and Cu–Sb–Se phases.
- Gap rises with Ag fraction, and sulfides are wider than selenides.
- Sulfides were too wide (1.74–2.21 eV), Cu2Ag selenides too narrow (about 0.43 eV), and NaAg2 compounds too wide (1.90–2.21 eV).
- The critic vetoed Cu2AgBiS4 and Cu2AgBiSe4 for charge imbalance. The notebook acknowledges this was a proposal error.
- Five relaxations went unspent.

**Iteration 4: 3d divalent metals (Mn, Fe, Co, Ni) in kesterite-type cells.**
- Fe and Co failed (E_hull 0.056–0.119, gaps near 0–0.8 eV), and so did MnCu2GeSe4 (E_hull 0.104).
- Ni gave stable in-window entries, but Ni2+ is d8 and not normally tetrahedral. The notebook flags the surrogate gaps for Ni, Fe and Co as unreliable.
- The zincblende prototype produced only known binaries (in the notebook, not in the table) and was not useful.

**Iteration 5: I–V–VI2 compounds in a chalcopyrite-type cell, II–IV–V2 pnictides, and P/Sb–Te famatinites.**
- Per the notebook, the kesterite chalcogenide space was already exhausted: all new proposals there were "already considered".
- CuAsS2 and KBiTe2 are the in-window hits. The notebook warns that:
  - The Cu–As–S and K–Bi–Te Materials Project hulls are sparse. CuAsS is a stable competitor, and only K3BiTe3 is listed for K–Bi–Te.
  - As3+ and Bi3+ lone-pair compounds probably prefer non-tetrahedral polymorphs.
- Misses:
  - KSbTe2 (0.55 eV), KAsS2 (2.45 eV) and CuBiTe2 (E_hull 0.093).
  - The II–IV–V2 pnictides with Ca, Sr or Mg: all E_hull 0.12–0.30.
  - CuAg2PSe4 (gap 2.15 eV) was too wide, and the Sb–Te famatinites too narrow (0.3–0.4 eV).
- The critic vetoed SrCu2SiSe4 and SrCu2SiTe4 for size mismatch.

## Caveats

- **Surrogate error.** All stabilities come from CHGNet relaxation with E_hull computed against the Materials Project hull. All gaps are from an ML "HSE-fidelity" predictor. Neither has been checked against DFT or experiment, and no error bars were computed.
- **Polymorph risk.** E_hull was assessed only in the kesterite-type, famatinite-type or chalcopyrite-type cell. The true ground states may be other polymorphs: stannite, wurtzite-derived, enargite, or rocksalt-derived for the lone-pair I–V–VI2 compounds. The notebook flags this repeatedly.
- **Hull completeness.** The 0.000 E_hull values for all iteration-3 compounds, and for CuAsS2, probably reflect missing competing phases in the database.
- **Ni, Fe, Co compounds.** Gaps and stability for open-shell 3d compounds are unreliable in this workflow.
- **Novelty.** Novelty means absence from the Materials Project database only. The notebook planned a literature check of ZnAg2GeSe4 and CdAg2GeSe4, but no result is recorded. Novelty beyond the database is unverified.
- **Not assessed.** Absorption coefficients, defect tolerance, band alignment, dynamic stability, and synthesizability were not examined.

## Recommended next steps

1. Run DFT (PBE+U or HSE) checks of the top candidates, starting with CdAg2GeSe4, ZnAg2GeSe4, CuAg2AsSe4, CuAg2SbSe4, MgAg2GeTe4 and MgAg2SnSe4. Compare kesterite-type against stannite and wurtzite-derived polymorphs, and against the full competing-phase set (Ag2Se, Sb2Se3, Ag3SbSe3, GeSe2 and similar).
2. Test the famatinite-type Ag–Sb/As–Se compounds against the real Ag–Sb–Se and Cu–Sb–Se phase diagrams, because every one came out at E_hull 0.000.
3. Check the literature for prior reports of the top candidates, to confirm they are new.
4. Try mixed S/Se or Se/Te anion alloys and Cu/Ag mixing to tune gaps. This needs prototype or supercell support that the current tool lacks.
5. Treat the Ni-containing and I–V–VI2 hits (NiAg2GeSe4, NiAg2SnSe4, Cu2NiGeS4, CuAsS2, KBiTe2) as low priority unless higher-level calculations support them.
6. If synthesis is considered, the Ag2–(Zn, Cd)–Ge–Se phase fields are the most plausible starting points, given their E_hull of 0.000 in this model.
