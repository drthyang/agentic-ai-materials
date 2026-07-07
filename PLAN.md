# Agentic AI for Materials Discovery — Build Plan

## The idea

Build a **closed-loop "AI materials scientist"**: an agent (or small team of agents)
that autonomously proposes candidate materials, screens them with real
computational-chemistry tools, learns from the results, and iterates — then writes
up its findings like a research report.

**Default discovery mission** (configurable): *find novel, thermodynamically stable
semiconductor compositions with a band gap near 1.4 eV* — the sweet spot for
single-junction photovoltaic absorbers. This target is ideal for a first build
because band gap and stability data are abundant (Materials Project) and cheap
surrogate models exist, so the loop can run end-to-end on a laptop with no DFT.

Alternative missions the same architecture supports later: battery cathode
candidates (high voltage, Li mobility), thermoelectrics (low thermal conductivity),
MOFs for CO₂ capture.

## Why this is interesting

- It's a real instance of the "AI scientist" pattern: hypothesize → experiment →
  observe → revise, not just a chatbot wrapper around a database.
- The agent's "experiments" are genuine physics-grounded computations (ML
  interatomic potentials, convex-hull stability analysis), so success is
  objectively measurable: *did it find candidates not in the known database that
  the surrogate models say are stable and on-target?*
- Great demo material: live dashboard of the agent exploring composition space,
  with a lab notebook it writes as it goes.

## Architecture

```
┌─────────────────────────────────────────────────────┐
│  Orchestrator (Claude via Anthropic API, tool use)   │
│  plan → propose → screen → evaluate → reflect loop   │
└──────────────┬──────────────────────────────────────┘
               │ tools
   ┌───────────┼────────────────┬─────────────────┐
   ▼           ▼                ▼                 ▼
 Knowledge   Candidate       Evaluation        Notebook
 - Materials  generation      - CHGNet/MACE     - lab_notebook.md
   Project   - element         relaxation +     - candidate DB
   API         substitution    formation energy   (SQLite)
 - literature - SMACT charge- - convex hull     - plots/reports
   search      balanced enum    (pymatgen)
              - agent's own   - band gap
                hypotheses      surrogate (MEGNet)
```

**Core loop (one "campaign iteration"):**
1. **Hypothesize** — agent reviews notebook + prior results, states a chemical
   hypothesis ("Se-substituted chalcopyrites in the I-III-VI₂ family may…")
2. **Propose** — generates 10–50 candidate compositions/structures via
   substitution on known prototypes (SMACT filter for charge balance / electronegativity sanity)
3. **Screen** — cheap filters first (novelty check against MP, SMACT), then
   ML-potential relaxation (CHGNet or MACE-MP) → formation energy → energy above
   convex hull; band-gap surrogate on survivors
4. **Evaluate & reflect** — agent analyzes which hypotheses paid off, updates its
   notebook, decides next direction (exploit vs explore)
5. **Report** — after N iterations, writes a research summary with ranked
   candidates, plots, and honest caveats

## Tech stack

| Layer | Choice | Notes |
|---|---|---|
| Agent runtime | Claude Agent SDK (Python) | tool use, subagents, memory out of the box |
| Model | claude-sonnet-5 for the loop, claude-fable-5 for reflection/reports | cost-conscious split |
| Materials data | `mp-api` (Materials Project) | free API key |
| Structure toolkit | `pymatgen`, `ase` | manipulation, convex hulls, prototypes |
| Composition sanity | `smact` | charge-balance / oxidation-state filters |
| ML potential | `chgnet` (or `mace-torch`) | relaxation + energies, CPU-friendly |
| Band gap surrogate | `matgl` (MEGNet pretrained) | fast property prediction |
| Storage | SQLite + markdown notebook | simple, inspectable |
| Dashboard (stretch) | FastAPI + simple frontend, or streamlit | watch the agent explore |

## Build phases

### Phase 0 — Skeleton & scope (½ day)
- Repo layout, `pyproject.toml` (uv), config file for the "mission" (target
  property, ranges, element palette, budget per iteration)
- Get Materials Project API key; smoke-test `mp-api`, `chgnet`, `smact` installs

### Phase 1 — Tool layer, no agent yet (1–2 days)
Deterministic Python functions, each unit-tested standalone:
- `search_known_materials(criteria)` — MP query
- `generate_candidates(prototype, substitutions)` — structure substitution
- `filter_candidates(comps)` — SMACT + novelty check vs MP
- `relax_and_score(structure)` — CHGNet relax → formation energy → e_above_hull
- `predict_band_gap(structure)` — MEGNet surrogate
- `notebook_write / notebook_read`, `candidates_db` CRUD
Milestone: a hand-written script chains these end-to-end for one known family
(e.g., CuInSe₂ substitutions) and produces sensible numbers.

### Phase 2 — Single-agent loop (2–3 days)
- Wire tools into Claude Agent SDK; system prompt encodes the scientist persona,
  mission config, and budget discipline
- Implement the hypothesize→propose→screen→reflect loop with iteration caps and
  cost guardrails (max structures relaxed per iteration)
- Persist everything: every hypothesis, candidate, score, and decision
Milestone: `python -m matdiscover run --iterations 5` completes a campaign
unattended and the notebook reads like coherent science.

### Phase 3 — Make it rigorous (2 days)
- Baselines to beat: random substitution and greedy element-similarity
  substitution with the same compute budget — does the agent's hypothesis-driven
  search find more/better candidates?
- Metrics: # novel candidates with e_above_hull < 50 meV/atom and gap in
  1.1–1.7 eV, per unit of compute
- Hold-out validation trick: hide a slice of known MP materials, see if the agent
  "rediscovers" them
Milestone: a results table + plot showing agent vs baselines.

### Phase 4 — Multi-agent + polish (2–3 days, pick favorites)
- **Critic agent**: reviews proposals before compute is spent (charge balance
  reasoning, synthesizability skepticism)
- **Literature agent**: web-search grounding for hypotheses ("has anyone made this?")
- Live dashboard: composition-space map, convex-hull plots, notebook stream
- Final auto-generated research report (markdown → PDF)

### Stretch ideas
- Active learning: fit a cheap Gaussian-process/BO layer over explored
  composition space; the agent uses it as an acquisition-function tool
- DFT validation hook: export top-5 candidates as VASP/Quantum ESPRESSO inputs
- Swap missions via config only, no code changes — proves generality

## Risks & mitigations

- **Surrogate model error** (~0.1 eV formation energy, band gaps worse):
  report uncertainty bands; frame outputs as "candidates for validation," never
  "discoveries"
- **Agent proposes garbage at scale**: hard SMACT/novelty gates before any
  compute; per-iteration budget caps
- **CHGNet slow on big cells**: cap at ≤ ~50 atoms/cell, prototype-based
  substitution keeps cells small
- **API costs**: sonnet for the loop, cache the MP queries, log token spend

## Definition of done (v1)

A single command runs a 10-iteration campaign that: stays within budget, finds
≥ a handful of novel on-target candidates, beats the random baseline, and emits a
readable research report with plots — all reproducible from a fresh clone.
