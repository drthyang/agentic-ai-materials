# Lab Notebook

## [hypothesis] iteration 1 — 2026-10-12 07:47 UTC

Kesterite family: quaternary I2-II-IV-VI4 with Ag/Cu, Zn/Cd/Mg, Sn/Ge/Si, S/Se. Isoelectronic substitution keeps charge balance; Se and Cd lower gap from CZTS 1.5 toward ~1.0-1.4; Ag raises gap. Expect Cu2CdSnS4, Ag2ZnSnS4, Cu2ZnGeSe4 etc. mostly known; focus on novel ones (Ag/Mg/Ge/Si mixes, Te).

## [observation] iteration 1 — 2026-10-12 07:49 UTC

16 novel kesterite-type evaluated, all near-stable (Ehull 0-0.034). Gaps (eV): CdAg2GeSe4 0.03; CdAg2GeTe4 0.17; CdSiAg2Se4 0.75; CdSiAg2Te4 0.33; MgAg2GeSe4 0.28; MgAg2GeTe4 0.87; MgSiAg2Se4 1.84; MgSiAg2Te4 1.63 (HIT, Ehull 0.014); MgCu2GeSe4 0.31; ZnAg2GeSe4 0.68; MgCu2GeTe4 0.52; MgCu2SiTe4 0.25; MgCu2SnTe4 0.35; MgSiAg2S4 2.46 (Ehull 0.012); MgAg2GeS4 1.78 (0.006); CdSiAg2S4 2.22. Trends: gap rises Te<Se<S, Cd<Mg, Sn<Ge<Si; Ag > Cu. Only one hit; 4 relaxations unused because the filtered pool had no more novel members.

## [reflection] iteration 1 — 2026-10-12 07:49 UTC

Hypothesis partly held: Mg/Si/Ag substitutions open gaps predictably, and the family is thermodynamically stable. Gaps are DFT-level so likely underestimated for the narrow ones. Next: interpolate between MgAg2GeS4 (1.78) and MgAg2GeSe4 (0.28) / mixed-anion or mixed cation (Mg/Zn, Ge/Sn, Si/Ge) near 1.4; ZnAg2GeS4-type and Zn/Mg Ag Sn variants; also try chalcopyrite prototype (AgGaTe2-like, Cu/Ag-Al/Ga/In with Te) and other families. Note propose_candidates substitutes all-at-once so lists should include the parent element to retain mixtures.

## [observation] iteration 2 — 2026-10-12 07:50 UTC

Iter 2. Chalcopyrite family: all 17 members known in MP (no novel). Kesterite Sn/Si/Mg leftovers: ZnSiAg2Se4 1.84 (Ehull 0); MgAg2SnS4 0.69 (0.011); MgAg2SnSe4 1.153 (Ehull 0.043) HIT borderline; MgCu2SnS4 0.49; MgCu2SnSe4 0.19. Zr/Ti kesterite (15 evaluated): many gaps in 1.1-1.7 window (ZnZr(CuS2)2 1.12, ZnZr(CuSe2)2 1.63, ZnZr(AgSe2)2 1.33, MgZr(CuS2)2 1.14, ZrCd(CuSe2)2 1.27) but all Ehull 0.065-0.24 -> unstable as kesterite (Zr prefers octahedral). TiZn(AgSe2)2 Ehull 0.014 but gap 1.89. Zincblende binaries proposed were known/nonsense (CuSb, AgSb); not evaluated.

## [reflection] iteration 2 — 2026-10-12 07:50 UTC

One borderline hit (MgAg2SnSe4, 1.15 eV, 0.043). Zr kesterites have right gaps but wrong stability (tetrahedral Zr disfavored) — falsified as stable absorbers. Ti-Ag-Se is stable but gap too wide; Ti/Sn mixed or Ti-Ag-Te might land ~1.4 (TiZn(AgTe2)2, TiCd(AgSe2)2 untested). Next: Ti analogs with Cd/Te/Ag (TiCd(AgSe2)2, TiMg(AgSe2)2, Ti Te variants), and Sn/Ge Ag-Zn-Se combinations; avoid chalcopyrite (all known). Propose_candidates cannot make mixed-site compounds, so interpolation must be through discrete members.

## [hypothesis] iteration 3 — 2026-10-12 07:50 UTC

Iter 3. Te Ag-Sn/Ti kesterites gave gaps 0.03-0.44 (too small, stable Ehull 0.014-0.05): Te route falsified for gap. Now test alkaline-earth (Ca, Sr, Ba) and Mn on the Zn site with Se anions and Ge/Si/Sn; Ca2+ more ionic, raises gap vs Zn/Cd (Mg trend: Cd<Mg), expect gaps ~1-1.7 in Cu selenides. Risk: large cation size destabilizes tetrahedral kesterite (Ehull). Evaluate the Se members only.

## [observation] iteration 3 — 2026-10-12 07:51 UTC

Iter 3 (20 relaxations, all novel). Te Ag kesterites: TiCd(AgTe2)2 0.09/0.048; MgTi(AgTe2)2 0.21/0.048; TiZn(AgTe2)2 0.07/0.051; CdAg2SnTe4 0.03/0.015; MgAg2SnTe4 0.19/0.014; ZnAg2SnTe4 0.44/0.019 -> all gaps too small. Alkaline-earth kesterite selenides (gap/Ehull): CaCu2GeSe4 0.30/0.11; CaCu2SiSe4 2.15/0.091; CaCu2SnSe4 0.21/0.117; SrCu2SiSe4 1.74/0.055; SrCu2SnSe4 0.11/0.083; CaAg2GeSe4 0.26/0.068; CaAg2SnSe4 1.45/0.089 (gap hit, unstable); SrAg2SnSe4 0.34/0.052; CaSi(AgSe2)2 2.18/0.061; MnCu2GeSe4 0.66/0.000; BaCu2SiSe4 1.81/0.054; SrAg2GeSe4 0.15/0.035. HITS: BaSi(AgSe2)2 (BaAg2SiSe4) gap 1.423 eV, Ehull 0.026; SrSi(AgSe2)2 gap 1.694, Ehull 0.021.

## [reflection] iteration 3 — 2026-10-12 07:51 UTC

Large alkaline-earth cations destabilize kesterite for Cu and Ca, but Sr/Ba with Ag and Si are near-stable and gap tunes down with cation size (Ca 2.18 > Sr 1.69 > Ba 1.42). Best result: BaAg2SiSe4 (1.42, 0.026). Caveats: kesterite may not be the ground-state structure for Ba (real BaAg2SiSe4-type compounds likely adopt other structures), gap is DFT-level. Next: Ba/Sr with Ag and Si/Ge S/Se mixtures (BaAg2SiS4, BaAg2GeS4, SrAg2SiS4), Ba Cu Si S; avoid Te and Ca, avoid Cu+Sn (small gaps). Mn-Cu-Ge-Se is stable but gap 0.66.

## [hypothesis] iteration 4 — 2026-10-12 07:51 UTC

Iter 4. Follow iter-3 lead: Ba/Sr + Ag/Cu + Si/Ge/Sn + S/Se kesterites. Expect BaAg2GeSe4-like gap small, sulfides wider (BaAg2GeS4 maybe ~1.5-1.8; BaAg2SnS4 ~1.2-1.4), BaCu2Si/Ge S4 ~1.5-2. Also Ba/Sr mixed with Zn/Cd? Keep Ba/Sr on divalent site, vary Group IV and anion. Evaluate novel only.

## [observation] iteration 4 — 2026-10-12 07:52 UTC

Iter 4 (20 relaxations, all novel). Ba/Sr sulfides (gap/Ehull): BaSi(AgS2)2 2.57/0.029; BaCu2SiS4 3.13/0.060; SrSi(AgS2)2 2.54/0.033; SrAg2GeS4 1.95/0.017; SrAg2SnS4 1.667/0.024 (HIT, window edge); SrCu2SiS4 3.17/0.058. Ca/TM Ag sulfides/selenides: CaAg2SnS4 0.52/0.063; CaAg2GeS4 1.75/0.060; CaSi(AgS2)2 2.27/0.067; MnAg2GeS4 0.25/0.021; MnSi(AgS2)2 0.09/0.052; FeAg2GeS4 0.29/0.106; FeAg2SnSe4 0.06/0.095; CoAg2SnS4 0.48/0.069; CoAg2GeS4 0.60/0.078; NiAg2SnS4 1.77/0.034; FeAg2GeSe4 0.15/0.075; CoAg2SnSe4 0.23/0.074; NiAg2SnSe4 0.64/0.049; NiAg2GeSe4 0.31/0.031. Only one hit: SrAg2SnS4. Open-shell Fe/Co/Mn gaps are spurious (small, metallic-like), Ca unstable.

## [reflection] iteration 4 — 2026-10-12 07:52 UTC

Hypothesis partly held: Sr/Ba-Ag kesterites remain near-stable and sulfides with Sn land at upper edge (SrAg2SnS4 1.67). Candidate pool so far: BaAg2SiSe4 (1.42, 0.026) best, SrAg2SnS4, SrAg2SiSe4, MgAg2SnSe4. TM (Fe/Co/Mn) and Ca routes falsified. Next (iter 5): kesterite space is nearly exhausted; maybe try zincblende-derived Zn/Cd/Ga/Al/N/P/As ternaries or Sr/Ba with Zn/Cd mixes; or just consolidate. Caveat: kesterite may not be ground state for Ba/Sr (Ehull relative to hull so OK but structure unverified).

## [hypothesis] iteration 5 — 2026-10-12 07:53 UTC

Iter 5. Cu/Ag-based Ba/Sr kesterite space is exhausted (all 'already considered'). Zincblende binaries all known. New family: alkali (Na/K) on monovalent site of kesterite: ionic, s-orbital-like VBM from Se p only (no Cu/Ag d), so gaps larger than Cu/Ag analogs; Sn selenides (low-lying Sn 5s CBM) expected to lie 1.1-1.8 eV. Risk: kesterite not ground state for Na/K (Ehull). Evaluate Sn/Ge selenides and a few sulfides.

## [observation] iteration 5 — 2026-10-12 07:54 UTC

Iter 5: 20 alkali (Na/K) kesterites evaluated, all novel. Gaps 2.17-3.44 eV, none in window. Many near-stable (Na2CdSiSe4 0.007, Na2CdGeSe4 0.010, Na2CdSnSe4 0.011, Na2ZnSiSe4 0.020, Na2ZnSnS4 0.025; K and Ba/Sr variants 0.05-0.074). Lowest gaps: K2BaSnSe4 2.17, K2MgSnSe4 2.19, K2ZnSnSe4 2.22 — still too wide.

## [reflection] iteration 5 — 2026-10-12 07:54 UTC

Hypothesis falsified for gap: removing Cu/Ag d states pushes gaps to 2.2-3.4 eV (too wide), though stability is good for Na. Overall campaign: best candidates BaAg2SiSe4 (1.42, Ehull 0.026), SrAg2SnS4 (1.67, 0.024), SrAg2SiSe4 (1.69, 0.021), MgAg2SnSe4 (1.15, 0.043), MgSiAg2Te4 (1.63, 0.014). Future: mixed Na/Ag or Na/Cu site (not supported by prototype tool), alloying alkali with Ag to interpolate between 0.3-1.8 (Ag) and 2.5+ (Na); structure ground state for Ba/Sr unverified; HSE-fidelity gaps still DFT-model-based.
