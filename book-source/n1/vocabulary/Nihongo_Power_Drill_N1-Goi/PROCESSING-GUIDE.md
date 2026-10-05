# 日本語パワードリル N1 文字・語彙 — unit-by-unit processing guide

Standing instructions for turning `Nihongo_Power_Drill_N1-Goi.pdf` (日本語パワードリル N1 文字・語彙, Nihongo Power Drill N1 Moji・Goi, アスク出版, 2010) into the site's vocabulary pages. Give a unit (e.g. "第7回" or "集中トレーニング③") and this is the process to follow.

This guide adapts the vocabulary master spec [`../PROCESSING-GUIDE.md`](../PROCESSING-GUIDE.md) and borrows the round layout of the sister book's guide [`../../grammar/Nihongo_Power_Drill_N1-Bunpou/PROCESSING-GUIDE.md`](../../grammar/Nihongo_Power_Drill_N1-Bunpou/PROCESSING-GUIDE.md). Everything in the master spec still applies (shared header/nav/footer, `day-page.css` `bp-*` / `vd-*` classes, three required sections, EN + Hindi + Gujarati, romaji under every Japanese line) unless overridden below.

---

## 1. The PDF

- **88 PDF pages.** There is a text layer, but it is **garbage OCR** (mis-encoded Shift-JIS fragments) — do not extract text from it. Render with PyMuPDF (`import pymupdf`; `page.get_pixmap(dpi=130–150)`, crop with `clip=` and 250 dpi for small furigana) and read visually.
- **No rotation quirk here.** Unlike the 文法 book, every page has `/Rotate 0` and renders upright; montages with `show_pdf_page()` are fine too.
- **Previous owner's handwriting.** Many pages (especially p.8–30) have pencil/pen circles on options, Vietnamese glosses, crossed-out options and furigana written in. **Ignore all handwriting** — read only the printed text, and take answers only from the 別冊. (Example: p.9 問題3 Q3 has option 2 後追い struck through by hand and both 3 and 4 circled; the printed options are 後先・後追い・後出し・後回し, the key says 4.)
- Layout: PDF 1 cover · PDF 2 inside cover (blank) · PDF 3 はじめに (p.3) · PDF 4–5 目次 (p.4–5) · PDF 6–7 学習スケジュール表 (p.6–7) · PDF 8–79 drills (p.8–79) · PDF 80 colophon · **PDF 81–88 別冊 解答 (answer booklet p.1–8).**

### Verified page offset — PDF page = printed page, throughout

| Printed pages | PDF page index | Checked at (stamped page number on the image) |
|---|---|---|
| p.3 – p.79 | **PDF = printed** (offset 0, no drift) | PDF 3 = はじめに (TOC p.3); PDF 8 stamp "8" (第1回); PDF 9 stamp "9"; PDF 44 stamp "44" (第16回); PDF 66 stamp "66" (集中⑨); PDF 79 stamp "79" (集中⑫) |
| 別冊 p.1 – p.8 | **PDF = 別冊 page + 80** | PDF 81 stamp "1"; PDF 88 stamp "8" |

No content pages are missing.

### Damaged spot — p.69 / p.70 (第26回 / 第27回)

A torn corner of p.70 lies on top of the bottom-right of p.69 in the scan:
- **p.69 (第26回) 問題4 Q2 option 4** is clipped at the right: 「先生にお手上げされたら、どうしていいのかわからな…」 — the ending (〜い) is obvious; reconstruct it and note "(end of line hidden by a torn scrap in the scan)".
- **p.70 (第27回) 問題2 Q5** is missing its top-left corner: on PDF 70 you can read 「…しますので、このベッドにうつ伏せになって寝てください。 … 下にして / 2 背中を下にして / …にして / 4 体を左向きにして」; the torn scrap visible on PDF 69 (rotated) supplies 「検査を、」「1 お腹を、」「3 体を右向きに」. Full item: 「検査をしますので、このベッドにうつ伏せになって寝てください。 1 お腹を下にして 2 背中を下にして 3 体を右向きにして 4 体を左向きにして」. Build it and say it was pieced together from the scrap.

### Answer key — 別冊 解答 present for 第1–30回 only

PDF 81–88 = 別冊 p.1–8, covering the 30 rounds in order. Each entry is headed with its printed range (e.g. 「第1回 (p.8–p.9)」) — use that heading to confirm you're on the right unit.

- It gives 問題1–4 answer numbers, plus two kinds of hint lines (`▶▶`), explained in the 「解答のヒント」 box at the top of PDF 81:
  - **⊂⊃ (chain icon)** = 慣用句や結びつきの強い表現 — a set phrase/collocation to memorise as a chunk (e.g. 第3回 問題3 Q6 ⊂⊃ 手当たり次第). Use it in the Why line and add the phrase to §1 / §3.
  - **→** = for 問題4, the word that would fit each *wrong* sentence instead of the underlined word (e.g. 第1回 問題4 Q1: 1→発達 2→発生 4→出発). These are "一例" (one possibility). Always show them in the Why line, credited "(別冊)".
- Answer-booklet page contents (verified): PDF 81 = 第1–3回 · PDF 82 = 第4–7回 · PDF 83 = 第8–11回 · PDF 84 = 第12–15回 · PDF 85 = 第16–19回 · PDF 86 = 第20–23回 · PDF 87 = 第24–27回 · PDF 88 = 第28–30回 (ends the booklet; library stamp in the blank space).
- **集中トレーニング①–⑫ have NO answers in the scanned 別冊** — the booklet ends after 第30回 at its p.8, and no 集中 entries appear anywhere in PDF 81–88. For those 12 units, work the a/b answers out at N1 level and label every one "**Answer worked out for this site — not from the book's answer key**" (header note + each Why line). Do **not** use the previous owner's circles as a source.

---

## 2. Unit definition

A **unit** is one heading in the TOC: a round (第N回) or one 集中トレーニング page. **42 units total** (30 rounds + 12 focused-training pages).

- **第1回 – 第30回**: 2 printed pages, 目標解答時間 10分, 20 points, **18 questions** in the official N1 文字・語彙 format:
  - 問題1 漢字読み — reading of the underlined kanji word ×5 (1点×5)
  - 問題2 言い換え類義 — closest meaning to the underlined word ×5 (1点×5)
  - 問題3 文脈規定 — word that fits （　） ×6 (1点×6)
  - 問題4 用法 — which sentence uses the word correctly ×2 (2点×2)
  - (Layout: p.even = 問題1 + 問題2, p.odd = 問題3 + 問題4.)
- **集中トレーニング①–⑫**: 1 printed page, 3分, 10 points: 10 sentences, each with a two-way choice `（ a ○○  b ○○ ）` — 「（　）の中のaとbのうち、文に合うほうを選びましょう」. Themes: ①② 動詞, ③④ 慣用句, ⑤⑥ カタカナ語, ⑦⑧⑨ 擬音語・擬態語, ⑩ パソコン関係のことば, ⑪ 大学生活で使うことば, ⑫ ビジネスで使うことば.

### Full unit table

| # | File | Unit | Topic | Printed pp | PDF pp | Answer PDF p |
|---|---|---|---|---|---|---|
| 1 | kai-01.html | 第1回 | — | 8–9 | 8–9 | 81 |
| 2 | kai-02.html | 第2回 | — | 10–11 | 10–11 | 81 |
| 3 | kai-03.html | 第3回 | — | 12–13 | 12–13 | 81 |
| 4 | kai-04.html | 第4回 | — | 14–15 | 14–15 | 82 |
| 5 | kai-05.html | 第5回 | — | 16–17 | 16–17 | 82 |
| 6 | training-01.html | 集中トレーニング① | 動詞 (1) | 18 | 18 | none (worked out) |
| 7 | training-02.html | 集中トレーニング② | 動詞 (2) | 19 | 19 | none (worked out) |
| 8 | kai-06.html | 第6回 | — | 20–21 | 20–21 | 82 |
| 9 | kai-07.html | 第7回 | — | 22–23 | 22–23 | 82 |
| 10 | kai-08.html | 第8回 | — | 24–25 | 24–25 | 83 |
| 11 | kai-09.html | 第9回 | — | 26–27 | 26–27 | 83 |
| 12 | kai-10.html | 第10回 | — | 28–29 | 28–29 | 83 |
| 13 | training-03.html | 集中トレーニング③ | 慣用句 (1) | 30 | 30 | none (worked out) |
| 14 | training-04.html | 集中トレーニング④ | 慣用句 (2) | 31 | 31 | none (worked out) |
| 15 | kai-11.html | 第11回 | — | 32–33 | 32–33 | 83 |
| 16 | kai-12.html | 第12回 | — | 34–35 | 34–35 | 84 |
| 17 | kai-13.html | 第13回 | — | 36–37 | 36–37 | 84 |
| 18 | kai-14.html | 第14回 | — | 38–39 | 38–39 | 84 |
| 19 | kai-15.html | 第15回 | — | 40–41 | 40–41 | 84 |
| 20 | training-05.html | 集中トレーニング⑤ | カタカナ語 (1) | 42 | 42 | none (worked out) |
| 21 | training-06.html | 集中トレーニング⑥ | カタカナ語 (2) | 43 | 43 | none (worked out) |
| 22 | kai-16.html | 第16回 | — | 44–45 | 44–45 | 85 |
| 23 | kai-17.html | 第17回 | — | 46–47 | 46–47 | 85 |
| 24 | kai-18.html | 第18回 | — | 48–49 | 48–49 | 85 |
| 25 | kai-19.html | 第19回 | — | 50–51 | 50–51 | 85 |
| 26 | kai-20.html | 第20回 | — | 52–53 | 52–53 | 86 |
| 27 | training-07.html | 集中トレーニング⑦ | 擬音語・擬態語 (1) | 54 | 54 | none (worked out) |
| 28 | training-08.html | 集中トレーニング⑧ | 擬音語・擬態語 (2) | 55 | 55 | none (worked out) |
| 29 | kai-21.html | 第21回 | — | 56–57 | 56–57 | 86 |
| 30 | kai-22.html | 第22回 | — | 58–59 | 58–59 | 86 |
| 31 | kai-23.html | 第23回 | — | 60–61 | 60–61 | 86 |
| 32 | kai-24.html | 第24回 | — | 62–63 | 62–63 | 87 |
| 33 | kai-25.html | 第25回 | — | 64–65 | 64–65 | 87 |
| 34 | training-09.html | 集中トレーニング⑨ | 擬音語・擬態語 (3) | 66 | 66 | none (worked out) |
| 35 | training-10.html | 集中トレーニング⑩ | パソコン関係のことば | 67 | 67 | none (worked out) |
| 36 | kai-26.html | 第26回 | — | 68–69 | 68–69 (p.69 問題4 Q2 opt 4 clipped) | 87 |
| 37 | kai-27.html | 第27回 | — | 70–71 | 70–71 (p.70 問題2 Q5 torn, rebuilt from scrap) | 87 |
| 38 | kai-28.html | 第28回 | — | 72–73 | 72–73 | 88 |
| 39 | kai-29.html | 第29回 | — | 74–75 | 74–75 | 88 |
| 40 | kai-30.html | 第30回 | — | 76–77 | 76–77 | 88 |
| 41 | training-11.html | 集中トレーニング⑪ | 大学生活で使うことば | 78 | 78 | none (worked out) |
| 42 | training-12.html | 集中トレーニング⑫ | ビジネスで使うことば | 79 | 79 | none (worked out) |

Always re-verify a unit's start page by reading the stamped page number and the 第N回 / 集中トレーニング heading on the rendered image before building.

---

## 3. Delivery

- Files live in `n1/vocabulary/power-drill/` (`kai-01.html` … `kai-30.html`, `training-01.html` … `training-12.html`). Page depth is three levels: assets `../../../assets/...`, site home `../../../index.html`, N1 home `../../index.html`, vocabulary hub `../../vocabulary.html`, book hub `index.html`.
- Same `<head>` as the reference (`auth.js` first, favicon, Noto Sans JP, `style.css` + `day-page.css`), same site header/nav/footer, `main.js` at the end.
- `<title>`: `N1 Vocabulary · パワードリル 第N回` (or `… 集中トレーニング①`).
- Breadcrumb: `Home / JLPT N1 / Vocabulary / 日本語パワードリル N1 文字・語彙 (index.html) / <unit>`.
- `bp-day-nav` at the bottom: previous / next unit **in book order** (the unit table). First unit's "previous" = the hub; last unit's "next" = back to the hub.
- **Hub update rule:** after building a unit, edit `n1/vocabulary/power-drill/index.html`: flip its chip from `<span class="day-chip soon" data-href="FILE.html">…</span>` to `<a class="day-chip ready" href="FILE.html">…</a>` and bump the `sample-note` line `In progress — N of 42 units built`. Do not touch `n1/vocabulary.html`.
- Reference implementation: [`n1/vocabulary/power-drill/kai-01.html`](../../../../n1/vocabulary/power-drill/kai-01.html).

## 4. Header block (`.bp-header`)

- `.bp-week`: `JLPT N1 · Vocabulary · 日本語パワードリル N1 文字・語彙` (+ romaji `(Nihongo Pawaa Doriru N1 Moji・Goi)`).
- `h1`: `第1回 — 漢字読み・言い換え類義・文脈規定・用法` (+ romaji), or `集中トレーニング① — 動詞 (1)`.
- Source: book name + printed pp + PDF pp.
- Words tested (`.bp-points` spans): the target word of every question (問題1/2/4 underlined words, 問題3 correct answers).
- Answer key: rounds — "別冊 解答, 「第N回 (p.x–p.y)」, PDF page N — confirmed, not guessed." 集中トレーニング — "No answer key in the scan — answers worked out for this site at N1 level, not from the book."
- Notes: drill-only book, no word lists or explanations — every meaning, example sentence and nuance note beyond the book's own question sentences is **added for this site** and marked "(added, not in book)"; format/score; any damaged spot; the exam traps of the round.

## 5. The three required sections, adapted

### §1 Vocabulary List — words tested this round
A `vd-wordlist` table (Japanese+romaji / English / Hindi / Gujarati / Note), one row per question target, in question order, grouped with a sub-heading row or `<h3>` per 問題 (漢字読み / 言い換え / 文脈規定 / 用法). For 問題2 give the word and its paraphrase (e.g. `仲介 ≈ 紹介`); for 問題3 the correct word; for 問題4 the headword plus the 別冊's → substitutes in the Note. Note column also says where it's tested (`問題1 Q3`) and holds one short (added, not in book) collocation/example. Then a small examples table (`bp-examples-table`) for the 4–6 hardest words: first row may be the book's completed question sentence labelled "(book: 問題3 Q2)", every other row "(added, not in book)".
- 集中トレーニング: list both a and b of every item (the drill *is* the contrast) — correct one first; mark the item number.

### §2 Quiz / Exercise Section
One `.bp-quiz` per question, using the grammar power-drill markup (`q-label`, `q-jp` with romaji, `q-translations` with Full sentence + EN/HI/GU, `bp-options` table with all options and the correct row `class="correct"`, `.bp-why`).
- **問題1 漢字読み**: sentence with the target word in `<u>…</u>`; options are kana readings — give each option's own meaning if it is a real word (e.g. あざやか = 鮮やか "vivid") so the distractors teach something; Why = reading + the kanji-reading trap (long/short vowel, voicing, 訓 vs 音).
- **問題2 言い換え類義**: underline the word; options table translates every option; Why explains the paraphrase and why the others don't match.
- **問題3 文脈規定**: （　） in the sentence; Why gives the collocation; add the 別冊's ⊂⊃ phrase where given.
- **問題4 用法**: the headword, then each of the four sentences as an option row (Japanese + romaji + EN/HI/GU of the sentence *as the learner reads it*); correct row marked; Why gives what each wrong sentence should have used — the 別冊's → words, credited "(別冊)".
- **集中トレーニング**: each item as a `.bp-quiz` with a two-row options table (a / b), translations of the completed sentence, Why — flagged "worked out for this site".

### §3 Confusion Pairs / Nuance Notes
`.bp-confusion` table (Form / Meaning / Key difference / Use when) built mainly from the **distractors the book actually used** (e.g. 華やか／鮮やか／艶やか／晴れやか; 気が短い／気が長い／気が強い／気が弱い; 気がしれない／気が済まない／気が利かない／気が乗らない), plus `.bp-callout` exam-trap notes.

## 6. Language & content rules
- EN + Hindi + Gujarati for every meaning, example and question sentence; romaji `<span class="romaji">` under every Japanese line (sentences, options, list entries). Long vowels as in the rest of the site (ou / uu: しゅうち = shuuchi).
- No reading passages exist in this book (all items are single sentences), so quote question sentences in full. There is no audio.
- Never invent questions or answers. The only unofficial answers allowed are the 集中トレーニング ones, flagged as above.

## Notes from the build (coordinator)
- **集中トレーニング answers ARE printed** in small type at the foot of each training page, but the scanner watermark covers most of it. Zoom the footer (e.g. `clip=(0, h-70, w, h)` at 300 dpi) and use any legible fragment to confirm your answers; still label answers "reasoned — not from an official key" unless the full line is legible.
- Hub chips are flipped by the coordinator's sync script — builders never edit index.html.
