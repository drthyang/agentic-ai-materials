# Benchmark: pv-absorber-v1

budget: 5 iterations x 20 relaxations

| strategy | scored | hits | hits/100 relax | rediscoveries | best |gap-ideal| (eV) |
|---|---|---|---|---|---|
| agent (claude-opus-5-5) | 98 | 13 | 13.27 | 0 | 0.017 |

hit = converged + gap in [1.1, 1.7] eV + e_above_hull <= 0.05 eV/atom + not a confirmed-known material
