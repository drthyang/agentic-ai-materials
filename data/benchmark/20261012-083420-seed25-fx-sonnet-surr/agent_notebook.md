# Lab Notebook

## [hypothesis] iteration 1 — 2026-10-12 08:34 UTC

Kesterite family: substituting Zn->Cd/Mg, Sn->Ge/Si, S->Se, Cu->Ag gives isoelectronic quaternaries with gaps tunable around 1.4 eV. Ag/Cd/Se variants lower gap from CZTS 1.5; Ge raises it. Propose wide family, filter for novel, evaluate ones likely in 1.1-1.7.

## [observation] iteration 1 — 2026-10-12 08:35 UTC

17 evaluated, all near-stable (ehull<=0.043). Hits in window: MgSi(AgTe2)2 (1.63 eV, ehull 0.014), MgAg2SnSe4 (1.15 eV, ehull 0.043). Near misses: MgAg2GeS4 1.78 (0.006), MgSi(AgSe2)2 1.84, ZnSi(AgSe2)2 1.84 (hull 0). Cu-Mg-Ge/Si-Se/Te and Cd-Ag-Ge-Se/Te gaps too low (<0.9). Many Cu analogues are already in MP. Gap trend noisy but Mg raises gap, Sn/Se/Te lower it.

## [reflection] iteration 1 — 2026-10-12 08:35 UTC

Hypothesis partly held: kesterite isoelectronic space is highly stable, gap tuned by chalcogen/group-IV/divalent site. Next: mixed-anion (S/Se) or mixed Ge/Sn on Mg-Ag to hit ~1.4 (between MgAg2SnSe4 1.15 and MgAg2GeS4 1.78), e.g. MgAg2SnSe2S2, MgAg2Ge0.5Sn0.5S4; also try Zn-Ag-Sn-Se-type with Ba/Sr via other prototypes. Note the prototype tool lacks anion-ordering; try chalcopyrite with Ag/Ga/Te, or Cu-Sb-S ternaries.

## [hypothesis] iteration 2 — 2026-10-12 08:35 UTC

Iter 2: Interpolate between MgAg2SnSe4 (1.15) and MgAg2GeS4 (1.78): Ag2-(Mg,Zn,Cd)-(Sn,Ge)-(S,Se) kesterites, e.g. MgAg2SnS4, ZnAg2SnS4, CdAg2SnS4, MgAg2GeSe4, ZnAg2GeSe4, Ba/Sr variants; also chalcopyrite AgGaS2/AgInS2-type with Ag/Ga/In/Te. Expect Sn-S and Ge-Se Ag compounds ~1.3-1.6.

## [observation] iteration 2 — 2026-10-12 08:36 UTC

Iter 2: 20 evaluated, all novel. Only hit: SrAg2SnS4 (gap 1.667, ehull 0.024) — marginal at top of window. Near-stable but off-window: SrAg2GeS4 (1.95, 0.017), SrAg2GeSe4 (0.15, 0.035; gap collapse suspicious, likely CHGNet/ML artefact on distorted geometry). In-window but unstable: CaAg2SnSe4 (1.45, 0.089), SrZr/BaZr(CuS2)2 (1.1-1.2, hull 0.18), CaZr(CuSe2)2 (1.31, 0.24). Ca/Cu-AE-Si/Ge/Sn-S: gaps 2.2-3.3 and hull 0.06-0.09 (unstable; kesterite is wrong structure for large AE). Gaps for Ca/Sr Se compounds near 0.1-0.3 are erratic. Chalcopyrite ternaries all known in MP (skipped).

## [reflection] iteration 2 — 2026-10-12 08:36 UTC

Large alkaline earths destabilise the kesterite prototype except Sr with Ag (larger Ag-S lattice tolerates Sr). Sr-Ag-Sn-S best. Next: Sr/Ba-Ag-Sn-S neighbours in different structures; mixed Sn/Ge on Sr-Ag (SrAg2Sn0.5Ge0.5S4) to bring gap from 1.67 toward 1.4 is not reachable via this tool; alternatives: Sr-Ag-Sn-S with Se partial, or explore zincblende-derived ternaries (Cu/Ag-Sb/Bi-chalcogenides, Zn-Sn-P2, Cu3PS4-like) and different prototypes. Avoid Ca, Cu-AE kesterites, Zr/Ti.

## [observation] iteration 3 — 2026-10-12 08:38 UTC

Iter 3: zincblende prototype gives only binaries (useless); chalcopyrite pnictide route mostly filtered by SMACT (Sn2+ chalcogenides only). Evaluated 20 novel: NO candidate satisfies both gap window and ehull<=0.05. In-window but unstable: TiMn(AgS2)2 (1.39, hull 0.092), ZnSnTe2 (1.35, 0.076), SrZr(AgS2)2 (1.61, 0.149). Near-stable off-window: TiCd(AgS2)2 (2.23, 0.007), BaTi(AgSe2)2 (2.03, 0.035), BaTi(AgS2)2 (2.25, 0.049), TiCd(AgSe2)2 (0.61, 0.019), MnAg2GeS4 (0.25, 0.021; Mn gap likely artefact), CdAg2SnTe4/TiCd(AgTe2)2 (gap ~0). Ti4+ Ag kesterites: S gives 2.2, Se 0.6-2.0; Ba/Sr-Ti-Ag-S/Se stable-ish with big gaps. Zr always unstable/low gap. Telluride gaps collapse.

## [reflection] iteration 3 — 2026-10-12 08:38 UTC

Iter 3 produced no new hits; best campaign hit remains SrAg2SnS4 (1.67, 0.024), MgSi(AgTe2)2 (1.63, 0.014), MgAg2SnSe4 (1.15, 0.043). Ti-based Ag kesterites are stable but gap overshoots (S) or undershoots (Se, Cd); a Ba/Sr-Ti-Ag mixed S/Se would sit ~1.4 but the tool lacks anion mixing. Next iters: avoid Zr, Te-Ag-Ti, zincblende binaries, SMACT-failing pnictides; try chalcopyrite with Ag-In/Ga-Se/Te + Sn/Ge mixing not available... explore Cu/Ag-Sb/Bi chalcogenide variants or Mg/Sr-Ag-Sn-Se and Cd-Ti-Cu(Se,S) (Cu analogues of TiCd(AgSe2)2 may land 1.0-1.4), and Mg-Ti-Ag. Note MP-novelty wasn't a problem; the bottleneck is gap landing in window with stability.

## [hypothesis] iteration 4 — 2026-10-12 08:38 UTC

Iter 4: Literature unhelpful. Hypothesis: Cu analogues of stable Ti/Ba/Sr-Ag kesterites (Cu has higher VBM -> lower gap than Ag), e.g. Ba/Sr/Cd/Zn/Mg-Ti-Cu-S/Se, and Sr/Ba-Ag-Sn-Se, Mg/Zn-Ti-Ag-Se, should land 1.1-1.7 eV (Ag-S 2.2 -> Cu-S ~1.5; Ag Se 0.6-2.0). Also Sn->Si/Ge mix with Sr-Ag-S/Se. Avoid Zr, Ca, Te.

## [observation] iteration 4 — 2026-10-12 08:39 UTC

Iter 4: 17 evaluated, all novel. HITS: BaSi(AgSe2)2 (gap 1.423, ehull 0.026) — best campaign hit, gap right at ideal; SrSi(AgSe2)2 (1.694, 0.021, marginal). Near: MgTi(AgSe2)2 (1.52, hull 0.053 just over). Misses: Cu-Ti kesterites gap 2.1-2.9 (hull 0.05-0.08; Cu did NOT lower gap as expected—Ti d-conduction band sets gap), MgCu2SnS4/Se4 stable but gap 0.2-0.5, TiZn(AgSe2)2 1.89 (0.014), TiZn(AgS2)2 2.05, MgTi(AgS2)2 1.79 (0.04), BaSi(AgS2)2 2.57, SrSi(AgS2)2 2.54, CaSi(AgSe2)2 2.18 (hull 0.061), MnSi(AgS2)2 0.09 (unstable).

## [reflection] iteration 4 — 2026-10-12 08:39 UTC

Large-AE (Ba>Sr>Ca) + Si + Ag + Se kesterite-like gives gap decreasing with AE size (2.18 Ca, 1.69 Sr, 1.42 Ba), stable for Sr/Ba. Cu analogues don't help. Best candidates: BaSi(AgSe2)2, SrSi(AgSe2)2, SrAg2SnS4, MgSi(AgTe2)2. Next (iter 5): verify/refine; possibly Ba-Ge/Sn-Ag-S analogues with different structure; Ba/Sr-Si-Ag-Se Na/K doping not possible. Caveat: CHGNet geometry for large AE in kesterite prototype may be unreliable (real structures are likely different, e.g. I-42m Ba2... ), so DFT confirmation needed.

## [hypothesis] iteration 5 — 2026-10-12 08:39 UTC

Iter 5: Refine around BaSi(AgSe2)2 (1.42, 0.026). Vary group-IV (Ge, Sn, Si) and AE (Ba, Sr, Mg, Zn) with Ag + S/Se; Ge/Sn lower the CBM relative to Si so BaGe/BaSn(AgSe2)2 may be ~1.0-1.4; SrGe(AgSe2)2, BaGe(AgS2)2, SrSn(AgS2)2 fill in. Also Ba/Sr Ag Sn S (SrAg2SnS4 1.67 -> Ba analogue lower). Skip Zr, Ca, Te, Cu-Ti.

## [observation] iteration 5 — 2026-10-12 08:40 UTC

Iter 5: Ba/Sr-Ag-(Si,Ge,Sn)-(S,Se) family fully explored already (all rejected as considered). Evaluated 14 novel: alkali (Na/K)-Al/Ga chalcopyrite-type are stable (hull 0-0.006) but gap 3.1-4.2 (wide gap, not PV). KSbTe2/KBiTe2 gap 0.36/0.56, hull ~0.05. Co/Ni/Ti Cu kesterites: Cu2NiGeS4 (0.49, 0.010), Cu2SiNiSe4 (0.24, 0.014) too low gap; TiCo(CuSe2)2 1.57 but hull 0.129. No new hits. Left 6 relaxations unspent: no remaining unexplored novel candidates with credible chemistry.

## [reflection] iteration 5 — 2026-10-12 08:40 UTC

Campaign conclusion: best leads are BaSi(AgSe2)2 (1.42 eV, hull 0.026; ideal gap), SrSi(AgSe2)2 (1.69, 0.021), SrAg2SnS4 (1.67, 0.024), MgSi(AgTe2)2 (1.63, 0.014), MgAg2SnSe4 (1.15, 0.043). Caveats: CHGNet geometry for large AE in the kesterite prototype is likely not the true ground-state structure; DFT/HSE and phonon checks and alternative structure types (e.g. Ba-Ag-Si-Se known as BaAg2GeS4-type I-42m/orthorhombic) are needed. Tool limitation: no anion/cation mixing, so interpolation (e.g. Ba/Sr mix, S/Se mix) wasn't testable. Divalent TM (Co, Ni, Fe, Mn) kesterites give too-low gaps; alkali-III-VI too wide; Sb/Bi tellurides too low.
