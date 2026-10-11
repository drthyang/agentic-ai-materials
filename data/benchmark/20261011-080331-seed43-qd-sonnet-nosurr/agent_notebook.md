# Lab Notebook

## [hypothesis] iteration 1 — 2026-10-11 08:03 UTC

Chalcopyrite I-III-VI2 with Cu/Ag, Al/Ga/In, S/Se/Te: gaps span ~1-2.7 eV. Known ternaries (CuGaS2 2.4, AgGaS2 2.7, AgInS2 1.9) are in MP, so aim for less-explored ones: mixed-cation / mixed-anion (e.g. AgAlSe2, CuAlTe2, AgInSe2 variants) and substituting Zn/Ge/Si/Sn into the prototype. Start with chalcopyrite substitutions; check novelty flags.

## [observation] iteration 1 — 2026-10-11 08:07 UTC

Chalcopyrite I-III-VI2 combos were all in MP (0 novel) -> skipped. Kesterite-derived I2-II-IV-VI4 gave many novel. Hits (novel, Ehull<=0.05, gap 1.8-3.1): MgAg2SnS4 (0.002, 1.87), MgAg2GeS4 (0.017, 1.89), MgAg2GeSe4 (0.020, 1.86), MgCu2SnS4 (0.020, 2.17), SrAg2GeS4 (0.013, 1.87, flagged novel in 2nd pass though initially listed non-novel). Stable but gap too low: ZnAg2GeSe4 (1.12), MgAg2SnSe4 (1.59), SrAg2SnS4 (1.72), SrAg2GeSe4 (1.69). Wide gap but unstable: Si-containing (Ehull 0.15-0.22), Ca-containing (0.07-0.10), SrCu2SiS4 (0.167, 2.97). Critic wrongly vetoed SrSi(AgS2)2 as charge-imbalanced (it is balanced). Gaps are low-ish; PBE-like trend: Ag/Sn/Se lower gap, Cu and S raise gap.

## [reflection] iteration 1 — 2026-10-11 08:07 UTC

Hypothesis (kesterite-type with Mg/Sr/Ag replacing Zn/Cu) partly confirmed: Mg and Sr stabilize; Ca and Si destabilize in this structure (size mismatch/tetrahedral Si-Mg). Next: Cu analogs with Sr/Ba and Ge/Sn (SrCu2GeS4 known; try SrCu2SnS4, BaCu2SnS4, MgCu2GeS4 variants), Zn-containing S analogs with Ag-Cu mixing, and explore other families (nitrides/phosphides via zincblende, e.g. Zn-IV-N2, Mg-IV-N2; Cu/Ag halide-chalcogenides). Aim for gaps ~2.4: Mg-Cu-Sn/Ge-S and Mg-Ag-Ge-S are close to 2. Avoid Si and Ca.

## [hypothesis] iteration 2 — 2026-10-11 08:07 UTC

Iter 2: Zincblende/chalcopyrite pnictide cross-substitution gives only known binaries/nitrides or fails SMACT (phosphides rejected) -> dead end. Remaining novel space in kesterite-type I2-II-IV-X4: Se/Te anions and SrCu2SnSe4. Tellurides expected to have low gaps (~1-1.7 eV) but Cu-Mg/Sr/Ba-Ge tellurides with large alkaline-earth cation (more ionic, less Cu d-p repulsion) might reach ~1.8. Test Cu-Te members as a gap-trend probe plus SrCu2SnSe4.

## [observation] iteration 2 — 2026-10-11 08:11 UTC

Iter 2: zincblende & chalcopyrite pnictide routes: all known or SMACT-rejected (phosphides rejected) -> no candidates. Kesterite tellurides (12 evaluated; 11 novel): many stable (SrCu2SnTe4 0.0, BaCu2SnTe4 0.001, BaAg2GeTe4 0.0, SrAg2GeTe4 0.016, MgAg2GeTe4 0.025, ZnAg2GeTe4 0.028) but gaps 0.15-1.5 eV, all below window. SrCu2SnSe4 Ehull 0.05, gap 1.11. Oxide kesterites (8): gaps in window for several (MgCu2GeO4 2.57, MgAg2GeO4 2.94, MgAg2SnO4 2.08, BaCu2GeO4 2.60) but Ehull 0.12-0.36 -> unstable (tetrahedral oxide kesterite is wrong structure; competing phases like silicates/germanates/binary oxides). No new hits this iteration.

## [reflection] iteration 2 — 2026-10-11 08:11 UTC

Gap trend by anion in this family: O (2-3.5) > S (1.7-2.2) > Se (1.1-1.9) > Te (0.15-1.5); stability trend opposite (Te, Se most stable relative to hull with Ba/Sr; oxides unstable in this structure). Target window thus sits at S, where iter-1 hits exist. Next iteration: stay at sulfides and tune gap upward toward 2.4: Mg/Zn-Cu-Ge-S, mixed-cation (Cu/Ag) or mixed anion S/Se alloys; alternatively explore sulfides with Ga/Al-based I-III-VI compositions in different structures, or Zn-rich II-IV-S. Avoid Te, avoid oxides in kesterite. Prototype library limits novelty: chalcopyrite/zincblende fully known.

## [observation] iteration 3 — 2026-10-11 08:17 UTC

Iter 3: Kesterite sulfides all 'already considered' (no new). Chalcopyrite-type A(II)Sn(II)X2 route productive. Hits: SrSnS2 (Ehull 0.045, gap 2.14), BaSnO2 (Ehull 0.0, gap 2.27; best ideal-gap hit so far). SrSnO2 Ehull 0.0 gap 3.13 (just above window). Stable but gap too low: CaSnSe2/SrSnSe2/BaSnSe2 (0.0, 0.17-0.23 eV), CaSnS2 (0.059, 1.48). Unstable: ZnSnS2 (0.12, 2.53), MgSnS2 (0.21, 2.46). ZAIS-like ordered Zn2/Mg2-(Cu/Ag)-(Al/Ga/In)S4 (11 evaluated): all unstable (Ehull 0.12-0.52) in kesterite ordering, gaps 1.4-3.5 -> falsified for this structure type. Caveat: Sn(II) oxide/sulfide gaps from the ML proxy may be unreliable (Sn2+ lone pair; disproportionation to SnO2/Sn possible), and ABO2 'chalcopyrite' prototype may be structurally unrealistic though hull says stable.

## [reflection] iteration 3 — 2026-10-11 08:17 UTC

Hypothesis: Sn(II) + large alkaline earth stabilizes; confirmed (Sr/Ba stable, Mg/Zn not; gap decreases S->Se strongly, rises toward O). ZAIS-type ordered alloys falsified (large mixed-site strain). Next iter: explore Sn(II)/Ge(II) variants - Ba/Sr SnO2-S mixed (can't mix anions in tool), Ca-Sn-O (CaSnO2 known), other alkaline earth-Sn(II) halides/oxide-chalcogenides; Sr/Ba-Ge/Sn with Te unlikely. Consider SrSnO2 gap tuning via Ba alloy (SrSnO2 3.13 vs BaSnO2 2.27) - Ba-rich mixing would give ~2.4-2.7. Avoid Mg/Zn with Sn(II), avoid ordered mixed-valent kesterites.

## [hypothesis] iteration 4 — 2026-10-11 08:17 UTC

Iter 4: extend ABX2 (A=Ca/Sr/Ba, B=Sn(II)/Ge(II), X=O/S) family that gave BaSnO2/SrSnS2. Test Ge(II) analogs, BaSnS2, and Ba/Sr-Ge-O/S; plus mixed A-site (Sr/Ba) not possible in tool, so also try Ag/Cu-based variants e.g. Cu/Ag + Sn/Ge + halide/chalcogen with In/Ga to see if anything novel. Expect Ge(II) to widen gaps vs Sn(II) (smaller lone-pair dispersion), Ba/Sr stabilizing. Aim gap ~2.4.

## [observation] iteration 4 — 2026-10-11 08:22 UTC

Iter 4: ABX2 (Ca/Sr/Ba, Sn/Ge, O/S) fully exhausted (all considered/SMACT-rejected). Nitride-phosphide kesterites vetoed (charge-imbalance, correct). NEW FAMILY HITS: Cu/Ag-P-S/Se tetrahedral I3-P-VI4 (Cu3PS4-type): CuAg2PS4 (Ehull 0.02, gap 2.45 - ideal), CuAg2PSe4 (0.000, 2.15), Cu2AgPSe4 (0.045, 2.14); calibration Cu3PS4 (known) 0.0, 1.88 (so model gives plausible gap). Ordered III/III' alloy: AlGa(AgS2)2 = Ag2AlGaS4 (0.0, 2.37) hit; AlGa(AgSe2)2 (0.132, 1.87), InGa(CuS2)2 (0.093, 2.00), AlZn2AgSe4 (0.274, 1.67) unstable. Critic correctly vetoed Cu+Ag(2+)-Ge imbalanced formulas (CuAg2GeS4 etc., actually 7+ vs 8-). 12 budget unspent: no further novel balanced candidates available from prototypes.

## [reflection] iteration 4 — 2026-10-11 08:22 UTC

Iter 4: Productive via charge-balanced cation-count thinking: kesterite has 4 cation sites summing to +8; I+I+I+V (P) and I+I+III+III' give new balanced sets. Hits: CuAg2PS4, CuAg2PSe4, Cu2AgPSe4, Ag2AlGaS4. Next (iter 5): look for further balanced 4-site combos (e.g. I+I+II+IV with Mg/Sr/Ba Ag-Ge-S already done; try I+II+II+... no), mixed Cu/Ag with Al/Ga/In in S (Cu-Ag mixing on I site not accessible); consider Ag2AlInS4/ Ag2GaInS4 are known. Possibly use iter 5 to re-check stability trends and finalize; ordered Se/Te alloys of Ga/Al fail (Ehull >0.09).

## [hypothesis] iteration 5 — 2026-10-11 08:22 UTC

Iter 5: all prior families exhausted (prototype library). New balanced 4-site class: (2,2,2,2) isovalent Zn/Mg ordered chalcogenide alloys MgZn3Se4, MgZnSe2, Mg3ZnSe4, Mg(Zn)Te analogs, S version Mg3ZnS4. Zn/Mg radii close -> low strain, ZnSe (2.7)/ZnTe (2.3) bulk gaps widen with Mg; expect Ehull small (<0.05) but wurtzite/zincblende polymorph issue vs rock-salt MgS/MgSe/MgTe (Mg-rich may go NiAs/rocksalt; MgTe wurtzite). Also AlGa(CuTe2)2, AlGa(AgTe2)2 as telluride probes (expect gap too low ~1.5). Not heavy-metal; ideal gap ~2.4 from Te-rich Zn-Mg.

## [observation] iteration 5 — 2026-10-11 08:24 UTC

Iter 5: Re-proposals of Cu3PS4-type, ordered III/III' alloys, chalcopyrite pnictide/halide and zincblende families all returned 'already considered' or SMACT-rejected -> prototype library exhausted. New family: isovalent (2,2,2,2) Zn/Mg ordered chalcogenides in kesterite ordering. Results: Mg3ZnS4 Ehull 0.000 but gap 3.395 (just above window; stable novel wide-gap, near-miss). Se/Te members all unstable: MgZn3Se4 0.21, MgZn3Te4 0.119, MgZnSe2 0.223 (1.95), MgZnTe2 0.131 (2.28), Mg3ZnSe4 0.414 (2.93), Mg3ZnTe4 0.27 (2.40) - gaps in window but not stable (zincblende/wurtzite-like ordering vs rocksalt/hexagonal competing phases). AlGa(CuTe2)2 (0.182, gap 0.10), AlGa(AgTe2)2 (0.139, 0.92): unstable and low gap, as expected. 11 budget left unspent (no further novel balanced candidates).

## [reflection] iteration 5 — 2026-10-11 08:24 UTC

Iter 5 reflection/campaign close: Zn/Mg alloy hypothesis falsified for Se/Te (large Ehull), partly confirmed for S (Mg3ZnS4 stable but gap too wide at 3.4). Best campaign hits (novel, Ehull<=0.05, gap in window): CuAg2PS4 (0.02, 2.45, ideal), Ag2AlGaS4 (0.0, 2.37), BaSnO2 (0.0, 2.27; caveat Sn(II) proxy), SrSnS2 (0.045, 2.14), CuAg2PSe4 (0.0, 2.15), Cu2AgPSe4 (0.045, 2.14), MgCu2SnS4 (0.02, 2.17), MgAg2SnS4/MgAg2GeS4/SrAg2GeS4/MgAg2GeSe4 (~1.87). Caveats: gaps are ML-HSE proxies, structural prototypes are idealized, and many 'hits' are Ag/Cu chalcogenides with covalent d-states, which are not ideal for blue/green QD emitters; Cu/Ag-based may have poor PLQY. Next steps if continued: experimental-style polymorph checks (e.g. Pn21 vs I-4 for Cu3PS4-type, enargite), phonon/dynamical stability of top hits, and expand prototype library to wurtzite-derived and non-tetrahedral structures.
