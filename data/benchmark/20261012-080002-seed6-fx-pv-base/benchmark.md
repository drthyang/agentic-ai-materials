# Benchmark: pv-absorber-v1

budget: 5 iterations x 20 relaxations

| strategy | scored | hits | hits/100 relax | rediscoveries | best |gap-ideal| (eV) |
|---|---|---|---|---|---|
| random | 87 | 0 | 0.0 | 0 | 0.043 |
| similarity | 64 | 1 | 1.56 | 0 | 0.01 |
| bayesopt | 95 | 2 | 2.11 | 0 | 0.032 |

hit = converged + gap in [1.1, 1.7] eV + e_above_hull <= 0.05 eV/atom + not a confirmed-known material
