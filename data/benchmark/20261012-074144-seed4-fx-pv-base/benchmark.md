# Benchmark: pv-absorber-v1

budget: 5 iterations x 20 relaxations

| strategy | scored | hits | hits/100 relax | rediscoveries | best |gap-ideal| (eV) |
|---|---|---|---|---|---|
| random | 62 | 2 | 3.23 | 0 | 0.01 |
| similarity | 56 | 1 | 1.79 | 0 | 0.01 |
| bayesopt | 91 | 1 | 1.1 | 0 | 0.01 |

hit = converged + gap in [1.1, 1.7] eV + e_above_hull <= 0.05 eV/atom + not a confirmed-known material
