# Campaign report: pv-absorber-v1

## Executive summary

Over five iterations I relaxed and scored 96 candidates, all novel versus Materials Project, almost all kesterite-type I2-II-IV-VI4 compounds. Five are near-stable (E_hull ≤ 0.043 eV/atom) with computed gaps inside the ~1.1–1.7 eV window the notebook worked toward: **BaSi(AgSe2)2** (1.42 eV, E_hull 0.026), **SrAg2SnS4** (1.67, 0.024), **SrSi(AgSe2)2** (1.69, 0.021), **MgSi(AgTe2)2** (1.63, 0.014) and **MgAg2SnSe4** (1.15, 0.043, borderline). Confidence is low to moderate. The gaps are DFT-level values that the notebook expects to be underestimated for narrow-gap members. The kesterite structure was assumed from the prototype and is not verified as the ground state, particularly for Sr/Ba. Nothing has been checked with higher-level calculations or synthesis. Several tested routes were clearly falsified (Zr/Ti, Te, Ca, open-shell 3d metals, alkali), so the positive findings come from one narrow region of chemical space, Ag with Mg/Sr/Ba and Si/Sn.

## Scored candidates

The window of ~1.1–1.7 eV is the one used in the notebook's reasoning. The explicit target specification is not part of the data I was given. Formation energy and E_hull are in eV/atom, and the gap is in eV.

| Iter | Formula | E_form | E_hull | Gap |
|---|---|---|---|---|
| 1 | CdAg2GeSe4 | -0.551 | 0.000 | 0.03 |
| 1 | CdSi(AgSe2)2 | -0.599 | 0.000 | 0.75 |
| 1 | CdSi(AgS2)2 | -0.721 | 0.000 | 2.22 |
| 1 | ZnAg2GeSe4 | -0.567 | 0.003 | 0.68 |
| 1 | MgAg2GeS4 | -0.798 | 0.006 | 1.78 |
| 1 | CdSi(AgTe2)2 | -0.344 | 0.008 | 0.33 |
| 1 | MgSi(AgSe2)2 | -0.739 | 0.011 | 1.84 |
| 1 | MgSi(AgS2)2 | -0.908 | 0.012 | 2.46 |
| 1 | CdAg2GeTe4 | -0.375 | 0.014 | 0.17 |
| 1 | MgSi(AgTe2)2 | -0.447 | 0.014 | 1.63 |
| 1 | MgAg2GeTe4 | -0.479 | 0.015 | 0.87 |
| 1 | MgCu2GeTe4 | -0.502 | 0.017 | 0.52 |
| 1 | MgAg2GeSe4 | -0.690 | 0.018 | 0.28 |
| 1 | MgCu2SnTe4 | -0.537 | 0.026 | 0.35 |
| 1 | MgCu2GeSe4 | -0.713 | 0.030 | 0.31 |
| 1 | MgCu2SiTe4 | -0.461 | 0.034 | 0.24 |
| 2 | ZnSi(AgSe2)2 | -0.614 | 0.000 | 1.84 |
| 2 | MgAg2SnS4 | -0.788 | 0.011 | 0.69 |
| 2 | TiZn(AgSe2)2 | -0.847 | 0.014 | 1.89 |
| 2 | MgCu2SnS4 | -0.866 | 0.014 | 0.49 |
| 2 | MgAg2SnSe4 | -0.700 | 0.043 | 1.15 |
| 2 | MgCu2SnSe4 | -0.734 | 0.047 | 0.19 |
| 2 | TiZn(CuS2)2 | -0.996 | 0.055 | 2.15 |
| 2 | ZrZn(CuS2)2 | -1.020 | 0.065 | 1.12 |
| 2 | ZrCd(CuS2)2 | -0.971 | 0.069 | 1.99 |
| 2 | MgTi(CuSe2)2 | -0.931 | 0.080 | 2.62 |
| 2 | ZrZn(AgSe2)2 | -0.853 | 0.080 | 1.33 |
| 2 | ZrCd(AgSe2)2 | -0.822 | 0.088 | 0.01 |
| 2 | MgZr(CuS2)2 | -1.147 | 0.093 | 1.14 |
| 2 | ZrCd(AgS2)2 | -0.920 | 0.097 | 1.88 |
| 2 | ZrZn(CuSe2)2 | -0.849 | 0.098 | 1.63 |
| 2 | ZrZn(AgS2)2 | -0.957 | 0.106 | 1.22 |
| 2 | MgZr(AgSe2)2 | -0.950 | 0.119 | 0.12 |
| 2 | ZrCd(CuSe2)2 | -0.801 | 0.127 | 1.27 |
| 2 | MgZr(CuSe2)2 | -0.939 | 0.144 | 1.54 |
| 2 | CaZr(CuSe2)2 | -1.035 | 0.244 | 1.31 |
| 3 | MnCu2GeSe4 | -0.525 | 0.000 | 0.66 |
| 3 | MgAg2SnTe4 | -0.530 | 0.014 | 0.19 |
| 3 | CdAg2SnTe4 | -0.425 | 0.015 | 0.03 |
| 3 | ZnAg2SnTe4 | -0.424 | 0.019 | 0.44 |
| 3 | SrSi(AgSe2)2 | -0.932 | 0.021 | 1.69 |
| 3 | BaSi(AgSe2)2 | -0.965 | 0.026 | 1.42 |
| 3 | SrAg2GeSe4 | -0.879 | 0.035 | 0.15 |
| 3 | MgTi(AgTe2)2 | -0.677 | 0.048 | 0.21 |
| 3 | TiCd(AgTe2)2 | -0.572 | 0.048 | 0.09 |
| 3 | TiZn(AgTe2)2 | -0.573 | 0.051 | 0.06 |
| 3 | SrAg2SnSe4 | -0.896 | 0.052 | 0.34 |
| 3 | BaCu2SiSe4 | -0.952 | 0.054 | 1.81 |
| 3 | SrCu2SiSe4 | -0.913 | 0.055 | 1.74 |
| 3 | CaSi(AgSe2)2 | -0.883 | 0.061 | 2.18 |
| 3 | CaAg2GeSe4 | -0.833 | 0.068 | 0.26 |
| 3 | SrCu2SnSe4 | -0.902 | 0.083 | 0.10 |
| 3 | CaAg2SnSe4 | -0.851 | 0.089 | 1.45 |
| 3 | CaCu2SiSe4 | -0.868 | 0.091 | 2.15 |
| 3 | CaCu2GeSe4 | -0.829 | 0.110 | 0.30 |
| 3 | CaCu2SnSe4 | -0.860 | 0.117 | 0.21 |
| 4 | SrAg2GeS4 | -0.971 | 0.017 | 1.95 |
| 4 | MnAg2GeS4 | -0.593 | 0.021 | 0.25 |
| 4 | SrAg2SnS4 | -0.961 | 0.024 | 1.67 |
| 4 | BaSi(AgS2)2 | -1.106 | 0.029 | 2.57 |
| 4 | NiAg2GeSe4 | -0.443 | 0.031 | 0.31 |
| 4 | SrSi(AgS2)2 | -1.083 | 0.033 | 2.54 |
| 4 | NiAg2SnS4 | -0.514 | 0.034 | 1.77 |
| 4 | NiAg2SnSe4 | -0.463 | 0.049 | 0.64 |
| 4 | MnSi(AgS2)2 | -0.686 | 0.052 | 0.09 |
| 4 | SrCu2SiS4 | -1.103 | 0.058 | 3.17 |
| 4 | CaAg2GeS4 | -0.928 | 0.060 | 1.75 |
| 4 | BaCu2SiS4 | -1.119 | 0.060 | 3.13 |
| 4 | CaAg2SnS4 | -0.922 | 0.063 | 0.52 |
| 4 | CaSi(AgS2)2 | -1.039 | 0.067 | 2.27 |
| 4 | CoAg2SnS4 | -0.504 | 0.069 | 0.48 |
| 4 | CoAg2SnSe4 | -0.441 | 0.074 | 0.23 |
| 4 | FeAg2GeSe4 | -0.419 | 0.075 | 0.15 |
| 4 | CoAg2GeS4 | -0.491 | 0.078 | 0.60 |
| 4 | FeAg2SnSe4 | -0.447 | 0.095 | 0.06 |
| 4 | FeAg2GeS4 | -0.501 | 0.106 | 0.29 |
| 5 | Na2CdSiSe4 | -1.028 | 0.007 | 3.10 |
| 5 | Na2CdGeSe4 | -0.961 | 0.010 | 2.44 |
| 5 | Na2CdSnSe4 | -0.983 | 0.011 | 3.14 |
| 5 | Na2ZnSiSe4 | -1.039 | 0.020 | 3.44 |
| 5 | Na2ZnSnS4 | -1.075 | 0.025 | 3.39 |
| 5 | Na2ZnGeSe4 | -0.969 | 0.026 | 2.85 |
| 5 | Na2ZnSnSe4 | -0.990 | 0.028 | 2.84 |
| 5 | Na2MgSnS4 | -1.222 | 0.031 | 3.28 |
| 5 | K2CdGeSe4 | -1.020 | 0.033 | 2.64 |
| 5 | Na2MgSnSe4 | -1.110 | 0.044 | 3.00 |
| 5 | K2ZnSnSe4 | -1.046 | 0.050 | 2.22 |
| 5 | K2ZnGeSe4 | -1.023 | 0.054 | 2.68 |
| 5 | BaNa2SnSe4 | -1.314 | 0.055 | 2.53 |
| 5 | BaNa2GeSe4 | -1.290 | 0.056 | 2.62 |
| 5 | K2MgSnSe4 | -1.167 | 0.064 | 2.19 |
| 5 | K2BaSnSe4 | -1.368 | 0.066 | 2.16 |
| 5 | Na2SrSnSe4 | -1.291 | 0.067 | 2.82 |
| 5 | K2ZnSnS4 | -1.111 | 0.069 | 3.28 |
| 5 | K2MgGeSe4 | -1.140 | 0.072 | 2.68 |
| 5 | Na2SrGeSe4 | -1.261 | 0.074 | 2.89 |

All 96 candidates converged and were flagged novel.

### Best candidates (gap ~1.1–1.7 eV, E_hull ≤ ~0.045)

| Formula | Gap (eV) | E_hull (eV/atom) | Comment |
|---|---|---|---|
| BaSi(AgSe2)2 | 1.42 | 0.026 | Best match to the ~1.4 eV target. |
| SrAg2SnS4 | 1.67 | 0.024 | Near the upper edge of the window. |
| SrSi(AgSe2)2 | 1.69 | 0.021 | Near the upper edge of the window. |
| MgSi(AgTe2)2 | 1.63 | 0.014 | Most stable of the five. |
| MgAg2SnSe4 | 1.15 | 0.043 | Borderline stability. |

Some compounds have gaps in the window but are too unstable to count as hits: CaAg2SnSe4 (1.45 eV, E_hull 0.089) and ZrZn(AgSe2)2 (1.33, 0.080), among others.

## Hypotheses tested and what was learned

The notebook has no hypothesis entry for iteration 2; the entry for that iteration contains only an observation and a reflection.

**Iteration 1: Cu/Ag–(Zn,Cd,Mg)–(Sn,Ge,Si)–(S,Se,Te) kesterites.**
- 16 novel candidates were evaluated, all with E_hull between 0 and 0.034 eV/atom.
- Gaps follow clear trends: Te < Se < S, Cd < Mg, Sn < Ge < Si, and Ag > Cu.
- The only in-window result was MgSi(AgTe2)2. The run left 4 relaxations unused because the filtered pool had no more novel members.

**Iteration 2: chalcopyrite check and Zr/Ti-for-Sn kesterites.**
- All 17 chalcopyrite candidates were already in Materials Project, so none were evaluated.
- The leftover Sn/Si/Mg kesterites gave MgAg2SnSe4 as a borderline hit.
- 15 Zr/Ti kesterites were evaluated. Several have gaps in the 1.1–1.7 eV range, but Zr compounds have E_hull of 0.065–0.244 eV/atom, which the notebook attributes to Zr preferring octahedral coordination. Zr-based stable absorbers are falsified. TiZn(AgSe2)2 is stable (0.014) but its gap is 1.89 eV, too wide.

**Iteration 3: Te–Ag–Sn/Ti kesterites, then alkaline-earth and Mn on the divalent site.**
- Te–Ag–Sn/Ti kesterites are stable (E_hull 0.014–0.051) but have gaps of 0.03–0.44 eV, too small. The Te route is falsified for this purpose.
- Ca, and large cations with Cu, destabilize the kesterite. For Ag and Si, the gap falls as the cation grows (Ca 2.18, Sr 1.69, Ba 1.42 eV) while the compounds stay near-stable.
- This produced BaSi(AgSe2)2 and SrSi(AgSe2)2.
- MnCu2GeSe4 is on the hull (E_hull 0.000) but has a gap of only 0.66 eV.

**Iteration 4: Ba/Sr and Ca/Mn/Fe/Co/Ni on the divalent site with S/Se.**
- SrAg2SnS4 landed at the upper window edge (1.67 eV).
- The Ba/Sr silicon sulfides (2.54–3.17 eV) are too wide.
- The Fe/Co/Mn compounds have small gaps (0.06–0.60 eV) and are mostly unstable, and the notebook treats these as likely spurious open-shell DFT artifacts.
- Ca is unstable (E_hull 0.060–0.067 for the sulfides).

**Iteration 5: Na/K on the monovalent site.**
- Removing Cu/Ag d states pushes gaps to 2.16–3.44 eV, none in the window, even though the Na compounds are quite stable (E_hull down to 0.007). The hypothesis is falsified for gap.

## Caveats

- **Gap accuracy.** The notebook describes the gaps as DFT-level, likely underestimated for narrow-gap members, and I have no error bars for them. Candidates near the window edges (1.67, 1.69, 1.15 eV) could fall outside it.
- **Open-shell metals.** Fe/Co/Mn/Ni gaps are likely spurious.
- **Structure.** All candidates are assumed to be kesterite-type. The notebook flags that Sr/Ba-containing members may adopt other structures. E_hull is measured against the existing hull, but competing structure types were not searched, so the near-stable results may not reflect the true ground state.
- **Novelty.** This means absence from Materials Project only, not from the wider literature.
- **No optical-absorption data.** Direct versus indirect gap, absorption strength, defect tolerance and band alignment were not examined.
- **Experimental validation.** There is none; no synthesis was attempted.
- **Candidate-level validation needed.** Each top candidate needs:
  - a structure search (including non-kesterite polymorphs and ordering variants),
  - phonon and decomposition-path checks,
  - hybrid-functional (HSE-type) or GW gaps with the absorption spectrum,
  - defect and doping calculations, and only then synthesis tests.

## Recommended next steps

1. Run structure-prediction and competing-phase checks on BaSi(AgSe2)2, SrSi(AgSe2)2, SrAg2SnS4, MgSi(AgTe2)2 and MgAg2SnSe4.
2. Recompute gaps for these five with a higher-level method.
3. Avoid the falsified routes: Zr kesterites, Te–Sn/Ti, Ca, Fe/Co/Mn, Cu with Ba/Sr Si sulfides, and pure Na/K compounds.
4. The notebook suggests alloying Na/K with Ag, or mixing cations or anions between discrete members, to interpolate between the ~0.3–1.8 eV Ag compounds and the 2.2+ eV alkali compounds. The prototype tool cannot generate mixed-site compounds, so this needs other tooling.
5. The notebook's iteration 4 reflection indicated that the Cu/Ag Ba/Sr kesterite space was nearly exhausted, and iteration 5 recorded the proposal tool treating further candidates as already considered. New families (or the non-kesterite structure types mentioned above) will probably be needed for further discoveries.
