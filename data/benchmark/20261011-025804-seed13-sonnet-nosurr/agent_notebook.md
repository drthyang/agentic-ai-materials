# Lab Notebook

## [hypothesis] iteration 1 — 2026-10-11 02:58 UTC

Kesterite family: Cu2ZnSnS4 (1.5 eV) -> isoelectronic substitutions (Ag for Cu, Cd/Mg/Ca for Zn, Ge/Si for Sn, Se/Te for S) keep 8-electron count and tetrahedral bonding; gaps should tune around 1.0-1.7. Expect many known (CZTSe, CZGS) so pick novel ones, e.g. Ag2ZnSnSe4, Ag2CdSnS4, Cu2CdGeS4, Cu2MgSnS4 etc. Run propose for the broad family.

## [observation] iteration 1 — 2026-10-11 03:06 UTC

21 evaluated. Novel hits (gap 1.1-1.7, ehull<=0.05): CdAg2GeSe4 (0.0, 1.28 eV - best), ZnAg2GeSe4 (0.0, 1.12), MgAg2SnSe4 (0.016, 1.59), SrAg2GeSe4 (0.003, 1.69, edge). Near misses: SrAg2SnSe4 (0.0, 1.70), MgAg2GeSe4 (0.02,1.86), MgAg2SnS4 (0.002,1.87). Fails: Si-containing Ag kesterites (ehull 0.13-0.17), Cu-Mg-Ge-Se/Te (ehull 0.10-0.14), Ca analogs (ehull 0.05-0.09; Ca too large/ionic). Calibration: ZnAg2SnSe4 (known) 0.0, 1.12 eV. ZnAg2SnTe4 gap 0.6. Critic vetoed MgCu2SiTe4 (size mismatch). Caveat: CHGNet ehull in kesterite-type only; real ground state might be other polymorph (e.g., stannite/ wurtzite-derived).

## [reflection] iteration 1 — 2026-10-11 03:06 UTC

Hypothesis supported: Ag-based selenide kesterite-type quaternaries with Ge/Sn and Zn/Cd/Mg/Sr are stable with gaps 1.1-1.7. Ag replacing Cu stabilizes vs Cu analogs (Mg-Cu-Ge-Se unstable). Si and Ca fail; S analogs too wide gap, Te too narrow, so Se is the sweet spot. Next: explore Ag-Cd/Zn/Mg + Ge/Sn Se mixed-anion (S/Se) alloys, Ba/Sr variants, Cu/Ag mixed, and other families (I-III-VI2 Ag chalcopyrite with Ga/In, Cu-Sb-Se, ternary pnictides) given dimensions. Also check ZnAg2GeSe4 and CdAg2GeSe4 in literature for novelty beyond MP.

## [observation] iteration 2 — 2026-10-11 03:18 UTC

Iter 2. Chalcopyrite/I-III-VI2 proposals nearly all known in MP (skipped). Zr/Ti on IV site of Ag-Se kesterite: Zr ones ehull 0 but gaps 0-0.65 (too small); Ti ones ehull 0.35+ (unstable). Ba vetoed (size mismatch). Ag-telluride kesterites NOVEL HITS: MgAg2GeTe4 (ehull 0.025, gap 1.49 - best), ZnAg2GeTe4 (0.028, 1.17), MgAg2SnTe4 (0.038, 1.17). Cd/Sr tellurides gap too small (0.1-0.5). Cu analogs: MgCu2SnSe4 (0.071, 1.38 - unstable), SrCu2SnSe4 (0.050, 1.11 - borderline), SrCu2SnTe4 (0.0, 0.87), MgCu2SnTe4 fails (0.109). Unspent: 2 relaxations.

## [reflection] iteration 2 — 2026-10-11 03:18 UTC

Small-cation (Mg, Zn) Ag-telluride kesterites with Ge hit window; gap trend: Ge > Sn, Mg > Zn > Cd > Sr. Ti fails, Zr gap too low. Next: try Mg/Zn Ag2 with Ge/Sn mixed S/Se or Se/Te anion (not supported by prototype tool directly), Ag-Mg-Ge-Se variants with Cu/Ag mix, and other families (e.g. ternary pnictides ZnSnP2/ Zn3P2-like, Cu-Sb-Se, Ba-Zr chalcogenide perovskites BaZrS3 variants, halide double perovskites) to diversify. Ehull of kesterite polymorph caveat remains.

## [hypothesis] iteration 3 — 2026-10-11 03:18 UTC

Iter 3: diversify to I3-V-VI4 famatinite/sulvanite-type (Cu/Ag)3(Sb/As)(S/Se)4 in kesterite-type cell. II-IV-V2 pnictide chalcopyrites all known in MP (skipped). Ag substitution widens gap vs Cu3SbSe4 (~0.3 eV); expect Ag-rich Sb/As sulfoselenides ~1.2-1.6. Ehull risk: true ground state is famatinite/enargite polymorph; CHGNet in kesterite cell may overestimate ehull. Evaluate ~15 novel: Cu2AgSb/As S/Se, CuAg2Sb/As S/Se, Ag3SbS4, Ag3SbSe4, Ag3AsSe4, NaAg2 variants (Na+ large, riskier).

## [observation] iteration 3 — 2026-10-11 03:23 UTC

Iter 3: II-IV-V2 pnictide chalcopyrites all known/SMACT-rejected. Evaluated 15 novel I3-V-VI4 kesterite-type (critic vetoed Cu2AgBiS4/Se4 charge imbalance - correct, I mis-included). All ehull 0.0. NOVEL HITS in window: CuAg2AsSe4 (1.38 eV, best), CuAg2SbSe4 (1.46), Ag3SbSe4 (1.67, edge), Ag3AsSe4 (1.68, edge). Sulfides too wide (1.74-2.2), Cu2Ag selenides too narrow (0.43), NaAg2 too wide (1.9-2.2). Trend: gap rises with Ag fraction; S > Se; As ≈ Sb. Caveats: ehull 0.0 for everything is suspicious - MP hull may lack competing Ag-Sb-Se / Cu-Sb-Se phases (e.g. Cu3SbSe4 famatinite tetragonal vs this cell; Ag3SbSe3 phases), and PBE-like CHGNet; real ground state may be polymorph. 5 relaxations unspent (no good remaining candidates in prototype tool).

## [reflection] iteration 3 — 2026-10-11 03:23 UTC

Hypothesis supported: Ag-rich Sb/As selenide famatinite-type give 1.4-1.7 eV. Best novel: CuAg2AsSe4, CuAg2SbSe4. Next iter: tune gap down for edge cases (Ag3 -> CuAg2 already done); mixed S/Se anion needs prototype support; test Cu/Ag-Zn/Cd-Ge/Sn selenide mixes; verify competing phases (Ag3SbSe3, Ag2Se, Sb2Se3) for ehull realism; try Cu-Ag ratios like Cu1.5Ag1.5 via supercell not supported. Also consider Ag-P/ Ag-Sb-Te variants (Ag3SbTe4 gap likely ~0.8). Unspent 5 budget was due to lack of good candidates, should have used more diverse families (e.g. zincblende prototype for I-III-VI/II-VI alloys).

## [hypothesis] iteration 4 — 2026-10-11 03:23 UTC

Iter 4: diversify with zincblende prototype: Ag/Cu-III-VI-type and I-V-VI2 (AgSbSe2/ AgBiS2-like, cation-ordered) and II-VI/III-V binaries/ternaries with gaps ~1.4 (CdTe-like, ZnTe-like, AlSb, GaAs-like). Expect most binaries known; look for novel ordered ternaries e.g. AgInTe2-like / CuAlTe2 / ZnSnAs2 analogs. Also revisit kesterite with Cd/Zn/Mg + Ag2 Ge/Sn mixtures not yet tried (e.g. Mn, Ba). Evaluate novel ones only.

## [observation] iteration 4 — 2026-10-11 03:29 UTC

Iter 4: zincblende prototype only produced binaries (all known) - useless. Kesterite with 3d M2+: Fe-Ag2 (ehull 0.07-0.12, gap ~0) and Co-Ag2 (ehull 0.056-0.087, gap 0-0.8) fail; MnCu2GeSe4 ehull 0.104 fail. Ni family: NiAg2GeSe4 (0.0, 1.65), NiAg2SnSe4 (0.0, 1.68) in window but at edge; NiAg2GeS4 (0.008, 1.74), NiAg2SnS4 (0.0, 1.90) too wide; NiAg2Ge/SnTe4 gaps 0.04-0.13; Cu2NiGeSe4 gap 0.26; Cu2NiGeTe4/SnTe4 ehull 0.07; Cu2NiGeS4 (0.013, 1.12 eV) hit, novel. Caveat: Ni2+ is d8 and normally square-planar/octahedral, not tetrahedral; CHGNet/ML gap for Ni (and Fe/Co) compounds is unreliable (non-magnetic/ML artifacts), so Ni hits are low confidence. 18 of 20 relaxations used.

## [reflection] iteration 4 — 2026-10-11 03:29 UTC

Hypothesis (3d-M kesterites) partially supported: only Ni gives stable in-window entries (NiAg2GeSe4, NiAg2SnSe4, Cu2NiGeS4) but these are low-confidence due to d8 tetrahedral oddness; Fe, Co, Mn fail. Most reliable discoveries remain main-group: CdAg2GeSe4, ZnAg2GeSe4, MgAg2GeTe4, CuAg2AsSe4, CuAg2SbSe4. Next (final iter 5): refine/rank best candidates, maybe test mixed Cu/Ag-Sb/As combos or Ag-Zn/Cd-Ge with literature check of novelty; avoid zincblende prototype (binaries only).

## [observation] iteration 5 — 2026-10-11 03:40 UTC

Iter 5: Kesterite chalcogenide space was already exhausted (all proposals 'already considered'). New I-V-VI2 chalcopyrite-cell: NOVEL HITS CuAsS2 (ehull 0.0, gap 1.46) and KBiTe2 (0.003, 1.30). Caveat: MP hull sparse for Cu-As-S (CuAsS is stable competitor; K-Bi-Te only K3BiTe3), As3+/Bi3+ lone-pair compounds likely prefer non-tetrahedral polymorphs, so low-moderate confidence. KSbTe2 (0, 0.55), KAsS2 (0, 2.45), CuBiTe2 (0.093) miss. II-IV-V2 with Ca/Sr/Mg + Sb/As/Zr: all ehull 0.12-0.30 fail (size mismatch/gaps ~0). P/Sb-Te famatinites: CuAg2PSe4 (0, 2.15) too wide; Sb-Te ones 0.3-0.4 eV too narrow; Cu2AgPSe4 0.045/2.14. Critic vetoed SrCu2SiSe4/Te4 (size mismatch).

## [reflection] iteration 5 — 2026-10-11 03:40 UTC

Campaign summary: best novel candidates: CdAg2GeSe4 (1.28, 0.0), ZnAg2GeSe4 (1.12), MgAg2GeTe4 (1.49, 0.025), MgAg2SnSe4 (1.59), CuAg2AsSe4 (1.38), CuAg2SbSe4 (1.46), CuAsS2 (1.46), KBiTe2 (1.30); Ni-based low confidence. Caveats: CHGNet ehull within prototype only, sparse MP hulls, polymorph risk. Next steps if continuing: DFT check of competing polymorphs (stannite, wurtzite-derived, rocksalt-derived for I-V-VI2), mixed-anion S/Se alloys, defect/absorption checks.
