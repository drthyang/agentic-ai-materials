# Lab Notebook

## [hypothesis] iteration 1 — 2026-10-12 06:16 UTC

Hypothesis: CuGaSe2 (chalcopyrite) is a known photovoltaic material (Schottky homodiode studies from 1979-2020). To achieve 1.4 eV gap with stability, propose isostructural substitutions: (1) Cu → Ag (similar ionic radius, +1 oxidation state) to tune hole mobility; (2) Ga → Al/In (isoelectronic group 13 substitution, Ga: 1.20 Å vs Al: 1.22 Å vs In: 1.44 Å) to modulate band edges; (3) Se → S/Te (chalcogen substitution, ionic radii 1.74 Å vs 1.84 Å) to adjust band gap. Expect 1.4 eV gap in AgGaS2 family based on Vegard's law extrapolation from CuGaSe2 (1.1-1.3 eV) and GaAs (1.42 eV). Literature confirms prior work on CuGaSe2 but limited reports on AgGa(S/Se/Te) combinations. Prioritize chalcopyrite-CuInSe2 prototype with substitutions {'Cu': ['Ag'], 'In': ['Ga', 'Al'], 'Se': ['S', 'Te']} to form novel AgGaS2, AgInTe2, CuAlS2 families.

## [hypothesis] iteration 2 — 2026-10-12 06:27 UTC

Hypothesis: AgGaS2 is documented in literature (2021 thin-film study), but prior work focused on nanostructures rather than bulk crystals. For 1.4 eV target, focus on unexplored combinations: (1) Chalcogen expansion: replace S with Te to increase band gap (AgGaTe2: estimated 1.5-1.7 eV from Vegard's law). (2) Dual cation substitution: Combine Ga/Al and Cu/Ag substitutions to engineer flat band edges. Propose expanding substitution space to {'Cu': ['Ag'], 'Ga': ['Al','In'], 'S': ['Se','Te']} while retaining chalcopyrite prototype. Novel candidates like AgInTe2 (predicted 1.3-1.5 eV) and CuAlS2 (1.2-1.4 eV) likely unexplored due to traditional focus on Cu/In/Se. Filter out known AgGa(S/Se) compounds to concentrate budget on novel combinations.

## [hypothesis] iteration 3 — 2026-10-12 06:43 UTC

Hypothesis: The Cu2ZnSnS4 (kesterite) prototype is well-characterized but has limited band gap tunability due to S/Se anion limitations. To reach 1.4 eV with stability, propose (1) Zn → Mg (ionic radius 0.66 Å vs 0.74 Å, +2 oxidation state) to reduce structural strain during chalcogen substitution and (2) Sn → Ge (1.22 Å vs 1.4 Å) to increase band gap via valence band modulation, paired with (3) S/Se → Te (ion radius 1.84 Å) for gradient anion substitution. The 2022 Cu2MgGeS4 study confirms synthetic feasibility of this family but lacks exploration of Te-chalcogen variants. Expect novel Cu2MgGeTe2 (1.4-1.6 eV from Vegard's law) to hit target with energy above hull <0.05 eV/atom due to Mg/Ge ionic size complementarity. Filter out Cu2MgGeS4 (known) and focus on Te-comprising variants as unexplored combinations.

## [hypothesis] iteration 4 — 2026-10-12 07:00 UTC

Hypothesis: Zincblende GaInSb family has minimal prior study (literature search found no direct reports on band gap engineering in this system). To reach 1.4 eV target, propose (1) Ga/In cation substitution with Al/Ga (Ga: 1.20 Å vs Al: 1.22 Å, +3 oxidation state) to reduce valence band offset; (2) Sb anion substitution with As/P (Sb: 2.45 Å vs As: 2.25 Å vs P: 1.80 Å) to linearly interpolate band gap via Vegard's law. Zincblende-GaAs prototype with substitutions {'Ga': ['Al'], 'In': ['Ga'], 'Sb': ['As','P']} will generate novel AlGaSb, GaGaP candidates. Prioritize evaluation of GaGaP (predicted 1.3-1.5 eV from GaP (2.26 eV) and GaSb (0.7 eV) extrapolation) as most unexplored high-confidence candidate based on k-p perturbation theory principles.

## [hypothesis] iteration 5 — 2026-10-12 07:10 UTC

Hypothesis: Building on kesterite-Cu2ZnSnS4's partial success in iteration 3, focus on Mg/Ge/Te anion substitution. Replace Zn→Mg (0.66 Å vs 0.74 Å), Sn→Ge (1.22 Å vs 1.4 Å) to reduce structural strain, and S→Te (1.84 Å) to increase band gap via Vegard's law. The 2022 Cu2MgGeS4 study confirms feasibility but excludes Te variants. Expect Cu2MgGeTe4 to achieve 1.4-1.6 eV band gap with ΔH <0.05 eV/atom due to Mg-Ge-Te ionic size complementarity. Filter out Cu2MgGeS4 (known) to concentrate on novel Te-based candidates.
