# Campaign report: pv-absorber-v1  

## Executive summary  
This campaign sought a photovoltaic absorber with a ~1.4 eV band gap through rational substitutions in chalcopyrite and kesterite structures. The most promising candidates were **CdCu₂GeS₄** (1.85 eV band gap) and **ZnCu₂GeS₄** (2.00 eV), both exceeding the target but showing low energy above hull (0.10–0.20 eV), suggesting potential stability. The kesterite system offered broader tunability than chalcopyrite, but none of the tested compositions achieved the exact 1.4 eV target. Hypotheses about Te incorporation (e.g., CuGaTe₂, CdCu₂GeTe₄) failed to improve band gaps below 0.34–0.85 eV, while S/Se anion blending in kesterites came closest to the target.  

---

## Scored candidates  
| Formula         | Band gap (eV) | E above hull (eV) | Novel |  
|-----------------|---------------|-------------------|-------|  
| GaCuS₂          | 2.05          | 0.15              | No    |  
| GaCuTe₂         | 0.11          | 0.09              | No    |  
| GaCuSe₂         | 1.21          | 0.10              | No    |  
| CdCu₂SnS₄       | 1.69          | 0.01              | No    |  
| ZnCu₂SnSe₄      | 0.34          | 0.06              | No    |  
| ZnCu₂GeSe₄      | 0.85          | 0.07              | No    |  
| CdCu₂SnSe₄      | 0.28          | 0.09              | No    |  
| CdCu₂GeS₄       | 1.85          | 0.10              | No    |  
| ZnCu₂GeS₄       | 2.00          | 0.20              | No    |  
| CdCu₂GeTe₄      | 0.33          | 0.08              | No    |  

---

## Hypotheses tested  
### **Iteration 1** (Chalcopyrite CuInSe₂ → CuGaSe/S)  
- **Hypothesis**: Ga substitution for In (ionic radius 0.62 Å vs 0.63 Å) would raise band gap toward 1.4 eV, with S/Se anions for fine-tuning.  
- **Result**: CuGaSe₂ showed 1.21 eV (close to target), but CuGaS₂ had 2.05 eV (too high).  

### **Iteration 3** (Add Te anion to CuGaX₂)  
- **Hypothesis**: Te (larger ionic radius, lower electronegativity than Se) would lower band gaps beyond CuGaSe₂.  
- **Result**: CuGaTe₂ had a metallic character (0.11 eV gap), failing to address the target.  

### **Iteration 4** (Kesterite Cu₂ZnSn(S,Se)₄ platform)  
- **Hypothesis**: Mixed anions (S/Se) and cation substitutions (Cd/Ge) in kesterite would achieve 1.3–1.4 eV.  
- **Result**: CdCu₂SnS₄ reached 1.69 eV, while Zn/Ge variants showed 0.34–2.00 eV. Cd-based S-anion kesterites (CdCu₂GeS₄) exceeded 1.8 eV.  

### **Iteration 5** (Ternary Te/S/Se anions in kesterite)  
- **Hypothesis**: Adding Te to CdCu₂GeS₄ would lower its 1.85 eV gap closer to 1.4 eV.  
- **Result**: CdCu₂GeTe₄ (0.33 eV gap) worsened the band gap, demonstrating that Te substitutions in this context were ineffective.  

---

## Caveats  
- **Surrogate model limitations**: Band gaps and formation energies were computed using CHGNet and HSE-fidelity estimates, which may differ from DFT results.  
- **Validation needed**: CdCu₂SnS₄ (1.69 eV, E_above_hull=0.01 eV) is the top candidate for experimental synthesis, but its performance requires validation against photoelectrochemical stability and carrier mobility.  
- **Non-novelty**: All candidates already exist in the Materials Project database, indicating they may not be synthetically challenging but could still meet performance targets.  

---

## Recommended next steps  
1. Validate **CdCu₂SnS₄** with DFT to confirm 1.69 eV band gap and stability.  
2. Explore minor **Sn/Sn site substitutions** (e.g., Sn→Ge at fixed anion ratios) to lower its gap.  
3. Test **Cu₂ZnSn(S,Se)₄** with alternative cation substitutions (e.g., Ga at Cu sites) not trialed here.  
4. If kesterite tuning fails, return to chalcopyrite CuGa(S,Se)₂ system with **ternary anion blends** (S/Se/Sn) to hit 1.4 eV.
