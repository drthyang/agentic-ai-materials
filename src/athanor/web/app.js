/* Athanor Mission Control — renders /api/snapshot into the shell.
   Vanilla JS on purpose: the dashboard ships inside the Python package with
   no build step, mirroring the stdlib-only server. */

"use strict";

const $ = (id) => document.getElementById(id);
const esc = (s) => String(s ?? "").replace(/[&<>"']/g,
  (c) => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));

const SUBS = {0:"₀",1:"₁",2:"₂",3:"₃",4:"₄",5:"₅",6:"₆",7:"₇",8:"₈",9:"₉"};
// CdAg2GeSe4 -> CdAg₂GeSe₄ (digits after a letter or ')' become subscripts)
const pretty = (formula) =>
  String(formula ?? "").replace(/(?<=[A-Za-z)])(\d)/g, (d) => SUBS[d]);

let colorMode = "status";
let snapshot = null;

/* ── data plumbing ─────────────────────────────────────────────── */

async function refresh() {
  try {
    const res = await fetch("/api/snapshot");
    snapshot = await res.json();
  } catch {
    $("status-msg").textContent = "dashboard server unreachable — retrying…";
    $("status-dot").classList.remove("live");
    return;
  }
  renderAll(snapshot);
}

function renderAll(s) {
  renderStatus(s);
  renderMission(s.mission);
  renderCampaign(s);
  renderAgent(s);
  renderPipeline(s);
  renderMap(s);
  renderFeed(s.feed);
  renderTop(s);
  renderNotebookPanel(s.notebook);
  renderNotebookPage(s.notebook);
}

/* ── status bar ────────────────────────────────────────────────── */

function renderStatus(s) {
  const t = s.totals, dot = $("status-dot");
  dot.classList.toggle("live", s.meta.running);
  let msg;
  if (!t.iterations_done) {
    msg = "no campaign data yet — start one with `athanor run`";
  } else {
    const latest = s.iterations[s.iterations.length - 1].iteration;
    const state = s.meta.running ? "running" : "idle";
    msg = `Iteration ${latest} of ${s.mission.budget.iterations} · ${state}`
        + (s.meta.last_activity ? ` · last activity ${s.meta.last_activity} UTC` : "");
  }
  $("status-msg").textContent = msg;
  const critic = s.mission.critic.enabled
    ? `critic ${s.mission.critic.model || s.mission.llm.model}` : "critic off";
  $("status-chips").innerHTML =
    `<span class="chip">agent ${esc(s.mission.llm.model)}</span>`
    + `<span class="chip">${esc(critic)}</span>`
    + `<span class="chip">refreshed ${s.meta.generated_at.slice(11, 16)} UTC</span>`;
}

/* ── summary cards ─────────────────────────────────────────────── */

function renderMission(m) {
  const [lo, hi] = m.band_gap_ev;
  const elems = m.allowed_elements.map((e) => `<span class="elem">${esc(e)}</span>`).join("")
    + m.excluded_elements.map((e) => `<span class="elem ex">${esc(e)}</span>`).join("");
  $("mission-card").innerHTML = `
    <span class="pill ${snapshot.meta.running ? "free" : "dim"}" style="align-self:flex-start">
      ${snapshot.meta.running ? "● running" : "○ idle"}</span>
    <div class="sum-title">${esc(m.name)}</div>
    <div class="sum-meta">gap ${lo}–${hi} eV (ideal ${m.band_gap_ideal_ev}) ·
      hull ≤ ${m.e_above_hull_max} eV/atom · ≤ ${m.max_elements} elements</div>
    <div class="elem-row" aria-label="Element palette">${elems}</div>
    <div class="sum-note">Targets &amp; budgets live in config/mission.yaml — this view reads, never edits.</div>`;
}

function renderCampaign(s) {
  const t = s.totals, b = s.mission.budget;
  const pct = t.relaxations_budget
    ? Math.min(100, 100 * t.relaxations_used / t.relaxations_budget) : 0;
  $("campaign-chip").textContent = s.meta.last_activity
    ? `last write ${s.meta.last_activity} UTC` : "";
  $("campaign-card").innerHTML = `
    <div class="stat-grid">
      <div class="stat"><div class="v">${t.iterations_done}<span class="u"> / ${b.iterations}</span></div>
        <div class="k">Iterations</div></div>
      <div class="stat"><div class="v">${t.proposed}</div><div class="k">Proposed</div></div>
      <div class="stat"><div class="v">${t.scored}</div><div class="k">Scored</div></div>
      <div class="stat"><div class="v hit-v">${t.hits}</div>
        <div class="k">Hits · ${t.rediscoveries} rediscover${t.rediscoveries === 1 ? "y" : "ies"}</div></div>
    </div>
    <div class="meter" aria-label="Relaxation budget">
      <div class="track"><div class="fill" style="width:${pct}%"></div></div>
      <div class="cap"><span>relaxations ${t.relaxations_used} / ${t.relaxations_budget}</span>
        <span>errors ${t.errors}</span></div>
    </div>`;
}

function renderAgent(s) {
  const m = s.mission, t = s.totals;
  const criticLine = m.critic.enabled
    ? `critic ${esc(m.critic.model || m.llm.model)} · fresh context per review · fails open`
    : "critic disabled in mission.yaml";
  $("agent-card").innerHTML = `
    <div class="sum-title">${esc(m.llm.model)}
      <span style="font-weight:400; color:var(--faint); font-size:12px">via ${esc(m.llm.backend)}</span></div>
    <div class="sum-meta" style="font-family:inherit">${criticLine}</div>
    <div style="display:flex; gap:6px; flex-wrap:wrap; margin-top:2px">
      <span class="pill note">${t.vetoed} vetoes · 0 eV spent</span>
      <span class="pill dim">${t.filtered_out - t.vetoed} filtered pre-compute</span>
      ${t.errors ? `<span class="pill warn">${t.errors} relax errors</span>` : ""}
    </div>
    <div class="sum-note">Vetoes cost zero relaxation budget — recorded as filtered_out rows for audit.</div>`;
}

/* ── discovery loop ────────────────────────────────────────────── */

function stageHtml(name, count, sub, cls = "") {
  return `<div class="stage ${cls}">
    <span class="s-name">${name}</span>
    <span class="s-count">${count}</span>
    <span class="s-sub">${sub}</span></div>`;
}
function flowHtml(drop = "", cls = "") {
  return `<div class="flow"><span class="arrow">→</span>
    ${drop ? `<span class="drop ${cls}">${drop}</span>` : ""}</div>`;
}

function renderPipeline(s) {
  const iters = s.iterations;
  if (!iters.length) {
    $("pipeline").innerHTML = `<p class="empty">no iterations yet — the loop appears here live</p>`;
    $("loopback").hidden = true;
    $("pipeline-title").textContent = "Discovery loop";
    return;
  }
  const it = iters[iters.length - 1];
  const total = it.proposed + it.filtered_out + it.scored + it.error;
  const chemFiltered = it.filtered_out - it.vetoed;
  const afterFilter = total - chemFiltered;
  const afterCritic = afterFilter - it.vetoed;
  const evaluated = it.scored + it.error;
  const hitsIter = s.candidates.filter((c) => c.iteration === it.iteration && c.flags.hit).length;
  const nbIter = s.notebook.filter((e) => e.iteration === it.iteration).length;
  const live = s.meta.running;

  $("pipeline-title").textContent = `Discovery loop — iteration ${it.iteration}`;
  $("pipeline").innerHTML =
    stageHtml("Propose", total, "prototype substitution, notebook + literature recall")
    + flowHtml(chemFiltered ? `−${chemFiltered} filtered` : "", "filtered")
    + stageHtml("Filter", afterFilter, "SMACT + mission chemistry — before any compute")
    + flowHtml(it.vetoed ? `−${it.vetoed} vetoed` : "", "veto")
    + stageHtml("Critic", afterCritic, "independent review · skeptical persona")
    + flowHtml(it.error ? `−${it.error} error` : "", "err")
    + stageHtml("Evaluate",
        `${evaluated}<span class="u"> / ${s.mission.budget.max_relaxations_per_iteration}</span>`,
        "CHGNet relax → E_hull · MEGNet gap (HSE)", live ? "active" : "")
    + flowHtml()
    + stageHtml("Record",
        `${hitsIter ? "+" + hitsIter : "0"}<span class="u"> hits</span>`,
        `DB rows · ${nbIter} notebook entr${nbIter === 1 ? "y" : "ies"}`, "terminal");

  $("loopback").hidden = false;
  const done = s.totals.iterations_done, planned = s.mission.budget.iterations;
  $("loopback-next").textContent = done < planned
    ? `next: iteration ${it.iteration + 1} / ${planned}` : "campaign complete";
}

/* ── composition map ───────────────────────────────────────────── */

function niceTicks(max, step) {
  const ticks = [];
  for (let v = 0; v <= max + 1e-9; v += step) ticks.push(+v.toFixed(4));
  return ticks;
}

function renderMap(s) {
  const pts = s.candidates.filter(
    (c) => c.e_above_hull != null && c.band_gap_ev != null);
  $("best-gap").textContent = s.totals.best_gap_distance != null
    ? `${s.totals.best_gap_distance.toFixed(2)} eV` : "—";
  if (!pts.length) {
    $("map").innerHTML = `<p class="empty">no scored candidates yet</p>`;
    $("map-caption").textContent = "";
    return;
  }
  const [lo, hi] = s.mission.band_gap_ev;
  const hullMax = s.mission.e_above_hull_max;
  const W = 860, H = 480, L = 64, R = 24, T = 20, B = 60;
  const xMax = Math.max(0.32, ...pts.map((p) => p.e_above_hull)) * 1.06;
  const yMax = Math.max(3.2, hi * 1.2, ...pts.map((p) => p.band_gap_ev)) * 1.05;
  const X = (v) => L + (v / xMax) * (W - L - R);
  const Y = (v) => H - B - (v / yMax) * (H - T - B);
  const xStep = xMax > 0.6 ? 0.1 : 0.05, yStep = 0.5;
  const maxIter = Math.max(...pts.map((p) => p.iteration));

  let g = `<rect width="${W}" height="${H}" fill="#fffdf9"/>`;
  for (const v of niceTicks(yMax, yStep)) {
    g += `<line x1="${L}" y1="${Y(v)}" x2="${W - R}" y2="${Y(v)}" stroke="#eee7da"/>`
       + `<text x="${L - 8}" y="${Y(v) + 3.5}" font-size="9.5" fill="#94897a"
            text-anchor="end" font-family="IBM Plex Mono, monospace">${v.toFixed(1)}</text>`;
  }
  for (const v of niceTicks(xMax, xStep)) {
    g += `<line x1="${X(v)}" y1="${T}" x2="${X(v)}" y2="${H - B}" stroke="#eee7da"/>`
       + `<text x="${X(v)}" y="${H - B + 18}" font-size="10" fill="#94897a"
            text-anchor="middle" font-family="IBM Plex Mono, monospace">${v.toFixed(2)}</text>`;
  }
  g += `<line x1="${L}" y1="${T}" x2="${L}" y2="${H - B}" stroke="#c9c0b0"/>`
     + `<line x1="${L}" y1="${H - B}" x2="${W - R}" y2="${H - B}" stroke="#c9c0b0"/>`
     + `<rect x="${X(0)}" y="${Y(hi)}" width="${X(hullMax) - X(0)}" height="${Y(lo) - Y(hi)}"
          fill="#3f6b25" opacity="0.09"/>`
     + `<rect x="${X(0)}" y="${Y(hi)}" width="${X(hullMax) - X(0)}" height="${Y(lo) - Y(hi)}"
          fill="none" stroke="#3f6b25" stroke-width="1.1" stroke-dasharray="5 3" opacity="0.55"/>`
     + `<text x="${X(hullMax) + 6}" y="${Y(hi) + 11}" font-size="10.5" fill="#3f6b25"
          font-weight="600" font-family="IBM Plex Sans, sans-serif">target window</text>`
     + `<text x="${(L + W - R) / 2}" y="${H - 14}" font-size="11" fill="#5f594f" text-anchor="middle"
          font-family="IBM Plex Sans, sans-serif">energy above hull (eV/atom)</text>`
     + `<text x="16" y="${(T + H - B) / 2}" font-size="11" fill="#5f594f" text-anchor="middle"
          font-family="IBM Plex Sans, sans-serif"
          transform="rotate(-90 16 ${(T + H - B) / 2})">band gap, HSE fidelity (eV)</text>`;

  const labels = [];
  for (const p of pts) {
    const cx = X(p.e_above_hull), cy = Y(p.band_gap_ev);
    const tip = `${p.formula} · gap ${p.band_gap_ev.toFixed(2)} eV · hull `
      + `${p.e_above_hull.toFixed(3)} · iter ${p.iteration}`
      + (p.flags.hit ? " · HIT" : p.flags.rediscovery ? " · REDISCOVERY" : "")
      + (p.is_novel === 0 ? " · known" : "");
    let fill = "#1f4fd8", r = 5, op = 0.62, ring = "";
    if (colorMode === "iteration") {
      op = maxIter > 1 ? 0.25 + 0.65 * ((p.iteration - 1) / (maxIter - 1)) : 0.7;
    } else if (p.flags.hit) {
      fill = "#3f6b25"; r = 6.5; op = 1; ring = `stroke="#fffdf9" stroke-width="2"`;
      labels.push({cx, cy, text: pretty(p.formula), color: "#3f6b25"});
    } else if (p.flags.rediscovery) {
      fill = "#a87a10"; r = 6.5; op = 1; ring = `stroke="#fffdf9" stroke-width="2"`;
      labels.push({cx, cy, text: pretty(p.formula), color: "#a87a10"});
    }
    g += `<circle cx="${cx}" cy="${cy}" r="${r}" fill="${fill}" opacity="${op}" ${ring}>
            <title>${esc(tip)}</title></circle>`;
  }
  labels.sort((a, b) => a.cy - b.cy).forEach((lb, i) => {
    const left = lb.cx > W * 0.75;
    const prev = labels[i - 1];
    if (prev && Math.abs(lb.cy - prev.cy) < 13 && Math.abs(lb.cx - prev.cx) < 90) {
      lb.cy = prev.cy + 13; // simple collision nudge for clustered hits
    }
    g += `<text x="${left ? lb.cx - 10 : lb.cx + 10}" y="${lb.cy + 3.5}" font-size="10.5"
          fill="${lb.color}" font-weight="600" text-anchor="${left ? "end" : "start"}"
          font-family="IBM Plex Mono, monospace">${esc(lb.text)}</text>`;
  });

  if (colorMode === "status") {
    g += `<circle cx="${W - 248}" cy="${T + 14}" r="5" fill="#1f4fd8" opacity="0.62"/>
      <text x="${W - 238}" y="${T + 18}" font-size="11" fill="#5f594f">scored</text>
      <circle cx="${W - 178}" cy="${T + 14}" r="5.5" fill="#3f6b25"/>
      <text x="${W - 168}" y="${T + 18}" font-size="11" fill="#5f594f">hit (novel)</text>
      <circle cx="${W - 92}" cy="${T + 14}" r="5.5" fill="#a87a10"/>
      <text x="${W - 82}" y="${T + 18}" font-size="11" fill="#5f594f">rediscovery</text>`;
  } else {
    g += `<text x="${W - R}" y="${T + 18}" font-size="11" fill="#5f594f" text-anchor="end">
      opacity = iteration (late is darker)</text>`;
  }

  $("map").innerHTML = `<svg viewBox="0 0 ${W} ${H}" preserveAspectRatio="none" role="img"
    aria-label="Band gap versus energy above hull; target window marked">${g}</svg>`;
  $("map-caption").innerHTML =
    `<span>${pts.length} scored candidates · ${s.totals.iterations_done} iterations ·
     hover a point for formula, gap, hull, iteration</span>`;
}

/* ── feed ──────────────────────────────────────────────────────── */

function renderFeed(feed) {
  $("feed-chip").textContent = feed.length ? `last ${feed.length} events` : "";
  if (!feed.length) {
    $("feed").innerHTML = `<p class="empty">no events yet</p>`;
    return;
  }
  $("feed").innerHTML = feed.map((e) => `
    <div class="evt">
      <span class="t">${esc(e.when.slice(5))}</span>
      <span class="tag ${esc(e.kind)}">${esc(e.kind)}</span>
      <span class="m">${e.formula ? `<span class="f">${esc(pretty(e.formula))}</span> ` : ""}${esc(e.text)}</span>
    </div>`).join("");
}

/* ── top candidates ────────────────────────────────────────────── */

function statusPill(flags, isNovel) {
  if (flags.hit) return `<span class="pill ok">● hit${isNovel === 1 ? " · novel" : ""}</span>`;
  if (flags.rediscovery) return `<span class="pill note">◆ rediscovery</span>`;
  return `<span class="pill free">scored</span>`;
}

function renderTop(s) {
  $("rank-chip").textContent =
    `ranked by hull within gap window first`;
  const rows = s.top;
  if (!rows.length) {
    $("top-body").innerHTML = `<tr><td colspan="6" class="empty">no data yet</td></tr>`;
    return;
  }
  $("top-body").innerHTML = rows.map((r) => `
    <tr>
      <td class="f">${esc(pretty(r.formula))}</td>
      <td class="num">${r.band_gap_ev != null ? r.band_gap_ev.toFixed(2) : "—"}</td>
      <td class="num">${r.e_above_hull != null ? r.e_above_hull.toFixed(3) : "—"}</td>
      <td class="num">${r.iteration}</td>
      <td>${statusPill(r.flags, r.is_novel)}</td>
      <td class="hyp" title="${esc(r.hypothesis || "")}">${esc(r.hypothesis || "—")}</td>
    </tr>`).join("");
}

/* ── notebook ──────────────────────────────────────────────────── */

function nbEntryHtml(e, clamp) {
  return `<article class="nb-entry ${esc(e.type)} ${clamp ? "clamp" : ""}">
    <div class="nb-head">
      <span class="pill ${e.type === "hypothesis" ? "free" : e.type === "reflection" ? "ok" : "note"}">${esc(e.type)}</span>
      <span class="when">iter ${e.iteration} · ${esc(e.when)}</span>
    </div>
    <p>${esc(e.text)}</p></article>`;
}

function renderNotebookPanel(entries) {
  const recent = entries.slice(-4).reverse();
  $("notebook-panel").innerHTML = recent.length
    ? recent.map((e) => nbEntryHtml(e, true)).join("")
    : `<p class="empty">no entries yet</p>`;
}

function renderNotebookPage(entries) {
  $("nb-count").textContent = entries.length ? `${entries.length} entries` : "";
  $("notebook-full").innerHTML = entries.length
    ? entries.slice().reverse().map((e) => nbEntryHtml(e, false)).join("")
    : `<p class="empty">no entries yet</p>`;
}

/* ── benchmark page ────────────────────────────────────────────── */

async function renderBenchmark() {
  let b;
  try {
    b = await (await fetch("/api/benchmark")).json();
  } catch {
    return;
  }
  if (!b.available) {
    $("bench-body").innerHTML = `<p class="empty">no benchmark run found —
      produce one with <span class="mono">athanor benchmark</span></p>`;
    $("bench-budget").textContent = "";
    return;
  }
  $("bench-title").textContent = `Benchmark — ${b.title}`;
  $("bench-budget").textContent = b.budget;
  const cols = b.rows.length ? Object.keys(b.rows[0]) : [];
  const table = b.rows.length ? `
    <div class="tbl-scroll"><table class="cands">
      <thead><tr>${cols.map((c) => `<th>${esc(c)}</th>`).join("")}</tr></thead>
      <tbody>${b.rows.map((r) => `<tr>${cols.map((c, i) =>
        `<td class="${i ? "num" : "f"}">${esc(r[c])}</td>`).join("")}</tr>`).join("")}
      </tbody></table></div>` : "";
  $("bench-body").innerHTML = table
    + (b.hit_definition ? `<p class="bench-note">hit = ${esc(b.hit_definition)}</p>` : "")
    + (b.has_plot ? `<img class="bench-img" src="/api/benchmark/plot.png"
         alt="hits per 100 relaxations by strategy">` : "");
}

/* ── wiring ────────────────────────────────────────────────────── */

document.querySelectorAll(".page-pill").forEach((btn) => {
  btn.addEventListener("click", () => {
    document.querySelectorAll(".page-pill").forEach((b) => b.classList.remove("active"));
    btn.classList.add("active");
    for (const page of ["campaign", "benchmark", "notebook"]) {
      $(`page-${page}`).hidden = page !== btn.dataset.page;
    }
    if (btn.dataset.page === "benchmark") renderBenchmark();
  });
});

document.querySelectorAll(".seg button").forEach((btn) => {
  btn.addEventListener("click", () => {
    document.querySelectorAll(".seg button").forEach((b) => b.classList.remove("active"));
    btn.classList.add("active");
    colorMode = btn.dataset.color;
    if (snapshot) renderMap(snapshot);
  });
});

$("open-notebook").addEventListener("click", () => {
  document.querySelector('[data-page="notebook"]').click();
});

$("export-csv").addEventListener("click", () => {
  if (!snapshot || !snapshot.candidates.length) return;
  const cols = ["iteration", "formula", "band_gap_ev", "e_above_hull",
                "formation_energy_per_atom", "converged", "is_novel"];
  const lines = [cols.join(",") + ",hit,rediscovery"];
  for (const c of snapshot.candidates) {
    lines.push(cols.map((k) => c[k] ?? "").join(",")
      + `,${c.flags.hit ? 1 : 0},${c.flags.rediscovery ? 1 : 0}`);
  }
  const blob = new Blob([lines.join("\n")], {type: "text/csv"});
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = `athanor-${snapshot.mission.name}-candidates.csv`;
  a.click();
  URL.revokeObjectURL(a.href);
});

refresh();
setInterval(refresh, 10_000);
