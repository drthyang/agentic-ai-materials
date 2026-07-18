# Walkthrough: how this all works

*One document to understand the entire project — the machine, the experiment
protocol, and everything run so far. ~15 minute read. Assumes materials
knowledge; explains the AI and protocol side.*

---

## 1. The mental model (one paragraph)

An LLM plays the role of a research scientist, but it can't touch anything
directly: every action goes through a fixed set of **tools** — Python
functions we wrote — that do the actual work (query databases, run physics,
write notes). The LLM reads tool results and decides the next call. Real
constraints (compute budgets, chemistry filters, what gets recorded) live
**in the tool code**, where the model can't talk its way around them. A
second LLM (the **critic**) reviews proposals before compute is spent. The
whole thing runs in **iterations** of the scientific method, keeps a lab
notebook as its memory, and is judged against **non-LLM baselines given the
exact same budget** — so "the AI helps" is a measured claim, not a demo.

```
        ┌─────────────── one iteration ───────────────┐
notebook → hypothesis → propose family → filters → critic → CHGNet/hull/gap
   ▲                     (SMACT, novelty)  (2nd LLM)         (the physics)
   └────────── observation + reflection ◄────── results ─────────┘
```

## 2. The cast

| role | what it is | file(s) |
|---|---|---|
| **Proposer** | qwen3:32b via Ollama (local). Hypothesizes, decides which tools to call | `src/athanor/llm/`, `agent/loop.py` |
| **Critic** | gemma4:26b — different model family on purpose. Reviews each evaluation batch *before* compute; vetoes are free | `agent/critic.py` |
| **Tools** | the agent's only hands: search MP, search literature, propose, evaluate, notebook I/O | `agent/tools.py` (schemas) over `tools/` (implementations) |
| **Physics** | CHGNet relaxation → formation energy → energy above MP convex hull; MEGNet (HSE fidelity) band gap | `tools/scoring.py` |
| **Filters** | SMACT charge balance + mission palette + duplicate check, applied before any compute | `tools/filters.py` |
| **The record** | append-only lab notebook (agent's memory between iterations) + SQLite ledger of every candidate ever considered | `notebook.py`, `db.py` |
| **Mission** | the science target as config: gap window, stability bar, element palette, budgets. Swap missions = swap YAML | `config/mission.yaml`, `config/missions/` |

## 3. One real iteration, step by step

This is iteration 2 of the benchmark-2 run (the one that produced the main
result), traced from the actual logs:

1. **Kickoff.** The loop sends the model a fresh, short prompt: mission,
   target, palette, budget. No conversation history — cross-iteration memory
   is the notebook, which keeps prompts small for local models.
2. `read_notebook` → the model reads its iteration-1 notes (silver
   chalcopyrites: gaps close but nothing novel enough).
3. `write_notebook(hypothesis)` → states: Ag-based *kesterites*
   (Ag₂-II-IV-VI₄) should combine CZTS-like tunability with unexplored
   composition space.
4. `propose_candidates(substitutions={Zn:[Mg,Cd], Sn:[Ge,Sn], S:[Se,Te]},
   prototype=kesterite)` → our code generates all 8 structures from the
   prototype geometry, rejects charge-imbalanced ones (SMACT), checks each
   against Materials Project for novelty, stores every proposal in SQLite,
   and returns the list with `novel: true/false` flags. The model never
   touches structure files — only formula strings.
5. `evaluate_candidates([...7 formulas...])` → **inside this tool**: the
   critic (gemma) reviews the batch first — anything vetoed is recorded and
   costs nothing; survivors get CHGNet relaxation, formation energy, hull
   distance (vs MP's GGA/GGA+U entries), and a band gap. Each evaluation
   decrements the iteration's relaxation budget (20). Results, including
   "gap in target window? near-stable?", go back to the model and to SQLite.
6. `write_notebook(observation / reflection)` → honest record: 4 of 7 in the
   target box, CdAg₂GeSe₄ on the hull.
7. Model replies with plain text instead of a tool call → iteration over.
   Next iteration starts at step 1 with a fresh prompt.

After the last iteration, the **final report** is generated with the full
notebook + database rows *injected into the prompt as ground truth* — the
model writes prose around real numbers. (Before this fix, qwen invented an
entire fictional campaign; see experiment log, benchmark 1 era.)

## 4. The numbers and their error bars

| number | meaning | trust level |
|---|---|---|
| `e_above_hull` (eV/atom) | distance above the MP convex hull, CHGNet energies both sides (uncorrected, GGA-scale) | ±~0.05; our "near-stable" bar is 0.05 |
| `band_gap_ev` | MEGNet multi-fidelity at HSE fidelity (index verified against Si) | screening-grade; ±0.3+ possible |
| `novel` | no entry with that reduced formula in Materials Project | **weakest link**: MP-novel ≠ new to science — always audit hits against literature/ICSD |
| **hit** | converged + gap in window + near-stable + not confirmed-known | the single success metric, identical for every strategy |
| **hits/100 relaxations** | hit efficiency per unit compute | the fair comparison when strategies spend different amounts |

## 5. The experiment protocol (why it's built this way)

- **Baselines:** every agent claim is compared to *random substitution* and
  *greedy chemical-similarity substitution* running the same filters, same
  scorer, same budget (5 iterations × 20 relaxations). Only the
  candidate-choosing strategy differs — so any performance gap is
  attributable to the strategy.
- **Seeds:** baselines are stochastic, so each is run at many seeds to get a
  mean ± std ("the band"). One run is an anecdote; the band is a measurement.
  Agent runs vary through LLM sampling instead — replicated by running the
  campaign multiple times.
- **One variable at a time:** benchmark 1 → 2 changed *only the prompts*
  (same model, seed, budget), so the outcome change is causally attributable.

## 6. The experiment log (everything run so far)

| # | when | what | result | analysis |
|---|---|---|---|---|
| 1 | 07-06 | build phases 0–2 (tools → agent loop), live qwen test | works; found+fixed: MP r2SCAN hull-scale bug, fabricated final report | commit history |
| 2 | 07-07 am | **benchmark 1**: agent vs baselines | agent 0 hits — did coherent science but only in *known* space (the "known-materials trap"); similarity 1 hit (CdCuSe₂) | `results/2026-07-07-benchmark-1/` |
| 3 | 07-07 | baseline seeds 1–3 (later 4–7) | random 1.38±1.15, similarity 3.01±0.62 hits/100relax (n=8) | `.../baseline-seed-statistics.md` |
| 4 | 07-07 pm | **benchmark 2**: same model, prompts made novelty-binding + families | **0 → 4 hits (57/100relax)**; silver-kesterite family; CdAg₂GeSe₄ on hull | `results/2026-07-07-benchmark-2/` |
| 5 | 07-07 | novelty audit of the 4 hits | 1 recently synthesized (validation!), 1 DFT-studied, 2 candidate-novel (Mg tellurides) | `.../novelty-audit.md` |
| 6 | 07-08 night | replicates attempt 1 | both died on a 300s timeout → backend hardened (retries, crash guard) | commit `2ea3ea8` |
| 7 | 07-08 | **replicates** (2 more agent runs) | 22.2 and 16.7 hits/100relax; **all 3 runs converge on the same Ag-kesterite family**; agent 32.0±17.9 vs similarity 3.01±0.62, p≈0.006 | `results/2026-07-08-replication/` |

**Current headline:** objective alignment (telling the agent novelty is the
mission) mattered more than model capability — the same local model went
from losing to a dumb baseline to beating it ~10× on hit efficiency, and the
chemistry it found is externally corroborated.

## 7. Commands

```bash
uv run athanor check                    # environment status
uv run athanor run --iterations 3      # one agent campaign
uv run athanor dashboard               # watch live (localhost:8517); --latest for benchmarks
uv run athanor benchmark --iterations 5 --seed N   # full comparison (~2h with agent)
uv run athanor benchmark --skip-agent  # baselines only (~10 min)
uv run pytest                              # 59 hermetic tests (no GPU/network)
```

## 8. Where things live

```
config/           mission.yaml (active) + missions/ (QD emitter, TCO)
src/athanor/  tools/ (physics+filters+search) · agent/ (loop, critic,
                  prompts, tool schemas) · llm/ (Ollama/Anthropic backends)
                  baselines.py · metrics.py · benchmark.py · dashboard.py
results/          committed analyses of every experiment (start here)
notes/            strategy, positioning, reading list
data/             gitignored: raw run DBs, caches, logs (local machine only)
PLAN.md           original build design (complete)  ·  ROADMAP.md  what's next
```

## 9. Open items

- Manual ICSD/OQMD check of MgAg₂GeTe₄ / MgAg₂SnTe₄ (the two possible
  genuine discoveries) — needs database access only a human has.
- SMACT falsely rejects InP (fix running in a separate session).
- Claude-backend capability run (needs ANTHROPIC_API_KEY).
- Preprint draft — all core claims now have support.
