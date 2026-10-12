# Lab Notebook

## [hypothesis] iteration 1 — 2026-10-12 08:26 UTC

Kesterite family: Cu2ZnSnS4 gap ~1.5. Substituting Ag for Cu, Cd/Mg for Zn, Ge/Si for Sn, and Se/S mixing tunes gap near 1.4. Expect Ag2ZnSnSe4, Cu2CdGeSe4, Cu2MgSnS4 etc. Many known; seek novel ones.

## [reflection] iteration 1 — 2026-10-12 08:27 UTC

20 evaluated. Only hit: MgAg2SnSe4 (gap 1.153, Ehull 0.043, novel). Near misses: MgAg2GeS4 (1.78, 0.006), MgSi(AgSe2)2 (1.84, 0.011), ZnSi(AgSe2)2 (1.84, 0.000), CaAg2SnSe4 (1.45 gap but Ehull 0.089). Gap trends: Sn<Ge<Si, S>Se>Te; Cu analogs too small gaps (semi-metal-like, CHGNet/ML gap noise). Gaps are noisy (Ge vs Sn inconsistent). Next: mixed anion S/Se on Ag2MgGe/ZnAg2GeSe4 (0.68)... try Ag2ZnGe(S,Se)4, Ag2MgGe(S0.5Se0.5), and Ag2CdSnSe4-like known calibration; also explore other families (e.g. Ag-Bi/Sb chalcohalides, Cu3SbS4-type).

## [hypothesis] iteration 2 — 2026-10-12 08:28 UTC

Iter 2: chalcopyrite and zincblende prototypes return only known compounds (no novelty). Mixed-anion not supported by tool. Stay in Ag-kesterite but vary the divalent site: Mn (d5, Mn2+ gap narrowing vs Mg), Ca/Sr (large, may reduce stability), Sn/Ge/Si tetravalent; and Zr/Ti-Cd/Mn combos for 4+ with Ag. Expect Mn-Ag2-Ge/Si-S4 ~1.4-1.8; Sr analogs interpolate between Mg and Ca (Ca Se-Sn gap 1.45 but hull 0.089). Spend on surrogate-high Mn items plus Sr/Zr/Cd diversity.

## [reflection] iteration 2 — 2026-10-12 08:28 UTC

Iter 2: 20 evaluated. HITS (novel, gap in window, Ehull<=0.05): BaSi(AgSe2)2 (gap 1.423, Ehull 0.026 - best), SrAg2SnS4 (1.667, 0.024), SrSi(AgSe2)2 (1.694, 0.021). Near: SrAg2GeS4 (1.95, 0.017), TiCd(AgS2)2 (2.23, 0.007). Chalcopyrite/zincblende prototypes yield only known compounds. Trends: large alkaline-earth (Sr, Ba) on divalent site is well tolerated in Ag-kesterite-type (Ehull 0.02-0.03) unlike Ca; Mn and Zr/Cd give near-zero gaps or high hull. Gap noise high for Se/Sn compounds (0.15-0.34 for Sr-Ge/Sn-Se). Next: Ba analogs (BaSi, BaGe with S/Se mixes), Sr/Ba with Si + Se/Te, check Ba-Si-Se hull; consider Cu analogs of Ba/Sr Si-Se, Na-based compounds.

## [reflection] iteration 3 — 2026-10-12 08:30 UTC

Iter 3: 20 evaluated, 0 hits. Cu analogs of Sr/Ba-kesterite (Si/Ge/Sn, S/Se/Te): Ehull 0.054-0.12, gaps either >1.7 (Si-S/Se) or <0.6 (Te, Sn): falsified; Cu does not tolerate large Sr/Ba site as well as Ag. Na/K alkali-kesterites (Ba/Sr/Ca, Ge/Sn, Se/Te): Ehull 0.055-0.096, gaps 2.2-3.0 (too wide) except BaNa2SnTe4 (gap 1.31, Ehull 0.058, just above hull limit; near-miss). Lesson: Ag is the key monovalent ion for stability in these; Te + alkali is the way to bring gaps into window; Na2Ba Sn Te4 / Ge Te4 variants and Ag/Na mixes are possible next steps. Best campaign hits remain BaSi(AgSe2)2 (1.42, 0.026), SrAg2SnS4, SrSi(AgSe2)2, MgAg2SnSe4.

## [hypothesis] iteration 4 — 2026-10-12 08:30 UTC

Iter 4: Exploit Ba/Sr-Ag kesterite family. Ba on divalent site gave best hit (BaSi(AgSe2)2). Test Ba/Sr with Ge/Sn/Si x S/Se/Te, and Ag-Cu-free; also Ca-Ba. Expect Ba-Ge-Se / Ba-Sn-S in 1.2-1.7 eV with Ehull ~0.03. Te variants with Si/Ge might narrow gaps toward 1.4 (BaNa2SnTe4 lesson: Te brings gap into window).

## [reflection] iteration 4 — 2026-10-12 08:31 UTC

Iter 4: Ba/Sr Ag-kesterite grid was already fully explored; chalcopyrite II-IV-V2 pnictides all known (no novelty). Evaluated 17 novel Ag-kesterites. HIT: MgSi(AgTe2)2 (gap 1.627, Ehull 0.014, novel). Near-miss: ZnSi(AgTe2)2 (1.717, Ehull 0.001). Zr-Zn(AgS2/Se2)2 gaps 1.22/1.33 but Ehull 0.08-0.11 (unstable). Ti-Zn S/Se stable (0.014-0.022) but gap 1.9-2.0; Te variants of Ti/Cd/Ge gaps <0.7. Ca-Si-Ag compounds unstable (0.06-0.09). Lesson: Si-Te Ag-kesterites with Mg/Zn sit at 1.6-1.7 eV and are stable; Te+Si is a good route; alloying Mg/Zn-Si-Te with Ge-Te could tune toward 1.4 (mixing not supported by tool). Grid is nearly exhausted; iteration 5 should try a new family (e.g. Ag-Bi/Sb chalcohalides or Cu3SbS4-type) if the tool permits.

## [hypothesis] iteration 5 — 2026-10-12 08:32 UTC

Iter 5: Ag-kesterite grid exhausted; zincblende yields known binaries. Test (a) Cu-kesterites with d0 Ti4+/Zr4+ and Mg/Sr/Ba/Cd/Ca: d0 chalcogenides (Cu-S/Se) with large A cations might give gaps 1.1-1.7 and ok hull; (b) Fe-containing Ag-kesterites (likely small gap, exploratory). Use surrogate to choose.

## [reflection] iteration 5 — 2026-10-12 08:33 UTC

Iter 5: 20 evaluated, 0 hits. Cu-kesterites with Ti/Zr d0: Ehull 0.05-0.22 (unstable); Zr ones have gaps in window (1.1-1.5) but hull 0.09-0.18. Closest: MgTi(AgSe2)2 (gap 1.516, Ehull 0.053 - marginal near-miss), TiCd(CuS2)2 (0.051, gap 2.16). Fe variants unstable/zero gap. Lesson: Ag is needed for stability; Ti/Zr tetravalent only mildly stable with Ag+Zn/Mg. Campaign best: BaSi(AgSe2)2 (1.42, 0.026), SrAg2SnS4, SrSi(AgSe2)2, MgAg2SnSe4, MgSi(AgTe2)2. Prototype tool limits (3 prototypes) exhausted novelty beyond Ag-kesterite; future work: mixed-anion/alloy and Ag-Sb/Bi chalcohalides if supported.
