# Benchmark: qd-emitter-v1

budget: 5 iterations x 20 relaxations

| strategy | scored | hits | hits/100 relax | rediscoveries | best |gap-ideal| (eV) |
|---|---|---|---|---|---|
| random | 63 | 0 | 0.0 | 0 | 0.075 |
| similarity | 50 | 1 | 2.0 | 0 | 0.145 |
| bayesopt | 68 | 0 | 0.0 | 0 | 0.136 |

hit = converged + gap in [1.8, 3.1] eV + e_above_hull <= 0.05 eV/atom + not a confirmed-known material
