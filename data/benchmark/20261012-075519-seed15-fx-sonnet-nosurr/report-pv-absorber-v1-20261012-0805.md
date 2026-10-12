# Campaign report: pv-absorber-v1

## Executive summary

Over five iterations, 98 novel candidates (all flagged as absent from the Materials Project) were scored. The target was a band gap of roughly 1.1–1.7 eV. The notebook treated Ehull up to about 0.05 eV/atom as near-stable. Six candidates met both criteria. Four are alkali-telluride kesterite-type compounds: Na2CdSnTe4, Na2ZnGeTe4, K2ZnSnTe4 and K2ZrCdTe4. Two are Ag-kesterites: MgAg2SnSe4 and MgSi(AgTe2)2. Na2CdSnTe4 is the strongest candidate, with Ehull = 0.000 and Eg = 1.17 eV. K2ZrCdTe4 has the gap closest to the 1.4 eV mid-window (1.375 eV) but Ehull = 0.037 eV/atom. All gaps and Ehull values are surrogate-model outputs with no DFT, hybrid-functional or experimental check. Confidence in any individual candidate is therefore low to moderate. The results are best read as a shortlist for verification.

## Scored candidates

All 98 were reported as novel versus the Materials Project and converged. E_f is the formation energy per atom (eV), Ehull is energy above hull (eV/atom), and Eg is the predicted band gap (eV). Rows are in the database order (by Ehull within each iteration).

**Candidates meeting the notebook's hit criteria (Eg 1.1–1.7 eV, Ehull ≲ 0.05):**

| Iter | Formula | E_f | Ehull | Eg |
|---|---|---|---|---|
| 1 | MgAg2SnSe4 | -0.700 | 0.043 | 1.15 |
| 1 | MgSi(AgTe2)2 | -0.447 | 0.014 | 1.63 |
| 3 | Na2CdSnTe4 | -0.778 | 0.000 | 1.17 |
| 3 | Na2ZnGeTe4 | -0.711 | 0.040 | 1.47 |
| 4 | K2ZnSnTe4 | -0.826 | 0.039 | 1.49 |
| 5 | K2ZrCdTe4 | -1.051 | 0.037 | 1.38 |

**Full results:**

### Iteration 1 (Ag/Cu kesterites)
| Formula | E_f | Ehull | Eg |
|---|---|---|---|
| CdAg2GeSe4 | -0.551 | 0.000 | 0.03 |
| CdSi(AgSe2)2 | -0.599 | 0.000 | 0.75 |
| ZnSi(AgSe2)2 | -0.614 | 0.000 | 1.84 |
| CdSi(AgS2)2 | -0.721 | 0.000 | 2.22 |
| ZnSi(AgTe2)2 | -0.355 | 0.001 | 1.72 |
| ZnAg2GeSe4 | -0.567 | 0.003 | 0.68 |
| MgAg2GeS4 | -0.798 | 0.006 | 1.78 |
| CdSi(AgTe2)2 | -0.344 | 0.008 | 0.33 |
| MgAg2SnS4 | -0.788 | 0.011 | 0.69 |
| MgSi(AgSe2)2 | -0.739 | 0.011 | 1.84 |
| MgCu2SnS4 | -0.866 | 0.014 | 0.49 |
| CdAg2GeTe4 | -0.375 | 0.014 | 0.17 |
| MgSi(AgTe2)2 | -0.447 | 0.014 | 1.63 |
| MgAg2SnTe4 | -0.530 | 0.014 | 0.19 |
| MgAg2GeSe4 | -0.690 | 0.018 | 0.28 |
| ZnAg2SnTe4 | -0.424 | 0.019 | 0.44 |
| MgCu2SnTe4 | -0.537 | 0.026 | 0.35 |
| MgCu2GeSe4 | -0.713 | 0.030 | 0.31 |
| MgAg2SnSe4 | -0.700 | 0.043 | 1.15 |
| MgCu2SnSe4 | -0.734 | 0.047 | 0.19 |

### Iteration 2 (chalcopyrite family; alkaline-earth/Zr kesterites)
| Formula | E_f | Ehull | Eg |
|---|---|---|---|
| MnCu2GeSe4 | -0.525 | 0.000 | 0.66 |
| NaGaS2 | -1.193 | 0.000 | 4.24 |
| NaAlS2 | -1.462 | 0.000 | 4.08 |
| MgCu2SiTe4 | -0.461 | 0.034 | 0.24 |
| BaCu2GeTe4 | -0.686 | 0.066 | 0.35 |
| BaCu2SnTe4 | -0.730 | 0.067 | 0.08 |
| SrCu2SnSe4 | -0.902 | 0.083 | 0.10 |
| SrCu2GeTe4 | -0.646 | 0.092 | 0.16 |
| CaCu2GeTe4 | -0.614 | 0.101 | 0.99 |
| CaCu2SnTe4 | -0.653 | 0.107 | 0.48 |
| CaCu2GeSe4 | -0.829 | 0.110 | 0.30 |
| CaCu2SnSe4 | -0.860 | 0.117 | 0.21 |
| BaZr(CuTe2)2 | -0.900 | 0.144 | 0.34 |
| BaZr(CuSe2)2 | -1.115 | 0.184 | 0.08 |
| SrZr(CuSe2)2 | -1.073 | 0.215 | 0.79 |
| CaZr(CuSe2)2 | -1.035 | 0.244 | 1.31 |
| CaZr(CuTe2)2 | -0.762 | 0.246 | 0.64 |
| SrZr(CuTe2)2 | -0.782 | 0.247 | 0.55 |

### Iteration 3 (Na-based kesterite-type; a few Ag/Mn)
| Formula | E_f | Ehull | Eg |
|---|---|---|---|
| Na2TiZnS4 | -1.403 | 0.000 | 3.82 |
| Na2CdSnTe4 | -0.778 | 0.000 | 1.17 |
| Na2MgSnTe4 | -0.875 | 0.008 | 1.91 |
| Na2TiZnSe4 | -1.250 | 0.016 | 3.36 |
| Na2ZnSnTe4 | -0.764 | 0.017 | 1.73 |
| Na2ZnSiSe4 | -1.039 | 0.020 | 3.44 |
| MnAg2GeS4 | -0.593 | 0.021 | 0.25 |
| Na2ZnSnS4 | -1.075 | 0.025 | 3.39 |
| Na2ZnGeSe4 | -0.969 | 0.026 | 2.85 |
| Na2ZnSnSe4 | -0.990 | 0.028 | 2.84 |
| Na2ZnGeS4 | -1.081 | 0.030 | 3.80 |
| Na2ZnGeTe4 | -0.711 | 0.040 | 1.47 |
| Na2TiZnTe4 | -0.907 | 0.043 | 2.04 |
| MnSi(AgS2)2 | -0.686 | 0.052 | 0.09 |
| Na2ZrZnTe4 | -0.955 | 0.055 | 2.53 |
| Na2ZnSiTe4 | -0.685 | 0.066 | 2.64 |
| Na2ZrZnSe4 | -1.278 | 0.102 | 3.35 |
| Na2FeSnTe4 | -0.617 | 0.117 | 0.04 |
| Na2CoSnTe4 | -0.617 | 0.122 | 0.00 |
| Na2ZrZnS4 | -1.416 | 0.129 | 4.37 |

### Iteration 4 (Na/K tellurides and selenides)
| Formula | E_f | Ehull | Eg |
|---|---|---|---|
| Na2CdGeSe4 | -0.961 | 0.010 | 2.44 |
| Na2CdSnSe4 | -0.983 | 0.011 | 3.14 |
| K2CdGeSe4 | -1.020 | 0.033 | 2.64 |
| K2ZnSnTe4 | -0.826 | 0.039 | 1.49 |
| K2ZnSiTe4 | -0.764 | 0.041 | 2.44 |
| K2CdSiTe4 | -0.755 | 0.046 | 2.35 |
| TiZn(AgTe2)2 | -0.573 | 0.051 | 0.06 |
| K2ZnGeTe4 | -0.766 | 0.058 | 0.98 |
| Na2MnSnTe4 | -0.650 | 0.060 | 1.12 |
| K2TiZnTe4 | -0.968 | 0.061 | 1.69 |
| Na2CdSiTe4 | -0.683 | 0.063 | 2.64 |
| Na2CaSnTe4 | -1.006 | 0.074 | 1.59 |
| CaAg2SnTe4 | -0.660 | 0.081 | 0.05 |
| K2MnSnTe4 | -0.727 | 0.082 | 1.52 |
| CaAg2GeTe4 | -0.607 | 0.083 | 0.87 |
| Na2MgSiTe4 | -0.771 | 0.084 | 2.62 |
| K2MgSiTe4 | -0.831 | 0.085 | 2.96 |
| K2CaSnTe4 | -1.070 | 0.093 | 0.52 |
| Na2CaGeTe4 | -0.933 | 0.116 | 2.02 |
| K2CaGeTe4 | -0.993 | 0.130 | 1.56 |

### Iteration 5 (Ti/Zr on the group-IV site)
| Formula | E_f | Ehull | Eg |
|---|---|---|---|
| K2TiCdSe4 | -1.307 | 0.000 | 2.73 |
| K2MgTiSe4 | -1.415 | 0.000 | 2.62 |
| K2TiZnSe4 | -1.325 | 0.000 | 2.89 |
| Na2TiCdSe4 | -1.235 | 0.007 | 3.37 |
| K2MgTiTe4 | -1.074 | 0.025 | 0.02 |
| K2TiCdTe4 | -0.987 | 0.026 | 0.28 |
| K2ZrZnSe4 | -1.354 | 0.027 | 2.74 |
| Na2TiCdTe4 | -0.919 | 0.028 | 0.01 |
| K2ZrCdTe4 | -1.051 | 0.037 | 1.38 |
| Na2MgTiTe4 | -1.014 | 0.038 | 0.96 |
| K2MgZrTe4 | -1.152 | 0.042 | 2.23 |
| Na2ZrCdTe4 | -0.963 | 0.043 | 2.51 |
| Na2MgZrTe4 | -1.068 | 0.044 | 2.54 |
| Na2MgTiSe4 | -1.350 | 0.052 | 3.18 |
| K2ZrZnTe4 | -1.036 | 0.056 | 1.82 |
| MgZr(AgTe2)2 | -0.712 | 0.078 | 0.38 |
| ZrZn(AgTe2)2 | -0.601 | 0.087 | 0.35 |
| ZrCd(AgTe2)2 | -0.595 | 0.090 | 0.02 |
| Na2ZrCdSe4 | -1.266 | 0.090 | 3.53 |
| ZrZn(CuTe2)2 | -0.569 | 0.140 | 0.53 |

Candidates proposed per iteration: 50, 52, 92, 33 and 33. Of these, 20, 18, 20, 20 and 20 were scored. Filtering removed 9, 26 and 8 in iterations 2, 3 and 5. No filtered count is recorded for iterations 1 and 4.

## Hypotheses tested and what was learned

**Iteration 1: Ag/Cu–Zn/Cd/Mg–Si/Ge/Sn–S/Se/Te kesterites.** The hypothesis was that mixed cation and anion substitution would land gaps in the target window.
- Stability was easy: all 20 had Ehull ≤ 0.047.
- Two hits resulted, MgAg2SnSe4 and MgSi(AgTe2)2.
- Near misses were ZnSi(AgTe2)2 (1.72 eV, Ehull 0.001), MgAg2GeS4 (1.78 eV) and ZnSi(AgSe2)2 (1.84 eV).
- Cd generally lowered the gap, and Cu–Sn/Ge selenides and tellurides were too narrow (about 0.2–0.5 eV).
- The hypothesis partly held.

**Iteration 2: chalcopyrite I-III-VI2 and II-IV-V2, plus alkaline-earth/Zr kesterites.**
- The chalcopyrite candidates were already in the Materials Project, apart from NaGaS2 and NaAlS2. Both are stable but wide-gap (about 4.1–4.2 eV).
- Per the notebook, SMACT rejected the phosphide members.
- The Ca/Sr/Ba and Zr kesterites were mostly unstable (Ehull 0.066–0.247) with small gaps.
- CaZr(CuSe2)2 had Eg = 1.31 eV but Ehull = 0.244. MnCu2GeSe4 was stable but narrow (0.66 eV).
- No hits. The hypothesis was falsified, and 2 relaxations went unspent.

**Iteration 3: Na-for-Cu kesterite-type compounds (after the Ag-kesterite space was found nearly exhausted).**
- The two novel Ag/Mn compounds, MnAg2GeS4 and MnSi(AgS2)2, had very small gaps, so Mn was a dead end.
- Gaps follow S > Se > Te, so the sulfides (3.4–3.8 eV) and selenides (2.8–3.4 eV) are too wide for the window.
- Two tellurides hit the window, Na2CdSnTe4 and Na2ZnGeTe4. Na2ZnSnTe4 (1.73 eV) and Na2MgSnTe4 (1.91 eV) were near misses.
- Fe and Co tellurides were unstable and metallic. Zr on the group-IV site was unstable.

**Iteration 4: extending to K, Si, Ca/Mn/Ti and selenides.**
- One new hit resulted, K2ZnSnTe4.
- Si tellurides were wide-gap (2.35–2.96 eV) and marginally stable.
- Several Ca/Mn/Ti-on-II-site tellurides had gaps in the window (1.12–1.69 eV, including Na2CaSnTe4, K2CaGeTe4, K2MnSnTe4, Na2MnSnTe4 and K2TiZnTe4) but Ehull of 0.06–0.13, above the cutoff.
- The Cd/Ge/Sn selenides were stable (Ehull 0.010–0.033) but too wide (2.4–3.1 eV).

**Iteration 5: Ti/Zr on the group-IV site.**
- The notebook states that the remaining Na/K–Zn/Cd/Mg–Sn/Ge telluride matrix had already been considered and that the zincblende prototype gave no novel members. Some of these compositions (for example K2CdSnTe4, K2MgSnTe4, Na2CdGeTe4) do not appear in the scored database.
- One hit resulted, K2ZrCdTe4.
- Ti and Zr selenides were stable (some at Ehull = 0) but wide (2.6–3.5 eV). Ti tellurides were metallic or near-metallic.
- Ag/Cu–Zr/Ti tellurides were unstable and narrow-gap.

**Overall learning:**
- The alkali-telluride kesterite-type family was the productive space, giving 4 of the 6 hits.
- Most variation in the gap came from the anion, with S > Se > Te.
- Zn gives wider gaps than Cd, and Si widens them. Cu and Ag chalcogenides generally came out too narrow, with exceptions among the Mg/Si Ag compounds.
- Large or unusual II-site cations (Ca, Ba, Sr, Mn) tended to push Ehull above 0.05 eV/atom.

## Caveats

- **Surrogate gaps.** Band gaps come from an ML model, and the notebook flags probable underestimation for Cd, Sn and Te compounds. Gaps for the hits could shift substantially, and the window of 1.1–1.7 eV is broad compared with typical errors.
- **Marginal stability.** Several hits have Ehull near 0.04 eV/atom (Na2ZnGeTe4 0.040, K2ZnSnTe4 0.039, K2ZrCdTe4 0.037, MgAg2SnSe4 0.043). That is marginal, and these may be metastable or unsynthesizable. Only Na2CdSnTe4 sits on the hull.
- **Structure and competing phases.** It has not been verified that the kesterite-type structure is the true ground state. This matters especially for the alkali compounds, where other structure types such as stannite variants may compete. Competing-phase decompositions (e.g. Na2Te/K2Te + CdTe/ZnTe + SnTe2/ZrTe2) were not checked.
- **Toxicity and practicality.** Three hits contain Cd (Na2CdSnTe4, K2ZrCdTe4 and, in the near misses, others). Alkali tellurides are likely to be hygroscopic and air-sensitive, which the campaign did not assess.
- **Properties not assessed.** No absorption coefficients, defect physics, carrier transport or direct-versus-indirect gap character were evaluated. Suitability as an absorber is therefore unproven.
- **Coverage.** Not every combination in the proposed families was scored. Some candidates were filtered out, and some intended compositions are absent from the scored data.

## Recommended next steps

1. Run DFT with hybrid functionals (HSE) or GW on the six hits. Start with Na2CdSnTe4, K2ZrCdTe4, K2ZnSnTe4 and Na2ZnGeTe4. Check gap size and direct/indirect character.
2. Build full competing-phase convex hulls and compare kesterite, stannite and other polymorphs for the alkali tellurides.
3. Compute phonons or molecular dynamics for dynamic stability, particularly for those with Ehull near 0.04 eV/atom.
4. Score the Cd-free or Zn-based alternatives, K2ZnSnTe4 and Na2ZnGeTe4, as a lower-toxicity path.
5. Complete the Na/K–Zn/Cd/Mg–Ge/Sn telluride matrix, confirming that the compositions the notebook says were "considered" are actually scored. Also test mixed-anion (Se/Te) and mixed-cation (Na/K) alloys, which the prototype tooling did not support.
6. Assess air stability and synthesizability (handling of alkali-containing tellurides) before any experimental effort.
7. Treat the Ag-kesterites MgAg2SnSe4 and MgSi(AgTe2)2 as secondary leads, since the near misses (ZnSi(AgTe2)2 at 1.72 eV and Ehull 0.001) suggest the family sits close to the window.
