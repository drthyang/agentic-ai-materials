# Campaign report: qd-emitter-v1

## Executive summary

Over 5 iterations, 95 novel candidates (absent from Materials Project) were relaxed and scored with CHGNet and an HSE-fidelity band-gap surrogate. By the notebook's own criteria (novel, E_hull ≤ 0.05 eV/atom, gap about 1.8–3.1 eV), **six candidates** emerged as hits: MgAg2SnS4, MgAg2GeS4, MgAg2GeSe4, MgCu2SnS4, Ba2InCuS4 and CaZn3S4. Two more, Ba2GaCuS4 and CaMg(ZnTe2)2, are borderline because their hull energies are just above the cutoff. Confidence is moderate to low. Every number comes from a machine-learned surrogate, with no DFT cross-check and no synthesis. Several hits sit at the low-gap edge, and the "novel" label only means absent from MP. The search was also limited by a small prototype menu (kesterite, chalcopyrite, zincblende) that was largely saturated after iteration 2.

## Scored candidates

Columns: iteration, formation energy per atom (eV), E_hull (eV/atom), band gap (eV). All 95 were novel and converged. ★ marks the notebook's hits and † marks its borderline cases.

| It | Formula | E_form | E_hull | Gap |
|---|---|---|---|---|
| 1 | ZnAg2GeSe4 | -0.681 | 0.000 | 1.12 |
| 1 | ★MgAg2SnS4 | -1.177 | 0.002 | 1.87 |
| 1 | MgAg2SnSe4 | -0.838 | 0.016 | 1.59 |
| 1 | ★MgAg2GeS4 | -1.165 | 0.017 | 1.89 |
| 1 | ★MgCu2SnS4 | -1.239 | 0.020 | 2.17 |
| 1 | ★MgAg2GeSe4 | -0.797 | 0.020 | 1.86 |
| 1 | CaAg2GeSe4 | -0.949 | 0.062 | 1.68 |
| 1 | CaAg2SnS4 | -1.297 | 0.068 | 2.28 |
| 1 | MgCu2SnSe4 | -0.819 | 0.071 | 1.38 |
| 1 | CaCu2SnS4 | -1.371 | 0.072 | 2.70 |
| 1 | CaAg2GeS4 | -1.273 | 0.094 | 2.16 |
| 1 | CaCu2GeS4 | -1.340 | 0.096 | 2.56 |
| 1 | BaCu2SiS4 | -1.431 | 0.128 | 2.90 |
| 1 | MgCu2GeSe4 | -0.717 | 0.136 | 1.10 |
| 1 | MgSi(AgSe2)2 | -0.715 | 0.145 | 2.35 |
| 1 | SrCu2SiS4 | -1.373 | 0.167 | 2.97 |
| 1 | MgSi(AgS2)2 | -1.132 | 0.167 | 2.54 |
| 1 | ZnSi(AgSe2)2 | -0.553 | 0.170 | 1.90 |
| 1 | CaCu2SiS4 | -1.293 | 0.241 | 2.95 |
| 2 | ZnCu2SnO4 | -1.178 | 0.002 | 0.26 |
| 2 | MgAg2GeTe4 | -0.423 | 0.025 | 1.49 |
| 2 | ZnAg2GeTe4 | -0.318 | 0.028 | 1.17 |
| 2 | ZnCu2GeO4 | -1.116 | 0.075 | 1.18 |
| 2 | MgSi(AgTe2)2 | -0.331 | 0.087 | 1.80 |
| 2 | ZnSi(AgTe2)2 | -0.222 | 0.095 | 2.04 |
| 2 | MgCu2GeTe4 | -0.372 | 0.101 | 0.90 |
| 2 | MgCu2GeO4 | -1.419 | 0.122 | 3.05 |
| 2 | MgCu2SnO4 | -1.362 | 0.145 | 2.42 |
| 2 | MgCu2SiTe4 | -0.275 | 0.173 | 0.87 |
| 2 | MgAg2GeO4 | -1.174 | 0.248 | 2.94 |
| 2 | ZnAg2SnO4 | -0.798 | 0.264 | 0.02 |
| 2 | MgAg2SnO4 | -1.084 | 0.305 | 2.08 |
| 2 | ZnCu2SiO4 | -1.238 | 0.378 | 2.12 |
| 2 | MgCu2SiO4 | -1.566 | 0.390 | 2.34 |
| 2 | MgSi(AgO2)2 | -1.283 | 0.554 | 2.82 |
| 3 | ★Ba2InCuS4 | -1.918 | 0.012 | 2.18 |
| 3 | Sr2InCuSe4 | -1.580 | 0.012 | 0.45 |
| 3 | Ba2GaCuSe4 | -1.588 | 0.027 | 1.68 |
| 3 | Sr2GaCuSe4 | -1.564 | 0.051 | 1.19 |
| 3 | †Ba2GaCuS4 | -1.925 | 0.056 | 2.64 |
| 3 | Sr2GaAgS4 | -1.896 | 0.077 | 2.59 |
| 3 | Ba2GaAgS4 | -1.875 | 0.095 | 2.50 |
| 3 | Sr2InCuS4 | -1.821 | 0.134 | 1.88 |
| 3 | Ca2GaAgS4 | -1.821 | 0.155 | 2.84 |
| 3 | Sr2InAgS4 | -1.754 | 0.176 | 2.24 |
| 3 | Sr2GaCuS4 | -1.824 | 0.180 | 2.95 |
| 3 | Ba2AlCuS4 | -1.882 | 0.220 | 2.89 |
| 3 | Ca2InCuS4 | -1.730 | 0.230 | 2.14 |
| 3 | Ca2GaCuS4 | -1.737 | 0.273 | 2.84 |
| 3 | Ca2AlAgS4 | -1.808 | 0.297 | 2.95 |
| 3 | Ca2AlCuS4 | -1.810 | 0.319 | 3.41 |
| 3 | Sr2AlCuS4 | -1.781 | 0.343 | 3.14 |
| 3 | Ba2AlAgS4 | -1.736 | 0.348 | 3.06 |
| 3 | Sr2AlAgS4 | -1.753 | 0.352 | 2.73 |
| 3 | Ca2GaCuSe4 | -1.238 | 0.360 | 2.05 |
| 4 | ★CaZn3S4 | -1.742 | 0.037 | 2.91 |
| 4 | BaZn3Te4 | -0.925 | 0.037 | 0.46 |
| 4 | †CaMg(ZnTe2)2 | -0.970 | 0.058 | 2.29 |
| 4 | SrZn3Te4 | -0.890 | 0.058 | 0.87 |
| 4 | CaZn3Te4 | -0.860 | 0.066 | 0.95 |
| 4 | BaZn3Se4 | -1.279 | 0.103 | 1.32 |
| 4 | MgZn3Te4 | -0.610 | 0.119 | 1.22 |
| 4 | MgZnTe2 | -0.700 | 0.131 | 2.27 |
| 4 | SrZn3Se4 | -1.251 | 0.134 | 1.30 |
| 4 | CaMg(ZnSe2)2 | -1.342 | 0.170 | 1.56 |
| 4 | BaZn3S4 | -1.572 | 0.192 | 2.52 |
| 4 | MgZn3Se4 | -0.970 | 0.210 | 1.47 |
| 4 | MgZnSe2 | -1.092 | 0.223 | 1.95 |
| 4 | SrZn3S4 | -1.549 | 0.227 | 2.47 |
| 4 | CaZnTe2 | -0.883 | 0.342 | 2.36 |
| 4 | Zn2SiSnN4 | -0.049 | 0.370 | 1.75 |
| 4 | Zn2SnGeN4 | 0.245 | 0.377 | 1.22 |
| 4 | Mg2SnGeN4 | -0.038 | 0.465 | 2.92 |
| 4 | Mg2SiSnN4 | -0.298 | 0.496 | 3.72 |
| 4 | Mg2SiGeN4 | -0.379 | 0.525 | 4.47 |
| 5 | Zn2InAgSe4 | -0.814 | 0.093 | 1.22 |
| 5 | Mg2InCuS4 | -1.473 | 0.119 | 1.79 |
| 5 | Mg2InAgS4 | -1.435 | 0.131 | 1.42 |
| 5 | Zn2InAgS4 | -1.111 | 0.145 | 1.71 |
| 5 | Mg2InAgSe4 | -0.976 | 0.201 | 1.14 |
| 5 | Mg2GaCuSe4 | -0.984 | 0.222 | 1.73 |
| 5 | Mg2GaCuS4 | -1.417 | 0.224 | 2.88 |
| 5 | Mg2GaAgSe4 | -0.965 | 0.229 | 1.40 |
| 5 | Mg2GaAgS4 | -1.374 | 0.234 | 2.85 |
| 5 | Zn2GaAgS4 | -1.059 | 0.239 | 2.96 |
| 5 | AlZn2CuSe4 | -0.755 | 0.257 | 1.36 |
| 5 | AlZn2AgSe4 | -0.736 | 0.274 | 1.67 |
| 5 | Zn2GaCuS4 | -1.027 | 0.305 | 2.14 |
| 5 | Mg2InCuSe4 | -0.868 | 0.315 | 1.36 |
| 5 | AlZn2CuS4 | -1.136 | 0.315 | 2.56 |
| 5 | AlZn2AgS4 | -1.098 | 0.328 | 2.94 |
| 5 | Mg2AlCuSe4 | -0.924 | 0.359 | 2.59 |
| 5 | Mg2AlAgSe4 | -0.909 | 0.372 | 2.59 |
| 5 | Mg2AlAgS4 | -1.350 | 0.385 | 3.24 |
| 5 | Mg2AlCuS4 | -1.244 | 0.516 | 3.48 |

## Hypotheses tested and what was learned

**Iteration 1: I–III–VI2 chalcopyrites and I2-II-IV-VI4 kesterites.**
- All 17 chalcopyrite candidates were already in MP, so they were skipped.
- 19 novel kesterite-type compounds were evaluated.
- The Mg-based sulfides and selenides gave four hits: MgAg2SnS4 (0.002 eV/atom, 1.87 eV), MgAg2GeS4 (0.017, 1.89), MgAg2GeSe4 (0.020, 1.86) and MgCu2SnS4 (0.020, 2.17).
- ZnAg2GeSe4 (0.000, 1.12 eV) and MgAg2SnSe4 (0.016, 1.59 eV) were near-stable but their gaps are too low.
- The larger Ca, Sr and Ba cations and the Si-containing compounds were unstable (E_hull 0.06–0.24).
- Mg is the largest II cation that stays stable in this structure. Selenides lower the gap by roughly 0.3–0.5 eV.
- The hits cluster at the low edge of the gap window (1.86–2.17 eV), below the roughly 2.4 eV ideal.

**Iteration 2: oxide and telluride kesterite variants.** This gave zero hits.
- The kesterite and chalcopyrite space with the Mg/Zn × Cu/Ag × Si/Ge/Sn × S/Se palette was exhausted, and zincblende gave only known binaries.
- 16 oxides and tellurides were evaluated.
- The oxides were either unstable or had no useful gap. ZnCu2SnO4 is near-stable (0.002) but its gap is 0.26 eV. The wide-gap oxides MgCu2GeO4 (3.05 eV) and MgAg2GeO4 (2.94 eV) have E_hull of 0.12 and 0.25.
- The near-stable tellurides MgAg2GeTe4 (1.49 eV) and ZnAg2GeTe4 (1.17 eV) have gaps that are too low.
- Four relaxations went unspent.

**Iteration 3: A2(II) M(I) M(III) Q4 compounds (Ba, Sr or Ca with Cu or Ag and Al, Ga or In).** 20 novel candidates were evaluated.
- Ba2InCuS4 was a hit (0.012 eV/atom, 2.18 eV).
- Ba2GaCuS4 was borderline (0.056, 2.64 eV).
- Sr2InCuSe4 (0.45 eV), Ba2GaCuSe4 (1.68 eV) and Sr2GaCuSe4 (1.19 eV) were near-stable or marginal but have low gaps.
- Stability rises with a larger A cation (Ba > Sr > Ca) and a larger III cation (In > Ga > Al), and Cu is more stable than Ag. Gap rises as the III cation shrinks and from selenide to sulfide.
- The Al and Ca members are very unstable (E_hull about 0.2–0.35).
- The kesterite-like tetrahedral geometry is probably not the true ground state for Ba compounds, so these E_hull values are relative to the hull only for this assumed structure.

**Iteration 4: nitrides and all-II chalcogenides.**
- One proposed II-IV-VI2 chalcopyrite batch was charge-imbalanced, which was my error. The critic vetoed it and no budget was used.
- The II2-IV-IV'-N4 nitrides (Zn or Mg with Si, Ge and Sn) were all strongly unstable (E_hull 0.37–0.53).
- Ordered all-II chalcogenides gave one hit, CaZn3S4 (0.037, 2.91 eV), which is at the upper edge of the gap window.
- The tellurides BaZn3Te4 and CaZn3Te4 are near-stable but have low gaps (0.46 and 0.95 eV).
- CaMg(ZnTe2)2 is borderline (0.058, 2.29 eV).
- Other sulfide and selenide members were unstable (E_hull 0.10–0.23).

**Iteration 5: ZnS-derived Zn2/Mg2–(Cu/Ag)–(Al/Ga/In)–(S/Se)4 ordered quaternaries. This hypothesis was falsified.**
- All 20 candidates had E_hull between 0.09 and 0.52 eV/atom. The best was Zn2InAgSe4 (0.093, 1.22 eV).
- Many sulfides had gaps in the target window but are strongly unstable.
- Instability grows as the III cation shrinks.
- The notebook attributes this, as a suggestion only, to phase separation into ZnS plus CuGaS2-type phases and to Mg's preference for octahedral coordination. Neither explanation was tested.

## Caveats

- **Surrogate error.** E_hull comes from CHGNet relaxations and the gaps from an HSE-fidelity surrogate. No error bars were measured in this campaign. The 0.05 eV/atom hull cutoff is comparable to typical ML-potential uncertainty, so the borderline cases (0.037–0.058) cannot be separated from noise. The gaps are bulk values, and quantum confinement in a nanocrystal would shift them upward.
- **Structure assumption.** All candidates were built on the kesterite-like prototypes. E_hull for compounds like Ba2InCuS4 may be misleading if the real ground state is a different structure type. Competing phases beyond what the database contains may also lower the true hull.
- **Novelty.** "Novel" here means absent from Materials Project only. No literature check beyond the notebook's brief grounding was done for individual hits. Iteration 2's notes say Cu2MgSnS4 is being studied in the literature, so MgCu2SnS4 may not be new in practice.
- **No other validation.** Phonon stability, defect chemistry, dopability, synthesizability and optical properties (absorption versus emission, quantum yield) have not been assessed. No DFT or experimental checks were done.

## Recommended next steps

1. Re-evaluate the six hits and two borderline compounds with DFT, using a full competing-phase hull and HSE or GW gaps.
2. Check phonon stability and the lowest-energy polymorph for each. Prioritize Ba2InCuS4, where kesterite is probably not the ground state, and MgAg2SnS4 (E_hull 0.002).
3. Search the literature for each hit's composition and structure type to confirm novelty.
4. Test tunability. The Mg–Ag/Cu–Sn/Ge–S(e) family gaps (1.86–2.17 eV) sit below the ideal, so S-rich or alloyed variants might raise them. CaZn3S4 (2.91 eV) is near the top of the window.
5. Add new prototypes, since the current menu is saturated, and avoid the oxide, nitride and Mg2/Zn2-(Cu/Ag)-III families that this campaign showed to be unstable.
6. If any compound passes DFT validation, attempt solid-state synthesis, starting with the most stable Mg-based sulfides.
