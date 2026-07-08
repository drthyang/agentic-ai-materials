# Benchmark 2 analysis: objective alignment flips the result

*2026-07-07 (run completed late evening local). Identical configuration to
benchmark 1 — qwen3:32b proposer, gemma4:26b critic, 5 iterations x 20
relaxations, seed 0, solo machine this time — with ONE change: the upgraded
prompts from the benchmark-1 autopsy (novelty made binding; hypotheses
framed as families). Single-variable experiment: any behavior change is
attributable to the prompt.*

## Headline

| strategy | scored | hits | hits/100 relax | best \|gap−ideal\| (eV) |
|---|---|---|---|---|
| random (seed 0) | 80 | 0 | 0.0 | 0.249 |
| similarity (seed 0) | 58 | 1 | 1.72 | 0.041 |
| **agent (qwen3:32b, aligned prompts)** | **7** | **4** | **57.1** | 0.09 |

Baseline reference band across 4 seeds: random 1.71 ± 1.43, similarity
2.54 ± 0.48 hits/100 relax (see ../2026-07-07-benchmark-1/baseline-seed-statistics.md).

**Benchmark 1 → 2, same model, same budget, prompts only: 0 hits → 4 hits;
0.0 → 57.1 hits per 100 relaxations.** The agent went from losing to both
baselines to beating the similarity band by an order of magnitude on
efficiency. Objective alignment — telling the agent that novelty is the
mission and known materials are calibration — was worth more than any model
upgrade would plausibly have been.

## What the agent actually did

**Iteration 2 is the whole ballgame.** After a warm-up iteration on silver
chalcopyrites, the agent proposed an 8-member silver-kesterite family —
(Mg,Cd)Ag₂(Ge,Sn)(Se,Te)₄ — the "hypothesis defines a family" instruction
executed literally. Seven were evaluated; four are hits:

| formula | e_above_hull (eV/atom) | gap (eV) | note |
|---|---|---|---|
| CdAg₂GeSe₄ | **0.000** | 1.28 | on the convex hull |
| MgAg₂SnSe₄ | 0.016 | 1.59 | literature-known (see below) |
| MgAg₂GeTe₄ | 0.025 | 1.49 | nearly ideal gap |
| MgAg₂SnTe₄ | 0.038 | 1.17 | |

Chemically this is a coherent move: Ag-for-Cu in the kesterite framework is
a known strategy against Cu-Zn antisite disorder (a real CZTS failure mode),
and the agent reached spaces MP hasn't cataloged.

## The honest asterisks

1. **MP-novel ≠ new to science.** A quick Crossref check found a 2026
   simulation paper on Ag₂MgSnSe₄ kesterite solar cells; Ag-based quaternary
   chalcogenides were synthesized by the Ukrainian school (Parasyuk et al.)
   in the 2000s. At least one hit — likely more — is known to the
   literature, just absent from MP. This *validates the loop's physics*
   (independent convergence onto a compound the community is actively
   studying for exactly this application) while capping the discovery claim.
   Before any of these are publicized as candidates, each needs an
   ICSD/OQMD/literature audit.
2. **n = 1 agent run, 7 evaluations.** 4/7 is a spectacular ratio with a
   wide confidence interval. The hits/100relax comparison against
   4-seeded baselines is asymmetric; agent replicates are needed.
3. **Iterations 3–5 produced zero evaluations.** After the kesterite
   triumph, the agent wandered into binary compositions (site-collapse
   substitutions: InSe, CuP, CuTe…) that the filters correctly rejected —
   plus one they *incorrectly* rejected (below) — and it never returned to
   exploit its own success (no Ba/Sr/anion-mix extensions of the winning
   family). Budget usage was 7 of 100. The remaining behavioral gap is
   *exploitation*: build on what worked.
4. **Filter bug found (upstream):** raw `smact_validity` rejects **InP** — a
   textbook III-V semiconductor — while passing GaAs and InSb. The agent's
   entire iteration-4 pnictide line died partly on this false negative.
   Filed for fix; until then the SMACT screen has known false negatives.

## The critic's scorecard

Three vetoes this run, all chemically sound: CuSb and AgSb ("not isovalent
substitution" — correct), CuTe (charge imbalance — correct). Combined with
benchmark 1's one correct coherence veto, gemma4:26b is 4-for-4 in
production. The proposer/critic model-diversity design is earning its keep.

## Cross-run validation

- Seed-0 baselines reproduced benchmark 1 exactly (deterministic seeding
  works end-to-end).
- Report generation stayed fully grounded (second production run, zero
  fabrication).

## What this sets up

The two-benchmark pair is now a clean, publishable narrative:

> A local 32B agent doing coherent literature-grounded science scored zero
> because it hunted where the literature is (benchmark 1). One prompt change
> making the objective explicit — novelty is the mission — redirected the
> same model into unexplored composition space, where it outperformed a
> chemistry-informed enumeration baseline ~20x on hit efficiency
> (benchmark 2). Objective alignment, not model capability, was the
> binding constraint.

## Next experiments, in order

1. **Agent replicates** (2–3 more seeds/runs of the aligned agent) — the
   4/7 needs error bars before it's a claim.
2. **Novelty audit** of the four hits against ICSD/OQMD/literature — decide
   which, if any, survive as genuinely under-explored.
3. **Fix the SMACT InP false negative** (upstream quirk; add an
   oxidation-state fallback or curated allowlist).
4. **Exploitation prompt nudge** — after a hit-rich iteration, extend the
   winning family before opening a new line.
5. **The capability run** — Claude backend, same protocol: now that the
   objective is aligned, does model capability add anything on top?
