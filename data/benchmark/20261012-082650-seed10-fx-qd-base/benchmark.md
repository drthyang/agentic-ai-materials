# Benchmark: qd-emitter-v1

budget: 5 iterations x 20 relaxations

| strategy | scored | hits | hits/100 relax | rediscoveries | best |gap-ideal| (eV) |
|---|---|---|---|---|---|
| random | 61 | 0 | 0.0 | 0 | 0.201 |
| similarity | 47 | 1 | 2.13 | 0 | 0.145 |
| bayesopt | 77 | 0 | 0.0 | 0 | 0.145 |

hit = converged + gap in [1.8, 3.1] eV + e_above_hull <= 0.05 eV/atom + not a confirmed-known material
