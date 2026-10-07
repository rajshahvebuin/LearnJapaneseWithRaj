// Learn Japanese with Raj: practice quiz
//
// Renders into <div class="tool-app" data-tool="quiz" data-src="…/assets/data/n1/quiz/" data-site-root="../">.
// index.json lists question banks: {banks:[{id, module, title, title_en, count, file}]}.
// Each bank file holds items: {q, qr?, en?, opts:[{t, r?, en?}], a, why?, src, unit}.
(function () {
  "use strict";

  const app = document.querySelector('.tool-app[data-tool="quiz"]');
  if (!app) return;

  const SRC = app.dataset.src;
  const ROOT = app.dataset.siteRoot || "";
  const LEVEL = app.dataset.level || "n1";
  const STORE = `ljwr-quiz-${LEVEL}`;
  const MODULE_NAMES = {
    grammar: "Grammar", vocabulary: "Vocabulary", kanji: "Kanji",
    "multi-skill": "All-in-one books", "mock-tests": "Mock tests",
  };
  const MODULE_ORDER = ["grammar", "vocabulary", "kanji", "multi-skill", "mock-tests"];

  const h = (tag, attrs, ...kids) => {
    const el = document.createElement(tag);
    for (const [k, v] of Object.entries(attrs || {})) {
      if (v == null || v === false) continue;
      if (k === "class") el.className = v;
      else if (k.startsWith("on")) el.addEventListener(k.slice(2), v);
      else el.setAttribute(k, v === true ? "" : v);
    }
    for (const kid of kids.flat()) {
      if (kid == null || kid === false) continue;
      el.append(kid.nodeType ? kid : document.createTextNode(String(kid)));
    }
    return el;
  };
  const load = (key, fallback) => {
    try {
      const v = localStorage.getItem(key);
      return v ? JSON.parse(v) : fallback;
    } catch (e) {
      return fallback;
    }
  };
  const save = (key, value) => {
    try {
      localStorage.setItem(key, JSON.stringify(value));
    } catch (e) {
      /* storage unavailable */
    }
  };
  const shuffle = (arr) => {
    for (let i = arr.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
  };
  const itemsOf = (data) => (Array.isArray(data) ? data : data.items || data.questions || data.cards || []);
  async function fetchJSON(url) {
    const res = await fetch(url, { cache: "force-cache" });
    if (!res.ok) throw new Error(`${res.status} ${url}`);
    return res.json();
  }

  const prefs = load(`${STORE}-prefs`, { banks: null, size: 20, romaji: true });
  let banks = [];
  const cache = {};
  let questions = [];
  let qi = 0;
  let answers = []; // {pick, correct}
  let answered = false;

  async function bankItems(b) {
    if (!cache[b.id]) cache[b.id] = itemsOf(await fetchJSON(SRC + (b.file || `${b.id}.json`))).map((it) => ({ ...it, bank: b.id }));
    return cache[b.id];
  }

  // ---------- setup screen ----------
  function setup() {
    const chosen = new Set(prefs.banks && prefs.banks.length ? prefs.banks : banks.map((b) => b.id));
    const boxes = [];
    const sum = h("span", { class: "sum" });
    const refreshSum = () => {
      const n = banks.filter((b) => chosen.has(b.id)).reduce((t, b) => t + (b.count || 0), 0);
      sum.textContent = `${chosen.size} book${chosen.size === 1 ? "" : "s"} · ${n.toLocaleString()} questions to draw from`;
      startBtn.disabled = n === 0;
    };
    const groups = MODULE_ORDER.concat([...new Set(banks.map((b) => b.module))].filter((m) => !MODULE_ORDER.includes(m)))
      .map((mod) => {
        const list = banks.filter((b) => b.module === mod);
        if (!list.length) return null;
        const items = list.map((b) => {
          const input = h("input", { type: "checkbox", value: b.id });
          input.checked = chosen.has(b.id);
          input.addEventListener("change", () => {
            if (input.checked) chosen.add(b.id);
            else chosen.delete(b.id);
            refreshSum();
          });
          boxes.push(input);
          return h("label", { class: "qz-bank" }, input,
            h("span", {}, h("span", { class: "t", lang: "ja" }, b.title), h("span", { class: "s" }, `${b.title_en ? b.title_en + " · " : ""}${(b.count || 0).toLocaleString()} questions`)));
        });
        const setAll = (on) => {
          items.forEach((lab) => {
            const input = lab.querySelector("input");
            input.checked = on;
            if (on) chosen.add(input.value);
            else chosen.delete(input.value);
          });
          refreshSum();
        };
        return h("div", { class: "qz-group" },
          h("div", { class: "qz-group-head" }, h("h3", {}, MODULE_NAMES[mod] || mod),
            h("span", {}, h("button", { type: "button", onclick: () => setAll(true) }, "All"), " · ", h("button", { type: "button", onclick: () => setAll(false) }, "None"))),
          h("div", { class: "qz-banks" }, items));
      });

    const sizeChips = [10, 20, 50, 100].map((n) => h("button", {
      class: "chip", type: "button", "aria-pressed": String(prefs.size === n),
      onclick: (e) => {
        prefs.size = n;
        sizeChips.forEach((c) => c.setAttribute("aria-pressed", String(c === e.currentTarget)));
      },
    }, `${n} questions`));
    const romajiBox = h("input", { type: "checkbox" });
    romajiBox.checked = prefs.romaji;
    romajiBox.addEventListener("change", () => (prefs.romaji = romajiBox.checked));

    const startBtn = h("button", { class: "btn btn-primary", type: "button", onclick: () => start([...chosen]) }, "Start quiz →");
    refreshSum();

    app.replaceChildren(h("div", { class: "qz-setup" },
      h("div", { class: "qz-panel" },
        h("h2", {}, "1. Choose the books"),
        h("p", {}, "Questions come from the exercises on the study pages. Every answer is the one the book's key gives."),
        groups),
      h("div", { class: "qz-panel" },
        h("h2", {}, "2. Set up the round"),
        h("div", { class: "qz-row" }, sizeChips, h("label", { class: "tl-toggle" }, romajiBox, "Show romaji"))),
      h("div", { class: "qz-panel qz-start-row" }, sum, startBtn)));
  }

  async function start(bankIds, fixed) {
    prefs.banks = bankIds;
    save(`${STORE}-prefs`, prefs);
    if (fixed) {
      questions = fixed;
    } else {
      app.replaceChildren(h("p", { class: "tool-loading" }, "Picking questions…"));
      const chosen = banks.filter((b) => bankIds.includes(b.id));
      const pools = await Promise.all(chosen.map(bankItems));
      questions = shuffle(pools.flat().filter((q) => q.opts && q.opts.length > 1 && q.a >= 0 && q.a < q.opts.length)).slice(0, prefs.size);
    }
    qi = 0;
    answers = [];
    question();
  }

  // ---------- question screen ----------
  function question() {
    const q = questions[qi];
    answered = false;
    const bank = banks.find((b) => b.id === q.bank);
    const bar = h("div", { class: "tl-progress" }, h("i", { style: `width:${(qi / questions.length) * 100}%` }));
    const score = answers.filter((a) => a.correct).length;
    const feedback = h("div", { class: "qz-feedback", hidden: true });
    const nextBtn = h("button", { class: "btn btn-primary", type: "button", hidden: true, onclick: next }, qi + 1 < questions.length ? "Next question →" : "See results →");

    const allRomaji = q.opts.every((o) => o.r);
    const opts = q.opts.map((o, i) => h("button", { class: "qz-opt", type: "button", onclick: () => pick(i) },
      h("span", { class: "num" }, String(i + 1)),
      h("span", {},
        h("span", { class: "t", lang: "ja" }, o.t || "—"),
        // Some books print romaji only under the correct option; show it up front
        // only when every option has it, otherwise reveal it after answering.
        prefs.romaji && o.r ? h("span", { class: "r", hidden: !allRomaji }, o.r) : null,
        o.en || o.hi || o.gu ? h("span", { class: "e" }, langLine(o)) : null)));

    function pick(i) {
      if (answered) return;
      answered = true;
      const correct = i === q.a;
      answers.push({ q, pick: i, correct });
      opts.forEach((b, j) => {
        b.disabled = true;
        b.classList.add("revealed");
        b.querySelectorAll(".r[hidden]").forEach((r) => (r.hidden = false));
        if (j === q.a) b.classList.add("correct");
        else if (j === i) b.classList.add("wrong");
      });
      app.querySelectorAll(".qz-sent-r[hidden]").forEach((r) => (r.hidden = false));
      feedback.replaceChildren(
        h("div", { class: `verdict ${correct ? "ok" : "no"}` }, correct ? "✓ Correct" : `✗ The answer is ${q.a + 1}: ${q.opts[q.a].t}`),
        q.en || q.hi || q.gu ? h("div", { class: "qz-langs" },
          ["en", "hi", "gu"].map((k) => (q[k] ? h("div", { class: "qz-lang" }, h("b", {}, k.toUpperCase()), h("span", { lang: k }, q[k])) : null))) : null,
        q.why ? h("p", {}, h("b", {}, "Why: "), q.why) : null,
        q.src ? h("p", { class: "src" }, "From ", h("a", { href: ROOT + q.src }, q.unit || "the study page"), " →") : null);
      feedback.hidden = false;
      nextBtn.hidden = false;
      nextBtn.focus({ preventScroll: true });
    }

    app.replaceChildren(
      h("div", { class: "tl-status" },
        h("span", {}, h("b", {}, `Question ${qi + 1} of ${questions.length}`)),
        h("span", {}, "Score ", h("b", {}, `${score} / ${answers.length}`))),
      bar,
      h("div", { class: "qz-card" },
        h("div", { class: "qz-meta" }, h("span", { class: "unit" }, bank ? bank.title : ""), h("span", {}, q.unit || "")),
        questionText(q),
        // For underlined-word (reading/writing) questions the sentence romaji gives the answer away.
        prefs.romaji && q.qr ? h("div", { class: "qz-qr qz-sent-r", hidden: !!q.u }, q.qr) : null,
        h("div", { class: "qz-opts" }, opts),
        feedback,
        h("div", { class: "qz-nav" },
          h("button", { class: "btn btn-sm", type: "button", onclick: finish }, "End quiz"),
          h("span", { class: "qz-keys" }, "Keys ", h("kbd", {}, "1"), "–", h("kbd", {}, String(q.opts.length)), " answer · ", h("kbd", {}, "Enter"), " next"),
          nextBtn)));

    keyHandler = (e) => {
      if (e.target.closest("input, select, textarea")) return;
      const n = parseInt(e.key, 10);
      if (!answered && n >= 1 && n <= q.opts.length) pick(n - 1);
      else if (answered && e.key === "Enter" && !e.target.closest("button, a")) next();
    };
  }

  // Option meanings in all three languages on one line: "EN · HI · GU".
  function langLine(o) {
    return ["en", "hi", "gu"].filter((k) => o[k]).map((k) => h("span", { lang: k }, o[k])).flatMap((el, i) => (i ? [" · ", el] : [el]));
  }

  // Kanji-reading and usage questions ask about one underlined word (field `u`,
  // sometimes "word / romaji"). Underline it in the sentence, or name it if absent.
  function questionText(q) {
    const word = q.u ? String(q.u).split(" / ")[0].trim() : "";
    const p = h("p", { class: "qz-q", lang: "ja" });
    const at = word ? q.q.indexOf(word) : -1;
    if (at >= 0) {
      p.append(q.q.slice(0, at), h("u", { class: "qz-u" }, word), q.q.slice(at + word.length));
      return p;
    }
    p.append(q.q);
    if (!word) return p;
    return h("div", {}, p, h("div", { class: "qz-qr" }, "Underlined word: ", h("u", { class: "qz-u", lang: "ja" }, word)));
  }

  function next() {
    if (qi + 1 < questions.length) {
      qi += 1;
      question();
    } else finish();
  }

  // ---------- results ----------
  function finish() {
    keyHandler = null;
    const total = answers.length;
    const right = answers.filter((a) => a.correct).length;
    const pct = total ? Math.round((right / total) * 100) : 0;
    const missed = answers.filter((a) => !a.correct);
    const best = load(`${STORE}-best`, 0);
    if (total >= 10 && pct > best) save(`${STORE}-best`, pct);

    app.replaceChildren(h("div", { class: "qz-card" },
      h("div", { class: "qz-result" },
        h("div", { class: "qz-score" }, `${pct}%`),
        h("p", {}, `${right} of ${total} correct${total < questions.length ? ` (stopped after ${total} of ${questions.length})` : ""}.`,
          best ? ` Best round so far: ${Math.max(best, total >= 10 ? pct : 0)}%.` : ""),
        h("div", { class: "qz-row" },
          missed.length ? h("button", { class: "btn btn-primary", type: "button", onclick: () => start(prefs.banks, shuffle(missed.map((m) => m.q))) }, `Retry the ${missed.length} missed`) : null,
          h("button", { class: "btn", type: "button", onclick: () => start(prefs.banks) }, "New round, same books"),
          h("button", { class: "btn", type: "button", onclick: setup }, "Change books"))),
      missed.length ? h("div", { class: "qz-review" },
        h("h3", { style: "margin:0" }, "Review what you missed"),
        missed.map(({ q, pick }) => h("div", { class: "qz-review-item" },
          h("div", { class: "q", lang: "ja" }, q.q),
          h("div", { class: "a" }, "Answer ", h("b", { lang: "ja" }, q.opts[q.a].t), " · you chose ", h("s", { lang: "ja" }, q.opts[pick].t)),
          q.why ? h("div", { class: "a" }, q.why) : null,
          q.src ? h("div", { class: "src" }, h("a", { href: ROOT + q.src }, q.unit || "Study page"), " →") : null))) : null));
  }

  let keyHandler = null;
  document.addEventListener("keydown", (e) => keyHandler && keyHandler(e));

  // ---------- boot ----------
  (async function init() {
    try {
      const index = await fetchJSON(SRC + "index.json");
      banks = (index.banks || []).filter((b) => b.count !== 0);
      if (!banks.length) throw new Error("no banks");
      setup();
    } catch (err) {
      app.replaceChildren(h("p", { class: "tool-error" },
        "The quiz data could not be loaded. If you opened this file directly from disk, run a local web server (for example ",
        h("code", {}, "python -m http.server"), ") and open the page through it."));
      console.error(err);
    }
  })();
})();
