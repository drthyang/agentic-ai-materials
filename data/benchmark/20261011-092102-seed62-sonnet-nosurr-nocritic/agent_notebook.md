# Lab Notebook

## [hypothesis] iteration 1 — 2026-10-11 09:21 UTC

Kesterite family: Cu2ZnSnS4 (gap ~1.5) mixed-cation/anion variants (Ag/Cu, Cd/Zn, Ge/Sn, S/Se) should keep gap in 1.1-1.7 and be near hull. Quaternary I2-II-IV-VI4 with isoelectronic substitutions; many known (CZTSe, CZGS, CCTS), aim for unexplored ones (Ag2ZnSnSe4, Ag2CdGeS4, Cu2CdSiS4 etc.). Se lowers gap, Ge/Si raise it, Ag raises it, Cd lowers it.

## [reflection] iteration 1 — 2026-10-11 09:22 UTC

Evaluated 20 novel Ag-based kesterite-type I2-II-IV-VI4. HITS: CdAg2GeSe4 (Eg 1.28, Ehull 0.00) and MgAg2GeTe4 (Eg 1.49, Ehull 0.025). Near misses: MgAg2GeSe4 (1.86, 0.02), MgAg2GeS4 (1.89, 0.017), CaAg2GeSe4 (1.68, 0.062), CdAg2GeTe4 (0.48, 0.017), ZrCd(AgSe2)2 (0.30, 0.0, gap too low). Trends: Si-containing variants unstable (Ehull 0.08-0.19, likely size mismatch); Ti/Zr (except Zr-Cd) very unstable; Ge is the sweet spot; Cd->Mg raises gap ~0.5-1.0 eV, Se->Te lowers it ~0.8 eV, so Mg/Cd mixing or Se/Te mixing could fine-tune (e.g. Cd0.5Mg0.5Ag2GeSe4, MgAg2Ge(Se,Te)4). Next: Cu/Ag mixed, Sn-based Ag analogues, chalcopyrite AgGaSe2-like alloys, and nitride/phosphide zincblende family for exploration. Caveat: CHGNet/ML gaps; Ag2CdGeSe4 hull 0 might reflect sparse competing phases.

## [observation] iteration 2 — 2026-10-11 09:23 UTC

Iter 2: 19 novel evaluated. HITS (gap 1.1-1.7, Ehull<=0.05): ZnAg2GeSe4 (1.12, 0.00), MgAg2SnSe4 (1.59, 0.016), MgAg2SnTe4 (1.17, 0.038), ZnAg2GeTe4 (1.17, 0.028), SrAg2GeSe4 (1.69, 0.003 - edge of window). Near: SrAg2SnSe4 (1.70, 0.0), SrAg2SnS4 (1.72, 0.0), SrAg2GeS4 (1.87, 0.013). Gap too low: CdAg2SnTe4 0.41, ZnAg2SnTe4 0.60. Cu-based Mg/Ca/Sr kesterites all unstable (Ehull 0.05-0.12) -> Cu with large/hard cations disfavored; Ag stabilizes. NaGaS2 gap 3.8 (wide, not useful). Chalcopyrite proposals were nearly all known in MP. 1 relaxation unspent (no good novel candidates left).

## [reflection] iteration 2 — 2026-10-11 09:23 UTC

Ag2-AE/M-Ge/Sn-Se4 family robust: Ag is the key to stability; gap ordering Zn(1.1)<Mg(1.6)~Sr(1.7)<..., Se->Te lowers ~0.4-0.8. Ideal ~1.4 might come from Zn/Mg mixing or Ge/Sn + Se/Te mixing (needs ordered supercells, not available via prototype subs). Next iteration: explore a different family (e.g. zincblende-derived I-III-VI / II-IV-V2 pnictides like ZnSnP2-type, Zn/Cd-Ge/Sn-P/As, or Ag-Sb/Bi chalcogenides) to diversify; also try Ag2-Ba/Sr-Ge-Te4 and Ag2-Zn-Sn-Se alloys.

## [observation] iteration 3 — 2026-10-11 09:24 UTC

Iter 3: II-IV-Sb2 chalcopyrite-type antimonides (Zn/Cd/Mg × Si/Ge/Sn) all unstable (Ehull 0.12-0.28) with gaps mostly <0.6 (ZnSiSb2 gap 1.2 but Ehull 0.28). P analogues rejected by SMACT. Pnictide family falsified in this prototype. BaAg2GeSe4 known in MP (gap 0.035 -> ML gap unreliable/low). Returning to Ag-chalcogenide kesterite family to fill gaps: Zn/Cd × Sn × S/Se, Zn Ge S, and Ag/Cu mixing.

## [observation] iteration 3 — 2026-10-11 09:25 UTC

Iter 3 results. (1) II-IV-Sb2 antimonides: all Ehull 0.12-0.28, falsified. (2) Fe/Mn Ag kesterites: Fe gives gap ~0 (metallic, Ehull 0.07-0.13); MnAg2GeS4 gap 2.24, Ehull 0.079 -> no. BaAg2GeTe4 (0.705, Ehull 0.0) and BaAg2SnTe4 (0.52, 0.007) stable but gap too low. (3) Alkali-pnictogen-chalcogenides: KBiTe2 HIT (gap 1.296, Ehull 0.003, novel vs MP) in chalcopyrite-derived prototype; KSbTe2 stable (0.547 eV) gap low; NaGaSe2 (2.20, 0.017), KGaSe2 (2.18, 0.0) wide gap. Caveat: KBiTe2 prototype is chalcopyrite-derived; real ground state likely rocksalt-ordered (alpha-NaFeO2-like) variant, and ML gap w/o SOC likely overestimates for Bi. Remaining 2 relaxations unspent: no novel candidates left.

## [reflection] iteration 3 — 2026-10-11 09:25 UTC

Pnictide II-IV-V2 and Fe/Mn kesterites falsified; Ag-chalcogenide kesterites (Ba, Te) stable but gap too low. New lead: A+Bi/Sb-Te2 (A=K) family; next iteration try K/Na-Bi-Se/Te variants, Cu/Ag-Bi-chalcogenides in other prototypes, and mixed anions (KBi(S,Te)2) — prototype tool is limited to 3 templates, so use zincblende-GaAs substitutions for ordered rocksalt-like analogues. Also revisit Ag2-Zn/Mg-Ge-Se alloy for ideal 1.4 eV, and verify KBiTe2 against literature (KBiTe2 / alkali bismuth tellurides as PV/thermoelectrics).

## [hypothesis] iteration 4 — 2026-10-11 09:25 UTC

Iter 4: Expand the A(I)-Bi/Sb-chalcogenide family (KBiTe2 hit, 1.30 eV). Substitute Cu->K/Na/Ag, In->Bi/Sb, Se->S/Se/Te in chalcopyrite template. Expect AgBiSe2/AgBiS2/NaBiSe2-type, KBiSe2, KBiS2 gaps rising from Te (1.3) to Se (~1.5-1.8) -> window. Ag-Sb/Bi lower gaps. Literature: alkali bismuth chalcogenide nanocrystals (NaBiS2, KBiS2) studied as photodetectors, so some may be in MP; look for novel ones. Also Ag-Bi-I/ Cu-Bi-I with halides in later step.

## [observation] iteration 4 — 2026-10-11 09:26 UTC

Iter 4 (20 budget, 20 used). A-Bi/Sb-X2 chalcopyrite subs all already considered (no new). (1) Remaining Ag2-AE-Ge/Sn-X4: CaAg2* unstable (Ehull 0.05-0.09, Ca too small/hard for Ag-chalcogenide); SrAg2GeTe4 (0.155 eV, 0.016) / SrAg2SnTe4 (0.10, 0.029) stable but metallic-ish; MgAg2SnS4 (1.87, 0.002) gap slightly high. No hits. (2) zincblende and II-IV-N2 subs: nearly all known; skipped. (3) NEW FAMILY: I3-V-VI4 famatinite-type (kesterite template with Zn->Cu/Ag, Sn->Sb/As). HITS (gap 1.1-1.7, Ehull<=0.05, novel vs MP): CuAg2AsSe4 (1.378 eV, Ehull 0.000) - closest to ideal; CuAg2SbSe4 (1.457, 0.000); Ag3SbSe4 (1.665, 0.000); Ag3AsSe4 (1.681, 0.000). Near misses: Ag3SbS4 1.79, Cu2AgSbS4 1.74, CuAg2SbS4 1.86, Cu2AgAsS4 1.87 (all Ehull 0); Cu2AgSbSe4/Cu2AgAsSe4 gap ~0.43 (Cu-rich Se, gap too low); P variants wide gap 2.1-2.4. Trend: Ag content raises gap (Cu2Ag 0.43 -> CuAg2 1.4 -> Ag3 1.67), S vs Se +0.4 eV. Caveats: CHGNet+ML gap; hull 0 for ordered Cu/Ag mixtures suggests competing phases may be sparse; Cu/Ag ordering on sites arbitrary; sharp gap jump Cu2Ag->CuAg2 (0.43->1.4) suspicious, may reflect ordering/structural artifact.

## [reflection] iteration 4 — 2026-10-11 09:26 UTC

Iter 4: Productive new family (I3-V-VI4 Cu/Ag-Sb/As-Se4). Best new leads: CuAg2AsSe4 (1.38 eV), CuAg2SbSe4 (1.46). Ag-chalcogenide kesterite II-IV family largely exhausted (Ca fails, Te gives low gap). Next (iter 5): verify with literature (Cu3SbSe4, Ag3SbSe4 / Ag3AsSe4 known as proustite/pyrargyrite-type? in reality Ag3AsS3 forms are different), try Cu2Ag mixed S/Se anions not possible in template; try Te-containing Sb variants (CuAg2SbTe4, Ag3SbTe4 known) and Cu3SbSe4-like Na/Li? Also S/Se ordered mixes are unavailable; consider remaining untried Cu2AgBi/ Cu2AgPSe4 irrelevant. Remember the gap jump caveat.

## [hypothesis] iteration 5 — 2026-10-11 09:26 UTC

Iter 5: Extend I3-V-VI4 famatinite family: Bi analogues (Cu/Ag-Bi-Se/S), Te analogues of Sb/As (Te lowers gap ~0.4-0.8 so Ag3(Sb/As)Te4 and CuAg2 could land near 1.1-1.4), plus Cu-rich S variants (Cu3AsS4 etc. perhaps known). Famatinite Cu3SbS4 is a studied PV absorber (lit), supporting family relevance. Aim: gap-tuned novel members closer to 1.4 than Ag3SbSe4; Ag-rich needed for gap, Se/Te for lowering.

## [observation] iteration 5 — 2026-10-11 09:28 UTC

Iter 5: Famatinite I3-V-VI4 Bi/Te variants all already 'considered' (0 new). Explored Co/Ni/Mn kesterites. 15 evaluated. HITS: NiAg2GeSe4 (1.648, Ehull 0.000), NiAg2SnSe4 (1.676, 0.000), Cu2NiGeS4 (1.12, 0.013). Near: NiAg2GeS4 (1.74, 0.008), NiAg2SnS4 (1.90, 0.0). Fails: Co variants unstable (0.056-0.11, except CoAg2SnS4 gap 1.39 but Ehull 0.092); MnCu2GeSe4 0.104, MnCu2SnS4 (1.50, 0.07); Si variants unstable again; Te gives gap ~0. Caveats: tetrahedral Ni2+ is chemically suspicious (d8 prefers square planar/octahedral); ML gap for open-shell TM likely unreliable (spin state, no U); hull may be flattered by sparse Ag-Ni-X competing phases. Treat Ni hits as low-confidence.

## [reflection] iteration 5 — 2026-10-11 09:28 UTC

Campaign end. Most robust leads: Ag-chalcogenide II-IV kesterite-types with closed-shell cations (CdAg2GeSe4 1.28, ZnAg2GeSe4 1.12, MgAg2SnSe4 1.59, MgAg2GeTe4 1.49) and I3-V-VI4 Cu/Ag-As/Sb-Se4 (CuAg2AsSe4 1.38, CuAg2SbSe4 1.46); plus KBiTe2 (1.30, caveat on SOC/prototype). Ni/Mn/Co extension is low-confidence. Falsified: pnictide II-IV-V2, Si, Ti/Zr, Fe, Ca-based. Next steps beyond this campaign: DFT/HSE+SOC verification, ordering/polymorph competition (e.g. stannite vs kesterite, sulvanite/enargite for Ag3SbSe4), and experimental synthesis feasibility. Tool limitation: 'already considered' blocks re-proposal of unevaluated formulas; 5 relaxations left unspent due to no further novel candidates.
