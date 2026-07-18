# Roadmap

PLAN.md (phases 0–4: tool layer, agent loop, baselines, critic/literature/
dashboard) is fully built. This roadmap covers what comes next. Guiding
principles carried forward:

- **Config over code** — new science targets should be new mission YAMLs.
- **Budgets and gates live in code**, never in prompts.
- **Reports are ground-truth-injected**, never model-recalled.
- **Every agent claim gets a baseline** — no result without a control.

---

## Short term (days–weeks): finish the science the machine was built for

- **Headline benchmark** *(in progress)* — agent (qwen3:32b) vs random vs
  similarity at equal compute; gemma4:26b as critic. Repeat with 3+ seeds for
  error bars; audit critic vetoes against outcomes (were vetoed candidates
  actually bad?).
- **Rediscovery validation** — populate `evaluation.holdout_formulas` with
  known PV absorbers (CuGaSe2, AgGaSe2, CuInS2), measure rediscovery rate.
  This is the credibility experiment.
- **Hybrid-critic and Claude-agent runs** — same benchmark with
  `critic.backend: anthropic`, then `--backend anthropic`: how much does
  discovery improve with model capability? (The capability-vs-outcome curve
  is the most interesting writeup angle.)
- **CdCuSe2 dossier** — literature deep-dive + DFT validation export
  (`athanor export`: VASP/Quantum ESPRESSO inputs for top candidates).
- **Mission gallery** *(started, see config/missions/)* — display-industry
  targets that work with today's surrogates:
  - `qd-emitter.yaml` — heavy-metal-free quantum-dot emitter candidates
    (visible-range gaps, Cd/Pb/Hg excluded — the RoHS problem QD makers
    actually have).
  - `tco.yaml` — transparent conductors for display electrodes (wide-gap
    stable oxides; transparency+stability screen only — see caveats inside).
- **CI** — GitHub Actions running the hermetic test suite (fast, no GPU).

## Mid term (1–2 months): widen what the agent can sense and propose

- **Quantum-adjacent screening with existing surrogates** — CHGNet predicts
  magnetic moments: add a `predict_magnetism` tool and a spintronics/magnet
  mission (e.g. stable ferromagnetic semiconductors). Wide-gap host screening
  (SiC/BN-like chemistries) as groundwork for qubit-host work.
- **Multi-fidelity validation ladder** — cheap screen (current stack) →
  tighter ML potential (e.g. MACE-MP-large) on survivors → DFT export for
  finalists. Uncertainty from model disagreement.
- **Active learning** — fit a cheap GP/BO surrogate over explored composition
  space; expose it to the agent as an acquisition-function tool ("where is
  expected improvement highest?").
- **Beyond fixed prototypes** — larger prototype library pulled from MP
  structure types; optionally symmetric random structures (PyXtal) as an
  exploration tool.
- **Agent architecture** — planner/proposer/critic separation; cross-campaign
  memory (what did *previous* campaigns learn about this chemistry?);
  dashboard panels for critic-veto audit and multi-campaign comparison.

## Long term (a quarter+): properties that need new surrogates or real DFT

- **Quantum materials proper** — the interesting targets need capabilities we
  don't have yet, roughly in order of tractability:
  1. *Optical/dielectric surrogates* (absorption spectra for emitters and
     transparency — ML models exist to evaluate)
  2. *Carrier effective masses / dopability* (needed to make the TCO mission
     honest; band-structure-level surrogates or cheap DFT)
  3. *Defect formation energies* (qubit hosts, phosphor activators — likely
     needs DFT in the loop, not surrogates)
  4. *Topological classification* (symmetry-indicator pipelines on DFT bands)
  5. *Superconductor Tc* (exploratory; published ML models are unreliable —
     treat as a research question, not a screen)
- **DFT in the loop** — queue finalists to a real DFT engine (local QE or
  cloud) and feed results back into campaign memory automatically.
- **Generative proposals** — a diffusion/VAE structure generator (e.g.
  CDVAE-family) as an additional candidate-generation tool next to
  substitution; the agent chooses which generator fits the hypothesis.
- **Write-up** — the capability-vs-outcome study (local vs hybrid vs Claude,
  with baselines and rediscovery rates) is a self-contained blog post or
  workshop paper once the benchmark matrix is run.
