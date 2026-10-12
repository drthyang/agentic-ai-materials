# Benchmark: pv-absorber-v1

budget: 5 iterations x 20 relaxations

| strategy | scored | hits | hits/100 relax | rediscoveries | best |gap-ideal| (eV) |
|---|---|---|---|---|---|
| random | 81 | 0 | 0.0 | 0 | 0.01 |
| similarity | 69 | 1 | 1.45 | 0 | 0.01 |
| bayesopt | 90 | 0 | 0.0 | 0 | 0.056 |

hit = converged + gap in [1.1, 1.7] eV + e_above_hull <= 0.05 eV/atom + not a confirmed-known material
