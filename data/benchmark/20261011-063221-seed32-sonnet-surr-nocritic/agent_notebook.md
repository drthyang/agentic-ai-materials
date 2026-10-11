# Lab Notebook

## [hypothesis] iteration 1 — 2026-10-11 06:32 UTC

Kesterite family: CZTS gap ~1.5 (S), CZTSe ~1.0. Substituting Zn->Cd/Mg, Sn->Ge/Si, Cu->Ag, and mixing S/Se/Te should tune the gap into 1.1-1.7 while keeping isoelectronic charge balance. Many known (CZTS, CZTSe, CZGeS etc.); target less-explored combos (Ag2CdGeS4, Cu2CdGeSe4, Cu2MgSnS4, Ag2ZnSnS4...). Propose broad family and screen for novelty.

## [observation] iteration 1 — 2026-10-11 06:33 UTC

16 evaluated. Novel hits in window & near-stable: CdAg2GeSe4 (Eg 1.28, Ehull 0), ZnAg2GeSe4 (1.12, 0), MgAg2SnSe4 (1.59, 0.016), MgAg2GeTe4 (1.49, 0.025), MgAg2SnTe4 (1.17, 0.038). Calibration ZnAg2SnSe4 (flagged known) 1.12, hull 0. Fails: Si-containing (hull 0.13-0.15, unstable), Cu-Mg-Ge-Se unstable (0.136). Te with Cd/Zn gap too small (0.4-0.6); S Mg too wide (1.87). Trends: Ag-kesterites stable; Mg widens gap ~0.5 vs Zn/Cd; Te lowers ~0.7 vs Se; Ge ≈ Sn.

## [reflection] iteration 1 — 2026-10-11 06:33 UTC

Hypothesis held for Ag-II-(Ge,Sn)-Se/Te. Next: unspent 4 relaxations (tool proposals only yielded these); explore Ag2-Mg/Cd-Ge-S (CdAg2GeS4 known), mixed Mg/Zn or Se/Te anion mixing for ~1.4 eV, and other families (chalcopyrite Ag-based, Cu-free). Si kesterites and Cu-Mg unfavorable — avoid. Note gap ceiling of PBE-ish ML may be noisy; Ehull near 0 for ZnAg2GeSe4/CdAg2GeSe4 are best leads.

## [hypothesis] iteration 2 — 2026-10-11 06:33 UTC

Iter 2: Extend Ag-kesterite leads. (a) Mixed S/Se anions in Ag2-Zn/Cd/Mg-Ge/Sn-(S,Se) to tune gaps to ~1.4 (Se-only ZnAg2GeSe4 1.12, CdAg2GeSe4 1.28, MgAg2SnSe4 1.59). Ag2-Cd/Zn-Sn/Ge-S likely wider (~1.7-2). (b) Ag/Cu mixing on cation site. (c) Chalcopyrite Ag-III-VI2 (AgInSe2 ~1.2, AgGaSe2 1.8) with Ga/In mixing and Te. Aim for novel compositions only.

## [observation] iteration 2 — 2026-10-11 06:35 UTC

Iter 2: 19 evaluated. Chalcopyrite Ag/Cu-III-VI2 and zincblende proposals all known (no spend). Zr-kesterites (Zr(Cd,Zn,Mg)(Ag,Cu)Se4/S4): hull 0 for several but gaps 0.07-0.65 (suspect metallic-like/ML artefact) -> out of window; Zr-S Cd and all Ti variants unstable (hull 0.35-0.48), MgZr(AgSe2)2 gap 1.58 but hull 0.46. MgAg2GeS4 hull 0.017, gap 1.89 (too wide). New: SrAg2GeSe4 (Eg 1.687, hull 0.003) - novel, in window edge; SrAg2SnSe4 (1.70, hull 0) borderline; CaAg2GeSe4 (1.68, hull 0.062) slightly unstable; CaAg2SnSe4 1.82, hull 0.051.

## [reflection] iteration 2 — 2026-10-11 06:35 UTC

Ti4+ doesn't fit kesterite; Zr gives tiny gaps. Alkaline-earth Ag2-AE-IV-Se4 family stable but gaps ~1.7 upper edge; Ba analog and Sr/Ba with Te could lower to ~1.3-1.4 (SrAg2GeTe4, SrAg2SnTe4, BaAg2GeSe4). Next iteration: Sr/Ba-Ag-Ge/Sn-Se/Te incl. Ba, and S/Se mix; also Cu-Sr/Ba analogs. Mixed-anion compositions not reachable via prototype tool; avoid saturated chalcopyrite/zincblende prototypes (all known).

## [hypothesis] iteration 3 — 2026-10-11 06:35 UTC

Iter 3: Sr/Ba-Ag2-(Ge,Sn)-(Se,Te)4 and Ba/Sr/Ca-Cu2 analogs. Sr Se gap ~1.69-1.70 at edge; Te lowers ~0.7 -> SrAg2GeTe4 may be ~1.0-1.2; Ba analogs and Cu analogs (Cu raises VBM, lowers gap ~0.3-0.5) may land 1.2-1.5. Also Cd/Zn mixed with Si-free group. Propose family via kesterite prototype with multi-element substitutions.

## [observation] iteration 3 — 2026-10-11 06:36 UTC

Iter 3: 18 evaluated. All AE-Ag/Cu-IV-Te4 (Sr, Ba, Ca) have gaps 0.02-0.87 (too small), though many hull<=0.03 (BaAg2GeTe4 0.0/0.705, SrCu2SnTe4 0.0/0.866, BaAg2SnTe4 0.007/0.52, BaCu2SnTe4 0.001/0.40). Ca-Cu/Ag-Te unstable (0.06-0.12). Cu-Se: SrCu2SnSe4 gap 1.109, hull 0.050 (borderline, novel); CaCu2GeSe4 gap 1.198 but hull 0.121; CaCu2SnSe4 0.944/0.108. Calibration BaAg2GeSe4 (known) 1.83, hull 0.006. S: SrAg2SnS4 1.72/0.0, SrAg2GeS4 1.87/0.013 (novel, slightly above window). No new in-window stable compound beyond marginal SrCu2SnSe4. Second proposal call forgot to include Se/Te substitution -> only S, wasted budget (2 left unspent).

## [reflection] iteration 3 — 2026-10-11 06:36 UTC

Gap trends in AE-Ag-IV-X4: S 1.72-1.87, Se 1.69-1.83, Te 0.1-0.7 (Sr/Ba); the Se->Te jump is too big, so a target of 1.4 needs mixed Se/Te (not accessible via tool) or Cu/Ag mixing. Best in-window novel leads overall: CdAg2GeSe4 (1.28, 0), ZnAg2GeSe4 (1.12, 0), SrAg2GeSe4 (1.69, 0.003), SrAg2SnSe4 (1.70, 0), MgAg2SnSe4 (1.59, 0.016), SrCu2SnSe4 (1.11, 0.05). Next (iter 4): try Cd/Zn-Ag-Sn analogs mixing with AE via substitutions of different prototypes (e.g., Sr-Cd mix not feasible); consider different families: Cu-free ternary pnictides/zincblende-derived (Zn3P2-like, CdSnP2, ZnSnP2-type via zincblende substitution), or Ag-Sb/Bi chalcogenides; make sure to specify anion substitution explicitly.

## [hypothesis] iteration 4 — 2026-10-11 06:36 UTC

Iter 4: new family — II-IV-V2 chalcopyrites (ZnSnP2 1.2-1.7, CdSnP2, ZnGeAs2, CdGeP2, MgSnP2, MgGeP2 etc.) and I-III-VI2/ I-V-VI2 (AgSbS2-like, CuSbSe2) via chalcopyrite prototype with Cu->Zn/Cd/Mg, In->Sn/Ge/Si, Se->P/As. Isoelectronic to III-V zincblende; Mg/Si widen gaps. Many known; screen for novel members and evaluate them, with explicit anion substitutions.

## [observation] iteration 4 — 2026-10-11 06:37 UTC

Iter 4: II-IV-V2 pnictide chalcopyrites all known (no spend); P variants fail SMACT. Switched to alkali-kesterite (A2-M-X-Se/Te4) via kesterite prototype, 20 evaluated, all novel. New in-window hits: Na2CuSbTe4 (Eg 1.278, hull 0.0), K2CuSbTe4 (1.301, hull 0.0), Na2CdSnTe4 (1.367, hull 0.032). Others: A2CuSbSe4 1.78-2.05 (hull 0); A2(Zn,Cd,Mg)(Ge,Sn)Se4 gaps 1.96-2.5, mostly hull<0.03 (Mg 0.055); Na2ZnGe/SnTe4 2.05-2.4; Na2CdGeTe4 1.74/0.021; K2CdSn/GeTe4 0.86-0.88/0.0; A2Cu(Ge,Sn)Se4 ~2.0 hull 0 (oxidation-state dubious). Trends: Te lowers gap ~0.6-1.0 vs Se; K lowers gap vs Na for Cd-Te; Sb5+/Cu+ Te best.

## [reflection] iteration 4 — 2026-10-11 06:37 UTC

Alkali-Cu-Sb-Te4 (sulvanite/kesterite-like, Cu+ Sb5+) is the most promising new family: stable and 1.3 eV. Next (iter 5): Rb/K/Na-Ag-Sb-Te4 and mixed A; Na/K-Cu-Sb-S4 won't work (gap wider); try Ag analogs (Na2AgSbTe4), Cu->Ag, Sb->Bi? (charge-balance fails). Also Na/K-Cd-Sn-Te with K/Na mixing not available; Na2CdSnTe4 hull 0.032 near-stable lead. Must explicitly include Ag in substitutions. Caveat: CHGNet/ML gap accuracy and Cu-Ge/Sn alkali compounds have unbalanced charges so likely artefacts.

## [hypothesis] iteration 5 — 2026-10-11 06:37 UTC

Iter 5: Extend A2-M(I)-Sb-X4 (Na2CuSbTe4 1.28, K2CuSbTe4 1.30, hull 0). Test Ag analogs (Ag lowers VBM -> wider gap), Sb->As/Bi, Se/S/Te variants, Rb absent from kesterite prototype so Na/K/Ca/Sr/Ba not Rb. Include Na2AgSbTe4, K2AgSbTe4, Na2AgSbSe4, Na2CuAsTe4, Na2CuBiTe4, and Cu/Ag with Sn-Cd-Te near-stable family. Explicit anion lists. Literature search gave nothing directly on these -> likely unexplored.

## [observation] iteration 5 — 2026-10-11 06:39 UTC

Iter 5: 14 evaluated, all novel, all hull<=0.003. In-window: Na2AgSbTe4 (1.367, hull 0), K2AgSbSe4 (1.24, 0), Na2AgSbSe4 (1.677, 0 edge), KBiTe2 (1.296, 0.003). Out: K2AgSbTe4 0.99; KSbTe2 0.55; As variants 1.8-2.4; Sb sulfides 2.4-2.7; Na2CuSnS4 2.88 (charge-unbalanced, dubious). Trends: Ag raises gap vs Cu for Te (1.28->1.37); K lowers gap vs Na by ~0.4; Se->Te lowers ~0.3-0.4; As widens vs Sb. 6 relaxations unspent: Cu-AE sulfide and other proposals were all 'already considered' or known.

## [reflection] iteration 5 — 2026-10-11 06:39 UTC

Hypothesis held: alkali-(Cu/Ag)-Sb(V)-chalcogenide kesterite-type is a stable novel family with tunable gap; Na2AgSbTe4 (1.37) is the closest to 1.4 eV, K2AgSbSe4 (1.24) and KBiTe2 (1.30) are also strong. Caveats: ML gaps/CHGNet hull only, structure assumed kesterite (real ground states likely differ, e.g. Cu3SbS4-like/other polymorph); hull computed vs MP so novel-vs-known may reflect database gaps. Next steps: DFT/HSE verification, competing polymorph checks, mixed Na/K and Se/Te anion mixing to land exactly 1.4 eV (not reachable by tool).
