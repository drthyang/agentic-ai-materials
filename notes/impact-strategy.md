# Impact strategy

*Started 2026-07-07, during the first headline benchmark run.*

## The strategic read of the field

Big labs won the scale game (GNoME's millions of predictions, MatterGen's
generative design, foundation potentials from Meta/Microsoft). But scale made
the field's credibility problem worse, not better:

- **Predicted-stable ≠ makeable.** The Cheetham–Seshadri critique of GNoME
  (many "new" materials are dopant variants, symmetry-broken duplicates, or
  implausible compositions); PhononBench showing ~26% average dynamical
  stability across generative models; recent work showing computed proposals
  drift away from the structural patterns of everything humans have actually
  synthesized.
- **Most agentic-discovery papers have no control group.** Demos, not
  experiments.
- **The bottleneck moved** from generating candidates to *trusting and
  validating* them.

**Therefore: the field is drowning in candidates and starving for rigor.**
Individual leverage = trustworthy + fast + specific, not big.

## Assets this project already has

1. **Controls** — equal-compute baselines (random, similarity) baked into the
   benchmark; almost nobody in agentic-materials can back their claims this way.
2. **Local-first** — a complete discovery loop on a laptop, zero API cost.
   Accessibility story no cloud demo tells; also the substrate for the
   capability-scaling experiment.
3. **The capability question** — the harness measures discovery outcomes vs
   model intelligence (Qwen → hybrid critic → Claude). Open research
   question, not a demo.
4. **Honest failure records** — fabricated-report catch, backwards-critic
   catch, energy-scale bug: documented, fixed, testable. This *is* the brand.

## Impact paths, ranked by leverage-per-effort

1. **The methodology study** (~80% built). Benchmark matrix: {agent model} ×
   {critic config} vs baselines, ≥3 seeds, + rediscovery rates. Publish
   honestly, negative results included. Venues: Digital Discovery, npj
   Computational Materials, NeurIPS/ICLR AI4Science workshops. A rigorous
   negative beats an inflated positive.
2. **A public benchmark for discovery agents.** Matbench-discovery exists for
   potentials; nothing for agents. The rediscovery machinery (masked
   materials, fixed budgets, standard hit metric) is the seed. Owning the
   yardstick is historically the highest-leverage move in an ML subfield.
3. **Missions with constraints that matter** + a validation partner. Cd-free
   QD emitters, In-free TCOs, earth-abundant PV. One experimental group
   willing to attempt a 5-candidate shortlist turns software into science.
   Solution-processable chalcogenides are cheap to attempt.
4. **Open tooling + teaching.** "AI scientist on a laptop" writeups/talks.
   Amplifies everything above; not the core contribution by itself.

## Credibility pitfalls (the ways this field kills trust)

- Overclaiming: always "surrogate-level candidates pending validation."
- LLM memorization vs reasoning: local models have read every chalcopyrite
  paper; rediscovery partly measures recall. Discuss it; genuinely-novel hits
  are the unambiguous evidence.
- Novelty leakage: "not in Materials Project" ≠ new to science. Check
  ICSD/OQMD/literature before publicizing any candidate.
- Property overreach: stability + gap are defensible with current surrogates;
  mobility/defects/Tc are not. ROADMAP.md long-term list is the boundary.

## 90-day arc

| Weeks | Focus |
|---|---|
| 1–2 | Benchmark matrix (seeds, critic variants, one Claude run) + rediscovery experiment |
| 3–5 | Write-up: arXiv preprint + blog post + repo as artifact; share in MP community / AI4Science circles |
| 6–12 | Follow the reception: benchmark-suite play (methodology interest) or experimental-collab play (domain hit) |

## Standing decisions

- 2026-07-07: benchmark #1 = fully local (qwen3:32b proposer, gemma4:26b
  critic), 5 iterations. Hybrid/Claude variants after.
- Report generation stays ground-truth-injected; never revert to
  model-recalled summaries.
