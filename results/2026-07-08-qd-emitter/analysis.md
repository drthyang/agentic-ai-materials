# QD-emitter mission: the generality test

*2026-07-08, seed 8. The heavy-metal-free quantum-dot emitter mission
(config/missions/qd-emitter.yaml — gap 1.8–3.1 eV, Cd/Pb/Hg banned) run
through the identical benchmark with ZERO code changes. Question: does the
architecture generalize across science targets via config alone?*

## Result

| strategy | scored | hits | hits/100 relax | best \|gap−ideal\| (eV) |
|---|---|---|---|---|
| random | 51 | 1 | 1.96 | 0.009 |
| similarity | 62 | 5 | 8.06 | 0.044 |
| agent | 3 | 2 | 66.7 | 0.507 |

## Reading — with the caveats leading

1. **The infrastructure generalized perfectly.** New target windows, new
   palette, new veto list — one YAML file. Filters, physics, metrics,
   dashboards all just ran. Claim C7 (config-only generality) is supported
   at the *systems* level without qualification.
2. **The agent's efficiency pattern repeated directionally (66.7 vs 8.06)
   but on 3 evaluations — too thin to claim alone.** Its two hits are
   MgAg₂GeS₄ (hull 0.017, gap 1.89) and MgAg₂GeSe₄ (0.020, 1.86): it carried
   its PV-campaign kesterite knowledge into the new window and reused it.
   Interpretation cuts both ways — cross-mission transfer (the S/O anion
   swap to raise the gap into the QD window is correct chemistry) or
   family over-fixation. More runs would tell.
3. **The proposer struggled in unfamiliar space; the filters did their
   job.** 10 of 13 non-kesterite proposals were genuinely charge-imbalanced
   II–III–VI₂ compositions (ZnGaS₂, AlZnSe₂, chlorides) and died at SMACT
   for free. This is the guardrail architecture working: a weak proposal
   stream costs almost nothing.
4. **The wider gap window is easier for everyone** — similarity jumped from
   ~3 (PV) to 8.06 hits/100relax. Cross-mission efficiency numbers are not
   comparable; within-mission comparisons only.
5. **The practical output of the mission is arguably similarity's:** three
   ON-HULL QD-window candidates — Cu₂SnGeS₄ (gap 1.81), Cu₂SiSnS₄ (2.05),
   Cu₂SnSeS₄ (2.44) — plus ZnSn₃S₄ and ZnCu₂SeS₄ near-hull. A defensible
   shortlist of heavy-metal-free emitter candidates for a novelty audit,
   from 62 relaxations of dumb enumeration. The mission gallery idea pays
   off regardless of which strategy wins.

## For the paper

C7 supported (systems-level, unqualified; agent-level, directional with
small-n caveat). The MgAg₂Ge(S,Se)₄ cross-mission reuse is a nice discussion
point: the same family satisfies two different missions at different anions
— chemically sensible and exactly what a materials scientist would try.
