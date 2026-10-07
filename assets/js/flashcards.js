// Learn Japanese with Raj: flashcards (vocabulary + kanji)
//
// Renders into <div class="tool-app" data-tool="cards" data-src="…/assets/data/n1/" data-site-root="../">.
// Reads vocab/index.json and kanji/index.json (lists of decks) and loads a deck file on demand.
// One deck menu covers both kinds: "All vocabulary", "All kanji", or a single book.
//
// Card shapes (from tools/extract_study_data.py):
//   vocab:        {jp, r, en, hi, gu, note?, src, unit}
//   kanji (char): {k, words:[{w, kana, r, en, hi, gu}], src, unit}
//   kanji (word): {w, kana, r, en, hi, gu, src, unit}
(function () {
  "use strict";

  const app = document.querySelector('.tool-app[data-tool="cards"]');
  if (!app) return;

  const BASE = app.dataset.src;
  const KINDS = { vocab: "Vocabulary", kanji: "Kanji" };
  const ROOT = app.dataset.siteRoot || "";
  const LEVEL = app.dataset.level || "n1";
  const STORE = `ljwr-fc-${LEVEL}`;

  // ---------- tiny helpers ----------
  const h = (tag, attrs, ...kids) => {
    const el = document.createElement(tag);
    for (const [k, v] of Object.entries(attrs || {})) {
      if (v == null || v === false) continue;
      if (k === "class") el.className = v;
      else if (k === "text") el.textContent = v;
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
      /* storage unavailable: progress just isn't remembered */
    }
  };
  const shuffle = (arr) => {
    for (let i = arr.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
  };
  const cardsOf = (data) => (Array.isArray(data) ? data : data.cards || data.items || []);
  const cardId = (deckId, c) => `${deckId}|${c.k || c.jp || c.w}`;

  // ---------- state ----------
  const prefs = load(`${STORE}-prefs`, { deck: "vocab:*", reverse: false, romaji: true, hideKnown: false, shuffled: false });
  const known = new Set(load(`${STORE}-known`, []));
  let decks = [];
  const deckCache = {};
  let all = []; // [{deckId, card}]
  let view = []; // filtered + ordered
  let pos = 0;
  let flipped = false;
  let query = "";

  // ---------- data ----------
  async function fetchJSON(url) {
    const res = await fetch(url, { cache: "force-cache" });
    if (!res.ok) throw new Error(`${res.status} ${url}`);
    return res.json();
  }

  async function loadDeck(d) {
    if (!deckCache[d.key]) deckCache[d.key] = cardsOf(await fetchJSON(`${BASE}${d.kind}/${d.file || d.id + ".json"}`));
    return deckCache[d.key];
  }

  // value is "<kind>:*" for every book of that kind, or a single deck key "<kind>:<id>"
  async function selectDeck(value) {
    prefs.deck = value;
    save(`${STORE}-prefs`, prefs);
    const [kind, id] = value.split(":");
    const chosen = decks.filter((d) => d.kind === kind && (id === "*" || d.id === id));
    status.textContent = "Loading cards…";
    const lists = await Promise.all(chosen.map(loadDeck));
    all = [];
    chosen.forEach((d, i) => lists[i].forEach((card) => all.push({ deckId: d.key, card })));
    rebuild(false);
  }

  function rebuild(keepOrder) {
    const q = query.trim().toLowerCase();
    let list = all.filter(({ deckId, card }) => {
      if (prefs.hideKnown && known.has(cardId(deckId, card))) return false;
      if (!q) return true;
      return searchText(card).includes(q);
    });
    if (!keepOrder && prefs.shuffled) list = shuffle(list);
    view = list;
    pos = 0;
    flipped = false;
    render();
  }

  function searchText(c) {
    const parts = [c.k, c.jp, c.w, c.kana, c.r, c.en, c.hi, c.gu];
    (c.words || []).forEach((w) => parts.push(w.w, w.kana, w.r, w.en));
    return parts.filter(Boolean).join(" ").toLowerCase();
  }

  // ---------- rendering ----------
  const deckSelect = h("select", { "aria-label": "Deck", onchange: (e) => selectDeck(e.target.value) });
  const search = h("input", {
    type: "search",
    placeholder: "Search word, kanji, reading, meaning",
    "aria-label": "Search cards",
    oninput: (e) => {
      query = e.target.value;
      rebuild(true);
    },
  });
  const toggle = (label, key, onchange) => {
    const input = h("input", { type: "checkbox" });
    input.checked = !!prefs[key];
    input.addEventListener("change", () => {
      prefs[key] = input.checked;
      save(`${STORE}-prefs`, prefs);
      onchange();
    });
    return h("label", { class: "tl-toggle" }, input, label);
  };
  const bar = h("div", { class: "tl-bar" },
    deckSelect, search,
    toggle("Meaning first", "reverse", () => render()),
    toggle("Romaji", "romaji", () => render()),
    toggle("Hide known", "hideKnown", () => rebuild(true)),
    toggle("Shuffle", "shuffled", () => rebuild(false)));

  const status = h("div", { class: "tl-status" });
  const progress = h("div", { class: "tl-progress" }, h("i"));
  const stage = h("div", { class: "fc-stage" });
  const actions = h("div", { class: "fc-actions" },
    h("button", { class: "btn fc-prev", type: "button", "aria-label": "Previous card", onclick: () => go(-1) }, "←"),
    h("button", { class: "btn fc-again", type: "button", onclick: () => mark(false) }, "Again"),
    h("button", { class: "btn fc-know", type: "button", onclick: () => mark(true) }, "Know it ✓"),
    h("button", { class: "btn fc-next", type: "button", "aria-label": "Next card", onclick: () => go(1) }, "→"));
  const keys = h("p", { class: "fc-keys" },
    h("kbd", {}, "Space"), " flip · ", h("kbd", {}, "←"), " ", h("kbd", {}, "→"), " move · ",
    h("kbd", {}, "K"), " know it · ", h("kbd", {}, "A"), " again");

  function romaji(text) {
    return prefs.romaji && text ? h("div", { class: "fc-romaji" }, text) : null;
  }

  function langs(c) {
    return h("div", { class: "fc-langs" },
      c.en ? h("div", { class: "fc-lang" }, h("b", {}, "EN"), h("span", {}, c.en)) : null,
      c.hi ? h("div", { class: "fc-lang" }, h("b", {}, "HI"), h("span", { lang: "hi" }, c.hi)) : null,
      c.gu ? h("div", { class: "fc-lang" }, h("b", {}, "GU"), h("span", { lang: "gu" }, c.gu)) : null);
  }

  function srcLink(c) {
    if (!c.src) return null;
    return h("div", { class: "fc-src" }, "From ", h("a", { href: ROOT + c.src }, c.unit || "the study page"), " →");
  }

  function front(c) {
    if (prefs.reverse) {
      if (c.words) return [h("div", { class: "fc-meaning-front" }, c.words.map((w) => w.en).filter(Boolean).slice(0, 3).join(" · "))];
      return [h("div", { class: "fc-meaning-front" }, c.en || "")];
    }
    if (c.k) return [h("div", { class: "fc-kanji", lang: "ja" }, c.k)];
    if (c.w) return [h("div", { class: "fc-jp", lang: "ja" }, c.w)];
    return [h("div", { class: "fc-jp", lang: "ja" }, c.jp), romaji(c.r)];
  }

  function back(c) {
    if (c.words) {
      return [
        h("div", { class: "fc-back-head" }, h("div", { class: "fc-kanji", lang: "ja", style: "font-size:3.6rem" }, c.k)),
        h("div", { class: "fc-words" }, c.words.map((w) => h("div", { class: "fc-word" },
          h("div", { class: "fc-word-top" },
            h("span", { class: "w", lang: "ja" }, w.w),
            w.kana ? h("span", { class: "k", lang: "ja" }, w.kana) : null,
            prefs.romaji && w.r ? h("span", { class: "r" }, w.r) : null),
          h("div", { class: "m" }, w.en || "", w.hi ? h("span", { lang: "hi" }, ` · ${w.hi}`) : null, w.gu ? h("span", { lang: "gu" }, ` · ${w.gu}`) : null)))),
        srcLink(c),
      ];
    }
    const word = c.w || c.jp;
    return [
      h("div", { class: "fc-back-head" },
        h("div", { class: "fc-jp", lang: "ja" }, word),
        c.kana && c.kana !== word ? h("div", { class: "fc-kana", lang: "ja" }, c.kana) : null,
        romaji(c.r)),
      langs(c),
      c.note ? h("div", { class: "fc-note" }, c.note) : null,
      c.ex ? h("div", { class: "fc-note", lang: "ja" }, "例: ", c.ex) : null,
      srcLink(c),
    ];
  }

  function render() {
    const total = view.length;
    const knownHere = view.filter(({ deckId, card }) => known.has(cardId(deckId, card))).length;
    status.replaceChildren(
      h("span", {}, total ? h("b", {}, `${pos + 1} / ${total}`) : h("b", {}, "0 cards"), total ? " cards" : ""),
      h("span", {}, `Known: `, h("b", {}, String(known.size)), knownHere && !prefs.hideKnown ? ` (${knownHere} in this view)` : ""));
    progress.firstChild.style.width = total ? `${((pos + 1) / total) * 100}%` : "0";

    if (!total) {
      stage.replaceChildren(h("div", { class: "fc-empty" },
        query ? "No card matches your search." : prefs.hideKnown ? "You've marked every card in this deck as known. 🎉 Turn off “Hide known” to review them again." : "This deck has no cards."));
      actions.hidden = true;
      return;
    }
    actions.hidden = false;
    const { deckId, card } = view[pos];
    const isKnown = known.has(cardId(deckId, card));
    const deck = decks.find((d) => d.key === deckId);
    const tag = deck ? deck.title_en || deck.title : "";
    const cardEl = h("button", {
      class: "fc-card" + (flipped ? " flipped" : ""),
      type: "button",
      "aria-label": flipped ? "Card back. Press to show the front" : "Card front. Press to show the answer",
      onclick: flip,
    },
      h("div", { class: "fc-face fc-front" }, h("span", { class: "fc-tag" }, tag), isKnown ? h("span", { class: "fc-known-badge" }, "Known") : null, front(card), h("span", { class: "fc-hint" }, "Tap or press Space to flip")),
      h("div", { class: "fc-face fc-back" }, back(card)));
    stage.replaceChildren(cardEl);
  }

  function flip() {
    flipped = !flipped;
    const el = stage.querySelector(".fc-card");
    if (el) el.classList.toggle("flipped", flipped);
  }

  function go(step) {
    if (!view.length) return;
    pos = (pos + step + view.length) % view.length;
    flipped = false;
    render();
  }

  function mark(isKnown) {
    if (!view.length) return;
    const { deckId, card } = view[pos];
    const id = cardId(deckId, card);
    if (isKnown) known.add(id);
    else known.delete(id);
    save(`${STORE}-known`, [...known]);
    if (isKnown && prefs.hideKnown) {
      view.splice(pos, 1);
      if (pos >= view.length) pos = 0;
      flipped = false;
      render();
    } else if (!isKnown) {
      // "Again": push this card a few places later so it comes back soon.
      const item = view.splice(pos, 1)[0];
      view.splice(Math.min(pos + 4, view.length), 0, item);
      flipped = false;
      render();
    } else {
      go(1);
    }
  }

  document.addEventListener("keydown", (e) => {
    if (e.target.closest("input, select, textarea")) return;
    if (e.key === " " || e.key === "Enter") {
      // A focused button or link already handles Space/Enter itself.
      if (e.target.closest("button, a")) return;
      e.preventDefault();
      flip();
    } else if (e.key === "ArrowRight") go(1);
    else if (e.key === "ArrowLeft") go(-1);
    else if (e.key === "k" || e.key === "K") mark(true);
    else if (e.key === "a" || e.key === "A") mark(false);
  });

  // ---------- boot ----------
  (async function init() {
    try {
      for (const kind of Object.keys(KINDS)) {
        const index = await fetchJSON(`${BASE}${kind}/index.json`);
        const list = (index.decks || []).filter((d) => d.count !== 0).map((d) => ({ ...d, kind, key: `${kind}:${d.id}` }));
        if (!list.length) continue;
        decks.push(...list);
        const total = list.reduce((n, d) => n + (d.count || 0), 0);
        deckSelect.append(h("optgroup", { label: KINDS[kind] },
          h("option", { value: `${kind}:*` }, `All ${KINDS[kind].toLowerCase()} (${total.toLocaleString()} cards)`),
          list.map((d) => h("option", { value: d.key }, `${d.title}${d.title_en ? " · " + d.title_en : ""} (${(d.count || 0).toLocaleString()})`))));
      }
      if (!decks.length) throw new Error("no decks");
      const valid = [...deckSelect.querySelectorAll("option")].some((o) => o.value === prefs.deck);
      const startDeck = valid ? prefs.deck : `${decks[0].kind}:*`;
      deckSelect.value = startDeck;
      app.replaceChildren(bar, status, progress, stage, actions, keys);
      await selectDeck(startDeck);
    } catch (err) {
      app.replaceChildren(h("p", { class: "tool-error" },
        "The flashcard data could not be loaded. If you opened this file directly from disk, run a local web server (for example ",
        h("code", {}, "python -m http.server"), ") and open the page through it."));
      console.error(err);
    }
  })();
})();
