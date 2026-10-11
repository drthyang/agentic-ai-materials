# Campaign report: pv-absorber-v1

## Executive summary

Over five iterations the campaign scored 98 candidates with CHGNet relaxation, formation energy, energy above hull (Ehull) and a surrogate "HSE-fidelity" band gap. Of these, 95 were novel with respect to Materials Project and 3 were deliberate calibration points. A candidate counted as a hit if it was novel, had a gap of 1.1–1.7 eV and had Ehull ≤ 0.05 eV/atom. Twelve candidates count as credible hits, plus one flagged as suspect:

- **Six Ag-based kesterites (I2-II-IV-VI4), iteration 1.**
- **Four Ag-rich famatinite-type I3-V-VI4 selenides, iteration 2.**
- **NaCu2SbSe4 and KCu2SbSe4, iteration 5.** KCu2SbSe4 has low confidence.
- **TiZn(AgS2)2, iteration 4.** Flagged as a likely evaluation artifact, not a discovery.

Two hypothesis families failed clearly on stability: ordered III2-II-IV-V4 arsenides and Mg-rich II2-I-III-VI4 phases. Confidence in every hit is limited. All numbers come from surrogate models. Several "Ehull = 0" results probably reflect a sparse convex hull rather than real stability. Polymorph competition (famatinite vs enargite) and Sb³⁺ competitor phases were never checked. None of these candidates has been validated by DFT or synthesis.

## Scored candidates

Units: Ef = formation energy (eV/atom); Ehull = energy above hull (eV/atom); Gap in eV. "Novel" means absent from Materials Project. It does not mean absent from the literature.

### Iteration 1: I2-II-IV-VI4 kesterite substitutions

| Formula | Novel | Ef | Ehull | Gap | Assessment |
|---|---|---|---|---|---|
| ZnAg2GeSe4 | yes | -0.68 | 0.000 | 1.12 | **Hit** |
| CdAg2GeSe4 | yes | -0.66 | 0.000 | 1.28 | **Hit** |
| MgAg2SnS4 | yes | -1.18 | 0.002 | 1.87 | Gap too wide |
| CdCu2SnS4 | no (calibration) | -1.05 | 0.011 | 1.69 | Calibration |
| MgAg2SnSe4 | yes | -0.84 | 0.016 | 1.59 | **Hit** |
| CdAg2GeTe4 | yes | -0.33 | 0.017 | 0.48 | Gap too small |
| MgAg2GeS4 | yes | -1.17 | 0.017 | 1.89 | Gap too wide |
| MgCu2SnS4 | yes | -1.24 | 0.020 | 2.17 | Gap too wide |
| MgAg2GeSe4 | yes | -0.80 | 0.020 | 1.86 | Gap too wide |
| MgAg2GeTe4 | yes | -0.42 | 0.025 | 1.49 | **Hit** |
| CdAg2SnTe4 | yes | -0.37 | 0.027 | 0.41 | Gap too small |
| ZnAg2GeTe4 | yes | -0.32 | 0.028 | 1.17 | **Hit** |
| MgAg2SnTe4 | yes | -0.46 | 0.038 | 1.17 | **Hit** |
| MgCu2SnSe4 | yes | -0.82 | 0.071 | 1.38 | Unstable |
| MnAg2GeS4 | yes | -0.91 | 0.079 | 2.24 | Unstable, gap too wide |
| MnCu2GeSe4 | yes | -0.53 | 0.104 | 0.93 | Unstable |
| CdSi(AgSe2)2 | yes | -0.57 | 0.130 | 1.71 | Unstable |
| MgCu2GeSe4 | yes | -0.72 | 0.136 | 1.10 | Unstable |
| MgSi(AgSe2)2 | yes | -0.71 | 0.145 | 2.35 | Unstable |
| ZnSi(AgSe2)2 | yes | -0.55 | 0.170 | 1.90 | Unstable |

### Iteration 2: I3-V-VI4 (famatinite-type, kesterite prototype)

| Formula | Novel | Ef | Ehull | Gap | Assessment |
|---|---|---|---|---|---|
| CuAg2AsSe4 | yes | -0.53 | 0.000 | 1.38 | **Hit** |
| CuAg2SbSe4 | yes | -0.57 | 0.000 | 1.46 | **Hit** |
| Ag3SbSe4 | yes | -0.57 | 0.000 | 1.67 | **Hit** |
| Ag3AsSe4 | yes | -0.54 | 0.000 | 1.68 | **Hit** |
| Cu2AgSbS4 | yes | -0.86 | 0.000 | 1.74 | Gap too wide |
| Ag3SbS4 | yes | -0.86 | 0.000 | 1.79 | Gap too wide |
| CuAg2SbS4 | yes | -0.86 | 0.000 | 1.86 | Gap too wide |
| Cu2AgAsS4 | yes | -0.82 | 0.000 | 1.87 | Gap too wide |
| CuAg2AsS4 | yes | -0.83 | 0.000 | 1.97 | Gap too wide |
| Cu2AgAsSe4 | yes | -0.48 | 0.000 | 0.44 | Gap too small |
| Cu2AgSbSe4 | yes | -0.52 | 0.000 | 0.43 | Gap too small |
| CuAg2SbTe4 | yes | -0.28 | 0.000 | 0.31 | Gap too small |
| CuAg2PSe4 | yes | -0.48 | 0.000 | 2.15 | Gap too wide |
| Cu3SbTe4 | yes | -0.25 | 0.001 | 0.32 | Gap too small |
| CuAg2PS4 | yes | -0.83 | 0.020 | 2.45 | Gap too wide |
| Cu2AgPSe4 | yes | -0.42 | 0.045 | 2.14 | Gap too wide |
| Cu2AgSbTe4 | yes | -0.21 | 0.045 | 0.38 | Gap too small |
| Cu3PSe4 | no (calibration) | -0.33 | 0.155 | 1.11 | Calibration (kesterite-derived polymorph) |

### Iteration 3: III2-II-IV-V4 arsenides and Mg2-Ag-III-VI4

| Formula | Novel | Ef | Ehull | Gap | Assessment |
|---|---|---|---|---|---|
| Mg2GaAgTe4 | yes | -0.58 | 0.172 | 1.69 | Unstable |
| CdIn2SiAs4 | yes | +0.06 | 0.289 | 0.38 | Unstable |
| Mg2AlAgTe4 | yes | -0.50 | 0.290 | 2.17 | Unstable |
| ZnGa2SnAs4 | yes | -0.04 | 0.298 | 0.37 | Unstable |
| ZnGa2GeAs4 | yes | -0.02 | 0.303 | 0.58 | Unstable |
| MgGa2SnAs4 | yes | -0.09 | 0.312 | 0.62 | Unstable |
| MgIn2SiAs4 | yes | -0.00 | 0.326 | 0.60 | Unstable |
| Al2ZnSnAs4 | yes | -0.08 | 0.337 | 0.71 | Unstable |
| CdGa2GeAs4 | yes | +0.05 | 0.337 | 0.59 | Unstable |
| MgAl2SnAs4 | yes | -0.13 | 0.343 | 1.27 | Unstable (gap in window) |
| Al2ZnGeAs4 | yes | -0.04 | 0.360 | 1.02 | Unstable |
| MgGa2GeAs4 | yes | -0.03 | 0.360 | 0.72 | Unstable |
| ZnIn2SiAs4 | yes | +0.10 | 0.371 | 0.42 | Unstable |
| Mg2AlAgSe4 | yes | -0.91 | 0.372 | 2.59 | Unstable |
| ZnGa2SiAs4 | yes | +0.04 | 0.373 | 0.74 | Unstable |
| Al2CdSnAs4 | yes | -0.01 | 0.375 | 1.25 | Unstable (gap in window) |
| MgGa2SiAs4 | yes | -0.01 | 0.380 | 1.14 | Unstable (gap in window) |
| Al2CdGeAs4 | yes | +0.04 | 0.400 | 1.42 | Unstable (gap in window) |
| CdGa2SiAs4 | yes | +0.11 | 0.405 | 1.05 | Unstable |
| Al2CdSiAs4 | yes | +0.09 | 0.457 | 1.34 | Unstable (gap in window) |

### Iteration 4: Ti/Zr on the kesterite IV site

| Formula | Novel | Ef | Ehull | Gap | Assessment |
|---|---|---|---|---|---|
| TiZn(AgS2)2 | yes | -1.55 | 0.000 | 1.55 | **Suspect**: Ef implausibly deep |
| TiZn(CuS2)2 | yes | -1.57 | 0.000 | 2.66 | Suspect Ef; gap too wide |
| TiCd(CuS2)2 | yes | -1.51 | 0.000 | 2.85 | Suspect Ef; gap too wide |
| MgTi(CuS2)2 | yes | -1.70 | 0.000 | 2.93 | Suspect Ef; gap too wide |
| ZrZn(CuS2)2 | yes | -1.56 | 0.000 | 0.30 | Suspect Ef; gap too small |
| ZrZn(AgS2)2 | yes | -1.54 | 0.000 | 0.19 | Suspect Ef; gap too small |
| ZrZn(CuSe2)2 | yes | -1.19 | 0.000 | 0.21 | Suspect Ef; gap too small |
| ZrZn(AgSe2)2 | yes | -1.18 | 0.000 | 0.65 | Suspect Ef; gap too small |
| ZrCd(AgSe2)2 | yes | -1.15 | 0.000 | 0.30 | Suspect Ef; gap too small |
| ZrZn(AgTe2)2 | yes | -0.78 | 0.000 | 0.07 | Gap too small |
| ZrZn(CuTe2)2 | yes | -0.67 | 0.000 | 0.23 | Gap too small |
| TiCd(AgS2)2 | yes | -0.96 | 0.351 | 2.40 | Unstable |
| TiZn(AgSe2)2 | yes | -0.62 | 0.353 | 2.23 | Unstable |
| TiCd(AgSe2)2 | yes | -0.59 | 0.357 | 2.35 | Unstable |
| MgTi(AgS2)2 | yes | -1.14 | 0.364 | 1.95 | Unstable |
| MgTi(AgSe2)2 | yes | -0.73 | 0.380 | 2.43 | Unstable |
| TiZn(CuSe2)2 | yes | -0.57 | 0.412 | 2.84 | Unstable |
| ZrCd(AgS2)2 | yes | -0.95 | 0.451 | 2.36 | Unstable |
| MgZr(AgSe2)2 | yes | -0.72 | 0.459 | 1.58 | Unstable |
| TiCd(CuSe2)2 | yes | -0.49 | 0.479 | 2.80 | Unstable |

### Iteration 5: Na/K-substituted I3-V-VI4

| Formula | Novel | Ef | Ehull | Gap | Assessment |
|---|---|---|---|---|---|
| NaCu2SbSe4 | yes | -0.77 | 0.000 | 1.55 | **Hit** (moderate confidence) |
| KCu2SbSe4 | yes | -0.81 | 0.000 | 1.52 | **Hit** (low confidence: K size mismatch) |
| NaAg2SbTe4 | yes | -0.45 | 0.000 | 1.08 | Just below window |
| NaCu2AsSe4 | yes | -0.74 | 0.000 | 1.05 | Just below window |
| NaAg2SbSe4 | yes | -0.78 | 0.000 | 1.90 | Gap too wide |
| NaAg2AsSe4 | yes | -0.75 | 0.000 | 1.92 | Gap too wide |
| NaCu2SbS4 | yes | -1.14 | 0.000 | 2.32 | Gap too wide |
| NaCu2AsS4 | yes | -1.10 | 0.000 | 2.47 | Gap too wide |
| NaAg2SbS4 | yes | -1.07 | 0.000 | 2.21 | Gap too wide |
| NaAg2AsS4 | yes | -1.04 | 0.000 | 2.17 | Gap too wide |
| KAg2SbTe4 | yes | -0.50 | 0.000 | 0.49 | Gap too small |
| KAg2SbSe4 | yes | -0.82 | 0.000 | 1.91 | Gap too wide |
| KCu2AsSe4 | yes | -0.77 | 0.000 | 1.83 | Gap too wide |
| KAg2AsSe4 | yes | -0.80 | 0.000 | 2.01 | Gap too wide |
| KCu2SbS4 | yes | -1.19 | 0.000 | 2.20 | Gap too wide |
| KCu2AsS4 | yes | -1.13 | 0.000 | 2.52 | Gap too wide |
| KAg2AsS4 | yes | -1.10 | 0.000 | 2.18 | Gap too wide |
| Na3SbSe4 | no (calibration) | -1.14 | 0.000 | 1.42 | Calibration |
| NaCu2SbTe4 | yes | -0.43 | 0.0005 | 0.71 | Gap too small |
| KCu2SbTe4 | yes | -0.47 | 0.006 | 0.48 | Gap too small |

Campaign statistics, proposed → scored: iteration 1, 58 → 20; iteration 2, 135 → 18 (40 filtered out); iteration 3, 28 → 20 (25 filtered out); iteration 4, 36 → 20; iteration 5, 22 → 20 (4 filtered out).

## Hypotheses tested and lessons learned

**Iteration 1: Ag-based I2-II-IV-VI4 kesterites (largely supported).**
- The hypothesis was multi-site substitution: Cu→Ag, Zn→Mg/Cd/Mn, Sn→Ge/Si, and S/Se/Te on the anion site.
- Six novel in-window hits came out at Ehull 0.000–0.038.
- Ag on the I-site stabilised Mg members: MgAg2X came in at 0.002–0.038, against 0.071 for MgCu2SnSe4.
- Every Si member was unstable (Ehull 0.13–0.17). Mn members were unstable (0.079–0.104).
- Te shifted gaps unevenly. Mg–Te members stayed at 1.17–1.49 eV, but the Cd–Te members dropped to 0.41–0.48 eV. That anomaly was noted and never resolved.

**Iteration 2: I3-V-VI4 with mixed Cu/Ag (supported for Ag-rich selenides).**
- Four novel in-window hits, all at Ehull 0.000: CuAg2AsSe4, CuAg2SbSe4, Ag3SbSe4 and Ag3AsSe4.
- Sulfides were too wide (1.74–1.97 eV). Cu-rich selenides and the tellurides were too narrow (0.31–0.44 eV).
- The prediction that P would reopen the Cu-rich members into the window was wrong. Every P member landed at 2.14–2.45 eV.
- One Cu↔Ag swap moved the gap by about 1 eV (Cu2AgSbSe4 0.43 → CuAg2SbSe4 1.46). The notebook flags a jump this size as suspicious.
- Process lesson: three families were proposed together and evaluated as one batch. The critic vetoed 13 candidates from the two ordered-alloy families as not testing the stated hypothesis. Those formulas, and more of the combinatorial set, were then locked out as already considered.

**Iteration 3: III2-II-IV-V4 ordered arsenides and Mg2-Ag-III-VI4 (falsified).**
- All 17 arsenide members came out at Ehull 0.29–0.46. Their formation energies were near zero or positive (−0.13 to +0.11).
- Gaps fell well below the parent-interpolation estimates. For example, ZnGa2GeAs4 came out at 0.58 eV against a predicted ~1.3 eV.
- The three Mg2 members gave gaps in line with interpolation (1.69–2.59 eV) but were unstable (Ehull 0.17–0.37).
- Conclusions: cross-family cation ordering on a shared anion is strongly penalised in this setup, and two tetrahedral Mg per formula unit is not tolerated. Phosphides failed the SMACT filter, as they had in iteration 2.

**Iteration 4: d0 Ti/Zr on the kesterite IV site (failed; artifact suspected).**
- The results split into two groups.
  - Eleven members sat at Ehull 0.000. Their formation energies were −0.67 to −1.70 eV/atom, and the sulfide/selenide ones (−1.15 to −1.70) are implausibly deep.
  - The rest sat at Ehull 0.35–0.48 with shallower formation energies.
- The split does not follow composition: TiZn(AgS2)2 is "on hull" while TiCd(AgS2)2 is at 0.35. The notebook therefore treats the Ehull = 0 group as a likely CHGNet or energy-correction artifact for early-transition-metal chalcogenides.
- TiZn(AgS2)2 (1.55 eV) is logged as suspect, not as a hit.
- The physically plausible group says tetrahedral d0 kesterites are strongly unstable.

**Iteration 5: Na/K on the I3-V-VI4 cation sites (gap trend confirmed; stability not properly tested).**
- Na raised gaps by roughly +0.4 to +1.1 eV compared with the iteration-2 parents at the same Cu/Ag count:
  - Cu2AgSbSe4 0.43 → NaCu2SbSe4 1.55
  - CuAg2SbTe4 0.31 → NaAg2SbTe4 1.08
  - Cu3SbTe4 0.32 → NaCu2SbTe4 0.71
- Every member came out at Ehull ≤ 0.006. That includes the K members, even though K is too large for tetrahedral sites. This most likely reflects a sparse hull (few Na/K–Cu/Ag–Sb/As–Se reference phases) rather than real stability.
- Sulfide formation energies (−1.04 to −1.19 eV/atom) look deep, which is the same kind of warning sign seen in iteration 4.

## Caveats

- **Surrogate band gaps.** The gaps come from a surrogate model, and the only error estimates are the calibration points:
  - CdCu2SnS4: model 1.69 eV against ~1.4 eV experimental (value as recorded in the notebook). This suggests the model overestimates Cu-kesterite gaps by ~0.3 eV.
  - Na3SbSe4: model 1.42 eV. The experimental gap was recalled as ~1.8–2 eV but was **not verified**. If that holds, the model underestimates alkali-rich members, which would push NaCu2SbSe4 toward or above the top of the window and NaAg2SbTe4 into it.
  - Hits near the window edges are therefore uncertain: ZnAg2GeSe4 (1.12), Ag3SbSe4 (1.67), Ag3AsSe4 (1.68), and the two members just below the window (1.05–1.08).
- **Stability from CHGNet against the Materials Project hull.**
  - Ehull = 0 can be an artifact of missing competitor phases. This is especially likely for the iteration-5 alkali members and the Ag famatinites, where Sb³⁺ competitors (AgSbSe2, Ag3SbSe3, NaSbSe2, Na3SbSe3, Cu3SbSe3, CuSbSe2) may be missing or under-weighted.
  - Sb⁵⁺/As⁵⁺ with Ag is chemically questionable.
- **Polymorph not explored.** Every candidate was relaxed in the kesterite-derived prototype. The Cu3PSe4 calibration (Ehull 0.155 in this polymorph, while its real ground state is enargite) shows that the polymorph choice matters. Famatinite vs enargite competition was never tested.
- **Artifact detection was manual.** The iteration-4 Ti/Zr results show the pipeline can report deep formation energies and Ehull = 0 for unphysical cases. No automated check was applied to the other iterations.
- **Novelty means absent from Materials Project only.** No literature check was run on each hit.
- **No independent validation.** None of the candidates has been checked by DFT, phonon calculations or synthesis.

## Recommended next steps

1. **DFT (PBE + HSE) relaxations and hull checks** for the 12 credible hits, prioritised by confidence:
   - ZnAg2GeSe4, CdAg2GeSe4 and MgAg2SnSe4 (on or near the hull in a well-studied family)
   - The Ag-rich famatinite selenides
   - NaCu2SbSe4
   - KCu2SbSe4 last
2. **Add Sb³⁺/As³⁺ competitor phases** to the hull explicitly (listed in Caveats) and recompute Ehull for the famatinite and alkali families.
3. **Compare polymorphs** (famatinite vs enargite, kesterite vs stannite) for the I3-V-VI4 hits.
4. **Re-evaluate TiZn(AgS2)2** with DFT, and as a sanity check compare its formation energy with a weighted sum of binary formation energies.
5. **Verify the experimental Na3SbSe4 gap** and use it to correct the alkali-member gap estimates. Add further known calibration compounds in each family.
6. **Look into the anomalies:**
   - The ~1 eV gap jump between Cu2AgSbSe4 and CuAg2SbSe4
   - The Cd–Te gap collapse against Zn–Te (CdAg2GeTe4 0.48 vs ZnAg2GeTe4 1.17)
7. **Unexplored follow-ups noted in the notebook:** mixed Na/Ag tellurides such as Na2AgSbTe4, which did not appear in the iteration-5 enumeration.
8. **Process:** propose and evaluate one family at a time, so that critic vetoes and combinatorial lockouts don't use up candidate families before they are tested.
