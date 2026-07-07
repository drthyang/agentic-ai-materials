# Benchmark 1 analysis: local agent vs baselines (PV absorber mission)

*2026-07-07. First full agent-vs-baseline comparison. Configuration:
qwen3:32b proposer + gemma4:26b critic (both local via Ollama), 5 iterations
x 20 relaxations budget per strategy, single seed (0). Artifacts in this
folder; raw DBs in `data/benchmark/20260707-1212/` (local machine only).*

## Headline result

| strategy | scored | hits | hits/100 relax | best \|gap−ideal\| (eV) |
|---|---|---|---|---|
| random | 80 | 0 | 0.0 | 0.249 |
| similarity | 58 | **1** | **1.72** | **0.041** |
| agent (qwen3:32b) | 10 | 0 | 0.0 | 0.186 |

*(hit = converged + gap in [1.1, 1.7] eV + ≤0.05 eV/atom above hull + not a
confirmed-known material)*

**The local agent lost to the similarity baseline — but the autopsy says the
interesting part is *why*, and it isn't "the model is dumb."**

## Finding 1: the agent did real science and found real materials — all of them already known

The notebook (this folder) shows five coherent, literature-grounded
iterations: Ga-for-In chalcopyrites → S anion tuning → Te (falsified:
CuGaTe₂ came out metallic at 0.11 eV) → a deliberate pivot to kesterites →
Cd/Ge kesterite substitutions. Ionic radii and electronegativities quoted are
correct; the falsification of the Te hypothesis is honest and the pivot is
exactly what a scientist would do.

But **every one of its 10 scored candidates is a known material**
(`novel=0`): CuGaSe₂, CuGaS₂, Cu₂CdSnS₄, Cu₂ZnGeS₄… Its best find,
CdCu₂SnS₄ (gap 1.69 eV, 0.011 eV/atom above hull), is inside the target
window and near-stable — a would-be hit, disqualified for being known.

**The known-materials trap:** literature grounding pulls the agent toward
famous, well-studied chemical space — which is precisely where nothing
novel remains. The blind baselines wandered into unknown territory
(CdCuSe₂) and scored. Under a novelty metric, the agent's best feature
(reading the literature) became its handicap. This is the most publishable
observation of the run.

Contributing mechanical cause: `propose_candidates` *told* the agent
`novel_vs_materials_project: false` for every candidate, and the agent spent
relaxations on them anyway. The mission prompt says "find novel materials"
once; nothing in the workflow makes novelty binding. Fixable (see next
steps).

## Finding 2: massive budget underuse

The agent used 10 of 100 allowed relaxations (baselines: 80 and 58). Small
hypothesis-driven batches are philosophically right, but 2–6 evaluations per
iteration cannot compete statistically with 20. The efficiency column
(hits/100 relax) partially corrects for this, but zero hits is zero.
A well-calibrated agent should propose broader batches per hypothesis
(one hypothesis ≠ one compound — it defines a *family*).

## Finding 3: the critic earned its keep (barely, but correctly)

Gemma issued exactly one veto: iteration-2's InCuS₂, reasoning it "does not
test the proposer's stated hypothesis" (the hypothesis was about S-for-Se
substitution in Cu–Ga chemistry; InCuS₂ tests nothing new). That's a
*coherence* veto, not a chemistry veto — correct, and a kind of review we
didn't explicitly design for. No wrong vetoes observed. One veto in five
iterations also means the critic is not the bottleneck.

## Finding 4: report grounding worked in production

Qwen's auto-generated final report (this folder) is fully faithful: every
number matches the database, hypotheses map to real iterations, failed lines
are called failures. The fabrication failure mode from the Phase-2 live test
did not recur after ground-truth injection. This subsystem is done.

## Finding 5: the similarity baseline is a serious opponent

Its hit, **CdCuSe₂** (gap 1.70 eV, 0.003 eV/atom above hull, no MP entry),
was found by dumb group/period-distance substitution. It also *re-found* two
known PV materials without being told about them: CuSbSe₂ (hull 0.000, gap
1.29 — an actively researched absorber) and CdCu₂SnS₄ (the same compound the
agent reached by literature reasoning — convergent evidence it's a sensible
lead). Chemistry-informed enumeration over a good prototype library is
strong; any agent claim must beat *this*, not random.

## Replicate note

An accidental concurrent duplicate run (partial, killed at iteration ~3)
reproduced the agent's qualitative behavior: same chalcopyrite opening, same
small batches, same all-known-materials pattern (see
`replicate-partial-agent_notebook.md`). Weak but real evidence the behavior
is systematic, not seed luck.

## Threats to validity

- **Single seed, single run** per strategy — no error bars yet.
- **Three concurrent benchmark processes** shared one Ollama instance
  (accidental triple-start). Slowed wall-clock ~2x; should not bias
  *quality*, but iteration timings from this run are not representative.
- **Novelty = "not in Materials Project"** — CdCuSe₂ may exist in
  ICSD/OQMD/literature; not yet checked. Do this before publicizing.
- Surrogate error bars apply to everything (CHGNet hulls ±~0.05 eV/atom,
  MEGNet gaps worse).

## Decisions taken (see repo commits following this analysis)

1. **Prompt upgrades:** make novelty binding ("known materials are
   calibration, not discoveries — do not spend relaxations on novel=false
   candidates except deliberate calibration") and push batch sizing
   ("a hypothesis defines a family; propose 10–30, evaluate the most
   informative 8–15").
2. **Benchmark lockfile** to prevent the concurrent-run footgun.
3. **Multi-seed baseline statistics** (no LLM needed) for error bars.
4. **Queued for next machine-idle window:** rerun the agent leg with the
   upgraded prompts, solo Ollama — benchmark 2.

## The writeup angle this run supports

"A locally-run LLM agent does coherent, literature-grounded materials
science — and that is exactly why it fails a novelty-scored benchmark that
blind enumeration passes." Capability isn't the only axis; *objective
alignment* (knowing what counts as success) is separately load-bearing.
Benchmark 2 tests whether prompt-level objective alignment closes the gap;
the Claude-backend run then tests whether model capability moves it further.
