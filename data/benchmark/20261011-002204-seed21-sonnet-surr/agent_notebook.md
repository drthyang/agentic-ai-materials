# Lab Notebook

## [hypothesis] iteration 1 — 2026-10-11 00:22 UTC

Kesterite family: Cu2ZnSnS4 gap ~1.5 eV. Substituting Zn->Cd/Mg, Sn->Ge/Si, S->Se/Te, Cu->Ag tunes gap; Se analogues lower gap, Ag raises. Expect Cu2CdSnSe4-like (known), Ag2ZnSnSe4, Cu2MgSnS4, Cu2ZnGeSe4 etc. Target novel members with gap 1.1-1.7 and low ehull.

## [observation] iteration 1 — 2026-10-11 00:28 UTC

12 evaluated (all Ag kesterite-type). Hits: CdAg2GeSe4 gap 1.28 ehull 0.0 (best); MgAg2GeTe4 gap 1.49 ehull 0.025. Others: Si analogues unstable (ehull 0.08-0.19); Ca analogues marginal; Te Cd gap 0.48 too low; ZrCd(AgSe2)2 stable but gap 0.3. Surrogate had no data.

## [reflection] iteration 1 — 2026-10-11 00:31 UTC

Novel hits in window & near-stable: CdAg2GeSe4 (1.28, 0.0), MgAg2GeTe4 (1.49, 0.025), MgAg2SnSe4 (1.59, 0.016). CdAg2SnSe4 (flagged known, calibration) gave 1.26/0.0 consistent w/ Ag-Cd-selenide trend. Sulfides Mg too wide (1.9). Next: mixed Cu/Ag, Cd-Mg alloys, Cu-containing Ge/Sn Se with Cd/Mg to hit ~1.4; target Mg/Cd Se Te mixes; explore other families (Cu-based with Zn/Cd Ge). Used 16/20 budget.

## [hypothesis] iteration 2 — 2026-10-11 00:31 UTC

Iter 2: Mixed Cu/Ag-on-kesterite with Cd/Zn/Mg and Ge/Sn in Se/S/Te. Cu raises VBM (lowers gap) vs Ag, so Cu-substituted Mg/Zn Ge/Sn selenides should move wide-gap Mg-Ag-Ge-Se (1.86) toward 1.4; also Zn/Cd-Cu sulfide-selenides. Also try Ag2ZnGeSe4/Ag2ZnSnSe4 (Zn between Cd and Mg gap). Calibrate with no known compounds; use novelty filter.

## [observation] iteration 2 — 2026-10-11 00:39 UTC

20 evaluated, all novel. In-window and near-stable: ZnAg2GeSe4 (1.12, ehull 0.0), ZnAg2GeTe4 (1.17, 0.028), MgAg2SnTe4 (1.17, 0.038). Near misses: SrCu2SnSe4 (1.11, 0.050 borderline), MgCu2SnSe4 (1.38 gap, ehull 0.071 - ideal gap but unstable). MgCu2SnS4 stable (0.02) but gap 2.17. Ca/Cu Ge/Sn selenides unstable (0.1+). Zr-Cu-selenides stable (0.0) but gap ~0.1-0.2 (metallic-like, Zr4+ d states); Ti analogues very unstable (0.4+). Surrogate top picks (CaCu2GeSe4) were unstable - gap-driven EI ignored hull.

## [reflection] iteration 2 — 2026-10-11 00:39 UTC

Ag-kesterite family confirmed: Zn/Cd/Mg Ag2 Ge/Sn Se/Te gives gaps 1.1-1.6 with ehull<0.04. Best portfolio so far: CdAg2GeSe4 (1.28, 0.0), ZnAg2GeSe4 (1.12, 0.0), MgAg2SnSe4 (1.59, 0.016), MgAg2GeTe4 (1.49), ZnAg2GeTe4 (1.17). Cu versions give right gaps for Mg/Sn Se but ehull too high; Zr/Ti dead ends. Next: alloy-like compositions (Zn/Cd or Se/Te mixes, e.g. S-Se mixed Ag2 with Zn/Cd Sn) to hit ~1.4 with ehull<0.02; mixed Cu/Ag; try other prototypes (chalcopyrite AgInSe2/AgGaTe2 analogues, zincblende-derived I-III-VI2 with Ag, Sb/Bi pnictides). Avoid Ti, Zr, Ca-Cu.

## [hypothesis] iteration 3 — 2026-10-11 00:39 UTC

Iter 3: Move to chalcopyrite prototype: I-III-VI2 with Ag/Cu/Na, Al/Ga/In/Sb/Bi, S/Se/Te. AgInSe2 (~1.2) AgGaSe2 (1.8) known; expect novel members via mixed-cation (e.g. Ag-Sb/Bi, Cu-Bi, Ag-Al-Te, Na-In) and I-V-VI2 (AgSbSe2, AgBiS2-like, CuSbSe2 ~1.1-1.4 ). Also Ga-Al-Te ordering. Use novelty filter; also try mixed-anion Se/S.

## [observation] iteration 3 — 2026-10-11 00:47 UTC

Iter 3: 16 evaluated. Chalcopyrite alkali I-III-S2 proposals mostly known; novel NaGaS2 (3.83) and NaAlS2 (4.65) stable but far too wide. K-Sb/Bi/As/Al variants critic-vetoed (size mismatch). Kesterite extension: SrAg2GeSe4 (gap 1.69, hull 0.003) in window edge; SrAg2SnSe4 (1.70, hull 0.0) borderline just out; NiAg2GeSe4 (1.65, 0.0) and NiAg2SnSe4 (1.68, 0.0) in window & stable (Ni2+ gap from CHGNet/ML likely unreliable - d8 usually tetrahedral-unfavourable). Sr/Ba tellurides gap 0.1-0.7 (too low, odd drop vs Mg/Zn Te 1.2-1.5, probably structure distortion). Fe/Co analogues unstable/metallic.

## [reflection] iteration 3 — 2026-10-11 00:47 UTC

Large A2+ (Sr) raise gap to ~1.7 for selenides (stable, hull~0), consistent with Cd 1.28 < Zn? < Sr 1.7 < Mg 1.86 trend not monotone; Cd/Zn (1.1-1.3) + Sr/Mg (1.6-1.9) suggests quaternary alloy e.g. (Cd,Sr) or Cd-Zn-Ge-Se ... targets ~1.4. Chalcopyrite alkali route is a dead end (wide gaps, known). Next iteration: mixed-anion Se/S or Se/Te Ag kesterites, and cation-mixed ordering if prototype allows; avoid Fe/Co, K-based. Portfolio so far best: CdAg2GeSe4 (1.28), ZnAg2GeSe4(1.12), MgAg2SnSe4 (1.59), SrAg2GeSe4(1.69), MgAg2GeTe4 (1.49). 4 budget left unspent (only 2 novel candidates remained non-vetoed).

## [hypothesis] iteration 4 — 2026-10-11 00:47 UTC

Iter 4: Ag2-(Zn,Cd,Mg,Sr)-(Ge,Sn)-(S,Se) kesterites: sulfides should widen gap vs selenides (Ag2ZnSnSe4 ~1.2?, Ag2CdGeS4 ~1.8?). Aim for ~1.4 with Ag2ZnSnSe4, Ag2CdSnS4, Ag2ZnSnS4, Ag2ZnGeS4, Ag2CdGeS4, and mixed Cu/Ag-Zn/Cd. Also Ba and Sn/Ge Se, Te mixes. Use novelty filter and critic.

## [observation] iteration 4 — 2026-10-11 00:56 UTC

Iter 4: 20 evaluated, all novel. No new hits in both windows. Sr Ag sulfides stable but gap too wide-ish: SrAg2SnS4 (1.72, hull 0.0 - just out), SrAg2GeS4 (1.87, 0.013). Na2Zr(Zn/Cd/Mg)(Se/Te)4 very unstable (0.45-0.54). Zr-Zn-Ag chalcogenides stable but gap 0.07-0.65. Sr/Ba Cu Sn/Ge tellurides stable-ish (hull 0-0.034) but gaps 0.2-0.9. Si analogues unstable (0.06-0.18). MnCu2GeSe4 unstable. BaSi(AgTe2)2 gap 1.27 but hull 0.056 (just over). Mixing/known candidates mostly exhausted by novelty filter in kesterite prototype (most of space 'already considered').

## [reflection] iteration 4 — 2026-10-11 00:56 UTC

Iter 4 hypothesis (S/Se Ag kesterites with Sr/Ba) partially confirmed: sulfides widen gap as expected (SrAg2SnS4 1.72 borderline), but nothing new inside window. Na/Zr dead end. Tellurides with large A2+ have too small gaps. Remaining ideas for iter 5: the best portfolio remains CdAg2GeSe4, ZnAg2GeSe4, MgAg2SnSe4, MgAg2GeTe4, ZnAg2GeTe4, SrAg2GeSe4 (1.69), SrAg2SnS4 (1.72, borderline). Kesterite prototype novelty space nearly exhausted; try different prototypes/anions unavailable (zincblende binaries all known/rejected). Consider hunting for mixed-anion compositions not covered by the generator via sulfide-selenide mixes, or finalizing.

## [hypothesis] iteration 5 — 2026-10-11 00:57 UTC

Iter 5: Switch to zincblende-derived II-IV-V2 pnictides (ZnSnP2, CdSnAs2, ZnGeAs2 style, ~1.1-1.7 eV) and Cu/Ag-I-III-V mixes; plus remaining kesterite Ag selenides with Zn/Cd/Mg mixes (Ag2 Ge/Sn Se). Reasoning: isoelectronic cation ordering in zincblende; pnictide gaps tunable by anion P/As/Sb and cation Zn/Cd/Mg. Use novelty filter, GP/critic advice.

## [observation] iteration 5 — 2026-10-11 01:08 UTC

Iter 5: zincblende proposals were only binaries, all known/already considered. Kesterite space with Ag/Na/Cl/I all rejected as already considered or SMACT-failing. Chalcopyrite II-IV-VI2/V2: 5 evaluated: ZnSnTe2 (gap 0.98, hull 0.084), ZnSnS2 (2.53, 0.122), CdSnS2 (2.42, 0.041 near-stable but too wide), ZnSnAs2 calibration known (0.37, hull 0.23 - CHGNet poor for this), ZrZnAs2 critic-vetoed. Mn(IV) Ag-kesterites (8) all critic-vetoed as chemically implausible. No new hits; 15+ budget unspent because novelty filter exhausted the space accessible by the three prototypes.

## [reflection] iteration 5 — 2026-10-11 01:08 UTC

Campaign final: Hypothesis of this iteration (II-IV-V2 pnictide/chalcogenide chalcopyrites) falsified in this evaluator (unstable or wrong gap; charge-imbalanced Sn(II) chalcogenides). Best portfolio from earlier iterations stands: CdAg2GeSe4 (1.28 eV, hull 0.0), ZnAg2GeSe4 (1.12, 0.0), MgAg2SnSe4 (1.59, 0.016), MgAg2GeTe4 (1.49, 0.025), ZnAg2GeTe4 (1.17, 0.028), SrAg2GeSe4 (1.69, 0.003), NiAg2GeSe4 (1.65, 0.0; gap suspect). Lesson: the Ag-II-IV-Se4 kesterite-type family is the productive one; follow-up would be DFT-level checks of the true ground-state polymorph (Ag2CdGeSe4 may prefer wurtzite-stannite/ Ag-based other structure) and alloying Zn/Cd to hit 1.4 exactly.
