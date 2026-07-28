# Athanor Mission Control — wireframes

Text wireframes of the dashboard UI (`athanor dashboard`, and the baked
static twin from `athanor export-pages`). These are **descriptive, not
aspirational**: every box, label, and number below is traced from the
shipped implementation, so this doubles as a spec to review changes
against.

Source of truth for each region:

| Layer | File |
|---|---|
| Structure (cards, pages, ids) | [`src/athanor/web/index.html`](src/athanor/web/index.html) |
| Layout, tokens, states | [`src/athanor/web/app.css`](src/athanor/web/app.css) |
| Content, data binding, SVG | [`src/athanor/web/app.js`](src/athanor/web/app.js) |
| Endpoints (`/api/snapshot`, `/api/benchmark`) | [`src/athanor/dashboard.py`](src/athanor/dashboard.py) |

The UI is **read-only by design** — no control writes back to the campaign.
Changing what a mission targets is a `config/mission.yaml` edit, never a
click.

---

## 0. Legend

```
┌───┐   card / panel boundary (1px --border, 12px radius)
├───┤   internal divider
│   │
▓▓▓▓    filled / active surface (--primary, white ink)
░░░░    tinted surface (--primary-tint-bg or a pill background)
▁▁▁▁    scrollable region continues past the edge
( … )   button / clickable control
[ … ]   chip (mono, small, --chip-bg)
< … >   dynamic value injected by app.js
●       live status dot (pulses when a campaign is running)
→       pipeline flow connector
```

Anything in `< >` comes from `/api/snapshot`; §9 maps each one to its
JSON field.

---

## 1. Frame — global chrome

Present on all three pages. Header and status bar are `flex-wrap: wrap`, so
they reflow rather than clip on narrow viewports.

```
┌──────────────────────────────────────────────────────────────────────────────────────┐
│ ▓▓▓  Athanor — Mission Control                 │  ① Campaign  ② Benchmark  ③ Notebook │
│ ▓▓▓  Closed-loop materials discovery ·  [v0.1] │  ▓▓▓▓▓▓▓▓▓▓                          │
│      agent + critic + surrogates               │                       ( Export CSV ) │
├──────────────────────────────────────────────────────────────────────────────────────┤
│ ● STATUS  Iteration <n> of <N> · running · last activity <HH:MM:SS> UTC              │
│                        [agent <model>]  [critic <model>]  [refreshed <HH:MM> UTC]    │
├──────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                      │
│                              « page content — §2 / §4 / §5 »                         │
│                                                                                      │
├──────────────────────────────────────────────────────────────────────────────────────┤
│ ⚠ Surrogate screening only — CHGNet relaxations and MEGNet band gaps (HSE fidelity). │
│   Candidates are leads, not discoveries: validate with DFT before any claim.          │
├──────────────────────────────────────────────────────────────────────────────────────┤
│      Athanor · read-only view of the campaign DB, lab notebook, and mission config    │
│                          · auto-refreshes every 10 s                                  │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

Notes

- **Brand mark** — 30px rounded square, `--primary` fill, inline SVG
  hexagon + four nodes (the closed loop, abstracted). No raster assets.
- **Page pills** — radio-style; the active one is solid `--primary`. The
  numeral is mono and dimmed. Switching pages only toggles `hidden` on the
  three `<main>` elements; no route, no reload.
- **Export CSV** is pushed right by `margin-left:auto` and is the only
  control that produces output — a client-side Blob of every candidate row
  (`iteration, formula, band_gap_ev, e_above_hull,
  formation_energy_per_atom, converged, is_novel, hit, rediscovery`).
- **Disclaimer bar** is warm-red (`--warn-*`) and never dismissible. It is
  the scientific-honesty guardrail, not a notification.

### Page grid

```
main : max-width 1480px · padding 16px 24px 24px · grid 3 × 1fr · gap 14px
       ├ .span2 → grid-column: span 2
       └ .span3 → grid-column: span 3
@media (max-width: 980px) → single column; span2/span3 collapse to span 1
```

---

## 2. Page ① Campaign — full desktop layout

The default view. Four rows; read top-left → bottom-right as *what we're
looking for → how far we've got → how the loop is running → what it found*.

```
┌──────────────────────────┐┌──────────────────────────┐┌──────────────────────────┐
│ MISSION  [config/mission ││ CAMPAIGN  [last write    ││ AGENT & CRITIC           │
│           .yaml]         ││            <ts> UTC]     ││                          │
│ ░● running░              ││  <8>/<12>      <96>      ││ <qwen3:32b>  via ollama  │
│ PV absorber              ││  ITERATIONS    PROPOSED  ││ critic <model> · fresh   │
│ gap 1.1–1.7 eV (ideal    ││                          ││ context per review ·     │
│ 1.35) · hull ≤ 0.05      ││  <41>          <3>       ││ fails open               │
│ eV/atom · ≤ 4 elements   ││  SCORED        HITS ·    ││ ░<7> vetoes · 0 eV░      │
│ [Cu][Ag][Ga][In][Se][S]  ││                <1> redis ││ ░<19> filtered pre-      │
│ [Zn][Sn][P̶b̶][C̶d̶]         ││ ▔▔▔▔▔▔▔▔▔▔▔░░░░░░░░░░░  ││  compute░                │
│ Targets & budgets live   ││ relax 41/100    errors 2 ││ Vetoes cost zero budget  │
│ in mission.yaml — this   ││                          ││ — recorded as            │
│ view reads, never edits. ││                          ││ filtered_out for audit.  │
└──────────────────────────┘└──────────────────────────┘└──────────────────────────┘
┌──────────────────────────────────────────────────────────────────────────────────┐
│ DISCOVERY LOOP — ITERATION <8>              [fresh context · notebook is memory]  │
│                                                                                  │
│  ┌────────┐  →   ┌────────┐  →   ┌────────┐  →  ┌────────┐   →  ┌────────┐       │
│  │PROPOSE │ −19  │ FILTER │ −7   │ CRITIC │ −2  │EVALUATE│      │ RECORD │       │
│  │  <68>  │filter│  <49>  │vetoed│  <42>  │error│░<41>/12░│     │ +<2>   │       │
│  │prototype│     │SMACT + │      │indepen-│     │░CHGNet ░│     │ hits   │       │
│  │substitu-│     │mission │      │dent    │     │░relax → ░│    │DB rows │       │
│  │tion…   │      │chem…   │      │review  │     │░hull…  ░│     │· 3 nb  │       │
│  └────────┘      └────────┘      └────────┘     └────────┘      └────────┘       │
│  ┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐   │
│    ↺ Loop closes through the lab notebook — the next iteration starts from a      │
│      fresh context and reads what this one learned.     next: iteration 9 / 12    │
│  └ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘   │
└──────────────────────────────────────────────────────────────────────────────────┘
┌───────────────────────────────────────────────────────┐┌─────────────────────────┐
│ COMPOSITION SPACE — GAP VS STABILITY                  ││ AGENT FEED [last 40     │
│              ░status░ iteration   BEST |GAP−IDEAL| <…> ││             events]     │
│                                                       ││ 07-18 SCORE  CuInSe₂ …  │
│  gap ▲                                                ││ 14:02                   │
│  (eV)│  ○      ○                                      ││ 07-18 HIT    CdCuSe₂ …  │
│      │    ┌ ─ ─ ─ ─ ─ ┐  ○                            ││ 14:03                   │
│      │    │ ● CdCuSe₂ │      target window            ││ 07-18 VETO   ZnSnP₂ …   │
│      │    │  ░░░░░░░  │  ○                            ││ 14:05                   │
│      │    │ ◆ AlSb    │                               ││ 07-18 NTBK   reflection │
│      │    └ ─ ─ ─ ─ ─ ┘        ○   ○                  ││ 14:06                   │
│      │  ○   ○                                         ││ ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁  │
│      └──────────────────────────────────────────▶     ││                         │
│         energy above hull (eV/atom)                   ││                         │
│   ● scored   ● hit (novel)   ● rediscovery            ││                         │
│  <41> scored candidates · <8> iterations · hover a    ││                         │
│  point for formula, gap, hull, iteration              ││                         │
└───────────────────────────────────────────────────────┘└─────────────────────────┘
┌───────────────────────────────────────────────────────┐┌─────────────────────────┐
│ TOP CANDIDATES        [ranked by hull within gap …]   ││ LAB NOTEBOOK ( Open full │
│                                                       ││                notebook )│
│ FORMULA   GAP (eV)  HULL (eV/at)  ITER  STATUS  HYPO… ││ ░hypothesis░  iter 8 ·  │
│ CdCuSe₂      1.70        0.003      3   ░● hit░  Cd…  ││ Chalcopyrite Cu–In–Se…  │
│ AlSb         1.62        0.000      6   ░◆ red░  Sb…  ││ ─────────────────────── │
│ ZnGeP₂       1.94        0.021      4   ░scored░ Zn…  ││ ░reflection░  iter 7 ·  │
│ …                                                     ││ Two of three vetoes …   │
└───────────────────────────────────────────────────────┘└─────────────────────────┘
```

---

## 3. Component detail

### 3.1 Mission card

Static per campaign — it exists so a reader can judge every number on the
page against the target that produced it.

```
┌────────────────────────────────────────────┐
│ MISSION                [config/mission.yaml]│   ← .upper label + mono chip
├────────────────────────────────────────────┤
│ ░● running░   ← .pill.free / .pill.dim ○ idle│
│ PV absorber                                 │   ← .sum-title 14px/700
│ gap 1.1–1.7 eV (ideal 1.35) · hull ≤ 0.05   │   ← .sum-meta, mono
│ eV/atom · ≤ 4 elements                      │
│ [Cu][Ag][Ga][In][Se][S][Zn][Sn]  [P̶b̶][C̶d̶]   │   ← .elem / .elem.ex
│ Targets & budgets live in config/mission.   │      (excluded = struck through,
│ yaml — this view reads, never edits.        │       warm-red)
└────────────────────────────────────────────┘
```

### 3.2 Campaign card

Four stats in a 2×2 grid, then the budget meter. `HITS` is the only stat
that takes a color (`--hit` green) — the page has exactly one number that
means *success*, and this is it.

```
┌────────────────────────────────────────────┐
│ CAMPAIGN                [last write <ts> UTC]│
├────────────────────────────────────────────┤
│   <8>/<12>              <96>                │  20px mono, tabular-nums
│   ITERATIONS            PROPOSED            │  10px uppercase --faint
│                                             │
│   <41>                  <3>                 │  ← green when > 0
│   SCORED                HITS · <1> rediscovery
│                                             │
│   ▔▔▔▔▔▔▔▔▔▔▔▔▔░░░░░░░░░░░░░░░░░░░░░░░░░░  │  5px track, --primary fill
│   relaxations 41 / 100            errors 2  │  10.5px mono, --faint
└────────────────────────────────────────────┘
```

The meter is the compute-honesty gauge: relaxations are the real cost, so
the budget is drawn as a bar rather than buried in text.

### 3.3 Agent & critic card

```
┌────────────────────────────────────────────┐
│ AGENT & CRITIC                              │
├────────────────────────────────────────────┤
│ qwen3:32b  via ollama                       │
│ critic gemma4:26b · fresh context per       │  ← or "critic disabled in
│ review · fails open                         │     mission.yaml"
│ ░<7> vetoes · 0 eV spent░  (note pill)      │
│ ░<19> filtered pre-compute░ (dim pill)      │
│ ░<2> relax errors░  (warn pill, only if >0) │
│ Vetoes cost zero relaxation budget —        │
│ recorded as filtered_out rows for audit.    │
└────────────────────────────────────────────┘
```

### 3.4 Discovery loop (pipeline strip)

The centerpiece: one horizontal funnel for the **latest** iteration, with
the loss at each step named on the connector. `.pipe-scroll` scrolls
horizontally below `min-width: 820px` rather than squashing the stages.

```
 stage: min-width 118px, flex 1        flow: fixed 92px, centered
┌──────────────────┐        ┌──────────────────┐        ┌──────────────────┐
│ PROPOSE          │   →    │ FILTER           │   →    │ CRITIC           │
│ <68>             │[−19    │ <49>             │[−7     │ <42>             │
│ prototype substi-│ filtered]│ SMACT + mission │ vetoed]│ independent      │
│ tution, notebook │  grey  │ chemistry —      │  warm  │ review ·         │
│ + literature     │  chip  │ before any compute│ red chip│ skeptical persona│
└──────────────────┘        └──────────────────┘        └──────────────────┘
        →              ┌──────────────────┐        →     ┌──────────────────┐
     [−2 error]        │▓EVALUATE ▓active▓│              │ RECORD           │
      warm chip        │▓<41> / <12>     ▓│              │ +<2> hits        │← --hit
                       │▓CHGNet relax →  ▓│              │ DB rows ·        │
                       │▓E_hull · MEGNet ▓│              │ <3> notebook     │
                       │▓gap (HSE)       ▓│              │ entries          │
                       └──────────────────┘              └──────────────────┘
 ┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐
   ↺  Loop closes through the lab notebook — the next iteration starts from a
      fresh context and reads what this one learned.      next: iteration 9 / 12
 └ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘
```

State rules

- `.stage.active` (blue tint + blue ink) is on **Evaluate** only while
  `meta.running` is true — it marks where compute is being spent right now.
- `.stage.terminal` colors Record's count `--hit` green.
- A connector renders its chip only when the drop is non-zero; the arrow
  always renders. Evaluate → Record has no chip by construction.
- Counts are derived, not stored: `Propose = proposed + filtered_out +
  scored + error`, `Filter = Propose − (filtered_out − vetoed)`,
  `Critic = Filter − vetoed`, `Evaluate = scored + error`.
- The loopback strip is dashed, not solid — it is a *narrative* edge
  (memory via notebook), not a data flow inside this iteration.

### 3.5 Composition map

A hand-rolled SVG scatter — `viewBox="0 0 860 480"`, margins L64 R24 T20
B60, `preserveAspectRatio="none"` so it fills the card at any width.

```
┌──────────────────────────────────────────────────────────────────────┐
│ COMPOSITION SPACE — GAP VS STABILITY   ░status░ iteration            │
│                                        BEST |GAP−IDEAL|  <0.05 eV>   │
├──────────────────────────────────────────────────────────────────────┤
│  3.0┤ ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·   ● scored  ● hit  ● red │← legend
│     │      ○                    ○                                     │
│  2.5┤ ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  │
│     │  ○        ○                                                     │
│  2.0┤ ·┌ ─ ─ ─ ─ ─ ─ ─ ─ ┐·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  │
│     │  │░░░░░░░░░░░░░░░░░│  target window   ← dashed --hit rect,      │
│  1.5┤ ·│░░● CdCuSe₂ ░░░░░│·  ·  ·  · ·         9% green fill;         │
│     │  │░░░◆ AlSb ░░░░░░░│                     x: 0 → hull_max        │
│  1.0┤ ·└ ─ ─ ─ ─ ─ ─ ─ ─ ┘·  ○  ·  ·  ·  ·     y: gap_lo → gap_hi     │
│     │     ○   ○                    ○                                  │
│  0.5┤ ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  │
│  0.0└─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────▶     │
│         0.00  0.05  0.10  0.15  0.20  0.25  0.30  0.35  0.40          │
│                    energy above hull (eV/atom)                        │
│ ← y axis label rotated −90°: "band gap, HSE fidelity (eV)"            │
├──────────────────────────────────────────────────────────────────────┤
│ <41> scored candidates · <8> iterations · hover a point for formula,  │
│ gap, hull, iteration                                                  │
└──────────────────────────────────────────────────────────────────────┘
```

Mark spec

| Class | Radius | Fill | Opacity | Label |
|---|---|---|---|---|
| scored | 5 | `--scored` blue | 0.62 | — |
| hit | 6.5 | `--hit` green | 1.0, 2px cream ring | formula, mono 10.5px |
| rediscovery | 6.5 | `--rediscovery` amber | 1.0, 2px cream ring | formula |
| *iteration mode* | 5 | blue | 0.25 → 0.90 by iteration | — |

- The **segmented control** (`status` / `iteration`) re-renders the SVG
  client-side from the cached snapshot; no refetch.
- Only hits and rediscoveries get text labels, with a 13px vertical
  collision nudge for clusters; labels flip to the left of the point past
  75% of the plot width.
- Every point carries an SVG `<title>` — the hover tooltip is native, so it
  survives with JS-less printing and screen readers.
- Axes autoscale: `xMax = max(0.32, max hull) × 1.06`,
  `yMax = max(3.2, gap_hi × 1.2, max gap) × 1.05` — the target window is
  always in frame even before anything scores near it.

### 3.6 Agent feed

Fixed 3-column grid (`82px · 88px · 1fr`), newest first, `max-height:
430px`, own scroll.

```
┌──────────────────────────────────┐
│ AGENT FEED     [last <40> events]│
├──────────────────────────────────┤
│ 07-18   ░SCORE░  CuInSe₂ gap 1.04│  ← time mono 10px --faintest
│ 14:02:11         eV · hull 0.012 │     tag 9.5px 700 uppercase
│ ─────────────────────────────────│     formula mono, message --secondary
│ 07-18   ░HIT░    CdCuSe₂ novel · │
│ 14:03:40         1.70 eV         │
│ 07-18   ░VETO░   ZnSnP₂ — critic:│
│ 14:05:02         P/Sn ratio …    │
│ 07-18   ░NTBK░   reflection      │
│ 14:06:15         logged (iter 8) │
│ ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ │
└──────────────────────────────────┘
```

Tag palette: `filtered` neutral · `veto` warm-red · `score` blue ·
`hit` green · `rediscovery` amber · `error` warm-red · `notebook` sand.

### 3.7 Top candidates table

```
┌────────────────────────────────────────────────────────────────────────┐
│ TOP CANDIDATES                    [ranked by hull within gap window …] │
├────────────────────────────────────────────────────────────────────────┤
│ FORMULA    GAP (eV)  HULL (eV/at)  ITER  STATUS         HYPOTHESIS     │
│ ─────────────────────────────────────────────────────────────────────  │
│ CdCuSe₂        1.70         0.003     3  ░● hit · novel░ Cd-for-Zn on… │
│ AlSb           1.62         0.000     6  ░◆ rediscovery░ III–V zinc-…  │
│ ZnGeP₂         1.94         0.021     4  ░scored░        Chalcopyrite… │
│ CuGaSe₂           —             —     2  ░scored░        —             │
└────────────────────────────────────────────────────────────────────────┘
   ↑ mono, 600      ↑ right-aligned, tabular-nums    ↑ pill  ↑ 340px ellipsis,
                                                              full text on hover
```

Formulas are rendered with real Unicode subscripts (`CdCuSe2 → CdCuSe₂`)
by a lookahead regex, so they read as chemistry without a math library.
Missing values render as `—`, never `null` or `0`.

### 3.8 Lab notebook panel

Last four entries, newest first, each clamped to three lines. The left
border encodes entry type.

```
┌──────────────────────────────────┐
│ LAB NOTEBOOK  ( Open full notebook)│
├──────────────────────────────────┤
│▍░hypothesis░       iter 8 · <ts> │  ▍blue   = hypothesis
│▍Chalcopyrite Cu–In–Se derivatives│  ▍amber  = decision
│▍should land near 1.3 eV if the …  │  ▍green  = reflection
│                                  │  ▍grey   = observation
│▍░reflection░       iter 7 · <ts> │  ▍faint  = report
│▍Two of three vetoes were right — │
│▍the Sn-rich family is off-target…│
│ ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ │
└──────────────────────────────────┘
```

`( Open full notebook )` is a ghost button that programmatically clicks the
③ Notebook pill — one destination, one implementation.

---

## 4. Page ② Benchmark

A single full-width card. Columns are read from the JSON rather than
hard-coded, so a new metric in `benchmark.py` appears here with no UI
change.

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ BENCHMARK — <2026-07-07 PV absorber>            [100 relaxations / strategy]  │
├──────────────────────────────────────────────────────────────────────────────┤
│ STRATEGY      HITS   HITS/100 RELAX   REDISCOVERIES   BEST |GAP−IDEAL|        │
│ ────────────────────────────────────────────────────────────────────────────  │
│ agent            3            3.0                1              0.05          │
│ similarity       1            1.0                0              0.31          │
│ random           0            0.0                0              0.62          │
│                                                                              │
│ hit = converged · gap in window · hull ≤ max · not confirmed-known            │
│                                                                              │
│ ┌────────────────────────────────────────────────────────────┐               │
│ │                                                            │               │
│ │        ▇▇▇▇▇                                               │               │
│ │        ▇▇▇▇▇      ▇▇▇▇▇                                    │  benchmark.png │
│ │        ▇▇▇▇▇      ▇▇▇▇▇      ▇▇▇▇▇                         │  (matplotlib)  │
│ │        agent    similarity   random                        │               │
│ └────────────────────────────────────────────────────────────┘               │
└──────────────────────────────────────────────────────────────────────────────┘
```

Empty state:

```
│ no benchmark run found — produce one with `athanor benchmark`                 │
```

---

## 5. Page ③ Notebook

The full scientific record, newest first, unclamped — the same entry
component as §3.8 with `-webkit-line-clamp` removed and no height cap.

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ LAB NOTEBOOK — FULL RECORD                                    [<37> entries]  │
├──────────────────────────────────────────────────────────────────────────────┤
│ ▍░reflection░                                       iter 8 · 2026-07-18 14:06 │
│ ▍Two of three vetoes were right — the Sn-rich family sits 0.2 eV above the    │
│ ▍window and the critic caught it before compute. Next iteration should push   │
│ ▍on Cd-for-Zn substitution instead, where the last two hits came from.        │
│                                                                              │
│ ▍░hypothesis░                                       iter 8 · 2026-07-18 13:58 │
│ ▍Chalcopyrite Cu–In–Se derivatives should land near 1.3 eV …                  │
│                                                                              │
│ ▍░observation░                                      iter 7 · 2026-07-18 13:41 │
│ ▍…                                                                           │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 6. States

Every panel has an explicit empty state; none of them is a spinner. The
dashboard is usable — and honest — before a single candidate exists.

### 6.1 Cold start (no campaign yet)

```
│ ○ STATUS  no campaign data yet — start one with `athanor run`                 │

┌ MISSION ────────────┐  ← still fully populated: the mission exists in config
┌ CAMPAIGN ───────────┐  ← 0 / 12 iterations, empty meter
┌ DISCOVERY LOOP ─────┐  "no iterations yet — the loop appears here live"
┌ COMPOSITION SPACE ──┐  "no scored candidates yet"        (caption hidden)
┌ AGENT FEED ─────────┐  "no events yet"                   (chip hidden)
┌ TOP CANDIDATES ─────┐  "no data yet"                     (colspan=6 row)
┌ LAB NOTEBOOK ───────┐  "no entries yet"
```

### 6.2 Running vs idle

| Signal | Running | Idle |
|---|---|---|
| Status dot | blue, 1.6s pulse (suppressed under `prefers-reduced-motion`) | grey, static |
| Status message | `Iteration 8 of 12 · running · last activity …` | `… · idle · …` |
| Mission pill | `● running` (blue tint) | `○ idle` (dim) |
| Evaluate stage | `.active` blue tint | plain |
| Loopback tail | `next: iteration 9 / 12` | `campaign complete` when done ≥ planned |

### 6.3 Server unreachable

Fetch failure leaves the last-rendered content in place and degrades only
the status bar — a dropped poll must never blank a chart you were reading.

```
│ ○ STATUS  dashboard server unreachable — retrying…                            │
```

### 6.4 Recorded (static) mode

`export-pages` bakes `data/snapshot.json` + `data/benchmark.json`. On first
load the client tries `api/snapshot`, falls back to the baked file, and
**cancels the 10s timer** — a recording never changes. The only visual
difference is one chip, and it is deliberately the warm "note" color:

```
│ [agent qwen3:32b] [critic gemma4:26b] ░recorded campaign · exported 2026-07-18░│
```

---

## 7. Responsive — ≤ 980px

Single column, source order preserved. The pipeline keeps its 820px
min-width and scrolls horizontally inside its card; the table and the
benchmark table do the same. Nothing reflows into a different reading
order, and no content is hidden at any width.

```
┌──────────────────────────────┐
│ ▓ Athanor — Mission Control  │  header wraps to 2–3 rows
│ ①Campaign ②Bench ③Notebook   │
│                (Export CSV)  │
├──────────────────────────────┤
│ ● STATUS  Iteration 8 of 12  │  chips wrap below
│ [agent …] [critic …]         │
├──────────────────────────────┤
│ ┌ MISSION ─────────────────┐ │
│ ┌ CAMPAIGN ────────────────┐ │
│ ┌ AGENT & CRITIC ──────────┐ │
│ ┌ DISCOVERY LOOP ──────────┐ │
│ │ ┌────┐→┌────┐→┌────┐ ▁▁▁ │ │ ← horizontal scroll, stages keep 118px
│ ┌ COMPOSITION SPACE ───────┐ │
│ │ (SVG scales; min-height  │ │
│ │  380px)                  │ │
│ ┌ AGENT FEED ──────────────┐ │
│ ┌ TOP CANDIDATES ──────────┐ │
│ │ table scrolls sideways ▁▁│ │
│ ┌ LAB NOTEBOOK ────────────┐ │
├──────────────────────────────┤
│ ⚠ Surrogate screening only …│
└──────────────────────────────┘
```

---

## 8. Interaction map

The whole surface has five interactions. That is the design: it is an
instrument panel, not an app.

```
( ① / ② / ③ pill )  → toggle main[hidden]; ② lazily fetches the benchmark
( status | iteration ) → re-render SVG from cached snapshot (no network)
( Export CSV )      → client-side Blob download of all candidate rows
( Open full notebook ) → clicks the ③ pill
  hover a point / a hypothesis cell → native tooltip (SVG <title> / title attr)

auto:  setInterval 10 s → GET api/snapshot → renderAll()   (cancelled in
       recorded mode)
```

Keyboard/a11y: all controls are real `<button>`s with a visible
`:focus-visible` ring; cards carry `aria-label`s; the map exposes
`role="img"` with a descriptive label; the pulse respects
`prefers-reduced-motion`.

---

## 9. Data binding

Every dynamic slot above, and where it comes from in `/api/snapshot`.

| Region | DOM id | Snapshot path |
|---|---|---|
| Status message | `status-msg` | `meta.running`, `meta.last_activity`, `iterations[-1].iteration`, `mission.budget.iterations` |
| Status chips | `status-chips` | `mission.llm.model`, `mission.critic.*`, `meta.generated_at` |
| Mission card | `mission-card` | `mission.{name,band_gap_ev,band_gap_ideal_ev,e_above_hull_max,max_elements,allowed_elements,excluded_elements}` |
| Campaign stats | `campaign-card` | `totals.{iterations_done,proposed,scored,hits,rediscoveries,relaxations_used,relaxations_budget,errors}` |
| Agent & critic | `agent-card` | `mission.llm`, `mission.critic`, `totals.{vetoed,filtered_out,errors}` |
| Pipeline | `pipeline` | `iterations[-1].{proposed,filtered_out,vetoed,scored,error}`, `candidates[].flags.hit`, `notebook[].iteration` |
| Map | `map` | `candidates[].{formula,band_gap_ev,e_above_hull,iteration,is_novel,flags}`, `mission.band_gap_ev`, `mission.e_above_hull_max` |
| Best-gap stat | `best-gap` | `totals.best_gap_distance` |
| Feed | `feed` | `feed[].{when,kind,formula,text}` |
| Top table | `top-body` | `top[].{formula,band_gap_ev,e_above_hull,iteration,flags,is_novel,hypothesis}` |
| Notebook | `notebook-panel`, `notebook-full` | `notebook[].{type,iteration,when,text}` |
| Benchmark | `bench-body` | `/api/benchmark`: `{available,title,budget,rows,hit_definition,has_plot}` |

`flags.hit` / `flags.rediscovery` are computed server-side by
`metrics.row_flags` — the UI never re-derives the hit rule, so dashboard,
benchmark table, and paper always agree.

---

## 10. Token reference

Colors live only in the `:root` block of `app.css`; nothing below is
duplicated in markup.

```
surfaces   --page-bg #faf7f2   --surface #ffffff   --raised #fffdf9
           --muted   #f7f3ec   --chip-bg #f3eee4   --group-bg #f6f1e8
lines      --border  #e8e2d8   --control #ddd5c7   --subtle  #eee7da
ink        --ink #191714  --secondary #5f594f  --faint #94897a  --faintest #b3a993
primary    --primary #1f4fd8  (hover #1a41b4, tint bg #eaf0fe, tint border #b9c6f4)
semantic   --hit #3f6b25 (green)   --rediscovery #a87a10 (amber)
           ok / note / warn triples for pill + chip backgrounds
type       IBM Plex Sans (variable) + IBM Plex Mono, both bundled — no CDN
scale      --fz-micro 10–11.5px · --fz-small 11.5–13px · --fz-body 12.5–14px
           · --fz-large 14–16px  (all clamp()-fluid)
```

Design rules the wireframes encode:

1. **One accent for identity, two for meaning.** Blue is the product;
   green means *hit*, amber means *rediscovery*. Nothing else earns color.
2. **Numbers are mono and tabular** everywhere they can be compared down a
   column.
3. **Every count names its denominator** — `41 / 100 relaxations`,
   `8 / 12 iterations`. A number without a budget beside it is a number
   that can mislead.
4. **Losses are labeled, not hidden.** Filtered, vetoed, and errored
   candidates appear on the pipeline connectors, because a funnel that only
   shows survivors overstates the method.
5. **No build step.** Vanilla JS, hand-written SVG, bundled fonts, zero
   dependencies — the UI ships inside the Python package, mirroring the
   stdlib-only server.
