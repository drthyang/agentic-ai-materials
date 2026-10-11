# Lab Notebook

## [hypothesis] iteration 1 — 2026-10-11 07:41 UTC

Family: I-III-VI2 chalcopyrites with Cu/Ag on I site, Al/Ga/In on III, S/Se mixed anion. Wide-gap members (AgGaS2 ~2.7, CuGaS2 ~2.4, CuAlS2 ~3.5, AgInS2 ~1.9) are in the visible window. Isoelectronic substitution and anion mixing (S/Se alloys) should tune gaps. Aim at novel mixed-anion/mixed-cation ordered variants, which are likely absent from MP. Literature: AgGaS2 visible emission known, I-III-VI2 QDs studied (Cd-free).

## [observation] iteration 1 — 2026-10-11 07:44 UTC

Chalcopyrite family: all 17 candidates known in MP (no novelty) -> skipped. Kesterite-type I2-II-IV-VI4 (19 evaluated, all novel). HITS (novel, ehull<=0.05, gap in window): MgAg2SnS4 (ehull 0.002, 1.87 eV), MgAg2GeS4 (0.017, 1.89), MgAg2GeSe4 (0.020, 1.86), MgCu2SnS4 (0.020, 2.17 eV). Near-stable but gap too low: ZnAg2GeSe4 (0.0, 1.12), MgAg2SnSe4 (0.016, 1.59). Larger Ca/Sr/Ba and Si-containing ones: gaps 2.2-3.0 but ehull 0.07-0.24 (unstable, mismatched cation size in kesterite). Trend: Mg is the largest II cation that stays stable in this structure; Si destabilises; selenides lower the gap ~0.3-0.5 eV; Ag vs Cu lowers gap vs Cu for S-Sn.

## [reflection] iteration 1 — 2026-10-11 07:44 UTC

Hypothesis partly confirmed: Mg-based quaternary sulfides give stable visible-gap novel compounds. Gaps cluster at the low edge (1.86-2.17) vs ideal 2.4. Next: raise gap via Mg-Cu-Ge-S (check novelty), Zn/Mg mixes, Cu-Mg-Sn-S analogs, and other families (Zn-based nitrides/phosphides, Ba-Zn-chalcogenides, Cu/Ag-halide mixed, Ag-Al/Ga-S). Chalcopyrite ternary space is fully covered in MP; avoid. Quantum confinement will blue-shift, so ~1.9 eV bulk may still be fine.

## [hypothesis] iteration 2 — 2026-10-11 07:44 UTC

Iter 2: Extend Mg-kesterite family to raise gap toward 2.4: Cu/Ag mixed on I site is not allowed by prototype, so use Mg/Zn II-site, Ge/Sn IV, S/Se anion, Cu-based (Cu gives higher gap than Ag). Expect Cu2MgGeS4 (~2.4?), Cu2MgSnS4 variants; also Cu2ZnGeS4/Cu2ZnSiS4 checks for novelty. Mg stable due to size match with Cu+/Sn. Literature: Cu2MgSnS4 is being studied (2026), so Mg-Cu-Sn-S may be borderline known; Mg-Ge likely less explored.

## [observation] iteration 2 — 2026-10-11 07:48 UTC

Iter 2: Mg/Zn x Cu/Ag x Si/Ge/Sn x S/Se kesterite space exhausted (all 'already considered'). Zincblende prototype gives only known binaries; chalcopyrite II-IV-N2 all known (P analogs rejected by SMACT). Only novel space: oxide and telluride kesterite variants; evaluated 16. ZERO hits. Oxides: ehull 0.002-0.55; only ZnCu2SnO4 near-stable (0.002) but gap 0.26 (metallic-like); wide-gap oxides (MgCu2GeO4 3.05 eV, MgAg2GeO4 2.94) have ehull 0.12-0.25 - tetrahedral oxide kesterite is wrong coordination for Mg/Ge. Tellurides: near-stable MgAg2GeTe4 (0.025, 1.49), ZnAg2GeTe4 (0.028, 1.17) but gaps too low; Si-tellurides gaps 1.8-2.0 but ehull 0.09. 4 relaxations left unspent (remaining novel candidates were Sn tellurides with expected gap <1.5).

## [reflection] iteration 2 — 2026-10-11 07:48 UTC

Prototype menu limits the search: kesterite/chalcopyrite/zincblende with the palette is nearly saturated. Anion exchange to O destabilises; Te lowers gap too much. Best campaign hits remain iter-1 Mg-Ag/Cu-Sn/Ge-S(e) kesterites (1.86-2.17 eV). Next iteration: try different substitution patterns not yet exhausted, e.g. kesterite with Ca/Sr/Ba on Zn site paired with Ag/Cu and Ge/Sn selenides/sulfides of different ratios is unstable; consider chalcopyrite with Zn/Mg + Sn/Ge + S? (not charge balanced); consider halide-containing (Cl/Br/I) substitutions of zincblende/chalcopyrite (e.g. Cu/Ag-halides, Zn-halides) or Al/Ga/In with N/P for novel ordered variants; avoid O and Te in kesterite.

## [observation] iteration 3 — 2026-10-11 07:51 UTC

Iter 3: zincblende (only known Cu/Ag halides) and chalcopyrite (only AgPN2, odd) offered nothing. New family found via kesterite substitution: A2(II=Ba/Sr/Ca) M(I=Cu/Ag) M'(III=Al/Ga/In) Q4. Evaluated 20 novel. HIT: Ba2InCuS4 (ehull 0.012, gap 2.18 eV). Borderline: Ba2GaCuS4 (0.056, 2.65 - just over hull limit). Near-stable but gap too low: Ba2GaCuSe4 (0.027, 1.68), Sr2InCuSe4 (0.012, 0.45), Sr2GaCuSe4 (0.051, 1.19). Trends: stability needs large A cation (Ba>Sr>Ca) and large III (In>Ga>Al); Al and Ca are very unstable (0.2-0.35). Cu more stable than Ag. Gap rises with smaller III (In<Ga<Al) and sulfide>selenide. Kesterite tetrahedral geometry is probably not the true ground state for Ba compounds (real ones likely different structure), so ehull is only relative to hull.

## [reflection] iteration 3 — 2026-10-11 07:51 UTC

Hypothesis (large AE + Cu + III chalcogenides) partly confirmed: one clean hit Ba2InCuS4 plus borderline Ba2GaCuS4. Next iter: Ba/Sr mixes impossible in prototype, but try Ba2 with Zn-free variants: Ba2InCuS4 analogs with Ag (Ba2InAgS4 is known), Ba2GaCuS4 at 0.056 could be tuned; Ba2InCuSe4 / Ba2InCuTe not useful (gap low). Consider alkaline-earth + Zn/Mg + IV + S in kesterite with Ba (Ba2ZnSnS4-type -> not balanced). Also consider S-rich Ba2(Ga,In) mixes not accessible. Try Ba-only with Cu/Ag + Ga/In + S/Se where gap 2-2.6: remaining untested Ba2InCuSe4, Ba2AlCuSe4 (likely unstable).

## [observation] iteration 4 — 2026-10-11 08:00 UTC

Iter 4: Ba/Sr2-M(I)-M(III)-Q4 family and pnictide/halide kesterite/chalcopyrite variants saturated (known or SMACT-rejected). My II-IV-VI2 chalcopyrite proposal was charge-imbalanced (error; critic vetoed all, no budget used). Evaluated: (a) II2-IV-IV'-N4 nitrides (Zn/Mg x Si/Ge/Sn): all ehull 0.37-0.53, useless. (b) All-II chalcogenide ordered kesterites AZn3Q4/AMgZn2Q4: HIT CaZn3S4 (ehull 0.037, gap 2.91 eV, novel). Near-stable but gap too low: BaZn3Te4 (0.037, 0.46), CaZn3Te4 (0.066, 0.95), CaMg(ZnTe2)2 (0.058, 2.29 - just over hull limit, in window). Others unstable: MgZnSe2/MgZnTe2 (0.22/0.13), SrZn3S4 0.227, BaZn3S4 0.19, Se analogs 0.10-0.21. Trend: only the Ca-for-Zn 1/4 substitution in ZnS-type is tolerated (size mismatch rises Ca<Sr<Ba) for sulfides; for tellurides larger cations tolerated better; gaps drop with Te/Se.

## [reflection] iteration 4 — 2026-10-11 08:00 UTC

Iter 4 result: one new hit, CaZn3S4 (2.91 eV, 0.037) - gap at upper edge; quantum confinement would push it into the UV so it's a marginal display candidate. Campaign hits: MgAg2SnS4, MgAg2GeS4, MgAg2GeSe4, MgCu2SnS4, Ba2InCuS4, CaZn3S4. Iter 5 ideas: ZnS-based dilute-Ca/Mg alloys with Se/Te anion mixing for lower gap (CaZn3(S,Se)4 not possible via prototype), Ca on Zn site in Zn-rich ordered structures with Cu/Ag-Ga/In ... avoid charge-imbalanced II-IV-VI2; check charge balance before proposing. CaMg(ZnTe2)2 near-border (0.058, 2.29 eV).

## [observation] iteration 5 — 2026-10-11 08:02 UTC

Iter 5: Evaluated 20 novel Zn2/Mg2-(Cu/Ag)-(Al/Ga/In)-(S/Se)4 ZnS-derived ordered quaternaries (II2 I III Q4 on kesterite sites). ZERO hits: ehull 0.09-0.52 eV/atom (best Zn2InAgSe4 0.093, gap 1.2). Gaps in window for many S members (2.1-2.96) but all strongly unstable. Trend: instability grows as III cation shrinks (In<Ga<Al); Mg2/Zn2 with Cu/Ag+III is not a stable ordering — probably competes with ZnS + CuGaS2 phase separation (positive mixing energy from Cu+/Ga3+ vs Zn2+ charge ordering mismatch) and Mg strongly prefers octahedral.

## [reflection] iteration 5 — 2026-10-11 08:02 UTC

Iter 5 hypothesis falsified. Final campaign hits (novel, ehull<=0.05, gap 1.8-3.1): MgAg2SnS4 (0.002, 1.87), MgAg2GeS4 (0.017, 1.89), MgAg2GeSe4 (0.020, 1.86), MgCu2SnS4 (0.020, 2.17), Ba2InCuS4 (0.012, 2.18), CaZn3S4 (0.037, 2.91). Borderline: Ba2GaCuS4 (0.056, 2.65), CaMg(ZnTe2)2 (0.058, 2.29). Lessons: stable novel space came from cation-size-matched kesterite-like substitutions (Mg with Cu/Ag + Sn/Ge; large Ba with In+Cu). Follow-up beyond this campaign: validate hits with DFT-level hull (CHGNet ehull vs competing phases), check real ground-state structures for Ba2InCuS4, assess phonon stability; prototype menu was saturated otherwise.
