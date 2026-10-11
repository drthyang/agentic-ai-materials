# Lab Notebook

## [hypothesis] iteration 1 — 2026-10-11 06:24 UTC

Kesterite Cu2ZnSnS4 (gap ~1.5) family: isoelectronic substitutions (Ag for Cu, Cd/Mg for Zn, Ge/Si for Sn, Se/S mixes) tune gap around 1.4. Expect Ag2ZnSnSe4, Cu2CdSnSe4, Cu2ZnGeSe4, Cu2CdGeS4 etc. to hit window; many are known so we focus on those novel. Also chalcopyrite CuInSe2 variants (CuGaTe2, AgInSe2 etc.) as second family.

## [observation] iteration 1 — 2026-10-11 06:25 UTC

Evaluated 18 novel kesterite-derived. Hits (gap 1.1-1.7, Ehull<=0.05): CdAg2GeSe4 (1.28, 0.000), ZnAg2GeSe4 (1.12, 0.000), MgAg2SnSe4 (1.59, 0.016), ZnAg2GeTe4 (1.17, 0.028), MgAg2SnTe4 (1.17, 0.038). Near misses: MgCu2SnSe4 (1.38 but Ehull 0.071). Sulfides too wide (1.9-2.2), tellurides too narrow for Cu, Si compounds unstable (>0.13), Mg-Cu Ge/Te unstable. Ag-based selenides best; Ag>Cu for stability when Mg/Cd substituted.

## [reflection] iteration 1 — 2026-10-11 06:25 UTC

Hypothesis held for Ag2-M-(Ge,Sn)-Se4. Next: mixed anions (S/Se) for MgAg2SnS4/Se4 tuning toward 1.4, Cd/Zn Ag2 SnSe4 variants (known - skip), chalcopyrite Ag/Cu with Ga/In and Se/Te, and Na/K-containing or other families for exploration. Avoid Si compounds. Did not spend the last 2 relaxations (only 18 novel good candidates chosen).

## [hypothesis] iteration 2 — 2026-10-11 06:25 UTC

Iter 2: Ag2-M-(Ge,Sn)-Se4 gives gaps 1.1-1.3 (Zn/Cd Ge) and 1.59 (Mg Sn). Anion mixing S/Se (Vegard-like bowing) should push Zn/Cd-Ag2GeSe4 up from 1.12-1.28 toward 1.4, and Se/Te mixing should pull MgAg2SnSe4 (1.59) down toward 1.4. Also mix cations on Ge/Sn sites (Ge/Sn) and Zn/Cd/Mg. Compose via kesterite prototype with multi-element substitution lists; ordered mixed anion cells may be filtered, so also test pure novel members.

## [observation] iteration 2 — 2026-10-11 06:27 UTC

Mixed-anion substitution not supported by propose_candidates (single replacement only); chalcopyrite and zincblende proposals nearly all known -> skipped. Evaluated 20 novel Ag2-M-IV-Se4 with M=Ca,Sr,Fe,Co,Ni, Ti/Zr(IV-site), BaCu2(Sn,Ge)Te4, CuBiTe2. Hits (gap 1.1-1.7, Ehull<=0.05): SrAg2GeSe4 (1.687, 0.003), NiAg2GeSe4 (1.648, 0.000), NiAg2SnSe4 (1.676, 0.000). SrAg2SnSe4 stable (0.000) but gap 1.701 (just outside). CaAg2GeSe4 gap 1.68 but Ehull 0.062; CaAg2SnSe4 0.051/1.82. Fe/Co analogs: metallic/small gap, unstable. Ti/Zr-on-IV-site with M2+ very unstable (0.37-0.49). BaCu2SnTe4 stable but gap 0.14; BaCu2GeTe4 0.5. CuBiTe2 unstable. Caveat: Ni2+ kesterite gaps in ML may be unreliable (d8, likely spin/ligand-field effects; verify). Gaps at upper edge (~1.65-1.7) for large cations; none near 1.4.

## [reflection] iteration 2 — 2026-10-11 06:27 UTC

Total now 8 hits across 2 iterations, but all cluster either 1.1-1.3 (Zn/Cd Ge Se) or 1.6-1.7 (Mg/Sr/Ni). To reach 1.4 need intermediate: cannot do ordered anion mixing via tool; try cation-site mixing is also unsupported. Next: single-substitution families whose gaps lie between, e.g. Ag2-Cd-Sn-Se4 / Ag2ZnSnSe4 (already considered, check results?), Cu2-Sr/Ba with Ge/Sn Se4 (BaCu2SnSe4 known), SrCu2GeSe4/SrCu2SnSe4 (gap likely ~2), Ag2 Sr tellurides (SrAg2GeTe4, SrAg2SnTe4 maybe ~1.2-1.4), CaAg2 tellurides, NiAg2 tellurides. Avoid Fe/Co/Ti/Zr. Explore new prototypes beyond kesterite (e.g. Na/K Cu/Ag chalcogenides) if tool permits.

## [hypothesis] iteration 3 — 2026-10-11 06:27 UTC

Iter 3: Gaps in Ag2-M-IV-Se4 sit at 1.1-1.3 (Zn/Cd) or 1.6-1.7 (Mg/Sr/Ni). Tellurides lower gap by ~0.4 eV (ZnAg2GeTe4 1.17, MgAg2SnTe4 1.17). Large-cation tellurides (Sr/Ca/Ba/Ni Ag2 Ge/Sn Te4) and Ag2 Cd/Zn SnSe4 / Cd-Mn variants could land 1.2-1.5. Also Mn (d5 high spin) analogs and Cd-Sn-Te. Literature search unhelpful (no direct data on these). Propose broad family via kesterite prototype with Ag, M, IV, Te/Se substitution.

## [observation] iteration 3 — 2026-10-11 06:28 UTC

Iter 3 (17 relaxations). Tellurides MAg2(Ge,Sn)Te4: Sr/Ca/Ni gaps 0.04-0.24 (metal-like), Ba 0.52-0.71 (Ehull 0.000-0.007) -> too narrow, no hits. Cu-Se: SrCu2SnSe4 gap 1.109, Ehull 0.050 (borderline hit); CaCu2GeSe4 1.20 but Ehull 0.121; CaCu2SnSe4 0.94/0.108; Cu2NiGeSe4 gap 0.26 (Ehull 0.041). Ag sulfides: SrAg2SnS4 1.72/0.000 (just outside window), SrAg2GeS4 1.87/0.013. Cu sulfides: SrCu2SnS4 (known, calibration) 2.75/0.0; CaCu2SnS4 2.70, CaCu2GeS4 2.56 unstable. Strong gap ordering: Cu-S ~2.7 > Ag-S 1.7-1.9 > Ag-Se 1.1-1.7 > Cu-Se ~1.1 > Te <0.7. No gap near 1.4 found from single substitutions.

## [reflection] iteration 3 — 2026-10-11 06:28 UTC

Hypothesis (Te lowers gap into window for large-M) falsified: Te overshoots to <0.7 eV. Only marginal new hit SrCu2SnSe4. Gap landscape is bracketed: Ag-Se (1.1-1.7) is the productive layer; SrAg2SnS4 (1.72) and SrAg2SnSe4 (1.70) sit just above 1.7. Next iteration: need intermediate—try Ag-Se with M in between Cd/Zn(1.1-1.3) and Mg (1.59), e.g. Mn/Cd-Sn Se variants already done; consider non-kesterite families (Ag/Cu-Sb/Bi chalcogenides, ABX2 chalcopyrite Ag-Ga/In-Se, Na/K-containing) or zincblende-derived pnictides since tool can't do mixed anions. Avoid Ca compounds (unstable), Te with Sr/Ca/Ni, Cu sulfides.

## [observation] iteration 4 — 2026-10-11 06:29 UTC

Iter 4 (20 relaxations). II-IV-V2 chalcopyrites all known; Ag/Cu-kesterite space mostly exhausted. New family: alkali kesterites A2-M-IV-X4 (A=Na,K) all novel. HITS: Na2CdSnTe4 (gap 1.367, Ehull 0.032), K2ZnSnTe4 (1.573, 0.000), KBiTe2 (1.296, 0.003, chalcopyrite-proto novel). Other alkali: selenides stable (Ehull 0-0.03) but gaps 1.96-2.5; Na2MgSnSe4 0.055; K2CdSnTe4 0.86, K2CdGeTe4 0.88 (too narrow, stable), K2ZnGeTe4 1.90, Na2ZnSnTe4 2.05, Na2CdGeTe4 1.74/0.021; KSbTe2 0.55 stable; NaGaS2/NaAlS2/KAlS2 wide (3-4.6). MnAg2GeS4 2.24, Ehull 0.079.

## [reflection] iteration 4 — 2026-10-11 06:29 UTC

Alkali-tellurium kesterites are productive: closed-shell alkali lifts gap vs Cu/Ag; Te lowers it; gap ordering Zn>Cd (Sn: Na2CdSnTe4 1.37 vs K 0.86 - K lowers gap vs Na) and Ge>Sn. Next (iter 5): Rb/Cs analogs unavailable (palette), so try Na/K mixes: Na2ZnSnTe4 2.05 / K2ZnSnTe4 1.57 / K2CdSnTe4 0.86 -> Mg-Te variants (K2MgSnTe4, Na2MgSnTe4, K2MgGeTe4), Na2ZnGeTe4, Ca/Sr/Ba-based alkaline-earth analogs, and Sn->Si. Also other Bi/Sb alkali tellurides (NaBiTe2 known), Na/K-Bi-Se ternaries.

## [hypothesis] iteration 5 — 2026-10-11 06:30 UTC

Iter 5: Alkali-Te kesterites productive (Na2CdSnTe4 1.37, K2ZnSnTe4 1.57). Gap tuning: Zn>Cd, Ge>Sn, Na>K. Try Mg/Mn/Ca/Sr/Ba variants, Na2ZnGeTe4-type, K2MgSnTe4, K2ZnGeTe4 (1.90 done), plus Na/K-Bi/Sb chalcopyrite-proto I-V-VI2 (KBiTe2 1.30 hit; NaBiTe2 known; KBiSe2, NaSbTe2, KBiS2, NaBiSe2). Expect K2MgSnTe4 ~1.7-2, Na2MnSnTe4 / K2MnSnTe4 could be ~1.4 (d5), Ba/Sr alkaline earth with alkali not charge balanced; instead use Ag/Na mix not possible. Focus on novel members.

## [observation] iteration 5 — 2026-10-11 06:31 UTC

Iter 5 (19 relaxations). K-alkaline-earth/Mn tellurides in kesterite proto are a rich family. HITS: K2CaGeTe4 (1.421, Ehull 0.019 - best near 1.4), K2CaSnTe4 (1.118, 0.033), K2SrGeTe4 (1.216, 0.013), K2SrSnTe4 (1.199, 0.012), K2BaGeTe4 (1.566, 0.000), K2BaSiTe4 (1.642, 0.000), K2CdSiTe4 (1.235, 0.000), K2MnSiTe4 (1.455, 0.045), Na2CaSnTe4 gap 1.458 but Ehull 0.169 (no). Misses: Na2CaGeTe4 1.73/0.0; K2MnGeTe4 1.10/0.002 (borderline), K2MnSnTe4 0.65, Na2MnXTe4 0.95-1.09, K2ZnSiTe4 2.07, Na Si compounds unstable, K2SrSiTe4 unstable. Trends: K stabilizes vs Na for large M; Ba>Sr>Ca in gap for Ge; Ge>Sn by ~0.1-0.3.  Caveat: kesterite structure assumed for large Ca/Sr/Ba, true ground state may differ; Ehull from CHGNet-ML.

## [reflection] iteration 5 — 2026-10-11 06:31 UTC

Hypothesis (alkali-Te kesterites with new M and IV choices give ~1.4 gaps) held strongly: ~8 new hits incl. K2CaGeTe4 at 1.42 eV, Ehull 0.019. Across campaign, best candidates: K2CaGeTe4, Na2CdSnTe4 (1.37), CdAg2GeSe4 (1.28), K2CdSiTe4 (1.235), KBiTe2 (1.30). Future work: verify structures (competing non-kesterite polymorphs for K2AeMTe4, e.g. K2BaSnTe4-like), mixed Ca/Sr or Ge/Sn alloys to fine-tune, defect/absorption checks with higher-level theory. Zr/Ti-IV-site variants unspent as earlier iterations found them unstable.
