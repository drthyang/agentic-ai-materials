# Campaign report: pv-absorber-v1

- **Executive summary**: This campaign identified six novel kesterite-derived compounds (iteration 2) with band gaps near the solar cell optimum (1.2–1.9 eV). While zincblende-based hypotheses (iterations 4–5) failed due to charge imbalance issues, the kesterite-Cu₂ZnSnS₄ substitution strategy successfully produced multiple stable candidates with tunable band gaps. The top performer, **CdAg₂GeSe₄**, showed a 0.00 eV energy above hull and 1.28 eV band gap, suggesting thermodynamic stability and photovoltaic suitability. However, higher *e_above_hull* values in other candidates indicate fragility requires further analysis.

- **Scored candidates**  
  | Formula         | Converged | *E_form* (raw) | *E_above_hull* (eV) | Band gap (eV) | Novel? |
  |------------------|-----------|----------------|---------------------|---------------|--------|
  | CdAg₂GeSe₄       | ✅        | b'¸/¿'         | 0.00                | 1.28          | ✅     |
  | MgAg₂SnSe₄       | ✅        | b'|mV¿'        | 0.02                | 1.59          | ✅     |
  | CdAg₂GeTe₄       | ✅        | b'(§¿'        | 0.02                | 0.48          | ✅     |
  | MgAg₂GeSe₄       | ✅        | b'¬L¿'        | 0.02                | 1.86          | ✅     |
  | MgAg₂GeTe₄       | ✅        | b'©Ø¿'         | 0.02                | 1.49          | ✅     |
  | CdAg₂SnTe₄       | ✅        | b'–»¿'        | 0.03                | 0.41          | ✅     |
  | MgAg₂SnTe₄       | ✅        | bÀî¿'         | 0.04                | 1.17          | ✅     |

  > Note: Formation energy values represent raw byte data from CHGNet and require decoding for physical interpretation.

- **Hypotheses tested**  
  1. **Iteration 1 (chalcopyrite-CuInSe₂ substitutions)**: Replacing In/Ga and Se/S/Te showed promise in literature but yielded only 4/4 known materials, indicating prior exploration of this design space.  
  2. **Iteration 2 (kesterite-Cu₂ZnSnS₄ substitutions)**: Systematic IV-group (Ge/Sn) and VI-group (Se/Te) substitutions with Mg/Cd and Ag produced 7 novel candidates. CdAg₂GeSe₄'s zero hull energy suggests it could be synthesizable as a near-equilibrium phase.  
  3. **Iterations 4–5 (zincblende-GaAs substitutions)**: Hypotheses about III-V permutations (Cu/Ag/In–As/P/Sb/Te) failed due to charge imbalances (e.g., +1 Cu with -2 Te), demonstrating the tight constraints of maintaining III-V stoichiometry for band gap engineering.

- **Caveats**  
  - *E_above_hull* ≥ 0.02 eV (e.g., MgAg₂GeSe₄ at 0.02 eV) suggests metastability; DFT recalculations and experimental synthesis attempts would validate stability.  
  - Band gaps from CHGNet (HSE-fidelity approximation) require *ab initio* recalculations for precision.  
  - No candidates demonstrated both <0.05 eV hull energy *and* 1.0–1.5 eV band gaps, limiting immediate photovoltaic relevance.

- **Recommended next steps**  
  1. Prioritize **CdAg₂GeSe₄** for DFT band structure validation and phase stability analysis, building on its zero hull energy and 1.28 eV gap.  
  2. Revisit zincblende designs with strict charge-balance constraints (e.g., In–Sb pairs) to avoid iteration 5 failures.  
  3. Investigate cation-anion co-substitution strategies (e.g., partial Te-for-Se in kesterites) to tune *E_above_hull* while retaining band gap benefits.
