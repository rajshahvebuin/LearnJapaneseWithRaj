# ドリル&ドリル N1 文字・語彙 — round-by-round processing guide

Standing instructions for turning `Drill_&_Drill_N1-Moji_Goi.pdf` (ドリル&ドリル 日本語能力試験 N1 文字・語彙, 星野恵子 + 辻和子, UNICOM Inc.) into the site's vocabulary pages. Give a section + round (e.g. "文脈規定 第7回") and this is the process to follow.

This guide adapts the vocabulary spec [`../PROCESSING-GUIDE.md`](../PROCESSING-GUIDE.md) (日本語総まとめ N1 語彙) and follows the sister book's guide [`../../grammar/Drill_&_Drill_N1-Bunpou/PROCESSING-GUIDE.md`](../../grammar/Drill_&_Drill_N1-Bunpou/PROCESSING-GUIDE.md) (same series, same 別冊 layout). Site chrome, CSS classes, the three required sections, language rules and romaji all still apply **except** where this file says otherwise.

**The PDF (178 pages) has a text layer, but it is poor OCR** (furigana mixed into the line, small kanji misread, digits read as l/I/o/H, columns run together). Use it only to *find* things (e.g. `【n】` / `正解` / `第N回` positions). **Always read questions, options and answers from rendered images**: PyMuPDF (`import pymupdf`; `doc[i-1].get_pixmap(dpi=…)`). Question pages: 110–130 dpi is enough. 別冊 pages are two dense columns — render each column separately (clip `x 0–0.5` and `x 0.42–0.92` of the page width, top/bottom halves) at 140 dpi. Very large single images are rejected by the image reader; keep each image under ~1300 px on its long side.

**Previous-owner marks.** This scan is of a used copy: on the question pages answers are circled / crossed out by hand (e.g. 漢字読み Q1 has 3 circled and 4 crossed), and a few Vietnamese pencil notes appear in the 別冊. Ignore all handwriting — the answer is always the printed 別冊 正解. The `facebook.com/…` banner at the top of every page is a scanner watermark, not book content.

---

## 1. What this book is

- A **pure drill book**: no vocabulary-explanation pages. 前書き (printed pp.2–4, PDF 2–4) lists the book's make-up and gives short study tips for each of the four question types (p.3 漢字読み, p.3–4 文脈規定, p.4 言い換え類義, p.4 用法). Summarise the relevant tip block in our own words on the **first round of each section** (the reference unit `kanji-01.html` does this for 漢字読み). PDF 5–10 = the same preface in English / Chinese / Korean — not needed.
- Every round has a 日付/得点 (date/score) grid at the top (`/6` or `/7` per attempt) — just a self-scoring box, not content. There is no 合格ライン line in this book.
- The 【別冊】正解・解説 **is included at the end of the same PDF** (PDF 86–178). The answer key is **official** for every unit except the gaps listed in §3 — never guess where the key exists; cite it as "別冊 p.N (PDF M)".

### What the 別冊 gives, per section

| Section | 別冊 entry contents |
|---|---|
| 漢字読み | 正解 n; the word + reading 「…」 + EN/CN/KR gloss; the question sentence again + EN/CN/KR translation; a **漢字** block for each kanji of the word (on-/kun-readings ①②③, each with words, EN gloss, and often a 例:「…」 sentence + translation); sometimes **選択肢の言葉** = the wrong options that are real words, with their kanji (e.g. 2「遡って」(遡る)). |
| 文脈規定 | 正解 n; the word + EN/CN/KR gloss; the completed sentence + translations; a ✎ 例 sentence; **選択肢の言葉** = each wrong option with a short Japanese definition (= …) and a 例:「…」 sentence. |
| 言い換え類義 | 正解 n + the correct paraphrase; the underlined word「…」= its Japanese definition + gloss; completed sentence + translations; ✎ 例; **選択肢の言葉** with definitions + examples. |
| 用法 | 正解 n; the word = definition + gloss; the correct sentence + translations; **使い方** (extra correct example); **正しい例文** = the wrong option sentences *rewritten correctly* (the replacement word is underlined, e.g. 2「…通学の乗客でいっぱいだ」). |

The 別冊 does explain wrong options (選択肢の言葉 / 正しい例文) — use it in each `.bp-why`; anything beyond it is ours and labelled "(added, not in book)". Don't reproduce the Chinese/Korean translations; write our own EN (do not copy the book's English verbatim) + HI + GU.

### Unit = one 回 (round)

| Section | Rounds | Qs per round | Pages per round | Numbering |
|---|---|---|---|---|
| 漢字読み (kanji reading, underlined word → choose reading) | 20 | 6 | 1 printed page | continuous 【1】–【120】 |
| 文脈規定 (contextually defined, fill the （　）) | 20 | 7 | 1 printed page | restarts 【1】–【140】 |
| 言い換え類義 (paraphrase, closest meaning to underlined word) | 10 | 6 | 1 printed page | restarts 【1】–【60】 |
| 用法 (usage, which of 4 sentences uses the word correctly) | 10 | 6 (3 per page) | 2 printed pages | restarts 【1】–【60】 |

**60 units total.** Section dividers: printed p.13 (PDF 13) = 文字 / 漢字読み 第1回–第20回; printed p.35 (PDF 35) = 語彙 divider; PDF 34 is blank; PDF 12 is blank.

---

## 2. Verified page offsets

Checked by reading the printed page number stamped on the rendered images (TOC = PDF 11, printed p.11):

**Main book**
- **PDF = printed** for printed pp.2–71 (checked PDF 2→2, 3→3, 11→11, 14→14, 36→36, 38→38, 40→40, 56→56, 66→66, 70→70, 71→71).
- **Two spreads of 用法 are missing from the scan:** printed pp.72–73 (用法 第4回, Q19–24) and pp.76–77 (用法 第6回, Q31–36). So PDF 72 = p.74, PDF 73 = p.75 (offset −2); PDF 74 = p.78 … PDF 81 = p.85 (offset −4). PDF 82 = blank, PDF 83 = 著者紹介 (colophon), PDF 84 = blank, PDF 85 = 別冊 cover.

**別冊 (answer booklet, restarts at p.1)**
- PDF 86 = 別冊 p.2 … PDF 91 = p.7 (**別冊 = PDF − 84**).
- **別冊 pp.8–9 are missing from the scan.** PDF 92 = p.10 onward: **別冊 = PDF − 82** (checked PDF 92→10, 104→22, 118→36, 120→38, 155→73, 167→85, 176→94, 178→96 = last page).
- 別冊 TOC: 漢字読み p.2 (PDF 86), 文脈規定 p.38 (PDF 120), 言い換え類義 p.73 (PDF 155), 用法 p.85 (PDF 167).

---

## 3. Answer-key status / gaps

- **漢字読み Q21–26 and the start of Q27** (on the missing 別冊 pp.8–9): no 正解 in the scan. PDF 91 ends with Q20 complete; PDF 92 (別冊 10) opens in the middle of Q27's 漢字 block (無 readings), then Q28. For those questions, work the answer out at N1 level and flag it in the header and in each `.bp-why`: "answer worked out — 別冊 pp.8–9 are missing from the scan; not from the official key". For Q27, the surviving 漢字 block (PDF 92) usually confirms the answer — say so.
- **用法 第4回 (Q19–24) and 第6回 (Q31–36)**: the *question pages* are missing, but the 別冊 entries survive (PDF 170–172, 173–174). The 別冊 gives the correct sentence and the **正しい例文** (the three wrong sentences rewritten, with the substituted word underlined), so the original options can only be partly reconstructed. Build these units from the 別冊: show the correct sentence as the answer, list the 正しい例文 as "the book's corrected versions of the wrong options", and state clearly in the header that the original question page is missing from the scan (never invent the original wrong sentences).
- Everything else: official key present.

---

## 4. Unit table

"Key PDF" = the PDF range in the 別冊 holding that round's entries (from the page with the round's first 【n】 to the page with its last). A round's entries often start mid-column — read from the 第N回 box to the next 第N+1回 box. Ranges were located from 【n】/第N回 positions and spot-checked on images; if a range is off by a page, fix it here when you build the unit.

### 漢字読み (Q【1】–【120】, 6 per round)

| File | Title | Qs | Printed p | PDF p | Key PDF (別冊 pp) |
|---|---|---|---|---|---|
| kanji-01.html | 漢字読み 第1回 | 1–6 | 14 | 14 | 86–87 (2–3) |
| kanji-02.html | 漢字読み 第2回 | 7–12 | 15 | 15 | 88–90 (4–6) |
| kanji-03.html | 漢字読み 第3回 | 13–18 | 16 | 16 | 90–91 (6–7) |
| kanji-04.html | 漢字読み 第4回 | 19–24 | 17 | 17 | 91 (7) — Q21–24 key missing (別冊 8–9) |
| kanji-05.html | 漢字読み 第5回 | 25–30 | 18 | 18 | 92–93 (10–11) — Q25–26 key missing, Q27 partial |
| kanji-06.html | 漢字読み 第6回 | 31–36 | 19 | 19 | 93–95 (11–13) |
| kanji-07.html | 漢字読み 第7回 | 37–42 | 20 | 20 | 95–96 (13–14) |
| kanji-08.html | 漢字読み 第8回 | 43–48 | 21 | 21 | 96–98 (14–16) |
| kanji-09.html | 漢字読み 第9回 | 49–54 | 22 | 22 | 98–99 (16–17) |
| kanji-10.html | 漢字読み 第10回 | 55–60 | 23 | 23 | 99–101 (17–19) |
| kanji-11.html | 漢字読み 第11回 | 61–66 | 24 | 24 | 101–103 (19–21) |
| kanji-12.html | 漢字読み 第12回 | 67–72 | 25 | 25 | 103–105 (21–23) |
| kanji-13.html | 漢字読み 第13回 | 73–78 | 26 | 26 | 105–106 (23–24) |
| kanji-14.html | 漢字読み 第14回 | 79–84 | 27 | 27 | 106–108 (24–26) |
| kanji-15.html | 漢字読み 第15回 | 85–90 | 28 | 28 | 108–110 (26–28) |
| kanji-16.html | 漢字読み 第16回 | 91–96 | 29 | 29 | 110–112 (28–30) |
| kanji-17.html | 漢字読み 第17回 | 97–102 | 30 | 30 | 112–114 (30–32) |
| kanji-18.html | 漢字読み 第18回 | 103–108 | 31 | 31 | 114–115 (32–33) |
| kanji-19.html | 漢字読み 第19回 | 109–114 | 32 | 32 | 116–117 (34–35) |
| kanji-20.html | 漢字読み 第20回 | 115–120 | 33 | 33 | 117–119 (35–37) |

### 文脈規定 (Q【1】–【140】, 7 per round)

| File | Title | Qs | Printed p | PDF p | Key PDF (別冊 pp) |
|---|---|---|---|---|---|
| bunmyaku-01.html | 文脈規定 第1回 | 1–7 | 36 | 36 | 120–121 (38–39) |
| bunmyaku-02.html | 文脈規定 第2回 | 8–14 | 37 | 37 | 121–122 (39–40) |
| bunmyaku-03.html | 文脈規定 第3回 | 15–21 | 38 | 38 | 122–124 (40–42) |
| bunmyaku-04.html | 文脈規定 第4回 | 22–28 | 39 | 39 | 124–126 (42–44) |
| bunmyaku-05.html | 文脈規定 第5回 | 29–35 | 40 | 40 | 126–127 (44–45) |
| bunmyaku-06.html | 文脈規定 第6回 | 36–42 | 41 | 41 | 127–129 (45–47) |
| bunmyaku-07.html | 文脈規定 第7回 | 43–49 | 42 | 42 | 129–130 (47–48) |
| bunmyaku-08.html | 文脈規定 第8回 | 50–56 | 43 | 43 | 131–132 (49–50) |
| bunmyaku-09.html | 文脈規定 第9回 | 57–63 | 44 | 44 | 132–134 (50–52) |
| bunmyaku-10.html | 文脈規定 第10回 | 64–70 | 45 | 45 | 134–136 (52–54) |
| bunmyaku-11.html | 文脈規定 第11回 | 71–77 | 46 | 46 | 136–137 (54–55) |
| bunmyaku-12.html | 文脈規定 第12回 | 78–84 | 47 | 47 | 137–139 (55–57) |
| bunmyaku-13.html | 文脈規定 第13回 | 85–91 | 48 | 48 | 139–141 (57–59) |
| bunmyaku-14.html | 文脈規定 第14回 | 92–98 | 49 | 49 | 141–143 (59–61) |
| bunmyaku-15.html | 文脈規定 第15回 | 99–105 | 50 | 50 | 143–145 (61–63) |
| bunmyaku-16.html | 文脈規定 第16回 | 106–112 | 51 | 51 | 145–147 (63–65) |
| bunmyaku-17.html | 文脈規定 第17回 | 113–119 | 52 | 52 | 147–149 (65–67) |
| bunmyaku-18.html | 文脈規定 第18回 | 120–126 | 53 | 53 | 149–151 (67–69) |
| bunmyaku-19.html | 文脈規定 第19回 | 127–133 | 54 | 54 | 151–153 (69–71) |
| bunmyaku-20.html | 文脈規定 第20回 | 134–140 | 55 | 55 | 153–154 (71–72) |

### 言い換え類義 (Q【1】–【60】, 6 per round)

| File | Title | Qs | Printed p | PDF p | Key PDF (別冊 pp) |
|---|---|---|---|---|---|
| iikae-01.html | 言い換え類義 第1回 | 1–6 | 56 | 56 | 155–156 (73–74) |
| iikae-02.html | 言い換え類義 第2回 | 7–12 | 57 | 57 | 156–157 (74–75) |
| iikae-03.html | 言い換え類義 第3回 | 13–18 | 58 | 58 | 157–158 (75–76) |
| iikae-04.html | 言い換え類義 第4回 | 19–24 | 59 | 59 | 158–159 (76–77) |
| iikae-05.html | 言い換え類義 第5回 | 25–30 | 60 | 60 | 159–160 (77–78) |
| iikae-06.html | 言い換え類義 第6回 | 31–36 | 61 | 61 | 160–161 (78–79) |
| iikae-07.html | 言い換え類義 第7回 | 37–42 | 62 | 62 | 161–162 (79–80) |
| iikae-08.html | 言い換え類義 第8回 | 43–48 | 63 | 63 | 162–163 (80–81) |
| iikae-09.html | 言い換え類義 第9回 | 49–54 | 64 | 64 | 163–165 (81–83) |
| iikae-10.html | 言い換え類義 第10回 | 55–60 | 65 | 65 | 165–166 (83–84) |

### 用法 (Q【1】–【60】, 6 per round, 3 per page)

| File | Title | Qs | Printed pp | PDF pp | Key PDF (別冊 pp) |
|---|---|---|---|---|---|
| youhou-01.html | 用法 第1回 | 1–6 | 66–67 | 66–67 | 167–168 (85–86) |
| youhou-02.html | 用法 第2回 | 7–12 | 68–69 | 68–69 | 168–169 (86–87) |
| youhou-03.html | 用法 第3回 | 13–18 | 70–71 | 70–71 | 169–170 (87–88) |
| youhou-04.html | 用法 第4回 | 19–24 | 72–73 | **missing from scan** | 170–172 (88–90) |
| youhou-05.html | 用法 第5回 | 25–30 | 74–75 | 72–73 | 172–173 (90–91) |
| youhou-06.html | 用法 第6回 | 31–36 | 76–77 | **missing from scan** | 173–174 (91–92) |
| youhou-07.html | 用法 第7回 | 37–42 | 78–79 | 74–75 | 174–175 (92–93) |
| youhou-08.html | 用法 第8回 | 43–48 | 80–81 | 76–77 | 175–176 (93–94) |
| youhou-09.html | 用法 第9回 | 49–54 | 82–83 | 78–79 | 176–177 (94–95) |
| youhou-10.html | 用法 第10回 | 55–60 | 84–85 | 80–81 | 177–178 (95–96) |

---

## 5. Delivery

- Pages live in `n1/vocabulary/drill-and-drill/` (depth 3: assets `../../../assets/...`, N1 home `../../../n1/index.html`, vocabulary hub `../../../n1/vocabulary.html`, book hub `index.html`).
- File names as in §4 (two-digit, zero-padded): `kanji-01…20`, `bunmyaku-01…20`, `iikae-01…10`, `youhou-01…10`.
- Copy the chrome exactly from the reference unit `n1/vocabulary/drill-and-drill/kanji-01.html` (`auth.js` first in `<head>`, favicon, Noto Sans JP, `style.css` + `day-page.css`, `body.level-page.n1`, header/nav, footer, `main.js`).
- Breadcrumb: Home / JLPT N1 / Vocabulary (`../../../n1/vocabulary.html`) / ドリル&ドリル N1 文字・語彙 (`index.html`) / <unit title>.
- `.bp-day-nav`: prev = previous unit (first unit → hub `index.html`); next = next unit in book order (kanji-20 → bunmyaku-01, bunmyaku-20 → iikae-01, iikae-10 → youhou-01; youhou-10 → hub). Label e.g. `Next: 漢字読み 第2回 (Q7–12) →`.
- Reuse existing classes only: `.bp-header`, `.bp-meta-grid`, `.bp-points`, `.bp-note(s)`, `.bp-section-title`, `.bp-point`, `.bp-table`, `.kd-kanji-table` (kanji blocks), `.vd-wordlist` / `.vd-table-wrap` (word lists), `.bp-quiz`, `.bp-options` (+ `tr.correct`), `.bp-why`, `.bp-confusion`, `.bp-callout`, `.bp-day-nav`. No new CSS.

### Hub update rule

`n1/vocabulary/drill-and-drill/index.html` has four `.week-block`s (漢字読み / 文脈規定 / 言い換え類義 / 用法), one chip per round. Unbuilt: `<span class="day-chip soon" data-href="kanji-02.html">第2回</span>`. When a unit is built, flip it to `<a class="day-chip ready" href="kanji-02.html">第2回</a>` and update the `.sample-note` text `In progress — N of 60 units built` (keep that exact wording; the sync script reads it). Don't touch `n1/vocabulary.html`.

---

## 6. Header block (every unit)

`.bp-header`: `bp-week` = "JLPT N1 · Vocabulary · ドリル&ドリル N1 文字・語彙 — <section>"; `h1` = "<section> 第N回" + romaji/English gloss. Meta grid:
- **Source**: printed p (PDF p) of the questions, plus 前書き p.3/4 if the tips are summarised.
- **Pattern**: chips — JLPT question type, item count, the words tested.
- **Answer key**: "Official — 【別冊】正解・解説 p.X–Y (PDF A–B)", then the key in one line, e.g. `(1)3 (2)1 (3)3 …`. Flag any worked-out answer (§3).
- **Notes**: drill-only book, so the word/kanji tables are built from the 別冊 entries; anything else is "(added, not in book)"; mention previous-owner pen marks are ignored.

## 7. The three required sections, per question type

### 7a. 漢字読み (6 Qs) — reference: `kanji-01.html`
1. **Points** — (round 1 only) the 前書き p.3 漢字読み tips summarised in our own words (6 trap types: long/short vowels, 清音/濁音, 促音, 半濁音, kanji with many readings, irregular readings) with a `.bp-table` of the book's examples. Then a `.kd-kanji-table` built from the 別冊 **漢字** blocks for every kanji of the tested words: Kanji / Reading(s) / Word / EN / HI / GU. Keep the 別冊's words; you may trim very long lists to the most useful 4–6 per reading, but never add words without "(added)". Include the 別冊 例 sentences as rows (our own translation).
2. **Every question** — `q-jp` with `<u>` on the tested word + romaji; "Underlined word" line + EN/HI/GU of the sentence; options table Option / Reading / English / Hindi / Gujarati (real-word distractors get their meaning from the 別冊 選択肢の言葉 with kanji; non-words = "not a word / not the reading of X"); `tr.correct` on the 別冊 正解; `.bp-why` = rule from the 別冊 漢字 block + why each distractor fails.
3. **Confusion pairs** — reading traps from the round's options (e.g. 出納 すいとう vs しゅつのう; 逆様 さかさま vs ぎゃく〜) + a `.bp-callout` exam trap.

### 7b. 文脈規定 (7 Qs)
1. **Points** — (round 1) 前書き p.3–4 tips summary; then a `.vd-wordlist` of the 7 correct words: Japanese / EN / HI / GU / Note (the 別冊 ✎ 例 sentence). 2. **Every question** — like the pattern-betsu `moji-bunmyaku-doushi-1.html`: blank `（　）` sentence + romaji, full sentence + EN/HI/GU, options table, `.bp-why` citing the 別冊 選択肢の言葉 definitions. 3. **Confusion pairs** — from the four options of each question (same kanji / similar meaning / similar sound).

### 7c. 言い換え類義 (6 Qs)
1. **Points** — (round 1) p.4 tips summary; `.vd-wordlist` of the 6 underlined words with their 別冊 Japanese definition (= …) and the correct paraphrase in the Note column. 2. **Every question** — underlined sentence, options (= paraphrases), `.bp-why` showing 下線語 = 正解 via the 別冊 definition. 3. **Confusion pairs** — the underlined word vs the near-miss options.

### 7d. 用法 (6 Qs)
1. **Points** — (round 1) p.4 tips summary; `.vd-wordlist` of the 6 headwords with the 別冊 definition + 使い方 example. 2. **Every question** — the headword, then a `.bp-options` table where each row is one whole sentence (JP + romaji / EN / HI / GU); `tr.correct` on the 正解; `.bp-why` gives, for each wrong sentence, the 別冊 正しい例文 (the word that should have been used). 3. **Confusion pairs** — headword vs the words the 正しい例文 substitute (e.g. 接客 vs 乗客 vs 来客 vs 顧客).

## 8. Language & content rules
- EN + Hindi + Gujarati for every meaning, example and question sentence; `<span class="romaji">` under every Japanese line (questions, options, table words, examples).
- No passages in this book, so the passage/transcript rule only means: don't paste long runs of the 別冊's text — paraphrase its explanations.
- Never invent questions or answers. Missing pages are stated as missing (§3).

## 9. Checks before finishing a unit
- Every 正解 re-read on the 別冊 image (the OCR digits are unreliable).
- Tags balanced (Python `html.parser`), relative links resolve, file ends with `</html>`.
- Hub chip flipped + `In progress — N of 60 units built` updated.

---

**Reference implementation:** [`n1/vocabulary/drill-and-drill/kanji-01.html`](../../../../n1/vocabulary/drill-and-drill/kanji-01.html) (漢字読み 第1回).
