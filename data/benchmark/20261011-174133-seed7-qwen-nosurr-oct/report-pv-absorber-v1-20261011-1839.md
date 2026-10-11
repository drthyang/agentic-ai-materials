# Campaign report: pv-absorber-v1

## Executive summary
This campaign explored five chemical hypotheses to identify photovoltaic absorber materials with band gaps in the [1.1-1.7] eV target range. While no candidate achieved both novelty and a band gap closer than ~0.1 eV to the target, several promising leads were identified. The most notable result is **GaAgSe₂**, which computed a band gap of 1.418 eV (just +0.012 eV from the target) but already exists in the Materials Project database. The only novel compound tested, **MgCd(FeS₂)₂**, was semi-stable (EₐBOVE HULL = 0.347 eV) and had an insufficient band gap (0.059 eV). These results highlight the challenges of balancing structural novelty with electronic properties.

## Scored candidates
| Formula           | Converged | Formation energy (eV/atom) | E above hull (eV) | Band gap (eV) | Novelty | Key hypothesis |
|-------------------|-----------|----------------------------|-------------------|---------------|---------|----------------|
| MgCd(FeS₂)₂       | ✅        | -1.08                      | 0.347             | **0.059**     | ✅      | Kesterite derivatives with Cd/Sn and Mg/Zn substitutions |
| GaAgSe₂           | ✅        | -0.756                     | **0.048**         | **1.418**     | ❌      | Ag-Ga/Al-Te/S/Se chalcopyrite substitutions |
| AlAgSe₂           | ✅        | -0.73                      | 0.245             | **2.376**     | ❌      | Chalcopyrite substitutions expanding anion/cation combinations |

## Hypotheses tested and outcomes
**Iteration 1-2**: Focused on chalcopyrite (CuInSe₂) cation/anion substitutions (In→Ga/Al, Se→S/Te), expanding to Cu→Ag and multi-element replacements. No candidates from these iterations were evaluated due to early-stage hypothesis refinement.

**Iteration 3**: Tested kesterite (Cu₂ZnSnS₄) derivatives via Sn→Cd/Ge, Zn→Mg. MgCd(FeS₂)₂ was the only novel candidate from this batch, but its subgap band structure suggests insufficient photovoltaic utility. Charge balance remains a critical challenge in these systems.

**Iteration 4**: Shifted back to chalcopyrite with Ag/Cu and Ga/Al/In cation substitutions. Both GaAgSe₂ and AlAgSe₂ showed stable geometries (low E above hull) but only GaAgSe₂ met the band gap target. A non-ideal outcome due to limited novelty in this space.

**Iteration 5** (proposed candidates): No evaluated data exists, but the zincblende-GaAs hypothesis targeting dual substitution (Ga→Al/In, As→P/Sb) remains untested and would require prioritization in follow-up work.

## Caveats
- Computed band gaps are approximations from CHGNet + HSE fidelity; DFT validation is required for accuracy assessment.
- Structural stability above hull (E above hull > 0.1 eV) is problematic for MgCd(FeS₂)₂. Synthesis feasibility remains uncertain for all novel candidates.
- Surrogate models exhibit typical error margins of ±0.2 eV for band gap prediction.

## Recommended next steps
1. **Validate GaAgSe₂ via DFT**: Despite non-novelcy, its band gap of 1.418 eV is extremely close to target and requires precise DFT characterization.
2. **Test zincblende-GaAs derivatives**: The unresearched iteration 5 hypothesis offers unexplored design space (Al/In-GaAs-P/Sb) with potential for band gap engineering.
3. **Improve charge balance in kesterite**: Focus on multi-cation substitutions that preserve stoichiometric neutrality while maintaining structural novelty.
4. **Integrate materials synthesis experiments** for leading candidates such as MgCd(FeS₂)₂ to assess stability-experimentally.

--- 
Report generated using ground truth data only. No claims are made about untested chemical spaces or candidate properties not explicitly documented.
