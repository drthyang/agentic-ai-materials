# Reading list

Curated for this project: each entry says *why* it matters here. Ordered
within sections from load-bearing to nice-to-have. Anything without a link is
easily found by title; links point to versions checked 2026-07.

**Suggested cadence:** one starred (★) paper per benchmark run — they take
about as long as an agent campaign. Tier 1 before the write-up; Tier 2 before
claiming any candidate is interesting; the rest as the roadmap reaches them.

---

## Tier 1 — the discourse your write-up enters (read first)

- ★ **Merchant et al., "Scaling deep learning for materials discovery"
  (GNoME)**, Nature 2023. The scale landmark: 2.2M predicted crystals. Read
  for what scale buys — and note what it doesn't (validation).
- ★ **Cheetham & Seshadri, "Artificial Intelligence Driving Materials
  Discovery?..."**, Chemistry of Materials 2024. THE critique: why most
  predicted "new materials" aren't. The rigor bar this project is built to
  clear — internalize the failure modes they catalog.
- ★ **Szymanski et al., "An autonomous laboratory for the accelerated
  synthesis of novel materials" (A-Lab)**, Nature 2023 — *paired with* the
  Leeman et al. critique in PRX Energy 2024 ("Challenges in high-throughput
  inorganic materials prediction and autonomous synthesis"). The
  claim-and-correction cycle in miniature; the pairing is the lesson.
- ★ **Riebesell et al., "Matbench Discovery"** (arXiv 2308.14920; later in
  Nature Machine Intelligence). How to build a benchmark the field adopts —
  the direct model for the discovery-agent benchmark idea in
  impact-strategy.md.
- **Zeni et al., "A generative model for inorganic materials design"
  (MatterGen)**, Nature 2025 ([arXiv](https://arxiv.org/pdf/2312.03687)).
  The generative counterpoint to substitution-based proposal; roadmap
  long-term item.
- **"PhononBench: a large-scale phonon-based benchmark"**
  ([arXiv 2512.21227](https://arxiv.org/pdf/2512.21227), 2025). Generative
  models average ~26% *dynamical* stability — a whole failure axis our hull
  screen doesn't see. Cite when discussing what "stable" means.
- **"Computed materials proposals depart from the structural memory of
  experimental discovery"** ([arXiv 2606.30967](https://arxiv.org/html/2606.30967),
  2026). Quantifies how AI proposals drift from what humans have ever
  actually made — the synthesizability gap, measured.

## Tier 2 — the surrogates this project stands on (know their error bars)

- ★ **Deng et al., "CHGNet: pretrained universal neural network potential..."**,
  Nature Machine Intelligence 2023. What our relaxations and energies
  actually are; read for training data (MPtrj) and known biases.
- **Chen & Ong, "A universal graph deep learning interatomic potential"
  (M3GNet)**, Nature Computational Science 2022 — and **Batatia et al.,
  "MACE-MP-0"** (arXiv 2401.00096). The alternatives; MACE is the roadmap's
  multi-fidelity step-up.
- **Chen et al., "Learning properties of ordered and disordered materials
  from multi-fidelity data"**, Nature Computational Science 2021. The exact
  multi-fidelity MEGNet band-gap model we call; explains the fidelity
  indices we probed with silicon.
- **Davies et al., "Computational screening of all stoichiometric inorganic
  materials" (SMACT)**, Chem 2016. Our cheap filter's foundations.
- **W. Sun et al., "The thermodynamic scale of inorganic crystalline
  metastability"**, Science Advances 2016. Why 50 meV/atom above hull is a
  defensible "near-stable" line — the number our missions assume.
- **Jain et al., "The Materials Project..."**, APL Materials 2013. The
  database underneath everything; skim for correction schemes (the r2SCAN
  mixing bug we hit lives here).

## Tier 3 — agentic science: what others built (position against these)

- ★ **Boiko et al., "Autonomous chemical research with large language
  models" (Coscientist)**, Nature 2023. The canonical LLM-runs-the-lab
  paper; note what's demo vs measured.
- **Bran et al., "ChemCrow: augmenting large-language models with chemistry
  tools"**, Nature Machine Intelligence 2024. The tool-augmentation pattern
  we use; compare their tool-surface decisions to ours.
- **"Agentic material science"** ([J. Mater. Informatics 2025](https://www.oaepublish.com/articles/jmi.2025.87)).
  Recent field review of agent-driven materials discovery — the related-work
  section starts here.
- **"A Survey of AI for Materials Science: Foundation Models, LLM Agents,
  Datasets, and Tools"** ([arXiv 2506.20743](https://arxiv.org/html/2506.20743v1),
  2025). Comprehensive map; use to check nothing major is missed in the
  write-up.
- **Chen et al., "ScienceAgentBench"** (arXiv 2410.05080). Rigorous agent
  evaluation for data-driven science — methodological cousin of our
  benchmark; steal evaluation-design ideas.
- **Lu et al., "The AI Scientist" (Sakana)**, arXiv 2408.06292. The
  fully-automated-research provocation and its critiques — useful contrast
  when explaining why our loop keeps physics gates in code.
- **Jablonka et al., "14 examples of how LLMs can transform materials
  science and chemistry"**, Digital Discovery 2023. Breadth survey of
  LLM-in-matsci patterns; good for spotting adjacent applications.
- **Abolhasani & Kumacheva, "The rise of self-driving labs in chemical and
  materials sciences"**, Nature Synthesis 2023. Where closed-loop
  computation meets robots — the world our loop would plug into.
- **"Agentic AI for Self-Driving Laboratories in Soft Matter: Taxonomy,
  Benchmarks, and Open Challenges"** ([arXiv 2601.17920](https://arxiv.org/pdf/2601.17920),
  2026). Fresh taxonomy + benchmark thinking for agentic SDLs.

## Tier 4 — deeper methods (as the roadmap reaches them)

- **Xie et al., "Crystal Diffusion Variational Autoencoder" (CDVAE)**, ICLR
  2022 — when adding generative proposals.
- **Lookman et al., "Active learning in materials science..."**, npj
  Computational Materials 2019 — before building the acquisition-function tool.
- **Aykol et al., "Thermodynamic limit for synthesis of metastable inorganic
  materials"**, Science Advances 2018 — sharpening synthesizability
  arguments.
- **"A Synthesizability-Guided Pipeline for Materials Discovery"**
  ([arXiv 2511.01790](https://arxiv.org/pdf/2511.01790), 2025) — candidate
  synthesizability filters worth evaluating as a tool.
- **Artrith et al., "Best practices in machine learning for chemistry"**,
  Nature Chemistry 2021 — the checklist to self-audit the write-up against.

## Keeping current (10 min/week, not a firehose)

- **Digital Discovery** (RSC) and **npj Computational Materials** tables of
  contents — where this work's peers publish.
- **Matbench Discovery leaderboard** — potential/surrogate progress.
- **[Awesome-LLM-Scientific-Discovery](https://github.com/HKUST-KnowComp/Awesome-LLM-Scientific-Discovery)**
  (curated repo, tracks the EMNLP 2025 survey) — new agent papers land here
  fast.
- arXiv `cond-mat.mtrl-sci` + `cs.AI` keyword alert: "materials" + "agent" /
  "discovery" / "benchmark".
