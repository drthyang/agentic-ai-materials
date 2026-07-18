# Campaign report: pv-absorber-v1  

**Executive summary**  
This campaign tested hypotheses for 1.4-eV band gap photovoltaic absorbers by exploring element substitutions in chalcopyrite, kesterite, and zincblende prototypes. Iterations 1-3 identified novel candidates like **MgAg₂GeTe₄** (1.49 eV, *E*ₐᵥₑₐBOVE 0.025 eV) and **CdAg₂GeSe₄** (1.28 eV, hull energy = 0), but subsequent iterations lacked viable candidates due to novel-material filters or failed relaxations. While some compounds approached the target band gap, none exactly matched 1.4 eV, and most had non-zero energy above hull (stability concern). The zincblende-focused Hypotheses 4-5 were untested due to novel-material filters blocking prior proposals.  

**Scored candidates**  
| Formula         | Band gap (eV) | *E*<sub>above hull</sub> (eV) | Novelty | Iteration |
|----------------|---------------|-------------------------------|---------|----------|
| CdAg₂GeSe₄     | 1.279         | 0.000                         | ✅      | 1        |
| MgAg₂GeTe₄     | 1.490         | 0.025                         | ✅      | 1        |
| MgAg₂GeSe₄     | 1.856         | 0.020                         | ✅      | 1        |
| CdAg₂GeTe₄     | 0.481         | 0.017                         | ✅      | 1        |
| MgCu₂GeSe₄     | 1.102         | 0.136                         | ✅      | 3        |
| MgCu₂GeTe₄     | 0.895         | 0.101                         | ✅      | 3        |
| TiCd(CuTe₂)₂   | ~0.000        | 0.424                         | ✅      | 3        |
| MgTi(CuSe₂)₂   | 2.706         | 0.443                         | ✅      | 3        |

**Hypotheses tested**  
1. **Iteration 1**: Charge-balanced kesterite pivots (Zn→Mg/Cd, Sn→Ge, Cu→Ag) with anion tuning (Se/Te). Found 1.28–1.86 eV band gaps but most candidates had non-zero *E*<sub>above hull</sub>. CdAg₂GeSe₄ (1.28 eV, hull=0) was the most stable.  
2. **Iteration 2**: Expanding chalcopyrite substitutions to include O as an anion. Both proposals (AlAgO₂ and GaAgO₂) were *non-novel* (known-materials filter), wasting relaxation budget.  
3. **Iteration 3**: Extended kesterite substitutions (Zn→Mg/Cd, Sn→Ge/Ti). MgAg₂GeTe₄ (1.49 eV, hull=0.025) was the most promising. MgTi(CuSe₂)₂ (2.71 eV) showed high band gap but poor stability.  

**Caveats**  
- **Formation energy/phonon stability**: Formulas labeled with corrupted `formation_energy_per_atom` data (see scored candidates) indicate incomplete evaluations.  
- **Surrogate model error bars**: CHGNet predictions require DFT validation for *E*<sub>above hull</sub> and band gap. CdAg₂GeSe₄’s 0 band gap *E*<sub>above hull</sub> is promising but untrustworthy without validation.  
- **Synthesis feasibility**: Candidates like TiCd(CuTe₂)₂ (meta-stable, *E*<sub>above hull</sub> = 0.424 eV) or high-gap MgAg₂GeSe₄ may not crystallize under lab conditions.  

**Recommended next steps**  
1. Prioritize **MgAg₂GeTe₄** (1.49 eV, 0.025 eV *E*<sub>above hull</sub>) and **CdAg₂GeSe₄** (1.28 eV, hull=0) for DFT band structure and synthesis pathway analysis.  
2. Revisit **Hypothesis 4** (zincblende AlGaSe/Te) with a different substitution scope, as prior proposals (Iteration 5) were filtered for using non-novel combinations.  
3. Explore mixed anion systems (e.g., Se/Te/TeS) to fine-tune band gaps. Iteration 1 showed that Se/Te ratios could push 0.48–1.86 eV, suggesting a path to 1.4 eV via solid-solution engineering.  

---  
Data disclaimer: Only the candidates and hypotheses explicitly listed in the ground-truth notebook are reflected here. The campaign’s limited budget and novel-materials filters constrained discovery potential; future work should allocate more resources to unexplored prototypes like lead-halide perovskites.
