# Campaign report: pv-absorber-v1

## Executive summary

The goal was to find new, thermodynamically stable photovoltaic absorbers with band gaps near 1.4 eV. A hit had to meet three conditions: band gap of 1.1–1.7 eV, energy above the convex hull (E_hull) of 0.05 eV/atom or less, and absence from Materials Project.

The campaign ran 5 iterations and scored 100 candidates. Structures were relaxed with CHGNet and band gaps came from a surrogate model trained to approximate HSE values. All 100 candidates converged, and 99 were novel; one known compound was run on purpose as a calibration point. **19 novel candidates met the hit criteria on paper.** Their confidence varies a lot:

- **Highest confidence:** Ag-based kesterites with d10 or Mg ions on the II site, all from iteration 1. Examples are CdAg2GeSe4 (1.28 eV, on the hull) and MgAg2GeTe4 (1.49 eV, 0.025 eV/atom).
- **Medium confidence:** Cu/Ag famatinite-type selenides from iteration 4, such as CuAg2AsSe4 (1.38 eV) and CuAg2SbSe4 (1.46 eV), and the Ni–Ag kesterites from iteration 2.
- **Low confidence:** the Sb5+ alkali tellurides from iteration 5 and the Ti-sulfide kesterite Ag2ZnTiS4 from iteration 3. Both groups show signs of hull artifacts.

Nothing here has been checked with DFT or synthesis. One calibration point suggests the surrogate overestimates band gaps by roughly 0.4 eV for one family.

## Campaign statistics

| Iteration | Proposed | Filtered out | Scored |
|---|---|---|---|
| 1 | 68 | — | 20 |
| 2 | 28 | — | 20 |
| 3 | 90 | 9 | 20 |
| 4 | 32 | 8 | 20 |
| 5 | 24 | 6 | 20 |

All 100 scored candidates converged.

## Scored candidates

Columns: E_f is formation energy (eV/atom), E_hull is energy above the hull (eV/atom), and Gap is the surrogate HSE-level band gap (eV). Formulas appear as the database stores them; for example, ZnAg2GeSe4 is Ag2ZnGeSe4 and TiZn(AgS2)2 is Ag2ZnTiS4. **Bold** marks a nominal hit (gap 1.1–1.7 eV, E_hull ≤ 0.05, novel).

### Iteration 1: I2-II-IV-VI4 kesterites

| Formula | E_f | E_hull | Gap | Novel |
|---|---|---|---|---|
| **ZnAg2GeSe4** | -0.68 | 0.000 | 1.12 | yes |
| **CdAg2GeSe4** | -0.66 | 0.000 | 1.28 | yes |
| **MgAg2SnSe4** | -0.84 | 0.016 | 1.59 | yes |
| CdAg2GeTe4 | -0.33 | 0.017 | 0.48 | yes |
| MgCu2SnS4 | -1.24 | 0.020 | 2.17 | yes |
| MgAg2GeSe4 | -0.80 | 0.020 | 1.86 | yes |
| **MgAg2GeTe4** | -0.42 | 0.025 | 1.49 | yes |
| CdAg2SnTe4 | -0.37 | 0.027 | 0.41 | yes |
| **ZnAg2GeTe4** | -0.32 | 0.028 | 1.17 | yes |
| **MgAg2SnTe4** | -0.46 | 0.038 | 1.17 | yes |
| ZnAg2SnTe4 | -0.36 | 0.039 | 0.60 | yes |
| MgCu2SnSe4 | -0.82 | 0.071 | 1.38 | yes |
| MnAg2GeS4 | -0.91 | 0.079 | 2.24 | yes |
| MgSi(AgTe2)2 | -0.33 | 0.087 | 1.80 | yes |
| ZnSi(AgTe2)2 | -0.22 | 0.095 | 2.04 | yes |
| MgCu2GeTe4 | -0.37 | 0.101 | 0.90 | yes |
| MnCu2GeSe4 | -0.53 | 0.104 | 0.93 | yes |
| MgCu2GeSe4 | -0.72 | 0.136 | 1.10 | yes |
| ZnSi(AgSe2)2 | -0.55 | 0.170 | 1.90 | yes |
| MgCu2SiTe4 | -0.27 | 0.173 | 0.87 | yes |

### Iteration 2: kesterites with 3d transition metals on the II site

| Formula | E_f | E_hull | Gap | Novel |
|---|---|---|---|---|
| NiAg2SnS4 | -0.94 | 0.000 | 1.90 | yes |
| **NiAg2SnSe4** | -0.63 | 0.000 | 1.68 | yes |
| **NiAg2GeSe4** | -0.58 | 0.0005 | 1.65 | yes |
| NiAg2GeS4 | -0.91 | 0.008 | 1.74 | yes |
| **Cu2NiGeS4** | -0.98 | 0.013 | 1.12 | yes |
| NiAg2GeTe4 | -0.28 | 0.036 | 0.13 | yes |
| Cu2NiGeSe4 | -0.58 | 0.041 | 0.25 | yes |
| NiAg2SnTe4 | -0.32 | 0.045 | 0.04 | yes |
| CoAg2SnSe4 | -0.57 | 0.056 | 0.60 | yes |
| FeAg2SnSe4 | -0.58 | 0.072 | ~0 (-0.003) | yes |
| Cu2NiGeTe4 | -0.25 | 0.074 | 0.09 | yes |
| CoAg2GeSe4 | -0.52 | 0.075 | 0.81 | yes |
| FeAg2GeSe4 | -0.53 | 0.078 | 0.02 | yes |
| CoAg2GeTe4 | -0.23 | 0.087 | 0.00 | yes |
| CoAg2SnS4 | -0.86 | 0.092 | 1.39 | yes |
| FeAg2GeTe4 | -0.20 | 0.112 | 0.01 | yes |
| CoAg2GeS4 | -0.83 | 0.113 | 1.51 | yes |
| FeAg2GeS4 | -0.85 | 0.135 | 0.01 | yes |
| CoCu2GeTe4 | -0.18 | 0.152 | 0.01 | yes |
| FeCu2GeTe4 | -0.16 | 0.157 | 0.01 | yes |

### Iteration 3: II-IV-V2 chalcopyrites, Si/Ti-site kesterites

| Formula | E_f | E_hull | Gap | Novel |
|---|---|---|---|---|
| TiZn(CuS2)2 | -1.57 | 0.000 | 2.66 | yes |
| TiCd(CuS2)2 | -1.51 | 0.000 | 2.86 | yes |
| **TiZn(AgS2)2** (low confidence) | -1.55 | 0.000 | 1.55 | yes |
| TiMn(CuS2)2 | -1.57 | 0.000 | 2.26 | yes |
| MgTi(CuS2)2 | -1.70 | 0.000 | 2.93 | yes |
| MgSnSb2 | -0.11 | 0.123 | 0.01 | yes |
| CdSi(AgSe2)2 | -0.57 | 0.130 | 1.71 | yes |
| SiNi(AgSe2)2 | -0.50 | 0.134 | 1.08 | yes |
| CdSi(AgS2)2 | -0.94 | 0.152 | 2.75 | yes |
| SiNi(AgS2)2 | -0.87 | 0.162 | 0.70 | yes |
| Cu2SiNiSe4 | -0.48 | 0.167 | 0.19 | yes |
| CdGeSb2 | +0.08 | 0.172 | 0.31 | yes |
| MgGeSb2 | -0.05 | 0.177 | 0.01 | yes |
| ZnGeSb2 | +0.11 | 0.199 | 0.23 | yes |
| CdSiSb2 | +0.17 | 0.251 | 0.55 | yes |
| ZnSiSb2 | +0.21 | 0.281 | 1.20 | yes |
| TiCd(AgS2)2 | -0.96 | 0.351 | 2.40 | yes |
| MgTi(AgS2)2 | -1.14 | 0.364 | 1.95 | yes |
| TiZn(CuSe2)2 | -0.57 | 0.412 | 2.84 | yes |
| TiNi(AgS2)2 | -0.82 | 0.441 | 0.07 | yes |

### Iteration 4: I3-V-VI4 famatinite/enargite-type compounds in the kesterite prototype

| Formula | E_f | E_hull | Gap | Novel |
|---|---|---|---|---|
| Cu2AgSbS4 | -0.86 | 0.000 | 1.74 | yes |
| Cu2AgSbSe4 | -0.52 | 0.000 | 0.43 | yes |
| Cu2AgAsS4 | -0.82 | 0.000 | 1.87 | yes |
| Cu2AgAsSe4 | -0.48 | 0.000 | 0.44 | yes |
| CuAg2SbS4 | -0.86 | 0.000 | 1.86 | yes |
| **CuAg2SbSe4** | -0.57 | 0.000 | 1.46 | yes |
| CuAg2SbTe4 | -0.28 | 0.000 | 0.31 | yes |
| CuAg2AsS4 | -0.83 | 0.000 | 1.97 | yes |
| **CuAg2AsSe4** | -0.53 | 0.000 | 1.38 | yes |
| CuAg2PSe4 | -0.48 | 0.000 | 2.15 | yes |
| Ag3SbS4 | -0.86 | 0.000 | 1.79 | yes |
| **Ag3SbSe4** | -0.57 | 0.000 | 1.67 | yes |
| **Ag3AsSe4** | -0.54 | 0.000 | 1.68 | yes |
| **NaCu2SbSe4** | -0.77 | 0.000 | 1.55 | yes |
| NaCu2AsSe4 | -0.74 | 0.000 | 1.05 | yes |
| NaAg2SbSe4 | -0.78 | 0.000 | 1.90 | yes |
| NaAg2AsSe4 | -0.75 | 0.000 | 1.92 | yes |
| CuAg2PS4 | -0.83 | 0.020 | 2.45 | yes |
| Cu2AgPSe4 | -0.42 | 0.045 | 2.14 | yes |
| Cu3AsS4 (calibration) | -0.75 | 0.084 | 1.78 | **no (known)** |

### Iteration 5: alkali-substituted I3-V-VI4

| Formula | E_f | E_hull | Gap | Novel |
|---|---|---|---|---|
| NaCu2SbS4 | -1.14 | 0.000 | 2.32 | yes |
| NaCu2AsS4 | -1.10 | 0.000 | 2.47 | yes |
| KCu2SbS4 | -1.19 | 0.000 | 2.20 | yes |
| **KCu2SbSe4** | -0.81 | 0.000 | 1.52 | yes |
| KCu2AsS4 | -1.13 | 0.000 | 2.52 | yes |
| KCu2AsSe4 | -0.77 | 0.000 | 1.83 | yes |
| NaAg2SbS4 | -1.07 | 0.000 | 2.21 | yes |
| NaAg2SbTe4 | -0.45 | 0.000 | 1.08 | yes |
| NaAg2AsS4 | -1.04 | 0.000 | 2.17 | yes |
| KAg2SbSe4 | -0.82 | 0.000 | 1.91 | yes |
| KAg2SbTe4 | -0.50 | 0.000 | 0.49 | yes |
| KAg2AsS4 | -1.10 | 0.000 | 2.18 | yes |
| KAg2AsSe4 | -0.80 | 0.000 | 2.01 | yes |
| **Na2CuSbTe4** (low confidence) | -0.65 | 0.000 | 1.28 | yes |
| **Na2AgSbTe4** (low confidence) | -0.64 | 0.000 | 1.37 | yes |
| **K2CuSbTe4** (low confidence) | -0.74 | 0.000 | 1.30 | yes |
| K2AgSbTe4 | -0.84 | 0.000 | 0.99 | yes |
| Na2CuSbSe4 | -1.00 | 0.000 | 2.05 | yes |
| NaCu2SbTe4 | -0.43 | 0.0005 | 0.71 | yes |
| KCu2SbTe4 | -0.47 | 0.006 | 0.48 | yes |

## Hypotheses tested and what was learned

### Iteration 1: Ag/Cu kesterites (I2-II-IV-VI4)

**Hypothesis:** Substituting on the I, II, IV and anion sites in the kesterite structure would tune the gap around the known CZTS/CZTSe range. Swaps with opposing effects (Ge+Se, Ag+Se, Mg+Te) should land near 1.4 eV.

**Result:** The hypothesis largely held for Ag kesterites. Six hits:

- On the hull: CdAg2GeSe4 (1.28 eV) and ZnAg2GeSe4 (1.12 eV).
- Near the hull: MgAg2SnSe4 (1.59 eV), MgAg2GeTe4 (1.49 eV), ZnAg2GeTe4 (1.17 eV) and MgAg2SnTe4 (1.17 eV).

**What failed:**
- Cu–Mg kesterites were not stable enough (0.07–0.17 eV/atom). MgCu2SnSe4 had a good gap (1.38 eV) but sat 0.071 eV/atom above the hull.
- Si on the IV site made the compounds unstable and pushed gaps too wide.
- Ag–Sn–Te and Ag–Cd–Te gaps were too small (0.4–0.6 eV).

**Trends:**
- Mg on the II site raises the gap by about 0.3–0.6 eV compared with Zn or Cd.
- Ag kesterites were much more stable than Cu–Mg ones.

### Iteration 2: 3d transition metals (Mn, Fe, Co, Ni) on the II site of Ag/Cu kesterites

**Hypothesis:** Mn- and Fe-based members would land at 1.1–1.6 eV, while Co and Ni members might be metallic or unstable.

**Result:** The prediction was mostly wrong, but not in a useful-only-as-failure way:

- Every Fe compound had a gap near zero and was 0.07–0.16 eV/atom above the hull.
- Co compounds were unstable or had gaps that were too small.
- All Te compounds with open-shell 3d metals were metallic or nearly so.
- Unexpectedly, the Ni–Ag kesterites sat on the hull. NiAg2SnSe4 (1.68 eV) and NiAg2GeSe4 (1.65 eV) are at the top edge of the window, and Cu2NiGeS4 (1.12 eV, 0.013 eV/atom) also qualified.
- Within the Ni–Ag kesterites the gap drops sharply from about 1.65 eV for Se to about 0.1 eV for Te. Swapping the whole anion therefore cannot reach 1.4 eV.

The Ni results are provisional. Ni2+ has a weak preference for tetrahedral sites, and magnetic ordering was not treated.

### Iteration 3: II-IV-V2 chalcopyrites, plus Si- and Ti-site kesterites

**Hypothesis:** II-IV-V2 chalcopyrites with Mg or Sb would be novel and land near 1.4 eV.

**Result:** This family had essentially no usable space:

- All P members were rejected by the SMACT filter, and all As members already exist in Materials Project.
- The novel Sb members were all unstable (0.12–0.28 eV/atom), and the Zn and Cd ones had positive formation energies.
- Si on the IV site again made kesterites unstable (0.13–0.17 eV/atom).

A side branch tested Ti4+ on the IV site. Several Ti sulfides came out on the hull, including Ag2ZnTiS4 (1.55 eV). However, the results do not make physical sense:

- Their formation energies (about -1.5 to -1.7 eV/atom) are 0.6–1.0 eV/atom more negative than comparable compounds.
- The Se analogue had a *larger* gap than the sulfide (2.84 vs 2.66 eV) and sat 0.41 eV/atom above the hull.

These results are flagged as a likely CHGNet or hull artifact, so Ag2ZnTiS4 is low confidence.

### Iteration 4: I3-V-VI4 famatinite/enargite-type compounds with Ag/Na substitution

**Hypothesis:** Replacing Cu with Ag in Cu3SbS4, Cu3AsSe4 and related compounds would raise their gaps toward 1.4 eV. The notebook records that the Ag–Cu–Sb–S chemical system had no entries in Materials Project.

**Result:** The hypothesis held for selenides. Five hits, all on the hull:

- CuAg2AsSe4: 1.38 eV, the closest to the target in the campaign.
- CuAg2SbSe4: 1.46 eV.
- NaCu2SbSe4: 1.55 eV.
- Ag3SbSe4: 1.67 eV.
- Ag3AsSe4: 1.68 eV.

**Other findings:**
- The prediction for sulfides was wrong: they came out at 1.7–2.0 eV.
- Tellurides had gaps that were too small, and P members had gaps that were too large.
- In selenides the gap does not change smoothly with the Cu:Ag ratio: 0.43 eV for Cu2Ag, 1.4–1.5 eV for CuAg2 and about 1.67 eV for Ag3.

**Calibration:** Known enargite Cu3AsS4 was evaluated in the kesterite structure. It gave 1.78 eV and 0.084 eV/atom above the hull, against the experimental gap of about 1.4 eV recorded in the notebook. This suggests the surrogate overestimates gaps in this family. It also shows that the kesterite polymorph is not the ground state; real enargite has a wurtzite-derived structure.

### Iteration 5: alkali (Na, K) on the I sites of I3-V-VI4

**Hypothesis:** More alkali would widen the gap, which would pull the tellurides up into the window.

**Result:** The trend appeared as predicted:
- NaCu2SbTe4 went from 0.71 eV to 1.28 eV for Na2CuSbTe4.
- NaAg2SbTe4 went from 1.08 eV to 1.37 eV for Na2AgSbTe4.

There were four nominal hits: Na2AgSbTe4 (1.37 eV), K2CuSbTe4 (1.30 eV), Na2CuSbTe4 (1.28 eV) and KCu2SbSe4 (1.52 eV). Sulfides came out at 2.2–2.5 eV, too wide.

**Red flag:** We predicted that K would destabilize these compounds, but every composition landed at E_hull ≤ 0.006 eV/atom. This most likely means the hull is missing competing phases, not that the compounds are stable. Sb5+ alongside Te2- is also chemically implausible; known compounds in this space contain Sb3+.

## Caveats

1. **Band gaps are surrogate estimates, not HSE calculations.** The only calibration point (Cu3AsS4: 1.78 eV vs about 1.4 eV experimental) suggests overestimation of roughly 0.4 eV in at least one family, and the actual error elsewhere is unknown. Only one calibration point was run in the whole campaign, so no error bar can be drawn.
2. **Hull completeness.** Nearly every I3-V-VI4 compound in iterations 4 and 5 landed at exactly 0.000 eV/atom above the hull. This partly reflects how few known phases Materials Project has in these chemical systems. Likely missing competitors include Sb3+ phases such as ASbX2, Cu3SbX3, AgSbX2 and Ag3SbS3.
3. **Fixed prototype structures.** All candidates were relaxed only in the kesterite or chalcopyrite structure, with no search over alternative structures. Real I3-V-VI4 compounds and alkali-containing compounds often adopt other structures; enargite, for example, is wurtzite-derived.
4. **Open-shell 3d metals.** The Ni and Co results ignore spin polarization and magnetic ordering, and the surrogate's accuracy for open-shell systems is uncertain.
5. **Suspected artifacts.** The Ti-sulfide kesterites show the physically inconsistent trends described in iteration 3.
6. **No validation at all.** Nothing has been checked with DFT or synthesis.

## Ranked shortlist by confidence

| Confidence | Candidates (gap eV / E_hull eV/atom) |
|---|---|
| Highest | CdAg2GeSe4 (1.28 / 0), MgAg2GeTe4 (1.49 / 0.025), MgAg2SnSe4 (1.59 / 0.016), ZnAg2GeSe4 (1.12 / 0) |
| Medium | CuAg2AsSe4 (1.38 / 0), CuAg2SbSe4 (1.46 / 0), NaCu2SbSe4 (1.55 / 0), Ag3SbSe4 (1.67 / 0), Ag3AsSe4 (1.68 / 0), NiAg2SnSe4 (1.68 / 0), NiAg2GeSe4 (1.65 / 0.0005), Cu2NiGeS4 (1.12 / 0.013) |
| Low | Na2AgSbTe4 (1.37 / 0), K2CuSbTe4 (1.30 / 0), Na2CuSbTe4 (1.28 / 0), KCu2SbSe4 (1.52 / 0), TiZn(AgS2)2 (1.55 / 0) |

ZnAg2GeTe4 (1.17 / 0.028) and MgAg2SnTe4 (1.17 / 0.038) also meet the hit criteria but sit near the low edge of the gap window.

## Recommended next steps

1. **Recompute the hulls with DFT (HSE or SCAN)** for all shortlisted candidates. Add the missing Sb3+ competitors (ASbX2, Cu3SbX3, AgSbX2, Ag3SbS3) and alternative structures (stannite, wurtzite-kesterite, enargite-type) before trusting any E_hull = 0 result.
2. **Run explicit HSE gap calculations** on the highest- and medium-confidence candidates. Add more known calibration compounds; the notebook proposed Cu3SbSe4, with an experimental gap of about 0.3 eV. This would put an error bar on the surrogate for each family.
3. **Test the Ni kesterites with spin-polarized DFT+U or HSE** to check that the gaps and hull positions survive once magnetism is treated.
4. **Check the Ti artifact directly**, comparing CHGNet against DFT formation energies for one or two Ti-sulfide kesterites. Do not pursue that branch until this is done.
5. **Consider synthesis only after steps 1–2**, starting with the d10 Ag kesterites (CdAg2GeSe4, MgAg2GeTe4). They use conventional oxidation states (Ge4+/Sn4+, tetrahedral d10 ions) and are the chemically most plausible candidates from this campaign.
