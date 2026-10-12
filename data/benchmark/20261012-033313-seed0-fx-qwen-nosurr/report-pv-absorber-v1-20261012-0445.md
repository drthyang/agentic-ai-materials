# Campaign report: pv-absorber-v1

- **Executive summary**: This campaign explored 5 iterations of cation/anion substitutions in chalcopyrite/kesterite/zincblende frameworks for photovoltaic absorbers. Only two iterations produced novel candidates: ZnSnS₂ (band gap 0.9 eV) and CdSnS₂ (0.48 eV) in iteration 3. Most scored candidates were non-novel (7/7), and no compounds achieved the 1.4 eV target. Hypotheses about Cu/Ag-Ga/Al-Ge/S/Se/Te families showed mixed success, with limited experimental validation of the proposed chemical design rules.

| formula | iteration | converged | formation_energy_per_atom (eV) | e_above_hull (eV) | band_gap_ev (eV) | is_novel | hypothesis |
|--------|-----------|-----------|-------------------------------|-------------------|------------------|----------|------------|
| GaAgS₂ | 1 | 1 | -0.7427 | 0.0250 | 1.799 | 0 | Hypothesis: In→Ga/Al and Se→S substitutions in CuInSe₂ to tune band gap |
| CdSnS₂ | 3 | 1 | -0.7558 | 0.0755 | 0.479 | 1 | Hypothesis on dual cation substitution in chalcopyrite framework |
| ZnSnS₂ | 3 | 1 | -0.7996 | 0.1212 | 0.902 | 1 | Dual cation substitution in chalcopyrite framework |
| CdAg₂GeS₄ | 4 | 1 | -0.6146 | 0.0047 | 1.608 | 0 | Hypothesis on kesterite family Ag/Cd/Ge substitutions |
| CuTe | 5 | 1 | -0.2811 | 0.0 | 0.291 | 0 | Hypothesis on zincblende-GaAs prototype for Cu-based PV |
| CuSe | 5 | 1 | -0.3307 | 0.0208 | 0.492 | 0 | Zincblende-GaAs prototype substitutions |
| CuS | 5 | 1 | -0.4084 | 0.0435 | 0.069 | 0 | Zincblende-GaAs prototype substitutions |

- **Hypotheses tested and what was learned**:
  - Iteration 1: Hypothesis on Ga/Al and S substitutions in chalcopyrite-CuInSe₂ showed high theoretical band gap (1.8 eV), but GaAgS₂ was non-novel. Indicates potential for gap tuning but highlights novelty challenges.
  - Iteration 3: Zn/Cd dual cation substitution yielded two novel candidates (ZnSnS₂ and CdSnS₂). ZnSnS₂ reached 0.9 eV (close to target), while CdSnS₂ was too low (0.48 eV). Demonstrates tunability via cation radii.
  - Iteration 4: Kesterite Cu₂ZnSnS₄ with Ag/Cd/Ge substitutions produced CdAg₂GeS₄ with 1.61 eV gap, but this was a non-novel compound. Shows promise for high-gap engineering but requires novel candidate exploration next.
  - Iteration 5: Zincblende-GaAs prototype substitutions with Cu/Te/Se/S all yielded non-novel candidates with poor band gaps (0.07-0.49 eV). Suggests zincblende framework may not support Cu-based 1.4 eV targets without radical substitutions.

- **Caveats**:  
  - Surrogate error bars not included in ground-truth data, but formation energies (e_above_hull) suggest moderate stability (e.g., ZnSnS₂ at 0.12 eV).  
  - Only two iterations produced novel candidates; most proposals overlapped with Materials Project database.  
  - Synthesis validation needed for ZnSnS₂ and CdSnS₂ to verify computational gap predictions and stability.

- **Recommended next steps**:
  1. Expand iteration 3's dual cation substitution strategy in chalcopyrite framework to higher Ge/Sn/Ge ratios to increase ZnSnS₂'s 0.9 eV gap toward 1.4 eV.
  2. Revisit kesterite family in iteration 4 with different Ge/Sn ratios and mixed chalcogens to find novel Ag/Cd-based 1.4 eV candidates. 
  3. Consider alternative frameworks beyond chalcopyrite/kesterite/zincblende (e.g., stannite, wurtzite) for novel Cu-based absorbers.
  4. Use experimental validation (DFT, synthesis trials) to confirm charge balance and phase stability of ZnSnS₂.
