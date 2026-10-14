# Benchmark: pv-absorber-v1

budget: 5 iterations x 20 relaxations

| strategy | scored | hits | hits/100 relax | rediscoveries | best |gap-ideal| (eV) |
|---|---|---|---|---|---|
| random-novel | 100 | 3 | 3.0 | 0 | 0.017 |
| similarity-novel | 94 | 2 | 2.13 | 0 | 0.082 |
| bayesopt-novel | 100 | 0 | 0.0 | 0 | 0.144 |

hit = converged + gap in [1.1, 1.7] eV + e_above_hull <= 0.05 eV/atom + not a confirmed-known material
