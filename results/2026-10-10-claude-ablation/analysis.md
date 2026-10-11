# Claude ablation: frontier vs local proposer, and which parts matter

*Runs 2026-10-10 18:37 to 2026-10-11 16:28 EDT on the user's Mac. API
spend $18.05 of a hard $40 cap (restated 2026-10-11; see Spend); the
2026-10-11 follow-up spent $0. Every number here is surrogate-level
(CHGNet relaxation, Materials Project hull, MEGNet HSE gap), not DFT or
experiment. **Read the first section before any table:** a structure
audit on 2026-10-11 showed that most hits depend on a defective
prototype, and it changes which conclusions hold.*

## Read this first: most hits depend on a defective prototype (2026-10-11)

**The defect.** The chalcopyrite and kesterite prototypes in
`src/athanor/prototypes.py` are not the structures their docstrings name.
Each is an 8-atom cell that holds half of the 16-atom conventional cell's
atoms in the full c ≈ 11 Å box: every atom sits at z ∈ [−0.125, 0.25],
leaving a ~7 Å empty gap, and the symmetry is P2 rather than I-42d or
I-4. It was found while building the novelty audit, when each hit's space
group was needed for comparison with OQMD and the prototypes came back P2.
Every candidate built on them, by every strategy (agents and baselines
alike, July and October), was relaxed from that start, and **all 93
distinct hits in this study are of those two types** (none is zinc
blende, whose prototype is a correct cell).

**The audit.** `scripts/structure_audit.py` applies each hit's own
substitution to a correct conventional cell built from the space group,
starts it at a predicted volume, and scores it with the unchanged
pipeline ([structure-audit.csv](structure-audit.csv)):

| mission | found by | distinct hits | still a hit in a correct bulk cell |
|---|---|---|---|
| PV | agents | 47 | 14 |
| PV | baselines | 11 | 4 |
| QD | agents | 14 | 4 |
| QD | baselines | 23 | 9 |

Every PV loss is the predicted band gap leaving the window (median shift
0.56 eV, up to 1.6 eV); none is a stability or convergence failure. In the
bulk cells 88 of 93 compositions sit on the hull, so in this pipeline the
stability criterion barely discriminates these families. Which geometry
gives the *right* gap is a question for DFT; the point is that the hit
labels depend on a starting geometry the benchmark never intended.

**Structure-robust hits per run, PV mission** (a run's hits whose
composition is still a hit in the correct cell):

| arm | n | robust hits/run: mean ± SD (range) | raw hits/run |
|---|---|---|---|
| random | 8 | 0.5 ± 0.8 (0–2) | 1.0 ± 0.9 |
| similarity | 8 | 0.9 ± 0.4 (0–1) | 2.0 ± 0.5 |
| BayesOpt | 8 | 0.2 ± 0.5 (0–1) | 1.5 ± 1.4 |
| qwen3:32b, no surrogate (July) | 3 | 0.3 ± 0.6 (0–1) | 2.7 ± 1.2 |
| qwen3:32b, no surrogate (same day, 2026-10-11) | 3 | 0.0 ± 0.0 (0–0) | 0.3 ± 0.6 |
| qwen3:32b, + rank_by_surrogate (same day) | 1 | 0 | 0 |
| Sonnet 5.5, no surrogate | 5 | 4.4 ± 1.3 (2–5) | 16.4 ± 2.1 |
| Sonnet 5.5, + rank_by_surrogate | 5 | 3.0 ± 1.4 (1–4) | 11.0 ± 2.5 |
| Sonnet 5.5, + surrogate, no critic | 3 | 4.3 ± 2.1 (2–6) | 15.0 ± 3.5 |
| Sonnet 5.5, no surrogate, no critic | 3 | 3.3 ± 2.3 (2–6) | 16.3 ± 3.2 |
| Opus 5.5, no surrogate | 3 | 4.3 ± 3.2 (2–8) | 18.7 ± 5.5 |

Exact one-sided permutation p-values on robust hits per run:
Sonnet > qwen same day p = 0.018 and > qwen July p = 0.018 (every Sonnet
run above every qwen run, the floor for 5 vs 3); Sonnet > similarity
p = 0.0008; Sonnet + surrogate > similarity p = 0.0062; Sonnet no
surrogate > Sonnet + surrogate p = 0.091; Opus > Sonnet p = 0.54;
similarity > BayesOpt p = 0.020; qwen July > similarity p = 0.99.
Surrogate × critic interaction (OLS on the 2×2, n = 16, two-sided):
raw hits p = 0.17, robust hits p = 0.20.

**What survives.** Sonnet 5.5 finds more structure-robust hits per run
than the local qwen3:32b proposer (both the July runs and today's) and
than the best baseline, similarity, at about a quarter of the raw
magnitude (4.4 robust vs 16.4 raw hits per Sonnet run).

**What does not.**
- The complete separation of Claude runs from baseline runs (worst Claude
  run: 1 robust hit; best baseline run: 2).
- The surrogate-tool effect (p = 0.09 on robust hits), and the reading
  that it acts through the critic: the interaction was never significant,
  even on raw hits (p = 0.17). The paid runs to balance the 2×2 at n = 5
  were approved and then cancelled before starting, once the audit made
  raw-hit precision moot.
- Sonnet's edge on the QD mission (robust hits 2.3 ± 1.2 vs similarity
  1.4 ± 0.9, p = 0.20).

**July claims that rest on the same prototypes** (paper/draft.md claim
table and abstract; results/2026-07-0*):
- **C3** (prompt alignment flips 0 → 4 hits, benchmark 2): 1 of the 4
  hits survives (MgAg₂SnSe₄). CdAg₂GeSe₄, MgAg₂GeTe₄ and MgAg₂SnTe₄ drop
  out of the gap window. The 0 of benchmark 1 (C2) is unaffected: it came
  from novelty, not from gaps.
- **C4** (advantage replicates, 32 ± 18 hits/100 relaxations, complete
  separation, p ≈ 0.006): robust hits/100 relaxations for the three runs
  are 14.3, 0 and 0; robust hits per run 0.3 ± 0.6 vs similarity
  0.9 ± 0.4. C4 does not survive, and today's same-day qwen runs (0.3 raw,
  0 robust hits per run) did not reproduce even the raw July result.
- **C5** (the found chemistry is real; "two predicted on-hull members",
  two Mg tellurides "appear unreported"): CdAg₂GeSe₄, ZnAg₂GeSe₄,
  MgAg₂GeTe₄ and MgAg₂SnTe₄ are all out of the window in the correct cell
  (bulk gaps 0.03, 0.66, 0.79, 0.20 eV). The convergence of runs on the
  Ag₂-(II)-(IV)-(VI)₄ family remains a true statement about what the agent
  proposed, not about what the physics supports.
- **C6** (AgGaSe₂ re-found blind in 14 relaxations): survives this check.
  Re-scored in a correct chalcopyrite cell AgGaSe₂ has gap 1.15 eV and
  sits on the hull, still inside the window; similarity's CuGaSe₂ (1.34 eV)
  also survives.
- **C7** (QD mission: agent pattern directional, MgAg₂Ge(S,Se)₄; similarity's
  on-hull QD shortlist): the system-level claim (config-only generality)
  is unaffected; both agent hits drop out (bulk gaps 1.58 and 0.34 eV),
  and of similarity's three on-hull candidates only Cu₂SiSnS₄ survives.
- The July "first screening hit" CdCuSe₂ (similarity; WALKTHROUGH.md,
  ROADMAP.md's "CdCuSe2 dossier", results/2026-07-07-benchmark-1): bulk gap
  0.14 eV, not a hit.
- Abstract sentences built on these: "32 ± 18 hits per 100 relaxations
  … complete separation, exact rank p ≈ 0.006", "two predicted on-hull
  members … two (Mg tellurides) appear unreported", and "transferring the
  discovered kesterite family across gap windows".

The prototypes are left unchanged here: fixing them changes the protocol
for every run, which is the user's call.

## Same-day qwen3:32b rerun (2026-10-11, $0 API)

The July protocol exactly (PV mission, 5 × 20 relaxations, gemma4:26b
critic, surrogate off, the July agent seeds 0, 6, 7), run locally today
with the Mac otherwise idle on Ollama:

| run | relaxations | raw hits | robust hits | July run with this seed |
|---|---|---|---|---|
| seed 0 | 3 | 1 (CdAg₂GeSe₄) | 0 | 7 relaxations, 4 hits |
| seed 6 | 8 | 0 | 0 | 9 relaxations, 2 hits |
| seed 7 | 3 | 0 | 0 | 12 relaxations, 2 hits |

The same-day qwen arm is weaker than July's (0.3 vs 2.7 raw hits per run;
p = 0.5 for July > today on robust hits, which are near zero for both). The
agent behaved as in July — few relaxations, iterations ending with nothing
evaluated after filters rejected its binaries — but did not land on the
silver-kesterite family the July runs converged on. Agent seeds name runs
only (LLM sampling is not seeded), so this is run-to-run variance plus
anything that changed since July (the critic model was re-pulled
2026-10-09). One qwen3:32b + `rank_by_surrogate` run also finished
(seed 71: 5 relaxations, 0 hits, and it never called the surrogate tool);
the other two were stopped before starting when work was paused. The
Sonnet-vs-qwen comparison now holds against same-day runs as well.

## Novelty audit vs OQMD and COD (2026-10-11, $0)

`scripts/novelty_audit.py` checked every distinct hit composition against
OQMD's public REST API (any entry; any with an ICSD id, i.e. imported from
an experimental ICSD structure; any in the same space group as the intended
structure) and against the Crystallography Open Database (experimental
structures, composition within 0.03 atomic fraction). ICSD itself is
licensed and was not queried. Responses are cached in
`data/novelty_cache/`; per-composition results in
[novelty-audit.csv](novelty-audit.csv).

| mission | found by | distinct hits | in OQMD | OQMD entry with ICSD id | OQMD, same space group | in COD | absent from both |
|---|---|---|---|---|---|---|---|
| PV | agents | 47 | 23 | 0 | 17 | 0 | 24 |
| PV | baselines | 11 | 2 | 0 | 1 | 0 | 9 |
| QD | agents | 14 | 12 | 0 | 6 | 0 | 2 |
| QD | baselines | 23 | 5 | 0 | 1 | 0 | 18 |

No hit matches an experimental structure in either open database; about
half of the PV agent hits are already in OQMD as hypothetical DFT entries.
Combining both audits, the PV agent hits that are **structure-robust and
absent from OQMD and COD** number 10 of 47: K₂AgSbSe₄, K₂CaGeTe₄,
K₂MnGeSe₄, K₂MnSiTe₄, K₂SrGeTe₄, K₂ZnSnTe₄, Na₂AgSbSe₄, Na₂CuSbTe₄,
Na₂MnGeSe₄, Na₂NiGeSe₄ (baselines: 3 of 11; QD agents: 1 of 14, Ba₂InCuS₄).
These are surrogate-level candidates for validation, nothing more: most put
an alkali cation on a tetrahedral kesterite site, a structure such
compounds are unlikely to adopt, and absence from OQMD and COD is not
absence from the literature or ICSD.

## Headline (raw hits, before the audit; superseded where the first section disagrees)

| question | answer (PV mission, cap = 100 relaxations per run) |
|---|---|
| Frontier vs local proposer | Claude Sonnet 5.5 found **16.4 ± 2.1 hits per run** (n=5) vs **2.7 ± 1.2** for qwen3:32b (n=3, July). Every Sonnet run beat every qwen run (exact p = 0.018, the smallest a 5-vs-3 split allows). Per relaxation, qwen was higher (32.0 vs 18.1 hits/100; not significant): it spent 9 of its 100 relaxations, Sonnet spent 91. |
| Agent vs baselines | All 19 Claude runs on PV (Sonnet and Opus, every configuration) beat all 24 baseline runs on both hits per run (min 9 vs max 4) and hits per 100 relaxations (min 10.0 vs max 4.4). |
| `rank_by_surrogate` tool | It **hurt**: 11.0 ± 2.5 hits per run with it vs 16.4 ± 2.1 without (n=5 each, p = 0.012). The 2×2 below locates most of the harm in its combination with the critic. |
| Critic | No effect without the surrogate (16.3 vs 16.4 hits per run). With the surrogate it vetoed 2.5× as often and the arm lost ~4 hits per run (p = 0.07, n=3 vs 5). |
| BayesOpt baseline, n=2 → 8 | 1.7 ± 1.6 hits/100: indistinguishable from random (1.4 ± 1.2, p = 0.35) and below similarity (3.0 ± 0.7, p = 0.023). The July n=2 reading (zero hits, "the known-materials trap") does not survive replication. |
| Second mission (QD emitter) | Sonnet 9.0 ± 2.6 hits per run vs similarity 3.8 ± 1.1 (n=3 vs 5, p = 0.018). Per relaxation the edge is not significant (11.7 vs 7.7 hits/100, p = 0.09), and one BayesOpt run (9 hits) beat one Sonnet run (6). The PV complete separation does **not** fully generalise. |
| Opus 5.5 vs Sonnet 5.5 | 18.7 ± 5.5 vs 16.4 ± 2.1 hits per run (n=3 vs 5, p = 0.27): no detectable difference at about 2.7× the cost per run. |

## PV mission: per-arm results

Metrics recomputed from each run's DB by `scripts/aggregate_ablation.py`.
SD is the sample SD (n−1; the July write-ups quoted the population SD,
which is why their spreads read smaller). Brackets are 95% percentile
bootstrap intervals of the mean; with n = 3–5 they are rough.

| arm | n | hits/100 relax: mean ± sd [95% CI] | hits/run: mean ± sd (min–max) | relaxations/run: mean (min–max) |
|---|---|---|---|---|
| random | 8 | 1.4 ± 1.2 [0.7, 2.2] | 1.0 ± 0.9 (0–3) | 75.1 (60–87) |
| similarity | 8 | 3.0 ± 0.7 [2.5, 3.4] | 2.0 ± 0.5 (1–3) | 66.1 (56–76) |
| bayesopt | 8 | 1.7 ± 1.6 [0.7, 2.7] | 1.5 ± 1.4 (0–4) | 86.8 (80–95) |
| qwen3:32b, no surrogate (July) | 3 | 32.0 ± 21.9 [16.7, 57.1] | 2.7 ± 1.2 (2–4) | 9.3 (7–12) |
| Sonnet 5.5, no surrogate | 5 | 18.1 ± 2.2 [16.4, 19.8] | 16.4 ± 2.1 (14–19) | 90.8 (89–93) |
| Sonnet 5.5, + rank_by_surrogate | 5 | 12.4 ± 2.1 [10.9, 14.2] | 11.0 ± 2.5 (9–15) | 88.4 (76–96) |
| Sonnet 5.5, + surrogate, no critic | 3 | 16.5 ± 3.2 [14.3, 20.2] | 15.0 ± 3.5 (13–19) | 90.7 (87–94) |
| Sonnet 5.5, no surrogate, no critic | 3 | 17.4 ± 3.4 [14.7, 21.3] | 16.3 ± 3.2 (14–20) | 93.7 (92–95) |
| Opus 5.5, no surrogate | 3 | 18.8 ± 5.5 [13.3, 24.2] | 18.7 ± 5.5 (13–24) | 99.0 (98–100) |

Per-run values (hits per run): qwen 4, 2, 2 · Sonnet no-surrogate 15, 19,
16, 18, 14 · Sonnet + surrogate 9, 15, 10, 12, 9 · + surrogate, no critic
19, 13, 13 · no surrogate, no critic 20, 15, 14 · Opus 13, 24, 19 ·
BayesOpt 0, 0, 4, 1, 1, 1, 3, 2. Every run, with its hit formulas, API cost
and cache-read share, is in [arms-pv-summary.md](arms-pv-summary.md) and
[arms-pv-per-run.csv](arms-pv-per-run.csv); the comparisons table there
has the exact permutation p-value and probability of superiority for each
pair.

### The surrogate × critic 2×2 (Sonnet 5.5, hits per run)

| | critic on | critic off |
|---|---|---|
| **no surrogate** | 16.4 ± 2.1 (n=5) | 16.3 ± 3.2 (n=3) |
| **+ rank_by_surrogate** | 11.0 ± 2.5 (n=5) | 15.0 ± 3.5 (n=3) |

Only the surrogate-plus-critic cell stands out. The agent called the tool
in every surrogate run (4–5 times per run), and the critic vetoed 59
candidates in those five runs against 24 without it, 16 of them as "does
not test the stated hypothesis / out of scope" against 5. One reading,
not established here: EI rankings pull the proposer's batches away from
its own stated family, and the critic, which judges batches against that
hypothesis, vetoes the drift. The cells with n=3 are too small to call the
interaction; they are reported, not claimed.

### Were the critic's vetoes right?

A vetoed candidate is never relaxed in its own run, but other runs often
relaxed the same composition. Of 113 vetoes across the critic-on PV arms,
80 compositions were relaxed somewhere in the study and 6 of those were
hits (qwen 0/7, Sonnet 2/22, Sonnet + surrogate 3/41, Opus 1/10). The
critic is mostly right about what it blocks; on these numbers it neither
helps nor hurts the hit count unless something else (the surrogate) feeds
it more to veto.

### What the frontier model did differently

The local model wrote good hypotheses and then barely used the budget
(9 of 100 relaxations; iterations ending with zero evaluations). Sonnet
spent ~90% of the cap and kept going after its first success. The chemistry
converged: Sonnet re-found all six of qwen's July hits (the
Ag₂-(II)-(IV)-(VI)₄ silver kesterites, e.g. CdAg₂GeSe₄, ZnAg₂GeSe₄,
MgAg₂GeTe₄) and then opened families qwen never reached, chiefly
K₂/Na₂-(II)-(IV)-Te₄ alkali tellurides. Hits recur across runs, so per-run
counts are not independent discoveries: the five no-surrogate Sonnet runs
produced 33 distinct hit compositions, the 24 baseline runs 11, with no
composition in common between agent and baseline hits.

## QD-emitter mission (second target)

`config/missions/qd-emitter.yaml`: gap 1.8–3.1 eV, Cd/Pb/Hg/Tl excluded.
Sonnet ran in the July qwen QD configuration (no surrogate, gemma critic).

| arm | n | hits/100 relax: mean ± sd [95% CI] | hits/run: mean ± sd (min–max) | relaxations/run |
|---|---|---|---|---|
| random | 5 | 4.9 ± 2.2 [3.2, 6.6] | 2.8 ± 1.3 (1–4) | 56.2 |
| similarity | 5 | 7.7 ± 1.5 [6.3, 8.6] | 3.8 ± 1.1 (2–5) | 48.8 |
| bayesopt | 5 | 5.4 ± 4.0 [3.2, 9.0] | 3.8 ± 2.9 (2–9) | 69.4 |
| qwen3:32b (July) | 1 | 66.7 | 2 | 3 |
| Sonnet 5.5, no surrogate | 3 | 11.7 ± 4.7 [6.3, 14.5] | 9.0 ± 2.6 (6–11) | 80.3 |

Sonnet beats similarity on hits per run (p = 0.018) and BayesOpt on both
metrics (p = 0.036), but not similarity per relaxation (p = 0.09), and
the separation is not complete. The QD baselines' seed 8 re-ran in October
and matched the July seed-8 run exactly (random 51 relaxations / 1 hit,
similarity 62 / 5), the best available check that the scorer, filters and
MP lookups have not drifted since July. Details: [arms-qd-summary.md](arms-qd-summary.md).

## Protocol

- **Cap:** 5 iterations × 20 CHGNet relaxations = 100 per run, for every
  strategy. This equalises relaxations only. It is **not** matched total
  compute: LLM inference (local or API) is not counted, and an agent may
  spend less than the cap. That is why both metrics are reported: hits per
  100 relaxations rewards spending little, hits per run rewards using the cap.
- **Hit:** converged + gap in window + hull ≤ 0.05 eV/atom + not a
  Materials Project composition (`metrics.row_flags`). MP-novel is not new
  to science (the July audit found Ag₂ZnGeSe₄ likely known and CdAg₂GeSe₄
  recently synthesised); none of the new hits has been audited against
  ICSD/OQMD. CHGNet hull errors (~0.05 eV/atom) are the size of the hull
  window itself.
- **Proposers:** `claude-sonnet-5-5` and `claude-opus-5-5`, adaptive
  thinking at `effort=high` (Sonnet's API default, set explicitly; no
  effort sweep), prompt caching on tools + system and on the growing turn
  (cache reads were 65–85% of input tokens per run). qwen3:32b (Ollama
  digest `030ee887880f`) in its default thinking mode, as run in July. No
  server-side refusal fallback, so an arm can never silently switch models;
  no run hit a refusal.
- **Critic:** gemma4:26b via Ollama (Q4_K_M, digest `777b927e3b6b`) for
  every agent arm except the no-critic arms.
- **Runs** are independent samples; the "seed" names agent runs and seeds
  only the baselines, which are deterministic per seed.
- **Code:** every October run directory records its `git_commit` in
  `run_config.json`; `src/` and `config/` are identical across all of them
  (132fc4b onward; later commits are data and scripts only).

### What is and isn't matched in the model ablation

The qwen arm is the three July runs (benchmark 2 seed 0, replicates 6 and
7). The Sonnet no-surrogate arm reproduces their configuration: with
`rank_by_surrogate` disabled the agent-facing code (prompts, tools, loop,
critic prompt) is identical to July apart from the matdiscover → athanor
rename (`git diff 2ea3ea8 HEAD`), and `uv.lock` is unchanged. Not
controlled: the runs are three months apart, and the critic model was
re-pulled on 2026-10-09 (the July digest was not recorded). The QD seed-8
reproduction above argues against drift in the scoring pipeline; it says
nothing about the critic. A same-day qwen3:32b rerun was not possible on
2026-10-10 (another session's 16 GB LM Studio model left too little
memory); it ran on 2026-10-11 — see "Same-day qwen3:32b rerun" above.

## Spend

[api-spend-ledger.csv](api-spend-ledger.csv): one row per agent run, token
counts and dollars only. 23 rows: pilot $0.12, 19 Sonnet runs $12.52
(~$0.66 each), 3 Opus runs $5.41 (~$1.80); **total $18.05**. Prices per
million tokens: Sonnet 5.5 $2 input / $10 output / $0.10 cache read /
$2.50 cache write; Opus 5.5 $4 / $20 / $0.20 / $5.00.

*Restatement (2026-10-11).* The runs were logged with Sonnet 5.5 cache
reads at $0.20 per million, giving $18.89 in total. The live
[pricing page](https://platform.claude.com/docs/en/about-claude/pricing)
prices cache hits on Sonnet 5.5 and Opus 5.5 at 0.05× base input (its
footnote 2), i.e. $0.10 for Sonnet; Opus's $0.20 was already right. Every
ledger row was re-priced from its own recorded token counts; the original
figure is kept in the `cost_usd_as_logged` column, and the per-run costs
in the summary tables are computed the same way. Each run's `usage.json`
keeps the cost as logged. The per-run stop ($3 Sonnet, $6 Opus) and the
$40 ledger cap were never reached.

## Reproduce

```bash
scripts/run_claude_ablation.sh                      # every run, in the order they ran
uv run python scripts/aggregate_ablation.py results/2026-10-10-claude-ablation/arms-pv.json
uv run python scripts/aggregate_ablation.py results/2026-10-10-claude-ablation/arms-qd.json
```

One agent run, e.g. the Sonnet no-surrogate arm:

```bash
ANTHROPIC_API_KEY=... uv run athanor benchmark --iterations 5 --seed 11 \
  --baselines none --tag sonnet-nosurr --backend anthropic \
  --model claude-sonnet-5-5 --effort high --no-surrogate --max-cost-usd 3 \
  --ledger results/2026-10-10-claude-ablation/api-spend-ledger.csv --spend-cap-usd 40
```

## Not run

- qwen3:32b + `rank_by_surrogate`: 1 of 3 runs (stopped when work was paused).
- The two extra runs per no-critic Sonnet cell (approved with a $5 cap,
  cancelled before starting; $0 spent).
- A fix of the prototypes and a rerun of the matrix on correct cells.
- An effort sweep for Sonnet, a Claude critic, the TCO and rediscovery
  missions with Claude, an ICSD check (licensed), and any DFT validation.
