# Lab Notebook

## [hypothesis] iteration 1 — 2026-10-12 07:34 UTC

Kesterite family I2-II-IV-VI4: gap tuned by isoelectronic substitution. CZTS ~1.5, CZTSe ~1.0. Ag for Cu widens gap and Cd/Mg for Zn, Ge for Sn, S/Se mixing shifts it. Propose Ag/Cu, Zn/Cd/Mg, Sn/Ge/Si, S/Se combos; target gap 1.1-1.7, e_hull<=0.05. Pick novel ones only.

## [observation] iteration 1 — 2026-10-12 07:34 UTC

20 novel kesterite-type evaluated, all near-stable (ehull<=0.047). Hits in window: MgAg2SnSe4 (gap 1.153, ehull 0.043), MgSi(AgTe2)2 (1.627, ehull 0.014). Near misses: ZnSi(AgTe2)2 1.717 ehull 0.001; MgAg2GeS4 1.78; MgSi(AgSe2)2 1.84 ehull 0.011; ZnSi(AgSe2)2 1.84 ehull 0; ZnAg2GeSe4 0.68 stable. Trends: Cu and Ag-Te/Sn lower gap; Si and S raise it; Ge-S-Ag Mg 1.78. Mg-containing and Ag compounds stable in this model. CdAg2GeSe4 gap ~0 (likely a PBE-like artefact/metallic).

## [reflection] iteration 1 — 2026-10-12 07:34 UTC

Hypothesis partially held: stable family, 2 hits. Next: fine-tune toward 1.4 eV between Ge-S (1.78) and Sn-Se (1.15) endpoints, e.g. Mg/Zn Ag2 (Ge,Sn) mixed anion Se/S not reachable by single-site substitution; try Mg/Zn-Ag2-Sn-S/Se with Ca/Sr/Ba analogs, or Ag2-ZnSnSe/Ge-Se with Mg; also explore Ga/In/Al chalcopyrites with Ag (AgAlTe2, AgGaTe2 variants) and different families (e.g. Cu-Sb-S) to diversify.

## [observation] iteration 2 — 2026-10-12 07:35 UTC

Iter 2: 20 novel kesterite-type evaluated. Only full hit: SrAg2SnS4 (gap 1.667, ehull 0.024) — at the edge of window. CaAg2SnSe4 gap 1.454 but ehull 0.089 (unstable). SrAg2GeS4 1.95/0.017, SrAg2GeSe4 0.15/0.035, SrAg2SnSe4 0.34/0.052. Ca/Sr-Cu kesterites all ehull 0.055-0.12 (too big cations; Cu worse than Ag). Zr-containing Cu2 compounds unstable (0.09-0.2) though gaps in window (MgZr(CuS2)2 1.14, MgZr(CuSe2)2 1.55). Chalcopyrite substitution mostly returns known compounds (only NaGaS2, NaAlS2 novel, not evaluated; budget spent). Trends: Sr stabilizes Ag kesterite best; Se with Sr/Ca gives gap collapse (likely metallic-like artifact).

## [reflection] iteration 2 — 2026-10-12 07:35 UTC

Large A-site (Ca,Sr) Ag kesterites stable-ish; Sr best. Gap too high for S-Sn-Sr (1.67), too low for Se. Next: mixed-site tuning not possible via single substitution, so try Sr/Ba-like with Ag-Sn-S under Zn/Mg mixing isn't available; try new families: zincblende-derived (Cu-Sb/ P/ As ternaries, e.g. Zn-Sn-P2, Cd-Sn-As2 style), Na/K-In/Ga chalcogenides, Cu-Sb-S type. Avoid Cu+Ca/Sr and Zr kesterites (unstable). Hit tally so far: 3 (MgAg2SnSe4, MgSi(AgTe2)2, SrAg2SnS4).

## [hypothesis] iteration 3 — 2026-10-12 07:36 UTC

Iter 3: zincblende prototype only gives binaries (all known) - dead end for novelty. Back to Ag kesterites: (a) Ag-Te with large A (Ca/Ba) and Sn/Ge: Te lowers gap vs S, Sr/Ba stabilise Ag; target ~1.4. (b) Group-4 B-site (Zr/Ti) with Ag instead of Cu (Ag was more stable than Cu with big cations): d0 Zr4+/Ti4+ chalcogenides have gaps in 1-2 eV; Ag may fix hull energies. Evaluate ~16.

## [observation] iteration 3 — 2026-10-12 07:36 UTC

Iter 3: zincblende prototype yields only known binaries (no ternaries) -> unusable. Evaluated 20 novel Ag kesterites. No full hits. Ag-Te Ca/Ba Sn/Ge: ehull 0.059-0.083, gaps 0.05-0.87 (fail). Zr-Ag all unstable (0.088-0.185), gaps mostly <0.4. Ti-Ag family is stable: TiCd(AgS2)2 0.007/2.23; TiZn(AgSe2)2 0.014/1.89; TiCd(AgSe2)2 0.019/0.61; BaTi(AgSe2)2 0.035/2.03; BaTi(AgS2)2 0.049/2.25; MgTi(AgS2)2 0.040/1.79; MgTi(AgSe2)2 gap 1.516 (in window) but ehull 0.053 (just misses). SrTi(AgSe2)2 0.071/2.33. Trend: Ti-Se gaps 0.6 (Cd) -> 1.5 (Mg) -> 1.9 (Zn) so A-site tunes gap.

## [reflection] iteration 3 — 2026-10-12 07:36 UTC

New stable family: Ti(IV)-Ag kesterites. Near hit MgTi(AgSe2)2 (1.52 / 0.053). Cd Ti Se gap 0.61 and Zn 1.89 bracket 1.4; mixed Zn/Cd would hit but single-site substitution can't; try Ti with Te, or Ge/Si sites vs Ti, Mn/Fe/Co/Ni A-site analogs (Mn2+ with Ti Ag Se). Avoid Zr and Ag-Te with Ca/Ba. Hit tally still 3 full hits + 1 near miss.

## [hypothesis] iteration 4 — 2026-10-12 07:37 UTC

Iter 4: Ti(IV)-Ag kesterites A2+Ti(AgX2)2 are stable; Ti-Se gap tunes with A site (Cd 0.61, Mg 1.52, Zn 1.89). Test A = Mn, Fe, Co, Ni, Ca, Sr (d-metal A-site could lower the gap), Ti-Te with Mg/Zn/Cd (Te lowers gap vs Se, expect ~1), Ti->Sn/Ge mixing with Se/S, plus Ti-Cu analogs with Mg/Zn/Cd. Aim: gap 1.1-1.7 with ehull<=0.05.

## [observation] iteration 4 — 2026-10-12 07:37 UTC

Iter 4: 20 novel Ag kesterites evaluated. NEW FULL HIT: SiNi(AgSe2)2 (NiAg2SiSe4) gap 1.632, ehull 0.036. Ti-TM A-site: TiMn(AgSe2)2 0.031/0.11; TiNi(AgSe2)2 gap 1.48 but ehull 0.072; TiMn(AgS2)2 1.39 but ehull 0.092; TiCo(AgSe2)2 1.12/0.127. Fe/Co/Ni Ti-Te metallic and unstable; TiZn(AgTe2)2 0.051/0.065. Ni group-14: NiAg2GeS4 2.45/0.033, NiAg2SnS4 1.77/0.034, NiAg2SnSe4 0.64/0.049, NiAg2GeSe4 0.31/0.031. MnAg2GeS4 0.021/0.25, MnSi(AgS2)2 0.052/0.09 (Mn gaps collapse, likely magnetic/PBE artefact). Te always collapses gap.

## [reflection] iteration 4 — 2026-10-12 07:37 UTC

Ni-Ag-Si-Se hit at 1.63 (upper edge); Ni Sn-S 1.77 slightly above. Ni2+ A-site stabilises Ag kesterites well (ehull 0.03-0.05). Hit tally: 4 full hits (MgAg2SnSe4, MgSi(AgTe2)2, SrAg2SnS4, NiAg2SiSe4). Next (iter 5): Ni/Cu-Ni A-site with Sn-Se/Ge-Se tuning between 0.64 and 1.77, e.g. NiAg2SnSe4 vs S; Ni-Ti? (TiNi(AgSe2)2 1.48/0.072); try Co/Ni with Si-Se/Ge-S; Pd-like absent. Avoid Te, Fe, Zr, Mn-gap collapse.

## [hypothesis] iteration 5 — 2026-10-12 07:38 UTC

Iter 5: exploit Ni2+/Co2+ A-site Ag kesterites (ehull 0.03-0.05, gaps 0.3-2.4). Gap should interpolate between Sn-S (1.77) and Sn-Se (0.64); Ni with Si-Se gave 1.63. Test Co, Ni, Mg, Zn, Cd, Ca, Sr, Ba A-site with Si/Ge/Sn B-site and S/Se, plus Cu analogs of Ni (Cu lowers gap vs Ag). Avoid Te, Fe, Zr, Mn. Choose novel only.

## [observation] iteration 5 — 2026-10-12 07:38 UTC

Iter 5: 18 novel evaluated. Co-Ag kesterites all unstable (0.07-0.10, ehull) -> Co bad. Ni-Cu: Cu2NiGeS4 0.010/0.49, Cu2NiGeSe4 0.023/0.89, Cu2SiNiSe4 0.014/0.24 stable but gaps low. Large alkaline earth Ag-Si-Se: NEW HITS BaSi(AgSe2)2 (BaAg2SiSe4) gap 1.423 ehull 0.026 (ideal gap!), SrSi(AgSe2)2 gap 1.694 ehull 0.021 (edge). BaSi(AgS2)2 0.029/2.57, SrSi(AgS2)2 0.033/2.54, Ca-Si Ag unstable (0.061-0.067). Ba/Cu-Si 0.054-0.06, gaps 1.8/3.1 (fail).

## [reflection] iteration 5 — 2026-10-12 07:38 UTC

Hypothesis held for Ba/Sr Si-Se Ag kesterites: best campaign result is BaAg2SiSe4 (1.42 eV, 0.026 eV/atom). Hit tally: 6 (MgAg2SnSe4, MgSi(AgTe2)2, SrAg2SnS4, NiAg2SiSe4, BaAg2SiSe4, SrAg2SiSe4). Lessons: big cation + small Si B-site with Ag is a sweet spot; Co/Cu large-cation fail. Caveat: kesterite prototype may not be ground-state structure for Ba/Sr (real analogs adopt other structure types), and model gaps are ML estimates — needs DFT/experimental validation.
