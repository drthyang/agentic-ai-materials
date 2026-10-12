# Benchmark: qd-emitter-v1

budget: 5 iterations x 20 relaxations

| strategy | scored | hits | hits/100 relax | rediscoveries | best |gap-ideal| (eV) |
|---|---|---|---|---|---|
| random | 53 | 1 | 1.89 | 0 | 0.182 |
| similarity | 45 | 1 | 2.22 | 0 | 0.145 |
| bayesopt | 72 | 1 | 1.39 | 0 | 0.048 |

hit = converged + gap in [1.8, 3.1] eV + e_above_hull <= 0.05 eV/atom + not a confirmed-known material
