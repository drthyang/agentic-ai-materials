# Campaign report: pv-absorber-v1

## Executive summary

Five iterations scored 99 candidates, all flagged novel against the Materials Project (MP). The notebook targets a band gap near 1.4 eV, with an acceptance window of 1.1–1.7 eV. Twelve candidates fall inside that window with a predicted energy above hull (Ehull) of 0.05 eV/atom or less. The most promising are in the I₃–V–VI₄ (Cu/Ag/Na/K–As/P/Sb–S/Se) family found in iterations 4–5. The closest to 1.4 eV are **CuAg₂PSe₄** (1.49 eV, Ehull 0.000), **NaAg₂AsSe₄** (1.45 eV, Ehull 0.004) and **BaSi(AgSe₂)₂** (1.42 eV, Ehull 0.026). **Confidence is low to moderate.** Every gap and stability value is a machine-learned surrogate prediction (the notebook describes the gaps as CHGNet-HSE-like and noisy). Nothing has been checked with DFT or synthesis, and the notebook documents at least one apparent surrogate inconsistency (see Caveats).

## Scored candidates

Columns: Ef = formation energy per atom (eV/atom), Ehull = energy above hull (eV/atom), Gap = predicted band gap (eV). ✓ marks a "hit": gap in 1.1–1.7 eV and Ehull ≤ 0.05. All 99 rows were converged and flagged novel.

| Iter | Formula | Ef | Ehull | Gap | Hit |
|---|---|---|---|---|---|
| 1 | CdAg2GeSe4 | -0.551 | 0.000 | 0.026 | |
| 1 | CdSi(AgSe2)2 | -0.599 | 0.000 | 0.745 | |
| 1 | ZnSi(AgSe2)2 | -0.614 | 0.000 | 1.841 | |
| 1 | ZnAg2GeSe4 | -0.567 | 0.003 | 0.677 | |
| 1 | MgAg2GeS4 | -0.798 | 0.006 | 1.777 | |
| 1 | CdSi(AgTe2)2 | -0.344 | 0.008 | 0.332 | |
| 1 | MgAg2SnS4 | -0.788 | 0.011 | 0.691 | |
| 1 | MgSi(AgSe2)2 | -0.739 | 0.011 | 1.837 | |
| 1 | MgSi(AgS2)2 | -0.908 | 0.012 | 2.463 | |
| 1 | MgCu2SnS4 | -0.866 | 0.014 | 0.490 | |
| 1 | CdAg2GeTe4 | -0.375 | 0.014 | 0.166 | |
| 1 | MgAg2GeTe4 | -0.479 | 0.015 | 0.870 | |
| 1 | MgAg2GeSe4 | -0.690 | 0.018 | 0.282 | |
| 1 | MgCu2GeSe4 | -0.713 | 0.030 | 0.307 | |
| 1 | MgAg2SnSe4 | -0.700 | 0.043 | 1.153 | ✓ |
| 1 | MgCu2SnSe4 | -0.734 | 0.047 | 0.189 | |
| 1 | CaAg2SnS4 | -0.922 | 0.063 | 0.517 | |
| 1 | CaCu2SnS4 | -0.976 | 0.089 | 2.199 | |
| 1 | CaCu2GeS4 | -0.966 | 0.090 | 2.625 | |
| 1 | CaCu2SnSe4 | -0.860 | 0.117 | 0.212 | |
| 2 | NaGaS2 | -1.193 | 0.000 | 4.245 | |
| 2 | NaAlS2 | -1.462 | 0.000 | 4.084 | |
| 2 | ZnGeSb2 | -0.127 | 0.009 | 0.239 | |
| 2 | SrAg2GeS4 | -0.971 | 0.017 | 1.946 | |
| 2 | SrSi(AgSe2)2 | -0.932 | 0.021 | 1.694 | ✓ |
| 2 | MnAg2GeS4 | -0.593 | 0.021 | 0.248 | |
| 2 | BaSi(AgSe2)2 | -0.965 | 0.026 | 1.424 | ✓ |
| 2 | BaSi(AgS2)2 | -1.106 | 0.029 | 2.565 | |
| 2 | CdGeSb2 | -0.109 | 0.032 | 0.135 | |
| 2 | SrSi(AgS2)2 | -1.083 | 0.033 | 2.543 | |
| 2 | SrAg2GeSe4 | -0.879 | 0.035 | 0.150 | |
| 2 | ZnSiSb2 | -0.075 | 0.048 | 0.906 | |
| 2 | MnSi(AgS2)2 | -0.686 | 0.052 | 0.086 | |
| 2 | CdSiSb2 | -0.071 | 0.057 | 0.200 | |
| 2 | Na2SrGeSe4 | -1.261 | 0.074 | 2.891 | |
| 2 | FeAg2GeSe4 | -0.419 | 0.075 | 0.151 | |
| 2 | MgSnSb2 | -0.231 | 0.079 | 0.035 | |
| 2 | MgGeSb2 | -0.181 | 0.081 | 0.058 | |
| 2 | FeAg2GeS4 | -0.501 | 0.106 | 0.289 | |
| 2 | FeSi(AgSe2)2 | -0.448 | 0.109 | 0.014 | |
| 3 | ZnSi(AgTe2)2 | -0.355 | 0.001 | 1.717 | |
| 3 | TiCd(AgS2)2 | -0.921 | 0.007 | 2.228 | |
| 3 | ZnAg2GeTe4 | -0.382 | 0.010 | 0.627 | |
| 3 | TiZn(AgSe2)2 | -0.847 | 0.014 | 1.887 | |
| 3 | MgCu2GeTe4 | -0.502 | 0.017 | 0.520 | |
| 3 | TiZn(AgS2)2 | -0.951 | 0.022 | 2.046 | |
| 3 | SrAg2SnS4 | -0.961 | 0.024 | 1.667 | ✓ |
| 3 | MgCu2SiTe4 | -0.461 | 0.034 | 0.245 | |
| 3 | SrAg2SnSe4 | -0.896 | 0.052 | 0.340 | |
| 3 | BaCu2SiSe4 | -0.952 | 0.054 | 1.812 | |
| 3 | SrCu2SiSe4 | -0.913 | 0.055 | 1.736 | |
| 3 | BaAg2GeTe4 | -0.682 | 0.059 | 0.203 | |
| 3 | SrSi(AgTe2)2 | -0.610 | 0.067 | 1.894 | |
| 3 | SrAg2GeTe4 | -0.645 | 0.068 | 0.690 | |
| 3 | BaSi(AgTe2)2 | -0.645 | 0.069 | 2.147 | |
| 3 | ZrZn(AgSe2)2 | -0.853 | 0.080 | 1.328 | |
| 3 | SrCu2SnSe4 | -0.902 | 0.083 | 0.105 | |
| 3 | ZrCd(AgSe2)2 | -0.822 | 0.088 | 0.014 | |
| 3 | ZrCd(AgS2)2 | -0.920 | 0.097 | 1.877 | |
| 3 | ZrZn(AgS2)2 | -0.957 | 0.106 | 1.223 | |
| 4 | Cu2AgSbSe4 | -0.396 | 0.000 | 0.056 | |
| 4 | Ag3SbS4 | -0.372 | 0.000 | 0.152 | |
| 4 | Ag3SbSe4 | -0.360 | 0.000 | 1.255 | ✓ |
| 4 | Cu2AgPSe4 | -0.363 | 0.000 | 1.934 | |
| 4 | CuAg2SbSe4 | -0.377 | 0.000 | 0.851 | |
| 4 | CuAg2PSe4 | -0.352 | 0.000 | 1.490 | ✓ |
| 4 | CuAg2SbS4 | -0.409 | 0.007 | 0.455 | |
| 4 | CuAg2AsSe4 | -0.337 | 0.007 | 0.040 | |
| 4 | Cu2AgAsSe4 | -0.356 | 0.007 | 0.040 | |
| 4 | Cu2AgSbS4 | -0.448 | 0.009 | 0.474 | |
| 4 | Cu2AgAsS4 | -0.412 | 0.010 | 1.627 | ✓ |
| 4 | CuAg2AsS4 | -0.372 | 0.012 | 1.560 | ✓ |
| 4 | CuAg2PS4 | -0.458 | 0.014 | 2.421 | |
| 4 | NaCu2PSe4 | -0.563 | 0.018 | 2.072 | |
| 4 | NaCu2AsSe4 | -0.548 | 0.023 | 0.448 | |
| 4 | NaCu2SbSe4 | -0.589 | 0.024 | 0.843 | |
| 4 | NaCu2PS4 | -0.710 | 0.026 | 3.236 | |
| 4 | NaCu2AsS4 | -0.627 | 0.034 | 2.530 | |
| 4 | NaCu2SbS4 | -0.656 | 0.046 | 1.221 | ✓ |
| 4 | Cu3MoS4 | -0.557 | 0.144 | 0.977 | |
| 5 | NaAg2SbSe4 | -0.568 | 0.000 | 0.640 | |
| 5 | Ag3AsSe4 | -0.319 | 0.000 | 0.211 | |
| 5 | NaAg2PS4 | -0.676 | 0.000 | 2.995 | |
| 5 | NaAg2PSe4 | -0.555 | 0.001 | 2.125 | |
| 5 | NaAg2AsSe4 | -0.529 | 0.004 | 1.451 | ✓ |
| 5 | KAg2SbSe4 | -0.601 | 0.005 | 0.879 | |
| 5 | NaAg2AsS4 | -0.569 | 0.007 | 1.650 | ✓ |
| 5 | NaAg2SbS4 | -0.599 | 0.011 | 0.882 | |
| 5 | KAg2AsSe4 | -0.560 | 0.014 | 1.557 | ✓ |
| 5 | KAg2PSe4 | -0.587 | 0.027 | 2.290 | |
| 5 | KAg2AsS4 | -0.590 | 0.030 | 1.914 | |
| 5 | KCu2AsSe4 | -0.577 | 0.035 | 0.558 | |
| 5 | KCu2SbSe4 | -0.616 | 0.036 | 0.906 | |
| 5 | KCu2PSe4 | -0.581 | 0.047 | 1.864 | |
| 5 | KCu2PS4 | -0.719 | 0.056 | 2.888 | |
| 5 | KCu2AsS4 | -0.629 | 0.056 | 2.089 | |
| 5 | KCu2SbS4 | -0.664 | 0.069 | 1.445 | |
| 5 | KCu2BiSe4 | -0.611 | 0.079 | 1.247 | |
| 5 | KCu2BiS4 | -0.658 | 0.101 | 0.425 | |

Search effort as reported in the campaign statistics: proposed/scored per iteration were 39/20, 110/20, 38/20, 49/20 and 24/19. Iteration 2 reports 33 filtered out. Iteration 4 reports 63 filtered out, which exceeds its proposed count of 49. I did not reconcile this.

## Hypotheses tested and what was learned

**Iteration 1: isoelectronic substitution on kesterite Cu₂ZnSnS₄.** The idea was to swap Ag for Cu, Cd/Mg for Zn, Ge/Si for Sn and Se/Te for S to tune the gap near 1.4 eV.
- Only MgAg₂SnSe₄ landed in the window (1.153 eV, Ehull 0.043), which is marginal.
- Near misses were MgAg₂GeS₄ (1.78 eV, Ehull 0.006), MgSi(AgSe₂)₂ (1.84 eV, Ehull 0.011) and ZnSi(AgSe₂)₂ (1.84 eV, Ehull 0.000).
- Se and Te Ag–Ge/Sn compounds had gaps that were too low, and Cd lowered the gap strongly.
- Ca destabilised the structure (Ehull above 0.06).
- The notebook has a reflection but no separate observation entry for this iteration.

**Iteration 2: chalcopyrites (I–III–VI₂) and II–IV–V₂ pnictides.** The notebook states that the chalcopyrite and zincblende ternaries were almost all already in MP.
- The novel II–IV–Sb₂ pnictides (Zn/Cd/Mg with Si/Ge/Sn) all had gaps below 0.95 eV and several were unstable, so this part was **falsified**.
- NaGaS₂ and NaAlS₂ are stable but have gaps above 4 eV.
- Large A-site kesterite-like compounds gave two hits: BaSi(AgSe₂)₂ (1.424 eV, Ehull 0.026) and SrSi(AgSe₂)₂ (1.694 eV, Ehull 0.021).
- Fe and Mn at the divalent site gave tiny gaps and/or instability.
- Sulfide analogues of the Ba/Sr–Ag–Si compounds had gaps of about 2.5 eV.

**Iteration 3: extending the Ba/Sr–Ag–Si–Se hits** (Ge/Sn for Si, Cu for Ag, tellurides, Ti/Zr at the tetravalent site).
- The only hit was SrAg₂SnS₄ (1.667 eV, Ehull 0.024).
- Most Ba/Sr selenide extensions failed on stability (Ehull 0.05–0.08) or gap (below about 0.35 eV for Sn, or about 1.7–1.8 eV for Si and Cu).
- Ba/Sr–Ag tellurides were unstable (Ehull 0.06–0.07).
- ZnSi(AgTe₂)₂ is stable (Ehull 0.001) with a gap of 1.72 eV, just above the window.
- Ti–Zn/Cd–Ag–S/Se compounds are stable but have gaps of 1.9–2.2 eV.
- ZrZn(AgS₂)₂ (1.22 eV) and ZrZn(AgSe₂)₂ (1.33 eV) have in-window gaps but Ehull of 0.08–0.11, so they are unstable.
- Observed trend: Sn lowers the gap strongly, while Si and Ti raise it.

**Iteration 4: I₃–V–VI₄ (famatinite/kesterite-like) compositions.** The planned A-site expansions around SrAg₂SnS₄ had mostly already been tested, so the iteration pivoted. The stated hypothesis (A-site variants of Ag₂SnS₄) therefore differs from what was actually run (Cu/Ag/Na with P/As/Sb). This pivot was productive: five hits.
- CuAg₂PSe₄: 1.49 eV, Ehull 0.000.
- Ag₃SbSe₄: 1.255 eV, Ehull 0.000.
- CuAg₂AsS₄: 1.56 eV, Ehull 0.012.
- Cu₂AgAsS₄: 1.63 eV, Ehull 0.010.
- NaCu₂SbS₄: 1.22 eV, Ehull 0.046 (marginal).
- Misses included Cu₂AgPSe₄ (1.93 eV), CuAg₂PS₄ (2.42 eV) and Cu₂AgSbS₄ (0.47 eV).
- As/Sb selenides mostly had gaps of 0.04–0.85 eV.
- Cu₃MoS₄ was unstable (Ehull 0.144).
- Gap trend: P > As > Sb and S > Se.

**Iteration 5: refining the I₃–V–VI₄ hits** with alkali–Ag₂–pnictogen chalcogenides.
- Three hits: NaAg₂AsSe₄ (1.451 eV, Ehull 0.004), KAg₂AsSe₄ (1.557 eV, Ehull 0.014) and NaAg₂AsS₄ (1.65 eV, Ehull 0.007).
- As gave in-window gaps, P gave gaps that were too wide (2.1–3.0 eV), and Sb gave gaps that were too narrow (0.64–0.88 eV).
- Ag-based alkali compounds were stable. K–Cu analogues were mostly unstable (Ehull 0.035–0.10) or off-window.
- KCu₂SbS₄ (1.445 eV) has Ehull 0.069 and KCu₂BiSe₄ (1.25 eV) has Ehull 0.079, so neither counts as a hit.

## Caveats

- **Surrogate accuracy.** Gaps are from a CHGNet-HSE-style surrogate and Ehull values are surrogate-based, so error bars are unquantified here. The notebook itself flags noise. Ag₃SbS₄ is predicted at 0.15 eV while Ag₃SbSe₄ is predicted at 1.26 eV, the opposite of the expected S > Se ordering. Some gaps also jump sharply between close compositions (CuAg₂PSe₄ at 1.49 eV against CuAg₂AsSe₄ at 0.04 eV). Gap-based rankings should be treated as hypotheses.
- **Window edges.** MgAg₂SnSe₄ (1.153 eV, Ehull 0.043) and NaCu₂SbS₄ (1.22 eV, Ehull 0.046) sit at the edge of the stability cutoff. An Ehull of up to 0.05 eV/atom does not imply synthesisability.
- **Novelty.** "Novel" here means absent from the MP database, not absent from the literature. Notebook comments note some related known compounds (e.g. BaAg₂GeSe₄ is known). A full literature check is still needed for each hit.
- **Structure assumptions.** Candidates were generated by substitution into prototype structures. Alternative polymorphs, cation ordering and competing phases were not explored.
- **No other properties.** Absorption coefficient, band-gap type (direct or indirect), defect tolerance, carrier transport and toxicity were not assessed. Ag, Sb and As-containing compounds raise cost and toxicity questions.
- **Validation needed for top candidates:** CuAg₂PSe₄, NaAg₂AsSe₄, KAg₂AsSe₄, NaAg₂AsS₄, Ag₃SbSe₄, BaSi(AgSe₂)₂, SrSi(AgSe₂)₂ and SrAg₂SnS₄.
  - Hybrid-functional (HSE) or GW gap calculations.
  - Convex-hull re-evaluation with DFT, including competing phases and phonon stability.
  - Band-gap type and optical absorption calculations.
  - Synthesis and measurement.

## Recommended next steps

1. Run DFT (PBE relaxation plus HSE or GW) on the 12 hits, prioritising the near-1.4 eV, low-Ehull members: CuAg₂PSe₄, NaAg₂AsSe₄, KAg₂AsSe₄ and BaSi(AgSe₂)₂.
2. Check the surrogate's reliability by comparing it with DFT for the anomalous cases (Ag₃SbS₄ vs Ag₃SbSe₄, As vs P selenides).
3. Do a targeted literature and database check on the shortlisted formulas to confirm novelty beyond MP.
4. Extend the productive alkali–Ag₂–As–chalcogenide family as the notebook suggests: Rb and Cs analogues, and mixed Na/K or mixed-anion variants (Li is not in the palette). This is a suggestion from the notebook, not a tested result.
5. Deprioritise the lines that stalled or were falsified: II–IV–Sb₂ pnictides, Ca- and Fe/Mn-containing kesterites, Ba/Sr–Ag tellurides, K–Cu I₃–V–VI₄ compounds, and Zr-based variants (unstable despite in-window gaps).
