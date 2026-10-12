# Lab Notebook

## [hypothesis] iteration 1 — 2026-10-12 08:20 UTC

Kesterite family: Cu2ZnSnS4 gap ~1.5. Substituting Ag for Cu, Cd/Mg for Zn, Ge/Si for Sn, Se/S mixing tunes gap near 1.4 via isoelectronic substitution. Ag2ZnSnS4 (~2.0), Cu2CdSnS4 (~1.4), Cu2ZnGeSe4 (~1.3-1.5), Ag2CdSnSe4 etc. Propose broad family, evaluate novel ones.

## [observation] iteration 1 — 2026-10-12 08:21 UTC

Evaluated 20 novel kesterite-type quaternaries. All near-stable (ehull 0-0.047). Only hit in window: MgAg2SnSe4 (gap 1.15, ehull 0.043, marginal). Gaps: Te compounds 0.03-0.6 (too low); Cu-Mg-Se/S 0.2-0.5 (CHGNet-HSE gaps low for Cu); Ag-Si-Se: Zn 1.84, Mg 1.84, Cd 0.75 (Cd lowers gap oddly); Ag-Ge-S Mg 1.78; Ag-Si-S 2.2-2.5. Zn-Ag-Ge-Se 0.68. Trends: S>Se>Te gap; Si/Ge raise gap; Ag raises over Cu; Cd lowers.

## [reflection] iteration 1 — 2026-10-12 08:21 UTC

Hypothesis partly held: stability easy, gap tuning needs targeting. Next: interpolate between 1.84 (Ag-Si/Ge-Se with Zn/Mg) and 0.68 (ZnAg2GeSe4): mixed Se/S or Ag2ZnSnSe4-like; MgAg2SnSe4 (1.15, ehull 0.043) is the lead — try Sn/Ge mixed, Mg->Zn alloy, or S-Se mixing e.g. MgAg2SnS... also Ag2ZnSnS4 (known?). Also try other prototypes (chalcopyrite Ag-Ga-Se / Cu-Al-Te, zincblende-derived) since Te chalcopyrites like AgInTe2/CuGaTe2 ~1.2-1.4. Avoid Cd-containing and Cu-Mg selenides.

## [hypothesis] iteration 2 — 2026-10-12 08:21 UTC

Iteration 2: (a) Kesterite Ag2-M-(Sn/Ge)-(S/Se) with mixed anions/cations to interpolate between 1.84 and 0.68 eV gaps around MgAg2SnSe4 (1.15): Zn/Mg x Sn/Ge x Se, S with Ag. (b) Chalcopyrite Ag/Cu-Ga/Al/In-Se/Te: AgGaTe2 (~1.3), CuAlTe2, AgAlTe2, AgInSe2 (1.2), mixed anions. Isoelectronic substitution, larger Ag lowers ionic bonding; Te lowers gap vs Se. Pick novel members only.

## [observation] iteration 2 — 2026-10-12 08:21 UTC

Iter 2: evaluated 20 novel compounds (chalcopyrite II-IV-V2 and I-III-VI2 were nearly all known in MP -> only NaGaS2 evaluated: gap 4.2, ehull 0, useless). BEST HIT: SrAg2SnS4 gap 1.667, ehull 0.024 (in window, near-stable) - a Sr-based kesterite-type (likely actually a different structure in reality, e.g. Ba/Sr-Ag-Sn-S family). Other near-stable: TiZn(AgSe2)2 gap 1.89, eh 0.014; TiZn(AgS2)2 2.05, eh 0.022; TiZn(CuSe2)2 3.05; TiMn(AgSe2)2 0.11. In-window but unstable (eh>0.05): ZrZn(AgS2)2 1.22/0.106, ZrZn(CuS2)2 1.12/0.065, ZrZn(CuSe2)2 1.63/0.098, ZrZn(AgSe2)2 1.33/0.08, TiMn(AgS2)2 1.39/0.092, MgTi(AgSe2)2 1.52/0.053 (marginal), CaAg2SnSe4 1.45/0.089. Trends: Zr lowers gap vs Ti by ~0.7 but destabilizes; Ti-Zn-Ag compounds are stable but gap ~1.9-2.0; Sr stabilizes Ag-Sn-S kesterite-type vs Ca; Mn lowers gap strongly.

## [reflection] iteration 2 — 2026-10-12 08:21 UTC

Hypothesis (d0 group-4 cations lower gap) partly held: gaps hit window but stability lost for Zr. Success: SrAg2SnS4. Next: explore Sr/Ba-Ag-(Sn,Ge)-(S,Se) family and mixed S/Se (SrAg2SnSe4 was 'bad' at -3.3 utility so likely unstable; try Ba, Sr with Sn-S, and Sr-Cu analogs), Ti/Zr mixed (Ti0.5Zr0.5) to balance stability and gap, MgTi(AgSe2)2 variants. Avoid chalcopyrite prototypes (all known). Check with literature whether SrAg2SnS4 is known experimentally.

## [hypothesis] iteration 3 — 2026-10-12 08:22 UTC

Iteration 3: Expand Sr/Ba/Ca-Ag/Cu-(Sn,Ge,Si)-(S,Se) kesterite-type family around SrAg2SnS4 (1.67, eh 0.024). Larger alkaline-earth A-site stabilizes Ag-Sn-S; Se substitution lowers gap toward 1.4; Ba larger than Sr; Ge variants raise gap. Also mixed Ti/Zr and Mg-Ti(AgSe2)2 variants. Literature search gave nothing specific, so novelty judged by MP only.

## [observation] iteration 3 — 2026-10-12 08:22 UTC

Iter 3: evaluated 20 novel A-site alkaline-earth kesterite-type compounds. HITS: BaSi(AgSe2)2 (BaAg2SiSe4) gap 1.423, ehull 0.026 -> near ideal and near-stable, best of campaign. SrSi(AgSe2)2 gap 1.694, ehull 0.021 (in window edge, near-stable). Others: BaSi/SrSi(AgS2)2 gap 2.5, ehull 0.03 (stable, too wide); BaTi(AgSe2)2 2.03/0.035. Ca analogs unstable (0.06-0.19); Cu analogs ehull>0.05 and gaps 1.7-3.2 (SrCu2SnSe4 0.1). Zr-Ca collapse gap to ~0.1 and unstable. Trends: gap Ca>Sr>Ba (2.18,1.69,1.42) for Ag-Si-Se: larger A lowers gap and stabilizes; Se lowers by ~1.1 vs S.

## [reflection] iteration 3 — 2026-10-12 08:22 UTC

Hypothesis held: larger A-site (Ba) tunes gap into window while retaining stability. Next iteration: BaAg2SiSe4 neighbors - Ba(Si,Ge)(AgSe2)2 mixes, BaAg2GeSe4/BaAg2SnSe4 are known in MP (skip), Ba-Ag-Si-Se-Te mixed anions, Sr/Ba alloy, Ba-Si-Ag-Se with Ga/In-doped; also try Ba with Cu-Ge/Si mixed or K/Na-based analogs. Check ehull improvement via Ba-Ag-Si-Se_xS mixed anions (BaAg2SiS2Se2) if prototype allows. Gap 1.42 is CHGNet-HSE estimate; real structure of BaAg2SiSe4 likely differs from kesterite (known BaAg2GeS4 is I-42m/Ama2 types), so DFT check recommended.

## [hypothesis] iteration 4 — 2026-10-12 08:23 UTC

Iteration 4: Ag-Se Ba/Sr kesterite-type family is exhausted in Se/S (all already considered). Test (a) alkali analogs A2(Ba,Sr)(Si,Ge,Sn)(Se,Te)4 with Na/K replacing Ag: ionic, stable-likely, gap may fall near 1.4 for Sn/Ge selenides (Sn s-states lower CBM); (b) Te analogs of Ba/Sr-Ag-Si/Ge: Te lowers gap from 1.42/1.69 and Ge lowers vs Si, probing the lower side. Surrogate ranks BaNa2SnSe4, BaNa2GeSe4, BaNa2SiSe4 top (high uncertainty).

## [observation] iteration 4 — 2026-10-12 08:24 UTC

Iter 4: evaluated 20 novel alkali (Na/K) A2(Ba,Sr)(Si,Ge,Sn)(Se,Te)4 and Ag-Te analogs. Only in-window: BaNa2SnTe4 gap 1.31, ehull 0.058 (marginally unstable, just above 0.05). Stable: K2BaSiSe4 / K2SrSiSe4 (ehull 0) but gap ~3.4 (too wide). Alkali Se compounds gaps 2.2-3.4, ehull 0.055-0.095. Te Ag compounds: BaSi(AgTe2)2 2.15/0.069, SrSi 1.89/0.067, Ge-Te 0.2-0.7. Trends: Sn<Ge<Si gap; Te lowers gap ~1 eV but destabilizes (ehull +0.06-0.1). No new in-window near-stable hit; best of campaign remains BaAg2SiSe4 (1.42/0.026).

## [reflection] iteration 4 — 2026-10-12 08:24 UTC

Alkali hypothesis mostly falsified: stable ones have too-wide gaps, narrow-gap ones are unstable. Closest: BaNa2SnTe4 (1.31/0.058) - could try K2BaSnTe4 (known in MP) or Na/K mixes, Ba(Na,Ag) mixed cations, Sn-Se/Te anion mix (BaNa2SnSe2Te2) in iter 5 to get ehull<0.05 with gap ~1.5. Also Ag/Na mix: BaNaAgSnSe4-like. Also anion mixes in BaAg2SiSe4 (Se/Te 3:1) to lower to ~1.3 with minor destabilization. Prototype only supports pure-element substitutions so mixed sites are limited.

## [observation] iteration 5 — 2026-10-12 08:25 UTC

Iter 5: hypothesis: Mn/Fe/Co/Ni on divalent site of Ag-Si/Ge/Sn-S/Se kesterite-type lowers gap into window. Zincblende prototype only yields binaries (known/rejected) - useless. Evaluated 20 novel TM compounds: NONE in window. Near-stable: MnAg2GeS4 (0.248 eV, eh 0.021), NiAg2GeS4 (2.45, 0.033), SiNi(AgS2)2 (0.41, 0.049). Fe/Co compounds unstable (eh 0.07-0.19) and gaps 0-0.9 (CHGNet-HSE metallic-ish for open-shell d). Only CoSi(AgS2)2 1.89 (eh 0.10). MnNi(AgS2)2 0.97 / 0.107. Falsified: open-shell TM cations collapse gap rather than tune it, and destabilize.

## [reflection] iteration 5 — 2026-10-12 08:25 UTC

Campaign conclusion: best novel candidates are BaAg2SiSe4 (gap 1.423, eh 0.026; ideal), SrAg2SiSe4 (1.69/0.021), SrAg2SnS4 (1.67/0.024), MgAg2SnSe4 (1.15/0.043). Closed-shell d0/d10/s0 cations work; open-shell 3d TMs don't. Caveat: kesterite-type is probably not the true ground-state structure for Ba/Sr compounds; CHGNet gaps are estimates - verify with DFT/HSE and competing structure types (e.g. BaAg2GeS4-type) before synthesis. Prototype tools limit mixed sites; future work: Ba(Si,Ge) and Se/Te mixing, Sr/Ba alloys.
