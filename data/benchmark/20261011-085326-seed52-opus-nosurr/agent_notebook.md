# Lab Notebook

## [hypothesis] iteration 1 — 2026-10-11 08:53 UTC

Iter 1: Kesterite I2-II-IV-VI4 family. CZTS (~1.5 eV) and CZTSe (~1.0 eV) bracket target. Hypothesis: isovalent II-site substitution (Mg, Mn, Fe, Sr) and I-site Ag, combined with Ge/Sn and S/Se, gives novel members in 1.1-1.7 eV; Ag raises gap and reduces Cu-Zn antisite disorder; Mg/Sr on II site raise gap (more ionic) so pairing with Se should bring them into window. Many Ag/Mg/Sr combos are absent from MP. Calibration: ZnCu2SnSe4 (known, exp ~1.0 eV) to check gap fidelity.

## [observation] iteration 1 — 2026-10-11 08:56 UTC

Iter 1 results (kesterite, CHGNet+HSE-fidelity gap):
HITS (novel, Ehull<=0.05, gap 1.1-1.7): CdAg2GeSe4 (1.28 eV, Ehull 0.000), ZnAg2GeSe4 (1.12 eV, 0.000), MgAg2SnSe4 (1.59 eV, 0.016), MgAg2GeTe4 (1.49 eV, 0.025).
Near-stable but gap too wide: MgCu2SnS4 2.17 (0.020), MgAg2SnS4 1.87 (0.002), MgAg2GeS4 1.89 (0.017), MgAg2GeSe4 1.86 (0.020). CdAg2GeTe4 stable-ish (0.017) but gap 0.48.
In window but unstable: MgCu2SnSe4 1.38 (0.071), MgCu2GeSe4 1.10 (0.136).
Fails: Fe members metallic (~0 eV) & unstable; Mn members unstable (0.08-0.10); Si-Se Ag members unstable (0.13-0.17).
Calibration: ZnCu2SnSe4 (CZTSe, exp ~1.0 eV) -> 0.34 eV, Ehull 0.057. So Cu-based gaps underestimated by ~0.6 eV here; Ag-based may be more reliable (less Cu-d/Se-p repulsion), but treat Cu gaps as lower bounds.
Critic vetoes: Sr on Zn site (too large); Si with Te.

## [reflection] iteration 1 — 2026-10-11 08:56 UTC

Hypothesis largely held for Ag-kesterites: Ag2-II-Ge-Se4 and Mg-based Ag selenide/telluride members are stable and in window. Mg on II site is a good gap-raiser that keeps stability with Ag (not with Cu+Se). Te strongly lowers gap with Cd (0.48) but Mg+Te lands 1.49. Next iteration: (1) exploit Ag kesterites — mixed-anion is not available, so explore Ag2MgSnTe4, Ag2ZnSnTe4?, Ag2MgGe(S/Se) gap tuning via Sn vs Ge in tellurides; Ag2CdSnSe4-type known; (2) explore chalcopyrite prototype with Ag-III-VI2 and Cu-III-VI2 substitutions (AgAlTe2, AgGaTe2 ~1.3 known; look for novel ones e.g. with In/Ga + Te mixtures are not possible; so maybe I-site Na/K?); (3) zincblende/ternary nitrides or phosphides (e.g. ZnGeP2-like via zincblende sub?). Unused 1 relaxation this iteration.

## [hypothesis] iteration 2 — 2026-10-11 08:57 UTC

Iter 2. Finding: II-IV-V2 pnictide chalcopyrites (Zn/Cd/Mg-Si/Ge/Sn-As2) are all KNOWN in MP; phosphides fail SMACT filter -> abandoned. Remaining novel space is in kesterite I2-II-IV-VI4. Hypotheses: (A) Ag2-II-Sn-Te4 (Mg/Zn/Cd): Sn vs Ge lowers gap slightly; MgAg2GeTe4 was 1.49 -> MgAg2SnTe4 ~1.2-1.4; Zn/Cd Sn tellurides may be ~0.5-1.0 (Cd-Ge-Te was 0.48) — test as bracket. (B) Cu2Mg(Si/Ge)Te4: Mg+Si widen gap, offsetting Te and Cu-d gap compression; MgCu2SnSe4 was 1.38 (but 0.071 Ehull) so Te/Si version may be ~1-1.5. (C) Ti4+ on IV site (d0): empty Ti-3d CB lowers CBM; Cu2ZnTiS4-type sulfides predicted ~1-1.5 eV in literature screening, but tetrahedral Ti may be thermodynamically disfavoured (Ti prefers octahedral) — explicit stability test. (D) Ag2CdSiS4 as a wide-gap bracket for Si-S Ag members.

## [observation] iteration 2 — 2026-10-11 09:00 UTC

Iter 2 results (20/20 budget used; 3 critic vetoes cost nothing).
NEW HITS (novel, Ehull<=0.05, gap 1.1-1.7): MgAg2SnTe4 1.17 eV (Ehull 0.038); Na2CdSnTe4 1.37 eV (0.032) — closest to 1.4 ideal; Na2MgGeTe4 1.14 eV (0.047, borderline both).
Near-miss: Na2CdGeTe4 1.74 eV (0.021) — just above window.
Ag-Sn tellurides: ZnAg2SnTe4 0.60 (0.039), CdAg2SnTe4 0.41 (0.027) — too small gap, as bracketed.
Na-kesterites are broadly near-stable (Ehull 0.007-0.055 for all 9!) but gaps mostly wide: Na2ZnSnSe4 2.29, Na2CdSnSe4 1.96, Na2CdGeSe4 2.41, Na2ZnSnTe4 2.05, Na2ZnGeTe4 2.42, Na2MgSnTe4 1.93 (0.055). Trend: Cd < Zn for gap (Cd 5s CBM lower), Te << Se. Anomaly: Na2MgGeTe4 (1.14) < Na2MgSnTe4 (1.93), opposite to usual Sn<Ge trend — treat as possible model artefact/structure distortion; needs care.
Ti4+ kesterites: Cu2(Zn,Cd,Mg)TiS4 all Ehull 0.000 but gaps 2.66-2.94 (too wide, opposite to hypothesis C that d0 Ti lowers CBM into window). Cu2ZnTiSe4 and all Ag-Ti members highly unstable (0.35-0.41).
MgCu2GeTe4 0.90 eV, Ehull 0.101 — Cu+Mg unstable again (consistent with iter 1).
Critic: Si4+ vetoed in Ag/Cu kesterites (size mismatch) — avoid Si in this prototype.
Pnictide II-IV-As2 chalcopyrites all known in MP; II-IV-P2 rejected by SMACT filter.

## [reflection] iteration 2 — 2026-10-11 09:00 UTC

Hypothesis A held for Mg (MgAg2SnTe4 1.17) but Zn/Cd-Ag-Sn tellurides are too narrow. Hypothesis C (Ti lowers gap) falsified: Cu-Ti-S stable but ~2.8 eV. New productive axis: Na on I site — near-universal near-stability in kesterite, gaps 1.1-2.4 eV; Cd+Te is the gap-lowering combo (Na2CdSnTe4 1.37). Next iteration ideas: (1) Na-kesterites with Cd/Zn + Sn/Ge + Te are exhausted; try K? (likely vetoed: too big) — instead try mixed I-site isn't possible; try Na2(Cd,Zn,Mg)-(Sn,Ge)-S? no, wider. Better: Na2-II-IV-Te4 with II = Mn/Fe? (Fe metallic before). (2) Ag2Mg-Sn/Ge chalcogenides gave 4 hits; consider Ag2Ca? (critic may veto size). (3) Explore zincblende prototype for ternary/novel binaries is limited. (4) Chalcopyrite with Na/Ag on I and Al/Ga/In on III with Te (NaInTe2, NaGaTe2 chalcopyrite-form?) — check novelty; Na-III-Te2 by analogy to Na-kesterite stability with gaps possibly 1.2-1.8. Also check Na2MgGeTe4 anomaly.

## [hypothesis] iteration 3 — 2026-10-11 09:00 UTC

Iter 3. Family: alkali/coinage I-III-VI2 chalcopyrites (prototype CuInSe2) with I = Na, Ag, K(?); III = Al, Ga, In; VI = S, Se, Te. Reasoning: iter 2 showed Na on the I site keeps kesterites near-stable (Ehull 0.007-0.055 for all 9) and gives gaps ~1.1-2.4 eV, with Te lowering the gap. Na+ (r_tet ~0.99 A) vs Cu+ (0.60) is larger but Na-kesterites still relaxed fine. Na has no d10 states, so VBM is purely anion-p -> gaps larger than Cu analogues; pairing Na with Te and In/Ga (low-lying s CBM) should bring the gap to 1.1-1.7. MP has NaInTe2 (0.64 eV, TlSe-type, known), but Na-Ga-Se has no NaGaSe2 and Na-Ga-Te/Na-Al-Te chalcopyrites appear absent; literature on Na-chalcopyrites is essentially empty -> boundary of knowledge. Expected: NaGaTe2 ~1.3-1.7, NaAlTe2 ~2, NaInSe2 ~1.5; Ag-III-VI2 mostly known (calibration AgGaTe2? skip). Risk: Na-III-VI2 ground states are layered/octahedral (alpha-NaFeO2-type) so tetrahedral chalcopyrite may sit above hull. K likely vetoed (too big).

## [observation] iteration 3 — 2026-10-11 09:04 UTC

Iter 3 (20/20 used, 1 veto: BaNa2SnTe4 flagged as charge-imbalanced — likely a formula-parsing artefact, but avoid Ba with Na; K2Ba works).
Chalcopyrite I-III-VI2 space is almost fully KNOWN in MP (only NaAlS2, NaGaS2, NaGaSe2, KAlS2, KGaSe2 novel). NaGaSe2 chalcopyrite: 2.20 eV, Ehull 0.017 — too wide. Chalcopyrite family abandoned.
Kesterite A2-II-IV-Q4 alkali extension — 8 NEW HITS (novel, Ehull<=0.05, gap 1.1-1.7):
 K2MgSnTe4 1.33 eV (0.000) <- closest to 1.4, on hull
 K2MgGeTe4 1.50 (0.000)
 K2BaGeTe4 1.57 (0.000)
 K2SrGeTe4 1.22 (0.013)
 K2SrSnTe4 1.20 (0.012)
 K2CaSnTe4 1.12 (0.033)
 Na2MnGeSe4 1.65 (0.008)
 Na2MnSnSe4 1.115 (0.000) (edge)
Edge/misses: K2MnGeTe4 1.100 (0.002) at boundary; Na2MnGeTe4 1.09 (0.043); Na2MnSnTe4 0.95 (0.046); K2MnSnTe4 0.65 (0.000); K2CdSnTe4 0.86, K2CdGeTe4 0.88 (both on hull, too narrow); K2CdGeSe4 2.41 (0.000, too wide); Na2CaGeTe4 1.73 (0.000, just above window).
Unstable: Na2CaSnTe4 (0.169), Na2SrSnTe4 (0.124), Na2SrGeTe4 (0.113) — Na lattice too small for Ca/Sr with Sn/Te; K accommodates large alkaline earths (all K-AE members ≤0.033).
Trends: K lowers gaps vs Na for Cd members (K2CdSnTe4 0.86 vs Na2CdSnTe4 1.37). Mn (d5) lowers gap ~0.5-1 eV vs Mg. Sn<Ge gap consistently for K members (normal trend restored). Caveat: Mn high-spin magnetism treatment in CHGNet/gap model uncertain; real K/Na kesterite-type tellurides are hygroscopic and the true ground-state structure may differ from kesterite (e.g. K2MnSnSe4 known in MP in another structure).

## [reflection] iteration 3 — 2026-10-11 09:04 UTC

Hypothesis (alkali kesterites with larger II cations, K for size matching) strongly supported: size-matching rule worked — K pairs with Ca/Sr/Ba (stable), Na does not (Ehull >0.11). Chalcopyrite sub-hypothesis failed for novelty reasons (space already in MP), not physics. Next iteration (4): (1) fill remaining K-family gaps: K2CaGeTe4, K2BaSnTe4 is known; K2(Ca,Sr,Ba,Mg)-(Sn,Ge)-Se4 likely too wide (~2+), test 1-2 as brackets; K2ZnSnTe4/K2ZnGeTe4 (Zn between Mg and Cd); (2) Na2Mn/K2Mn selenides gave in-window gaps — try Na2Mn with Si? (Si vetoed with Cu/Ag, maybe ok with Na) and K2MnGeSe4/K2MnSnSe4(known); (3) Ag2-AE (Ca/Sr) tellurides likely vetoed for size; (4) Consider exploration of a different prototype for iter 5 (zincblende-derived ternaries not available — limited). Prioritise robustness: avoid edge-of-window results.

## [hypothesis] iteration 4 — 2026-10-11 09:04 UTC

Iter 4. Exploit/complete the alkali kesterite A2-II-IV-Q4 family (literature essentially silent on K/Na kesterite-type tellurides/selenides; MP has no K-Zn-Sn-Te or K-Mn-Ge-Se entries). Sub-hypotheses: (A) K2Zn(Sn,Ge)Te4: Zn sits between Mg and Cd in CBM energy; K2Mg gave 1.33/1.50 and K2Cd 0.86/0.88, so K2Zn should interpolate to ~1.1-1.4 and remain stable (K hosts all II cations so far). (B) K2CaGeTe4: K2CaSnTe4 1.12, Ge raises gap ~0.2-0.4 -> ~1.4. (C) K2-(Mg,Ca,Sr,Ba,Mn)-(Ge,Sn)-Se4 selenides: Se raises gap ~0.5-0.8 vs Te; K2Mn tellurides were 0.65-1.10 so K2MnGeSe4/K2MnSnSe4 should land ~1.3-1.7; AE selenides expected >2 eV (brackets, 1-2 only). (D) Na2Mg(Sn,Ge)Se4 vs known Na2MgGeTe4 anomaly check is low value; skip. Size rule from iter 3: Na only with small II (Zn, Cd, Mg, Mn); K with anything.

## [observation] iteration 4 — 2026-10-11 09:08 UTC

Iter 4 (20/20 used, no vetoes). NEW HITS (novel, Ehull<=0.05, gap 1.1-1.7):
 K2CaGeTe4 1.42 eV (0.019) <- nearly ideal 1.4 (predicted 1.4 from Sn->Ge shift; confirmed)
 K2MnGeSe4 1.44 eV (0.000) <- on hull, ideal gap (predicted 1.3-1.7; confirmed)
 K2ZnSnTe4 1.57 eV (0.000) on hull
 SrAg2GeSe4 1.69 eV (0.003) edge of window
Misses: K2ZnGeTe4 1.90 (0.000), K2ZnSnSe4 2.27 (0.000) too wide. Zn hypothesis partly wrong: K2Zn gaps > K2Mg (1.57 vs 1.33 for Sn-Te), not interpolated between Mg and Cd.
Ag/Cu-AE kesterites: AE-Te members are near-stable but gaps collapse (BaAg2SnTe4 0.52, BaAg2GeTe4 0.71, SrAg2SnTe4 0.10, SrAg2GeTe4 0.16, BaCu2SnTe4 0.14, BaCu2GeTe4 0.50, SrCu2SnTe4 0.87). Ca on II site with Ag/Cu unstable (0.05-0.12): CaAg2GeSe4 1.68 but 0.062; CaCu2GeSe4 1.20 but 0.121. Cu-AE models probably underestimate gap (Cu calibration -0.6 eV), so SrCu2SnTe4 (0.87, on hull) could be ~1.4 in reality — flag as uncertain.
Note: evaluate_candidates accepted previously-proposed-but-unevaluated formulas (K2CaGeTe4, K2MnGeSe4).

## [reflection] iteration 4 — 2026-10-11 09:08 UTC

The alkali-kesterite line keeps paying off: K2-II-IV-Q4 is stable for every II tested (Mg, Ca, Sr, Ba, Zn, Mn, Cd) and the gap is tuned by II + IV + Q. Two near-ideal (~1.42-1.44 eV) members found this iteration. The coinage-metal AE kesterite branch mostly failed: tellurides too narrow, Ca unstable; only SrAg2GeSe4 is a marginal hit. Ag-AE-Se is the useful Ag sub-space (Sr/Ba-Ag-Sn-Se are partly known in MP). For iter 5 (final): (1) finish the K/Na alkali space with the remaining unevaluated members, e.g. K2MnSnSe4 is known; K2BaGeSe4/K2SrGeSe4 probably too wide; Na2Zn/Mg with Se also too wide. Better: test robustness of the top hits (compare Ehull across polymorph-sensitive members) — can't do with this tool. (2) Explore BaAg2GeSe4/SrAg2SnSe4 analogues with Cd/Zn?? done. (3) Spend the last budget on unexplored combinations: K2Mn(Ge)S4? K2Mg/Ca/Zn-Ge/Sn-Se brackets, Na2Cd/Mn-Si-Se (Si with Na not tested), Ag2SrSnSe4-type with Ge/Si. Keep stability-first prioritisation.

## [hypothesis] iteration 5 — 2026-10-11 09:08 UTC

Iter 5 (final). Family: Si4+ on the IV site in alkali kesterites A2-II-Si-Te4 (A = K, Na), plus a few Se brackets. Reasoning: in iters 2-4 swapping Sn->Ge raised the gap by ~0.2-1.0 eV for K members (K2CaSnTe4 1.12 -> K2CaGeTe4 1.42; K2MgSnTe4 1.33 -> K2MgGeTe4 1.50). Si (more electropositive than Ge, higher-lying antibonding Si-3s/Te-5p CBM) should raise it further. The best place to use this is the narrow-gap K tellurides: K2CdGeTe4 0.88 -> K2CdSiTe4 ~1.2-1.5; K2MnGeTe4 1.10 -> K2MnSiTe4 ~1.3-1.5; K2SrGeTe4 1.22 -> K2SrSiTe4 ~1.4-1.6; Na2MnGeTe4 1.09 -> Na2MnSiTe4 ~1.3. Mg/Ca/Ba/Zn-Si members are expected to be too wide (>1.7) and serve as brackets. Si was vetoed for Cu/Ag kesterites because of size mismatch with small I cations; the large K/Na tetrahedral framework is less tight, but Si-Te bonds are weak, so stability is the main risk (Si-Te tetrahedra exist in e.g. thiosilicate-like tellurosilicates such as Na/K tellurosilicates, so not impossible). MP has no entries in K-Cd-Si-Te or K-Mn-Si-Te; literature search returned nothing -> past the knowledge boundary. Secondary exploration: K2(Fe,Co)GeSe4 — Co2+ d7 is happy in tetrahedra; earlier Fe members (with Cu/Ag) were metallic, but with K the narrower bands may open a gap.

## [observation] iteration 5 — 2026-10-11 09:11 UTC

Iter 5 (20/20 used, no vetoes). Si-on-IV alkali kesterites.
NEW HITS (novel, Ehull<=0.05, gap 1.1-1.7):
 K2CdSiTe4 1.235 eV (0.000) on hull — predicted 1.2-1.5 from K2CdGeTe4 0.88 + Si shift; confirmed
 K2MnSiTe4 1.455 eV (0.045) — predicted 1.3-1.5; confirmed but Ehull near limit
 K2BaSiTe4 1.64 eV (0.000) on hull
 K2MgSiTe4 1.69 eV (0.005) edge of window
 K2MnSiSe4 1.675 eV (0.040) edge of window
Misses: K2ZnSiTe4 2.07 (0.000), K2CdSiSe4 2.69 (0.009), Na2CaSiTe4 2.05 (0.000) too wide; K2CaSiTe4 1.455 but Ehull 0.098; K2SrSiTe4 1.88 (0.105).
Na-Si tellurides are all UNSTABLE (0.09-0.21) except Na2CaSiTe4 — opposite of Na-Ge/Sn behaviour; Si + small Na makes the lattice too tight (except Ca pairing). Na2MnSiSe4 1.56 but 0.151.
Exploration Co/Fe: K2CoGeSe4 2.31 (0.021), K2CoSnSe4 2.12 (0.020) stable but wide (caution: d-d / spin treatment); K2FeGeSe4 0.63 (0.010), K2FeSnSe4 0.44 (0.000) stable but narrow. Fe gives gapped (not metallic) states in K lattice, unlike Cu/Ag-Fe members.
Trend: Ge->Si raises gap ~0.35 eV (Cd, Mn Te) and ~0.2-0.65 for others; Si stability is good with K + small/medium II (Cd, Mn, Mg, Zn, Ba) but poor with Ca/Sr (non-monotonic; Ba on hull).

## [reflection] iteration 5 — 2026-10-11 09:11 UTC

Final reflection. Si hypothesis held for K tellurides (5 hits, 2 on hull), falsified for Na (size/tightness → unstable), consistent with the iter-3 size-matching rule extended to the IV site: the smaller Si needs the larger K framework. Campaign totals: ~25 novel kesterite-type hits in A2-II-IV-Q4 (A = Ag, Na, K). Closest to ideal 1.4 eV and on/near hull: K2MnGeSe4 1.44 (0.000), K2CaGeTe4 1.42 (0.019), K2MnSiTe4 1.455 (0.045), K2MgSnTe4 1.33 (0.000), Na2CdSnTe4 1.37 (0.032), K2CdSiTe4 1.235 (0.000), CdAg2GeSe4 1.28 (0.000). Caveats for follow-up: (1) Ehull is only relative to MP phases + the kesterite polymorph; real alkali compounds such as K2MnSnSe4 take other structures, so competing polymorphs (e.g. K2BaSnTe4-type, isolated-tetrahedra structures) must be checked with DFT; (2) Cu-gap calibration was off by -0.6 eV, so Ag/alkali gaps should be validated with HSE/experiment; (3) Mn/Fe/Co magnetism in the model is uncertain; (4) alkali tellurides are air/moisture sensitive — this matters for practical use. Next campaign: polymorph search for top K-hits, DFT-HSE gaps, and optical absorption (direct vs indirect).
