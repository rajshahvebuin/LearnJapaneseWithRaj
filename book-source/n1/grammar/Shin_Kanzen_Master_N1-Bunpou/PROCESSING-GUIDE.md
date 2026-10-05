# 新完全マスター文法 N1 — unit-by-unit processing guide

Standing instructions for turning `Shin_Kanzen_Master_N1-Bunpou.pdf` (新完全マスター文法 日本語能力試験N1, スリーエーネットワーク, 2011) into the site's grammar pages. Give a unit (e.g. "第1部 5課", "問題 1課〜8課", "第3部 7課", "模擬試験 第2回") and this is the process to follow.

This guide adapts the master spec [`book-source/n1/grammar/PROCESSING-GUIDE.md`](../PROCESSING-GUIDE.md) (written for 日本語総まとめ). Everything in the master spec still applies — page template, `bp-*` classes, the three required sections, EN + Hindi + Gujarati for every meaning/example/quiz sentence, romaji under every Japanese line, and "(added, not in book)" marking — unless this file says otherwise.

The PDF is scanned/image-only (no text layer; 199 pages, 500×712 pt). Render pages to PNG with PyMuPDF (`import pymupdf`; `page.get_pixmap(dpi=150)`) and read them visually. 110 dpi is enough for page-number checks; use 150–170 dpi (or crop half-pages) for furigana and the dense 別冊 answer grid.

---

## 1. What a unit is

A **unit** = one TOC entry that has its own heading bar in the book: one 課, one 問題 review set, one 模擬試験 回, or a group of IV 文法形式の整理 sections (see table). Read from the unit's first page until the next heading bar begins — include every page in between.

- **第1部 課** (1課–20課): a 〔復習〕 box (N2 forms to review), 3–6 numbered grammar points (each: ⇒ meaning line, ①②③ examples, 🔗 connection line with 動/イ形/ナ形/名 boxes, ⚠ usage note, sometimes a 硬い言い方 tag), then drill sets **[1]…[n]** (one per point, usually 3 items but 2–7 occur — always take the item count from the scan) and a mixed set **[1〜n]**. Drills are **3-option (a・b・c)**, not the exam's 4. 7課 and 11課 are only 2 pages long; the rest are 4.
- **第1部 問題 (1課〜N課)**: 2-page review tests, 15 items, JLPT-style 4-option (1・2・3・4) fill-in-the-blank. No grammar points.
- **第1部 IV 文法形式の整理 A–G**: summary tables that regroup forms already taught (with the 課 they came from) plus some forms taught here for the first time (marked ＊ in the book), followed by 練習1／練習2 drills (mixed formats: particle fill-ins, matching, conjugation write-ins).
- **第2部 文の組み立て 1課–3課**: 2 pages each — 1 page of rules (forms that need a following negative, forms that attach to question words / numbers, noun-modifying forms, connection traps) with cross-references to 第1部, then 12 ★ sentence-ordering items (4 blanks each; in all 36 items the ★ is the 3rd blank).
- **第3部 文章の文法 1課–12課**: 4 pages each — explanation sections (A, B, 1., 2. with 例) then 練習1, 練習2 where present (short-passage blanks, choose/conjugate/write-in) and a **まとめ** passage cloze (5 numbered blanks, 4 options).
- **模擬試験 第1回・第2回**: 4 pages each, real-exam format — 問題1 (items 1–10, fill-in), 問題2 (items 11–15, ★ ordering), 問題3 (items 16–20, passage cloze).
- **問題紹介** (front matter): 4 pages explaining the three JLPT grammar question types with 例題1–5. Worth one short page; answers are explained in the book itself.

## 2. Page-number offset — it drifts, always re-check

Verified by reading the printed page number (the oval stamp at the bottom corner) on rendered images at 20+ places. **The scan drops the blank verso after each part-title page, so the offset shrinks by 1 at each part boundary:**

| Section | Printed pages | PDF page = printed + | Checked at (PDF → printed) |
|---|---|---|---|
| Front matter (はじめに, 目次, 本書をお使いになる方へ) | i–xi (roman) | — | PDF 9 = viii, PDF 12 = xi |
| 問題紹介 (title page PDF 13) | 2–5 | **+12** | 14→2, 15→3, 16→4, 17→5 |
| 実力養成編 title page | 6 (PDF 18; p.7 blank omitted) | — | — |
| 第1部 文の文法1 (1課 … IV G) | 8–109 | **+11** | 19→8, 20→9, 35→24, 47→36, 51→40, 59→48, 67→56, 85→74, 91→80, 103→92, 105→94, 119→108, 120→109 |
| 第2部 title page | 110 (PDF 121; p.111 blank omitted) | — | — |
| 第2部 文の文法2 | 112–117 | **+10** | 122→112, 123→113, 124→114, 126→116, 127→117 |
| 第3部 title page | 118 (PDF 128; p.119 blank omitted) | — | — |
| 第3部 文章の文法 | 120–167 | **+9** | 129→120, 130→121, 131→122, 135→126, 155→146, 163→154, 171→162, 175→166, 176→167 |
| 模擬試験 title page | 168 (PDF 177; p.169 blank omitted) | — | — |
| 模擬試験 + 索引 | 170–180 | **+8** | 178→170, 179→171, 180→172, 182→174, 185→177, 186→178 |
| Colophon, series ad, covers | — | — | PDF 189–192 |
| **別冊 解答** (cover PDF 193) | 別冊 p.2–7 | 別冊 p.N = PDF **192+N** | 194→2 … 199→7 |

Before building any unit, render its first page and confirm the stamp matches this table.

## 3. Answer key — the 別冊 IS in this PDF

The separate 別冊 解答 booklet is bound in at the end (PDF 193 cover, PDF 194–199 = 別冊 p.2–7). It gives **answers only, no explanations** — every "Why" callout is our own reasoning; say so in the header ("answers confirmed from 別冊 p.X; explanations are mine").

| 別冊 page | PDF | Covers |
|---|---|---|
| p.2 | 194 | 第1部 1課–8課, 問題(1課〜4課), 問題(1課〜8課) |
| p.3 | 195 | 9課–17課, 問題(1課〜12課), 問題(1課〜16課) |
| p.4 | 196 | 18課–20課, 問題(1課〜20課), IV A–E |
| p.5 | 197 | IV F–G, 第2部 1課–3課, 第3部 1課–3課 |
| p.6 | 198 | 第3部 4課–8課 |
| p.7 | 199 | 第3部 9課–12課, 模擬試験 第1回・第2回 |

Caveats:
- **★ ordering items (第2部, 模擬試験 問題2)**: the 別冊 lists only the number of the tile that goes in the ★ slot, not the full order. Work out the full order yourself, check that it puts the official tile at ★, and flag the full order as "reasoned; ★ tile confirmed from 別冊".
- **Write-in items** (IV 練習, 第3部 練習): the 別冊 sometimes lists alternatives separated by ／ — reproduce all of them.
- **問題紹介 例題1–5**: answered and explained in the book itself (p.2–5); cite that.
- If any 別冊 cell is illegible even at 170 dpi, apply the master-guide rule: work it out at N1 level and flag transparently that it is not from the official key.

## 4. Unit table

Filenames live in `n1/grammar/shin-kanzen-master/`. Order = book order (= hub order = prev/next order).

| # | Unit id | Title | Printed pp | PDF pp | Output filename | Answers |
|---|---|---|---|---|---|---|
| 1 | 問題紹介 | 問題紹介 (例題1–5) | 2–5 | 14–17 | `mondai-shoukai.html` | in-book p.2–5 |
| 2 | 第1部 1課 | 時間関係 | 8–11 | 19–22 | `part1-lesson-01.html` ✅ built | 別冊 p.2 |
| 3 | 第1部 2課 | 範囲の始まり・限度 | 12–15 | 23–26 | `part1-lesson-02.html` | 別冊 p.2 |
| 4 | 第1部 3課 | 限定・非限定・付加 | 16–19 | 27–30 | `part1-lesson-03.html` | 別冊 p.2 |
| 5 | 第1部 4課 | 例示 | 20–23 | 31–34 | `part1-lesson-04.html` | 別冊 p.2 |
| 6 | 問題(1課〜4課) | review test | 24–25 | 35–36 | `part1-review-01-04.html` | 別冊 p.2 |
| 7 | 第1部 5課 | 関連・無関係 | 26–29 | 37–40 | `part1-lesson-05.html` | 別冊 p.2 |
| 8 | 第1部 6課 | 様子 | 30–33 | 41–44 | `part1-lesson-06.html` | 別冊 p.2 |
| 9 | 第1部 7課 | 付随行動 | 34–35 | 45–46 | `part1-lesson-07.html` | 別冊 p.2 |
| 10 | 第1部 8課 | 逆接 | 36–39 | 47–50 | `part1-lesson-08.html` | 別冊 p.2 |
| 11 | 問題(1課〜8課) | review test | 40–41 | 51–52 | `part1-review-01-08.html` | 別冊 p.2 |
| 12 | 第1部 9課 | 条件 | 42–45 | 53–56 | `part1-lesson-09.html` | 別冊 p.3 |
| 13 | 第1部 10課 | 逆接条件 | 46–49 | 57–60 | `part1-lesson-10.html` | 別冊 p.3 |
| 14 | 第1部 11課 | 目的・手段 | 50–51 | 61–62 | `part1-lesson-11.html` | 別冊 p.3 |
| 15 | 第1部 12課 | 原因・理由 | 52–55 | 63–66 | `part1-lesson-12.html` | 別冊 p.3 |
| 16 | 問題(1課〜12課) | review test | 56–57 | 67–68 | `part1-review-01-12.html` | 別冊 p.3 |
| 17 | 第1部 13課 | 可能・不可能・禁止 | 58–61 | 69–72 | `part1-lesson-13.html` | 別冊 p.3 |
| 18 | 第1部 14課 | 話題・評価の基準 | 62–65 | 73–76 | `part1-lesson-14.html` | 別冊 p.3 |
| 19 | 第1部 15課 | 比較対照 | 66–69 | 77–80 | `part1-lesson-15.html` | 別冊 p.3 |
| 20 | 第1部 16課 | 結末・最終の状態 | 70–73 | 81–84 | `part1-lesson-16.html` | 別冊 p.3 |
| 21 | 問題(1課〜16課) | review test | 74–75 | 85–86 | `part1-review-01-16.html` | 別冊 p.3 |
| 22 | 第1部 17課 | 強調 | 76–79 | 87–90 | `part1-lesson-17.html` | 別冊 p.3 |
| 23 | 第1部 18課 | 主張・断定 | 80–83 | 91–94 | `part1-lesson-18.html` | 別冊 p.4 |
| 24 | 第1部 19課 | 評価・感想 | 84–87 | 95–98 | `part1-lesson-19.html` | 別冊 p.4 |
| 25 | 第1部 20課 | 心情・強制的思い | 88–91 | 99–102 | `part1-lesson-20.html` | 別冊 p.4 |
| 26 | 問題(1課〜20課) | review test | 92–93 | 103–104 | `part1-review-01-20.html` | 別冊 p.4 |
| 27 | IV A・B | 動詞の意味に着目-1・-2 | 94–99 | 105–110 | `part1-iv-ab.html` | 別冊 p.4 |
| 28 | IV C・D | 古い言葉を使った言い方／「もの・こと・ところ」を使った言い方 | 100–103 | 111–114 | `part1-iv-cd.html` | 別冊 p.4 |
| 29 | IV E・F | 二つの言葉を組にする言い方／助詞・複合助詞 | 104–107 | 115–118 | `part1-iv-ef.html` | 別冊 p.4 (E), p.5 (F) |
| 30 | IV G | 文法的性質の整理 | 108–109 | 119–120 | `part1-iv-g.html` | 別冊 p.5 |
| 31 | 第2部 1課 | 文の組み立て-1 決まった形 | 112–113 | 122–123 | `part2-lesson-01.html` | 別冊 p.5 (★ tile only) |
| 32 | 第2部 2課 | 文の組み立て-2 名詞を説明する形式 | 114–115 | 124–125 | `part2-lesson-02.html` | 別冊 p.5 (★ tile only) |
| 33 | 第2部 3課 | 文の組み立て-3 接続に注意 | 116–117 | 126–127 | `part2-lesson-03.html` | 別冊 p.5 (★ tile only) |
| 34 | 第3部 1課 | 時制 | 120–123 | 129–132 | `part3-lesson-01.html` | 別冊 p.5 |
| 35 | 第3部 2課 | 条件を表す文 | 124–127 | 133–136 | `part3-lesson-02.html` | 別冊 p.5 |
| 36 | 第3部 3課 | 視点を動かさない手段-1 動詞の使い方、自動詞・他動詞の使い分け | 128–131 | 137–140 | `part3-lesson-03.html` | 別冊 p.5 |
| 37 | 第3部 4課 | 視点を動かさない手段-2「〜てくる・〜ていく」 | 132–135 | 141–144 | `part3-lesson-04.html` | 別冊 p.6 |
| 38 | 第3部 5課 | 視点を動かさない手段-3 受身・使役・使役受身 | 136–139 | 145–148 | `part3-lesson-05.html` | 別冊 p.6 |
| 39 | 第3部 6課 | 視点を動かさない手段-4「〜てあげる・〜てもらう・〜てくれる」 | 140–143 | 149–152 | `part3-lesson-06.html` | 別冊 p.6 |
| 40 | 第3部 7課 | 指示表現「こ・そ・あ」の使い分け | 144–147 | 153–156 | `part3-lesson-07.html` | 別冊 p.6 |
| 41 | 第3部 8課 | 「は・が」の使い分け | 148–151 | 157–160 | `part3-lesson-08.html` | 別冊 p.6 |
| 42 | 第3部 9課 | 接続表現 | 152–155 | 161–164 | `part3-lesson-09.html` | 別冊 p.7 |
| 43 | 第3部 10課 | 省略・繰り返し・言い換え | 156–159 | 165–168 | `part3-lesson-10.html` | 別冊 p.7 |
| 44 | 第3部 11課 | 文体の一貫性 | 160–163 | 169–172 | `part3-lesson-11.html` | 別冊 p.7 |
| 45 | 第3部 12課 | 話の流れを考える | 164–167 | 173–176 | `part3-lesson-12.html` | 別冊 p.7 |
| 46 | 模擬試験 第1回 | mock test 1 | 170–173 | 178–181 | `mock-test-1.html` | 別冊 p.7 (★ tile only for 11–15) |
| 47 | 模擬試験 第2回 | mock test 2 | 174–177 | 182–185 | `mock-test-2.html` | 別冊 p.7 (★ tile only for 11–15) |

Not units: 索引 (printed 178–180, PDF 186–188), title pages, colophon.

IV grouping rationale: A is 4 pages and B–G are 2 pages each; A+B share a theme (verb-derived forms), C+D are both "old/fixed word" forms, E+F are both particle/pairing forms, and G (grammatical properties, with a long 14-item 練習1) stands alone. Each grouped page keeps the book's A/B… sub-headings.

## 5. Delivery

- Build each unit at `n1/grammar/shin-kanzen-master/<filename>` using exactly the template of `n1/grammar/week-1/day-1.html` (same `<head>`, `auth.js`, `style.css` + `day-page.css`, site header/nav/footer, `main.js`). Asset paths are `../../../assets/...`; N1 home `../../index.html`; grammar hub `../../grammar.html`.
- Breadcrumb: `Home / JLPT N1 / Grammar / 新完全マスター文法 N1 (→ index.html) / <unit short name>` (e.g. `1課`, `問題 1〜4課`, `IV A・B`, `第2部 1課`, `第3部 7課`, `模擬試験 第1回`).
- `.bp-week` line: `JLPT N1 · Grammar · 新完全マスター文法 N1 — <部> · <section (I/II/III/IV)>` + romaji.
- Header block (`.bp-meta-grid`): Source (book + printed pp + PDF pp), grammar points covered, Answer key (別冊 page + PDF page, and whether ★-order/explanations are ours), Notes (register tags, exam traps, format quirks).
- `.bp-day-nav` at the bottom: **prev** = previous unit in the table, except `part1-lesson-01.html` (prev = the `index.html` hub; 問題紹介 is reached from the hub, and `mondai-shoukai.html` itself has prev = hub, next = `part1-lesson-01.html`); **next** = next unit's filename even if not built yet. The last unit's next = `index.html`.
- **Hub update rule**: after building a unit, edit `n1/grammar/shin-kanzen-master/index.html` — replace that unit's `<span class="day-chip soon">…</span>` with `<a class="day-chip ready" href="<filename>">…</a>` (keep the label), and update the "N of 47 units built" line in the `.sample-note`. Do not touch `n1/grammar.html` (it already links this hub via a `module-card`).

## 6. Adapting the three required sections

Always include all three sections; if one is empty write *(None on this page.)* with a one-line reason.

### 第1部 課 (lessons 1–20)
- **Grammar Points**: one `.bp-point` per numbered point (【1】…). Field table: Reading / Meaning EN (include the book's ⇒ line in Japanese) / HI / GU / Connection (copy the 🔗 line exactly, e.g. `動 辞書形／た形 + が早いか`) / Register (`.bp-badge.formal` only where the book prints 硬い言い方; where the book prints 書き言葉 or 話し言葉 use a plain `.bp-badge` labelled "book tag 書き言葉" / "book tag 話し言葉"; otherwise neutral, with a note if it is literary) / Typical use (translate the ⚠ note — these notes are what the drills test). Formation table per master spec, "(added, not in book)" for anything not on the 🔗 line. Examples table = every ①②③ example. Put the 〔復習〕 box at the top as a `.bp-callout` + examples table (N2 forms, translated).
- **Quiz**: every item of every drill set [1]…[n] and [1〜n], labelled `[2] Q3` etc. Options table has 3 rows (a/b/c). "Why" must reference the ⚠ rule being tested.
- **Confusion Pairs**: table across the lesson's points (+ the 〔復習〕 N2 forms where they are near-synonyms) and 1–3 `.bp-callout` exam traps.

### 第1部 問題 review sets
- Grammar Points: *(None — review test covering 1課〜N課; see those lesson pages.)* Optionally list which 課 each item tests.
- Quiz: all 15 items, 4 options (1–4), answers from the 別冊, "Why" naming the 課 of the correct form.
- Confusion Pairs: the forms the distractors pitted against each other.

### 第1部 IV 文法形式の整理
- Grammar Points: reproduce each summary table as `.bp-table`s. Forms marked ＊ (first taught here) get a full `.bp-point`; forms cross-referenced to an earlier 課 get one row (form, meaning, 課 link) instead of a full block.
- Quiz: 練習1／練習2 in whatever format the book uses (particle fill-ins, matching ①–⑤ to a–g, conjugation write-ins). For write-ins, show the full completed sentence and list every accepted answer the 別冊 gives.
- Confusion Pairs: the core of these sections — e.g. 動詞由来 forms with similar meanings, こと／もの／ところ forms.

### 第2部 文の組み立て (★ ordering)
- Grammar Points: the rule page as `.bp-point`s grouped by the book's [1][2][3] headings (e.g. 後に否定が来るもの, 疑問詞につくもの, 数字につくもの); each form with its example sentence, translations and the cross-referenced 課.
- Quiz: all 12 ★ items. For each: the sentence with four blanks and the ★ position, tiles 1–4 with romaji, `.bp-order-chain` (full order), `.bp-assembled` sentence, translations, and which tile is at ★. This book **does** use the official ★ format. Flag: "★ tile confirmed from 別冊; full order reasoned".
- Confusion Pairs: forms whose collocation rules are easy to mix (e.g. 〜たりとも + 1+counter vs 〜からある + large number).

### 第3部 文章の文法 (passage grammar)
- Grammar Points: one `.bp-point` per explanation section (A, B, 1., 2. …) — the rule, every 例 sentence translated, and notes. Formation tables only where the section is about a form (e.g. 受身・使役); otherwise skip the formation table and say why.
- Quiz: 練習1, 練習2 (where present — 2課 and 3課 have no 練習2; 練習1 is often several short passages of 2-choice items) and まとめ. **Do not reproduce book passages** (a full-passage page was blocked by the API's content filter). For each passage give a summary card labelled "Passage summary (not the book's text)" in EN/HI/GU in our own words, then one `.bp-quiz` per blank that quotes only the sentence containing the blank, with its translations, an options table and a "Why" that refers to the context (viewpoint, tense consistency, こ・そ・あ reference…). Write-in blanks: show the accepted form(s). Do not transcribe passages into scratch notes either. Reference: `part3-lesson-02.html`.
- Confusion Pairs: the pairs the section contrasts (自動詞/他動詞, てくる/ていく, は/が, こ/そ/あ, だ・である vs です・ます).

### 模擬試験
- Grammar Points: a short table of the pattern each item tests (meaning, connection, and the 課 that teaches it — link the lesson page). Mark N2 forms or set phrases the book never teaches as a numbered point "not a numbered point". Reference: `mock-test-1.html`.
- Quiz: 問題1 (1–10), 問題2 (11–15 ★, as in 第2部), 問題3 (16–20 passage cloze, as in 第3部), with the time/score info if printed. Answers from 別冊 p.7.
- Confusion Pairs: the traps across the whole test, cross-linked to the relevant lesson pages.

### 問題紹介
- Grammar Points: the three question types (文法形式の判断／文の組み立て／文章の文法) and the book's solving advice.
- Quiz: 例題1–5 with the book's own explained answers.
- Confusion Pairs: the forms in 例題1 (が最後／が早いか／ものなら／とたんに).

## 7. Language rules (unchanged from master)

Intermediate learner, Hindi and Gujarati native speakers: every meaning, example, quiz sentence and option gets EN + HI + GU; romaji (`<span class="romaji">`) under every Japanese line, including formation examples, options and tiles; concise English explanations.

---

**Reference implementation:** [`n1/grammar/shin-kanzen-master/part1-lesson-01.html`](../../../../n1/grammar/shin-kanzen-master/part1-lesson-01.html) (第1部 1課 時間関係) is the first unit built under this guide — copy its structure, tone and depth for every later 第1部 lesson.
