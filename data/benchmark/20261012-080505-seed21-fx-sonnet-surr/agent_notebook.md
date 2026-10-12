# Lab Notebook

## [hypothesis] iteration 1 — 2026-10-12 08:05 UTC

Kesterite family Cu2-M-X-S4 variants: isoelectronic substitution (Zn->Cd/Mg, Sn->Ge/Si, Cu->Ag, S->Se) tunes the gap. CZTS ~1.5 eV, CZTSe ~1.0; mixing S/Se or Ag/Cd variants should land in 1.1-1.7. Propose broad family, pick novel ones.

## [observation] iteration 1 — 2026-10-12 08:06 UTC

Batch1 (Ag2-AE/M-Si/Ge-Se4 kesterite-type, 12 evaluated): HITS BaSi(AgSe2)2 = Ag2BaSiSe4 gap 1.42, Ehull 0.026; Ag2SrSiSe4 gap 1.69, Ehull 0.021. Others: Ge variants gap ~0 (too small); Cd/Mg Si: 0.75/1.84 stable; Ca ehull>0.05; Zr variants unstable (0.09-0.17). Batch2 (Cu2-Ba/Sr-Si/Ge-Se/Te4, 6): all Ehull>0.05, Te gaps too small; Cu2BaSiSe4 gap 1.81, ehull 0.054; none hit. Note the proposer substitution is a cross-product; known BaCu2GeSe4/SrCu2GeSe4 skipped. Caveat: kesterite prototype for large Ba/Sr likely not true ground state (real compounds are other structure types), so DFT hull values may not reflect polymorph competition.

## [reflection] iteration 1 — 2026-10-12 08:06 UTC

Hypothesis partly held: Si (not Ge) on tetrahedral site opens gap; Ba/Sr + Ag + Si + Se gives 1.4-1.7 eV near hull. Ge variants metallic-like in this gap model. Next: tune Ag2BaSiSe4 with S/Se mixing, Ag2BaSi(S,Se)4, Ag2BaGe with S (raise gap), Ag2Ba(Si,Ge) alloys, Cd-Si-S etc. Also try other prototypes (chalcopyrite/zincblende) for variety. Didn't use last 2 relaxations.

## [hypothesis] iteration 2 — 2026-10-12 08:06 UTC

Iter 2: Refine Ag2-AE-Si-Se4 hits. (a) S/Se anion tuning: S raises gap, so Ag2BaSiS4, Ag2SrSiS4 wider; Ge-S variants (Ge gave ~0 gap with Se, S should open it) Ag2BaGeS4, Ag2SrGeS4, Ag2CdGeS4, Ag2ZnSiS4/Ge. (b) Sn variants with Se/S. Cd/Zn-Si-S. Anion S/Se mixing to interpolate 1.4. Target gap 1.1-1.7 with Ehull<=0.05; pick novel only.

## [observation] iteration 2 — 2026-10-12 08:07 UTC

Batch A (Ag-AE/Cd/Mg-Si/Ge/Sn-S4, 8 novel): HIT SrAg2SnS4 gap 1.667, Ehull 0.024. Others near-stable but gaps off: BaSi(AgS2)2 2.57/0.029; SrSi(AgS2)2 2.54/0.033; SrAg2GeS4 1.95/0.017; CdSi(AgS2)2 2.22/0.0; MgSi(AgS2)2 2.46/0.012; MgAg2GeS4 1.78/0.006 (just above window); MgAg2SnS4 0.69/0.011. Batch B (Ca/Sr Cu/Ag, 12 novel): all Ehull>0.05 (Ca too small for kesterite-type site, Cu-Ca/Sr worse); CaAg2SnSe4 gap 1.45 but Ehull 0.089 (unstable). Gap trends: S>Se by ~0.6-0.9 eV, Si>Ge>Sn, Cu(S) too wide.

## [reflection] iteration 2 — 2026-10-12 08:07 UTC

Ag-(Sr/Ba)-(Si/Sn)-chalcogen kesterite-type is the productive family: 3 hits total (Ag2BaSiSe4 1.42, Ag2SrSiSe4 1.69, Ag2SrSnS4 1.67). Ca and Cu analogues fail on stability. Next: Ba-Ag-Sn-S known (skipped); try mixed S/Se anions (e.g. Ag2SrGeS2Se2, Ag2MgGeS4-xSex which would bring 1.78 down to ~1.4 and MgAg2GeS4 is nearly on hull), Ag2Sr(Ge,Sn)S4 alloys, Ag2Mg(Ge,Sn) alloys; and new prototypes (chalcopyrite AgInS2-like, Ag-Sb/Bi chalcogenides). Mg-Ag-Ge-S/Se mixed anion is top priority.

## [observation] iteration 3 — 2026-10-12 08:09 UTC

Iter 3: chalcopyrite/zincblende proposals mostly known/trivial (novel ones NaGaS2/Se2, NaAlS2, AgSbAs2 likely wide/odd; skipped). Evaluated 20 novel kesterite-type Ag2-M-M'-X4. HIT: MgAg2SnSe4 gap 1.153, Ehull 0.043 (Se lowers MgAg2SnS4 0.69? non-monotonic: S 0.69 -> Se 1.15, gap-model noise). Near-stable but gap off: ZnAg2GeSe4 0.68/0.003; ZnSi(AgSe2)2 1.84/0.0; MnAg2GeS4 0.25/0.021; TiCd(AgS2)2 2.23/0.007; TiZn(AgS2)2 2.05/0.022; TiZn(AgSe2)2 1.89/0.014; TiCd(AgSe2)2 0.61/0.019; BaTi(AgS2)2 2.25/0.049; BaTi(AgSe2)2 2.03/0.035; TiMn(AgSe2)2 0.11/0.031. In window but unstable: ZrZn(AgS2)2 1.22/0.106; TiMn(AgS2)2 1.39/0.092; SrZr(AgS2)2 1.61/0.149. Zr variants generally unstable; Ti(IV) variants stable but gap 2+ (S) or ~1.9-2.0 (Se).

## [reflection] iteration 3 — 2026-10-12 08:09 UTC

Iter 3: one new hit (MgAg2SnSe4, 1.15/0.043, marginal). Total hits 4 in Ag-(Ba/Sr/Mg)-(Si/Sn)-chalcogen family. Ti-containing kesterite-types stable but gaps too wide; Mn/Zr give small gaps or instability. Proposer tools for other prototypes return mostly known binaries/ternaries; chalcopyrite novel members are wide-gap Na compounds. Next: explore Ag2Ba/Sr-Ti with Se/Te mix or Ti-Cu variants (gap lowered), Ag2BaSn-type Se alloys, Ti with Ba + Te; Mg-Ag-Sn-Se neighbors (Mg-Ag-Ge-Se-S alloys); mixed Zn/Cd on Ti site. Also verify tool allows mixed-anion formulas.

## [observation] iteration 4 — 2026-10-12 08:10 UTC

Iter 4: 20 evaluated (all novel). HIT: MgSi(AgTe2)2 = Ag2MgSiTe4 gap 1.627, Ehull 0.014. Near misses: ZnSi(AgTe2)2 1.717/0.001 (just above window); MgTi(AgS2)2 1.785/0.040; MgTi(AgSe2)2 1.52 but Ehull 0.053 (marginal fail). Failures: Ti/Zr/Fe-Te and Zr/Fe variants (gap ~0 or Ehull>0.07); CdSi(AgTe2)2 0.33/0.008; MgAg2GeTe4 0.87/0.015; Sr/Ba Si-Te 1.9-2.1 but Ehull ~0.07 (Te too large/soft for big AE in this prototype). Mo/W rejected by SMACT. Mixed-anion formulas not tested (proposer only gives pure-anion). Total hits: 5.

## [reflection] iteration 4 — 2026-10-12 08:10 UTC

Si tetrahedral + Te anion + small divalent (Mg/Zn) gives stable Ag tellurides with gaps 1.6-1.7; Ge lowers to 0.7-0.9, so Si/Ge alloys on MgAg2(Si,Ge)Te4 would give ~1.2-1.4 (target for iter 5), as would Zn/Mg mixing on divalent site with Si-Te. Ti-based stable but gaps off; Zr/Fe dropped. Alloys not reachable via the proposer directly (maybe try Si->Ge,Si list and see if it accepts). Last iteration: exploit Mg/Zn-Si/Ge-Te and Se/Te anion mixing, MgAg2SnSe4-type neighbors.

## [reflection] iteration 5 — 2026-10-12 08:11 UTC

Iteration 5: 20 evaluated, 0 new hits. Cu-Mg-(Si/Ge/Sn)-(S/Se/Te) kesterite-types near-stable (0.0-0.047) but gaps 0.2-0.7 (too small); MnCu2GeSe4 0.66/0.0. K-Ga/Al/Sb/Bi chalcopyrite-type: KGaSe2 3.3 and KAlS2 3.9 stable but wide; KSbTe2/KBiTe2 gaps 0.4-0.6, ehull ~0.05. Fe/Co/Ni Ag kesterite-types unstable (0.05-0.11) with gaps mostly <1 (CoSi(AgS2)2 1.89 but 0.10); Ca-Te unstable (0.08). Proposer rejects pure-anion alloys already considered; mixed-anion/alloy formulas not reachable. Campaign total: 5 hits (Ag2BaSiSe4 1.42/0.026; Ag2SrSiSe4 1.69/0.021; Ag2SrSnS4 1.67/0.024; Ag2MgSnSe4 1.15/0.043; Ag2MgSiTe4 1.63/0.014). Future: Si/Ge and Se/Te alloy tuning of Mg/Zn Ag tellurides, which proposer couldn't do.
