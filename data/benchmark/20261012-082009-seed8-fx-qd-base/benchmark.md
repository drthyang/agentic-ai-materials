# Benchmark: qd-emitter-v1

budget: 5 iterations x 20 relaxations

| strategy | scored | hits | hits/100 relax | rediscoveries | best |gap-ideal| (eV) |
|---|---|---|---|---|---|
| random | 51 | 0 | 0.0 | 0 | 0.071 |
| similarity | 62 | 1 | 1.61 | 0 | 0.145 |
| bayesopt | 65 | 0 | 0.0 | 0 | 0.075 |

hit = converged + gap in [1.8, 3.1] eV + e_above_hull <= 0.05 eV/atom + not a confirmed-known material
