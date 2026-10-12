# Lab Notebook

## [hypothesis] iteration 1 — 2026-10-12 07:40 UTC

Kesterite family Cu2ZnSnS4 (gap ~1.5 expt). Isoelectronic substitutions: Zn->Cd/Mg, Sn->Ge/Si, S->Se, Cu->Ag mix. Expect gap tuning: Se lowers gap, Cd lowers, Ge raises. Aim for novel members like Cu2CdGeSe4, Ag2ZnSnS4, Cu2MgSnS4, mixed S/Se anions that land in 1.1-1.7 eV.

## [observation] iteration 1 — 2026-10-12 07:41 UTC

17 novel/known evaluated (16 novel). All kesterite-type, ehull 0-0.047. Only hit: MgAg2SnSe4 gap 1.153, ehull 0.043 (marginal both). Trends: Se/Te and Sn/Ge-Cu compounds gaps 0.2-0.6 (too low, CHGNet/HSE-surrogate); Si and Mg raise gap (MgSi(AgSe2)2 1.84, ZnSi(AgSe2)2 1.84 hull 0; MgAg2GeS4 1.78 hull 0.006; CdSi(AgS2)2 2.22). Cd/Ag-Ge-Se 0.03-0.68. Zn/Cd-Ag-Sn selenides and Cu-Cd analogs already known. Gaps just above window: Ag2MgGeS4 1.78, Ag2ZnSiSe4 1.84; just below: MgAg2SnSe4 1.15. Cannot mix anions/cations in a single compound via this tool (substitution is full-site).

## [reflection] iteration 1 — 2026-10-12 07:41 UTC

Hypothesis partly held: kesterite substitutions give stable novel compounds, but gaps rarely land in window; Cu variants too narrow, Ag-Si/Ge too wide. Next: try Ag-Mg/Zn-Ge-Se alloy-equivalent via ordered compounds (e.g. other prototypes: chalcopyrite AgGaS2/AgInS2 type, CuGaTe2 analogs, AgAlSe2, AgGaSe2 variants, Cu-Ga-S), or ZnGeP2/ZnSnAs2 type pnictides from zincblende. Keep Mg-Ag-Sn-Se as a lead; try Ag-Ge-S with Zn/Cd bridging 1.1-1.7. Unused 3 relaxations (no novel candidates left).

## [hypothesis] iteration 2 — 2026-10-12 07:41 UTC

Iter 2: chalcopyrite family I-III-VI2 and II-IV-V2 pnictides. Ag/Cu-Ga/In/Al chalcogenides with Se/Te/S combos; gaps: CuGaSe2 1.7, AgInSe2 1.2, CuInS2 1.5, AgGaSe2 1.8, AgInS2 1.9, CuAlSe2 2.7. Expect Ag-In-Se/Te, Cu-In-S, Cu-Ga-Te (~1.2) near window. Pnictides: ZnSnP2 (~1.4 expt), ZnGeAs2, CdSnP2 variants. Novel ones likely among unusual pairings (CdSnP2 / CdGeP2 /MgSnP2 etc. via zincblende/chalcopyrite). Check MP for known and evaluate novel.

## [observation] iteration 2 — 2026-10-12 07:42 UTC

Iter 2: 20 novel evaluated. Chalcopyrite II-IV-Sb2 antimonides: gaps 0.04-0.9 (too low), hull 0.01-0.08. NaGaS2/NaAlS2 stable but gap >4. CuBiTe2 gap 1.446 but hull 0.052 (just misses). CuAsS2 gap 0.68 hull 0.085. Mixed I3-V-VI4 (famatinite/enargite-like on kesterite proto): HITS: Ag3SbSe4 gap 1.255 hull 0.0; CuAg2AsS4 gap 1.56 hull 0.012; Cu2AgAsS4 gap 1.627 hull 0.010. Others: Ag3SbS4 0.15 (odd, likely surrogate noise), CuAg2SbSe4 0.85 hull 0, Cu2AgPSe4 1.93 hull 0, CuAg2PS4 2.42, Ag3AsSe4 0.21, Cu(Ag)SbS4 0.46-0.47. Gap trends noisy between Sb/As.

## [reflection] iteration 2 — 2026-10-12 07:42 UTC

Pnictide chalcopyrite route failed (Sb gaps too small; P ones filtered by SMACT). I3-V-VI4 Cu/Ag-As/Sb chalcogenides on kesterite-type lattice succeeded: 3 novel hits (Ag3SbSe4, CuAg2AsS4, Cu2AgAsS4), all near-stable. Next: extend family — Cu3AsSe4-Ag variants (Cu2AgAsSe4, CuAg2AsSe4 not evaluated), Cu2AgSbSe4, Cu2AgPS4-like, Cu-Ag-As-S/Se mixes, Na/K-substituted; and Cu-Bi-Te variants (hull 0.052 marginal). Caveat: Ag3SbS4 0.15 vs Ag3SbSe4 1.26 is non-monotonic, gaps from the surrogate may be unreliable; compounds are of enargite/famatinite-type and real-world polymorph issues (these exist as known Cu3AsS4 enargite) might make kesterite-type ehull optimistic.

## [hypothesis] iteration 3 — 2026-10-12 07:43 UTC

Iter 3: extend I3-V-VI4 (Cu/Ag/Na-As/Sb/Bi/P-S/Se) on kesterite proto. Cu->Ag raises gap, Se lowers vs S, As/Sb intermediate. Target Cu2AgAsSe4, CuAg2AsSe4, Cu2AgSbSe4, Cu2AgSbS4, Cu2AgBiS4/Se4, Ag3BiS4, Ag3AsS4, Cu3PS4-types, Cu3AsSe4 (known probably). Exploit hits from iter 2; literature search returned nothing useful.

## [observation] iteration 3 — 2026-10-12 07:44 UTC

Iter 3: I3-V-VI4 and I-V-VI2 families were all 'already considered' (only KSbTe2, KBiTe2, KAsS2 novel). Pivoted to AE-Zr/Ti-(Cu/Ag)2-Q4 kesterite-type. 20 evaluated, all novel. Zr/Ti compounds unstable (ehull 0.09-0.24) in kesterite lattice though several gaps in window (BaZr(CuS2)2 1.16, SrZr(AgS2)2 1.61, CaZr(CuSe2)2 1.31) - fails stability. Stable: SrAg2GeS4 ehull 0.017 gap 1.95 (too wide); SrAg2GeSe4 ehull 0.035 gap 0.15 (too small; surrogate Se-Ge-Ag gaps suspiciously low). CaAg2Ge/Cu variants hull 0.06-0.11. KSbTe2 0.054, gap 0.36; KAsS2 hull 0.114. No hits this iteration.

## [reflection] iteration 3 — 2026-10-12 07:44 UTC

Hypothesis falsified: bulky AE + Zr/Ti on kesterite sites is energetically unfavorable (real BaCu2SnS4-type structures differ; Zr/Ti prefer octahedral). Stable ones are Ge-based with gap bracket 0.15 vs 1.95 for S vs Se — mixed S/Se (SrAg2Ge(S,Se)4) would land near 1.1-1.7 but tool does not support anion mixing. Next iter (4): try zincblende-derived or kesterite with Sr/Ba-Ag-Ge/Sn-S/Se where Sn replaces Ge (SrAg2SnS4 gap?), and Mg/Zn-Ag-Ge-S, expected gap ~1.4-1.7; also K/Na-Ag-Sb/Bi chalcogenides. Campaign leads remain Ag3SbSe4, CuAg2AsS4, Cu2AgAsS4, MgAg2SnSe4. Many family members flagged 'already considered' so move to unexplored ones.

## [hypothesis] iteration 4 — 2026-10-12 07:44 UTC

Iter 4: Go back to II-IV-Ag2/Cu2-Q4 kesterite members not yet tried: Ag2 with Zn/Cd/Mg/Sr/Ba + Sn (S), Cu2Mg/Sr/Ba Sn/Ge Se/S, and Ag2 Zn/Cd Ge S. Expect Sn-S Ag compounds ~1.3-1.7 (Sn lowers vs Ge; S wider than Se). Also Cu/Ag-Zn/Cd-Sn-S ordered variants and Mg-Cu-Sn-Se. Evaluate only novel ones.

## [observation] iteration 4 — 2026-10-12 07:45 UTC

Iter 4: 16 novel evaluated on kesterite proto. HIT: SrAg2SnS4 gap 1.667, ehull 0.024 (both in window, gap at upper edge). Marginal: CaAg2SnSe4 gap 1.454 but ehull 0.089 (unstable). SrAg2SnSe4 gap 0.34 hull 0.052; CaAg2SnS4 gap 0.52 hull 0.063 (surrogate gaps for Ag-Sn-Se/Ca look noisy). Na2-AE/Cd-Sn/Ge-Q4 are stable (hull 0.005-0.045; Na2CdGeS4 0.005, Na2CdSnSe4 0.011) but gaps 2.4-3.4 eV, too wide. Unspent: 4 relaxations (remaining novel candidates were wide-gap Na/AE members).

## [reflection] iteration 4 — 2026-10-12 07:45 UTC

Hypothesis partly held: Sr-Ag-Sn-S is a new near-stable candidate in window (SrAg2SnS4). Na2 family too wide-gap; Ca variants unstable. Lessons: Sr (large AE) pairs best with Ag-S on this lattice; gap ordering S>Se holds but surrogate gives noisy low gaps for some Ag-Se/Ca. Next (iter 5): look at neighbors of SrAg2SnS4 not yet tried, e.g. Cu analogs SrCu2SnS4 / BaCu2SnS4 (may be known), K/Na-Ag-Sb/Bi chalcogenides, and Ag-containing Sn/Ge sulfides with Mg/Zn; consider zincblende nitrides (ZnSnN2-like) as exploration. Priority: SrAg2SnS4 as campaign lead alongside Ag3SbSe4, CuAg2AsS4, Cu2AgAsS4, MgAg2SnSe4.

## [hypothesis] iteration 5 — 2026-10-12 07:45 UTC

Iter 5: Neighbors of SrAg2SnS4 lead: Ba/Sr/Mg/Zn/Cd + Ag2/Cu2 + Sn/Ge/Si + S/Se on kesterite lattice not yet tried (BaAg2SnS4, BaAg2GeS4, SrCu2SnS4, BaCu2SnS4, SrCu2GeS4, ZnAg2SnS4, MgAg2SnS4, CdAg2SnS4...). Large AE + Ag-S pair was best (iter 4); Sn lowers gap vs Ge, so Ba/Sr Ag Sn S and Sr Cu Ge/Sn S should sit 1.3-1.8. Also zincblende exploration: ZnSnN2-like/ZnGeN2 (gap dependent on ordering).

## [observation] iteration 5 — 2026-10-12 07:46 UTC

Iter 5: 19 novel evaluated. HITS: BaSi(AgSe2)2 gap 1.423 ehull 0.026 (best campaign hit, gap ~ideal); SrSi(AgSe2)2 gap 1.694 ehull 0.021 (window edge). Others: BaSi/SrSi(AgS2)2 stable (0.029/0.033) but gap ~2.55; Ba/Sr-Cu2-Si-S/Se hull 0.054-0.06 unstable; SrCu2SnSe4 hull 0.083 gap 0.1; CaSi(AgSe2)2 hull 0.061 gap 2.18; all Te analogs unstable (0.06-0.086) and gaps either <0.9 or >1.8. Zincblende proposals were all known/trivial, not evaluated.

## [reflection] iteration 5 — 2026-10-12 07:46 UTC

Hypothesis held: large AE (Sr, Ba) + Ag + group-IV + chalcogen are near-stable on kesterite-type lattice; Si-Se Ag compounds hit the gap window (S too wide, Te unstable, Ca too small). Campaign leads: BaSi(AgSe2)2 (1.42/0.026), SrAg2SnS4 (1.67/0.024), SrSi(AgSe2)2 (1.69/0.021), Ag3SbSe4 (1.26/0.0), CuAg2AsS4 (1.56/0.012), Cu2AgAsS4 (1.63/0.010), MgAg2SnSe4 (1.15/0.043). Caveats: CHGNet kesterite-type ehull is likely optimistic (real Ba/Sr-Ag-Si-Se probably adopt different structures, e.g. BaAg2GeS4-type), surrogate gaps noisy. Next steps beyond campaign: DFT check of competing polymorphs, mixed S/Se anion alloys of Ba-Si-Ag.
