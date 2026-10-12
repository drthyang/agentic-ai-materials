# Lab Notebook

## [hypothesis] iteration 1 — 2026-10-12 07:25 UTC

Kesterite family: Cu2ZnSnS4 gap ~1.5 (HSE), Se analog ~1.0. Substitutions Ag for Cu, Cd/Mg/Ca? for Zn, Ge/Si for Sn, and S/Se mixing should tune gap to ~1.1-1.7. Quaternary cation-mixed compounds (e.g. Ag2ZnSnS4, Cu2CdGeS4, Cu2ZnGeSe4 known; focus on novel ones e.g. Ag2CdSnS4, Ag2ZnGeS4, Cu2MgSnS4, Cu2CdSiS4). Expect Ag/Cd to widen/narrow gap moderately and stay near hull. Search for novel ones.

## [observation] iteration 1 — 2026-10-12 07:26 UTC

Evaluated 20 novel Ag2-M-X-Q4 kesterite-type compounds (M=Zn,Cd,Mg; X=Si,Ge,Sn; Q=S,Se,Te). All stable (ehull<=0.043). Hits in window: MgAg2SnSe4 (gap 1.153, ehull 0.043 - marginal), MgSi(AgTe2)2 (gap 1.627, ehull 0.014 - best). Near misses: ZnSi(AgTe2)2 1.717 (ehull 0.001), MgAg2GeS4 1.777 (0.006), MgSi(AgSe2)2 1.84, ZnSi(AgSe2)2 1.84 (0.0). Trends: Si widens gap most, Cd narrows gap (Cd 5s lowers CBM), Sn/Cd/Te narrow; sulfides 1.8-2.5. Gaps are mostly too big for Si/S and too small for Cd/Sn/Te; Cu was always replaced by Ag in this generator (no Cu variants).

## [reflection] iteration 1 — 2026-10-12 07:26 UTC

Hypothesis partly held: Ag-kesterite family is thermodynamically robust and tunable; 2 of 20 hit window. Next: target mid-gap members by mixing (e.g., Mg/Zn with Ge-Sn mixed, S/Se mixed anions like MgAg2GeSe2S2, ZnAg2GeS4-ish), and explore Ag->Cu/Ag mixing, Sn-Si partial, plus other families (chalcopyrite Ag/Cu-Ga/In-Te, e.g. AgGaTe2/AgInS2 mixes). Prioritise MgAg2SnSe4 and MgSi(AgTe2)2 refinements (Zn/Mg mixing to lower ehull).

## [hypothesis] iteration 2 — 2026-10-12 07:27 UTC

Iter 2: Move to chalcopyrite family and mixed-anion/mixed-cation members. Ternary Ag/Cu-III-VI2 endpoints are known (AgGaSe2 1.8, AgInSe2 ~1.2, AgGaTe2 ~1.3 exp); gaps in the 1.1-1.7 window are reached by alloying Ga/In and S/Se/Te. Propose novel ordered mixed variants (e.g. Ag-Al/Ga/In with Se/Te mixtures, Cu/Ag with Al-Te). Also Ag kesterite Mg/Zn-Ge-Se-S mixes to tune between 1.8 (S) and 0.3-0.7 (Se).

## [observation] iteration 2 — 2026-10-12 07:28 UTC

Iter 2: chalcopyrite Ag-III-VI2 all 9 known (novel=false) – skipped. Cu-kesterite (generator keeps Cu if Ag not in list) evaluated 20 novel. Near-stable (ehull<=0.05) but gaps too small: MgCu2GeSe4 (0.31, 0.030), MgCu2SnS4 (0.49, 0.014), MgCu2SnSe4 (0.19, 0.047), MgCu2GeTe4 (0.52, 0.017), MgCu2SiTe4 (0.25,0.034), MgCu2SnTe4 (0.35,0.026), MnCu2GeSe4 (0.66, 0.000). In-window gaps only for MgZr(CuSe2)2 (1.545) and MgZr(CuS2)2 (1.14) but ehull 0.144/0.093 -> unstable. Ca/Sr/Ti/Zr variants unstable (ehull 0.05-0.14). No new hit this iteration; Cu gaps ~0.8-1 eV lower than Ag analogs in this model.

## [reflection] iteration 2 — 2026-10-12 07:28 UTC

Hypothesis (Cu analogs via Mg/Mn/Ge/Si) falsified for gap: Cu-VBM pushes gaps too low; big cations (Ca, Sr) and Zr/Ti on tetrahedral sites destabilize. Next iteration: Ag-kesterite mixed-site alloys (Ag/Cu mixing is impossible in generator, so use Mg/Zn + Si/Ge anion mixes in Ag2 family: e.g. Ag2MgGeS4 (1.78) vs Se 0.28 -> S/Se mixing needs a mixed-anion formula, may not be available), or zincblende-GaAs derived III-V/II-VI-like ternaries (e.g. Zn-Sn-P2, Zn-Si-As2, Cd-Ge-P2 analogs ZnSiP2/CdSnAs2 type) which are an unexplored family with gaps ~1-2 eV. Prioritise MgSi(AgTe2)2 and ZnSi(AgTe2)2 as best existing leads.

## [hypothesis] iteration 3 — 2026-10-12 07:28 UTC

Iter 3: zincblende-derived II-IV-V2 pnictides (ZnSnP2 ~1.2-1.7, ZnGeP2 ~2.0, CdSnAs2 small, ZnSnAs2, MgSnP2 etc.). Many ternaries known; aim at novel ones: Mg/Cd/Zn with Si/Ge/Sn and P/As/Sb, plus I-III-V2-ish / Ag-containing variants, and Cu/Ag-IV-V nitrides. Isoelectronic ordering of GaAs (1.4 eV) cation pair -> II+IV. Expect gaps 0.5-2 eV; P-based with Sn/Ge near window.

## [observation] iteration 3 — 2026-10-12 07:30 UTC

Iter 3: used 16/20 relaxations (rest: no novel candidates left in generator). (a) zincblende prototype only gives binaries (known). (b) II-IV-Sb2 antimonides (novel: ZnGeSb2 0.24 eV/0.009, ZnSiSb2 0.91/0.048, CdGeSb2 0.14/0.032, CdSiSb2 0.20/0.057, MgSnSb2, MgGeSb2 ~0 gap, ehull ~0.08) - gaps too small. P analogs rejected by SMACT filter. (c) Alkali I-III-VI2 (novel NaGaSe2 3.08, KGaSe2 3.31, NaGaS2 4.2, KAlS2 3.9, NaAlS2 4.1 all stable but far too wide; KSbTe2 0.36, KBiTe2 0.56 too narrow). (d) CuBiTe2: gap 1.446, ehull 0.052 - in window, marginally above hull limit (0.05); best lead of iteration but not strictly qualifying. (e) Nitrides: TiCdN2 gap 1.51 but ehull 0.124; CdSnN2 (calibration, known) 1.71/0.122 unstable. Cu kesterite sulfides and Cu chalcopyrites all known/already considered.

## [reflection] iteration 3 — 2026-10-12 07:30 UTC

Hypotheses largely falsified: pnictide gaps too small (Sb) and alkali chalcogenides too wide. Generator is limited (3 prototypes, 2-site substitution restricts to known fam.). Pattern: gaps bracket window but novel compositions rarely land inside. Best leads so far: MgSi(AgTe2)2 (1.63, 0.014), CuBiTe2 (1.45, 0.052), MgAg2SnSe4 (1.15, 0.043). Next iteration: explore Bi/Sb-based I-V-VI2 variants with mixing e.g. CuBiTe2-like with Ag/Cu on different sites, Na/K-Bi/Sb with Se (gap tuning between), and intermediate-gap Ga/Al-Te alkali (NaGaTe2/KGaTe2 known) ; also Ag kesterite Te/Sn-Ge intermediate (e.g. MgAg2GeTe4, MgAg2SnTe4) and Zn/Mg-Si-Te variants not yet considered.

## [hypothesis] iteration 4 — 2026-10-12 07:30 UTC

Iter 4: Fill the Ag-kesterite gap-map holes between Se (too narrow/wide) and Te: Mg/Zn × Si/Ge/Sn × Te, plus Se variants with Mg/Zn and Sn/Ge not yet evaluated (some may already be done; generator reports novelty). Also Mn/Mg/Zn-Ag Te variants, and Ag-Cd-Si-Te leads are too narrow (0.33) while Mg/Zn-Si-Te are 1.6-1.7; Mg/Zn-Ge-Te expected ~1.2-1.5 (Ge lowers gap vs Si). Aim: ZnAg2GeTe4, MgAg2GeTe4, MgAg2SnTe4, ZnAg2SnTe4. Mn also tried.

## [observation] iteration 4 — 2026-10-12 07:31 UTC

Iter 4 (20/20 used, all novel): (a) Ca-Ag-kesterites: ehull 0.06-0.09, unstable; only CaAg2SnSe4 in-window (1.45) but ehull 0.089. (b) CuAsS2 (0.68, 0.085), KAsS2 (2.82, 0.114): no. (c) AII-Sn(II)-Q2 chalcopyrite-type (Ba/Sr/Ca-Sn-S/Se/Te): ehull 0.11-0.26, metallic-ish gaps ~0: falsified. (d) Ag-Zr/Ti kesterites: ZrZn(AgSe2)2 gap 1.33 ehull 0.080; ZrZn(AgS2)2 1.22 / 0.106; ZrCd(AgSe2)2 0.01/0.088; TiZn(AgSe2)2 gap 1.887 ehull 0.014 (stable, gap slightly high - best near-miss, Ti d0 CBM lowers gap vs Si/Ge analogs ~1.84). No qualifying material this iteration. Sandbox of generator largely exhausted (many 'already considered').

## [reflection] iteration 4 — 2026-10-12 07:31 UTC

Iter 4: hypotheses to widen scope to Ca, Sn(II), Zr/Ti failed on stability, except TiZn(AgSe2)2 (stable, 1.89 eV, a bit wide). Trend: Zr gives in-window gaps but ehull 0.08-0.1; Ti stable but gap too wide. Next (final iter 5): try Ti-containing Ag kesterites with Mg/Cd/Zn and Te (TiZn(AgTe2)2, TiCd(AgSe2)2, TiCd(AgS2)2 predicted narrower, e.g. Cd lowers gap by ~0.5-1 eV -> TiCd(AgSe2)2 might be ~1.2-1.4 and stable), plus TiMg(AgTe2)2, TiZn(AgTe2)2, Hf-free. Also reconsider MgSi(AgTe2)2 (1.63, 0.014) as the best qualifying lead in the campaign.

## [hypothesis] iteration 5 — 2026-10-12 07:31 UTC

Iter 5: Ti(IV) on the Sn site in Ag kesterites (TiZn(AgSe2)2 was stable, 1.89 eV). Ti d0 lowers CBM; Cd/Te lower gap further. Expect TiCd(AgSe2)2, TiMg(AgSe2)2, TiZn/Mg/Cd(AgTe2)2, TiCd(AgS2)2 and Ti-S analogs to land 1.1-1.7 with ehull<0.05. Also Ti-Si/Ge mixed not available; Ag->Cu not generated.

## [observation] iteration 5 — 2026-10-12 07:33 UTC

Iter 5 (17/20 used). (a) Ti-Ag-Te kesterites: TiZn/TiCd/MgTi(AgTe2)2 ehull 0.048-0.051 but gaps 0.07-0.21 -> no. Ti S/Se analogs were already considered. Chalcopyrite generator fully exhausted. (b) 3d-metal (Mn/Fe/Co/Ni) Ag kesterites: Fe, Co unstable (ehull 0.07-0.11) with erratic gaps; Mn: MnAg2GeS4 0.25 eV/0.021, MnSi(AgS2)2 0.09/0.052. Ni: NiAg2GeS4 2.45/0.033, NiAg2SnS4 1.77/0.034 (just above window), NiAg2GeSe4 0.31/0.031, SiNi(AgS2)2 0.41/0.049, and SiNi(AgSe2)2 gap 1.632 eV, ehull 0.036 -> IN WINDOW and near-stable, novel. Caveat: gaps for Ni compounds vary erratically (2.45 vs 0.31 vs 1.63) suggesting d-state/magnetic-ordering sensitivity in the ML gap predictor; Ni2+ prefers square-planar/octahedral, so tetrahedral kesterite is questionable and needs DFT validation.

## [reflection] iteration 5 — 2026-10-12 07:33 UTC

Campaign end. Qualifying candidates: SiNi(AgSe2)2 (1.63, 0.036; low confidence due to Ni d-states), MgSi(AgTe2)2 (1.63, 0.014; most credible, s-p band edges), MgAg2SnSe4 (1.15, 0.043), plus CuBiTe2 (1.45, 0.052, marginal). Lessons: Ag-kesterite with main-group M/Si/Ge on Mg/Zn is thermodynamically robust; gap tuned by anion (S>Se>Te) and cation s-orbital; transition-metal d-cations (Ti, Fe, Co, Zr) gave unstable or narrow-gap systems. Next steps if continued: validate MgSi(AgTe2)2 with DFT/HSE, phonons, and test Mg/Zn-Si-Te-Se anion mixing for ~1.4 eV.
