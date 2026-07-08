# Rediscovery experiment: the loop re-finds hidden known absorbers

*2026-07-08, seed 8. Protocol: CuGaSe₂, AgGaSe₂, and CuInS₂ — all real,
well-characterized PV chalcopyrites — were masked from Materials Project
search results and novelty checks (config/missions/rediscovery.yaml). To
every strategy they look like unknown chemical space. Question: does the
search machinery find materials we KNOW are good?*

## Result

| strategy | scored | hits | hits/100 relax | rediscoveries (of 3) |
|---|---|---|---|---|
| random | 63 | 2 | 3.17 | 0 |
| similarity | 79 | 2 | 2.53 | 1 (CuGaSe₂) |
| **agent** | 14 | 5 | **35.7** | **1 (AgGaSe₂)** |

**The agent re-found AgGaSe₂ blind at iteration 3** — hull 0.048 eV/atom,
gap 1.42 eV (0.018 from the mission ideal; the compound's experimental gap
is ~1.8 eV — surrogate error noted). It reached the compound through its
own hypothesis chain (Ag-chalcopyrite reasoning), not through database
lookup, since the database was masked. Similarity re-found CuGaSe₂;
random found none. Equal rediscovery *count* between agent and similarity —
but the agent did it in 14 relaxations to similarity's 79.

## Secondary observations

1. **Fourth consecutive convergence on Ag-kesterites.** This run (a variant
   condition — masking changes novelty signals) again found ZnAg₂GeSe₄ and
   CdAg₂GeSe₄ on the hull, plus MgAg₂GeTe₄. Its 35.7 hits/100relax is
   consistent with the three official replicates (57.1/22.2/16.7); we keep
   it out of that statistic because the mission differs, but it is a fourth
   independent observation of the same regime and the same chemistry.
2. **A new family probed:** Si-based quaternaries (ZnSi(AgSe₂)₂ and
   relatives) — moderately unstable (0.08–0.17 eV/atom), correctly measured
   as such, honestly recorded. Exploration with negative results is the
   system working.
3. **Budget usage improving:** 14 evaluations (vs 7–12 in earlier runs).

## What this claim is and is not

It **is**: evidence the hypothesize→filter→evaluate machinery can navigate
to known-good materials without database access to them — the loop's search
component works, independent of its novelty component.

It **is not**: proof of pure reasoning. The LLM has read the PV literature;
masking our databases does not mask its training data. AgGaSe₂ likely sits
in its prior. The honest statement: the agent can *reach and physically
confirm* literature-plausible materials through the loop, which is exactly
what we want it doing one step past the literature boundary — where its
prior ends and the surrogates take over. (The candidate-novel Mg tellurides
from the replication runs are that step.)

Rediscovery rate is 1/3 for both informed strategies at this budget — CuInS₂
went unfound by everyone. A larger budget or more seeds would presumably
raise this; 100 relaxations against the space of chalcogenides is a small
net.
