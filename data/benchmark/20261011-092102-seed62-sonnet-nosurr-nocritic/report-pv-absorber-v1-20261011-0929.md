# Campaign report: pv-absorber-v1

## Executive summary

Over 5 iterations, 92 candidates were relaxed and scored (20, 19, 18, 20 and 15 per iteration). All were evaluated with CHGNet relaxation and an ML, HSE-fidelity band-gap model. 91 were novel versus the Materials Project. One, MnCu2SnS4, was flagged `is_novel = 0` in the database and appears to be a known compound. The target window was a band gap of about 1.1–1.7 eV with E_hull ≤ 0.05 eV/atom.

15 novel compounds met both criteria:
- Ag-based kesterite-type I₂-II-IV-VI₄ compounds: CdAg2GeSe4, ZnAg2GeSe4, MgAg2SnSe4, MgAg2GeTe4, MgAg2SnTe4, ZnAg2GeTe4 and SrAg2GeSe4.
- Famatinite-type I₃-V-VI₄ compounds: CuAg2AsSe4, CuAg2SbSe4, Ag3SbSe4 and Ag3AsSe4.
- KBiTe2.
- Ni-containing kesterite-type compounds: NiAg2GeSe4, NiAg2SnSe4 and Cu2NiGeS4.

The most credible leads by gap and stability are CuAg2AsSe4 (1.38 eV, E_hull 0.000), CdAg2GeSe4 (1.28 eV, E_hull 0.000) and CuAg2SbSe4 (1.46 eV, E_hull 0.000). All results are surrogate-model predictions with no DFT, HSE or experimental confirmation. Confidence is moderate at best. The Ni, Mn and Co results, the KBiTe2 prototype and the Cu/Ag-mixed compounds carry specific doubts, listed under caveats.

## Scored candidates

All values come from the campaign database: E_f is the formation energy per atom (eV), E_hull is the energy above hull (eV/atom), and the gap is the ML HSE-fidelity band gap (eV). Window hits are gap 1.1–1.7 eV and E_hull ≤ 0.05.

### Iteration 1: Ag/Cd/Mg/Ca kesterite-type variants

| Formula | E_f | E_hull | Gap | Note |
|---|---|---|---|---|
| CdAg2GeSe4 | -0.657 | 0.000 | 1.279 | **hit** |
| ZrCd(AgSe2)2 | -1.148 | 0.000 | 0.295 | gap too low |
| CdAg2GeTe4 | -0.326 | 0.017 | 0.481 | gap too low |
| MgAg2GeS4 | -1.165 | 0.017 | 1.893 | gap high |
| MgAg2GeSe4 | -0.797 | 0.020 | 1.856 | gap high |
| MgAg2GeTe4 | -0.423 | 0.025 | 1.490 | **hit** |
| CaAg2GeTe4 | -0.587 | 0.058 | 0.240 | |
| CaAg2GeSe4 | -0.949 | 0.062 | 1.679 | E_hull above cutoff |
| CdSi(AgTe2)2 | -0.230 | 0.083 | 1.055 | |
| MgSi(AgTe2)2 | -0.331 | 0.087 | 1.802 | |
| CdSi(AgSe2)2 | -0.568 | 0.130 | 1.714 | |
| MgCu2GeSe4 | -0.717 | 0.136 | 1.102 | |
| MgSi(AgSe2)2 | -0.715 | 0.145 | 2.348 | |
| CdSi(AgS2)2 | -0.937 | 0.152 | 2.751 | |
| MgSi(AgS2)2 | -1.132 | 0.167 | 2.541 | |
| CaSi(AgSe2)2 | -0.867 | 0.187 | 2.510 | |
| TiCd(AgSe2)2 | -0.590 | 0.357 | 2.354 | |
| MgTi(AgSe2)2 | -0.725 | 0.380 | 2.433 | |
| MgZr(AgSe2)2 | -0.720 | 0.459 | 1.579 | |
| CaZr(AgSe2)2 | -0.882 | 0.493 | 2.471 | |

### Iteration 2: Sn analogues, Sr/Ba, and Cu-based Mg/Ca/Sr kesterites

| Formula | E_f | E_hull | Gap | Note |
|---|---|---|---|---|
| ZnAg2GeSe4 | -0.681 | 0.000 | 1.119 | **hit** |
| SrAg2SnS4 | -1.369 | 0.000 | 1.720 | just above window |
| SrAg2SnSe4 | -1.059 | 0.000 | 1.701 | just above window |
| NaGaS2 | -1.810 | 0.000 | 3.827 | wide gap |
| SrAg2GeSe4 | -1.021 | 0.003 | 1.687 | **hit** (edge of window) |
| SrAg2GeS4 | -1.354 | 0.013 | 1.867 | gap high |
| MgAg2SnSe4 | -0.838 | 0.016 | 1.588 | **hit** |
| CdAg2SnTe4 | -0.366 | 0.027 | 0.412 | gap too low |
| ZnAg2GeTe4 | -0.318 | 0.028 | 1.171 | **hit** |
| MgAg2SnTe4 | -0.461 | 0.038 | 1.172 | **hit** |
| ZnAg2SnTe4 | -0.358 | 0.039 | 0.596 | gap too low |
| SrCu2SnSe4 | -1.045 | 0.050 | 1.109 | |
| MgCu2SnSe4 | -0.819 | 0.071 | 1.383 | |
| SrCu2GeTe4 | -0.614 | 0.078 | 0.161 | |
| MgCu2GeTe4 | -0.372 | 0.101 | 0.895 | |
| CaCu2SnSe4 | -0.979 | 0.108 | 0.944 | |
| MgCu2SnTe4 | -0.409 | 0.109 | 0.483 | |
| CaCu2GeTe4 | -0.554 | 0.116 | 0.034 | |
| CaCu2GeSe4 | -0.928 | 0.121 | 1.198 | |

### Iteration 3: Ba tellurides, alkali pnictogen/gallium chalcogenides, Fe/Mn kesterites, II-IV-Sb2

| Formula | E_f | E_hull | Gap | Note |
|---|---|---|---|---|
| BaAg2GeTe4 | -0.704 | 0.000 | 0.705 | gap too low |
| KSbTe2 | -0.741 | 0.000 | 0.547 | gap too low |
| KGaSe2 | -1.275 | 0.000 | 2.177 | wide gap |
| KBiTe2 | -0.736 | 0.003 | 1.296 | **hit** (see caveats) |
| BaAg2SnTe4 | -0.746 | 0.007 | 0.516 | gap too low |
| NaGaSe2 | -1.169 | 0.017 | 2.202 | wide gap |
| FeAg2SnSe4 | -0.579 | 0.072 | -0.003 | |
| FeAg2GeSe4 | -0.525 | 0.078 | 0.018 | |
| MnAg2GeS4 | -0.914 | 0.079 | 2.236 | |
| FeAg2GeTe4 | -0.199 | 0.112 | 0.012 | |
| FeAg2SnTe4 | -0.243 | 0.119 | 0.011 | |
| MgSnSb2 | -0.112 | 0.123 | 0.009 | |
| FeAg2GeS4 | -0.851 | 0.135 | 0.013 | |
| CdGeSb2 | 0.078 | 0.172 | 0.315 | |
| MgGeSb2 | -0.054 | 0.177 | 0.006 | |
| ZnGeSb2 | 0.110 | 0.199 | 0.229 | |
| CdSiSb2 | 0.171 | 0.251 | 0.548 | |
| ZnSiSb2 | 0.206 | 0.281 | 1.201 | gap in window, but E_hull 0.28 |

### Iteration 4: famatinite-type I₃-V-VI₄ and remaining Ag-kesterite members

| Formula | E_f | E_hull | Gap | Note |
|---|---|---|---|---|
| Ag3SbS4 | -0.856 | 0.000 | 1.791 | gap slightly high |
| Ag3SbSe4 | -0.573 | 0.000 | 1.665 | **hit** |
| CuAg2SbS4 | -0.856 | 0.000 | 1.862 | gap slightly high |
| CuAg2SbSe4 | -0.565 | 0.000 | 1.457 | **hit** |
| Cu2AgSbS4 | -0.855 | 0.000 | 1.738 | gap slightly high |
| Cu2AgSbSe4 | -0.523 | 0.000 | 0.425 | gap too low |
| Ag3AsSe4 | -0.541 | 0.000 | 1.681 | **hit** |
| CuAg2AsS4 | -0.828 | 0.000 | 1.974 | gap high |
| CuAg2AsSe4 | -0.530 | 0.000 | 1.378 | **hit** |
| Cu2AgAsS4 | -0.824 | 0.000 | 1.869 | gap high |
| Cu2AgAsSe4 | -0.483 | 0.000 | 0.436 | gap too low |
| MgAg2SnS4 | -1.177 | 0.002 | 1.871 | gap slightly high |
| SrAg2GeTe4 | -0.651 | 0.016 | 0.155 | gap too low |
| CuAg2PS4 | -0.830 | 0.020 | 2.448 | wide gap |
| SrAg2SnTe4 | -0.689 | 0.029 | 0.100 | gap too low |
| Cu2AgPSe4 | -0.425 | 0.045 | 2.139 | wide gap |
| CaAg2SnSe4 | -0.998 | 0.051 | 1.816 | |
| CaAg2SnS4 | -1.297 | 0.068 | 2.279 | |
| CaAg2SnTe4 | -0.625 | 0.072 | 0.062 | |
| CaAg2GeS4 | -1.273 | 0.094 | 2.148 | |

### Iteration 5: Ni/Co/Mn kesterite-type variants

| Formula | E_f | E_hull | Gap | Note |
|---|---|---|---|---|
| NiAg2SnS4 | -0.936 | 0.000 | 1.897 | gap high |
| NiAg2SnSe4 | -0.631 | 0.000 | 1.676 | **hit** (low confidence) |
| NiAg2GeSe4 | -0.583 | 0.0005 | 1.648 | **hit** (low confidence) |
| NiAg2GeS4 | -0.911 | 0.008 | 1.744 | gap slightly high |
| Cu2NiGeS4 | -0.979 | 0.013 | 1.120 | **hit** (low confidence) |
| Cu2NiGeSe4 | -0.577 | 0.041 | 0.255 | gap too low |
| NiAg2SnTe4 | -0.323 | 0.045 | 0.039 | gap too low |
| CoAg2SnSe4 | -0.569 | 0.056 | 0.603 | |
| MnCu2SnS4 | -0.998 | 0.070 | 1.496 | flagged `is_novel = 0` in the database |
| CoAg2GeSe4 | -0.524 | 0.075 | 0.809 | |
| CoAg2SnS4 | -0.860 | 0.092 | 1.388 | |
| MnCu2GeSe4 | -0.531 | 0.104 | 0.931 | |
| CoAg2GeS4 | -0.835 | 0.113 | 1.512 | |
| Cu2SiNiSe4 | -0.479 | 0.167 | 0.190 | |
| CoCu2SiSe4 | -0.419 | 0.233 | 0.334 | |

## Hypotheses tested and what was learned

**Iteration 1: mixed-cation/anion kesterites.**
- Hypothesis: isoelectronic substitution (Ag/Cu, Cd/Zn/Mg, Ge/Si/Sn, S/Se/Te) keeps the gap in 1.1–1.7 eV and keeps compounds near the hull.
- Hits: CdAg2GeSe4 and MgAg2GeTe4.
- Trends: Si-containing variants were unstable (E_hull 0.08–0.19). Ti/Zr variants were very unstable, except ZrCd(AgSe2)2, which is stable but has too small a gap. Ge was the best IV-site element. Replacing Cd with Mg raised the gap, and replacing Se with Te lowered it.

**Iteration 2: Sn analogues, Sr, Zn, and Cu versions.**
- Hits: ZnAg2GeSe4, MgAg2SnSe4, MgAg2SnTe4, ZnAg2GeTe4 and SrAg2GeSe4.
- Near misses: SrAg2SnSe4 and SrAg2SnS4 (gaps 1.70 and 1.72 eV, E_hull 0.000).
- Cu-based Mg/Ca/Sr kesterites were all unstable (E_hull 0.05–0.12), so Ag appears to be what stabilizes the large or hard cations. The notebook records that 1 relaxation went unspent.

**Iteration 3: pnictide and alkali-chalcogenide exploration.**
- The II-IV-Sb2 chalcopyrite-type antimonides were falsified. They were all unstable (E_hull 0.12–0.28) with mostly small gaps. P analogues were rejected by the SMACT filter.
- Fe kesterites were metallic (gap ≈ 0). MnAg2GeS4 had E_hull 0.079.
- BaAg2GeTe4 and BaAg2SnTe4 are stable but have gaps of 0.7 and 0.5 eV.
- KBiTe2 (1.30 eV, E_hull 0.003) was the one new hit. KSbTe2 is stable with a low gap. NaGaSe2 and KGaSe2 have wide gaps.
- The notebook records that BaAg2GeSe4 is already in the Materials Project, with an ML gap of 0.035 eV, so the ML gap looks unreliable there.
- 2 relaxations went unspent.

**Iteration 4: famatinite-type I₃-V-VI₄ family.**
- Hits: CuAg2AsSe4, CuAg2SbSe4, Ag3SbSe4 and Ag3AsSe4, all at E_hull 0.000.
- Trends: more Ag raises the gap (Cu2Ag 0.43 eV, CuAg2 about 1.4 eV, Ag3 about 1.67 eV for the selenides). S versus Se adds about 0.4 eV. P variants have wide gaps (2.1–2.4 eV).
- The sharp jump from Cu2Ag to CuAg2 was flagged in the notebook as possibly an ordering or structural artifact.
- Ca-based Ag kesterites were unstable (E_hull 0.05–0.09). Sr-Te variants were stable but have near-zero gaps.

**Iteration 5: Ni/Co/Mn extension.**
- Hits: NiAg2GeSe4, NiAg2SnSe4 and Cu2NiGeS4.
- Co variants were unstable, except CoAg2SnS4, which has a gap of 1.39 eV but E_hull 0.092. Mn variants were unstable, and Si variants were again unstable.
- Te variants gave gaps near zero. The Bi/Te variants of the famatinite family had already been considered, so the tool returned no new candidates.
- 5 relaxations went unspent.

**Overall:** the Ag-containing, closed-shell-cation kesterite-type and famatinite-type selenides and tellurides were the productive families. Pnictide II-IV-V2 compounds, Si-, Ti/Zr-, Fe- and Ca-based variants, and Cu-with-large-cation variants were falsified in this setup.

## Caveats

- **Surrogate accuracy.** E_hull comes from CHGNet relaxations and the gaps from an ML HSE-fidelity model. The error bars were never quantified in this campaign. The BaAg2GeSe4 case shows the gap model can be badly off for compounds that are already known.
- **Hull of exactly 0.** Many Ag compounds sit at E_hull ≈ 0.000, which may reflect sparse competing phases in the reference data rather than true stability.
- **Ordering and polymorphs.** Cu/Ag and cation site ordering was arbitrary. Competing polymorphs (stannite versus kesterite, or sulvanite/enargite-type structures for Ag3SbSe4) were not examined.
- **KBiTe2.** Its prototype is chalcopyrite-derived, and the real ground state is probably a rocksalt-ordered variant. The gap is likely overestimated for a Bi compound because spin-orbit coupling is not included.
- **Ni, Co, Mn and Fe compounds.** Tetrahedral Ni²⁺ is chemically suspect. The ML gap for open-shell transition metals is probably unreliable (no Hubbard U, spin state unspecified). The Ni hits are low confidence.
- **Gap accuracy near the window edge.** Several "hits" (SrAg2GeSe4, Ag3SbSe4, Ag3AsSe4, NiAg2GeSe4, NiAg2SnSe4) lie within about 0.05 eV of the 1.7 eV upper edge. That is well inside the plausible model error.
- **Novelty.** Novelty was checked only against the Materials Project. Some compounds may exist in the literature. A Crossref check was not documented for most candidates. MnCu2SnS4 was flagged as not novel.
- **Required validation.**
  - Hybrid-functional DFT (HSE with SOC for Bi and Sb compounds).
  - Phonon stability.
  - A full competing-phase hull including relevant binaries and ternaries.
  - Polymorph and ordering searches.
  - Defect and absorption calculations.
  - Synthesis feasibility checks.

## Recommended next steps

1. Verify the top candidates with HSE(+SOC) and a rigorous hull analysis: CuAg2AsSe4, CuAg2SbSe4, CdAg2GeSe4, ZnAg2GeSe4, MgAg2SnSe4, MgAg2GeTe4 and KBiTe2.
2. Test competing structure types and cation orderings for the famatinite-type Ag compounds, and the rocksalt-ordered variant for KBiTe2.
3. Tune the gap toward about 1.4 eV by alloying. Candidates are Zn/Mg or Cd/Mg mixing, Se/Te mixing, and Ge/Sn mixing. This needs ordered supercells, which the prototype tool does not provide.
4. Treat the Ni, Co and Mn results as exploratory until checked with spin-polarized DFT+U.
5. Do a literature and database novelty check on the hit list before any synthesis effort.
