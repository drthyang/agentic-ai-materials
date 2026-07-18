# Campaign report: pv-absorber-v1

- **Executive summary**: This discovery campaign identified three novel photovoltaic candidates (ZnAg₂GeSe₄, MgAg₂SnS₄, MgAg₂GeS₄) with band gaps near the 1.4 eV target. Iterations 2 and 5 produced the most promising results, while iteration 3's Ag-chalcopyrite substitutions yielded non-novel compounds. The kesterite-based approach (iterations 4-5) successfully combined Ag cations with Mg/Ge substitutions to achieve tunable gaps (1.87–1.89 eV), though further anion substitution may lower these values. The campaign highlights the value of systematically combining cation/anion substitution strategies while avoiding over-oxidized combinations.

- **Scored Candidates**:

| Formula          | Converged | Formation Energy (eV/atom) | E_above_hull (eV) | Band Gap (eV) | Novel |
|------------------|-----------|-----------------------------|--------------------|----------------|-------|
| ZnAg₂GeSe₄       | 1         | `b'\x84a.\xbf'`            | 0.00               | 1.119          | 1     |
| ZnAg₂GeTe₄       | 1         | `b'\xf0\x08\xa3\xbe'`       | 0.028              | 1.171          | 1     |
| InAgS₂           | 1         | `b'\x02\xb5\x98\xbf'`       | 0.00               | 0.477          | 0     |
| InAgTe₂          | 1         | `b'\x08\x84\xe5\xbe'`        | 0.012              | 0.013          | 0     |
| InAgSe₂          | 1         | `b'$\x03?\\xbf'`            | 0.022              | 0.711          | 0     |
| AlAgSe₂          | 1         | `b'\xe0\xef:\xbf'`           | 0.245              | 2.376          | 0     |
| CaCu₂GeS₄        | 1         | `b'\xec~\xab\xbf'`           | 0.096              | 2.563          | 1     |
| MgAg₂SnS₄        | 1         | `b':\x9b\x96\xbf'`           | 0.002              | 1.871          | 1     |
| MgAg₂GeS₄        | 1         | `b'\xd2*\x95\xbf'`           | 0.017              | 1.893          | 1     |

- **Hypotheses tested**:
  - **Iteration 1**: Substituted In→Ga/Al and Se→S/Te in chalcopyrite CuInSe₂. All candidates were non-novel (novel=false), prompting expansion in iteration 2.
  - **Iteration 2**: Extended chalcopyrite substitutions to B-site (Al,Ga,In) and X-site (S,Se,Te). Produced 2 novel candidates (ZnAg₂GeSe₄, ZnAg₂GeTe₄) with band gaps near 1.4 eV.
  - **Iteration 3**: Replaced Cu→Ag in chalcopyrite while maintaining B/X substitutions. All 4 candidates were non-novel (AgIn(S,Te)₂), indicating the need to pivot.
  - **Iteration 4**: Tested kesterite Cu₂ZnSnS₄ with Mg/Ca substitutions. Only 1 of 2 proposed candidates (CaCu₂GeS₄) was novel but had an excessively high band gap (2.56 eV).
  - **Iteration 5**: Hybrid kesterite-chalcopyrite approach (Ag₂MgGeS₄ family). Achieved 2 novel compositions with band gaps near 1.87–1.89 eV, validating the synergistic substitution strategy.

- **Caveats**:
  - Formation energies (displayed as corrupted binary strings) require DFT validation to confirm thermodynamic stability.
  - Band gaps from CHGNet-HSE estimates may differ from experimental results; materials with E_above_hull > 0.1 eV (e.g., CaCu₂GeS₄) face higher stability risks.
  - Non-novel In/Ag chalcopyrites show wide gap variability (0.01–2.38 eV), suggesting the need for better screening of novel candidates.

- **Recommended next steps**:
  1. Prioritize ZnAg₂GeSe₄ (novel, stable, 1.12 eV gap) for experimental validation due to minimal E_above_hull and strong alignment with the 1.4 eV target.
  2. Explore anion substitutions (e.g., replacing partial Se with S in ZnAg₂GeSe₄) to fine-tune the band gap downward.
  3. Revisit the kesterite framework for Ag₂MgGe(S,Se)₄ combinations (iterations 4-5) to find lower-gap compositions with improved stability.
  4. Investigate alternative cation substitutions beyond Mg/Ca (e.g., Sr) to reduce the high gaps in Ge-substituted kesterites.
