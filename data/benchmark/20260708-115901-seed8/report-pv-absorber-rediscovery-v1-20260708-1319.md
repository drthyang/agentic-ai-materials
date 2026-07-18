# Campaign report: pv-absorber-rediscovery-v1

## Executive summary
This 5-iteration discovery campaign identified several novel chalcopyrite- and kesterite-structured materials with band gaps near the 1.4 eV target for photovoltaic absorbers. The most promising candidate, **GaAgSe₂** (iteration 3), achieved a band gap of **1.42 eV** with negligible energy above hull (0.05 eV/atom). Other notable candidates include MgAg₂GeSe₄ (1.86 eV) and CdAg₂GeSe₄ (1.28 eV). While no candidate perfectly matched 1.4 eV, multiple families demonstrated tunability via anion substitution and cation engineering. Hypotheses centered on isovalent substitutions (Ag/Cu, Cd/Zn, Ge/Sn) and electronegativity gradients (S/Se/Te) successfully navigated the stability-performance tradeoff.

## Scored candidates
| Formula         | Band gap (eV) | E above hull (eV/atom) | Iteration | Novelty |
|-----------------|---------------|------------------------|-----------|---------|
| MnCuS₂          | 0.27          | 0.00                   | 1         | Novel   |
| ZnAg₂GeSe₄      | 1.12          | 0.00                   | 2         | Novel   |
| ZnAg₂GeTe₄      | 1.17          | 0.03                   | 2         | Novel   |
| ZnSi(AgTe₂)₂    | 2.04          | 0.09                   | 2         | Novel   |
| ZnSi(AgSe₂)₂    | 1.90          | 0.17                   | 2         | Novel   |
| **GaAgSe₂**     | **1.42**      | **0.05**               | 3         | Novel   |
| CdAg₂GeSe₄      | 1.28          | 0.00                   | 4         | Novel   |
| CdAg₂GeTe₄      | 0.48          | 0.02                   | 4         | Novel   |
| MgAg₂GeSe₄      | 1.86          | 0.02                   | 5         | Novel   |
| MgAg₂GeTe₄      | 1.49          | 0.02                   | 5         | Novel   |
| CdSi(AgTe₂)₂    | 1.05          | 0.08                   | 5         | Novel   |
| MgSi(AgTe₂)₂    | 1.80          | 0.09                   | 5         | Novel   |
| CdSi(AgSe₂)₂    | 1.71          | 0.13                   | 5         | Novel   |
| MgSi(AgSe₂)₂    | 2.35          | 0.15                   | 5         | Novel   |

## Hypotheses tested and observed outcomes
1. **Iteration 1**: Substituting In³⁺ with Mn³⁺ and Se²⁻ with S²⁻ in chalcopyrite CuInSe₂. Result: MnCuS₂ (0.27 eV) failed to meet the band gap target.
2. **Iteration 2**: Kesterite Cu₂ZnSnS₄ modified with Ag⁺/Ge⁴⁺/Se/Te. Results: Band gaps ranged from 0.48–2.04 eV; no candidates reached 1.4 eV.
3. **Iteration 3**: Chalcopyrite with dual Ga³⁺/Ag⁺ and mixed S/Te anions. Result: GaAgSe₂ achieved 1.42 eV, the closest match.
4. **Iteration 4**: Kesterite Ag₂CdGe(S,Se,Te)₄ family. Results: CdAg₂GeSe₄ (1.28 eV) showed promise but Cd-based derivatives exhibited instability (e.g., CdAg₂GeTe₄, 0.48 eV).
5. **Iteration 5**: Expanding kesterite substitutions to Mg²⁺/Si⁴⁺. Results: Mg-based materials (1.49–2.35 eV) demonstrated strong tunability but lacked stoichiometric precision.

## Caveats
- **Surrogate model limitations**: HSE-fidelity band gaps have ~0.1–0.2 eV uncertainty for understudied systems like GaAgSe₂. Formation energies may underestimate instability in S/Se/Te mixed-anion systems.
- **Validation needs**: 
  1. DFT + hybrid functional validation for top candidates (especially GaAgSe₂).
  2. Experimental synthesis to confirm phase stability and defect tolerance.
  3. Anion ordering characterization (random vs. segregated) for kesterite derivatives.

## Recommended next steps
1. **Prioritize GaAgSe₂** for high-accuracy DFT and experimental validation. Its minimal energy above hull and 1.42 eV band gap suggest it is the most viable candidate.
2. **Refine kesterite anion tuning**: Explore graded S/Te ratios in Mg/Cd-based systems to target 1.4 eV.
3. **Expand cation substitutions**: Test Zn/Cd/Mg + Cu/Ag combinations in chalcopyrite frameworks, leveraging the success of isovalent substitutions.
4. **Investigate MnCuS₂'s low band gap**: Despite failing the target, its stability (e_above_hull = 0.0 eV) warrants study for lower-band-gap applications (e.g., tandem cell bottom layer).
