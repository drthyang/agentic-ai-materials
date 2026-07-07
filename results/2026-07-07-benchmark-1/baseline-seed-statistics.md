# Baseline statistics across seeds (PV absorber mission)

*2026-07-07. Four independent seeds (0 = benchmark 1; 1-3 run afterward) of
the two non-LLM baselines, 5 iterations x 20 relaxations each. Establishes
the error bars the agent must be judged against. Baselines are cheap, so we
can afford real statistics here — the agent cannot (see analysis.md,
"Threats to validity").*

## Per-seed hits per 100 relaxations

| seed | random | similarity |
|---|---|---|
| 0 | 0.00 | 1.72 |
| 1 | 1.67 | 2.70 |
| 2 | 1.23 | 2.90 |
| 3 | 3.95 | 2.82 |

## Aggregate

| strategy | mean | std | range |
|---|---|---|---|
| random | 1.71 | 1.43 | 0.00 – 3.95 |
| similarity | **2.54** | **0.48** | 1.72 – 2.90 |

## Reading

1. **Random is a coin flip.** Its hit rate swings from 0 to 3.95 across
   seeds — a single random run tells you almost nothing. This is the
   concrete justification for seeding: benchmark 1's "random = 0 hits" was
   the low tail of a wide distribution, not a stable fact.

2. **Similarity is reliably strong.** Mean 2.54 with std 0.48 — low variance
   is itself a result: chemistry-informed enumeration over a good prototype
   library *consistently* works. This is the real opponent; beating random
   is not enough.

3. **The bar for the agent.** To claim the LLM adds value, an agent run must
   land at or above the similarity band (~2.5, roughly 2.0–3.0). Benchmark
   1's agent scored 0.00 — below even random's mean. Benchmark 2 (upgraded
   novelty-binding prompts) tests whether objective alignment moves it into
   contention.

## Caveat

n=4 seeds is enough to see the shape (random wide, similarity tight) but not
for tight confidence intervals. Std shown is population std over the 4
observations. A publication-grade claim would want ~10 seeds for the
baselines; cheap to add later if a headline result depends on it.
