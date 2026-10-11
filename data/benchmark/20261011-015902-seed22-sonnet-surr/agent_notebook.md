# Lab Notebook

## [hypothesis] iteration 1 — 2026-10-11 01:59 UTC

Kesterite family: substitute Cu->Ag, Zn->Cd/Mg, Sn->Ge/Si, S->Se to tune gap. CZTS ~1.5 eV, CZTSe ~1.0; Ag/Cd analogues and mixed-anion variants (Ag2ZnSnS4, Cu2CdSnS4, Cu2ZnGeS4, Cu2MgSnS4, Ag2CdSnS4...) likely near 1.1-1.7 eV. Many are known (Cu2CdSnS4, Cu2ZnGeS4); target the less explored ones.

## [observation] iteration 1 — 2026-10-11 02:14 UTC

Hits (novel, ehull<=0.05, gap 1.1-1.7): CdAg2GeSe4 (0.0, 1.28 eV - best), ZnAg2GeSe4 (0.0, 1.12), MgAg2SnSe4 (0.016, 1.59), SrAg2GeSe4 (0.003, 1.69). Near-miss: SrAg2SnSe4 (0.0, 1.701). Too wide: Mg/Ag sulfides (~1.9), MgCu2SnS4 (2.17). Unstable: Ca/Mn/Fe/Cu-Mg-Ge-Se (ehull 0.05-0.14). Fe gives zero gap. Critic vetoed 5 malformed Si formulas (charge imbalance). Chalcopyrite Ag swaps all known in MP. Ag selenides with Ge/Sn are the sweet spot; Ag stabilizes vs Cu.

## [reflection] iteration 1 — 2026-10-11 02:14 UTC

Hypothesis largely held: Ag2-M-(Ge,Sn)-Se4 family gives stable, in-window gaps. Next: explore tellurides/mixed S-Se (e.g. Ag2CdGe(S,Se)4, Ag2SrGeS4 for gap tuning), Ba/Sr Te variants, Cd-Sn mixtures, Zn/Cd/Mg Ag Sn Te. Avoid Fe, Ca, Cu-Mg-Ge-Se, Si formulas. Surrogate will be usable now (>6 scored).

## [hypothesis] iteration 2 — 2026-10-11 02:15 UTC

Iter 2: extend Ag2-M-(Ge,Sn)-X4 family: Te and mixed S/Se anions (Se->Te narrows gap, S widens), Ba/Sr/Cd/Zn/Mg with Ge/Sn. Expect Ag2BaSnSe4, Ag2CdSnSe4, Ag2ZnSnSe4 (~1.2-1.5), tellurides likely <1.1 but Mg/Sr/Ba may keep in window. Sulfide Ge with Cd/Zn maybe ~1.7-2. Use kesterite prototype with Ag substitution.

## [observation] iteration 2 — 2026-10-11 02:27 UTC

Iter 2 (18 evaluated of 20; 8 critic vetoes). New hits (novel, ehull<=0.05, gap 1.1-1.7): CdAg2SnSe4 (0.0, 1.262), ZnAg2SnSe4 (0.0, 1.124), MgAg2GeTe4 (0.025, 1.49), ZnAg2GeTe4 (0.028, 1.171), MgAg2SnTe4 (0.038, 1.172). Tellurides: Cd/Sr gaps 0.1-0.5 (too small), Zn/Mg Ge gaps in window. Sulfides Ag-Cd/Zn-Sn/Ge: stable but gap 2.0-2.3 (too wide). Cu-selenides with Zn/Cd (Ge/Sn): ehull 0.06-0.11, gaps 0.3-0.85 — unstable, Ag clearly needed. Critic vetoed Ba (and Sr sulfide) kesterites for size mismatch (Ba/Sr likely prefer other structure types; SrAg2*Se4 results from iter1 may be artifacts of the kesterite relaxation). Zincblende prototype yields only binaries, unhelpful. Note: 'already considered' formulas in propose are not necessarily evaluated; evaluate_candidates still accepted them.

## [reflection] iteration 2 — 2026-10-11 02:27 UTC

Hypothesis held: Ag2-M-(Ge,Sn)-Se4 and Zn/Mg Ag Ge/Sn Te4 give stable in-window gaps. Gap tuning: S ~2.0-2.3, Se ~1.1-1.3 (Zn/Cd), Te ~0.4-1.5. Ideal 1.4 not yet hit by a stable candidate; best ~1.26-1.28 (CdAg2SnSe4, CdAg2GeSe4). Next: need anion mixing (S/Se, Se/Te) to dial 1.4 — prototype tool only does full substitutions, so try Mg/Zn/Cd mixing is not supported; consider Ag/Cu mixing or Mg-Ag-Ge-Se (1.86) vs Zn (1.12) -> alloy suggestion. Also explore other families (chalcopyrite AgGaTe2-type, Ag-Sb/Bi ternaries, Cu-Ba-chalcogenides, halides like Cu-Sb-Cl) and avoid Ba/Sr kesterites, Cu-selenides, Fe/Mn/Ca.

## [hypothesis] iteration 3 — 2026-10-11 02:27 UTC

Iter 3: Ag2-M-(Ge,Sn)-X4 kesterite family is exhausted (all combos already considered). New direction: tetravalent d0 Zr/Ti on the Sn/Ge site (Ag2-M-Zr/Ti-S/Se4), Zr4+ r=0.72 ~ Sn4+; expected gaps 1.2-1.8 for selenides (Zr/Ti d0 CB lowers gap vs Ge/Sn s-CB? uncertain; Ti likely too small/low gap). Also probe novel Na-Ga/Al chalcogenides (NaGaS2, NaGaSe2, NaAlS2) as likely wide-gap controls. Ag preferred over Cu per iter 1-2.

## [observation] iteration 3 — 2026-10-11 02:44 UTC

Iter 3 (20 evaluated). Only hit: Ag2ZnTiS4 [TiZn(AgS2)2] ehull 0.0, gap 1.554 (novel). Zr family: stable (ehull 0) for Zn/Cd/Mg Se and Zn S variants but gaps 0.15-0.65 (too small; Zr d-band CB). Ti-Se / Ti-Cd Ag compounds ehull 0.35 (unstable); but Ti-Cu-S (Zn: gap 2.66; Cd: 2.85) stable and too wide. Na-Ga/Al chalcogenides: NaGaSe2 (0.017, 2.20), NaGaS2 (3.8), NaAlS2 (4.6) - wide gap. Results are internally inconsistent (e.g. ZrCd(AgS2)2 unstable but ZrZn stable, Ti-Se unstable vs Ti-S stable) suggesting CHGNet hull references are patchy; Ag2ZnTiS4 should be treated with caution.

## [reflection] iteration 3 — 2026-10-11 02:44 UTC

Zr/Ti substitution gave one hit (Ag2ZnTiS4, 1.55 eV). Zr gives too-small gaps; Ti-Cu too wide. Next (iter 4-5): validate Ag2ZnTiS4 via literature; try Ti/Zr-Se mixes not possible; consider Hf-like analogues (not in palette), Mo/W (likely metallic), Ag-Sb/Bi halides, Cu-/Ag-based pnictides (Zn3P2-type, ZnSnP2 analogues, CdSnP2/ZnGeAs2) via zincblende or chalcopyrite with P/As; those have gaps 1.0-2 and are mostly known but Ag-/Cd- variants may be novel. Avoid Na-III-VI2 and Zr kesterites.

## [hypothesis] iteration 4 — 2026-10-11 02:45 UTC

Iter 4: II-IV-V2 pnictide chalcopyrites and ABX2 Sb/Bi ternaries are all known in MP (except KSbTe2, KBiTe2). Focus on novel Ag2-M-Si-Te4/Se4 kesterites: Si (small, hard) should widen the gap relative to Ge/Sn tellurides (0.4-1.5) toward ~1.4 eV; Ca variant tests size. Also KSbTe2/KBiTe2 as lone-pair alkali tellurides (probably narrow gap, exploratory).

## [observation] iteration 4 — 2026-10-11 02:50 UTC

Iter 4 (17 evaluated). Hit: KBiTe2 (novel, ehull 0.003, gap 1.296 eV). KSbTe2 stable but gap 0.55. Ag2-M-Si-Te4 kesterites unstable (ehull 0.08-0.12) with gaps 1.05-2.04; CaSi(AgTe2)2 gap 1.25 but ehull 0.12; CaSi(AgSe2)2 ehull 0.19. Alkaline-earth/Si/Ge/Sn pnictide chalcopyrites (Ca/Sr/Ba x As/Sb) strongly unstable (ehull 0.13-0.30); Mg/Zn/Cd-Si/Ge-Sb2 unstable or zero gap. KGaSe2 stable but 2.18 eV. II-IV-V2 As and I-V-VI2 Sb/Bi (Na, Cu, Ag, K) mostly already in MP/considered. Note KBiTe2 may be metastable-polymorph in chalcopyrite-derived cell; real structure likely layered/NaCl-type ordered — treat cautiously.

## [reflection] iteration 4 — 2026-10-11 02:50 UTC

Pnictide hypothesis falsified for novel Ca/Sr/Ba and Sb members; Si tellurides falsified. Productive new lead: alkali-Bi tellurides (KBiTe2 1.30 eV, ehull 0.003). Next iteration (5): probe analogues (Na/K/Ag with Bi/Sb mixtures, ordered rocksalt-derived I-V-VI2 like AgBiS2-type), K-Bi-Se/S already in MP. Also consider validating Ag2ZnTiS4 and KBiTe2 via literature. Avoid Ca/Sr/Ba pnictides, Si-Te kesterites, K/Na-III chalcogenides (too wide).

## [hypothesis] iteration 5 — 2026-10-11 02:50 UTC

Iter 5: chalcopyrite I-III/V-VI2 all already considered. Test alkali (Na/K) kesterite-type A2MBX4 (M=Zn/Cd/Mg, B=Sn/Ge, X=Se/Te): ionic Ag/Cu replacement; Te variants expected narrower gaps than selenides, hopefully 1.1-1.7. Also two Ti-S Ag compounds with Mn/Ni as extension of Ag2ZnTiS4 (likely small gap, low priority). Caveat: alkali ions in tetrahedral kesterite sites are likely strained; true structures probably differ (e.g., K2CdSnSe4 is known).

## [observation] iteration 5 — 2026-10-11 02:57 UTC

Iter 5 (20 evaluated, no vetoes). New hits (novel, ehull<=0.05, gap 1.1-1.7): K2MgSnTe4 (0.0, 1.329), K2MgGeTe4 (0.0, 1.499), K2ZnSnTe4 (0.0, 1.573), Na2CdSnTe4 (0.032, 1.367), Na2MgGeTe4 (0.047, 1.136), TiMn(AgS2)2 (0.0, 1.479; Mn magnetism/DFT gap suspect). Misses: Na selenides stable but gaps 1.96-2.48; K2Cd tellurides 0.86-0.88 (too low); K2ZnGeTe4 1.90; TiNi(AgS2)2 unstable. Gap trend: K tellurides with Mg/Zn nearest 1.4 target. Caveat: kesterite cell for large K likely not the true ground state; CHGNet hull ~0 may be an artifact of patchy references.

## [reflection] iteration 5 — 2026-10-11 02:57 UTC

Alkali-telluride kesterite hypothesis held: K2MgSnTe4 (1.33 eV, ehull 0) is the closest to 1.4 eV among stable novel candidates in the campaign aside from CdAg2Ge/SnSe4 (1.26-1.28). Se->Te and Mg/Zn choice tunes the gap. Follow-up if more iterations: K/Na mixing, K2Mg(Sn,Ge)Te4 alloys, validating structures with polymorph searches (K compounds probably prefer different structure types), and DFT-level checks of Ag2ZnTiS4, TiMn(AgS2)2, KBiTe2. Campaign ends here.
