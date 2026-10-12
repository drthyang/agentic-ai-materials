# Rerun with both scoring defects fixed

*Runs 2026-10-11 23:33 to 2026-10-12 04:50 EDT on the user's Mac. API
spend $5.89 of a $20 cap. Every number is surrogate-level (CHGNet
relaxation, Materials Project hull, MEGNet HSE gap): candidates for
validation, not discoveries.*

## Read this first

- **What changed.** Two scoring defects behind every earlier result are
  fixed. The chalcopyrite and kesterite prototypes are now real 16-atom
  conventional cells (2aa21eb; they were 8-atom half-cells with a ~7 Å empty
  slab). The convex hull now uses Materials Project's MP2020-corrected
  energies, CHGNet's own scale (edc49f9). Before that fix, oxides,
  chalcogenides and halides looked 0.1–0.35 eV/atom more stable than they
  are, and the "near-stable" test barely filtered anything.
- **The critic did not run in the Claude arms.** In all 10 Sonnet runs the
  gemma4:26b critic answered every one of its 99 reviews in 40–130 ms with
  no parseable verdict, and fail-open approved all 962 candidates. These
  are effectively **critic-off** runs, while the qwen3:32b runs had a
  working critic. See "The critic failure" below. The code now stops such a
  run after three consecutive failed reviews (6a9d0e2). A rerun of the
  Sonnet arm with a working critic is approved and pending.
- **Two kinds of evidence, kept separate.** *New runs* (this directory)
  made their own choices while seeing correct scores. *Re-scored old runs*
  (results/2026-10-10-claude-ablation/) are the October and July choices,
  made while seeing defective scores, re-scored with both fixes.

## New runs: PV absorber mission

Same protocol as October: 5 iterations × 20 CHGNet relaxations, the same
seeds, gap window 1.1–1.7 eV, hull ≤ 0.05 eV/atom, absent from Materials
Project. Hits are distinct compositions per run.

| arm | n | hits per run, mean ± SD (range) | hits / 100 relaxations | relaxations per run |
|---|---|---|---|---|
| random | 8 | 0.6 ± 1.2 (0–3) | 0.9 ± 1.7 | 75 |
| similarity | 8 | 0.9 ± 0.4 (0–1) | 1.3 ± 0.6 | 66 |
| BayesOpt (GP + EI) | 8 | 0.6 ± 0.7 (0–2) | 0.7 ± 0.8 | 87 |
| qwen3:32b, no surrogate (critic working) | 3 | 0.3 ± 0.6 (0–1) | 5.6 ± 9.6 | 6 (4–7) |
| Sonnet 5.5, no surrogate (critic failed open) | 5 | **5.4 ± 1.5 (3–7)** | 5.6 ± 1.6 | 96 |
| Sonnet 5.5 + `rank_by_surrogate` (critic failed open) | 5 | 6.2 ± 3.3 (4–12) | 6.4 ± 3.2 | 96 |

Exact permutation tests on the difference in means, **two-sided**:

| comparison | hits per run | hits / 100 relaxations |
|---|---|---|
| Sonnet vs similarity | p = 0.0008 | p = 0.0008 |
| Sonnet vs qwen3:32b | p = 0.018 (every Sonnet run above every qwen run) | p = 0.96 |
| Sonnet + surrogate vs Sonnet | p = 0.86 | p = 0.78 |
| qwen3:32b vs similarity | p = 0.15 | p = 0.27 |
| similarity vs BayesOpt | p = 0.67 | p = 0.11 |
| BayesOpt vs random | p = 1.0 | p = 0.81 |

- **Sonnet finds more than every baseline and than the local model.** That
  holds per run, and per relaxation against the baselines. The local model
  relaxed only 4–7 of its 100-relaxation budget, so its per-relaxation rate
  rests on one hit and is not distinguishable from Sonnet's.
- **There is no complete separation.** The worst Sonnet run (3 hits) ties
  the best baseline run (random, seed 3).
- **`rank_by_surrogate` has no detectable effect** (p = 0.86).
- **The three baselines are indistinguishable from one another.**
- **The hits are a few families.** Across the ten Sonnet runs the most
  frequent are MgAg₂SnSe₄ (10 of 10 runs), BaSi(AgSe₂)₂, SrSi(AgSe₂)₂ and
  SrAg₂SnS₄ (8 each), and MgSi(AgTe₂)₂ (7). Per-run counts are therefore not
  independent discoveries. Baselines mostly re-find CuSnS₂.

Per-run values, hit formulas, critic counts and costs:
[arms-pv-summary.md](arms-pv-summary.md), [arms-pv-per-run.csv](arms-pv-per-run.csv).

### QD emitter mission (baselines only)

| arm | n | hits per run, mean ± SD (range) |
|---|---|---|
| random | 5 | 0.2 ± 0.4 (0–1) |
| similarity | 5 | 0.8 ± 0.4 (0–1) |
| BayesOpt | 5 | 0.2 ± 0.4 (0–1) |

No Claude QD arm was run: the approved API work covered the PV arms only.

## The critic failure

- **What happened.** The qwen3:32b arm ran first, with the critic working
  (7 vetoes in 9 reviews; one review failed open). The Sonnet lane started
  as soon as that arm released its model.
- **What the log shows.** The Ollama server log shows gemma4:26b reloaded
  at 03:25 with partial GPU offload (mmap disabled, 16.6 GB of system memory
  free). From then on every critic request returned HTTP 200 within
  40–130 ms, without verdicts.
- **Likely cause, not yet diagnosed.** Another session was sharing the Mac
  at the time, and its own gemma4 calls may have forced a reload with
  different settings. A direct, logged critic call in a reserved Ollama
  slot is planned.
- **Consequence.** The ten Sonnet runs are critic-off runs. In October,
  re-scored with both fixes, the critic made no significant difference
  (Sonnet 7.4 ± 0.9 with it, 6.3 ± 0.6 without, p = 0.27). So the Sonnet
  vs baselines and Sonnet vs qwen conclusions do not hinge on it, but the
  like-for-like comparison with the qwen arm does.
- **Flagging and the fix.** Every one of the ten runs carries ledger status
  `critic_failed_open`, from the end-of-run check added the same night.
  From 6a9d0e2 on, a run stops after three consecutive failed reviews,
  before the batch that hit the limit is relaxed, with status
  `critic_unavailable`.

## Re-scored old runs (separate evidence)

October and July runs, their own choices re-scored by
`scripts/rescore_runs.py`, from
results/2026-10-10-claude-ablation/arms-pv-summary.md. "Hull fix only"
keeps each run's own 8-atom cells. "Both fixes" rebuilds every evaluated
candidate in a correct cell. Reconstructing each row's CHGNet energy from
its stored formation energy reproduced the stored old-scale hull for
4,733 of 4,733 rows.

| arm (October unless noted) | n | raw hits per run | hull fix only | both fixes, mean ± SD (range) |
|---|---|---|---|---|
| random | 8 | 1.0 | 0.0 | 0.6 ± 1.2 (0–3) |
| similarity | 8 | 2.0 | 0.0 | 0.9 ± 0.4 (0–1) |
| BayesOpt | 8 | 1.5 | 0.1 | 0.6 ± 0.7 (0–2) |
| qwen3:32b (July) | 3 | 2.7 | 0.0 | 0.3 ± 0.6 (0–1) |
| qwen3:32b (2026-10-11) | 3 | 0.3 | 0.0 | 0.0 ± 0.0 |
| Sonnet 5.5 | 5 | 16.4 | 0.8 | 7.4 ± 0.9 (7–9) |
| Sonnet 5.5 + surrogate | 5 | 11.0 | 0.2 | 4.6 ± 2.9 (2–9) |
| Sonnet 5.5, no critic | 3 | 16.3 | 0.0 | 6.3 ± 0.6 (6–7) |
| Sonnet 5.5 + surrogate, no critic | 3 | 15.0 | 0.3 | 6.3 ± 1.5 (5–8) |
| Opus 5.5 | 3 | 18.7 | 0.3 | 11.0 ± 2.0 (9–13) |

Two-sided p on "both fixes":
- Sonnet vs similarity: 0.0008
- Sonnet vs qwen (July or same-day): 0.018
- surrogate effect: 0.095
- Opus vs Sonnet: 0.036
- QD mission, Sonnet vs similarity: 17.7 ± 3.2 vs 0.8 ± 0.4, p = 0.018

With the hull fixed but the old cells kept, almost nothing is stable:
the half-cells were high in energy, and the uncorrected hull had hidden
that.

## Where the two kinds of evidence agree and differ

- **Baselines: identical.** They are deterministic per seed, and the fresh
  runs reproduce the re-score run for run: 24 of 24 match in hits and
  relaxations. That independently validates the re-score.
- **The local model: the same.** About 0.3 hits per run. It still spends
  under a tenth of its budget.
- **Sonnet: same direction, smaller in the rerun.** The rerun gives 5.4 ±
  1.5 against 7.4 ± 0.9 re-scored (p = 0.04). The rerun's critic was off,
  though. Against the re-scored October *no-critic* arm (6.3 ± 0.6) the
  difference is not significant (p = 0.52). Seeing correct scores did not
  make the agent find more.
- **The surrogate tool: no effect in either** (p = 0.86 rerun, 0.095
  re-score). The October raw-hit effect (p = 0.012 one-sided) was an
  artifact of the defects.
- **Not rerun:** Opus (no gain expected to justify the cost), the October
  critic-off Sonnet arms (the rerun's Sonnet arms became critic-off by
  accident), and any QD agent arm.

## Structure audit of the new hits

`scripts/structure_audit.py` rebuilt each new hit route in its prototype,
started it from a predicted volume instead of the prototype's lattice,
and re-scored it:

| mission | found by | hit routes | still hits |
|---|---|---|---|
| PV | agents | 19 | 17 |
| PV | baselines | 5 | 5 |
| QD | baselines | 2 | 2 |

Both PV misses sit at a window edge. GaCu₂SbS₄ (qwen) gave 1.14 eV in
its run and 1.04 eV from the other starting volume. SrSi(AgSe₂)₂ (Sonnet)
gave 1.69 eV and 1.72 eV. These are relaxation noise near a threshold,
not a structural defect. Hits on correct cells are robust, as they should
be ([structure-audit.csv](structure-audit.csv)).

## Novelty audit of the new hits

*Pending.* `scripts/novelty_audit.py` was still querying OQMD when this
was written (its API returned intermittent 502s); the results will go to
[novelty-audit.csv](novelty-audit.csv) and into this section.

## Spend

[api-spend-ledger.csv](api-spend-ledger.csv) has 10 runs, $5.89 in total
($0.51–0.64 per run), at Sonnet 5.5's $2 input, $10 output, $0.10 cache
hit and $2.50 cache write per million tokens.
- Tokens: 459 calls; 1,038 uncached input, 952,767 cache-write and
  3,987,386 cache-read input tokens (81% of input from cache); 310,517
  output tokens.
- Each run has a `started` row, then a final row with role `proposer` and
  status `critic_failed_open`.
- The per-run stop ($1.25) and the $20 study cap were never reached. The
  qwen runs and baselines cost $0.

## Protocol and code

- Runs used the code at the commits recorded in each `run_config.json`,
  with `prototype_cells` showing 16-atom chalcopyrite and kesterite cells.
- Fixes applied in the same branch before the runs:
  - critic auto-approvals counted (440e172);
  - one relaxation per proposal and hits counted per composition, tool-free
    final report, both bad critic pairings refused (8f780da);
  - critic and proposer spend under one cap, killed runs counted (d9c9405);
  - element references from MP, with no silent fallback (463e327).
- The fail-closed critic rule (6a9d0e2) landed after these runs.
- Proposer: claude-sonnet-5-5 at effort high, prompt caching.
  qwen3:32b via Ollama.
- Critic: gemma4:26b via Ollama, working for qwen, failed open for Sonnet
  (see above).

## Reproduce

```bash
scripts/run_fixed_prototypes.sh                   # qwen arm, PV and QD baselines
ATHANOR_BENCHMARK_LOCK=data/benchmark/.lock-api \
  scripts/run_fixed_prototypes.sh sonnet          # Claude lane (key from ~/.config/anthropic/key)
uv run python scripts/aggregate_ablation.py results/2026-10-12-fixed-prototypes/arms-pv.json
uv run python scripts/structure_audit.py results/2026-10-12-fixed-prototypes/arms-pv.json \
  results/2026-10-12-fixed-prototypes/arms-qd.json
uv run python scripts/novelty_audit.py results/2026-10-12-fixed-prototypes/arms-pv.json \
  results/2026-10-12-fixed-prototypes/arms-qd.json
```

## Next

- Diagnose the gemma4 failure with a logged direct call. Rerun the five
  Sonnet no-surrogate runs with a working critic (approved, about $3).
- Re-check the robust-and-absent hits against the literature, and run DFT
  on a handful.
- The hull criterion still carries CHGNet-vs-MP disagreements of tens of
  meV/atom: zinc-blende GaAs sits 0.13 eV/atom above the hull on either
  energy scale. A second interatomic potential would show which hits
  depend on it.
