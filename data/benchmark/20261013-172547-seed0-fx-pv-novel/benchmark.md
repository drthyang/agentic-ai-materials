# Benchmark: pv-absorber-v1

budget: 5 iterations x 20 relaxations

| strategy | scored | hits | hits/100 relax | rediscoveries | best |gap-ideal| (eV) |
|---|---|---|---|---|---|
| random-novel | 100 | 0 | 0.0 | 0 | 0.104 |
| similarity-novel | 99 | 2 | 2.02 | 0 | 0.082 |
| bayesopt-novel | 100 | 0 | 0.0 | 0 | 0.021 |

hit = converged + gap in [1.1, 1.7] eV + e_above_hull <= 0.05 eV/atom + not a confirmed-known material
