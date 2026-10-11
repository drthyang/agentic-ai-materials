# Campaign report: pv-absorber-v1

- **Executive summary**: This campaign tested five hypotheses for novel photovoltaic absorber materials through element substitution in established prototype structures. Only three candidates were successfully scored: one novel compound (CdAg₂GeSe₄, band gap 1.28 eV) and two known materials (AlAs, InAs). While CdAg₂GeSe₄ shows promising formation stability (e_above_hull=0.0) and a band gap near the target (~1.4 eV), limited relaxation budget constrained experimental validation. Hypotheses for chalcopyrite Fe and kesterite Ge substitutions generated novel candidates, but none achieved precise 1.4 eV tuning.

---

| Formula         | Converged | Formation energy (eV/atom) | E above hull (eV) | Band gap (eV) | Novel? |
|----------------|-----------|----------------------------|-------------------|---------------|--------|
| CdAg₂GeSe₄     | ✅        | -0.657                     | 0.0               | 1.279         | ✅      |
| AlAs           | ✅        | -0.492                     | 0.065             | 2.587         | ❌      |
| InAs           | ✅        | -0.197                     | 0.088             | 0.012         | ❌      |

---

## Hypotheses tested & observations
1. **Iteration 1-2 (Chalcopyrite Ga/In, Se/Te substitutions)**: Predicted band gap tuning via Ga/Al and Se/S/Te substitutions. No novel candidates scored in iterations 1-2.
2. **Iteration 3 (Chalcopyrite CuFe(S,S,Te)₂)**: Explored Fe for In in CuFe(S,Se,Te)₂. Generated one novel candidate (CdAg₂GeSe₄, e_above_hull=0.0). Literature confirmed no prior PV studies of this system.
3. **Iteration 5 (ZB AlGaInAsP quaternaries)**: Tested ternary (Al,Ga,In)(As,P) mixtures. Scored AlAs (non-novel, 2.59 eV gap) and InAs (non-novel, near-gap semiconductor). Surrogate models suggested potential for 1.4 eV tuning, but no novel candidates converged.

## Caveats
- **Surrogate model limitations**: CHGNet relaxations and HSE band gaps lack DFT validation. CdAg₂GeSe₄'s 1.28 eV gap requires experimental confirmation, as SMACT filters may overestimate stability.
- **Synthesis challenges**: Kesterite-derived systems (e.g., CdAg₂GeSe₄) may suffer from elemental volatility (Ag, Se) during fabrication. Energy above hull=0.0 indicates thermodynamic stability in simulation, but kinetic barriers remain untested.

## Recommended next steps
1. **Validate CdAg₂GeSe₄ with DFT**: Confirm band gap and stability using hybrid functionals (HSE06/PBE0).
2. **Expand kesterite Te content**: Test higher Te ratios to raise the 1.28 eV band gap toward 1.4 eV target while maintaining stability.
3. **Explore alternative valence engineering**: Revisit chalcopyrite CuInSe₂ with dual cation-anion substitutions combining Al/P and Ga/S for finer gap control.
4. **Assess processability**: Screen compounds for elemental volatility (e.g., Ag/Se losses during sintering), which may impact candidate viability despite thermodynamic stability.
