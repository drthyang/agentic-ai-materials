# Lab Notebook

## [hypothesis] iteration 1 — 2026-10-10 22:37 UTC

Kesterite CZTS family (gap ~1.5 eV for CZTS, 1.0 for CZTSe). Isoelectronic substitution: Zn->Cd/Mg, Sn->Ge/Si, Cu->Ag, S/Se mixing should tune gap into 1.1-1.7 eV, with less-explored combos (Ag2CdSnS4-like, Cu2MgSnS4, Cu2CdGeS4 ...) being novel. Also chalcopyrite variants (Cu/Ag-Ga/In-S/Se/Te) with Ag/Al mixes.

## [observation] iteration 1 — 2026-10-10 22:44 UTC

Evaluated 14 novel kesterite-type quaternaries. Hits (gap 1.1-1.7, ehull<=0.05): CdAg2GeSe4 (ehull 0.000, gap 1.28), ZnAg2GeSe4 (0.000, 1.12), MgAg2SnSe4 (0.016, 1.59). Stable but gap too wide: MgAg2GeSe4 1.86, MgAg2GeS4 1.89, MgAg2SnS4 1.87, MgCu2SnS4 2.17. Si-containing all unstable (ehull 0.13-0.17), Si too small for the Sn site. MgCu2SnSe4 gap 1.38 but ehull 0.071 (just outside); MgCu2GeSe4 ehull 0.136. Chalcopyrite substitutions all already known in MP; not evaluated. Used 14/20 budget; no more novel candidates in the generated pool.

## [reflection] iteration 1 — 2026-10-10 22:44 UTC

Hypothesis largely held: Ag-based selenide kesterite-type compounds with Ge/Sn on the tetravalent site give stable, ~1.1-1.6 eV gaps. Gap trend S>Se by ~0.3-0.6 eV, Mg>Cd>Zn widening. Si fails on stability. Caveats: CHGNet ehull and ML gap, structure type (kesterite vs stannite/wurtzite-derived) may differ from true ground state; need verification. Next: explore mixed S/Se Ag compounds (e.g., CdAg2Ge(S,Se)4), Cd/Mg-Ag-Sn-Se, and other prototypes beyond the pool.
