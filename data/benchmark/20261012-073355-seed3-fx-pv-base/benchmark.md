# Benchmark: pv-absorber-v1

budget: 5 iterations x 20 relaxations

| strategy | scored | hits | hits/100 relax | rediscoveries | best |gap-ideal| (eV) |
|---|---|---|---|---|---|
| random | 76 | 3 | 3.95 | 0 | 0.064 |
| similarity | 71 | 1 | 1.41 | 0 | 0.01 |
| bayesopt | 89 | 0 | 0.0 | 0 | 0.144 |

hit = converged + gap in [1.1, 1.7] eV + e_above_hull <= 0.05 eV/atom + not a confirmed-known material
