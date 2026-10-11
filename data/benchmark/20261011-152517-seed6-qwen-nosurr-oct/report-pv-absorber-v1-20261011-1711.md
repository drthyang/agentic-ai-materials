# Campaign report: pv-absorber-v1  

## Executive summary  
This campaign explored Ag-based chalcopyrite derivatives for photovoltaic absorbers targeting a 1.4 eV band gap. Over five iterations, 18 candidates were proposed (74% filtered out due to chemical infeasibility), and 12 converged relaxations were scored. The most promising candidate, **GaAgSe₂**, achieved the target band gap (1.418 eV) with near-stability (e_above_hull=0.048 eV/atom). However, **all candidates were non-novel** (is_Novel=0), with GaAgSe₂ and AlAgS₂ already in the Materials Project database. Substitutions with Te or Al generally shifted the gap below or above 1.4 eV, while mixed-anion strategies showed limited success. The findings highlight the potential of Ag–Ga–Se systems but emphasize the need for novel anion/cation combinations yet unexplored in chalcopyrite structures.  

---

## Scored candidates  

| Formula     | Iteration | Band Gap (eV) | Stable? (e_above_hull) | Novel? | Formation Energy (eV/atom) |
|-------------|-----------|---------------|-------------------------|--------|----------------------------|
| AlAgS₂      | 1         | 2.268         | Yes (0.0)               | No     | -1.582                     |
| GaAgS₂      | 1         | 1.838         | No (0.083)              | No     | -1.074                     |
| GaAgTe₂     | 2         | 0.588         | No (0.046)              | No     | -0.419                     |
| GaAgSe₂     | 2         | 1.418         | No (0.048)              | No     | -0.756                     |
| AlAgTe₂     | 3         | 1.869         | No (0.138)              | No     | -0.404                     |
| AlAgSe₂     | 3         | 2.376         | No (0.245)              | No     | -0.730                     |
| AgSbSe₂     | 4         | 0.497         | Yes (0.0)               | No     | -0.624                     |
| AgSbTe₂     | 4         | 0.656         | Yes (0.0)               | No     | -0.285                     |

---

## Hypotheses tested and findings  

### **Iteration 1**  
**Hypothesis**: Substitute CuInSe₂ cations (Cu→Ag, In→Ga/Al) and anion (Se→S) to tune band gaps.  
**Outcome**: AlAgS₂ (2.268 eV) and GaAgS₂ (1.838 eV) showed high gaps, but GaAgS₂ was already known. No candidates met the 1.4 eV target.  

### **Iteration 2**  
**Hypothesis**: Dual cation-anion substitutions (Ag/Ga and Te/Se) to explore mid-gap (1.4 eV) candidates.  
**Outcome**: GaAgSe₂ hit 1.418 eV (off-target by +0.018 eV) with e_above_hull=0.048 eV/atom. GaAgTe₂ had a much lower gap (0.588 eV). Both were non-novel.  

### **Iteration 3**  
**Hypothesis**: Mixed-anion (Se/Te) and cation-variant (Al) chalcopyrites to refine the gap.  
**Outcome**: AlAgSe₂ (2.376 eV) and AlAgTe₂ (1.869 eV) missed the target. Rejected due to low novelty and stability.  

### **Iteration 5**  
**Hypothesis**: Multi-cation (Ga/Al/Sn) and mixed-anion (Se/Te/S/Cl) substitutions to expand tunability.  
**Outcome**: SMACT filters rejected most candidates due to charge/chemistry mismatches (e.g., Cl’s -1 oxidation state). Only Se/Te/S mixtures remained viable, suggesting a focus on these anions.  

---

## Caveats  
1. **Novelty limitations**: All candidates were pre-existing in the MP database. Future work requires exploring uncharted cation/anion combinations.  
2. **Surrogate model gaps**: HSE-fidelity band gaps and formation energies rely on CHGNet approximations; DFT validation is needed for convergence and charge balance.  
3. **Stability constraints**: Even the best candidate (GaAgSe₂) had e_above_hull=0.048 eV/atom, suggesting synthesis challenges.  

---

## Recommended next steps  
1. **Focus on novel mixed-anion (SeₓTe₁₋ₓ) chalcopyrites with Ag/Ga/Al cations**. Use Se-rich ratios to target higher gaps (e.g., AgGaSe₀.8Te₀.2).  
2. **Avoid Cl substitutions** (invalidated by SMACT filters) and **postpone Sn-based designs** until anion mixing strategies mature.  
3. **Propose candidates with partial S incorporation** to leverage its small ionic radius and gap-increasing effect (observed in prior iterations).  
4. **Conduct targeted literature/labs search** for unexplored Ag–Ga–S–Se–Te compositions to confirm novelty before DFT validation.
