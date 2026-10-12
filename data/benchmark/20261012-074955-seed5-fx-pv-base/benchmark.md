# Benchmark: pv-absorber-v1

budget: 5 iterations x 20 relaxations

| strategy | scored | hits | hits/100 relax | rediscoveries | best |gap-ideal| (eV) |
|---|---|---|---|---|---|
| random | 79 | 0 | 0.0 | 0 | 0.031 |
| similarity | 61 | 1 | 1.64 | 0 | 0.01 |
| bayesopt | 84 | 1 | 1.19 | 0 | 0.051 |

hit = converged + gap in [1.1, 1.7] eV + e_above_hull <= 0.05 eV/atom + not a confirmed-known material
