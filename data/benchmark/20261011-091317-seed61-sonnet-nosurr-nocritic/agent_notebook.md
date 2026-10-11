# Lab Notebook

## [hypothesis] iteration 1 — 2026-10-11 09:13 UTC

Kesterite family I2-II-IV-VI4 with isoelectronic substitutions (Cu->Ag, Zn->Cd/Mg, Sn->Ge/Si, S->Se/Te). CZTS gap ~1.5, CZTSe ~1.0; mixed S/Se or Ag/Cd variants should tune gap into 1.1-1.7. Aim for less-studied ones (Ag2ZnSnS4, Cu2CdGeS4, Cu2MgSnS4, Ag2CdSnS4, Cu2ZnGeSe4 etc.) likely novel in MP.

## [observation] iteration 1 — 2026-10-11 09:14 UTC

14 novel kesterite variants evaluated. HITS (gap 1.1-1.7, ehull<=0.05): CdAg2GeSe4 (1.28 eV, ehull 0.0), ZnAg2GeSe4 (1.12, 0.0), ZnAg2GeTe4 (1.17, 0.028). Near misses: MgCu2SnSe4 (1.38 but ehull 0.071), MgCu2GeSe4 (1.10, ehull 0.136). Mg-Ag-sulfides/Ge-Se stable but gap 1.86-1.89 (too wide). Si variants unstable (ehull 0.13-0.15). Ag-tellurides gaps mostly too low (0.4-0.6) except Zn-Ge. Many Cu/S known in MP (non-novel, skipped).

## [reflection] iteration 1 — 2026-10-11 09:14 UTC

Hypothesis held for Ag-Ge-Se kesterites (Zn, Cd). Ge better than Si for stability; Mg widens gap. Next: alloys/mixed anion (S/Se) of Ag2(Zn,Cd)GeSe4 to push gap toward 1.4, Ag-Sn-Se Cd/Zn variants, and different prototypes (chalcopyrite Ag-based, e.g. AgInTe2/ AgGaTe2 variants). Propose_candidates seems to only handle one substitution per element per site; use multiple calls.

## [hypothesis] iteration 2 — 2026-10-11 09:14 UTC

Iteration 2: Extend the Ag-Ge-Se kesterite hits by (a) mixed-anion S/Se variants Ag2(Zn,Cd)Ge(S,Se)4 -- S widens gap from 1.1-1.28 toward 1.4; (b) Ag2(Zn,Cd)SnSe4 (Sn lowers gap vs Ge, Cd lowers vs Zn); (c) chalcopyrite Ag-based (AgGaSe2/AgInSe2 are known; try AgGaTe2, AgAlTe2, CuAlTe2, alloys not in MP). Pure S analogues expected gap too wide (~1.8) so focus on Se and Se-rich.

## [observation] iteration 2 — 2026-10-11 09:16 UTC

20 relaxations. NEW HIT: Na2CdSnTe4 (gap 1.367, ehull 0.032, novel) -- best near 1.4 eV. Also CaCu2GeSe4 gap 1.20 but ehull 0.121 (not stable). Zr-based Cu2(II)Zr Se4 (II=Cd,Mg,Ca,Sr,Ba) all ehull 0 but gaps 0.04-0.19 (suspicious: Zr4+ d0 selenides should have wider gaps; likely model artefact/ different structure; not credible). Ti analogues unstable (ehull 0.36-0.49). MnCu2GeSe4 ehull 0.10. Alkali kesterites: Na2CdSnSe4 1.96/0.019, Na2ZnSnSe4 2.29/0.007, Na2ZnSnTe4 2.05/0.023, K2CdGeSe4 2.41/0.0, K2CdSnTe4 0.86/0.0 -- stable but gaps outside window except Na2CdSnTe4. Wasted one relaxation on CdAg2SnSe4 (flagged known by MP; gap 1.26, ehull 0) -- not a discovery. Chalcopyrite I-III-VI2 and II-IV-As2 all known in MP; zincblende prototype yields nothing useful (SMACT rejects P/As binaries).

## [reflection] iteration 2 — 2026-10-11 09:16 UTC

Alkali-substituted kesterites are stable (Na/K stabilise via ionic bonding) and gap tunes with chalcogen: Te lowers gap, Cd lower than Zn, Sn lower than Ge. Gaps sit around Na2CdSnTe4 = 1.37. Next iteration: explore K/Na mixed or Na2CdSnTe4 neighbours: K2CdSnTe4 is 0.86, Na2CdSnTe4 1.37 -> try Na/K ordered, Na2CdGeTe4, Na2ZnGeTe4, K2ZnSnTe4, K2CdGeTe4, Na2CdSnSe/Te variants (untested in this batch), Na2MgSnTe4, Ca/Sr-based. Zr-Cu kesterite gaps are untrustworthy; avoid or verify. Avoid candidates flagged non-novel. Prototypes limited; chalcopyrite/ zincblende families mostly known.

## [hypothesis] iteration 3 — 2026-10-11 09:16 UTC

Iteration 3: Neighbours of Na2CdSnTe4 (1.37 eV, ehull 0.032). Alkali (Na,K) II-IV tellurides/selenides: vary II (Zn,Cd,Mg), IV (Sn,Ge), chalcogen (Te, Se/Te mix) and alkali (Na,K,Ag-Na mixes). Expect Ge raises gap vs Sn, Zn raises vs Cd, K lowers (K2CdSnTe4 0.86). So Na2CdGeTe4, Na2ZnSnTe4(2.05 done), K2ZnSnTe4, K2CdGeTe4, Na2MgSnTe4, plus Cu/Ag-Na mixes. Also Ag2 and Cu2 with Ca/Sr/Ba Sn/Ge Te variants.

## [observation] iteration 3 — 2026-10-11 09:17 UTC

Iter 3, 20 relaxations, all novel. HITS: K2MgSnTe4 (1.33 eV, ehull 0.0), K2MgGeTe4 (1.50, 0.0), Na2MgGeTe4 (1.14, 0.047), SrAg2GeSe4 (1.69, 0.003; edge of window), SrCu2SnSe4 (1.11, ehull 0.050 borderline). Near: SrAg2SnSe4 gap 1.70 ehull 0 (just outside). Mg-alkali selenides gap 2.2-2.5 too wide; Na2MgSnTe4 1.93. Ca-based Ag/Cu unstable (0.05-0.11). Sr/Ba Ag tellurides stable but gaps 0.1-0.7 (too small). Ba-Cu-Sn-Te 0.4.

## [reflection] iteration 3 — 2026-10-11 09:17 UTC

Hypothesis held: alkali-Mg tellurides fill the window, K stabilizes (hull 0) and Mg gives 1.3-1.5 eV. Trend: Te lowers gap ~1 eV vs Se; Sr/Ba Ag-Se near 1.7 edge. Next: K/Rb-like with Mg/Zn/Cd mixed-cation alloys (K2Mg1-xCdxSnTe4), K2ZnSnTe4 etc were already tested; try Se/Te mixed anions of K2MgSnSe4 (2.5) and Te (1.33) to tune ~1.4-1.9 -> but already in window with Te. Sr/Ba Ag2 Sn/Ge S/Se/Te mixes (SrAg2Sn(Se,Te)4) to bring 1.70 to ~1.4. Caveat: CHGNet/ML gaps are rough; verify by DFT. Ca-based unstable; avoid.

## [observation] iteration 4 — 2026-10-11 09:18 UTC

Iter 4: 20 relaxations, all novel (K/Na-II-IV-Te4 kesterite-type, II = Mg,Zn,Cd,Ca,Sr,Ba; IV = Si,Ge,Sn). HITS (gap 1.1-1.7, ehull<=0.05): K2CaGeTe4 (1.42, 0.019 -- best, nearly ideal), K2CdSiTe4 (1.235, 0.0), K2BaGeTe4 (1.57, 0.0), K2SrSnTe4 (1.20, 0.012), K2SrGeTe4 (1.22, 0.013), K2CaSnTe4 (1.12, 0.033), K2MgSiTe4 (1.69, 0.005; edge). Stable but gap out: K2ZnSiTe4 2.07/0.0, Na2CaGeTe4 1.73/0.0, Na2CaSiTe4 2.05/0.0. Unstable: all Na-Si-Mg/Zn/Cd (0.09-0.13), Na2CaSnTe4 0.17, Na2Sr*, BaNa2*, K2CaSiTe4, K2SrSiTe4 (~0.1). Trends: K stabilizes large II cations (Ca/Sr/Ba) while Na prefers smaller ones; Si surprisingly OK with K+Cd/Mg/Zn.

## [reflection] iteration 4 — 2026-10-11 09:18 UTC

Hypothesis held strongly: K-based Te kesterite-type family yields 7 new window hits, K2CaGeTe4 (1.42 eV, 0.019) closest to ideal. Caveats: CHGNet/ML gaps rough; the large-II (Ca/Sr/Ba) members are probably not true kesterite ground states (likely other structure types e.g. K2BaSnTe4-like, which is why K2BaSnTe4 is in MP) so hull is relative to the competing phases; verify with DFT. Next (final iteration): fill gaps with Se/Te or S/Te analogues of K2(Ca,Sr)Ge, maybe Rb-free; Ag/Cu with K? or K2CdGeTe4-type neighbours already done. Consider consolidating best candidates: K2CaGeTe4, K2MgSnTe4, K2MgGeTe4, Na2CdSnTe4, CdAg2GeSe4.

## [hypothesis] iteration 5 — 2026-10-11 09:18 UTC

Iteration 5: Complete the K-II-IV-chalcogenide family with Ag-for-K / Se-for-Te variations. (a) K2(Mg,Zn,Cd,Ca,Sr)(Ge,Sn)Se4 gaps likely too wide (~2.4) so skip mostly; (b) Ag-containing mixes: AgK(II)IVTe4 not available as single substitution, so use Cu->K on Cu2ZnGeTe4-like (Zn/Cd/Mg + Si/Ge/Sn + Te/Se). Focus on Te kesterite-types with K not yet tested: K2ZnGeTe4, K2ZnSnTe4, K2CdGeTe4, K2MnGeTe4? Prior notes say Zn/Cd tested partly; check novelty via propose_candidates. Also S-containing K-Ca-Sn etc, and Ba/Sr with Si/Sn on Na. Use as many novel ones as possible.

## [observation] iteration 5 — 2026-10-11 09:19 UTC

Iter 5: 20 relaxations, all novel. Mn-based alkali chalcogenides are the new hits (Mn2+ lowers gap vs Mg/Zn): K2MnGeSe4 1.44 eV/ehull 0.0 (best, ~ideal), Na2MnGeSe4 1.65/0.008, Na2MnSnSe4 1.115/0.0, K2MnSiSe4 1.675/0.04, K2MnSiTe4 1.455/0.045. Borderline outside: K2MnGeTe4 gap 1.10/0.002 (1.100 not >1.1 strictly flagged out), Na2MnGeTe4 1.09/0.043, K2MnSnTe4 0.65, Na2MnSnTe4 0.95. Wide gaps (2.6-2.95): K2(Zn,Cd,Mg)SiSe4, Na2(Ca)(Sn,Ge)Se4. Unstable: Na2MnSi*, Na2SrSnSe4, Ag-Ca/Sr-Si chalcogenides (0.08-0.13). Caveat: Mn compounds are magnetic; nonmagnetic ML gap unreliable (Mn d-d / AFM state).

## [reflection] iteration 5 — 2026-10-11 09:19 UTC

Final iteration: Mn on II site gives selenides in the window with hull ~0 (K2MnGeSe4 best). Campaign overall: ~25 novel window hits across Ag-Ge-Se kesterites, alkali-Mg/Ca/Sr/Ba/Cd tellurides, and alkali-Mn selenides. Top picks to carry forward: K2MnGeSe4, K2CaGeTe4, K2MgSnTe4, Na2CdSnTe4, CdAg2GeSe4, K2MgGeTe4. Caveats: CHGNet ehull vs only known competing phases, ML band gaps rough, large-II compounds possibly not in kesterite ground-state structure, Mn magnetism not treated. Next step beyond this campaign: DFT/HSE verification with spin polarization, phonon and competing-phase checks (e.g. K2MnGeSe4 vs. known K-Ge-Se phases).
