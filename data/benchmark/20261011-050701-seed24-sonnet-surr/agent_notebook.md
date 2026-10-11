# Lab Notebook

## [hypothesis] iteration 1 — 2026-10-11 05:07 UTC

Kesterite family: substitute Cu->Ag, Zn->Cd/Mg/Ca?, Sn->Ge/Si, S->Se/Te. Cd/Ag/Ge/Se variants (Ag2ZnSnSe4, Cu2CdGeSe4, Ag2CdSnS4 etc.) should give gaps near 1.1-1.7 eV by Se/S mixing and be near hull due to isoelectronic substitution. Aim at less-explored members.

## [observation] iteration 1 — 2026-10-11 05:14 UTC

20 novel kesterite-type evaluated. Hits (gap 1.1-1.7, ehull<=0.05): CdAg2GeSe4 (1.28 eV, hull 0.0) best; ZnAg2GeSe4 (1.12, 0.0); MgAg2SnSe4 (1.59, 0.016); ZnAg2GeTe4 (1.17, 0.028); MgAg2SnTe4 (1.17, 0.038). Near-stable but gap too big: Mg-Ag-S/Ge-Se (1.86-1.89), MgCu2SnS4 (2.17). Si variants unstable (hull 0.13-0.17). Cu-Mg selenides unstable. Ag consistently stabilizes; gap order S>Se>Te; Mg raises gap vs Zn/Cd.

## [reflection] iteration 1 — 2026-10-11 05:14 UTC

Hypothesis supported: Ag-based Ge/Sn selenides/tellurides in kesterite-type are stable with suitable gaps. Next: explore Ag2-(Zn,Cd,Mg)-(Ge,Sn)-(S,Se) mixed anion, and Ca/Sr/Ba or other prototypes (chalcopyrite AgInSe2-like, Cu-Ag mixing, Cd-Zn mixing) to tune gaps; avoid Si. Caveat: gaps are CHGNet/ML estimates; ZnAg2GeSe4 at 1.12 is near the lower edge.

## [hypothesis] iteration 2 — 2026-10-11 05:14 UTC

Iteration 2: Extend to kesterite-type mixed-anion/mixed-cation Ag compounds (Ag2-Zn/Cd-Ge/Sn-(S,Se) with mixed Se/Te), plus chalcopyrite-type Ag/Cu-(Ga,In,Al)-(S,Se,Te) with unexplored combos (e.g. AgAlTe2, AgGaTe2 variants) and Sn/Ge-based. Reasoning: Ag stabilised hull in iter 1; gap order S>Se>Te; Cd/Zn lower gap than Mg. Aim at 1.2-1.5 eV by Se/Te mixing, and Cd/Zn Sn/Ge S selenides.

## [observation] iteration 2 — 2026-10-11 05:22 UTC

Iter 2: 20 novel evaluated. Chalcopyrite Ag-Al/Ga proposals were all known (skipped). Kesterite-type with Ca/Sr/Ba/Ti/Zr: Ti/Zr (4+) variants unstable (hull 0.29-0.49) except ZrCd(AgSe2)2 (hull 0.0 but gap 0.30). Sr-Ag2-Ge/Sn-Se are stable: SrAg2GeSe4 gap 1.687 hull 0.003 (hit, at upper edge); SrAg2SnSe4 gap 1.701 hull 0.0 (just outside window); SrAg2GeS4 1.87/0.013. Ca variants worse hull (CaAg2GeSe4 0.062, gap 1.68). SrAg2SnTe4 gap 0.1 (hull 0.029). Ba-Ti/Zr unstable.

## [reflection] iteration 2 — 2026-10-11 05:22 UTC

Sr (large A2+) stabilises Ag2-A-Ge/Sn-Se4; gaps ~1.7 are at the upper edge. Next: tune down by alloying — Sr/Cd or Sr/Zn mixed, Se/Te mixed anions (e.g. SrAg2SnSe2Te2, Se3Te), or Cu partial substitution; Ba-Ag2-Ge/Sn-Se (BaAg2SnSe4 known, BaAg2GeSe4 known). Avoid Ti/Zr 4+ and Ca. Chalcopyrite prototype yields only known compounds; try ternary/quaternary outside these prototypes (e.g. zincblende-derived II-IV-V2 with Sn/Ge pnictides, Cu-Sb-Se).

## [hypothesis] iteration 3 — 2026-10-11 05:22 UTC

Iter 3: (a) Tune Sr/Ba-Ag2-(Ge,Sn)-Se4 gaps down via mixed Se/Te anions and Sr->Ba (larger A, lower gap). (b) II-IV-V2 pnictide chalcopyrites from zincblende/GaAs prototype (ZnSnP2, ZnSnAs2, CdGeAs2, CdSiP2 style; ZnSnP2 gap ~1.2-1.7 lit.) - try less common combos (Mg-Sn-P/As, Cd-Sn-P, Zn-Ge-As, Zn-Sn-Sb). Many known; evaluate only novel ones.

## [observation] iteration 3 — 2026-10-11 05:25 UTC

Iter 3 first batch: SrAg2GeTe4 gap 0.155 hull 0.016; BaAg2GeTe4 gap 0.705 hull 0.0 -> tellurides too narrow; Te route ruled out for Sr/Ba. Critic vetoed 9 non-kesterite candidates (Sb chalcopyrites II-IV-Sb2, K/Na-Ga/Sb/Bi chalcogenides) because my notebook hypothesis was multi-part and mismatched; zincblende prototype only yields binaries (useless). Mixed-anion not supported by propose tool (single-element substitution lists per site). Lesson: state one focused hypothesis per batch.

## [hypothesis] iteration 3 — 2026-10-11 05:25 UTC

Focused hypothesis: Cu-based Sr/Ba kesterite-type chalcogenides A-Cu2-(Ge,Sn)-(S,Se)4 (A = Sr, Ba). Cu d-band raises VBM relative to Ag, lowering the gap ~0.3-0.5 eV from the 1.7 eV Ag-Sr-Se compounds into the 1.1-1.7 window; large A2+ cation stabilised Ag analogues (hull ~0). Also Cd/Zn-Cu analogs with Sr excluded. Test SrCu2GeSe4, SrCu2SnSe4, BaCu2GeSe4, BaCu2SnSe4, S analogues.

## [observation] iteration 3 — 2026-10-11 05:35 UTC

Iter 3 results. SrCu2SnSe4: gap 1.109, hull 0.050 (borderline, marginal). Ag2-M-(Ge,Sn)-(S,Se)4 with 3d M: NiAg2GeSe4 (1.648, hull 0.0) and NiAg2SnSe4 (1.676, hull 0.0) = new hits, upper window edge; NiAg2GeS4 1.744/0.008, NiAg2SnS4 1.897/0.0 too wide. Co: CoAg2GeS4 1.51/0.113 and CoAg2SnS4 1.39/0.092 right gap but unstable; Co selenides gap 0.6-0.8. Fe: gap ~0 and unstable. MnAg2GeS4 gap 2.24 hull 0.079. Cu substitution for Ag in Ni: Cu2NiGeSe4 gap 0.26. Tellurides (Ni, Sr, Ba) gaps <0.7 all -> too narrow. Caveat: tetrahedral Ni2+ in CHGNet/ML gap may be unreliable (Ni d8 normally square planar; spin state); treat as suspect.

## [reflection] iteration 3 — 2026-10-11 05:35 UTC

Gap tuning: Ag->Cu and Se->Te both close gaps too much; S->Se is the useful lever. Best candidates now: CdAg2GeSe4 (1.28, 0), ZnAg2GeSe4 (1.12), MgAg2SnSe4 (1.59), SrAg2GeSe4 (1.69), NiAg2GeSe4 (1.65). Next iterations: non-kesterite families untried (critic requires single focused hypothesis per batch); consider mixing via other prototypes, Cd/Zn-rich Ag selenides with Si-free, or check Co/Ni alloy ideas; the tool cannot do mixed-anion/mixed-cation alloys so single-site substitutions only. Pnictide II-IV-V2 via chalcopyrite prototype got only vetoed/known entries; Sb-based novel ones (ZnGeSb2, CdGeSb2, MgSnSb2, MgGeSb2) remain unevaluated and would need own focused hypothesis.

## [hypothesis] iteration 4 — 2026-10-11 05:35 UTC

Iter 4 focused hypothesis: alkali (Na,K) analogues A2-M-(Sn,Ge)-Se4 of kesterite (charge balanced 2x(+1)+2+4). Closed-shell alkali raises gap vs Cu/Ag; Se and heavier Cd/Sn should bring it to 1.1-1.7. Stability risk: tetrahedral-vs-other coordination (K2 compounds known in other structure types, e.g. K2ZnSnS4-type), so hull may be >0.05. Pnictide II-IV-V2 chalcopyrite batch mostly already considered; only ZnSiSb2/CdSiSb2 novel, skipped. Evaluate Na/K Cd/Zn/Mn Ge/Sn selenides; one of K2CdSnSe4 (known) as calibration not planned.

## [observation] iteration 4 — 2026-10-11 05:38 UTC

Iter 4 alkali kesterite-type (10 novel evaluated): all near-stable (hull 0-0.029). Zn/Cd gaps 1.96-2.49 too wide. Mn versions are hits: K2MnGeSe4 1.443/0.0 (best, ideal), Na2MnGeSe4 1.646/0.008, Na2MnSnSe4 1.115/0.0. Mn2+ d5 gap from ML may be suspect (spin), but trend clear: Mn lowers gap vs Zn. Pnictide II-IV-V2 batch: nearly all previously considered; skipped.

## [reflection] iteration 4 — 2026-10-11 05:41 UTC

Iter 4 batch 2: all stable (hull<=0.046) but no new hits. Mn/Co sulfides 1.85-2.29 too wide; Mn tellurides too narrow (0.65-0.95; K2MnGeTe4 1.100 on boundary, rounds just out). Gap tuning in this family: S>Se>Te with Se sweet spot; Se Mn selenides are the hits (K2MnGeSe4 1.44/0.0 best; Na2MnGeSe4 1.65; Na2MnSnSe4 1.115). Co selenides not tested; Fe/Co K2 selenides and Rb/Cs analogues not available. Next (iter 5): K2/Na2 Co/Fe/Ni Ge/Sn Se4, and K2MnGeSe4 neighbours; caveat Mn d5 gaps unreliable.

## [hypothesis] iteration 5 — 2026-10-11 05:41 UTC

Iter 5 focused hypothesis: alkali (Na,K) kesterite-type A2-M-(Ge,Sn)-Se4 with M = Co, Ni, Fe (3d divalent, tetrahedral) as neighbours of the Mn hits (K2MnGeSe4 1.44). Co2+ lowers gap vs Mn (seen in Ag series) so Co selenides should land ~1.0-1.5 eV; hull expected ~0 given alkali family stability. Literature search found no prior reports (gap in knowledge). Also K/Na Co sulfides as wider-gap controls if budget allows.

## [observation] iteration 5 — 2026-10-11 05:44 UTC

Iter 5: 16 novel evaluated. Hit: Na2NiGeSe4 gap 1.402 (ideal), hull 0.002. Borderline: Na2FeGeSe4 gap 1.325 but hull 0.057 (fails). Co selenides gaps 1.9-2.3 (wider than Mn, hypothesis that Co lowers gap falsified); K2/Na2 Ni Sn Se and K2 Ni Ge Se ~2.0-2.1; Fe selenides 0.4-0.8 (K) too narrow. Ni/Co tellurides 0.08-0.65 too narrow. Ni d8 tetrahedral caveat: ML gap may be unreliable (Ni2+ prefers square planar), so Na2NiGeSe4 is suspect; only one hit at 1.4 isn't a trend (K/Sn analogues are 2.0+).

## [reflection] iteration 5 — 2026-10-11 05:44 UTC

Campaign summary: robust stable hits in kesterite-type Ag selenides (CdAg2GeSe4 1.28/0.0, ZnAg2GeSe4 1.12, MgAg2SnSe4 1.59, SrAg2GeSe4 1.69, NiAg2GeSe4 1.65) and alkali-Mn selenides (K2MnGeSe4 1.44/0.0, Na2MnGeSe4, Na2MnSnSe4), plus Na2NiGeSe4 1.40/0.002. Lever: S->Se->Te for gap, Ag/Cu/alkali and A-site size for hull. Failures: Si, Ti/Zr, Fe, tellurides, Co alkali selenides too wide. Caveats: all gaps are CHGNet/ML estimates; open-shell 3d (Mn, Ni) gaps need DFT+U/HSE verification; CdAg2GeSe4 is the most trustworthy lead. Future: verify with explicit HSE, check competing phases and dynamic stability.
