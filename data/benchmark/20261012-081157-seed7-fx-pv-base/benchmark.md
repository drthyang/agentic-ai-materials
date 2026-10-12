# Benchmark: pv-absorber-v1

budget: 5 iterations x 20 relaxations

| strategy | scored | hits | hits/100 relax | rediscoveries | best |gap-ideal| (eV) |
|---|---|---|---|---|---|
| random | 76 | 0 | 0.0 | 0 | 0.01 |
| similarity | 76 | 1 | 1.32 | 0 | 0.01 |
| bayesopt | 82 | 0 | 0.0 | 0 | 0.01 |

hit = converged + gap in [1.1, 1.7] eV + e_above_hull <= 0.05 eV/atom + not a confirmed-known material
