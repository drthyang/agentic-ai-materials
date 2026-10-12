# Campaign report: pv-absorber-v1

- **Executive summary**: This 5-iteration campaign aimed to discover novel photovoltaic absorber materials with 1.4 eV band gaps through isostructural substitution strategies. While all scored candidates (4 total) achieved formation energies below 0.1 eV/atom, band gaps fell short of the target (≤0.87 eV vs goal of 1.4 eV). Iteration 3's MgAg₂GeTe₄ demonstrated the highest band gap (0.87 eV) and energy above hull (0.015 eV), but no candidate met all discovery criteria. The kesterite-based hypothesis (Cu₂ZnSnS₄ derivatives) showed greater stability than chalcopyrite systems but insufficient band gap tuning.

| Formula         | convergence | *E*<sub>form</sub>/atom (eV) | *E*<sub>hull</sub> (eV) | band gap (eV) | novel |
|-----------------|-------------|-------------------------------|--------------------------|---------------|-------|
| CdAg₂GeSe₄      | 1           | -0.55                         | 0.0                      | 0.03          | 1     |
| CdAg₂SnTe₄      | 1           | -0.425                        | 0.015                     | 0.03          | 1     |
| MgCu₂GeSe₄      | 1           | -0.713                        | 0.03                      | 0.31          | 1     |
| MgAg₂GeTe₄      | 1           | -0.479                        | 0.015                     | 0.87          | 1     |

## Hypotheses tested

**Iteration 1:**  
- **Strategy**: Chalcopyrite → kesterite substitution cascade (Ag/Cd/Ge/Se) in Cu₂ZnSnS₄ prototype  
- **Target**: 1.4 eV at Ag₂CdGeSe₄ via Vegard's law extrapolation  
- **Outcome**: Both candidates exhibited indirect zero or near-zero band gaps (∼0.03 eV), invalidating the hypothesis  

**Iteration 3**:  
- **Strategy**: Dual cation/anion expansion in kesterite using Mg/Ge/Te substitutions  
- **Target**: 1.4 eV at Ag₂MgGeTe₄ via ionic radius complementarity  
- **Outcome**: MgAg₂GeTe₄ showed highest band gap (0.87 eV) but with 57% shortfall from target. Structural stability (ΔH=0.015 eV) suggests feasibility  

**Iteration 4**:  
- **Strategy**: Zincblende GaInSb with Al/Ga/As substitutions  
- **Outcome**: No candidates scored due to strict filtering of known materials in Ga-Sb systems  

## Caveats
- Surrogate model error bounds ±0.1 eV for band gaps prevent confirmation of <1.5 eV candidates  
- MgAg₂GeTe₄ requires DFT validation of electronic structure and experimental verification of Te-based kesterite phase stability  
- Cation disorder in kesterite systems (A₂BCD₄) may require *ab initio* ordered structure screening  

## Recommended next steps
1. **Alternative cation engineering**: Test Bi³+ partial substitution in MgAg₂GeTe₄ to p-dope valence band (based on 6p/5p orbital interactions)  
2. **Structural reparameterization**: Screen non-kesterite topologies (e.g., stannite/clinoclase) for better cation/anion size matching in Mg-Ge-Te system  
3. **Hybrid band gap approach**: Combine MgAg₂GeTe₄ with high-gap perovskites via heterojunction design to reach 1.4 eV effective gap
