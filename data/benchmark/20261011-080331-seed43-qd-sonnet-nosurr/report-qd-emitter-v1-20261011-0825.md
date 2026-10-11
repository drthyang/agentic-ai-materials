# Campaign report: qd-emitter-v1

## Executive summary

Over five iterations the campaign scored 77 candidates, and 76 of them were novel relative to the Materials Project. The one known compound, Cu3PS4, was a deliberate calibration point. The target window is not stated explicitly in the data. The notebook screened for a gap of roughly 1.8–3.1 eV, with about 2.4 eV treated as ideal, and for Ehull ≤ 0.05 eV/atom. Eleven novel compounds met both criteria. The closest to ideal were **CuAg2PS4** (Ehull 0.020, gap 2.45 eV), **Ag2AlGaS4** (0.000, 2.37 eV) and **BaSnO2** (0.000, 2.26 eV). All gaps and stabilities come from a surrogate pipeline (CHGNet relaxation plus an ML "HSE-fidelity" gap), and nothing has been checked with DFT or experiment. Confidence is therefore low to moderate. The BaSnO2 and SrSnS2 results carry an extra caveat because they contain Sn(II). The iteration-5 notebook entry also flags that many hits are Cu/Ag chalcogenides, which may be poor blue/green quantum-dot emitters.

## Scored candidates

Columns: Ef = formation energy (eV/atom), Ehull = energy above hull (eV/atom), Eg = ML band gap (eV). Every candidate is novel except Cu3PS4, which is marked as known.

### Iteration 1: kesterite-type I2-II-IV-VI4 (sulfides and selenides)

| Formula | Ef | Ehull | Eg |
|---|---|---|---|
| ZnAg2GeSe4 | -0.68 | 0.000 | 1.12 |
| SrAg2SnS4 | -1.37 | 0.000 | 1.72 |
| MgAg2SnS4 | -1.18 | 0.002 | 1.87 |
| SrAg2GeSe4 | -1.02 | 0.003 | 1.69 |
| SrAg2GeS4 | -1.35 | 0.013 | 1.87 |
| MgAg2SnSe4 | -0.84 | 0.016 | 1.59 |
| MgAg2GeS4 | -1.17 | 0.017 | 1.89 |
| MgCu2SnS4 | -1.24 | 0.020 | 2.17 |
| MgAg2GeSe4 | -0.80 | 0.020 | 1.86 |
| CaAg2SnS4 | -1.30 | 0.068 | 2.28 |
| MgCu2SnSe4 | -0.82 | 0.071 | 1.38 |
| CaCu2SnS4 | -1.37 | 0.072 | 2.70 |
| CaAg2GeS4 | -1.27 | 0.094 | 2.15 |
| CaCu2GeS4 | -1.34 | 0.096 | 2.56 |
| MgCu2GeSe4 | -0.72 | 0.136 | 1.10 |
| MgSi(AgSe2)2 | -0.71 | 0.145 | 2.35 |
| SrCu2SiS4 | -1.37 | 0.167 | 2.97 |
| MgSi(AgS2)2 | -1.13 | 0.167 | 2.54 |
| ZnSi(AgSe2)2 | -0.55 | 0.170 | 1.90 |
| CaSi(AgS2)2 | -1.27 | 0.216 | 2.82 |

### Iteration 2: kesterite-type tellurides, one selenide and oxides

| Formula | Ef | Ehull | Eg |
|---|---|---|---|
| SrCu2SnTe4 | -0.75 | 0.000 | 0.84 |
| BaAg2GeTe4 | -0.70 | 0.000 | 0.70 |
| BaCu2SnTe4 | -0.75 | 0.001 | 0.39 |
| SrAg2GeTe4 | -0.65 | 0.016 | 0.16 |
| MgAg2GeTe4 | -0.42 | 0.025 | 1.49 |
| ZnAg2GeTe4 | -0.32 | 0.028 | 1.17 |
| BaCu2GeTe4 | -0.67 | 0.034 | 0.50 |
| MgAg2SnTe4 | -0.46 | 0.038 | 1.17 |
| SrCu2SnSe4 | -1.04 | 0.050 | 1.11 |
| SrCu2GeTe4 | -0.61 | 0.078 | 0.16 |
| MgCu2GeTe4 | -0.37 | 0.101 | 0.90 |
| MgCu2SnTe4 | -0.41 | 0.109 | 0.48 |
| MgCu2GeO4 | -1.42 | 0.120 | 2.57 |
| MgAg2GeO4 | -1.17 | 0.248 | 2.94 |
| ZnAg2SnO4 | -0.80 | 0.263 | 0.02 |
| BaCu2GeO4 | -1.33 | 0.297 | 2.60 |
| SrCu2GeO4 | -1.36 | 0.301 | 3.51 |
| MgAg2SnO4 | -1.08 | 0.305 | 2.08 |
| BaAg2GeO4 | -1.20 | 0.311 | 1.69 |
| SrAg2GeO4 | -1.18 | 0.364 | 2.98 |

### Iteration 3: ABX2 Sn(II) compounds and ZAIS-like ordered alloys

| Formula | Ef | Ehull | Eg |
|---|---|---|---|
| CaSnSe2 | -1.69 | 0.000 | 0.17 |
| SrSnSe2 | -1.77 | 0.000 | 0.18 |
| BaSnSe2 | -1.81 | 0.000 | 0.23 |
| SrSnO2 | -2.36 | 0.000 | 3.13 |
| BaSnO2 | -2.35 | 0.000 | 2.26 |
| SrSnS2 | -1.93 | 0.045 | 2.14 |
| CaSnS2 | -1.92 | 0.059 | 1.48 |
| Mg2InCuS4 | -1.47 | 0.119 | 1.79 |
| ZnSnS2 | -1.18 | 0.122 | 2.53 |
| Mg2InAgS4 | -1.44 | 0.131 | 1.42 |
| Zn2InAgS4 | -1.11 | 0.145 | 1.71 |
| MgSnS2 | -1.40 | 0.208 | 2.46 |
| Mg2GaCuS4 | -1.42 | 0.224 | 2.88 |
| Mg2GaAgS4 | -1.37 | 0.234 | 2.85 |
| Zn2GaAgS4 | -1.06 | 0.239 | 2.96 |
| Zn2GaCuS4 | -1.03 | 0.305 | 2.14 |
| AlZn2CuS4 | -1.14 | 0.315 | 2.56 |
| AlZn2AgS4 | -1.10 | 0.328 | 2.94 |
| Mg2AlAgS4 | -1.35 | 0.385 | 3.24 |
| Mg2AlCuS4 | -1.24 | 0.516 | 3.48 |

### Iteration 4: Cu3PS4-type compounds and ordered III/III' alloys

| Formula | Ef | Ehull | Eg |
|---|---|---|---|
| CuAg2PSe4 | -0.48 | 0.000 | 2.15 |
| Cu3PS4 (known; calibration) | -0.92 | 0.000 | 1.88 |
| AlGa(AgS2)2 = Ag2AlGaS4 | -1.45 | 0.000 | 2.37 |
| CuAg2PS4 | -0.83 | 0.020 | 2.45 |
| Cu2AgPSe4 | -0.42 | 0.045 | 2.14 |
| InGa(CuS2)2 | -1.08 | 0.093 | 2.00 |
| AlGa(AgSe2)2 | -0.76 | 0.132 | 1.87 |
| AlZn2AgSe4 | -0.74 | 0.274 | 1.67 |

### Iteration 5: isovalent Zn/Mg ordered chalcogenides and telluride probes

| Formula | Ef | Ehull | Eg |
|---|---|---|---|
| Mg3ZnS4 | -1.94 | 0.000 | 3.39 |
| MgZn3Te4 | -0.61 | 0.119 | 1.22 |
| MgZnTe2 | -0.70 | 0.131 | 2.27 |
| AlGa(AgTe2)2 | -0.36 | 0.139 | 0.92 |
| AlGa(CuTe2)2 | -0.31 | 0.182 | 0.10 |
| MgZn3Se4 | -0.97 | 0.210 | 1.47 |
| MgZnSe2 | -1.09 | 0.223 | 1.95 |
| Mg3ZnTe4 | -0.66 | 0.270 | 2.40 |
| Mg3ZnSe4 | -1.04 | 0.414 | 2.93 |

### Best hits (novel, Ehull ≤ 0.05, gap in the roughly 1.8–3.1 eV window)

| Formula | Ehull | Eg | Note |
|---|---|---|---|
| CuAg2PS4 | 0.020 | 2.45 | Closest to the 2.4 eV ideal |
| Ag2AlGaS4 | 0.000 | 2.37 | |
| BaSnO2 | 0.000 | 2.26 | Sn(II) caveat |
| MgCu2SnS4 | 0.020 | 2.17 | |
| CuAg2PSe4 | 0.000 | 2.15 | |
| SrSnS2 | 0.045 | 2.14 | Sn(II) caveat |
| Cu2AgPSe4 | 0.045 | 2.14 | |
| MgAg2GeS4 | 0.017 | 1.89 | |
| MgAg2SnS4 | 0.002 | 1.87 | |
| SrAg2GeS4 | 0.013 | 1.87 | |
| MgAg2GeSe4 | 0.020 | 1.86 | |

Near misses on gap:
- Mg3ZnS4: stable but 3.39 eV, above the window.
- SrSnO2: stable but 3.13 eV, just above the window.
- SrAg2SnS4: stable but 1.72 eV, just below the window.

## Hypotheses tested and what was learned

**Iteration 1: kesterite-type I2-II-IV-VI4 with Mg/Sr/Ca/Zn, Ag/Cu, Si/Ge/Sn and S/Se.**
- Chalcopyrite I-III-VI2 combinations were all already in the Materials Project, so none were evaluated.
- Mg and Sr stabilised the structure. Ca (Ehull 0.07–0.10) and Si (0.15–0.22) destabilised it.
- Gaps were somewhat low. The observed trend was that Ag, Sn and Se lower the gap, while Cu and S raise it.
- The critic wrongly vetoed SrSi(AgS2)2 as charge-imbalanced, but it is balanced.
- Partly confirmed.

**Iteration 2: tellurides, SrCu2SnSe4 and oxides in the kesterite structure.**
- The zincblende and chalcopyrite pnictide routes gave only known compounds or SMACT rejections, with phosphides rejected, so they were a dead end.
- Several tellurides are stable (SrCu2SnTe4, BaCu2SnTe4, BaAg2GeTe4 and others near the hull), but all have gaps of 0.15–1.5 eV, below the window.
- Oxide kesterites have gaps in the window for several members (MgCu2GeO4 2.57, MgAg2SnO4 2.08, BaCu2GeO4 2.60). All are unstable, with Ehull 0.12–0.36, so the tetrahedral oxide kesterite looks like the wrong structure.
- The gap trend by anion is O > S > Se > Te, and stability runs roughly the other way. The window therefore sits at sulfides.
- No hits.

**Iteration 3: II-IV-VI2 / Sn(II) ABX2 compounds and ZAIS-like ordered alloys.**
- Sn(II) with a large alkaline earth works: BaSnO2 (0.000, 2.26) and SrSnS2 (0.045, 2.14) are hits.
- The selenides are stable but have gaps of only 0.17–0.23 eV.
- ZnSnS2 and MgSnS2 are unstable (Ehull 0.12 and 0.21).
- All 11 ordered Zn/Mg-(Cu/Ag)-(Al/Ga/In)-S4 alloys are unstable (Ehull 0.12–0.52), so that hypothesis is falsified.
- Caveat recorded in the notebook: the ML gaps for Sn(II) compounds may be unreliable because of the lone pair, and disproportionation is possible. The ABO2 "chalcopyrite" prototype may also be structurally unrealistic, even though the hull calculation says stable.

**Iteration 4: Cu3PS4-type and ordered III/III' alloys, found by counting cation charges.**
- The kesterite has four cation sites summing to +8. I+I+I+V (with P) and I+I+III+III' give new charge-balanced sets.
- Hits are CuAg2PS4, CuAg2PSe4, Cu2AgPSe4 and Ag2AlGaS4.
- The Cu3PS4 calibration gives a plausible gap (1.88 eV) and Ehull of 0.
- The Se/Te and Zn-containing alloys are unstable (Ehull 0.09–0.27).
- The critic correctly vetoed charge-imbalanced Cu+Ag-Ge formulas.
- Only 8 candidates were scored, and the notebook records 12 budget units left unspent because no further novel balanced candidates were available.

**Iteration 5: isovalent Zn/Mg ordered chalcogenides.**
- The prototype library was by then exhausted. Re-proposals returned "already considered" or SMACT rejections.
- Mg3ZnS4 is stable (Ehull 0.000) but its 3.39 eV gap is too wide.
- All Se and Te members are unstable (Ehull 0.12–0.41), even where their gaps fall in the window (for example MgZnTe2 at 2.27 and Mg3ZnTe4 at 2.40).
- The AlGa(CuTe2)2 and AlGa(AgTe2)2 probes are unstable and have low gaps.
- Falsified for Se/Te and only partly confirmed for S.

## Caveats

- **Surrogate errors.** Energies come from CHGNet relaxation and gaps from an ML model with HSE-level fidelity. No error bars were quantified in this campaign. Ehull values of 0.02–0.05 are within plausible model error, so "stable" means only "near the computed hull".
- **Idealised prototypes.** Structures are element substitutions on three prototypes (chalcopyrite, kesterite, zincblende). The real ground-state polymorphs, such as Pn21 versus I-4 for Cu3PS4-type compounds, were not searched. Competing phases are limited to what is in the Materials Project.
- **Sn(II) compounds.** BaSnO2 and SrSnS2 depend on a gap proxy that may be unreliable for lone-pair cations. Disproportionation was not tested.
- **Application fit.** Many hits are Cu/Ag chalcogenides with covalent d-states. The notebook flags these as not ideal for blue/green quantum-dot emitters, with possible poor photoluminescence quantum yield. Nothing in this campaign tests emission properties.
- **Data limits.** Iteration 4 scored only 8 candidates and iteration 5 scored 9. Iterations 1–3 each scored 20, a cap that may have limited coverage.
- **Missing validation.** No DFT beyond the surrogate, no phonon or dynamical-stability checks, no defect or doping analysis, and no synthesis was done.

## Recommended next steps

1. Run hybrid-functional DFT for the top hits (CuAg2PS4, Ag2AlGaS4, CuAg2PSe4, BaSnO2, SrSnS2, MgCu2SnS4, MgAg2SnS4, MgAg2GeS4). Include an explicit polymorph search and phonon calculations.
2. Check competing phases for the Sn(II) compounds, such as SnO2 or Sn disproportionation products, and test the gaps with a more reliable method.
3. Assess the likely emission of the Cu/Ag-based hits, including defect levels, since these are the main risk for emitter use.
4. Extend the prototype library to wurtzite-derived and non-tetrahedral structures. Substitution on the current three prototypes is largely exhausted, and later iterations returned mostly already-considered or rejected candidates.
5. Treat the wide-gap stable near-misses (Mg3ZnS4, SrSnO2) as candidates for gap tuning. This would need alloying, which the current tool cannot represent, because it cannot mix sites or anions.
6. Avoid further work on Si- and Ca-containing kesterites, oxide kesterites, ordered Zn/Mg-Se/Te alloys and Zn/Mg-Al/Ga/In ZAIS-like alloys. All were unstable here.
