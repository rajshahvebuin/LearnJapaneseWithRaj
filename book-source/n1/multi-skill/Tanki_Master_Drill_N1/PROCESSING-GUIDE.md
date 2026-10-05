# 短期マスター 日本語能力試験ドリル N1 — unit-by-unit processing guide

This guide covers turning `Tanki_Masuta_Doriru_N1.pdf` (短期マスター 日本語能力試験ドリル N1, 凡人社編集部 編, 凡人社) into the site's pages under `n1/multi-skill/tanki-master-drill/`. To build a unit, name it by its filename from the table in §3, then follow the steps below.

The PDF has 125 pages and is scanned, with no text layer (the only text is a "www.minainai.com" footer stamp). Render pages with PyMuPDF and read them visually: `import pymupdf; doc[i-1].get_pixmap(dpi=130)`. 110–150 dpi is enough. Use 140+ dpi for furigana and for the 別冊 answer grid, because the boxed question numbers are small. Keep scratch renders out of the repo.

Other guides still apply wherever this file is silent:
- 文字・語彙 → `book-source/n1/vocabulary/PROCESSING-GUIDE.md` and `book-source/n1/kanji/PROCESSING-GUIDE.md`
- 文法 → `book-source/n1/grammar/PROCESSING-GUIDE.md` (master) and `book-source/n1/grammar/Drill_&_Drill_N1-Bunpou/PROCESSING-GUIDE.md`, which covers ★ ordering and passage cloze
- 読解 → `book-source/n1/reading/PROCESSING-GUIDE.md`
- 聴解 → `book-source/n1/listening/PROCESSING-GUIDE.md`

---

## 1. What this book is

- It is a **short, all-section drill book**. It is **not** organised by 回 or by day. The structure, from the TOC on PDF 3 and the intro on PDF 4–5, is:
  - **練習問題** (practice): 文字・語彙 p.1 → 文法 p.9 → 読解 p.15 → 聴解 p.41
  - **まとめのテスト** (review test, about half the length of the real exam): 文字・語彙 p.54 → 文法 p.58 → 読解 p.62 → 聴解 p.77. The section divider is p.53. The book suggests 文字・語彙・文法・読解 55分 and 聴解 30分.
  - **別冊 解答・聴解スクリプト** is bound at the end of the same PDF.
- Every page carries a question-type label in its top corner (漢字読み, 文脈規定, 言い換え類義, 用法, 文の文法1/2, 文章の文法, 内容理解（短文／中文／長文）, 統合理解, 主張理解（長文）, 情報検索, 課題理解, ポイント理解, 概要理解, 即時応答, 統合理解). Quote this label in each unit header.
- The book has **no explanations, word lists or grammar notes at all.** Everything except the questions and options is ours: §1 key words or patterns, every translation, every "Why" note, and §3. Say so in each unit's header Notes.
- The intro table on p.ii (PDF 4) compares the real exam's question count per 大問 with the まとめのテスト count. For example, 漢字読み has 6 in the real exam and 3 in the まとめのテスト. The practice sets are larger than the exam: 漢字読み has 9 and 文脈規定 has 10.

### Unit = one or more 問題 of one section (our choice, following the book's own 問題 blocks)

The book's natural blocks are the 問題 numbers inside each section. They are grouped into units of about 12–20 questions so pages stay a manageable length. **Never split a 問題 across units.** That gives 14 units: 9 practice units and 5 review-test units.

---

## 2. Verified page offsets

All offsets were checked against the printed page numbers on the rendered images:

**Main book: PDF page = printed page + 6.**
- PDF 8 → p.2, PDF 9 → 3, PDF 10 → 4, PDF 11 → 5, PDF 13 → 7, PDF 20 → 14, PDF 48 → 42, PDF 49 → 43, PDF 57 → 51, PDF 83 → 77, PDF 90 → 84.
- Front matter: PDF 1 = cover, PDF 2 = blank, PDF 3 = 目次 (p.i), PDF 4 = この本で勉強する人へ (p.ii), PDF 5 = CD/別冊/how-to-use (p.iii).
- Section divider pages carry no number: PDF 7 (文字・語彙, p.1), PDF 15 (文法, p.9), PDF 21 (読解, p.15), PDF 47 (聴解, p.41), PDF 59 (まとめのテスト, p.53).
- Blank pages: PDF 14 (p.8), PDF 46 (p.40), PDF 58 (p.52).

**別冊: PDF page = 別冊 printed page + 90.**
- PDF 91 = 別冊 cover (p.1). PDF 92 → 別冊 p.2 (解答 starts), PDF 93 → 3, PDF 94 → 4, PDF 95 → 5 (聴解スクリプト starts), PDF 104 → 14, PDF 115 → 25 (まとめのテスト scripts start), PDF 125 → 35 (last page).
- Always cite pages as "別冊 p.N (PDF M)".

### Answer key — official, answers only

- **別冊 解答 p.2–4 (PDF 92–94).** It is a grid of 問題 / question number / answer number.
  - p.2: 練習 文字・語彙 and 文法 問題1, then 文法 問題1 Q13–15 and 問題2–3, then 読解 問題1–8
  - p.3: 読解 問題9–14 and 聴解 問題1–5 (left column), plus まとめ 文字・語彙 and 文法 問題1 Q1–4
  - p.4: まとめ 文法 Q5 to the end, 読解, 聴解
- The key gives **no explanations.** All reasoning, including wrong-option analysis, is ours. Never change an answer. Re-read the grid at 140 dpi before you rely on it.
- 聴解 問題5 (統合理解) items with 質問1／質問2 are listed as e.g. `1 質問1 3 質問2 1`.

### 聴解スクリプト (scripts) — for our reference only, never reproduced

- Practice: 問題1 別冊 p.5–9 (PDF 95–99), 問題2 p.9–14 (99–104), 問題3 p.14–18 (104–108), 問題4 p.18–22 (108–112), 問題5 p.22–24 (112–114). Boundaries are approximate. A 問題 header can sit mid-page, so read from one 問題 header to the next.
- まとめのテスト: p.25–35 (PDF 115–125). 問題1 starts at p.25, 問題2 at about p.27, 問題3 at about p.30, 問題4 at about p.32, 問題5 at about p.34. Check these when you build.

---

## 3. Unit table

| File | Title (hub chip) | Question types | Qs | Printed pp | PDF pp | Answer-key PDF (別冊) | Audio tracks |
|---|---|---|---|---|---|---|---|
| moji-goi-1.html | 文字・語彙 問題1–2 | 漢字読み (Q1–9) · 文脈規定 (Q1–10) | 19 | 2–4 | 8–10 | 92 (p.2) | — |
| moji-goi-2.html | 文字・語彙 問題3–4 | 言い換え類義 (Q1–9) · 用法 (Q1–9) | 18 | 5–7 | 11–13 | 92 (p.2) | — |
| bunpou-1.html | 文法 問題1 | 文の文法1 (Q1–15) | 15 | 10–11 | 16–17 | 92 (p.2) | — |
| bunpou-2.html | 文法 問題2–3 | 文の文法2 ★ (Q1–7) · 文章の文法 (Q1–5) | 12 | 12–14 | 18–20 | 92 (p.2) | — |
| dokkai-1.html | 読解 問題1–6 | 内容理解（短文）×6, 1 Q each | 6 | 16–21 | 22–27 | 92 (p.2) | — |
| dokkai-2.html | 読解 問題7–10 | 内容理解（中文）×4, 3 Qs each | 12 | 22–29 | 28–35 | 92–93 (p.2–3) | — |
| dokkai-3.html | 読解 問題11–14 | 内容理解（長文）4Q · 統合理解 3Q · 主張理解（長文）4Q · 情報検索 2Q | 13 | 30–39 | 36–45 | 93 (p.3) | — |
| choukai-1.html | 聴解 問題1–2 | 課題理解 (1–6番) · ポイント理解 (1–7番) | 13 | 42–47 | 48–53 | 93 (p.3) | Tracks 2–16 |
| choukai-2.html | 聴解 問題3–5 | 概要理解 (1–6番) · 即時応答 (1–14番) · 統合理解 (1–3番) | 23 | 48–51 | 54–57 | 93 (p.3) | Tracks 17–44 |
| matome-moji-goi.html | まとめ 文字・語彙 問題1–4 | 漢字読み 3 · 文脈規定 4 · 言い換え類義 3 · 用法 3 | 13 | 54–57 | 60–63 | 93 (p.3) | — |
| matome-bunpou.html | まとめ 文法 問題1–3 | 文の文法1 5 · 文の文法2 3 · 文章の文法 5 | 13 | 58–61 | 64–67 | 93–94 (p.3–4) | — |
| matome-dokkai-1.html | まとめ 読解 問題1–4 | 短文 ×2 (1Q each) · 中文 ×2 (3Q each) | 8 | 62–67 | 68–73 | 94 (p.4) | — |
| matome-dokkai-2.html | まとめ 読解 問題5–8 | 長文 4Q · 統合理解 (A/B) 3Q · 主張理解 4Q · 情報検索 2Q | 13 | 68–76 | 74–82 | 94 (p.4) | — |
| matome-choukai.html | まとめ 聴解 問題1–5 | 課題理解 3 · ポイント理解 4 · 概要理解 3 · 即時応答 7 · 統合理解 1 (質問1/2) | 18 | 77–84 | 83–90 | 94 (p.4) | Tracks 45–67 |

Page notes:
- Practice 文字・語彙 問題2 Q10 runs over onto p.4 (PDF 10), which holds only that question.
- 文法 問題3 (文章の文法) is a passage on p.13 (PDF 19) with its options on p.14 (PDF 20).
- まとめ 文法 問題3 is p.60–61 (PDF 66–67).
- 読解 practice: in the page labels, 問題5 and 問題6 are 短文, not 中文. The intro table's exam count (短文 4) does not match the practice count, so trust the page labels.
- まとめ 読解 問題6 is the A/B 統合理解 pair. 問題8 is 情報検索: the questions are on p.75 (PDF 81) and the 市民一般検診 information table is on p.76 (PDF 82).
- まとめ 聴解 問題5 uses the timetable printed on p.84 (PDF 90).

### Audio track map (one folder, `Tanki_Masuta_Doriru_N1-AudioCD/Track N.mp3`, 1–67, single CD)

Cite as "CD · Track N", using the listening pages' `<span class="ld-track">CD, Track N</span>` badge. **Never publish the audio, never link to the mp3, and never add `<audio>`.**

| Block | Instructions track | Item tracks |
|---|---|---|
| Track 1 | (title or opening; not tied to any question) | — |
| 練習 問題1 課題理解 | 2 | 1番 3 · 2番 4 · 3番 5 · 4番 6 · 5番 7 · 6番 8 |
| 練習 問題2 ポイント理解 | 9 | 1番 10 · 2番 11 · 3番 12 · 4番 13 · 5番 14 · 6番 15 · 7番 16 |
| 練習 問題3 概要理解 | 17 | 1番–6番 = 18–23 |
| 練習 問題4 即時応答 | 24 | 1番–14番 = 25–38 |
| 練習 問題5 統合理解 | 39 | 1番 talk 39 / 質問 40 · 2番 41–42 · 3番 43–44 (question page shows 41 and 43; script shows 42 and 44. Check the split when you build) |
| まとめ 問題1 課題理解 | 45 | 1番 46 · 2番 47 · 3番 48 |
| まとめ 問題2 ポイント理解 | 49 | 1番 50 · 2番 51 · 3番 52 · 4番 53 |
| まとめ 問題3 概要理解 | 54 | 1番–3番 = 55–57 |
| まとめ 問題4 即時応答 | 58 | 1番–7番 = 59–65 |
| まとめ 問題5 統合理解 | 66 | 1番 (talk + 質問1/2) 67 |

---

## 4. Delivery

- Pages live in `n1/multi-skill/tanki-master-drill/`, at depth 3. Assets are `../../../assets/...`. Breadcrumb links use `../../../index.html`, `../../../n1/index.html` and `../../../n1/multi-skill.html`, then the book hub `index.html`.
- Copy the chrome exactly from `moji-goi-1.html`: `auth.js` first in `<head>`, favicon, Noto Sans JP, `style.css` + `day-page.css`, `body.level-page.n1`, header/nav, footer and `main.js`.
- Breadcrumb: Home / JLPT N1 / All-in-one / 短期マスター N1 / <unit short title>.
- `.bp-day-nav`: prev = the previous unit in table order (the first unit links back to the hub), next = the next unit (the last unit links back to the hub). Label both with the chip title.
- Reuse existing classes only. Do not edit the CSS or JS. Classes: `.bp-header`, `.bp-meta-grid`, `.bp-points`, `.bp-note(s)`, `.bp-section-title`, `.bp-point(-head)`, `.bp-badge(.formal)`, `.bp-table`, `.bp-formation-table`, `.bp-examples-table`, `.bp-quiz`, `.q-label`, `.q-jp`, `.q-translations`, `.bp-options` (+ `tr.correct`), `.bp-why`, `.bp-order-chain`, `.bp-assembled`, `.bp-confusion`, `.bp-callout`, `.bp-day-nav`, `.vd-table-wrap`/`.vd-wordlist`, `.kd-*`, `.rd-passage-label`, `.rd-strategy`, `.rd-tr` and `.ld-track`.
- **Hub update rule** (`index.html`): each unit is one chip in one of the five `.week-block`s. These are 練習 文字・語彙 / 練習 文法 / 練習 読解 / 練習 聴解 / まとめのテスト. When you build a unit, change `<span class="day-chip soon" data-href="FILE.html">LABEL</span>` to `<a class="day-chip ready" href="FILE.html">LABEL</a>`. Then update the `.sample-note` text `In progress — N of 14 units built`. Keep that exact pattern, because the sync script reads it. When N = 14, change it to `Complete — 14 of 14 units built`.

## 5. Header block (every unit)

`.bp-week` = "JLPT N1 · All-in-one · 短期マスター N1 — 練習問題 <section>" (or "まとめのテスト <section>"). `h1` = the 問題 numbers and type labels, plus romaji and an English gloss. Meta grid:
- **Source**: book, section, printed pp (PDF pp), and 問題/Q ranges.
- **Words tested / Patterns tested / Question types**: chips.
- **Answer key**: "Official, answers only — 別冊 解答 p.N (PDF M)", followed by the full answer string.
- **Notes**: the book has no explanations, so §1, all translations, Why notes and §3 are ours. Compare the exam's 大問 count with this set's count (p.ii table). For 聴解, the audio note (see §6d).

## 6. The three required sections, per section type

### 6a. 文字・語彙 (漢字読み / 文脈規定 / 言い換え類義 / 用法) — reference: `moji-goi-1.html`
1. **Key Words**: one `.vd-wordlist` (Japanese+romaji / EN / HI / GU / Note), with one row per question's *correct* word in question order. Note = 問題/Q number + related readings, compounds or set phrases. Label the whole table "(added, not in book)".
2. **Quiz**: every question. Give the type's instruction line once per 問題, with romaji and EN/HI/GU. For each Q: `q-jp` with the sentence (underline the target with `<u>` for 漢字読み and 言い換え類義, or `（　　）` for 文脈規定) and romaji; Full sentence (文脈規定 only) + EN/HI/GU; a 4-row options table with EN/HI/GU for **every** option. For 漢字読み options that are not real words, write "not a real word / वास्तविक शब्द नहीं / સાચો શબ્દ નથી". If an option is a real word written with other kanji, give that kanji. `tr.correct` follows the 別冊 key. `.bp-why` explains why the answer fits and why each distractor fails (particles, collocations, kanji look-alikes, voicing).
   - **用法** (choose the sentence where the word is used correctly): the 4 options are whole sentences. Give each option sentence with romaji + EN/HI/GU, and say in the Why what is wrong with each incorrect sentence and which word would fit it.
   - **言い換え類義**: give the original sentence and the sentence with the answer substituted, both with translations.
3. **Confusion Pairs**: `.bp-confusion` tables built from the option sets, plus a `.bp-callout` exam trap.

### 6b. 文法 (文の文法1 / 文の文法2 ★ / 文章の文法)
Follow the Drill&Drill guide §6a–6c (one `.bp-point` per tested pattern, with field, formation and examples tables). There is no 別冊 ポイント to cite, so every field table is ours: mark connection rules and examples "(added, not in book)" unless they come from the question itself. ★ items: stem with `＿＿＿ ＿＿＿ ★ ＿＿＿`, tiles with romaji, `.bp-order-chain`, `.bp-assembled` + EN/HI/GU, and the ★ answer. **文章の文法**: do **not** reproduce the passage. Give a 2–3 sentence "Passage summary (not the book's text)" in EN/HI/GU, then for each blank quote only the sentence that contains it.

### 6c. 読解 (all types)
- **No long passages.** For each 問題: `.rd-passage-label` with the type label, a 2–3 sentence **"Passage summary (not the book's text)"** in EN/HI/GU in our own words, and the source line (author/title) if the book prints one. Then one `.bp-quiz` per question: the question stem (book's, with romaji + EN/HI/GU), quoting **only the sentence(s) the question needs**, an options table with EN/HI/GU for every option, `tr.correct` from the key, and a `.bp-why` that points to *where* in the passage the answer is (paraphrased).
- 統合理解 (A/B): summarise A and B separately (1–2 sentences each).
- 情報検索: describe the table or pamphlet in your own words (what columns or conditions it has). Quote only the cells needed for each answer.
- §1 for reading units = **Key vocabulary** from the passages (`.vd-wordlist`, 10–20 N1 words), plus an optional `.rd-strategy` box for the question type.
- §3 = confusion pairs from the vocabulary or the options (e.g. similar-looking answer choices), plus one exam-trap callout about the question type.
- If any output is blocked by the content filter, leave that part out and report it. Do not try to work around the filter.

### 6d. 聴解 (all types)
- **Audio is never published.** Header note: "The book's audio CD is kept locally and is not published. Play the matching track from your own copy." For each 番, give the `.ld-track` badge "CD, Track N" from §3.
- **No transcripts.** For each 番, write a 2–3 sentence **"Script summary (not the book's text)"** in EN/HI/GU, in our own words. Include the question sentence (it is printed in the 別冊 script and spoken on the audio) with romaji + EN/HI/GU. Quote at most the one or two key lines that decide the answer.
- 課題理解 / ポイント理解 / 統合理解 have printed options: use an options table with EN/HI/GU. Picture options (e.g. 問題1 1番) are described in words.
- 概要理解 / 即時応答 have **no printed options**, because the options are only in the audio and script. Give each option as a short paraphrase line, not a verbatim script. For 即時応答, the prompt and 3 replies are one line each and short, so you may quote them. Mark the correct one from the key.
- §1 = useful listening expressions or vocabulary from the scripts (`.vd-wordlist`). §3 = confusion pairs (e.g. similar-sounding replies in 即時応答, keigo traps).

## 7. Language rules

- EN + Hindi + Gujarati for every meaning, example, question and option. Use simple English.
- `<span class="romaji">` under every Japanese line: questions, options, words and confusion forms.
- Anything we add that is not from the book is labelled "(added, not in book)".

## 8. Checks before finishing a unit

- Every answer matches 別冊 p.2–4. Re-read the grid at 140 dpi, because 1 and 7 and 3 and 8 are easy to confuse at low dpi.
- No passage or script reproduced beyond the sentences quoted per question. No audio links.
- Tags balance (Python `html.parser`), all relative links resolve, and the file ends with `</html>`.
- Hub chip flipped and `In progress — N of 14 units built` updated.

---

**Reference implementation:** `n1/multi-skill/tanki-master-drill/moji-goi-1.html` (練習問題 文字・語彙 問題1–2).

## Notes from the build (coordinator)
- **Practice 聴解 問題5 tracks (verified by track length):** Track 39 = 問題5 + 1番 instructions only; Track 40 = 1番 talk + both 質問; Track 41 = 2番 heading/instructions, Track 42 = 2番 conversation; Track 43 = 3番 heading, Track 44 = 3番 conversation. Cite 40, 41+42 and 43+44.
- **p.ii table** counts 大問 (passages/items), not individual questions.
- **Hub chips** are flipped by the coordinator's sync script; builders never edit index.html.
- **Known key doubt:** まとめ 読解 問題8 Q2 — the key's answer 3 conflicts with the table's 眼科 period (12月〜翌年1月); the page keeps the book's answer and flags it.

