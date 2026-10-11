# Campaign report: pv-absorber-v1

## Executive summary

The campaign ran one iteration. It tested whether isoelectronic substitution in the kesterite (Cu2ZnSnS4) prototype could give new compounds with gaps of 1.1–1.7 eV that are close to the convex hull. Of 52 proposed candidates, 14 novel kesterite-type quaternaries were relaxed and scored. Three met the screening criteria (ehull ≤ 0.05 eV/atom, gap 1.1–1.7 eV): **CdAg2GeSe4** (ehull 0.000, gap 1.28 eV), **ZnAg2GeSe4** (ehull 0.000, gap 1.12 eV) and **MgAg2SnSe4** (ehull 0.016, gap 1.59 eV). All numbers come from a CHGNet relaxation and an ML band-gap predictor, with no DFT or experimental check. Confidence is therefore low to moderate, and these are leads for validation rather than confirmed discoveries.

## Scored candidates

All 14 were novel relative to the Materials Project, and all relaxations converged. The table is sorted by energy above hull. "Hit" means ehull ≤ 0.05 eV/atom and gap 1.1–1.7 eV.

| Formula | E_form (eV/atom) | E_above_hull (eV/atom) | Gap (eV) | Hit? |
|---|---|---|---|---|
| CdAg2GeSe4 | -0.657 | 0.000 | 1.28 | Yes |
| ZnAg2GeSe4 | -0.681 | 0.000 | 1.12 | Yes |
| MgAg2SnS4 | -1.177 | 0.002 | 1.87 | No (gap too wide) |
| MgAg2SnSe4 | -0.838 | 0.016 | 1.59 | Yes |
| MgAg2GeS4 | -1.165 | 0.017 | 1.89 | No (gap too wide) |
| MgCu2SnS4 | -1.239 | 0.020 | 2.17 | No (gap too wide) |
| MgAg2GeSe4 | -0.797 | 0.020 | 1.86 | No (gap too wide) |
| MgCu2SnSe4 | -0.819 | 0.071 | 1.38 | No (ehull just above cutoff) |
| CdSi(AgSe2)2 | -0.568 | 0.130 | 1.71 | No (unstable) |
| MgCu2GeSe4 | -0.717 | 0.136 | 1.10 | No (unstable) |
| MgSi(AgSe2)2 | -0.715 | 0.145 | 2.35 | No (unstable) |
| CdSi(AgS2)2 | -0.937 | 0.152 | 2.75 | No (unstable) |
| MgSi(AgS2)2 | -1.132 | 0.167 | 2.54 | No (unstable) |
| ZnSi(AgSe2)2 | -0.553 | 0.170 | 1.90 | No (unstable) |

## Hypotheses tested and what was learned

**Iteration 1: kesterite isoelectronic substitution.**
- **Hypothesis:** In the kesterite CZTS family, substituting Zn→Cd/Mg, Sn→Ge/Si, Cu→Ag and mixing S/Se should tune the gap into 1.1–1.7 eV. Less-explored combinations were expected to be novel. Chalcopyrite variants (Cu/Ag with Ga/In and S/Se/Te, with Ag/Al mixes) were also proposed.
- **Result, Ag selenides:** The hypothesis largely held for Ag-based selenides with Ge or Sn on the tetravalent site. These gave the three hits above.
- **Result, Si:** All six Si-containing compounds were unstable (ehull 0.13–0.17 eV/atom). The notebook attributes this to Si being too small for the Sn/Ge site. That explanation was not tested directly.
- **Result, sulfides:** The Mg–Ag and Mg–Cu sulfides were near the hull (ehull ≤ 0.02) but had gaps of 1.87–2.17 eV, above the target window.
- **Result, Cu selenides:** MgCu2SnSe4 had a 1.38 eV gap but an ehull of 0.071, just outside the cutoff. MgCu2GeSe4 had an ehull of 0.136.
- **Gap trends from the data:**
  - For Ge–Ag–Se, the gap widens Zn (1.12) < Cd (1.28) < Mg (1.86).
  - Sulfides generally have larger gaps than selenides, but the size varies a lot. MgAg2SnS4 vs MgAg2SnSe4 differs by about 0.28 eV. MgCu2SnS4 vs MgCu2SnSe4 differs by about 0.79 eV. MgAg2GeS4 vs MgAg2GeSe4 differs by only about 0.04 eV.
  - The notebook's summary of an S–Se offset of "~0.3–0.6 eV" is therefore not consistently supported, and the offset should not be treated as a reliable rule.
- **Chalcopyrite variants:** Every chalcopyrite substitution generated was already in the Materials Project, so none were evaluated.
- **Budget:** 14 of 20 relaxations were used. The generated pool had no further novel candidates.

Only this one iteration was run, so there is no evidence yet on whether the trends hold in other families.

## Caveats

- **Surrogate error:** Formation energies and ehull values come from CHGNet relaxations. Band gaps come from an ML predictor described as HSE-fidelity. Error bars were not quantified in this campaign. Ehull differences of a few to tens of meV/atom (for example MgAg2SnS4 at 0.002 vs MgAg2SnSe4 at 0.016) are likely within model error.
- **Hull reference:** An ehull of 0.000 is relative to the Materials Project phases, which may be incomplete for these quaternary systems. It does not show that the compound is thermodynamically stable.
- **Structure type:** The relaxed structures were assumed to be kesterite-type. The true ground state could be stannite, wurtzite-derived or another polymorph, and no polymorph comparison was done. This would change both the ehull and the gap.
- **Not checked:** Phonon stability, competing binary and ternary phases, defect chemistry and band-edge alignment were not examined. Absorption strength and gap type (direct or indirect) were also not assessed.
- **Chemistry:** Ag-containing compounds raise cost and Ag-related defect questions for photovoltaic use.

## Recommended next steps

1. **DFT validation.** Run DFT (PBE or HSE) on CdAg2GeSe4, ZnAg2GeSe4 and MgAg2SnSe4. Compare kesterite, stannite and wurtzite-derived polymorphs, and check the hull against competing phases such as Ag2Se, GeSe2 and the binary chalcogenides.
2. **Follow-up substitutions from the notebook.** Try mixed S/Se Ag compounds (for example CdAg2Ge(S,Se)4) and Cd/Mg–Ag–Sn–Se variants. These are the next steps the notebook suggests, not results.
3. **New prototypes.** The pool of kesterite and chalcopyrite substitutions is largely used up, so prototypes beyond the current list are needed.
4. **Cu–Mg selenides.** Re-examine MgCu2SnSe4 (gap 1.38 eV, ehull 0.071) with higher-fidelity methods. It might still be metastable and synthesizable.
5. **Synthesis.** If DFT confirms the leading candidates, try solid-state synthesis and then measure the gap.
