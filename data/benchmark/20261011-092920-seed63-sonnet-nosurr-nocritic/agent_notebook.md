# Lab Notebook

## [hypothesis] iteration 1 — 2026-10-11 09:29 UTC

Kesterite family: CZTS gap ~1.5 (S), CZTSe ~1.0. Substituting Zn->Cd/Mg, Sn->Ge/Si, Cu->Ag, anion S/Se mixing should tune gap into 1.1-1.7. Propose many multi-element substitutions on kesterite, evaluate novel ones.

## [observation] iteration 1 — 2026-10-11 09:30 UTC

16 novel Ag-based kesterite-type evaluated. Hits (gap 1.1-1.7, ehull<=0.05): CdAg2GeSe4 (gap 1.28, ehull 0.0), MgAg2GeTe4 (1.49, 0.025). Near misses: MgAg2GeSe4 (1.86, 0.02), CdAg2GeTe4 (0.48, 0.017), CaAg2GeSe4 (1.68, 0.062). Si-containing: unstable (0.08-0.19). Zr-containing: Cd/Mg-Zr tellurides/selenide hull 0 but gaps 0-0.84 (ZrCd(AgSe2)2 0.30); Ca-Zr, Mg-Zr-Se unstable. Note: propose_candidates forced Cu->Ag; no Cu-based variants were generated. Trend: Se->Te lowers gap ~0.8 eV; Mg->Cd lowers gap ~0.6.

## [reflection] iteration 1 — 2026-10-11 09:30 UTC

Hypothesis supported: Ag2-II-Ge-X4 family yields stable, in-window candidates. Caveat: CdAg2GeSe4 probably resembles known Ag2CdGeSe4 (a known compound in different structure) — novelty is relative to MP only; CHGNet/ML gaps are uncertain. Next: mixed anions (Se/Te, S/Se) e.g. Ag2CdGe(Se,Te) to tune; Ag2-Cd/Zn-Sn-S/Se; Cu-Ag mixing; Zn variants; and a different family (chalcopyrite, I-III-VI2 Ag-based, or Sb/Bi chalcogenides) for exploration. Avoid Si and Ca/Zr.

## [hypothesis] iteration 2 — 2026-10-11 09:30 UTC

Iter 2: Explore chalcopyrite family with mixed-cation/anion substitutions: Ag(In,Ga,Al)(S,Se,Te)2 and Cu variants (CuAlTe2, CuGaTe2, etc. mostly known). Novel ones likely come from Sb/Bi/Sn/Ge-containing or exotic pairs (e.g., AgInTe2 known; AgAlTe2, AgGaTe2 maybe). Gaps: AgGaSe2 1.8, AgInSe2 1.2, AgGaTe2 1.3, so Ga/In mixing and Te should land in window. Also try kesterite Cu2-Zn/Cd-Ge/Sn-Se/Te variants for Cu-containing members.

## [observation] iteration 2 — 2026-10-11 09:31 UTC

Iter 2 (20 relaxations, all novel). Chalcopyrite proposals were nearly all known in MP (only NaGaS2/NaAlS2 novel: ehull 0 but gaps 3.8/4.6, wide). Kesterite with Cu: MgCu2SnSe4 gap 1.38 but ehull 0.071 (no); SrCu2SnSe4 gap 1.11 ehull 0.050 (borderline); MgCu2GeSe4 1.10/0.136; Cu tellurides: BaCu2GeTe4 ehull 0.034 gap 0.50; SrCu2SnTe4, BaCu2SnTe4 hull 0 but gaps 0.87/0.14; MgCu2SnS4 gap 2.17 ehull 0.02. Ag-Sn: HITS MgAg2SnSe4 (gap 1.59, ehull 0.016) and MgAg2SnTe4 (gap 1.17, ehull 0.038). Near misses: SrAg2SnSe4 (1.70, 0.0), SrAg2SnS4 (1.72, 0.0), MgAg2SnS4 (1.87, 0.002). Ba/Sr/Cd Ag2SnTe4: gap 0.1-0.5 (too low).

## [reflection] iteration 2 — 2026-10-11 09:31 UTC

Hypothesis partly supported: Ag2-Mg-Sn-Se/Te give 2 new hits; total 4 hits across campaign (CdAg2GeSe4, MgAg2GeTe4, MgAg2SnSe4, MgAg2SnTe4). Cu analogs are less stable than Ag analogs (Ag favored in this model). Gap trend: Mg<Sr(~)... Mg gives wide gaps in Se, Te lowers; Ba/Sr tellurides collapse. Next: anion mixing (Se/Te) within Mg/Sr Ag2Sn/Ge to hit ideal 1.4 (e.g. SrAg2SnSe4 + Te, MgAg2SnS2Se2), Zn analogs, Cu/Ag mixes; chalcopyrite novelty is exhausted since MP covers most — switch prototype to zincblende-derived or Sb/Bi chalcogenides if available. Note wrapper can't do mixed-anion in one go easily; try listing multiple replacements.

## [observation] iteration 3 — 2026-10-11 09:33 UTC

Iter 3 (19 relaxations, all novel). NEW HITS: ZnAg2GeSe4 (gap 1.12, ehull 0.0), ZnAg2GeTe4 (1.17, 0.028), KBiTe2 (1.30, 0.003; chalcopyrite-type prototype, real structure likely layered/rocksalt-ordered, so unverified), SrAg2GeSe4 (1.69, 0.003, edge of window). Misses: ZnAg2SnTe4 (0.60, 0.039), SrAg2GeTe4 (0.16), KSbTe2 (0.55), KGaSe2/NaGaSe2 (2.2, stable but wide); MgAg2GeS4 / SrAg2GeS4 stable but gap 1.87-1.89. All Ca (Ag or Cu) and Mn-sulfide kesterites unstable (ehull 0.05-0.12). The zincblende prototype only gives binaries, so it was not useful. Cumulative hits: 8 (CdAg2GeSe4, MgAg2GeTe4, MgAg2SnSe4, MgAg2SnTe4, ZnAg2GeSe4, ZnAg2GeTe4, SrAg2GeSe4, KBiTe2).

## [reflection] iteration 3 — 2026-10-11 09:33 UTC

Hypothesis that Zn and Sr Ag2-Ge chalcogenides are in the window: supported. Ag2-II-Ge-Se/Te is the most productive family. Ca fails consistently, so avoid it. Next iteration: (1) check KBiTe2 and ZnAg2GeSe4 against the literature and consider their true ground-state structures, since the CHGNet relaxation is limited to the prototype; (2) explore other alkali-Bi tellurides/selenides (RbBiTe2 not in palette; try K/Na-Bi-Se/Te, Ag-Bi mixes); (3) test anion mixing Se/Te in Zn/Mg Ag2Ge/Sn to reach 1.4 eV. The wrapper does not appear to support mixed anions, so use alloy ideas only conceptually.

## [hypothesis] iteration 4 — 2026-10-11 09:33 UTC

Iter 4: (a) Fill remaining Ag2-II-IV-X4 gaps: Zn/Cd/Ba with Sn/Ge and S/Se (ZnAg2SnSe4, CdAg2SnSe4, ZnAg2GeS4, CdAg2GeS4, BaAg2GeSe4...). Expect Zn/Cd Se with Sn near 1.0-1.4, sulfides 1.6-1.9. (b) Chalcopyrite pnictide II-IV-V2 (Zn/Cd/Mg Sn/Ge P/As) and I-V-VI2 (Ag/Cu/Na/K with Bi/Sb) for exploration. Literature search returned nothing useful on Ag2ZnGeSe4, so MP novelty is the only check.

## [observation] iteration 4 — 2026-10-11 09:34 UTC

Iter 4 (20 relaxations, all novel in MP). Ag2-II-IV-X4 and I-V-VI2 / pnictide chalcopyrite spaces were exhausted (all "already considered" or known in MP). Switched to famatinite-type I3-V-VI4 (Cu/Ag with Sb/As/P/Bi, S/Se/Te) on the kesterite prototype. NEW HITS (gap in window, ehull<=0.05): CuAg2AsSe4 (1.378, 0.0) closest to ideal; CuAg2SbSe4 (1.457, 0.0); Cu2AgBiS4 (1.587, 0.0); Ag3SbSe4 (1.665, 0.0); Ag3AsSe4 (1.681, 0.0). Misses: sulfides Sb/As Ag/Cu 1.74-1.97 (stable, too wide); Cu2AgSbSe4/Cu2AgAsSe4 gap ~0.43 (Cu-rich selenides collapse, nonmonotonic jump 0.4 -> 1.4 going from 2 to 1 Cu — suspicious, CHGNet/ML gap noise); Cu2AgBiSe4 0.96; P compounds 2.1-2.4; tellurides 0.3-0.45. Note: Ag3SbSe4/Ag3AsSe4 in a famatinite structure are probably not true ground states (real Ag3SbS4 is pyrargyrite-type), though MP hull says 0.

## [reflection] iteration 4 — 2026-10-11 09:34 UTC

Hypothesis (new I3-V-VI4 family contains window gaps) supported: 5 new hits, total 13 across campaign. Gap trends: S > Se > Te by ~0.3-1.2 eV; Ag increases gap vs Cu; As ~ Sb; Bi lowers. Next (iter 5): exploit by mixed S/Se is unavailable; try Ag-rich sulfide-Bi analogs, Na/K-containing variants (Na3SbS4-type are wide), or Cu2AgBiS4 relatives with Zn/Cd mixing; also consider confirming robustness e.g. CuAg2AsSe4 neighbors (Cu/Ag/Sb/As Se). Remaining unevaluated: Cu3AsSe4-type known; Ag-Bi with Zn/Cd (Ag2ZnBi?) not charge balanced. Try famatinite with Sn->Sb/As and Zn->Cu/Ag only partially explored.

## [hypothesis] iteration 5 — 2026-10-11 09:35 UTC

Iter 5: Ti/Zr-containing Ag2-II-(Ti,Zr)-X4 sulfides/selenides (earlier Zr tellurides had low gaps, S/Se should be wider; Ti4+ d0 gives CB of d states, gap ~1-1.7) plus Na2-II-Ge-X4 (likely wide). Evaluate Ti/Zr Ag sulfide/selenide with Zn/Cd/Mg/Sr, and a couple of Na ones. Ca avoided.

## [observation] iteration 5 — 2026-10-11 09:36 UTC

Iter 5 (20 relaxations, all novel in MP). ONE new hit: TiZn(AgS2)2 = Ag2ZnTiS4 (gap 1.554, ehull 0.0). Zr-containing with Zn/Mg/Mn: stable (hull 0) but gaps 0-0.65 (metallic/narrow). Ti/Zr with Cd, Mg, Sr (and Ti selenides): unstable (0.35-0.5), gaps >1.7 – these are likely relaxation artifacts/mismatched sites. Na2-II-Ge-Se4: near-stable (0.011-0.055) but gaps 2.4-2.5, too wide. Caveat: Ag2ZnTiS4 in kesterite structure with Ti4+ tetrahedral is chemically unusual (Ti prefers octahedral); Ag2ZnTiS4 ehull 0 vs. other Ti analogs 0.35 suggests an isolated result; treat with caution.

## [reflection] iteration 5 — 2026-10-11 09:36 UTC

Hypothesis partly supported (1/20). Campaign total ~14 in-window, near-stable novel (MP-novel) compositions; strongest: Ag2-II-Ge/Sn-Se/Te kesterites (ZnAg2GeSe4, CdAg2GeSe4, MgAg2SnSe4), famatinite-type CuAg2AsSe4 (1.38), CuAg2SbSe4, Cu2AgBiS4, plus Ag2ZnTiS4. Caveats: gaps from ML/CHGNet-fidelity, prototype-restricted structures (true ground states may differ, e.g. Ag3SbSe4), novelty only vs MP. Follow-up recommendations: DFT/HSE verification, competing-phase check with real structures, mixed-anion alloys (Se/Te, S/Se) to tune gap to 1.4, and experimental feasibility check.
