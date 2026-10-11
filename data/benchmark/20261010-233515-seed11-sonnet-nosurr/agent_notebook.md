# Lab Notebook

## [hypothesis] iteration 1 — 2026-10-10 23:35 UTC

Kesterite family: CZTS (gap ~1.5, known). Isoelectronic substitutions Cu->Ag, Zn->Cd/Mg, Sn->Ge/Si, S->Se should tune gap near 1.4 eV. Ag-based and mixed Cd/Ge kesterites are less explored; expect Se analogs ~1.0-1.4. Propose broad family, evaluate only novel ones.

## [observation] iteration 1 — 2026-10-10 23:43 UTC

17 novel evaluated. Hits (gap 1.1-1.7, Ehull<=0.05): CdAg2GeSe4 (0.0, 1.28), MgAg2SnSe4 (0.016, 1.59), ZnAg2GeSe4 (0.0, 1.12), MgAg2GeTe4 (0.025, 1.49), MgAg2SnTe4 (0.038, 1.17), ZnAg2GeTe4 (0.028, 1.17). Near-stable but wide gap: MgAg2GeS4 1.89, MgAg2GeSe4 1.86, MgAg2SnS4 1.87. Si-containing: unstable (Ehull>0.13). Cd-Te compounds gap too small (0.4-0.5). MgCu2GeSe4 unstable (0.136). Caveat: propose_candidates applies substitutions simultaneously, so Cu was never mixed with Ag.

## [reflection] iteration 1 — 2026-10-10 23:43 UTC

Hypothesis held: Ag-based Ge/Sn kesterites with Se/Te anions give stable, in-window gaps. Si is destabilizing (size mismatch). Next: Cu/Ag mixed cations, S/Se anion mixing (e.g. MgAg2Sn(S,Se)4 targeting 1.4), Ca/Sr/Ba and chalcopyrite/zincblende prototypes for exploration; also Zn Ag2 SnSe4 is known (calibration).

## [hypothesis] iteration 2 — 2026-10-10 23:43 UTC

Iteration 2: Extend Ag-kesterite hits. Wide-gap S/Se Mg/Ge/Sn analogs (1.6-1.9) should drop toward 1.4 with heavier alkaline-earth / Cd / Zn and Se; Ca/Sr/Ba on the divalent site with Ag2 Sn/Ge Se4 (larger A cation) may give stable compounds with gaps 1.2-1.7. Also try Zn/Cd Ag2SnS4/Se4 and Ag2 Ge S4 variants. Literature search gave nothing specific on Ag2-II-IV-VI4 gaps.

## [observation] iteration 2 — 2026-10-10 23:51 UTC

19 novel evaluated. Ag-AE series: SrAg2GeSe4 (Ehull 0.003, gap 1.687) borderline hit; SrAg2SnSe4 (0.0, 1.70), SrAg2SnS4 (0.0, 1.72), SrAg2GeS4 (0.013, 1.87) just above window; Sr/Ba tellurides stable but gap ~0.1-0.7 (metallic-like, too small). Ca analogs unstable (0.05-0.09), Ca size too small for tetrahedral kesterite. Cu-based: SrCu2SnSe4 (0.050, 1.11) marginal; Ca-Cu all unstable (0.07-0.12). Chalcopyrite batch nearly all known, not evaluated. Note Sr compounds likely adopt a different true structure (Sr large, e.g. Ba2... trigonal/ orthorhombic) but the hull says stable in this prototype.

## [reflection] iteration 2 — 2026-10-10 23:51 UTC

Sr is the sweet spot among AE cations in Ag2-AE-IV-Se4 (stable, gap ~1.7 edge). Gap-lowering needed: Se->Te mixing is too aggressive; try Sr(Ag,Cu)-mixed or Cd/Sr cation mixing, or S/Se with Sn/Ge mixing. Prior-iteration Zn/Cd/Mg Ag2 Ge/Sn Se/Te remain best hits (CdAg2GeSe4 1.28, ZnAg2GeSe4 1.12). Next: unexplored prototypes (zincblende-derived pnictides e.g. Zn-Sn-P/As II-IV-V2, I-III-VI with Na), and Cu/Ag mixtures via custom approach. Propose_candidates cannot mix elements at one site, which limits alloy exploration.

## [observation] iteration 3 — 2026-10-11 00:08 UTC

Iteration 3: II-IV-V2 chalcopyrite and I-III-VI2 families were almost entirely known or SMACT-rejected (P compounds rejected), nothing evaluated there. Moved to kesterite with Zr/Ti on IV site and Mn/Fe/Mg/Ca/Ba on II site. 20 evaluated (critic vetoed 5 Ba-Ti/Zr by radius mismatch). No hits. Stable (Ehull 0) but gap far too small: ZrZn(AgSe2)2 0.65, ZrCd(AgSe2)2 0.30, ZrZn(AgS2)2 0.19, ZrMn(AgSe2)2 0.0, ZrZn(CuSe2)2 0.21, ZrZn(CuS2)2 0.30, MgZr(CuSe2)2 0.19, MgZr(CuS2)2 0.18, MgZr(AgS2)2 0.33. These small gaps with Ehull=0 look suspicious (Zr4+ in tetrahedral site is chemically implausible; hull likely lacks competing phases; ML gap may be unreliable). In-window gap but unstable: MgZr(AgSe2)2 (gap 1.58, Ehull 0.46). Wide gap: Na2MgZrS4 stable, gap 3.9. Fe-Ag-Ge/Sn-Se/S: unstable (0.07-0.14), gap ~0 (metallic). MnAg2GeS4 Ehull 0.079 gap 2.24. Ca/Ti variants unstable.

## [reflection] iteration 3 — 2026-10-11 00:08 UTC

Hypothesis (Zr/Ti kesterites with Mg swapping up the gap) falsified: d0 Zr/Ti on tetrahedral site gives small gaps when stable, wide/unstable otherwise. No new hits this iteration. Best campaign candidates remain iteration-1 Ag-Ge/Sn kesterites (CdAg2GeSe4, ZnAg2GeSe4, MgAg2SnSe4, MgAg2GeTe4) and SrAg2GeSe4. Next (iter 4-5): stay in the proven Ag-II-IV-Se/Te family; explore zincblende-GaAs prototype for novel ternary/quaternary I-III-VI or Ag-Sb/Bi variants; or Cd/Zn-Ag2-Ge S/Se with Te partial -- but mixed-anion not supported; consider Cd-Ag2-SnS4/Se4 sister compounds already considered. Avoid Zr/Ti/Fe/Mn/Ca/Na2 variants.

## [hypothesis] iteration 4 — 2026-10-11 00:08 UTC

Iteration 4: zincblende prototype yields only binaries (useless). Instead test alkali (Na/K) I2-II-IV-VI4 kesterite-type with Se/Te: ionic alkali raises CBM relative to Cu/Ag, so Te analogs (small gaps for Ag) may reach 1.1-1.7. Expect Ehull may be higher because alkali tetrahedral coordination is unnatural (real compounds have different structure, e.g. K2CdSnSe4 known), so treat as exploratory. Evaluate ~16 mixing Na/K, Zn/Cd/Mg, Sn/Ge, Se/Te.

## [observation] iteration 4 — 2026-10-11 00:14 UTC

Iter 4: zincblende prototype gives only binaries (nothing evaluated). 20 alkali kesterite-type novel compounds evaluated; most near-stable. New hits (gap 1.1-1.7, Ehull<=0.05): K2ZnSnTe4 (Ehull 0.0, gap 1.57), K2MgSnTe4 (0.0, 1.33), Na2CdSnTe4 (0.032, 1.37). Near misses: Na2CdGeTe4 (0.021, 1.74), K2ZnGeTe4 (0.0, 1.90), K2CdSnTe4 (0.0, 0.86), K2CdGeTe4 (0.0, 0.88). Selenides all gap 1.96-2.5 (too wide). Caveat: K-based compounds in tetrahedral kesterite prototype are probably not true ground-state structures; Ehull 0 vs hull of known phases (K2CdSnSe4 etc. have different real structures) means actual stability/gap needs structure check. Te + Sn lowers gap; Mg/Zn/Cd trend Cd < Mg < Zn.

## [reflection] iteration 4 — 2026-10-11 00:14 UTC

Alkali tellurostannates worked: three new in-window hits, two with Ehull 0. For iteration 5: refine around K/Na-II-Sn-Te (e.g. Rb/Cs not in palette; try Ba/Sr-based or Na/K with Ca/Sr, Mn; K2Zn/Mg Sn Te variants; Ag/Na mixes not possible). Also vary Sn-Te with Zn/Cd/Mg for Na (Na2ZnSnTe4 2.05, Na2MgSnTe4 1.93 too wide). Selenides too wide; stick with tellurides. Caveat on structure realism should be flagged in final summary.

## [hypothesis] iteration 5 — 2026-10-11 00:14 UTC

Iteration 5: Literature gives nothing on alkali-II-IV-Te4. Extend iteration 4 hits: Na/K-(Mn, Ca, Sr, Ba, Mg, Zn, Cd)-(Sn, Ge)-Te4. Te+Sn lowers gap; Mg/Zn/Cd site tuned gap; Mn/Ca/Sr/Ba on II site untested for alkali. Also Na/K with Ag-free Ge/Sn Te at gap boundary (Na2CdGeTe4 1.74, K2ZnGeTe4 1.90) -> expect Sn analogs with Mn/Ca lie in window. Evaluate novel ones only.

## [observation] iteration 5 — 2026-10-11 00:21 UTC

Iter 5: 15 novel alkali-AE/Mn-IV-Te4 evaluated (K2BaSnTe4 known, skipped). New hits (gap 1.1-1.7, Ehull<=0.05): K2CaGeTe4 (0.019, 1.42 - closest to 1.4), K2SrSnTe4 (0.012, 1.20), K2SrGeTe4 (0.013, 1.22), K2BaGeTe4 (0.0, 1.57), K2CaSnTe4 (0.033, 1.12). Near misses: Na2CaGeTe4 (0.0, 1.73), K2MnGeTe4 (0.002, 1.10), Na2MnGeTe4 (0.043, 1.09). Na-Sr/Ba and Na2CaSnTe4 unstable (0.06-0.17). K2Mn-Sn gap 0.65. Trend: K is a better host than Na for large AE cations; gap Ca>Sr for Ge. Caveat: ML gap and hull for hypothetical kesterite-type structures; real alkali/AE tellurides likely adopt other structure types (e.g. K2BaSnTe4-like), so structure verification and a PBE/HSE check are needed.

## [reflection] iteration 5 — 2026-10-11 00:21 UTC

Hypothesis held: heavier K + Ca/Sr/Ba on the II site with Ge/Sn tellurides gives stable in-window gaps; 5 new hits, K2CaGeTe4 best (1.42 eV, Ehull 0.019). Campaign-wide: Ag-kesterite selenides (CdAg2GeSe4, ZnAg2GeSe4), alkali tellurides (K2CaGeTe4, K2MgSnTe4, K2SrSnTe4, K2BaGeTe4). Failures: Si, Zr/Ti, Fe/Mn Ag, Ca-Cu. Unspent 5 relaxations since no further novel compounds in the family were proposable. Next steps beyond campaign: verify structures against true K-AE-Ge-Te structure types, check dynamical stability, toxicity/air-stability of tellurides, and defect tolerance.
