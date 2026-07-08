# [DRAFT] Objective alignment, not model capability, unlocks LLM-agent materials discovery on a laptop

*Working draft. Markdown now, convert to LaTeX at submission. Every claim
links to a results/ artifact — keep it that way.*

**Title options** (pick at submission):
1. Objective alignment, not model capability, unlocks LLM-agent materials
   discovery on a laptop *(the finding)*
2. What does an AI materials scientist need: capability or a well-posed
   objective? *(the question)*
3. Benchmarking a local LLM discovery agent against the baselines nobody
   runs *(the methodology flag)*

**Target venues:** Digital Discovery (primary) · npj Comput. Mater. ·
AI4Science workshop (fast visibility). arXiv first regardless.

---

## Abstract (draft)

Large-language-model agents are widely proposed as autonomous materials
scientists, but are rarely evaluated against controls. We built a closed-loop
discovery agent that runs entirely on consumer hardware — a local 32B-parameter
proposer, an independent 26B critic, and physics-grounded tools (universal
interatomic potential relaxation, convex-hull thermodynamics, surrogate band
gaps) — and benchmarked it against random and chemical-similarity substitution
baselines at identical compute budgets on a photovoltaic-absorber mission.
The naive agent performed coherent, literature-grounded science yet scored
zero: it searched exclusively in known chemical space (the "known-materials
trap"). A single prompt-level change making novelty an explicit, binding
objective — with no model or budget change — raised hit efficiency from 0 to
32 ± 18 hits per 100 relaxations across three replicates, versus 3.0 ± 0.6
for the strongest baseline (complete separation, exact rank p ≈ 0.006). All
replicates independently converged on the Ag₂(II)(IV)(VI)₄ kesterite family;
two predicted on-hull members correspond to a recently synthesized compound
and an independently DFT-studied photovoltaic candidate, and two (Mg
tellurides) appear unreported. In a hold-out test with three known
photovoltaic absorbers masked from all database tools, the agent re-derived
AgGaSe₂ through its own hypothesis chain in 14 relaxations — five times
fewer than the enumeration baseline needed to re-find one. A second mission
(heavy-metal-free quantum-dot emitters) ran with zero code changes,
transferring the discovered kesterite family across gap windows via anion
substitution. Our results suggest that for LLM discovery agents,
objective specification is a stronger lever than model scale, and that
controlled baselines — absent from most agentic-discovery reports — are
essential to measuring either.

---

## Claims → evidence map (the paper's skeleton)

| # | claim | evidence | artifact |
|---|---|---|---|
| C1 | A fully local LLM agent can run closed-loop, physics-grounded discovery | system + campaigns | repo; WALKTHROUGH.md |
| C2 | Un-aligned, it does real science but zero discovery (known-materials trap) | benchmark 1 autopsy: all 10 candidates known; coherent notebook | results/2026-07-07-benchmark-1/ |
| C3 | Objective alignment alone flips the outcome | benchmark 2: same model/seed/budget, prompts only, 0→4 hits | results/2026-07-07-benchmark-2/ |
| C4 | The advantage replicates and separates from baselines | 3 runs: 57.1/22.2/16.7 vs similarity 3.01±0.62 (n=8), p≈0.006 | results/2026-07-08-replication/ |
| C5 | The found chemistry is real | CdAg₂GeSe₄ synthesized externally; MgAg₂SnSe₄ DFT literature; convergent family across runs | novelty-audit.md |
| C6 | The loop re-finds hidden known materials | agent re-found AgGaSe₂ blind (it3, 14 relax); similarity re-found CuGaSe₂ (79 relax); random 0/3 | results/2026-07-08-rediscovery/ |
| C7 | The architecture generalizes across missions via config | QD mission ran unchanged; agent pattern directional (2 hits/3 evals, small-n caveat); similarity produced 3 on-hull QD candidates | results/2026-07-08-qd-emitter/ |
| C8 | Honest failure catalog | fabricated reports (fixed by grounding), critic chemistry errors (fixed by model diversity), SMACT InP false negative, budget timidity | analyses passim |

## Section outline

1. **Introduction** — agentic-discovery hype vs the validation critique
   (GNoME/Cheetham-Seshadri, A-Lab/PRX Energy); the missing-controls problem;
   our question: what actually limits an LLM discovery agent?
2. **System** — Fig. 1 architecture; tools/budgets-in-code design;
   proposer/critic model diversity; notebook-as-memory; ground-truth report
   generation. (Condensed WALKTHROUGH §§1–3.)
3. **Benchmark protocol** — hit definition; equal-compute baselines; seeds;
   one-variable-at-a-time; novelty via MP + literature audit. (WALKTHROUGH §5.)
4. **Results**
   4.1 The known-materials trap (benchmark 1)
   4.2 Objective alignment flips the result (benchmark 2)
   4.3 Replication and statistics (Fig. 2)
   4.4 Convergent chemistry + external validation (Fig. 3, audit table)
   4.5 Rediscovery [TBD] · 4.6 Second mission [TBD]
5. **Failure catalog** (its own section — this is the paper's credibility
   signature): fabrication, critic errors, filter false negatives, budget
   underuse, timeout fragility. What each cost and how each was caught.
6. **Limitations** — surrogate error bars; MP-novelty weakness; n=3 agent
   replicates; single model family tested; synthesizability unaddressed
   beyond hull distance.
7. **Discussion** — objective alignment as the cheap lever; implications for
   "AI scientist" claims; what a capability ladder (local→frontier) would
   test; benchmark release for discovery agents.

## Figures

- **Fig. 1** — architecture / one-iteration trace (redraw WALKTHROUGH §1
  diagram properly).
- **Fig. 2** — the money plot: per-run hits/100relax; baseline band (n=8 each)
  vs 3 agent runs; log y-axis. Data ready in results/.
- **Fig. 3** — gap-vs-hull map of all scored candidates across runs, target
  box shaded, Ag-kesterite family highlighted, symbols by run (shows
  convergence). Data in run DBs.
- **Table 1** — benchmark 1 vs 2 vs replicates summary. **Table 2** —
  novelty audit of hits.

## Writing conventions

- "Candidates for validation", never "discoveries".
- Every number cites its results/ file; no number appears only in prose.
- The failure catalog stays in the main text, not supplementary — it's the
  differentiator.

## TODO

- [x] Fold in rediscovery result (C6) — done, see §4.5 source material in results/2026-07-08-rediscovery/
- [x] Fold in QD-emitter result (C7) — done, results/2026-07-08-qd-emitter/
- [ ] User: ICSD/OQMD check on MgAg₂GeTe₄, MgAg₂SnTe₄ → upgrades or kills
      the "unreported" language in the abstract
- [ ] Decide: Claude capability run in v1 or follow-up?
- [ ] Fig. 2/3 generation script (paper/figures.py) from run DBs
- [ ] Methods details: CHGNet/MEGNet versions, MP thermo-type pinning,
      uncorrected-energy hull comparison (from scoring.py docstrings)
