# Benchmark: qd-emitter-v1

budget: 5 iterations x 20 relaxations

| strategy | scored | hits | hits/100 relax | rediscoveries | best |gap-ideal| (eV) |
|---|---|---|---|---|---|
| random | 53 | 2 | 3.77 | 0 | 0.044 |
| similarity | 40 | 2 | 5.0 | 0 | 0.108 |
| bayesopt | 65 | 2 | 3.08 | 0 | 0.025 |

hit = converged + gap in [1.8, 3.1] eV + e_above_hull <= 0.05 eV/atom + not a confirmed-known material
