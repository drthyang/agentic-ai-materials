# Lab Notebook

## [hypothesis] iteration 1 — 2026-10-11 08:25 UTC

Iter 1 hypothesis: Kesterite I2-II-IV-VI4 family is the best-validated ~1.0-1.5 eV absorber platform (CZTS 1.5 eV, CZTSe 1.0 eV; Ge in kesterite raises gap — Chem. Mater. band-gap grading; Li-for-Cu widens gap). Explore multi-site substitution: Cu->Ag (raises gap, reduces antisite disorder), Zn->Mg/Cd/Mn/Fe (II-site with similar tetrahedral radius), Sn->Ge/Si (smaller IV raises gap), S->Se/Te mixed anion tuning. Expect novel members such as Ag2MgGeSe4, Cu2MgGeSe4, Ag2CdGeS4-type mixtures to land 1.1-1.7 eV; stability risk highest for Mg (prefers octahedral) and Si. Will prioritize novel members with Se (gap lowering counters Ge/Ag widening).

## [observation] iteration 1 — 2026-10-11 08:29 UTC

Iter 1 results (kesterite prototype, 20 relaxations, 19 novel + 1 calibration).
HITS (novel, gap 1.1-1.7, Ehull<=0.05): CdAg2GeSe4 (1.28 eV, 0.000), ZnAg2GeSe4 (1.12, 0.000), MgAg2SnSe4 (1.59, 0.016), MgAg2GeTe4 (1.49, 0.025), MgAg2SnTe4 (1.17, 0.038), ZnAg2GeTe4 (1.17, 0.028).
Near-stable but gap too wide: MgCu2SnS4 (2.17, 0.020), MgAg2SnS4 (1.87, 0.002), MgAg2GeS4 (1.89, 0.017), MgAg2GeSe4 (1.86, 0.020).
Gap OK but unstable: MgCu2SnSe4 (1.38, 0.071), MgCu2GeSe4 (1.10, 0.136).
Fail: MnCu2GeSe4 (0.93, 0.104), MnAg2GeS4 (2.24, 0.079), all Si members (Ehull 0.13-0.17), CdAg2GeTe4 (0.48), CdAg2SnTe4 (0.41).
Calibration: CdCu2SnS4 (known) 1.69 eV, Ehull 0.011 — exp ~1.4 eV, so model may overestimate by ~0.3 eV for Cu-kesterites.
Trends: Ag on I-site stabilises Mg members (MgAg2X ~0.00-0.04 vs MgCu2SnSe4 0.07). Si on IV-site is always unstable (>0.13). Te: Mg-Te keeps gap high (1.2-1.5) while Cd-Te collapses gap (<0.5) — anomalous Cd vs Zn-Te difference (ZnAg2GeTe4 1.17 vs CdAg2GeTe4 0.48) worth scrutiny.

## [reflection] iteration 1 — 2026-10-11 08:29 UTC

Hypothesis largely supported: Ag-based kesterites with Mg/Zn/Cd on II-site and Ge/Sn on IV-site are near-stable and tunable through the anion. Six novel in-window candidates. Mn/Fe and Si substitutions fail. Next iteration ideas: (1) exploit — mixed-anion Ag2Mg(Ge,Sn)(Se,Te)4 not possible in this prototype directly, but try Ag2-(Mg/Zn)-(Ge/Sn) with S/Se cross IV-site and Ca/Sr? (likely too large for tetrahedral); (2) explore chalcopyrite family: Ag(Al,Ga,In)(S,Se,Te)2 and Cu(Al,Ga)(Se,Te)2 — many known, so look for novel combos, possibly with Sb/Bi? (3) zincblende-derived III-V alloys (e.g., AlSb-type, In/Ga-P-As novel ordered members). Keep calibration in mind: Cu-kesterite gap may be overestimated ~0.3 eV; favour candidates near 1.4-1.6 model gap.

## [hypothesis] iteration 2 — 2026-10-11 08:30 UTC

Iter 2. First check: every II-IV-V2 chalcopyrite (Zn/Cd/Mg + Si/Ge/Sn + As/N) is already in MP, and the phosphides got rejected by SMACT. That family is used up for novelty, so I'm dropping it.
Main hypothesis: there are novel tetrahedral quaternaries in the kesterite prototype beyond I2-II-IV-VI4, using other valence splits that still sum to 8:
(a) I3-V-VI4 famatinite/enargite with Cu/Ag mixed on the I-site (Cu2AgSbS4, CuAg2SbS4, Ag3SbS4, Cu2AgAsS4/Se4, Ag3AsSe4, CuAg2AsSe4). Ag 4d sits deeper than Cu 3d, which means less p-d repulsion at the VBM, so the gap should widen from Cu3SbS4 (~0.9 eV) toward 1.2-1.5 eV.
(b) I2-III-III'-VI4 cation-ordered chalcopyrite analogues: Cu2AlInTe4, Ag2AlInTe4, Cu2AlGaTe4, Ag2AlGaTe4, Cu2GaInS4. The gap should interpolate between the parent chalcopyrites, with some bowing.
(c) II2-I-III-VI4 (II-VI : I-III-VI2 at 2:1 ordering): Cd2AgInSe4, Cd2AgGaTe4, Cd2CuInS4, Zn2AgInSe4, Zn2AgGaTe4, Cd2CuAlTe4, Mg2CuInSe4, Mg2AgInSe4. Predicted gaps are roughly 1.2-1.7 eV.
Risks: (b) and (c) are ordered versions of known pseudo-binary alloys, so expect Ehull of a few meV up to about 0.03. Mg on a tetrahedral site may destabilise. Calibration from iter 1: Cu-containing gaps may be overestimated by ~0.3 eV.

## [observation] iteration 2 — 2026-10-11 08:35 UTC

Iter 2 results. Used 18 relaxations (17 novel + 1 calibration); 2 left unspent.
PROCESS LESSON: I proposed 3 families in parallel, then evaluated them in one batch. The critic judged the whole batch against a single hypothesis (I3-V-VI4) and vetoed all 13 of the I2-III-III'-VI4 and II2-I-III-VI4 candidates as "not testing the hypothesis". Vetoed formulas then count as "already considered" and can't be re-proposed. So in this campaign the ordered-alloy families (Cu2AlInTe4, Ag2AlInTe4, Cd2AgInSe4, Cd2AgGaTe4, etc.) are now locked out. Rule from now on: propose one family, then evaluate it, before proposing the next.
I3-V-VI4 (famatinite type, kesterite prototype) HITS (novel, in window, Ehull 0.000): CuAg2AsSe4 1.38 eV, CuAg2SbSe4 1.46, Ag3SbSe4 1.67, Ag3AsSe4 1.68.
Stable but gap too wide: Cu2AgSbS4 1.74, Ag3SbS4 1.79, CuAg2SbS4 1.86, Cu2AgAsS4 1.87, CuAg2AsS4 1.97.
Stable but gap too small: Cu2AgAsSe4 0.44, Cu2AgSbSe4 0.43, CuAg2SbTe4 0.31, Cu3SbTe4 0.32 (Ehull 0.001), Cu2AgSbTe4 0.38 (Ehull 0.045).
P members: CuAg2PSe4 2.15 (0.000), Cu2AgPSe4 2.14 (0.045), CuAg2PS4 2.45 (0.020). All too wide.
Calibration: Cu3PSe4 (known) came out at Ehull 0.155 and 1.11 eV in this kesterite-derived polymorph. The real ground state is enargite (wurtzite-derived), and the hull does include known phases, so a 0.000 Ehull here is not just a missing hull reference.
Trends: in the selenides there is a sharp jump between Cu2Ag (~0.4 eV) and CuAg2/Ag3 (1.4-1.7 eV). The Ag-rich members fit the Ag-4d / weaker p-d repulsion picture, but a 1 eV jump from one Cu<->Ag swap is suspicious (possibly a relaxation or gap-model artifact, or a CBM change with ordering). P members are 2.1-2.5 eV no matter the Cu/Ag ratio.
CAVEATS: (1) Sb5+/As5+ with Ag is chemically questionable. Real Ag-Sb-Se chemistry prefers Sb3+ (AgSbSe2, Ag3SbSe3). The model says Ehull 0, but the hull may be missing those phases or CHGNet may be over-stabilising. (2) Famatinite vs enargite polymorph competition was not tested.

## [reflection] iteration 2 — 2026-10-11 08:35 UTC

The I3-V-VI4 hypothesis held for Ag-rich selenides: 4 new in-window, on-hull candidates. The other part of my prediction was wrong. P did not reopen Cu-rich members into the window; it pushed every P member to >2.1 eV. Cu-rich Sb/As selenides collapse to ~0.4 eV.
The campaign now has 10 hits across two families: Ag-kesterites from iter 1, and Ag-rich famatinites.
Next iteration options:
(1) Check the ~1 eV jump between Cu2AgSbSe4 and CuAg2SbSe4 in some other way. The tool can't do anion mixing, so this needs care.
(2) Explore a genuinely different family, proposed and evaluated one at a time: zincblende-GaAs prototype ordered binaries are all known, so look at heavier I3-V-VI4 variants. Also try I2-II-IV-VI4 with Ag and II=Zn/Cd/Mg plus IV=Ge/Sn in S/Se/Te combos not yet evaluated, and kesterites with Fe/Co/Ni on the II site (magnetic, high risk).
(3) Retry ordered I2-III-III'-VI4 using different formulas that aren't locked out (e.g. Ag2GaInS4 is known; not many left).
Always run propose → evaluate one family at a time, so the critic matches each batch to the right hypothesis.

## [hypothesis] iteration 3 — 2026-10-11 08:36 UTC

Iter 3 hypothesis: one family only, the II2-I-III-VI4 ordered tetrahedral quaternaries. These are 2 II-VI : 1 I-III-VI2 superstructures built on the kesterite prototype, with Cu->II, Zn->I, Sn->III. Literature grounding: AgCd2GaS4 has been made as a real quaternary phase (J. Alloys Compd. 2000, AgGaS2-CdS quasi-binary), and there are older reports of ordered wurtzite/zincblende quaternary superstructures (1972 review). So the family is chemically real, but most members are not in MP.
Gap estimate: roughly a weighted interpolation of the parent gaps, with bowing:
- CdTe (1.5) + AgInTe2 (1.0) or CuInTe2 (1.0) should give ~1.2-1.4 eV.
- ZnTe (2.3) + AgInTe2 or CuInTe2 should give ~1.4-1.6 eV.
- ZnTe + CuGaTe2 (1.2) should give ~1.6 eV.
- CdSe (1.7) + CuInSe2 (1.0) should give ~1.3 eV.
- MgTe (3.5) + AgInTe2 should give ~1.5-1.8 eV.
- Sulfides and Ga/Al selenides will mostly be too wide; I include a few as controls.
Stability expectation: the parent pseudo-binaries show wide solid solubility (small mixing enthalpy), so Ehull should be small, about 0-0.04 eV/atom. Mg is the risk. Cu members may come out ~0.3 eV over-estimated (iter-1 calibration).
Excluded: the formulas vetoed in iter 2 (Cd2AgInSe4, Cd2AgGaTe4, Cd2CuInS4, Zn2AgInSe4, Zn2AgGaTe4, Cd2CuAlTe4, Mg2CuInSe4, Mg2AgInSe4).

## [decision] iteration 3 — 2026-10-11 08:37 UTC

Iter 3 pivot: almost all of the II2-I-III-VI4 family is locked out as "already considered". The iter-2 proposal had generated the full combinatorial set, not just the 8 formulas I listed in the notebook. Only Mg2AlAgSe4, Mg2AlAgTe4 and Mg2GaAgTe4 remain. I'll keep Mg2GaAgTe4 and Mg2AlAgTe4 as possible add-ons later.
New family (one family, evaluated alone): III2-II-IV-V4, i.e. ordered (2 III-V : 1 II-IV-V2) tetrahedral quaternaries in the kesterite prototype (Cu->III, Zn->II, Sn->IV, S->V). They obey the octet rule: 2*3+2+4 = 12 = 4*3.
Reasoning: the II-IV-V2 compounds are the isoelectronic cation-split analogues of III-V. Lattice-matched pairs (GaAs/ZnGeAs2, GaP/ZnSiP2, InP/CdSnP2 or ZnSnP2, AlAs/ZnGeAs2) should mix with small strain enthalpy, so Ehull should be modest.
Gap estimates (parents, then expected):
- GaAs 1.42 + ZnGeAs2 1.15 -> ~1.3 eV
- GaAs + ZnSnAs2 0.74 -> ~1.1 eV
- AlAs 2.2 + ZnGeAs2 -> ~1.7 eV
- AlAs + ZnSnAs2 -> ~1.5 eV
- InP 1.34 + ZnGeP2 2.0 or CdGeP2 1.72 -> 1.5 eV
- InP + CdSnP2 1.17 -> ~1.2 eV
Literature search found essentially no prior work on these ordered quaternaries (only the parent II-IV-V2 gap tables), so this is past the edge of what has been reported.
Risks:
- The Ehull reference includes the binary III-V and II-IV-V2 phases, and alloy mixing enthalpy plus the octet-rule-violating bonds in this ordering could give 0.02-0.08 eV/atom.
- SMACT may reject the phosphides, as it did in iter 2.

## [observation] iteration 3 — 2026-10-11 08:40 UTC

Iter 3 III2-II-IV-V4 (arsenide) results: hypothesis decisively falsified on stability. All 17 novel members came out at Ehull 0.29-0.46 eV/atom, far above the 0.05 cutoff. Formation energies are near zero or positive (-0.13 to +0.11 eV/atom).
Gaps came out much lower than the parent interpolation:
- ZnGa2GeAs4: 0.58 eV (I predicted ~1.3)
- ZnGa2SnAs4: 0.37 eV
- ZnGa2SiAs4: 0.74 eV
- CdGa2SiAs4: 1.05 eV
In-window gaps, but all unstable:
- Al2CdGeAs4: 1.42 eV, Ehull 0.40
- Al2CdSnAs4: 1.25 eV, Ehull 0.38
- Al2CdSiAs4: 1.34 eV, Ehull 0.46
- MgAl2SnAs4: 1.27 eV, Ehull 0.34
- MgGa2SiAs4: 1.14 eV, Ehull 0.38
Interpretation: the bond-valence sum at As is formally 3 for every As, but this ordering creates III-As-IV / II-As-III environments that real III-V/II-IV-V2 alloys avoid. On top of that, the CHGNet energetics (or a strained prototype geometry) clearly penalize the structure, and the strong gap reduction suggests large bowing or relaxation distortion. Real GaAs-ZnGeAs2 alloys are disordered or phase-separate. Ordered kesterite-type III-V/II-IV-V2 is not a viable route on this platform. All phosphides failed SMACT, as in iter 2.

## [hypothesis] iteration 3 — 2026-10-11 08:40 UTC

Iter 3 mini-batch (3 remaining relaxations): these are the last unlocked members of the II2-I-III-VI4 family, Mg2GaAgTe4, Mg2AlAgTe4 and Mg2AlAgSe4. The reasoning is that MgTe/MgSe can adopt tetrahedral (zincblende/wurtzite) coordination. Iter 1 also showed that Ag stabilises Mg tetrahedral members (MgAg2SnTe4 Ehull 0.038, MgAg2GeTe4 0.025).
Expected gaps:
- Mg2GaAgTe4: MgTe 3.5 eV + AgGaTe2 1.3 eV should give ~1.6-1.9 eV.
- Mg2AlAgTe4: ~1.9-2.2 eV.
- Mg2AlAgSe4: likely >2 eV, included as a control.
I expect Mg2GaAgTe4 to be the only plausible in-window hit. This tests whether 2:1 Mg-chalcogenide:Ag-III-VI2 ordering is near-stable.

## [observation] iteration 3 — 2026-10-11 08:42 UTC

Iter 3 Mg2-Ag-III-VI4 mini-batch:
- Mg2GaAgTe4: 1.69 eV, Ehull 0.172 (unstable)
- Mg2AlAgTe4: 2.17 eV, Ehull 0.29
- Mg2AlAgSe4: 2.59 eV, Ehull 0.37
The gaps matched the interpolation prediction, but all three are unstable. With two Mg per formula unit on tetrahedral sites, the structure is strongly destabilised. Mg-rich tetrahedral phases lose to rocksalt MgSe and wurtzite/NiAs-type MgTe plus AgIII-VI2. Mg is tolerable only at 1 per 8 atoms with Ag present (iter 1).

## [reflection] iteration 3 — 2026-10-11 08:42 UTC

Iter 3 reflection: no hits this iteration (0/20). Both hypotheses failed on stability.
(1) III2-II-IV-V4 kesterite-type ordering of III-V + II-IV-V2 gives Ehull ~0.3-0.45 for every member. Cross-family cation ordering (mixing different valence sets onto the shared anion) is strongly penalised. Do not revisit.
(2) Mg-rich (2 Mg per formula unit) tetrahedral quaternaries are unstable (Ehull 0.17-0.37).
Process lesson: an iter-2 proposal can lock out an entire combinatorial family (34 formulas), not just the ones evaluated. Before planning, check which families are already consumed by running propose cheaply first.
What has worked, all within the I/II/IV/VI kesterite-type valence split with Ag:
- Ag2-II-IV-VI4 with II = Zn/Cd/Mg (1 per formula unit), IV = Ge/Sn, VI = Se/Te
- I3-V-VI4 with Ag-rich I-site
Stable members share chalcogenide anions and monovalent coinage-metal-rich cation sublattices.
Iter 4 ideas:
(a) Chalcopyrite prototype I-III-VI2 with I = Ag/Cu, III = Al/Ga/In and VI = S/Se/Te. Most members are known, but check the novelty flags; maybe Na/K on the I-site, though likely unstable.
(b) Kesterite with Sn -> Ti/Zr (tetrahedral d0, cf. sulvanite Cu3VS4 with tetrahedral V5+). Novel and exploratory: Ag2ZnTiSe4, Cu2ZnTiS4, Ag2CdTiS4.
(c) Kesterite with Zn -> Fe/Co/Ni/Mn is likely to fail, given that Mn and Fe failed in iter 1.
(d) I3-V-VI4 with Bi5+ is chemically unrealistic. Instead extend the Ag-rich famatinites with Te/Se combinations that are not yet evaluated, e.g. Ag3AsTe4 or Ag3SbTe4 (gap may be too small).
Priority for iter 4: (b) as exploration, plus any unconsumed Ag-kesterite members.

## [hypothesis] iteration 4 — 2026-10-11 08:43 UTC

Iter 4 hypothesis, one family only: d0 transition metals (Ti4+, Zr4+) on the IV site of the I2-II-IV-VI4 kesterite. Substitutions: Sn->Ti/Zr, Cu->Cu/Ag, Zn->Zn/Cd/Mg, S->S/Se/Te.
Reasoning:
- Tetrahedral d0 cations in thio/selenide sulvanite-type frameworks are real: Cu3VS4 has tetrahedral V5+, and Cu3NbSe4/Cu3TaS4 are both known.
- With a d0 Ti/Zr cation, the CBM becomes metal-d (e-type orbitals in a tetrahedral field) instead of Sn-5s/anion-p antibonding. The VBM stays Cu/Ag-d + chalcogen-p.
- Expected gaps: Zr 4d sits higher than Ti 3d, so Zr members should be ~0.4-0.7 eV wider. Ag members should be wider than Cu (deeper 4d, as seen in iters 1-2). Proposed windows: Ag2(Zn,Cd)TiSe4/S4 at ~1.2-1.7 eV, Cu2ZnZrSe4 at ~1.3 eV, Te members probably <1 eV.
Literature: no reports of Cu2ZnTiS4 or Ag2ZnZrSe4-type quaternaries (search came back empty; MP has nothing in Cu-Zn-Ti-S). This is genuinely past the edge of what is known.
Main risk: TiS2/ZrS2/ZrSe2 (octahedral, very stable) plus Cu2S/ZnS may beat the tetrahedral quaternary. Ehull could be 0.05-0.2. This is an exploration bet. The falsification criterion is Ehull >0.1 for all members.

## [observation] iteration 4 — 2026-10-11 08:46 UTC

Iter 4 results: Ti/Zr on the kesterite IV site. 20 relaxations, all on novel candidates.
The results split into two regimes, and I'm treating that split as an artifact warning rather than as chemistry.
Regime A: "on hull", Ehull 0.000, with implausibly deep Ef of -1.19 to -1.70 eV/atom.
- TiZn(CuS2)2: 2.66 eV, Ef -1.57
- TiZn(AgS2)2: 1.55 eV, Ef -1.55 (nominally in window)
- TiCd(CuS2)2: 2.85 eV
- MgTi(CuS2)2: 2.93 eV, Ef -1.70
- ZrZn(CuS2)2: 0.30 eV
- ZrZn(AgS2)2: 0.19 eV
- ZrZn(CuSe2)2: 0.21 eV, Ef -1.19
- ZrZn(AgSe2)2: 0.65 eV
- ZrCd(AgSe2)2: 0.30 eV
- ZrZn(CuTe2)2: 0.23 eV
- ZrZn(AgTe2)2: 0.07 eV
Regime B: Ehull 0.35-0.48, shallower Ef of -0.49 to -1.14, gaps 1.6-2.9.
- All Ti selenides: Ti-Zn/Cd/Mg with Cu/Ag-Se, gaps 2.2-2.8 eV
- TiCd(AgS2)2: 2.40 eV, Ehull 0.35
- MgTi(AgS2)2: 1.95 eV, Ehull 0.36
- ZrCd(AgS2)2: 2.36 eV, Ehull 0.45
- MgZr(AgSe2)2: 1.58 eV, Ehull 0.46
Sanity check: Regime A formation energies make no sense. Cu2ZnSnS4 sits at about -0.6 eV/atom, and a weighted Cu2S + ZnS + TiS2 sum would put Cu2ZnTiS4 near -0.7 to -0.8, not -1.57. Zr-chalcogenides with Cu/Ag d10 coming out at ~0.2 eV gap is also unlike any tetrahedral d0 system. The flips between regimes don't follow composition: TiZn(AgS2)2 is on hull, yet TiCd(AgS2)2 is at 0.35. I suspect a failure in the CHGNet or energy-correction scheme for early-TM chalcogenides in this tetrahedral setting, possibly a relaxation into a strongly distorted or metallic-like configuration. Regime B (Ehull ~0.35-0.48) is more physically plausible, and it says the tetrahedral d0 kesterites are strongly unstable against octahedral TiS2/ZrSe2 plus the binaries.
Conclusion: I'm not claiming TiZn(AgS2)2 (1.55 eV, Ehull 0) as a discovery. It should be flagged as SUSPECT pending an independent check, such as DFT or a recompute of Ef. The MP Ag-Ti-S system contains only Ti-rich octahedral phases (Ti6AgS12 stable).

## [reflection] iteration 4 — 2026-10-11 08:46 UTC

Iter 4 reflection: the d0 Ti/Zr kesterite hypothesis failed as a reliable result. The physically plausible members (Regime B) sit at Ehull 0.35-0.48. The members that come out "stable" have formation energies too deep to be real, which points to an evaluation artifact for early-TM chalcogenides.
Lessons:
(1) Check Ef against a weighted sum of binary formation energies. Any Ehull=0 with |Ef| far above the weighted binaries should be treated as an artifact.
(2) Octahedral-preferring d0 cations (Ti, Zr), like Mg-rich and Si members earlier, do not sit happily on tetrahedral sites.
Campaign status: the credible hits remain the 10 from iters 1-2 (Ag2-II-IV-VI4 kesterites and Ag-rich I3-V-VI4 famatinites). TiZn(AgS2)2 is logged as suspect, not as a hit.
For iter 5, the final one: go back to the productive chemistry space using the chalcopyrite prototype, which hasn't been touched yet. Look for novel I-III-VI2 members, e.g. Ag/Cu with Fe3+ or Sb3+/Bi3+ on the III site, and check novelty flags before evaluating. Alternatively, use the last iteration to add calibration points on the existing hits. Avoid Ti/Zr/Mo/W.

## [hypothesis] iteration 5 — 2026-10-11 08:48 UTC

Iter 5 hypothesis, one family only: substituting Na+ (and K+ as a control) onto the cation sites of the I3-V-VI4 famatinite (kesterite prototype, Sn->Sb/As).
Reasoning:
- Na+ is isovalent with Ag+ and almost the same size in tetrahedral coordination (Shannon IV-coordinate radii: Na 0.99 Å, Ag 1.00 Å). It should therefore sit on the Ag sublattice with little strain.
- Na has no d10 shell. Swapping Na in should cut the p-d repulsion at the VBM even more than Cu->Ag does, which pushes the VBM down and widens the gap.
- Na3SbS4 and Na3SbSe4 are known compounds built from tetrahedral SbX4 units (wide gap, solid electrolytes). So Na with Sb5+ chalcogenides is chemically real, and MP has no Na-Ag-Sb-Se phases at all.
Targets:
- Te members whose Ag/Cu parents were too narrow (CuAg2SbTe4 0.31 eV, Cu3SbTe4 0.32). Na on one site of three should raise these toward 1.1-1.5 eV.
- Cu-rich selenides at ~0.4 eV (Cu2AgSbSe4), where Cu2NaSbSe4 or Cu2NaAsSe4 may reopen the gap.
- Ag-rich selenides already at 1.4-1.7 eV. Ag2NaSbSe4 is probably too wide (>1.7) and serves as a control.
Risks:
- The Sb3+ competitor Na2CuSbS3 (MP, stable) could undercut sulfides.
- K is too large for tetrahedral sites, so I expect Ehull >0.1 for K members.
Falsification criterion: all Na members end up at Ehull >0.05, or Te members stay below 1.0 eV.

## [observation] iteration 5 — 2026-10-11 08:51 UTC

Iter 5 results for Na/K-substituted I3-V-VI4 famatinites. 20 relaxations: 19 novel plus 1 calibration (Na3SbSe4, known). Every one converged, and every one came out at Ehull 0.000, except KCu2SbTe4 at 0.006.
In-window hits (novel):
- NaCu2SbSe4: 1.55 eV, Ef -0.77
- KCu2SbSe4: 1.52 eV, Ef -0.81
Just below the window: NaAg2SbTe4 1.085 eV and NaCu2AsSe4 1.05 eV.
Gap too small: NaCu2SbTe4 0.71, KCu2SbTe4 0.48, KAg2SbTe4 0.49.
Gap too wide: Ag-rich selenides (NaAg2SbSe4 1.90, NaAg2AsSe4 1.92, KAg2SbSe4 1.91, KAg2AsSe4 2.01), KCu2AsSe4 1.83, and all sulfides (2.18-2.52).
The hypothesis held on direction. Na raises gaps strongly against its Cu/Ag parents from iter 2, at the same Cu/Ag count:
- Cu2AgSbSe4 0.43 -> NaCu2SbSe4 1.55 (+1.1)
- Cu2AgAsSe4 0.44 -> NaCu2AsSe4 1.05
- CuAg2SbTe4 0.31 -> NaAg2SbTe4 1.09
- Cu3SbTe4 0.32 -> NaCu2SbTe4 0.71
- Ag-rich selenides go from 1.4-1.7 to 1.9 (overshoot, as predicted for the control)
K does not raise gaps consistently against Na: K is higher for the Cu-As selenide and sulfide, lower for the Ag tellurides.
CAVEATS, stated honestly:
(1) Every member sits at Ehull 0, including the K members. K+ (IV-coordinate radius ~1.37 Å) on a tetrahedral site should be strongly destabilised, so the uniform 0.000 most likely reflects a sparse hull. There are few Na/K-Cu/Ag-Sb/As-Se ternary or quaternary references; MP's Na-Ag-Sb-Se system is empty. Sb3+ competitors such as NaSbSe2, Na3SbSe3 and KCu2SbS3-type phases may be missing or under-weighted.
(2) Formation energies of the sulfides (-1.05 to -1.19 eV/atom) and of Na3SbSe4 (-1.14) look deep compared with a rough weighted-binary estimate. This is the same warning sign as the iter-4 artifact, though it is less extreme for the selenides (about -0.75).
(3) Calibration: Na3SbSe4 came out at 1.42 eV. I recall the experimental optical gap as roughly 1.8-2 eV but have not checked this. If it holds, the gap model underestimates Na-rich members by about 0.4-0.5 eV, which would push NaAg2SbTe4 (1.09) up into the window and NaCu2SbSe4 (1.55) toward the top edge or above it.
Of the hits, NaCu2SbSe4 is the more credible one, because Na is size-matched to the Ag sites. KCu2SbSe4 is ranked low because of the size mismatch, despite its Ehull 0.

## [reflection] iteration 5 — 2026-10-11 08:51 UTC

Iter 5 / campaign reflection.
The gap part of the hypothesis was confirmed. Na+, which is size-matched to Ag+ and has no d shell, sets a gap-raising lever of +0.4 to +1.1 eV on Cu/Ag famatinites. It is a usable tuning knob: Cu-rich Sb selenides move from 0.4 eV to 1.55 eV.
The stability part has not been properly tested. A uniform Ehull of 0 that includes oversized K is evidence that the hull is sparse, not evidence that these compounds are stable.
Campaign summary of credible hits:
- Ag2-II-IV-VI4 kesterites: ZnAg2GeSe4 1.12 eV, CdAg2GeSe4 1.28 eV (plus other iter-1 hits)
- Ag-rich famatinites: CuAg2AsSe4 1.38, CuAg2SbSe4 1.46, Ag3SbSe4 1.67, Ag3AsSe4 1.68
- New this iteration: NaCu2SbSe4 1.55 (moderate confidence) and KCu2SbSe4 1.52 (low confidence)
Rejected or suspect: III2-II-IV-V4 (Ehull ~0.3-0.45), Mg-rich tetrahedral phases, Ti/Zr kesterites (Ef artifact), and TiZn(AgS2)2.
Recommended follow-ups, beyond this campaign:
(1) DFT (HSE) hull checks for the famatinite hits against Sb3+ competitors: AgSbSe2, Ag3SbSe3, NaSbSe2, Na3SbSe3, Cu3SbSe3, CuSbSe2.
(2) Compare enargite and famatinite polymorphs.
(3) Check the experimental Na3SbSe4 gap to calibrate the alkali-member gaps.
(4) Mixed Na/Ag tellurides (e.g. Na2AgSbTe4), which did not appear in this enumeration, may land near 1.4 eV.
