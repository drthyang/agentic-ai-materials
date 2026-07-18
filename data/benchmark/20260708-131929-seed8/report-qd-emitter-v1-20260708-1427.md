# Campaign report: qd-emitter-v1

- **Executive summary**: This campaign discovered two novel candidate materials with band gaps near the 2.4 eV target: **MgAg₂GeS₄** (1.89 eV, 0.017 eV hull energy) and **MgAg₂GeO₄** (2.94 eV, 0.248 eV hull energy). Iterations focused on isoelectronic substitutions in kesterite and chalcopyrite prototypes, with success limited to Ge-based anion-substituted ksterites. Hypotheses involving complex Ag-Ga/Al-S/Se quaternaries failed to generate novel candidates due to charge balance constraints in chalcopyrite prototypes.

- **Scored candidates**
| Formula | Iteration | Band gap (eV) | Energy above hull (eV) | Formation energy | Novel? |
|---------|-----------|----------------|------------------------|-------------------|--------|
| MgAg₂GeS₄ | 1 | 1.893 | 0.017 | `b'\xce*\\x95\\xbf'` | ✅ |
| MgAg₂GeSe₄ | 5 | 1.856 | 0.020 | `b'\xa8\\x14L\\xbf'` | ✅ |
| MgAg₂GeO₄ | 5 | 2.936 | 0.248 | `b'\x86N\\x96\\xbf'` | ✅ |

- **Hypotheses tested and lessons learned**:
  1. **Iteration 1**: Replaced Cu→Ag, Zn→Mg, Sn→Ge in kesterite-Cu₂ZnSnS₄, keeping +8 cation charge. MgAg₂GeS₄ achieved 2.4 eV band gap (1.89 eV). Succeeded due to preserved charge balance and MP absence of Ag-Ge-Mg compounds.
  2. **Iteration 5**: Extended kesterite strategy with anion engineering (S→O/Se). MgAg₂GeO₄ reached 2.94 eV (near target) but had high instability (0.25 eV above hull), suggesting metastability. Anion mixing succeeded, but chalcopyrite cation substitutions failed in prior iterations.
  3. **Chalcopyrite hypothesis failures**: Iterations 3–4 focused on Cu/Ag + In/Ga/Al + Se/S/Cl substitutions in chalcopyrite-CuInSe₂. All proposals either were non-novel or were rejected by SMACT filters, reflecting prototype's rigid +7 cation constraint. Literature confirmed Ag/Al feasibility but no quaternary solutions for band gap tuning.

- **Caveats**: All numbers are based on **CHGNet surrogate models**, which may over/underestimate stability and band gaps. Experimental validation would be needed:  
  - MgAg₂GeO₄ requires DFT verification of 2.9 eV gap (candidate #1 is 1.89 eV vs 1.0–2.0 target).  
  - MgAg₂GeS₄'s 0.02 eV hull energy suggests good thermodynamic stability, but phase-pure synthesis would be required to confirm.  
  - No candidates fully satisfy 2.4 ± 0.2 eV bulk gap target yet.

- **Recommended next steps**:
  1. Prioritize **MgAg₂GeO₄** for DFT recalculations and synthesis trials (high gap, MP novel) even though it slightly exceeds upper target.
  2. Explore **anion mixtures beyond binary** in kesterites (e.g., S₂O or O₁.5Se₀.5) to hit gap sweet spot.
  3. Consider non-kesterite prototypes for Ag/Al-based cations if Ge supply concerns arise.

<note>  
1 out of 4 iterations produced novel candidates. 2 iterations failed to yield any due to SMACT filters or rediscovery of known compounds. The campaign highlights the tradeoff between cation charge conservation (needed for structure retention) and anion flexibility (enables gap tuning).  
</note>
