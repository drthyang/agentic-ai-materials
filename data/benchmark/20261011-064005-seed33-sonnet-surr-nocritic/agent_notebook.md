# Lab Notebook

## [hypothesis] iteration 1 — 2026-10-11 06:40 UTC

Kesterite family Cu2ZnSnS4 (gap ~1.5) analogs: cation/anion substitution (Ag for Cu, Cd/Mg for Zn, Ge/Si for Sn, Se/Te mixes) should keep gap in 1.1-1.7 and stay near hull. Also chalcopyrite variants (Cu/Ag-Ga/In-S/Se/Te). Propose large family, evaluate novel members.

## [reflection] iteration 1 — 2026-10-11 06:41 UTC

20 evaluated, all novel. Hits (gap 1.1-1.7, ehull<=0.05): CdAg2GeSe4 (1.28, 0.0), ZnAg2GeSe4 (1.12, 0.0), MgAg2GeTe4 (1.49, 0.025), MgAg2SnSe4 (1.59, 0.016), MgAg2SnTe4 (1.17, 0.038), ZnAg2GeTe4 (1.17, 0.028). Near: CaAg2GeSe4 gap 1.68 but hull 0.062. Failures: Si and Zr/Ti-type B-site (Si hull >0.08, Zr heavy hull for Mg/Ca); Zr-Cd gap 0.3. Trends: Se->Te lowers gap ~0.4-0.7; Mg/Ca raise gap; S gives ~1.9 (too wide). Next: mixed anion Se/S or Ag/Cu mixing to tune gap to 1.4 (e.g. Ag2CdGe(S,Se)4, Cu-Ag alloys with Cd/Mg), chalcopyrite family Ag-Ga/In-Se/Te, and non-chalcogenide families.

## [hypothesis] iteration 2 — 2026-10-11 06:41 UTC

Iter 2: Gap tuning around iteration-1 hits. (a) Cu analogs with Cd/Zn/Mg and Ge/Sn in Se/Te (Cu raises VBM -> lower gap than Ag; Cu-Mg-Sn-Se, Cu-Cd-Ge-Se etc. may be near 1.4 and stable). (b) Ag chalcopyrite-like in zincblende/chalcopyrite prototype: AgGaSe2/AgInSe2 are known, so test AgAl/Ga Te variants & Cu-Ga-Te. Evaluate novel only; use kesterite prototype with Cu and Ag substitution to include Cd/Mg/Zn, Ge/Sn, Se/Te.

## [observation] iteration 2 — 2026-10-11 06:42 UTC

Iter 2: 20 evaluated, all novel. Chalcopyrite proposals all known (skipped). Cu analogs with Mg/Ca/Mn are unstable (hull 0.07-0.14) — Cu does not like these II sites; gaps 1.1-1.4 (MgCu2SnSe4 1.38 but hull 0.071). Sr/Ba (large II cation, non-kesterite relaxed) are stable: SrAg2GeSe4 gap 1.687 hull 0.003 (hit at edge), SrAg2SnSe4 1.701 hull 0.0 (just above window), SrCu2SnSe4 1.109 hull 0.050 (borderline), SrCu2SnTe4 0.87 hull 0, BaAg2GeTe4 0.70 hull 0, BaCu2GeTe4 0.50 hull 0.034. Tellurides with Sr/Ba too narrow (0.1-0.9). Ca-Ag-Sn-Se 1.82 hull 0.051.

## [reflection] iteration 2 — 2026-10-11 06:42 UTC

Hypothesis partly held: Sr/Ba stabilizes Ag/Cu quaternaries, Cu lowers gap ~0.6 vs Ag. Gap ladder for Sr selenides: Ag 1.7, Cu 1.1 -> a Cu/Ag mix (e.g. Sr(CuAg)SnSe4) or Se/Te mix (SrAg2Ge(Se,Te)4, S/Se mix for Sr/Ba Cu variants like BaCu2SnSe4/BaCu2GeSe4, known) should land near 1.4. Next iter: try mixed anion/cation sites if tooling permits, Sr/Ba Cu-sulfides (SrCu2GeS4, SrCu2SnS4, BaCu2SnS4 ~ gap ~2?) and Ba-Ag-Sn-Se/S; also non-chalcogenide families (e.g., Zn/Cd-IV-pnictides, Cu-Sb/Bi chalcogenides, Ag-Bi-I) since chalcopyrite prototype yields only known compounds. Avoid Mg/Ca-Cu, Si, Zr.

## [hypothesis] iteration 3 — 2026-10-11 06:42 UTC

Iter 3: Sr/Ba stabilised Ag/Cu quaternaries. Gap ladder: Sr-Ag-Se ~1.7, Sr-Cu-Se ~1.1. Test Ba-Ag selenides (BaAg2SnSe4/GeSe4, expect ~1.6-1.8), Sr/Ba-Cu sulfides (S widens gap vs Se by ~0.6 -> Cu-S ~1.7-2?), and Cd/Zn-Cu-Ge/Sn-Se/S which could land near 1.4. Also Ag-Cu mixed via 'Cu': ['Cu','Ag'] not possible, so use Ag/Cu pairs. Avoid Mg/Ca-Cu, Si, Zr. Evaluate novel only.

## [observation] iteration 3 — 2026-10-11 06:44 UTC

Iter 3: 20 evaluated, all novel, ZERO hits. Alkali-alkaline-earth-M(IV) selenides (A2BMSe4): Ti/Zr variants hull 0.3-0.6 (unstable), gaps 2.2-2.9. Sn/Ge: K2BaSnSe4 (hull 0, gap 2.72), K2SrSnSe4 (0.005, 2.39) stable but too wide; BaNa2SnSe4 hull 0.058 gap 1.93; Na2SrSnSe4 0.099 gap 1.75. Ag-Ti/Zr-Se (Sr/Ba/Zn) hull 0.3-0.4, gap 2.2-2.4. SrAg2SnS4 hull 0 gap 1.72 (just above window), SrAg2GeS4 hull 0.013 gap 1.87. Sulfide Sr-Ag stays ~1.7 like selenide - S/Se gap sensitivity small for Sr-Ag.

## [reflection] iteration 3 — 2026-10-11 06:44 UTC

Iter 3 hypothesis falsified for alkali/Ti/Zr family (too wide or unstable; I should have predicted wide gaps for d0/closed-shell alkali chalcogenides and Ti/Zr instability in kesterite-type frame). Best vein remains Ag2-(Cd,Zn,Mg,Sr)-(Ge,Sn)-(Se,Te)4 with 6+ hits. Sr-Ag-Sn-S at 1.72 and SrAg2SnSe4 1.70 sit at window edge; a Te partial substitution would lower gap but tooling can't mix anions in-site. Next (iters 4-5): stay in proven Ag/Cu-Cd/Zn/Sr/Mg-Ge/Sn-Se family; possible new angles: Cd/Zn-Cu-Sn/Ge selenides not yet evaluated novelties, Cu-Ag mixed, Mn/Fe/Co II-site variants, or zincblende-derived pnictides (Zn-Sn-As2, Cd-Ge-As2 - known?). Avoid alkali, Ti, Zr.

## [reflection] iteration 4 — 2026-10-11 06:45 UTC

Iter 4: 20 evaluated, all novel. NEW FAMILY hits (famatinite-type I3-V-VI4, all hull 0): CuAg2AsSe4 (1.378, ideal), CuAg2SbSe4 (1.457), Cu2AgBiS4 (1.587), Ag3SbSe4 (1.665), Ag3AsSe4 (1.681). Near-window: Ag3SbS4 1.79, Cu2AgSbS4 1.74, CuAg2SbS4 1.86; Cu2Ag-Se with Sb/As gap only 0.43 (Cu-rich, narrow), Cu2AgBiSe4 0.96 hull 0.009; P variants wide/less stable. Gap ladder: more Ag -> wider; Se<S. Fe/Co II-site Ag selenides failed (hull 0.056-0.078, gaps ~0-0.8); MgCu2SnS4 gap 2.17 hull 0.02. Zincblende prototype yields only binaries (useless). Next (iter 5): explore Ag/Cu-Bi/Sb mixed in famatinite with Se (e.g. Cu-Ag-Bi-Se Ag-rich — Ag3BiSe4 failed SMACT), Te-containing mixes, and other I3-V-VI4 or sulvanite-type. Test Cu2AgSbTe4/Ag3SbTe4 (not evaluated, likely too narrow).

## [hypothesis] iteration 5 — 2026-10-11 06:46 UTC

Iter 5: Extend famatinite I3-V-VI4 hits (CuAg2AsSe4 1.38, CuAg2SbSe4 1.46). Fill untested neighbors: CuAg2/Cu2Ag with As/Sb/Bi and S/Se/Te (e.g. Cu2AgAsS4, CuAg2AsS4, Cu2AgAsSe4, CuAg2BiS4/Se4, Ag3BiS4, Te variants, Ag-As-S). Expect Ag-rich selenides/Te-Ag near 1.1-1.5; Bi lowers gap vs Sb. Also Cu-Ag II-IV variants with Cd/Zn Sn selenides. Novel only.

## [reflection] iteration 5 — 2026-10-11 06:47 UTC

Iter 5: Kesterite/famatinite space nearly exhausted (almost all proposals 'already considered'). Evaluated 11 novel: NEW HIT KBiTe2 (gap 1.296, hull 0.003) - alkali-Bi-telluride. KSbTe2 stable but 0.55. Te famatinites too narrow (0.3-0.44; Cu2AgBiTe4 hull 0.073). CaAg2(Ge,Sn)S4 unstable & wide (2.1-2.3, hull 0.07-0.09). K/Na-Ga-Se2 and NaGaS2 stable but wide (2.2-3.8); KAsS2 2.45. Overall campaign hits: CdAg2GeSe4, ZnAg2GeSe4, Mg/Ag tellurides/selenides, SrAg2GeSe4, CuAg2AsSe4 (1.38), CuAg2SbSe4, Cu2AgBiS4, Ag3SbSe4, Ag3AsSe4, KBiTe2. Lesson: A-Bi-Te (ALS-type) family is promising; wasted 9 budget units because tooling rejects already-seen formulas and limited prototypes. Future: Na/K/Rb-Bi/Sb mixed Te/Se, Ag/Cu-alkali-Bi chalcogenides.
