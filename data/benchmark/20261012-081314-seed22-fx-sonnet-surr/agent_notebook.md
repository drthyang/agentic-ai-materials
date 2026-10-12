# Lab Notebook

## [hypothesis] iteration 1 — 2026-10-12 08:13 UTC

Kesterite Cu2ZnSnS4 (gap ~1.5) family: isoelectronic substitutions (Ag for Cu, Cd/Mg for Zn, Ge/Si for Sn, Se for S) tune gap around 1.4. Expect Ag2ZnSnSe4, Cu2CdSnSe4, Cu2ZnGeSe4-type mixes in 1.1-1.7 range; many known in MP, so focus on less-explored combos (Ag/Cd/Ge mixes, Mg).

## [reflection] iteration 1 — 2026-10-12 08:14 UTC

20 novel kesterite-type evaluated. Only hit: MgAg2SnSe4 (gap 1.153, Ehull 0.043) - marginal. Near misses: MgAg2GeS4 (1.78, 0.006), MgSi(AgSe2)2 (1.84, 0.011), ZnSi(AgSe2)2 (1.84, 0.0). Trends: Se Ag-Ge/Sn gaps too low (CHGNet/HSE-ish; Cd lowers gap heavily); Te too low; Ca destabilizes (Ehull>0.06). Mg-Ag-Ge-S gap 1.78 and Mg-Ag-Sn-Se 1.15 bracket window -> try Mg-Ag-Sn-S analogs w/ mixed anion or Ge/Sn mixing, Zn-Ag-Sn-Se, Ag-Zn-Ge-S-Se. Next: other prototypes (chalcopyrite AgInS2-type, Ag/Cu-Ga/In ternaries, Sb/Bi chalcogenides) and Zn/Mg-Ag-Ge/Sn with partial substitution for gap interpolation.

## [hypothesis] iteration 2 — 2026-10-12 08:14 UTC

Iter 2: chalcopyrite family I-III-VI2 with mixed cation/anion (Ag/Cu, Ga/In/Al, S/Se) plus zincblende-derived ternaries (II-IV-V2 e.g. ZnSnP2, ZnGeP2, CdSnAs2 variants, Mg/Zn-Si/Ge/Sn-P/As). Gap interpolation: CuGaSe2 1.7, AgInSe2 1.2, CuInS2 1.5, AgGaSe2 1.8; mixed Ag/Cu with Ga/In and S/Se should land 1.1-1.7. Prioritize novel mixed compositions (ordered 8-atom cells would be quaternary-like). Also try II-IV-V2 pnictides.

## [reflection] iteration 2 — 2026-10-12 08:15 UTC

Iter 2: Chalcopyrite/zincblende ternaries almost all known in MP; novel II-IV-Sb2 pnictides (ZnSiSb2, ZnGeSb2, CdXSb2, MgXSb2) all have gaps <0.95 eV (CHGNet-HSE) and several unstable -> falsified. NaGaS2/NaAlS2 stable but gap >4. Hits from large-A-site kesterite-like family: BaSi(AgSe2)2 (gap 1.424, Ehull 0.026) and SrSi(AgSe2)2 (1.694, 0.021) - both novel, in window. Fe and Mn at divalent site give tiny gaps/unstable; Sr/Ba stabilize with Ag-Si/Ge. Trend: Ba/Sr-Ag-Si-Se gaps 1.4-1.7; S analogs 2.5. Next: Ba/Sr-Ag-Ge/Sn mixes w/ Se (BaAg2GeSe4 known), Ba/Sr Cu-Si/Ge-Se, Ba-Ag-Si-Se/Te, Sr/Ba-Zn-Si-Se with Cu; try mixed Ba-Sr analogs.

## [hypothesis] iteration 3 — 2026-10-12 08:15 UTC

Iter 3: Extend the Ba/Sr-Ag-Si-Se hits (BaSi(AgSe2)2 1.42, SrSi(AgSe2)2 1.69). Substitute Ge/Sn for Si, Cu for Ag, Ca/Mg/Ba/Sr mixes, S/Se anion mixing, on kesterite prototype. Expect Ge to lower gap slightly (SrGe(AgSe2)2 ~1.4-1.5), Cu raises/lowers stability. Chemistry: large A2+ cations stabilize the Ag-tetrahedral framework; the gap is set by Ag-d/Se-p VBM and Si/Ge s CBM.

## [observation] iteration 3 — 2026-10-12 08:16 UTC

Iter3 (20 evals). Only hit: SrAg2SnS4 (gap 1.667, Ehull 0.024) - novel, edge of window. Sr/Ba Cu/Ag-Si/Sn selenides: Ehull 0.05-0.08, gaps either <0.35 (Sn) or ~1.7-1.8 (Si, Cu). Ba/Sr Ag tellurides unstable (0.06-0.07). ZnSi(AgTe2)2 stable (0.001) gap 1.72; ZnAg2GeTe4 0.01/0.63. MgCu2GeTe4 0.017/0.52. Ti-Zn/Cd-Ag-S/Se: stable (0.007-0.022) but gaps 1.9-2.2. Zr analogs: gaps in window for ZrZn(AgS2)2 (1.22) & ZrZn(AgSe2)2 (1.33) but Ehull 0.08-0.11 -> unstable.

## [reflection] iteration 3 — 2026-10-12 08:16 UTC

Large-A Sn sulfide idea worked once (SrAg2SnS4). Ba/Sr selenide extension mostly failed on stability or gap. Gap/stability tradeoff: Sn lowers gap strongly, Si/Ti raise; intermediate (Ge, or Ti/Sn mix) may land at 1.4. Next iter: Ba/Sr/Ca-Ag-Ge-Se/S-Se mixed anion not accessible by tool; try Ca/Sr with Ag-Sn-S variants (Cu-Ag), Ti-Cd with Se (TiCd(AgSe2)2 untested, expect ~1.9), Ge-Sn cation mixing, and other prototypes (zincblende-derived nitrides/phosphides e.g. Zn-Ge-N, Cu3PS4-like). Also explore Zr-Zn compounds with stabilizing Sr/Ba.

## [hypothesis] iteration 4 — 2026-10-12 08:17 UTC

Iter 4: Explore around SrAg2SnS4 (1.667, 0.024). Sn-S lowers gap vs Ge-S/Si-S; try Ba/Ca/Mg/Zn/Cd at A site with Ag2SnS4, Ag2(Ge,Sn)S4 with Sr/Ba, Cu variants, and Zr/Ti-Sn mixed. Expect BaAg2SnS4 ~1.5-1.6 (larger A lowers gap slightly), Cd/Zn analogs ~1.2-1.4 (Cd lowers gap), Sr/Ba-Ag2Ge S4 ~2. Also Ag->Cu.

## [observation] iteration 4 — 2026-10-12 08:18 UTC

Iter4 (20 evals): kesterite-prototype I3-V-VI4 family (Cu/Ag/Na with Sb/As/P) – very productive; many stable. HITS (novel, gap in window, Ehull<=0.05): CuAg2PSe4 (1.49, 0.000) [best, near 1.4], Ag3SbSe4 (1.255, 0.000), CuAg2AsS4 (1.56, 0.012), Cu2AgAsS4 (1.63, 0.010), NaCu2SbS4 (1.22, 0.046). Misses: Cu2AgPSe4 1.93/0.0; CuAg2PS4 2.42; Cu2AgSbS4 0.47; Ag3SbS4 0.15 (odd vs Ag3SbSe4 1.26 - CHGNet-gap noise, structure-dependent); As/Sb selenides gap ~0.04-0.85 (metallic-ish); Na-Cu-P/As/Sb gaps range 0.4-3.2, Ehull 0.02-0.05; Cu3MoS4 unstable (0.144). Earlier planned A-site kesterite expansions were mostly already tested.

## [reflection] iteration 4 — 2026-10-12 08:18 UTC

Iter4: Moving from II-IV (A2+B4+) to I3-V (famatinite-like) compositions gave 5 hits, best CuAg2PSe4. Gap trend: P > As > Sb, S > Se, Ag raises gap relative to Cu for Se-P. Next (iter 5, last): refine around hits—Ag/Cu ratio variants with mixed pnictogen not possible via tool but try Na/K/Ag3-PSe4, Ag3AsS4, Ag3PSe4, Ag3AsSe4, Cu2AgPSe4 neighbors, Na-Ag-Sb-S, K analogs; check Ag3PSe4/Ag3AsS4 gaps (expect 1.4-1.7). Caveat: gaps from CHGNet-HSE surrogate noisy (Ag3SbS4 vs Ag3SbSe4 inversion); treat with caution.

## [hypothesis] iteration 5 — 2026-10-12 08:18 UTC

Iter 5: Refine the I3-V-VI4 hits. Substitute on kesterite prototype: Ag3PSe4, Ag3AsS4, Ag3AsSe4, Ag3PS4, K/Na-Ag mixes with P/As/Sb, Cu-Ag mixed with As/P/Sb Se/S. Expect gaps 1.2-1.7 for P/As sulfoselenides with Ag-rich; use surrogate to prioritize novel ones.

## [observation] iteration 5 — 2026-10-12 08:19 UTC

Iter5 (19 evals, all novel). HITS (gap in window, Ehull<=0.05): NaAg2AsSe4 (1.451, 0.004) [best, closest to 1.4], KAg2AsSe4 (1.557, 0.014), NaAg2AsS4 (1.65, 0.007). Misses: NaAg2PSe4 2.13/0.001; NaAg2PS4 3.0; Sb analogs 0.64-0.88; Ag3AsSe4 0.21; KAg2PSe4 2.29/0.027; KAg2AsS4 1.91/0.03. K-Cu analogs mostly unstable (0.035-0.10) or off-gap; KCu2SbS4 1.445 but Ehull 0.069, KCu2BiSe4 1.25/0.079 unstable.

## [reflection] iteration 5 — 2026-10-12 08:19 UTC

Iter5: Alkali-Ag2-As-chalcogenide extension of the I3-V-VI4 family worked: 3 new hits, with As giving window gaps (P too wide, Sb too narrow); Se/S shifts gap by ~0.2. Ag-based alkali compounds are stable; Cu-based K compounds are not (size mismatch). Campaign totals of hits: CuAg2PSe4 1.49, NaAg2AsSe4 1.45, BaSi(AgSe2)2 1.42 best near 1.4. Gaps are CHGNet-HSE surrogate, noisy; DFT verification and synthesis recommended. Future: Rb/Cs-Ag-As-Se, Na/K-Ag-As/P mixed anions, Li not in palette.
