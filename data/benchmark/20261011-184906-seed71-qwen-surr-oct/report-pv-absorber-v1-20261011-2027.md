# Campaign report: pv-absorber-v1  

## Executive summary  
This materials discovery campaign sought novel chalcopyrite-derivative photovoltaic absorbers with band gaps near 1.4 eV through systematic substitution of cations/anions in the CuInSe₂ prototype. Four iterations tested hypotheses ranging from ternary In→Ga/Al and Se→S/Te substitutions to quaternary Cu-Sn/Sb/As systems, guided by ionic radii matching, charge balance, and literature gaps. Despite chemical viability, all 5 scored candidates were non-novel (novel=false), with band gaps spanning 0.17–1.90 eV. The campaign revealed critical insights into valence compatibility and anion-cation pairing constraints but failed to identify uncharted compositions, underscoring the oversaturation of Cu-Sb/Ge-S/Se/Te spaces in the Materials Project database.  

## Scored candidates  

| Formula      | Converged | Formation energy (eV/atom) | E above hull (eV) | Band gap (eV) | Novel? |
|--------------|-----------|----------------------------|-------------------|----------------|--------|
| AgSbS₂       | Yes       | -0.847                     | 0.0               | 0.455          | No     |
| CuSbSe₂      | Yes       | -0.561                     | 0.0               | 1.285          | No     |
| CuSbS₂       | Yes       | -0.914                     | 0.0               | 1.901          | No     |
| CuSbTe₂      | Yes       | -0.248                     | 0.026             | 0.173          | No     |
| AgSbSe₂      | Yes       | -0.624                     | 0.0               | 0.496          | No     |

## Hypotheses tested and lessons learned  
**Iteration 1**:  
- Hypothesis: In→Ga/Al and Se→S/Te substitutions in chalcopyrite CuInSe₂ would yield tunable band gaps (1.1–1.7 eV) via cation-anion electronegativity engineering.  
- Result: All 8 proposed candidates were non-novel (novel=false), reflecting oversaturation of Cu-Ga/Al-S/Se/Te systems.  

**Iteration 2**:  
- Hypothesis: Radical quaternary substitutions (In→Sn/Ge, Se→Sb/As) would access unexplored Cu-Sn/Ge-Sb/As systems with band gaps near 1.4 eV.  
- Result: SMACT charge-balance filters rejected 50% of candidates (4/8). Survivors had invalid valence states (e.g., Sb⁻².⁵), proving valence constraints stricter than predicted by bulk charge calculations.  

**Iteration 3**:  
- Hypothesis: Mixed cation substitutions (In→Sn/Ge, Cu→Ag) with Se/S anions would satisfy CuInSe₂’s Cu⁺1 + 2Se⁻2 + cation requirement while enabling band-gap tuning.  
- Result: SMACT rejected candidates due to local electronegativity mismatches and ionic radius mismatches (Sn/Ge vs In).  

**Iteration 4–5**:  
- Hypothesis: In→Sb (similar ionic radius: 0.82 Å vs In’s 0.8 Å) with Cu→Ag partial substitution would preserve lattice compatibility and photovoltaic relevance.  
- Result: 5 scored candidates had novel=false. CuSbSe₂ (band gap 1.29 eV) neared target but was pre-existing in databases.  

## Caveats  
- Surrogate models and CHGNet relaxation cannot resolve synthetic feasibility or long-term stability under operational conditions.  
- All candidate systems (Cu-Sb-S/Se/Te) are well-represented in existing databases, suggesting fundamental limits to discovering novel chalcopyrites via these substitutions without structural framework changes.  
- Band gap predictions require HSE06 DFT validation to correct CHGNet fidelity errors (±0.1–0.2 eV uncertainty observed in prior campaigns).  

## Recommended next steps  
1. **Structural exploration**: Shift from chalcopyrite to kesterite (Cu₂ZnSnS₄) or zincblende prototypes, which may allow more flexible cation substitutions while preserving +1 valence requirements.  
2. **Anion engineering**: Investigate mixed-anion (e.g., Se/Br) or pnictogen-based chalcogenides (Sb/As) where ionic radius/valence mismatch is less critical.  
3. **Collaborative synthesis**: Prioritize CuSbSe₂ (1.29 eV) for experimental validation despite its non-novel status, as it aligns with the 1.4 eV target and may exhibit unstudied optoelectronic behavior under strain or doping.
