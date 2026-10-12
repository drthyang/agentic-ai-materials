# Benchmark: pv-absorber-v1

budget: 5 iterations x 20 relaxations

| strategy | scored | hits | hits/100 relax | rediscoveries | best |gap-ideal| (eV) |
|---|---|---|---|---|---|
| random | 60 | 0 | 0.0 | 0 | 0.056 |
| similarity | 74 | 1 | 1.35 | 0 | 0.01 |
| bayesopt | 83 | 1 | 1.2 | 0 | 0.082 |

hit = converged + gap in [1.1, 1.7] eV + e_above_hull <= 0.05 eV/atom + not a confirmed-known material
