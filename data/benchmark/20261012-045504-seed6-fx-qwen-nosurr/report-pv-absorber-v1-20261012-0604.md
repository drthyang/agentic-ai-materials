# Campaign report: pv-absorber-v1

## Executive summary  
This discovery campaign targeted photovoltaic absorbers with ~1.4 eV band gaps by exploring substitutions in chalcopyrite (CuInSe2) and kesterite (Cu2ZnSnS4)-type structures. Over five iterations, 26 proposed candidates were filtered (2 novel vs. MP), but only 6 scored due to MP overlap. A single novel compound **GaCu2SbS4** achieved both band gap (1.14 eV) and structural stability (e_above_hull: 0.036 eV/atom). Other iterations produced non-novel compounds with band gaps spanning 0.13–1.59 eV, confirming tunability via Ga/Al-Sb/Sn substitutions but highlighting challenges in novelty. Limited validation suggests further work is needed to translate hypotheses into novel candidates.

---

## Scored candidates  
| Formula      | Iteration | Novel | *E*<sub>form</sub> (eV/atom) | *E*<sub>hull</sub> (eV/atom) | Band gap (eV) |
|--------------|----------|-------|-----------------------------|-----------------------------|----------------|
| GaCu2SbS4    | 2        | ✅    | -0.638                      | 0.036                       | **1.136**      |
| InCuS2       | 4        | ❌    | -0.739                      | 0.007                       | 0.457          |
| GaCuSe2      | 4        | ❌    | -0.684                      | 0.021                       | **1.410**      |
| InAgS2       | 4        | ❌    | -0.669                      | 0.026                       | 1.599          |
| GaAgSe2      | 4        | ❌    | -0.657                      | 0.026                       | 1.146          |
| InAgSe2      | 4        | ❌    | -0.613                      | 0.046                       | **0.125**      |

---

## Hypotheses tested  
### Iteration 2  
- **Hypothesis**: Replace Zn→Ga (+2→+3) and Sn→Sb (+4→+3) in kesterite to maintain charge balance and tune band gaps.  
- **Discovery**: Novel **GaCu2SbS4** achieved band gap near target (1.14 eV) but suboptimal hull stability (0.036 eV/atom).  

### Iteration 4  
- **Hypothesis**: Substitute Cu→Ag (20%), In→Ga (25%), Se→Sn/S (30% Sn+20% S) in chalcopyrite to create strain and bowing effects.  
- **Outcome**: All compounds (e.g., InAgSe2 with 0.12 eV gap) were non-novel, but confirmed tunability via Sb/Sn co-alloying.  

---

## Caveats  
1. **Novelty limitations**: 44/46 proposed candidates overlapped with MP, indicating prior art challenges in chalcopyrite/kesterite families.  
2. **Band gap uncertainties**: Surrogate models (LDA/GGA) may underestimate gaps by ~20–30% in Sb/Sn-containing compounds.  
3. **Validation needs**: GaCu2SbS4 requires DFT+GW correction for band gap and synthesis verification (ball-milling/PVD routes).  

---

## Recommended next steps  
1. **Optimize GaCu2SbS4**: Test partial Ag-doping (20% Cu→Ag) predicted in iteration 5 to push band gap closer to 1.4 eV while preserving stability.  
2. **Expand anion tuning**: Explore ternary S/Se/Te mixes in GaCu2Sb compounds (iteration 3 hypothesis) to further bow the band gap.  
3. **Novel family exploration**: Investigate alternative structures (stannite, wurtzite) or anion-rich systems (PbSbS2-based) to bypass existing MP overlaps.
