# Campaign report: qd-emitter-v1

## Executive summary

Over five iterations, 69 candidates were relaxed and scored with a CHGNet-based pipeline. All 69 were flagged novel against the Materials Project (MP). The notebook does not state the target gap window explicitly. The "in-window" judgements in it imply roughly 1.8–3.1 eV, and this report uses that reading.

Nine candidates came out near-stable (E_hull ≤ ~0.02 eV/atom, except Cu2AgPSe4 at 0.045) with gaps in that range. The strongest are:
- **CuAg2PS4** (E_hull 0.020, gap 2.45 eV)
- **CuAg2PSe4** (E_hull 0.000, 2.15 eV)
- **AgAl0.5Ga0.5S2**, written AlGa(AgS2)2 (E_hull 0.000, 2.37 eV)

Confidence is low to moderate. All numbers are surrogate-model outputs on idealized kesterite-type cells, and no DFT or experimental validation was done. Several leads are probably optimistic, or less novel than they look (see Caveats).

## Scored candidates

All values come from the campaign database. E_form and E_hull are in eV/atom, and the gap is in eV. All entries converged and are novel versus MP. "Iter" is the iteration.

| Iter | Formula | E_form | E_hull | Gap |
|---|---|---|---|---|
| 1 | ZnAg2GeSe4 | -0.681 | 0.000 | 1.119 |
| 1 | MgAg2SnS4 | -1.177 | 0.002 | 1.871 |
| 1 | MgAg2SnSe4 | -0.838 | 0.016 | 1.588 |
| 1 | MgAg2GeS4 | -1.165 | 0.017 | 1.893 |
| 1 | MgCu2SnS4 | -1.239 | 0.020 | 2.174 |
| 1 | MgAg2GeSe4 | -0.797 | 0.020 | 1.856 |
| 1 | CaAg2GeSe4 | -0.949 | 0.062 | 1.679 |
| 1 | CaAg2SnS4 | -1.297 | 0.068 | 2.279 |
| 1 | MgCu2SnSe4 | -0.819 | 0.071 | 1.383 |
| 1 | CaCu2SnS4 | -1.371 | 0.072 | 2.704 |
| 1 | CaAg2GeS4 | -1.273 | 0.094 | 2.148 |
| 1 | CaCu2GeS4 | -1.340 | 0.096 | 2.563 |
| 1 | CaCu2GeSe4 | -0.928 | 0.121 | 1.198 |
| 1 | MgCu2GeSe4 | -0.717 | 0.136 | 1.102 |
| 1 | MgSi(AgSe2)2 | -0.715 | 0.145 | 2.348 |
| 1 | MgSi(AgS2)2 | -1.132 | 0.167 | 2.541 |
| 1 | ZnSi(AgSe2)2 | -0.553 | 0.170 | 1.904 |
| 1 | CaCu2SiS4 | -1.293 | 0.241 | 2.951 |
| 2 | SrAg2SnS4 | -1.369 | 0.000 | 1.720 |
| 2 | ZnCu2SnO4 | -1.178 | 0.002 | 0.260 |
| 2 | SrAg2GeS4 | -1.354 | 0.013 | 1.867 |
| 2 | MgAg2GeTe4 | -0.423 | 0.025 | 1.490 |
| 2 | ZnAg2GeTe4 | -0.318 | 0.028 | 1.171 |
| 2 | MgAg2SnTe4 | -0.461 | 0.038 | 1.172 |
| 2 | ZnCu2GeO4 | -1.116 | 0.075 | 1.179 |
| 2 | MgCu2GeTe4 | -0.372 | 0.101 | 0.895 |
| 2 | MgCu2SnTe4 | -0.409 | 0.109 | 0.483 |
| 2 | BaSi(AgSe2)2 | -0.987 | 0.114 | 2.245 |
| 2 | MgCu2GeO4 | -1.420 | 0.121 | 2.572 |
| 2 | BaCu2SiS4 | -1.431 | 0.128 | 2.898 |
| 2 | BaSi(AgS2)2 | -1.385 | 0.129 | 2.906 |
| 2 | MgCu2SnO4 | -1.362 | 0.145 | 2.421 |
| 2 | SrCu2SiS4 | -1.373 | 0.167 | 2.967 |
| 2 | SrSi(AgS2)2 | -1.316 | 0.179 | 2.712 |
| 2 | SrCu2SiSe4 | -0.895 | 0.183 | 2.032 |
| 2 | MgAg2GeO4 | -1.174 | 0.248 | 2.936 |
| 2 | ZnAg2SnO4 | -0.798 | 0.264 | 0.017 |
| 2 | MgAg2SnO4 | -1.084 | 0.305 | 2.084 |
| 3 | SrAg2SnSe4 | -1.059 | 0.000 | 1.701 |
| 3 | AlGa(AgS2)2 | -1.451 | 0.000 | 2.372 |
| 3 | Ag2SnGeS4 | -0.977 | 0.000 | 1.364 |
| 3 | Cu2SnGeS4 | -1.031 | 0.000 | 1.812 |
| 3 | SrAg2GeSe4 | -1.021 | 0.003 | 1.687 |
| 3 | SrCu2SnSe4 | -1.045 | 0.050 | 1.109 |
| 3 | InGa(CuS2)2 | -1.082 | 0.093 | 1.998 |
| 3 | AlGa(AgSe2)2 | -0.758 | 0.132 | 1.866 |
| 3 | SiAg2SnS4 | -0.885 | 0.181 | 2.038 |
| 3 | Cu2SiSnS4 | -0.924 | 0.193 | 2.368 |
| 4 | CuAg2PSe4 | -0.476 | 0.000 | 2.152 |
| 4 | CuAg2PS4 | -0.830 | 0.020 | 2.448 |
| 4 | Cu2AgPSe4 | -0.425 | 0.045 | 2.139 |
| 5 | Zn2InAgSe4 | -0.814 | 0.093 | 1.216 |
| 5 | Mg2InCuS4 | -1.473 | 0.119 | 1.792 |
| 5 | Mg2InAgS4 | -1.435 | 0.131 | 1.418 |
| 5 | Zn2InAgS4 | -1.111 | 0.145 | 1.708 |
| 5 | Mg2InAgSe4 | -0.976 | 0.201 | 1.141 |
| 5 | Mg2GaCuS4 | -1.417 | 0.224 | 2.883 |
| 5 | Mg2GaAgSe4 | -0.965 | 0.229 | 1.402 |
| 5 | Mg2GaAgS4 | -1.374 | 0.234 | 2.854 |
| 5 | Zn2GaAgS4 | -1.059 | 0.239 | 2.955 |
| 5 | AlZn2CuSe4 | -0.755 | 0.257 | 1.356 |
| 5 | AlZn2AgSe4 | -0.736 | 0.274 | 1.674 |
| 5 | Zn2GaCuS4 | -1.027 | 0.305 | 2.138 |
| 5 | AlZn2CuS4 | -1.136 | 0.315 | 2.560 |
| 5 | AlZn2AgS4 | -1.098 | 0.328 | 2.940 |
| 5 | Mg2AlCuSe4 | -0.924 | 0.359 | 2.592 |
| 5 | Mg2AlAgSe4 | -0.909 | 0.372 | 2.594 |
| 5 | Mg2AlAgS4 | -1.350 | 0.385 | 3.240 |
| 5 | Mg2AlCuS4 | -1.244 | 0.516 | 3.483 |

### Leads (near-stable and in the visible-gap window)

| Formula | E_hull | Gap (eV) | Notes |
|---|---|---|---|
| CuAg2PS4 | 0.020 | 2.448 | Sulfophosphate; best gap |
| AgAl0.5Ga0.5S2 (AlGa(AgS2)2) | 0.000 | 2.372 | Ordered alloy of known AgAlS2/AgGaS2 |
| MgCu2SnS4 | 0.020 | 2.174 | |
| CuAg2PSe4 | 0.000 | 2.152 | |
| MgAg2GeS4 | 0.017 | 1.893 | |
| MgAg2SnS4 | 0.002 | 1.871 | |
| SrAg2GeS4 | 0.013 | 1.867 | |
| MgAg2GeSe4 | 0.020 | 1.856 | |
| Cu2SnGeS4 | 0.000 | 1.812 | Edge of the window |

Cu2AgPSe4 (E_hull 0.045, gap 2.139) is borderline-stable.

## Hypotheses tested and what was learned

**Iteration 1: wide-gap I2-II-IV-VI4 kesterite-type quaternaries.**
- Simple chalcopyrite I-III-VI2 substitutions were all already in MP (17 of 17), so none were novel.
- In the kesterite-derived I2-II-IV-VI4 family, Mg-containing sulfides and selenides were novel, near-stable and had gaps of about 1.86–2.17 eV.
- Ca on the divalent site was too large and gave E_hull of 0.06–0.24.
- Si on the tetravalent site destabilised the structure (E_hull 0.15–0.24).
- Selenides generally had lower gaps than sulfides.
- The hypothesis partly held. The gaps sit at the low end of the window.

**Iteration 2: more kesterite-lattice chemistries (O, Te anions; Sr/Ba A-site).**
- Oxides were unstable (E_hull 0.075–0.30), apart from ZnCu2SnO4. That one has E_hull 0.002 but a gap of only 0.26 eV.
- Tellurides were near-stable for Ag compounds (E_hull 0.025–0.038) but had gaps of 1.17–1.49 eV.
- Sr/Ba-based compounds with Ag and Ge/Sn were a productive direction.
  - SrAg2GeS4 (E_hull 0.013, 1.87 eV) was a hit.
  - SrAg2SnS4 (E_hull 0.000, 1.72 eV) fell just below the window.
- Si analogues again had gaps of about 2.0–2.97 eV but E_hull of about 0.11–0.18.

**Iteration 3: Se analogues, mixed-valent group-IV kesterites, ordered I-III-III' alloys.**
- Sr selenides had gaps of 1.69–1.70 eV, below the window (SrCu2SnSe4: 1.11 eV, E_hull 0.050).
- AgAl0.5Ga0.5S2 was a near-ideal hit (E_hull 0.000, 2.37 eV). It is an ordered alloy of known AgAlS2 and AgGaS2, so its novelty is compositional and ordering-based only.
- Cu2SnGeS4 (E_hull 0.000, 1.81 eV) was a hit and is novel in MP. Ag2SnGeS4 (E_hull 0.000) has a gap of 1.36 eV.
- Si-containing mixed-group-IV compounds were unstable again (E_hull 0.18–0.19).
- InGa(CuS2)2 (E_hull 0.093) and AlGa(AgSe2)2 (E_hull 0.132) were unstable.

**Iteration 4: I3-P(V)-VI4 sulfophosphates (pnictide on the tetravalent site).**
- CuAg2PS4 (2.45 eV, E_hull 0.020) and CuAg2PSe4 (2.15 eV, E_hull 0.000) were hits, and Cu2AgPSe4 was borderline.
- The notebook records that Cu3PS4/Se4, Cu2AgPS4 and Ag3PS4/Se4 are already in MP.
- The critic vetoed Ge/Si-on-the-P-site analogues for charge imbalance, and the notebook judges those vetoes correct.
- Only 3 of the 20 budgeted relaxations were used because the novel proposal space was exhausted.

**Iteration 5: ordered (II-VI)2(I-III-VI2) quaternaries M2ABX4 (M = Zn, Mg; A = Cu, Ag; B = Al, Ga, In).**
- The hypothesis was falsified. All 18 evaluated compounds were unstable, with E_hull of 0.09–0.52 eV/atom.
- Several had in-window gaps (e.g. Zn2GaAgS4 2.96 eV, Mg2GaCuS4 2.88 eV) but E_hull of 0.22–0.33.
- The least unstable compounds contain In (E_hull 0.09–0.15) but have gaps below 1.8 eV.
- The notebook attributes this to cation size and charge mismatch and to likely phase separation into ZnS-type plus chalcopyrite. This is an interpretation, not something tested directly.
- Ordered mixing appears to work only for isovalent cation pairs (e.g. Al/Ga).

**Other observations.** The zincblende and pnictide/nitride proposals returned only known or already-considered compositions, or failed charge-balance filters. The three available prototypes limited the accessible chemistry, and the notebook records the proposal space as nearly exhausted by iterations 3–5.

## Caveats

- **Surrogate-model error.** Formation energy and E_hull come from CHGNet relaxations. Gaps are HSE-fidelity surrogate predictions. No error bars were computed. Differences of a few hundredths of an eV/atom in E_hull (e.g. 0.002 vs 0.020) are not meaningful at this level.
- **Wrong-lattice bias.** Every compound was relaxed in a kesterite-derived cell. The notebook notes that real Sr/Ba compounds adopt other structure types, and that real Cu3PS4 is enargite-type. Hull energies for the Sr and P compounds are therefore likely optimistic.
- **Cu/Ag ordering.** The Cu/Ag ordering in the mixed sulfophosphates was arbitrary and not explored.
- **Novelty is only versus MP.** The notebook flags that Cu3PS4–Ag3PS4 solid solutions may exist experimentally, which would lower the true novelty of CuAg2PS4/Se4. AgAl0.5Ga0.5S2 is an ordered alloy of known compounds.
- **Many gaps sit at the low edge of the window.** The Mg/Sr/Ge/Sn sulfides are at about 1.8–1.9 eV.
- **No validation.** No DFT, phonon, competing-phase or synthesis work was done. Hull energies were evaluated against the MP hull as available in the pipeline.
- **No emission properties.** Nothing was computed about emission, such as quantum yield or defect behaviour. Only gap and stability were screened.

## Recommended next steps

1. Re-relax the top leads (CuAg2PS4, CuAg2PSe4, AgAl0.5Ga0.5S2, MgCu2SnS4, MgAg2GeS4/SnS4, SrAg2GeS4, Cu2SnGeS4) in their likely true competing structure types, such as enargite- or wurtzite-derived cells and the actual Sr/Ba phases. Then recompute hull energies.
2. Check the literature and ICSD for Cu/Ag thiophosphate solid solutions and for AgAl(1-x)GaxS2 alloys to establish true novelty.
3. Run DFT (hybrid-functional gaps, phonons and a full competing-phase analysis) on the top 3–5 candidates.
4. Explore other Cu/Ag site orderings in the sulfophosphates.
5. Explore isovalent-only alloying, since this is the one mixing strategy that worked. Examples are Ga/Al, Cu/Ag and ordered S/Se.
6. Avoid Si-, O- and Te-containing kesterite-type variants and the 2:1 II-VI/I-III-VI2 quaternaries, which failed on stability or gap in this campaign.
7. Expand beyond the three available prototypes to reach new chemistries.
