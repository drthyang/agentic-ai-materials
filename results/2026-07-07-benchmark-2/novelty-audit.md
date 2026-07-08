# Novelty audit of the benchmark-2 hits

*2026-07-07 evening. Web + Crossref literature check on the four
MP-novel hits from the aligned-agent run. "MP-novel" means no Materials
Project entry; this audit asks what the rest of science knows. A definitive
claim would additionally require ICSD and OQMD lookups (no API integration
yet — manual check recommended before any publicizing).*

## Verdicts

| hit | our prediction | literature status | verdict |
|---|---|---|---|
| **CdAg₂GeSe₄** | on hull (0.000), gap 1.28 | **Synthesized** — recent mechanochemical synthesis, described as "a previously unknown quaternary chalcogenide", wurtzstannite Pmn2₁ | Known (recently). **Retrospective validation**: the loop's top-stability call is a compound experimentalists just made. |
| **MgAg₂SnSe₄** | hull 0.016, gap 1.59 | **DFT-studied, not synthesized** (as far as found) — ab-initio PV studies since ~2020; 2025–26 device simulations report high projected efficiencies | Computationally known. Independent-convergence validation; synthesis apparently open. |
| **MgAg₂GeTe₄** | hull 0.025, gap 1.49 | **No direct literature found.** Only adjacent analogs (Ag₂BeSnX₄, Ag₂MgSn(S,Se)₄) are studied | **Candidate-novel** pending ICSD/OQMD check. |
| **MgAg₂SnTe₄** | hull 0.038, gap 1.17 | **No direct literature found** — Te members of this family appear unstudied | **Candidate-novel** pending ICSD/OQMD check. |

Related family datapoint: Ag₂CdSnSe₄ (not among our hits) has been known
since 2001 with a 2024 structural revision — the Ag-kesterite family broadly
is real, synthesizable chemistry.

## What this means

1. **The loop's physics is validated twice over.** Its strongest stability
   claim (CdAg₂GeSe₄ on the hull) corresponds to a real compound made by
   mechanochemistry; its second hit matches an independent DFT literature
   that projects strong PV performance for the same composition. An agent +
   surrogate stack that *retrodicts* current experimental and computational
   frontiers is doing something right.
2. **Two possible genuine discoveries.** The tellurides MgAg₂GeTe₄ and
   MgAg₂SnTe₄ have no findable literature. If ICSD/OQMD come back empty,
   these are publishable as new predicted near-stable PV-window
   semiconductors (with all surrogate caveats).
3. **The agent found an active research frontier on its own.** Ag-based
   kesterites for PV are a live 2020s research direction; the agent, told
   only "novelty is the mission", navigated there in one iteration. The
   known-materials trap analysis from benchmark 1 and this outcome are two
   sides of the same coin: the model knows where the frontier is — the
   objective determines whether it stops at it or steps past it.
4. **Metric refinement for benchmark 3+:** "not in MP" was a reasonable v1
   novelty proxy but underestimates the literature. Options: add an OQMD
   check, an ICSD lookup where licensing allows, or a Crossref-based
   auto-audit in the metrics pipeline (search each hit formula, flag ones
   with direct matches).

## Sources

- CdAg₂GeSe₄ / Ag₂CdSnSe₄ synthesis and structures:
  [mechanochemical synthesis of multinary selenides (TU Berlin)](https://depositonce.tu-berlin.de/items/51e3aaa2-66ce-42bd-b0c5-eb8cc971d2de),
  [structural evaluation of Ag2CdSnSe4 (Z. Naturforsch. B, 2024)](https://www.degruyterbrill.com/document/doi/10.1515/znb-2024-0056/html?lang=en),
  [Ag2Se–CdSe–SnSe2 phase system (2001)](https://www.sciencedirect.com/science/article/abs/pii/S092583880101845X)
- Ag₂MgSn(S,Se)₄ DFT/PV studies:
  [ab-initio study, Solar Energy ~2020](https://www.sciencedirect.com/science/article/abs/pii/S0038092X20309403),
  [Ag2MgSnSe4 device simulation, 2025–26](https://link.springer.com/article/10.1007/s11082-025-08521-5)
- Adjacent family (Ag₂BeSnX₄) DFT studies:
  [J. Nanoparticle Research 2025](https://link.springer.com/article/10.1007/s11051-025-06303-4),
  [kesterite solar cell modeling](https://www.sciencedirect.com/science/article/abs/pii/S0038092X23008289)
- Quaternary IV-selenide structures:
  [Inorg. Chem. 2024](https://pubs.acs.org/doi/10.1021/acs.inorgchem.4c00363)
