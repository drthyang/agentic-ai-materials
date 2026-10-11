# Benchmark: qd-emitter-v1

budget: 5 iterations x 20 relaxations

| strategy | scored | hits | hits/100 relax | rediscoveries | best |gap-ideal| (eV) |
|---|---|---|---|---|---|
| random | 61 | 3 | 4.92 | 0 | 0.044 |
| similarity | 47 | 4 | 8.51 | 0 | 0.044 |
| bayesopt | 77 | 3 | 3.9 | 0 | 0.108 |

hit = converged + gap in [1.8, 3.1] eV + e_above_hull <= 0.05 eV/atom + not a confirmed-known material
