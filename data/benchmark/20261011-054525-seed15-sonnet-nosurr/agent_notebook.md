# Lab Notebook

## [hypothesis] iteration 1 — 2026-10-11 05:45 UTC

Kesterite family I2-II-IV-VI4: CZTS gap ~1.5, CZTSe ~1.0. Substituting Zn->Cd/Mg, Sn->Ge/Si, Cu->Ag, S<->Se mixes tunes gap by cation/anion size and electronegativity. Expect many in 1.1-1.7 eV; many known (CZTS, CZTSe, CZGS, Ag2ZnSnS4) so I only evaluate novel ones.

## [observation] iteration 1 — 2026-10-11 05:48 UTC

18 novel evaluated (Ag2-II-IV-VI4 kesterite-type). Hits (gap 1.1-1.7, hull<=0.05): CdAg2GeSe4 (1.28, hull 0.0) best; ZnAg2GeSe4 (1.12, 0.0); MgAg2GeTe4 (1.49, 0.025); MgAg2SnSe4 (1.59, 0.016); ZnAg2GeTe4 (1.17, 0.028). Misses: Si analogs unstable (hull 0.08-0.19); Ca analogs unstable; sulfides Mg-Ag2-Sn/GeS4 stable but gap ~1.87-1.89; CdAg2GeTe4 gap 0.48; ZnAg2SnTe4 0.60. Chalcopyrite Ag variants all known (not evaluated). Trends: Te lowers gap ~0.8 vs Se for Cd/Ca but not Zn; Si destabilizes; Ge/Sn good. 2 relaxations unspent.

## [reflection] iteration 1 — 2026-10-11 05:48 UTC

Hypothesis held: Ag-kesterite-type selenides/tellurides with Ge/Sn give stable ~1.1-1.6 eV gaps. Next: mixed-anion (S/Se) Zn/Cd/Mg Ag2 Ge compounds to push ZnAg2GeSe4 up toward 1.4, Cu/Ag mixed cation, and exploring other families (Na/K-based chalcogenides, nitrides/phosphides on zincblende) for exploration. Note I should check structural reality (kesterite assumed; real Ag2CdGeSe4 may be different polymorph, e.g. Pmn21 wurtzstannite) and unbudgeted candidates should be used next time.

## [observation] iteration 2 — 2026-10-11 05:54 UTC

Iter 2: 18 novel evaluated, 2 relaxations unspent (no more novel ideas worth it). Cu2-Mg-Ge/Sn-Se4: MgCu2SnSe4 gap 1.38 but hull 0.071 (miss); MgCu2GeSe4 1.10/0.136; SrCu2SnSe4 1.11/0.050 (borderline); MgCu2SnS4 hull 0.02 but gap 2.17; MnCu2GeSe4 0.93/0.10. Alkali chalcopyrite-type NaGaSe2 2.20 (hull 0.017), NaGaS2 3.83 -> too wide. Ti/Zr kesterite-type: TiZn(AgS2)2 gap 1.55 hull 0.0 (HIT); TiMn(AgS2)2 gap 1.48 hull 0.0 (HIT, Mn magnetic - gap unreliable); Zr analogs gaps 0.2-0.65 (too small, hull 0); TiZn(CuS2)2 2.66; Se Ti analogs and Cd/Mg Ti analogs hull 0.35-0.41 unstable. Caveat: hull 0.0 for Ti/Zr quaternaries is suspicious (sparse competing phases in Ag-Ti-Zn-S MP data; also Ti4+ tetrahedral in kesterite is chemically odd - octahedral preferred), so treat as unverified. Calibration: ZnGeAs2 etc pnictide chalcopyrites all known.

## [reflection] iteration 2 — 2026-10-11 05:54 UTC

Hypothesis (Cu/mixed variants of Ge/Sn kesterites) mostly falsified: Cu Mg analogs are marginally unstable or too wide-gap. New lead: Ti-containing Ag2 sulfide quaternaries (TiZnAg2S4, TiMnAg2S4) hit window but need skepticism on hull and structure (Ti would prefer octahedral; kesterite prototype forced). Next: check literature on Ag2ZnTiS4-type / compete with binaries (Ag2S, TiS2, ZnS); try Ag-Zn-Ge-S/Se mixed-anion for fine tuning; explore non-tetrahedral families (e.g., Ba/Sr-Cu/Ag-Sb/Bi chalcogenides, halide perovskite-like Cs-free: Ag-Bi-I, Cu-Sb-S) with zincblende prototype tools limited. Prototype tool only supports 3 structures, so mixed-anion needs workaround.

## [hypothesis] iteration 3 — 2026-10-11 05:55 UTC

Iter 3: Mixed-anion and mixed-cation Ag2-(Zn,Cd,Mg)-(Ge,Sn)-(S,Se,Te)4 kesterite-type. ZnAg2GeSe4 (1.12) and CdAg2GeSe4 (1.28) sit at the edge; S substitution on Se (smaller anion, lower VBM) should raise gap toward 1.4, Sn->Ge partially tunes. Also Ag2-Cd-Sn-Se4, Ag2-Zn-Sn-Se4 and Cd/Zn-Ag2 Sn S4 as fill-ins, plus Te/Se mixes for Mg. Mixed anion formulas may be reported by the tool; try.

## [observation] iteration 3 — 2026-10-11 05:59 UTC

Iter 3: Ag2-II-IV-VI4 kesterite family is exhausted (only MgAg2SnTe4, CdAg2SnTe4 novel). MgAg2SnTe4: gap 1.17, hull 0.038 (HIT, marginal); CdAg2SnTe4 0.41 (miss). II-IV-V2 pnictide chalcopyrites (Sb with Mg/Zn/Cd, As/Sb with Ca/Sr): all unstable (hull 0.12-0.30) and mostly wrong gap; falsified (ZnSiSb2 gap 1.2 but hull 0.28). Alkali I-III-VI2: KGaSe2 gap 2.18 hull 0 (too wide); KSbTe2 0.55 hull 0; KBiTe2 gap 1.30, hull 0.003 (HIT, novel vs MP, best of iteration; MP only has K3BiTe3). Caveat: KBiTe2 forced into chalcopyrite-type prototype; true ground state probably layered/rocksalt-ordered (alpha-NaFeO2-like) - gap may differ. 17 relaxations used, 3 unspent (no novel candidates left).

## [reflection] iteration 3 — 2026-10-11 05:59 UTC

Pnictide hypothesis falsified; alkali-Bi-chalcogenide idea productive. Next (iter 4): explore I-V-VI2 / Bi-based chalcogenides beyond the prototype set (e.g. mixed K/Na/Ag-Bi-Se/Te, Ag-Bi-I, Cu-Sb-S via zincblende/chalcopyrite relabeling), and check KBiTe2 polymorph via literature. Also consider mixed-cation Mg/Ag-Sn-Te tuning to lower MgAg2SnTe4 hull. Kesterite Ag2 family should be left alone.

## [hypothesis] iteration 4 — 2026-10-11 05:59 UTC

Iter 4: Extend KBiTe2 lead: I-V-VI2 (Na,K,Ag,Cu)(Bi,Sb)(S,Se,Te)2 using chalcopyrite prototype relabeling. Lone-pair Bi3+ chalcogenides (NaBiS2 known, literature) have gaps 1.0-1.5; K/Na with Se/Te should fall in window. Also Ca/Sr/Ba-based variants not feasible. Evaluate only novel ones; caveat prototype is not true ground state (rocksalt-ordered) so hull may be inflated.

## [observation] iteration 4 — 2026-10-11 06:02 UTC

Iter 4: Bi/Sb I-V-VI2 chalcopyrite relabelings all "already considered" (no new). Zincblende prototype yields only binaries. Switched to alkali kesterite-type A2-II-IV-VI4 (A=Na,K), 20 evaluated, all novel. HITS: K2ZnSnTe4 gap 1.57 hull 0.0; Na2CdSnTe4 gap 1.37 hull 0.032 (best gap). Near-misses: K2CdSnTe4 0.86/0.0; Na2CdGeTe4 1.74/0.021; K2ZnGeTe4 1.90/0.0. Selenides all 1.96-2.49 (too wide) though stable (hull 0-0.03). Mg and Ba/Sr analogs unstable (0.055-0.12). K2TiZnTe4 gap 0.0 (metal). Trend: Te + Sn + Cd lowers gap; Zn->Cd lowers ~0.7 in K, 0.7 in Na Sn Te. Caveat: kesterite-type forced for large alkali; real structure likely different (e.g., K2ZnSnTe4 might be non-tetrahedral/ chain), hull 0.0 vs sparse MP phase space.

## [reflection] iteration 4 — 2026-10-11 06:02 UTC

Alkali kesterite-type tellurostannates productive: two new hits. Next (iter 5): mixed Zn/Cd or Na/K tuning toward 1.4 (e.g. K2(Zn0.5Cd0.5)SnTe4, NaK mixed) — prototype tool cannot do mixes directly; try Rb/Cs not in palette. Remaining ideas: Na2/K2 with Mn/Fe/Co II sites (magnetic, unreliable), Na2CdSnTe4 hull refinement. Also check that real structures of A2MSnTe4 differ. Hypothesis (alkali analog gap raised, Te lowers into window) partially held: only Te+Sn with Zn/Cd.

## [hypothesis] iteration 5 — 2026-10-11 06:02 UTC

Iter 5: Fill remaining alkali-A2-M-IV-Te4 space: K2CdGeTe4/Se4 (Cd lowers gap vs Zn K2ZnGeTe4 1.90 -> maybe ~1.2-1.4), Mn/Fe II-site analogs (Mn2+ d5 wide-gap high-spin; gaps unreliable but novel), Ti/Zr-Mn variants as exploratory. Prior: Te+Cd+Ge/Sn tunes into window. Caveat: Mn/Fe magnetic, treat gaps skeptically.

## [observation] iteration 5 — 2026-10-11 06:04 UTC

Iter 5: 16 evaluated, all novel. HITS (gap 1.1-1.7, hull<=0.05): Na2MnSnSe4 1.115/0.0; Na2MnGeSe4 1.646/0.008; Na2ZrMnTe4 1.493/0.0 (Zr4+ tetrahedral and Mn magnetic - suspect). Near: Na2MnGeTe4 1.09/0.043, Na2MnSnTe4 0.95/0.046. Misses: K2CdGeTe4 0.88/0, K2CdGeSe4 2.41, K2ZrCdTe4 2.12, K2MnSnTe4 0.65, Fe analogs metallic/small, Ti analogs metallic. Hull 0.0 for Zr/Ti variants suspicious (sparse competing phases). Caveat: Mn gaps from non-spin-polarized/magnetic uncertain, kesterite-type forced for alkali.

## [reflection] iteration 5 — 2026-10-11 06:04 UTC

Iter 5: Hypothesis partially held: Cd lowers gap too much with K Ge Te (0.88), Mn selenides land in window but Mn magnetism makes gaps unreliable. Best overall candidates of campaign (trustworthy, non-magnetic): CdAg2GeSe4 (1.28, 0.0), ZnAg2GeSe4, K2ZnSnTe4 (1.57), Na2CdSnTe4 (1.37, 0.032), KBiTe2 (1.30), MgAg2SnTe4. Future: validate with spin-polarized DFT/HSE, check real polymorphs (wurtzstannite, layered), mixed-anion/cation alloys for fine tuning to 1.4. 4 relaxations unspent (remaining novel candidates mostly Ti/Zr-Mn/Fe low-value).
