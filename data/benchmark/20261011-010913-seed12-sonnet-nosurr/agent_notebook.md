# Lab Notebook

## [hypothesis] iteration 1 — 2026-10-11 01:09 UTC

Kesterite CZTS (gap ~1.5 eV) family: substitute Cu->Ag, Zn->Cd/Mg, Sn->Ge/Si, S->Se to tune gap near 1.4. Se lowers gap, Ag raises it, Cd lowers. Expect Cu2CdSnS4, Cu2ZnSnSe4 etc. mostly known; Ag/Cd/Ge/Se mixes may be novel. Test whole family, evaluate novel members.

## [observation] iteration 1 — 2026-10-11 01:20 UTC

Evaluated 24 novel kesterite variants (18 passing converged). Hits (gap 1.1-1.7, hull<=0.05): CdAg2GeSe4 (1.28, 0.000), ZnAg2GeSe4 (1.12, 0.000), MgAg2SnSe4 (1.59, 0.016), MgAg2GeTe4 (1.49, 0.025), ZnAg2GeTe4 (1.17, 0.028), MgAg2SnTe4 (1.17, 0.038). Near-misses: MgAg2GeSe4 1.86, MgAg2SnS4 1.87, MgAg2GeS4 1.89 (too wide); CdAg2GeTe4 0.48, ZrCd(AgSe2)2 0.30 (too narrow; hull 0). Cu-Mg variants unstable (hull 0.07-0.14), though MgCu2SnSe4 gap 1.38. Critic vetoed Si (too small) and Ca (too large) substitutions. Trend: Ag-Ge/Sn-Se with Zn/Cd/Mg is stable; gap S>Se>Te, Mg>Zn>Cd.

## [reflection] iteration 1 — 2026-10-11 01:20 UTC

Hypothesis held for Ag-based selenide/telluride kesterites. Next: explore mixed-anion (S/Se, Se/Te) and mixed-cation (Zn/Mg, Cd/Mg) alloys to tune gap toward 1.4 (e.g., Ag2Zn0.5Mg0.5GeSe4, Ag2MgSn(S,Se)4), plus other families (wurtzite-derived, Ag-based chalcopyrites like AgInSe2 analogs, AgGaTe2). Note gap is DFT-ML fidelity; confirm stability vs competing phases. Avoid Si and Ca in kesterite sites.

## [hypothesis] iteration 2 — 2026-10-11 01:20 UTC

Iter 2: Chalcopyrite sweep (Ag/Na, Al/Ga/Sb/Bi, S/Te) mostly known in MP -> skipped. Instead extend iteration-1 winning Ag2-M-(Ge/Sn)-(Se/Te)4 family to new divalent M = Sr, Ba, Co, Fe. Larger Sr/Ba may destabilize kesterite (hull) but lower gap relative to Mg; Co/Fe (d-metals) may give gap ~1.4 but DFT gaps on magnetic ions less reliable. Evaluate ~12 novel.

## [observation] iteration 2 — 2026-10-11 01:31 UTC

Iter 2 results (19 evaluated). Hits: SrAg2GeSe4 (gap 1.687, hull 0.003; edge of window), SrCu2SnSe4 (1.109, hull 0.050; borderline both). Near: SrAg2SnSe4 gap 1.701 hull 0.000 (just over). Sr/Ba Ag tellurides stable but gaps 0.1-0.7 (too narrow). Co/Fe Ag2-M-X-Se4: hull 0.056-0.11, gaps <0.8 (rejected). Zr/Ti-based Ag2 variants: ZrZn(AgSe2)2 stable but gap 0.65; Ti and Sr-Zr/Ti variants hull 0.35-0.44 (unstable, gap>2.2). Chalcopyrite sweep mostly known in MP (only NaGaS2, NaAlS2 novel, not evaluated).

## [reflection] iteration 2 — 2026-10-11 01:31 UTC

Sr extension partially succeeded: gap pushed to ~1.7 for Ag-Se (Sr wider than Zn/Cd, near Mg). Zr/Ti/Co/Fe sites falsified (unstable or metallic-narrow). Next: mixed-cation alloys not accessible through the tool directly; try Sr/Ba Ag-Se with Ge/Sn and mix of Se/Te anion (not available as single substitution list but can probe via Sr/Ba-Ag-Ge-S? likely too wide). Better: Cd/Zn/Mg Ag2 Sn Se4 combos with gap ~1.4 are in the 1.1-1.6 range already; try non-kesterite families (zincblende-derived I-II-V, e.g. Ag/Cu-Zn-Sb/P/As, ternary nitrides/phosphides like ZnSnP2, Zn-Sn-As, CdSnP2 analogs) for iteration 3. Avoid Co/Fe/Ti.

## [hypothesis] iteration 3 — 2026-10-11 01:32 UTC

Iter 3: II-IV-V2 chalcopyrites (ZnSnAs2, CdGeAs2, MgSiN2 etc.) all known in MP -> skipped. Pivot to alkali (Na/K) replacing Cu/Ag in kesterite-type A2-M-(Sn/Ge)-(Se/Te)4. Hypothesis: Na+ is isovalent with Cu+/Ag+ but without d-band repulsion at VBM, so gaps widen vs Ag analogs (Ag-Cd-Ge-Se 1.28, Ag-Zn-Ge-Se 1.12); Te variants should land ~1.2-1.7. Risk: hull (Na tetrahedral coordination unfavored, likely competing phases such as Na2SnSe3 etc.). All novel in MP, evaluate ~16 mix of Se/Te.

## [observation] iteration 3 — 2026-10-11 01:40 UTC

Iter 3: evaluated 20 novel alkali kesterite-type (all converged). Hits (gap 1.1-1.7, hull<=0.05): K2MgSnTe4 (1.329, hull 0.000), Na2CdSnTe4 (1.367, 0.032), K2ZnSnTe4 (1.573, 0.000), Na2MgGeTe4 (1.136, 0.047). Near: Na2CdGeTe4 1.739/0.021. Selenides all too wide (1.96-2.54), though many stable (K2ZnSnSe4, K2ZnGeSe4, K2CdGeSe4 hull 0). K2CdSnTe4 and K2CdGeTe4 gap 0.86-0.88 (too narrow, hull 0). II-IV-V2 chalcopyrites all known in MP (nothing novel). Caveat: K/Na-kesterite is a prototype-imposed structure; real ground states likely different (hull 0.0 vs MP suggests competing phases are only those in MP; K2 M Sn Te4 may adopt other structure types).

## [reflection] iteration 3 — 2026-10-11 01:40 UTC

Hypothesis partly held: alkali replacement widens gaps; Se too wide, Te lands in window. Best new leads: K2MgSnTe4 (1.33 eV, hull 0), K2ZnSnTe4, Na2CdSnTe4. Trend for Te: Cd<Mg<Zn gap for Sn; Ge widens. Next iteration: mix Se/Te anion or explore K/Na with Ag/Cu alloys (half-alkali), Rb-like not in palette; try Ba/Sr-based A-M-Sn-Te or K2-Cd/Zn-Sn-(S/Se) not needed. Also consider Ba2/Sr2-based ZnSnSe-type or Na2-Ca... and check literature for K2MgSnTe4-like compounds (e.g. K2Zn Sn Te4 known as different structure types) to assess real-structure stability.

## [hypothesis] iteration 4 — 2026-10-11 01:40 UTC

Iter 4: Complete the alkali-telluride kesterite-type grid (Na/K x Zn/Cd/Mg/Sr/Ba/Ca x Sn/Ge x Te) for members not yet evaluated, esp. Na2ZnSnTe4, Na2MgSnTe4, K2MgGeTe4, K2ZnGeTe4, Sr/Ba variants. Larger divalent cations (Sr) widen/shift gap similar to Mg in Ag series; Cd narrows. Expect several with gap 1.2-1.7 and hull<=0.05. Literature search found no prior reports for these quaternaries (no relevant hits) so they're plausibly novel.

## [observation] iteration 4 — 2026-10-11 01:52 UTC

Iter 4: evaluated 19 novel alkali-telluride kesterite-type (all converged). Hits (gap 1.1-1.7, hull<=0.05): K2CaGeTe4 (1.421, 0.019 - best, near-ideal), K2BaGeTe4 (1.566, 0.000), K2BaSiTe4 (1.642, 0.000), K2MgSiTe4 (1.692, 0.005, edge), K2SrSnTe4 (1.199, 0.012), K2SrGeTe4 (1.216, 0.013), K2CaSnTe4 (1.118, 0.033). Near: Na2CaGeTe4 1.73/0.000; Na2MnGeTe4 1.09/0.043. Rejected: Na-Sr/Ba (hull 0.06-0.12), Na2CaSnTe4 hull 0.17, K2Ca/SrSiTe4 hull ~0.10, Mn variants gap too narrow (0.65-1.1). Trend: K stabilises large divalent (Ca, Sr, Ba) sites better than Na; Ge/Si widen gap vs Sn; gap Ca<Sr/Ba pattern non-monotonic. Caveat: prototype-imposed structure; real ground states for K2AE-TetTe4 likely differ (e.g. different coordination for large Ca/Sr/Ba), and gaps are ML-fidelity.

## [reflection] iteration 4 — 2026-10-11 01:52 UTC

Hypothesis held: K2-AE-(Ge/Sn/Si)-Te4 yields multiple stable, in-window novel candidates; K2CaGeTe4 is the best lead (1.42 eV, hull 0.019). Na analogs with large AE unstable. Next (iter 5): validate by probing competing-structure risk (can't directly), try K/Ca-Ge with Se/Te mixing is unavailable; could explore Ag/K combos or Ca-Ge-Te related, and rank final leads: K2CaGeTe4, K2BaGeTe4, K2SrGeTe4, K2MgSnTe4, Na2CdSnTe4, CdAg2GeSe4.

## [observation] iteration 5 — 2026-10-11 01:58 UTC

Iter 5: hypothesis was to fill the gaps in the K2-AE-IV-Te4 grid (Si with Zn/Cd) and test Ca/Ba/Si Ag analogs. Evaluated 14 novel candidates, all converged. One new hit: K2CdSiTe4 (gap 1.235, hull 0.000). K2ZnSiTe4 is stable but too wide (2.07). Ag-Si and Ag-Ca tellurides: BaSi(AgTe2)2 1.27/hull 0.056, CaSi(AgTe2)2 1.25/hull 0.122 (gap in window, hull too high). CaAg2Ge/SnTe4 are narrow (0.06-0.24) and unstable. All K2-AE-IV-Se4 are too wide (2.5-2.7 eV), though K2BaSnSe4, K2BaGeSe4 and K2CdSiSe4 are stable. ZnSi(Ag)2 variants have hull 0.095-0.17. I left 6 relaxations unspent because the remaining candidates (K2 Ca/Ba/Zn Si/Ge Se4) were predicted to be wide-gap Se compounds.

## [reflection] iteration 5 — 2026-10-11 01:58 UTC

Campaign-end summary. Best novel leads, ranked by gap proximity to 1.4 eV and hull: K2CaGeTe4 (1.42, 0.019); K2MgSnTe4 (1.33, 0.000); CdAg2GeSe4 (1.28, 0.000); K2CdSiTe4 (1.235, 0.000); K2BaGeTe4 (1.57, 0.000); K2SrGeTe4 and K2SrSnTe4 (~1.2, ~0.012); K2ZnSnTe4 (1.57, 0.000); Na2CdSnTe4 (1.37, 0.032); ZnAg2GeSe4 (1.12, 0.000). Trends: Te gives gaps in the window for alkali kesterite-types and Se gives gaps that are too wide; Ag-Se works for Zn/Cd/Mg/Sr. Caveats: the kesterite prototype is imposed, so real ground-state structures of the K2-AE-IV-Te4 compounds probably differ (hull is measured only against phases in MP). Gaps are ML-fidelity. Next steps would be to check competing polymorphs (e.g. the K2 M Sn Te4 structure types) and run DFT-level gap checks on the top 3.
