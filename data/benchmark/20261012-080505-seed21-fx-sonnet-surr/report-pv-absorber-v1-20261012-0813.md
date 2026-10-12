# Campaign report: pv-absorber-v1

## Executive summary

Over five iterations the campaign scored 98 candidates, all flagged novel against the Materials Project database. The working target was a band gap of 1.1–1.7 eV with E_hull ≤ 0.05 eV/atom; this window is stated in the iteration 2 hypothesis. Five candidates met both criteria, all kesterite-type Ag2-M-M'-X4 chalcogenides:

- Ag2BaSiSe4 (1.42 eV, E_hull 0.026)
- Ag2SrSiSe4 (1.69 eV, E_hull 0.021)
- Ag2SrSnS4 (1.67 eV, E_hull 0.024)
- Ag2MgSnSe4 (1.15 eV, E_hull 0.043)
- Ag2MgSiTe4 (1.63 eV, E_hull 0.014)

Confidence is low to moderate. Everything is computed (relaxation plus a gap model) with no synthesis, no higher-level electronic structure, and no polymorph search. Two hits sit within about 0.01 eV of the window's upper edge. Ag2MgSnSe4 is marginal on stability, and its gap trend contradicts the S-vs-Se trend seen elsewhere, so the notebook attributes it to gap-model noise. The campaign found no hits in its final iteration (5).

## Scored candidates

Hits are bold. "Hit" means gap 1.1–1.7 eV and E_hull ≤ 0.05 eV/atom. E_form is formation energy per atom (eV), E_hull is energy above hull (eV/atom), and Gap is in eV.

### Iteration 1

| Formula | E_form | E_hull | Gap |
|---|---|---|---|
| CdAg2GeSe4 | -0.551 | 0.000 | 0.026 |
| CdSi(AgSe2)2 | -0.599 | 0.000 | 0.745 |
| MgSi(AgSe2)2 | -0.739 | 0.011 | 1.837 |
| MgAg2GeSe4 | -0.690 | 0.018 | 0.282 |
| **SrSi(AgSe2)2 (Ag2SrSiSe4)** | -0.932 | 0.021 | 1.694 |
| **BaSi(AgSe2)2 (Ag2BaSiSe4)** | -0.965 | 0.026 | 1.423 |
| SrAg2GeSe4 | -0.879 | 0.035 | 0.150 |
| BaCu2SiSe4 | -0.952 | 0.054 | 1.812 |
| SrCu2SiSe4 | -0.913 | 0.055 | 1.736 |
| CaSi(AgSe2)2 | -0.883 | 0.061 | 2.177 |
| BaCu2GeTe4 | -0.686 | 0.066 | 0.350 |
| CaAg2GeSe4 | -0.833 | 0.068 | 0.258 |
| ZrCd(AgSe2)2 | -0.822 | 0.088 | 0.014 |
| SrCu2GeTe4 | -0.646 | 0.092 | 0.156 |
| BaCu2SiTe4 | -0.630 | 0.098 | 0.541 |
| SrCu2SiTe4 | -0.595 | 0.119 | 0.268 |
| MgZr(AgSe2)2 | -0.950 | 0.119 | 0.116 |
| CaZr(AgSe2)2 | -1.092 | 0.173 | 0.092 |

### Iteration 2

| Formula | E_form | E_hull | Gap |
|---|---|---|---|
| CdSi(AgS2)2 | -0.721 | 0.000 | 2.220 |
| MgAg2GeS4 | -0.798 | 0.006 | 1.777 |
| MgAg2SnS4 | -0.788 | 0.011 | 0.691 |
| MgSi(AgS2)2 | -0.908 | 0.012 | 2.463 |
| SrAg2GeS4 | -0.971 | 0.017 | 1.946 |
| **SrAg2SnS4** | -0.961 | 0.024 | 1.667 |
| BaSi(AgS2)2 | -1.106 | 0.029 | 2.565 |
| SrSi(AgS2)2 | -1.083 | 0.033 | 2.543 |
| SrAg2SnSe4 | -0.896 | 0.052 | 0.340 |
| SrCu2SiS4 | -1.103 | 0.058 | 3.173 |
| CaAg2GeS4 | -0.928 | 0.060 | 1.752 |
| BaCu2SiS4 | -1.119 | 0.060 | 3.133 |
| CaAg2SnS4 | -0.922 | 0.063 | 0.517 |
| SrCu2SnSe4 | -0.902 | 0.083 | 0.105 |
| CaCu2SiS4 | -1.066 | 0.089 | 3.311 |
| CaCu2SnS4 | -0.976 | 0.089 | 2.199 |
| CaAg2SnSe4 | -0.851 | 0.089 | 1.454 |
| CaCu2GeS4 | -0.966 | 0.090 | 2.625 |
| CaCu2GeSe4 | -0.829 | 0.110 | 0.301 |
| CaCu2SnSe4 | -0.860 | 0.117 | 0.212 |

### Iteration 3

| Formula | E_form | E_hull | Gap |
|---|---|---|---|
| ZnSi(AgSe2)2 | -0.614 | 0.000 | 1.841 |
| ZnAg2GeSe4 | -0.567 | 0.003 | 0.677 |
| TiCd(AgS2)2 | -0.921 | 0.007 | 2.228 |
| TiZn(AgSe2)2 | -0.847 | 0.014 | 1.887 |
| TiCd(AgSe2)2 | -0.818 | 0.019 | 0.609 |
| MnAg2GeS4 | -0.593 | 0.021 | 0.248 |
| TiZn(AgS2)2 | -0.951 | 0.022 | 2.046 |
| TiMn(AgSe2)2 | -0.747 | 0.031 | 0.110 |
| BaTi(AgSe2)2 | -1.164 | 0.035 | 2.033 |
| **MgAg2SnSe4** | -0.700 | 0.043 | 1.153 |
| BaTi(AgS2)2 | -1.280 | 0.049 | 2.245 |
| MnSi(AgS2)2 | -0.686 | 0.052 | 0.086 |
| SrTi(AgS2)2 | -1.253 | 0.056 | 2.170 |
| SrTi(AgSe2)2 | -1.129 | 0.071 | 2.326 |
| TiMn(AgS2)2 | -0.872 | 0.092 | 1.392 |
| ZrCd(AgS2)2 | -0.920 | 0.097 | 1.877 |
| ZrZn(AgS2)2 | -0.957 | 0.106 | 1.223 |
| BaZr(AgS2)2 | -1.273 | 0.144 | 0.379 |
| SrZr(AgS2)2 | -1.250 | 0.149 | 1.610 |
| ZrMn(AgS2)2 | -0.883 | 0.159 | 0.017 |

### Iteration 4

| Formula | E_form | E_hull | Gap |
|---|---|---|---|
| ZnSi(AgTe2)2 | -0.355 | 0.001 | 1.717 |
| CdSi(AgTe2)2 | -0.344 | 0.008 | 0.332 |
| **MgSi(AgTe2)2 (Ag2MgSiTe4)** | -0.447 | 0.014 | 1.627 |
| MgAg2GeTe4 | -0.479 | 0.015 | 0.870 |
| MgTi(AgS2)2 | -1.088 | 0.040 | 1.785 |
| MgTi(AgTe2)2 | -0.677 | 0.048 | 0.212 |
| TiCd(AgTe2)2 | -0.572 | 0.048 | 0.091 |
| TiZn(AgTe2)2 | -0.573 | 0.051 | 0.065 |
| MgTi(AgSe2)2 | -0.943 | 0.053 | 1.516 |
| SrSi(AgTe2)2 | -0.610 | 0.067 | 1.894 |
| SrAg2GeTe4 | -0.645 | 0.068 | 0.690 |
| BaSi(AgTe2)2 | -0.645 | 0.069 | 2.147 |
| MgZr(AgTe2)2 | -0.712 | 0.078 | 0.380 |
| ZrZn(AgTe2)2 | -0.601 | 0.087 | 0.346 |
| ZrCd(AgTe2)2 | -0.595 | 0.090 | 0.020 |
| MgZr(AgS2)2 | -1.083 | 0.134 | 0.230 |
| TiFe(AgS2)2 | -0.785 | 0.171 | 0.977 |
| TiFe(AgSe2)2 | -0.631 | 0.173 | 0.334 |
| TiFe(AgTe2)2 | -0.385 | 0.179 | 0.009 |
| ZrFe(AgS2)2 | -0.802 | 0.233 | 0.025 |

### Iteration 5 (no hits)

| Formula | E_form | E_hull | Gap |
|---|---|---|---|
| MnCu2GeSe4 | -0.525 | 0.000 | 0.661 |
| KGaSe2 | -1.113 | 0.000 | 3.307 |
| KAlS2 | -1.494 | 0.000 | 3.920 |
| MgCu2SnS4 | -0.866 | 0.014 | 0.490 |
| MgCu2GeTe4 | -0.502 | 0.017 | 0.520 |
| MgCu2SnTe4 | -0.537 | 0.026 | 0.346 |
| MgCu2GeSe4 | -0.713 | 0.030 | 0.307 |
| MgCu2SiTe4 | -0.461 | 0.034 | 0.245 |
| MgCu2SnSe4 | -0.734 | 0.047 | 0.189 |
| SiNi(AgS2)2 | -0.606 | 0.049 | 0.411 |
| KBiTe2 | -0.735 | 0.050 | 0.564 |
| KSbTe2 | -0.682 | 0.054 | 0.361 |
| CoAg2SnS4 | -0.504 | 0.069 | 0.477 |
| CoSi(AgSe2)2 | -0.455 | 0.076 | 0.757 |
| CoAg2GeS4 | -0.491 | 0.078 | 0.598 |
| CaAg2GeTe4 | -0.607 | 0.083 | 0.868 |
| CaSi(AgTe2)2 | -0.569 | 0.086 | 1.920 |
| CoSi(AgS2)2 | -0.578 | 0.103 | 1.893 |
| FeAg2GeS4 | -0.501 | 0.106 | 0.289 |
| FeSi(AgSe2)2 | -0.448 | 0.109 | 0.014 |

## Hypotheses tested and what was learned

**Iteration 1: isoelectronic kesterite substitutions.**
- The idea was to tune the gap of Cu2ZnSnS4-type compounds into 1.1–1.7 eV by substituting Zn→Cd/Mg, Sn→Ge/Si and Cu→Ag. Se for S was a further option.
- It partly held. Ag + Ba/Sr + Si + Se gave 1.42 and 1.69 eV near the hull.
- Ge variants had gaps near zero in this gap model.
- Ca variants had E_hull > 0.05.
- Zr variants were unstable (E_hull 0.09–0.17).
- Cu-Ba/Sr-Si/Ge-Se/Te variants (six candidates) all had E_hull > 0.05. The Te members had small gaps.
- The notebook flags that the kesterite prototype is probably not the true ground state for large Ba/Sr, so hull values may not reflect competing polymorphs.

**Iteration 2: anion tuning and Sn variants.**
- S widens the gap relative to Se, so Ge and Cd variants were expected to move into the window.
- One new hit appeared: SrAg2SnS4 (1.667 eV, E_hull 0.024).
- Observed trends: S gaps are about 0.6–0.9 eV above Se gaps, and the cation order is Si > Ge > Sn. Cu-S compounds are too wide (2.2–3.3 eV).
- Near misses: MgAg2GeS4 (1.78 eV, E_hull 0.006) was just above the window. Several others were stable but off-gap.
- Ca and Cu analogues failed on stability. CaAg2SnSe4 has a gap of 1.45 eV but E_hull 0.089.

**Iteration 3: broader cation sets (Zn/Cd/Mn on the divalent site, Ti/Zr on the tetravalent site).**
- One marginal hit: MgAg2SnSe4 (1.153 eV, E_hull 0.043). Its gap is higher than that of the S analogue (0.69 eV), contrary to the trend above; the notebook calls this gap-model noise.
- Ti(IV) compounds were stable but too wide (about 1.9–2.3 eV).
- Zr and Mn compounds gave small gaps or were unstable.
- Several in-window gaps were unstable: ZrZn(AgS2)2, TiMn(AgS2)2 and SrZr(AgS2)2.
- Chalcopyrite/zincblende proposals were mostly known compounds, or novel but wide-gap Na compounds, and were skipped.

**Iteration 4: tellurides and Ti/Zr/Fe-containing variants.**
- One hit: Ag2MgSiTe4 (1.627 eV, E_hull 0.014).
- ZnSi(AgTe2)2 has E_hull of about 0.001 and a gap of 1.717 eV, just above the window.
- MgTi(AgSe2)2 has a gap of 1.52 eV but E_hull 0.053, a marginal fail.
- Sr/Ba silicon tellurides have E_hull of about 0.07, so Te appears too large or soft for the big alkaline earths in this prototype.
- Ti/Zr/Fe tellurides and Zr/Fe variants failed (gap near 0 or E_hull > 0.07).
- Mo and W were rejected by the SMACT filter.

**Iteration 5: Cu-Mg kesterite-types, 3d-metal Ag kesterite-types, alkali chalcopyrite-types.**
- No new hits. The notebook for this iteration contains only a reflection entry. The hypothesis text was taken from the candidate database, and no iteration-5 observation entry was recorded.
- Cu-Mg-(Si/Ge/Sn)-chalcogenides were near-stable (E_hull 0.0–0.047) but with gaps of 0.2–0.7 eV, too small.
- Fe/Co/Ni Ag kesterite-types were unstable (E_hull 0.05–0.11).
- KGaSe2 and KAlS2 were stable but wide-gap (3.3 and 3.9 eV).
- KSbTe2 and KBiTe2 have gaps of 0.4–0.6 eV with E_hull about 0.05.
- KGaSe2 and KAlS2 are simple compositions that the tool flags as novel. This is worth a manual literature recheck.

**Overall:** the productive family is Ag-(Ba/Sr/Mg/Zn)-(Si/Sn)-chalcogen kesterite-type. Ca, Cu, Ti, Zr, Fe, Co and Mn variants did not produce hits. The proposer could not generate mixed-anion or alloy formulas, so the planned fine-tuning (for example S/Se or Si/Ge mixing) was never tested.

## Caveats

- **Surrogate-level data.** Gaps come from a gap model and stability from relaxed-structure E_hull. No error bars were computed. The notebook itself notes model noise, including the non-monotonic S-to-Se gap in Mg-Ag-Sn-X4. Such models usually carry errors of several tenths of an eV, so hits near the 1.1 and 1.7 eV boundaries (Ag2MgSnSe4, Ag2SrSiSe4, Ag2SrSnS4) and near-misses on both sides are not reliably separable.
- **Prototype assumption.** All hits were evaluated in a kesterite-type prototype. For large Ba/Sr cations the notebook expects other structure types to be the true ground states, so E_hull values of 0.02–0.03 may understate competition from other polymorphs. The Ag2MgSnSe4 E_hull of 0.043 is already close to the 0.05 cutoff.
- **Novelty.** Novelty is relative only to the Materials Project database. Known compounds such as BaCu2GeSe4 and SrCu2GeSe4 were skipped. Novel compounds may exist in the literature but not in the database.
- **Absorber relevance.** No absorption coefficient, band-edge character (direct vs. indirect), defect tolerance, or carrier transport was assessed. Only the gap window and E_hull were screened.

Validation the top candidates would need:
- Higher-level electronic structure for the gap, such as hybrid functional or GW, with direct/indirect character.
- A competing-phase and polymorph search, including non-kesterite structure types for Ba/Sr, plus phonon stability.
- Synthesis attempts and structural characterization.

## Recommended next steps

1. Run the validation above first, prioritizing Ag2BaSiSe4, Ag2SrSnS4 and Ag2MgSiTe4, which have the most margin on both criteria. Ag2SrSiSe4 and Ag2MgSnSe4 are edge cases.
2. Revisit ZnSi(AgTe2)2 (1.717 eV, E_hull 0.001) and MgAg2GeS4 (1.78 eV, E_hull 0.006). Both are on or near the hull and just above the gap window, so a small correction could move them in.
3. Extend the tooling to mixed-anion and alloy formulas, for example Si/Ge mixing on MgAg2(Si,Ge)Te4 or Se/Te mixing. This was the planned next step in iterations 4 and 5 and could not be run.
4. Explore non-kesterite prototypes for the Ba/Sr compounds.
5. Recheck the literature for the simple novel-flagged compositions (KGaSe2, KAlS2) before calling them discoveries.
