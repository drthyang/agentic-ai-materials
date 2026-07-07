# Positioning: the full-stack materials scientist

*The problem this document solves: a skill set spanning crystal growth,
experiment planning, measurement, analysis, discovery, scripting, and
software engineering reads as "unfocused" to people trained to look for
one-domain depth. The fix is not to claim depth in a single lane — it is to
make the integration itself undeniable and visible.*

## The thesis

Agentic AI for science is the first field where the **integrator profile is
the scarce one**. Building a credible discovery loop requires, in one head:

- knowing why a hull energy or a PBE gap can't be trusted (materials depth),
- designing controlled experiments with budgets and baselines (scientific
  method),
- and shipping the software that runs unattended for hours (engineering).

Single-domain experts must form a three-person team to do what this profile
does alone. That is the story — and it can't just be *said*, it has to be
*shown*. This repo is the proof-of-work.

## What each part of the project evidences

| Skill claimed | Artifact that proves it |
|---|---|
| Materials judgment | GGA/r2SCAN energy-scale bug caught from one absurd number; HSE-fidelity choice verified against Si; mission palettes reflecting real constraints (RoHS, In supply) |
| Experimental design | Equal-compute baselines, seeded runs, rediscovery hold-outs, one shared hit metric |
| Scientific integrity | Fabricated-report catch → ground-truth-injected reports; backwards-critic catch → model-diversity fix; caveats in every artifact |
| Software engineering | Pluggable backends, budgets enforced in code, 54 hermetic tests, live dashboard, CI-ready |
| Communication | Lab notebooks, auto-generated reports, README/ROADMAP, (next) the write-up |

## Visibility plan — artifacts over adjectives

Every claim needs a public, linkable artifact:

1. **The repo itself** — pinned on GitHub, README written for a first-time
   visitor (done). The commit history *is* a portfolio: bugs found, fixed,
   tested, explained.
2. **The write-up** (weeks 3–5): arXiv preprint + accessible blog version.
   The blog title sells the integration: building and *benchmarking* an AI
   materials scientist on a laptop.
3. **Short talks**: local AI/materials meetups, group seminars, AI4Science
   workshop lightning talks. One talk = one rehearsable 10-min story:
   "candidates are cheap, trust is expensive; here's a loop with controls."
4. **The dashboard GIF** — 15 seconds of the point cloud crawling toward the
   target box is the single most shareable artifact this project produces.
   Record it during the next long run.
5. **Engagement where the field lives**: Materials Project community,
   matbench/AI4Science threads, thoughtful comments on the papers in
   reading-list.md. Visibility compounds from specific technical
   contributions, not broadcasting.

## Framing language that works (and what to avoid)

- ✅ "I build closed-loop discovery systems and benchmark whether the AI
  actually helps" — concrete, falsifiable, memorable.
- ✅ "Full-stack materials scientist: from crystal growth to the software
  that plans the next growth."
- ❌ "Jack of all trades / generalist" — invites the master-of-none read.
- ❌ Listing seven skills as a flat list — always pair a skill with the
  artifact that proves it (table above).

## The honest risk assessment

The integrator profile wins in emerging fields and loses in mature ones.
Agentic-AI-for-materials is maybe two years old as a field — timing is
right. The risk is spreading thin across the project's many possible
directions; the mitigation is the 90-day arc in impact-strategy.md: one
study, finished and published, before anything else.
