# Campaign report: pv-absorber-v1

## Executive summary

Over five iterations (94 scored candidates; 93 novel relative to Materials Project, plus one known calibration compound), the campaign searched kesterite-derived chalcogenides for stable compounds with band gaps near 1.4 eV. The notebook worked to a 1.1–1.7 eV window with E_hull ≤ 0.05 eV/atom. By that screen, 19 novel candidates qualify. These fall into three families: Ag-selenide kesterites (iterations 1–2), alkali/alkaline-earth telluride kesterites (iterations 4–5), and the I-V-VI2 compound KBiTe2 (iteration 4).

- **Closest to 1.4 eV:** K2CaGeTe4 (gap 1.42 eV, E_hull 0.019) and Na2CdSnTe4 (1.37 eV, E_hull 0.032).
- **Other notable hits:** CdAg2GeSe4 (1.28 eV, E_hull 0.000) and KBiTe2 (1.30 eV, E_hull 0.003).
- **Confidence:** low to moderate. Every number comes from CHGNet relaxation plus an ML band-gap predictor, with no DFT or experimental confirmation. Several structure assumptions are doubtful, listed in the caveats below.

## Scored candidates

Columns: E_form is formation energy per atom (eV), E_hull is energy above hull (eV/atom), and Gap is the predicted band gap (eV). All entries converged. All are flagged novel except SrCu2SnS4, which is known and was run as a calibration point. Values are rounded.

| Formula | Iter | E_form | E_hull | Gap |
|---|---|---|---|---|
| ZnAg2GeSe4 | 1 | -0.681 | 0.000 | 1.119 |
| CdAg2GeSe4 | 1 | -0.657 | 0.000 | 1.279 |
| MgAg2SnS4 | 1 | -1.177 | 0.002 | 1.871 |
| MgAg2SnSe4 | 1 | -0.838 | 0.016 | 1.588 |
| MgAg2GeS4 | 1 | -1.165 | 0.017 | 1.893 |
| MgCu2SnS4 | 1 | -1.239 | 0.020 | 2.174 |
| MgAg2GeSe4 | 1 | -0.797 | 0.020 | 1.856 |
| CdAg2SnTe4 | 1 | -0.366 | 0.027 | 0.412 |
| ZnAg2GeTe4 | 1 | -0.318 | 0.028 | 1.171 |
| MgAg2SnTe4 | 1 | -0.461 | 0.038 | 1.172 |
| ZnAg2SnTe4 | 1 | -0.358 | 0.039 | 0.596 |
| MgCu2SnSe4 | 1 | -0.819 | 0.071 | 1.383 |
| MgCu2GeTe4 | 1 | -0.372 | 0.101 | 0.895 |
| MgCu2SnTe4 | 1 | -0.409 | 0.109 | 0.483 |
| CdSi(AgSe2)2 | 1 | -0.568 | 0.130 | 1.714 |
| MgCu2GeSe4 | 1 | -0.717 | 0.136 | 1.102 |
| CdSi(AgS2)2 | 1 | -0.937 | 0.152 | 2.751 |
| ZnSi(AgSe2)2 | 1 | -0.553 | 0.170 | 1.904 |
| SrAg2SnSe4 | 2 | -1.059 | 0.000 | 1.701 |
| NiAg2SnSe4 | 2 | -0.631 | 0.000 | 1.676 |
| BaCu2SnTe4 | 2 | -0.754 | 0.000 | 0.139 |
| NiAg2GeSe4 | 2 | -0.583 | 0.0005 | 1.648 |
| SrAg2GeSe4 | 2 | -1.021 | 0.003 | 1.687 |
| BaCu2GeTe4 | 2 | -0.672 | 0.034 | 0.499 |
| CaAg2SnSe4 | 2 | -0.998 | 0.051 | 1.816 |
| CoAg2SnSe4 | 2 | -0.569 | 0.056 | 0.603 |
| CaAg2GeSe4 | 2 | -0.949 | 0.062 | 1.679 |
| FeAg2SnSe4 | 2 | -0.579 | 0.072 | -0.003 |
| CoAg2GeSe4 | 2 | -0.524 | 0.075 | 0.809 |
| FeAg2GeSe4 | 2 | -0.525 | 0.078 | 0.018 |
| CuBiTe2 | 2 | -0.247 | 0.093 | 0.631 |
| SrTi(AgSe2)2 | 2 | -0.938 | 0.373 | 2.357 |
| TiMn(AgSe2)2 | 2 | -0.492 | 0.395 | 2.207 |
| CaTi(AgSe2)2 | 2 | -0.864 | 0.438 | 2.723 |
| SrZr(AgSe2)2 | 2 | -0.944 | 0.440 | 2.331 |
| TiCo(AgSe2)2 | 2 | -0.438 | 0.450 | 2.037 |
| TiFe(AgSe2)2 | 2 | -0.427 | 0.487 | 0.146 |
| CaZr(AgSe2)2 | 2 | -0.882 | 0.493 | 2.471 |
| BaAg2GeTe4 | 3 | -0.704 | 0.000 | 0.705 |
| SrAg2SnS4 | 3 | -1.369 | 0.000 | 1.720 |
| SrCu2SnS4 (known; calibration) | 3 | -1.450 | 0.000 | 2.754 |
| BaAg2SnTe4 | 3 | -0.746 | 0.007 | 0.516 |
| SrAg2GeS4 | 3 | -1.354 | 0.013 | 1.867 |
| SrAg2GeTe4 | 3 | -0.651 | 0.016 | 0.155 |
| SrAg2SnTe4 | 3 | -0.689 | 0.029 | 0.100 |
| NiAg2GeTe4 | 3 | -0.281 | 0.036 | 0.126 |
| Cu2NiGeSe4 | 3 | -0.577 | 0.041 | 0.255 |
| NiAg2SnTe4 | 3 | -0.323 | 0.045 | 0.039 |
| SrCu2SnSe4 | 3 | -1.045 | 0.050 | 1.109 |
| CaAg2GeTe4 | 3 | -0.587 | 0.058 | 0.240 |
| CaAg2SnTe4 | 3 | -0.625 | 0.072 | 0.062 |
| CaCu2SnS4 | 3 | -1.371 | 0.072 | 2.704 |
| CaCu2GeS4 | 3 | -1.340 | 0.096 | 2.563 |
| CaCu2SnSe4 | 3 | -0.979 | 0.108 | 0.944 |
| CaCu2GeSe4 | 3 | -0.928 | 0.121 | 1.198 |
| K2ZnSnSe4 | 4 | -1.222 | 0.000 | 2.265 |
| K2CdGeSe4 | 4 | -1.169 | 0.000 | 2.409 |
| K2CdSnTe4 | 4 | -0.899 | 0.000 | 0.864 |
| K2ZnSnTe4 | 4 | -1.001 | 0.000 | 1.573 |
| KSbTe2 | 4 | -0.741 | 0.000 | 0.547 |
| NaGaS2 | 4 | -1.810 | 0.000 | 3.827 |
| NaAlS2 | 4 | -2.075 | 0.000 | 4.647 |
| KAlS2 | 4 | -1.717 | 0.000 | 3.059 |
| K2CdGeTe4 | 4 | -0.863 | 0.000 | 0.884 |
| K2ZnGeTe4 | 4 | -0.902 | 0.000 | 1.896 |
| KBiTe2 | 4 | -0.736 | 0.003 | 1.296 |
| Na2ZnSnSe4 | 4 | -1.121 | 0.007 | 2.292 |
| Na2ZnGeSe4 | 4 | -1.094 | 0.011 | 2.480 |
| Na2CdSnSe4 | 4 | -1.085 | 0.019 | 1.957 |
| Na2CdGeTe4 | 4 | -0.680 | 0.021 | 1.739 |
| Na2ZnSnTe4 | 4 | -0.712 | 0.023 | 2.053 |
| Na2CdGeSe4 | 4 | -1.052 | 0.029 | 2.413 |
| Na2CdSnTe4 | 4 | -0.699 | 0.032 | 1.367 |
| Na2MgSnSe4 | 4 | -1.209 | 0.055 | 2.156 |
| MnAg2GeS4 | 4 | -0.914 | 0.079 | 2.236 |
| Na2CaGeTe4 | 5 | -1.098 | 0.000 | 1.731 |
| K2MnSnTe4 | 5 | -0.932 | 0.000 | 0.646 |
| K2ZnSiTe4 | 5 | -0.802 | 0.000 | 2.069 |
| K2CdSiTe4 | 5 | -0.798 | 0.000 | 1.235 |
| K2BaGeTe4 | 5 | -1.187 | 0.000 | 1.566 |
| K2BaSiTe4 | 5 | -1.122 | 0.000 | 1.642 |
| K2MnGeTe4 | 5 | -0.709 | 0.002 | 1.100 |
| K2SrSnTe4 | 5 | -1.128 | 0.012 | 1.199 |
| K2SrGeTe4 | 5 | -1.087 | 0.013 | 1.216 |
| K2CaGeTe4 | 5 | -1.059 | 0.019 | 1.421 |
| K2CaSnTe4 | 5 | -1.085 | 0.033 | 1.118 |
| Na2MnGeTe4 | 5 | -0.588 | 0.043 | 1.088 |
| K2MnSiTe4 | 5 | -0.694 | 0.045 | 1.455 |
| Na2MnSnTe4 | 5 | -0.618 | 0.046 | 0.947 |
| Na2ZnSiTe4 | 5 | -0.615 | 0.094 | 2.791 |
| K2SrSiTe4 | 5 | -0.987 | 0.105 | 1.875 |
| Na2CdSiTe4 | 5 | -0.600 | 0.105 | 1.796 |
| Na2MnSiTe4 | 5 | -0.506 | 0.165 | 2.035 |
| Na2CaSnTe4 | 5 | -0.865 | 0.169 | 1.458 |

### Candidates meeting the screen (gap 1.1–1.7 eV, E_hull ≤ 0.05 eV/atom)

Computed from the table above:

- **Iteration 1:**
  - ZnAg2GeSe4
  - CdAg2GeSe4
  - MgAg2SnSe4
  - ZnAg2GeTe4
  - MgAg2SnTe4
- **Iteration 2:**
  - SrAg2GeSe4
  - NiAg2GeSe4
  - NiAg2SnSe4
- **Iteration 4:**
  - Na2CdSnTe4
  - K2ZnSnTe4
  - KBiTe2
- **Iteration 5:**
  - K2CaGeTe4 (1.421 eV, E_hull 0.019)
  - K2CaSnTe4
  - K2SrGeTe4
  - K2SrSnTe4
  - K2BaGeTe4
  - K2BaSiTe4
  - K2CdSiTe4
  - K2MnSiTe4

Marginal cases:
- SrCu2SnSe4 has E_hull 0.0504, just over the cut-off, and a gap of 1.109 eV.
- K2MnGeTe4 has a gap of 1.0996 eV, just under the cut-off, and E_hull 0.002.
- SrAg2SnSe4 (1.701 eV, E_hull 0.000) and SrAg2SnS4 (1.720 eV, E_hull 0.000) are stable but sit just above 1.7 eV.
- Na2CaSnTe4 (1.458 eV) has E_hull 0.169, so it fails on stability.

## Hypotheses tested and what was learned

**Iteration 1: isoelectronic substitution on kesterite (Ag for Cu, Cd/Mg/Zn for Zn, Ge/Si/Sn for Sn, S/Se/Te mixes).**
- Supported for Ag2-M-(Ge,Sn)-Se4, which gave five hits at 1.1–1.6 eV.
- Sulfides were too wide, at 1.9–2.2 eV in the cases evaluated (excluding the unstable Si compounds). Cu tellurides were too narrow or unstable.
- Si compounds were unstable (E_hull > 0.13).
- MgCu2SnSe4 had a gap of 1.38 eV but E_hull of 0.071.

**Iteration 2: extend Ag2-M-IV-Se4 to Ca, Sr, Fe, Co, Ni, plus Ti/Zr on the IV site.** (Notebook notes also record mixed-anion substitution as unsupported by the tool, and the chalcopyrite and zincblende proposals as nearly all known.)
- Only partly supported: SrAg2GeSe4, NiAg2GeSe4 and NiAg2SnSe4 are hits, but all sit at the upper edge (1.65–1.69 eV).
- Fe and Co analogues were metallic or small-gap and unstable.
- Ti/Zr on the IV site was very unstable (E_hull 0.37–0.49).
- Ba-Cu tellurides were stable or near-stable but too narrow (0.14–0.50 eV).
- CuBiTe2 was unstable.

**Iteration 3: tellurides with large M cations, and Cu/Ag sulfides, to reach ~1.4 eV.**
- Falsified for the tellurides. Sr/Ca/Ni Ag tellurides had gaps of about 0.04–0.24 eV, and Ba tellurides 0.52–0.71 eV.
- The only borderline new hit was SrCu2SnSe4 (E_hull 0.0504, gap 1.109 eV).
- Cu sulfides with Ca were unstable.
- SrCu2SnS4 was run as a known calibration point and returned a gap of 2.75 eV.
- Empirical gap ordering across the iteration 1–3 families: Cu-S (~2.7) > Ag-S (1.7–1.9) > Ag-Se (1.1–1.7) > Cu-Se (~1.1) > Te (<0.7, apart from the Zn/Mg Ag tellurides ~1.17).
- No single substitution gave a gap near 1.4 eV in that space.

**Iteration 4: switch family to alkali (Na, K) kesterites A2-M-IV-X4 and alkali I-V-VI2 / I-III-VI2 compounds.**
- Productive. Na2CdSnTe4, K2ZnSnTe4 and KBiTe2 were hits.
- Alkali selenides were stable but wide (about 1.96–2.5 eV).
- K2CdSnTe4 and K2CdGeTe4 were stable but too narrow (about 0.86–0.88 eV).
- KSbTe2 was too narrow (0.55 eV). NaGaS2, NaAlS2 and KAlS2 were very wide (3.1–4.6 eV).

**Iteration 5: alkali/alkaline-earth/Mn tellurides in the kesterite prototype.**
- Strongly supported, with eight hits including K2CaGeTe4 (1.42 eV).
- Observed trends:
  - K stabilizes large-M compounds relative to Na.
  - Gaps for Ge compounds are larger than for Sn, by about 0.1–0.3 eV.
  - For K2MGeTe4, the gap rises from Sr to Ba (1.22 to 1.57 eV). Ca (1.42) does not follow that order.
- Misses:
  - Na-Si compounds were unstable.
  - K2SrSiTe4 was unstable.
  - K2MnSnTe4 had a gap of 0.65 eV.
  - Na2CaSnTe4 had E_hull 0.169.

## Caveats

- **Method limits.** Stabilities come from CHGNet relaxations, and gaps are ML predictions at "HSE fidelity". No DFT or experimental validation was done, so the error bars are unquantified. Gap errors of a few tenths of an eV would change which candidates fall in the window. The 0.05 eV/atom stability cutoff is also within plausible CHGNet error.
- **Novelty is relative to Materials Project only.** The literature searches did not find direct data on these families.
- **Structure assumption.** Every candidate was relaxed from a substituted prototype. For large cations (Ca, Sr, Ba on the M site, and the alkali-containing compounds generally), the true ground state may be a different structure type. The notebook flags this for K2AeMTe4. The reported E_hull values would then be misleading.
- **Ni, Mn, Fe and Co compounds.** Ni2+ gaps are flagged in the notebook as likely unreliable (d8 and ligand-field effects). Mn (d5) results carry similar doubts. The notebook does not state that metallic or near-zero gaps for Fe and Co compounds are artefacts, but the same d-electron concerns apply.
- **Properties not assessed.** Direct or indirect nature of the gap, absorption coefficient, defect tolerance, carrier transport, and chemical and air stability. Several top candidates contain Cd, and the alkali tellurides are likely moisture-sensitive (a general expectation, not a campaign result).
- **Relaxation budget.** In iteration 1, two relaxations were left unspent (18 evaluated). Some proposals were filtered out as known or unsupported, so coverage of the families is incomplete.

## Recommended next steps

1. Run DFT validation, with hybrid-functional gaps, on the leading candidates: K2CaGeTe4, Na2CdSnTe4, K2CdSiTe4, K2SrGeTe4, K2SrSnTe4, K2BaGeTe4, CdAg2GeSe4, ZnAg2GeSe4 and KBiTe2.
2. Check competing polymorphs and decomposition products for the alkali/alkaline-earth tellurides, including a full convex-hull analysis with non-kesterite structure types.
3. Fine-tune gaps by alloying, for example Ca/Sr or Ge/Sn mixes. The propose tool could not do this directly, so it needs custom supercells.
4. Treat Ni, Mn, Fe and Co results with caution until checked with spin-polarized, higher-level calculations.
5. Compute absorption spectra and defect energetics for the best candidates. If a candidate survives, assess synthesizability, including handling of air-sensitive tellurides.
6. Avoid the unproductive regions found here: Si-based Ag/Cu kesterites, Ti/Zr on the IV site, Ca-Cu/Ag compounds, Sr/Ca/Ni Ag tellurides, and Cu and alkali sulfides.
