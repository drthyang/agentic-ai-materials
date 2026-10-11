# Campaign report: pv-absorber-v1

## Executive summary

The campaign ran five iterations and scored 91 novel, converged candidates. The target was a band gap near 1.4 eV with a low energy above hull. By the notebook's working criterion (gap 1.1–1.7 eV, E_hull ≤ 0.05 eV/atom), 15 candidates qualify. They fall into two families: Ag-based Ge/Sn kesterite-type selenides and tellurides, and alkali/alkaline-earth Ge/Sn tellurides. The closest to 1.4 eV are K2CaGeTe4 (1.42 eV, E_hull 0.019) and Na2CdSnTe4 (1.37 eV, E_hull 0.032). All numbers come from a CHGNet relaxation and an ML "HSE-fidelity" gap surrogate on hypothetical kesterite-type structures, with no DFT or experimental check. Confidence in any individual candidate is therefore low. Many of the alkali tellurides probably do not adopt the kesterite-type structure in reality.

## Scored candidates

All candidates are novel versus the Materials Project and converged. E_f is the formation energy per atom (eV), E_hull is in eV/atom, and the gap is in eV. ✓ marks candidates meeting the working criterion (gap 1.1–1.7 eV and E_hull ≤ 0.05).

### Iteration 1 (Ag/Cu kesterite-type, Mg/Zn/Cd, Si/Ge/Sn, S/Se/Te)

| Formula | E_f | E_hull | Gap | Hit |
|---|---|---|---|---|
| CdAg2GeSe4 | -0.657 | 0.000 | 1.28 | ✓ |
| ZnAg2GeSe4 | -0.681 | 0.000 | 1.12 | ✓ |
| MgAg2SnS4 | -1.177 | 0.002 | 1.87 | |
| MgAg2SnSe4 | -0.838 | 0.016 | 1.59 | ✓ |
| CdAg2GeTe4 | -0.326 | 0.017 | 0.48 | |
| MgAg2GeS4 | -1.165 | 0.017 | 1.89 | |
| MgAg2GeSe4 | -0.797 | 0.020 | 1.86 | |
| MgAg2GeTe4 | -0.423 | 0.025 | 1.49 | ✓ |
| CdAg2SnTe4 | -0.366 | 0.027 | 0.41 | |
| ZnAg2GeTe4 | -0.318 | 0.028 | 1.17 | ✓ |
| MgAg2SnTe4 | -0.461 | 0.038 | 1.17 | ✓ |
| ZnAg2SnTe4 | -0.358 | 0.039 | 0.60 | |
| CdSi(AgSe2)2 | -0.568 | 0.130 | 1.71 | |
| MgCu2GeSe4 | -0.717 | 0.136 | 1.10 | |
| MgSi(AgSe2)2 | -0.715 | 0.145 | 2.35 | |
| CdSi(AgS2)2 | -0.937 | 0.152 | 2.75 | |
| MgSi(AgS2)2 | -1.132 | 0.167 | 2.54 | |

### Iteration 2 (Ca/Sr/Ba Ag- and Cu-kesterite-type)

| Formula | E_f | E_hull | Gap | Hit |
|---|---|---|---|---|
| SrAg2SnSe4 | -1.059 | 0.000 | 1.70 | (borderline: 1.701, just above window) |
| SrAg2SnS4 | -1.369 | 0.000 | 1.72 | |
| BaAg2GeTe4 | -0.704 | 0.000 | 0.70 | |
| SrAg2GeSe4 | -1.021 | 0.003 | 1.69 | ✓ (borderline) |
| BaAg2SnTe4 | -0.746 | 0.007 | 0.52 | |
| SrAg2GeS4 | -1.354 | 0.013 | 1.87 | |
| SrAg2GeTe4 | -0.651 | 0.016 | 0.16 | |
| SrAg2SnTe4 | -0.689 | 0.029 | 0.10 | |
| SrCu2SnSe4 | -1.045 | 0.050 | 1.11 | (marginal: E_hull 0.0504) |
| CaAg2SnSe4 | -0.998 | 0.051 | 1.82 | |
| CaAg2GeTe4 | -0.587 | 0.058 | 0.24 | |
| CaAg2GeSe4 | -0.949 | 0.062 | 1.68 | |
| CaAg2SnS4 | -1.297 | 0.068 | 2.28 | |
| CaAg2SnTe4 | -0.625 | 0.072 | 0.06 | |
| CaCu2SnS4 | -1.371 | 0.072 | 2.70 | |
| CaAg2GeS4 | -1.273 | 0.094 | 2.15 | |
| CaCu2GeS4 | -1.340 | 0.096 | 2.56 | |
| CaCu2SnSe4 | -0.979 | 0.108 | 0.94 | |
| CaCu2GeSe4 | -0.928 | 0.121 | 1.20 | |

### Iteration 3 (Zr/Ti, Mn/Fe, Na2-type; no hits)

| Formula | E_f | E_hull | Gap | Hit |
|---|---|---|---|---|
| ZrZn(AgSe2)2 | -1.183 | 0.000 | 0.65 | |
| ZrCd(AgSe2)2 | -1.148 | 0.000 | 0.30 | |
| ZrZn(AgS2)2 | -1.543 | 0.000 | 0.19 | |
| ZrMn(AgSe2)2 | -1.127 | 0.000 | ~0.00 | |
| MgZr(AgS2)2 | -1.666 | 0.000 | 0.33 | |
| ZrZn(CuSe2)2 | -1.188 | 0.000 | 0.21 | |
| ZrZn(CuS2)2 | -1.556 | 0.000 | 0.30 | |
| MgZr(CuSe2)2 | -1.276 | 0.000 | 0.19 | |
| MgZr(CuS2)2 | -1.709 | 0.000 | 0.18 | |
| Na2MgZrS4 | -2.107 | 0.000 | 3.88 | |
| FeAg2SnSe4 | -0.579 | 0.072 | -0.003 | |
| FeAg2GeSe4 | -0.525 | 0.078 | 0.02 | |
| MnAg2GeS4 | -0.914 | 0.079 | 2.24 | |
| FeAg2GeS4 | -0.851 | 0.135 | 0.01 | |
| CaZr(AgS2)2 | -1.487 | 0.293 | 2.74 | |
| TiZn(AgSe2)2 | -0.617 | 0.353 | 2.23 | |
| MgZr(AgSe2)2 | -0.720 | 0.459 | 1.58 | (in-window gap, but E_hull far too high) |
| CaZr(AgSe2)2 | -0.882 | 0.493 | 2.47 | |
| Na2ZrZnSe4 | -0.988 | 0.502 | 2.57 | |
| Na2MgZrSe4 | -1.082 | 0.543 | 2.39 | |

### Iteration 4 (Na/K I2-II-IV-VI4 kesterite-type)

| Formula | E_f | E_hull | Gap | Hit |
|---|---|---|---|---|
| K2ZnSnSe4 | -1.222 | 0.000 | 2.26 | |
| K2ZnSnTe4 | -1.001 | 0.000 | 1.57 | ✓ |
| K2CdSnTe4 | -0.899 | 0.000 | 0.86 | |
| K2CdGeSe4 | -1.169 | 0.000 | 2.41 | |
| K2CdGeTe4 | -0.863 | 0.000 | 0.88 | |
| K2MgSnTe4 | -0.977 | 0.000 | 1.33 | ✓ |
| K2ZnGeSe4 | -1.197 | 0.000 | 2.49 | |
| K2ZnGeTe4 | -0.902 | 0.000 | 1.90 | |
| Na2ZnSnSe4 | -1.121 | 0.007 | 2.29 | |
| Na2ZnGeSe4 | -1.094 | 0.011 | 2.48 | |
| Na2ZnGeTe4 | -0.690 | 0.015 | 2.42 | |
| Na2CdSnSe4 | -1.085 | 0.019 | 1.96 | |
| Na2CdGeTe4 | -0.680 | 0.021 | 1.74 | |
| Na2ZnSnTe4 | -0.712 | 0.023 | 2.05 | |
| Na2CdGeSe4 | -1.052 | 0.029 | 2.41 | |
| K2MgSnSe4 | -1.311 | 0.030 | 2.54 | |
| Na2CdSnTe4 | -0.699 | 0.032 | 1.37 | ✓ |
| Na2MgGeSe4 | -1.186 | 0.055 | 2.45 | |
| Na2MgSnSe4 | -1.209 | 0.055 | 2.16 | |
| Na2MgSnTe4 | -0.782 | 0.055 | 1.93 | |

### Iteration 5 (Na/K with Ca/Sr/Ba/Mn, Ge/Sn tellurides)

| Formula | E_f | E_hull | Gap | Hit |
|---|---|---|---|---|
| Na2CaGeTe4 | -1.098 | 0.000 | 1.73 | |
| K2MnSnTe4 | -0.932 | 0.000 | 0.65 | |
| K2BaGeTe4 | -1.187 | 0.000 | 1.57 | ✓ |
| K2MnGeTe4 | -0.709 | 0.002 | 1.10 | (near miss: 1.0997) |
| K2SrSnTe4 | -1.128 | 0.012 | 1.20 | ✓ |
| K2SrGeTe4 | -1.087 | 0.013 | 1.22 | ✓ |
| K2CaGeTe4 | -1.059 | 0.019 | 1.42 | ✓ |
| K2CaSnTe4 | -1.085 | 0.033 | 1.12 | ✓ |
| Na2MnGeTe4 | -0.588 | 0.043 | 1.09 | (near miss) |
| Na2MnSnTe4 | -0.618 | 0.046 | 0.95 | |
| BaNa2GeTe4 | -0.978 | 0.063 | 1.76 | |
| BaNa2SnTe4 | -1.004 | 0.066 | 1.70 | |
| Na2SrGeTe4 | -0.913 | 0.113 | 1.69 | |
| Na2SrSnTe4 | -0.933 | 0.124 | 1.73 | |
| Na2CaSnTe4 | -0.865 | 0.169 | 1.46 | (in-window gap, but unstable) |

## Hypotheses tested and what was learned

**Iteration 1: Ag-based kesterite substitutions (supported).** The hypothesis was that isoelectronic substitution on kesterite (Cu→Ag, Zn→Cd/Mg, Sn→Ge/Si, S→Se) would tune the gap near 1.4 eV.
- Six hits came out of 17 evaluated: CdAg2GeSe4, ZnAg2GeSe4, MgAg2SnSe4, MgAg2GeTe4, MgAg2SnTe4 and ZnAg2GeTe4.
- Si compounds were strongly unstable (E_hull > 0.13).
- Cd tellurides had gaps of only 0.4–0.5 eV.
- Mg sulfides and selenides had gaps of 1.86–1.89 eV, too wide.
- The substitution tool applies replacements simultaneously, so Cu and Ag were never mixed.

**Iteration 2: Ca/Sr/Ba on the divalent site, plus Cu analogs (partly supported).**
- Sr was the best alkaline-earth cation. SrAg2GeSe4 (E_hull 0.003, 1.69 eV) is a borderline hit. SrAg2SnSe4 and SrAg2SnS4 are stable but sit just above the window (1.70 and 1.72 eV).
- Ca analogs were unstable (E_hull 0.05–0.12).
- Sr and Ba tellurides had gaps of 0.1–0.7 eV, too small.
- SrCu2SnSe4 (E_hull 0.0504, 1.11 eV) is marginal on stability.
- The chalcopyrite batch was nearly all already known and was not evaluated.

**Iteration 3: Zr/Ti, Mn/Fe and Na2-type variants (falsified).** No hits.
- Compounds with Zr on the IV site were stable (E_hull 0) but had gaps of 0–0.65 eV.
- The one in-window Zr compound, MgZr(AgSe2)2, has E_hull 0.46.
- Fe compounds were metallic-like and unstable.
- The II-IV-V2 and I-III-VI2 families were almost entirely known or rejected by the filters, so nothing was evaluated there.
- The notebook flags the small-gap, E_hull = 0 Zr results as suspicious. Tetrahedral Zr⁴⁺ is chemically implausible, and the hull may lack competing phases.

**Iteration 4: alkali (Na/K) I2-II-IV-VI4 tellurides (supported).**
- The zincblende prototype gave only binaries, so nothing was evaluated from it.
- Three hits came out of 20 evaluated: K2ZnSnTe4 (1.57 eV), K2MgSnTe4 (1.33 eV) and Na2CdSnTe4 (1.37 eV). The two K compounds have E_hull of 0.
- All selenides had gaps of 1.96–2.54 eV, too wide.

**Iteration 5: alkali plus Ca/Sr/Ba/Mn, Ge/Sn tellurides (supported).**
- Five hits came out of 15 evaluated: K2CaGeTe4, K2SrSnTe4, K2SrGeTe4, K2BaGeTe4 and K2CaSnTe4.
- K is a better host than Na for large alkaline-earth cations. The Na–Sr, Na–Ba and Na2CaSnTe4 compounds are unstable (E_hull 0.06–0.17).
- The notebook records that K2BaSnTe4 is already known and was skipped, and that 5 of the relaxation budget went unspent because no further novel family members could be proposed.

## Caveats

- **Surrogate error.** E_hull comes from CHGNet relaxations, and gaps come from an ML model claimed to be HSE-fidelity. No error bars were computed. Gap differences of a few tenths of an eV (for example 1.69 vs 1.70 eV at the window edge) are not meaningful at this fidelity.
- **Structure realism.** Every candidate was relaxed in a kesterite-type prototype. The notebook notes that real Sr, K and alkali compounds in these chemistries likely adopt other structure types (for example the K2CdSnSe4 and K2BaSnTe4 types). An E_hull of 0 against the available hull therefore does not prove stability.
- **Hull completeness.** The Zr results suggest the reference hull may be missing competing phases.
- **Novelty.** "Novel" means only that the composition is absent from the Materials Project. Literature searches found nothing specific on these families, but this is not an exhaustive prior-art check.
- **Practical issues not assessed:** toxicity (Cd), air stability of alkali tellurides, defect tolerance, and magnetism for Mn/Fe compounds.

## Recommended next steps

1. Run DFT (PBE relaxation plus HSE or GW gaps) on the top candidates. These are K2CaGeTe4, Na2CdSnTe4, K2MgSnTe4, K2SrSnTe4, K2SrGeTe4, CdAg2GeSe4, ZnAg2GeSe4, MgAg2GeTe4 and MgAg2SnSe4.
2. Run structure searches (or compare against known K–AE–Ge/Sn–Te structure types) for the alkali tellurides. Check phonon and dynamical stability, and compare against competing binary and ternary phases.
3. Compute optical absorption and defect and carrier properties for any that survive. Test synthesizability and air stability.
4. Treat Zr/Ti, Fe/Mn Ag, Ca–Cu and Si-containing kesterites as low priority, since the campaign found them unstable or poorly gapped.
5. Explore Cu/Ag or S/Se/Te mixing on single sites with a different generation tool, since the current tool cannot mix elements at one site. This could tune the Sr–Ag selenides (gap about 1.7 eV) and the K–Cd tellurides (gap about 0.9 eV) toward 1.4 eV.
