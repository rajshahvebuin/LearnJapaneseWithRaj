# 短期マスター 日本語能力試験ドリル N5 — unit-by-unit processing guide

This guide covers turning `Tanki_Master_Drill_N5.pdf` (短期マスター 日本語能力試験ドリル N5, 凡人社編集部 編, 凡人社) into the site's pages under `n5/multi-skill/tanki-master-drill/`. To build a unit, name it by its filename from the table in §3, then follow the steps below.

It mirrors the N1 edition of the same series (`book-source/n1/multi-skill/Tanki_Master_Drill_N1/PROCESSING-GUIDE.md`, built pages in `n1/multi-skill/tanki-master-drill/`). Where this file is silent, the N1 guide applies, and after it the general guides:
- 読解 → `book-source/n1/reading/PROCESSING-GUIDE.md`
- 聴解 → `book-source/n1/listening/PROCESSING-GUIDE.md`

---

## 0. Scan notes (read this first)

The PDF has **89 pages** and is a **mix of two kinds of page**:

| PDF pages | Kind | How to read it |
|---|---|---|
| 1 | Cover (image) | — |
| 2–30 | **Re-typed** pages (Word → PDF, MS Mincho). They have a real **text layer** | `page.get_text()` gives clean Japanese (the console may show mojibake on Windows; write the text to a UTF-8 file). Still render the page to check pictures and underlines |
| 31–45 | Scanned (practice 聴解) | Render at 110–140 dpi. **PDF 37** (6番/7番 options) is faint; use 140 dpi |
| 46–61 | Re-typed, with text layer (まとめのテスト 文字・語彙／文法／読解) | as PDF 2–30. PDF 61 is an image (the 読解 問題4 cinema board) |
| 62–70 | Scanned (まとめ 聴解) | **PDF 65** (4番 options) and **PDF 70** are faint at 80 dpi but fully readable at 140 dpi |
| 71–89 | Scanned 別冊 (answer key + listening scripts) | 140 dpi for the key grid and furigana |

Render with PyMuPDF: `import pymupdf; doc[i-1].get_pixmap(dpi=130)`. Keep scratch renders out of the repo.

**Missing from the scan:** the book's front matter — 目次 (table of contents), the intro page that compares question counts with the real exam, and the CD/how-to-use page — is **not in this PDF**. The structure below is reconstructed from the section dividers and the 別冊 key. Nothing else is missing: every 問題 in the key has its question page, and every listening item has its script.

Underlines: in the re-typed pages the target word of 漢字読み / 表記 / 言い換え類義 is underlined. The text layer does not carry the underline, so confirm it on the render.

---

## 1. What this book is

- A **short, all-section drill book**, not organised by 回 or by day:
  - **練習問題** (practice): 文字・語彙 → 文法 → 読解 → 聴解
  - **まとめのテスト** (review test, "about half the number of questions of the real exam", PDF 46). 目安の時間 (suggested time): 文字・語彙 13分, 文法・読解 25分, 聴解 15分.
  - **別冊 解答・聴解スクリプト** is bound at the end of the same PDF (PDF 71–89).
- Question types (our names, matching the JLPT N5 大問): 文字・語彙 問題1 漢字読み · 問題2 表記 · 問題3 文脈規定 · 問題4 言い換え類義; 文法 問題1 文の文法1 · 問題2 文の文法2 (★) · 問題3 文章の文法; 読解 内容理解（短文）+ 情報検索; 聴解 課題理解 · ポイント理解 · 発話表現 · 即時応答. The scanned 聴解 pages carry the label in the top corner (課題理解, ポイント理解, 発話表現, 即時応答); the re-typed pages carry no label, so the label in our header is ours.
- The book has **no explanations, word lists or grammar notes.** Everything except the questions and options is ours: §1 words/patterns, every translation, every "Why" note and §3. Say so in each unit's header Notes.
- Practice 文字・語彙 問題3 Q9–15 and まとめ 文字・語彙 問題3 Q3–5 have a **picture** under each question (the picture shows the situation). Describe it in one short line in words; never embed the image.

### Unit = one or more 問題 of one section (following the book's own 問題 blocks)

Never split a 問題 across units. N5 sentences are short, so units hold 12–30 items. That gives **12 units**: 8 practice units and 4 review-test units.

---

## 2. Verified page offsets

**Main book: PDF page = printed page + 1.**
- Verified on rendered footers: PDF 16 → p.15, PDF 17 → 16, PDF 19 → 18, PDF 22 → 21, PDF 25 → 24, PDF 30 → 29, PDF 33 → 32, PDF 37 → 36, PDF 41 → 40, PDF 43 → 42, PDF 45 → 44, PDF 46 → 45, PDF 47 → 46, PDF 51 → 50, PDF 56 → 55, PDF 61 → 60, PDF 65 → 64, PDF 69 → 68.
- PDF 2–15 have **no printed footer** (re-typed pages); their printed numbers (p.1–14) are inferred from the same +1 offset.
- Section dividers (no questions): PDF 2 (練習問題 文字・語彙, p.1), PDF 16 (文法, p.15), PDF 24 (読解, p.23), PDF 32 (聴解, p.31), PDF 46 (まとめのテスト intro, p.45).
- Blank pages: PDF 15 (p.14), PDF 23 (p.22), PDF 31 (p.30).

**別冊: PDF page = 別冊 printed page + 70.**
- PDF 71 = 別冊 cover (p.1). PDF 72 → 別冊 p.2 (解答 starts), PDF 73 → 3, PDF 74 → 4, PDF 75 → 5 (聴解スクリプト starts), PDF 80 → 10, PDF 85 → 15 (まとめのテスト scripts start), PDF 89 → 19 (last page).
- Always cite pages as "別冊 p.N (PDF M)".

### Answer key — official, answers only

**別冊 解答 p.2–4 (PDF 72–74).** A grid of 問題 / question number / answer. Read at 140 dpi.
- p.2 (PDF 72): 練習 文字・語彙 問題1–4; 文法 問題1 (all 24), 問題2, 問題3; 読解 問題1–4
- p.3 (PDF 73): 練習 読解 問題5–6; 聴解 問題1–4; まとめ 文字・語彙 問題1 Q1–4 (bottom left), then (top right) 問題1 Q5–6, 問題2–4; まとめ 文法 問題1–3; まとめ 読解 問題1
- p.4 (PDF 74): まとめ 読解 問題2–4; まとめ 聴解 問題1–4

Full key, transcribed and checked at 140 dpi:

| Block | Answers |
|---|---|
| 練習 文字・語彙 問題1 | 1-2 2-3 3-4 4-1 5-2 6-1 7-4 8-1 9-3 10-2 11-3 12-4 13-2 14-3 15-1 16-2 17-1 18-3 |
| 練習 文字・語彙 問題2 | 1-4 2-3 3-2 4-4 5-1 6-1 7-3 8-4 9-1 10-2 11-2 12-4 |
| 練習 文字・語彙 問題3 | 1-2 2-4 3-3 4-4 5-2 6-1 7-2 8-1 9-3 10-1 11-4 12-3 13-3 14-1 15-1 |
| 練習 文字・語彙 問題4 | 1-4 2-3 3-1 4-4 5-2 6-1 7-3 |
| 練習 文法 問題1 | 1-2 2-4 3-3 4-2 5-1 6-2 7-3 8-4 9-3 10-4 11-1 12-2 13-3 14-2 15-4 16-1 17-3 18-4 19-3 20-1 21-3 22-2 23-3 24-4 |
| 練習 文法 問題2 (★) | 1-2 2-3 3-2 4-1 5-4 6-4 7-2 |
| 練習 文法 問題3 | 1-3 2-1 3-4 4-3 5-4 |
| 練習 読解 | 問題1 ①4 · 問題2 ①3 · 問題3 ①2 · 問題4 ①2 · 問題5 ①1 ②3 · 問題6 ①2 |
| 練習 聴解 問題1 | 1-2 2-4 3-4 4-3 5-1 6-3 7-2 |
| 練習 聴解 問題2 | 1-1 2-3 3-1 4-2 5-3 6-4 |
| 練習 聴解 問題3 | 1-2 2-3 3-2 4-1 5-3 |
| 練習 聴解 問題4 | 1-3 2-2 3-1 4-3 5-1 6-2 |
| まとめ 文字・語彙 | 問題1 1-3 2-3 3-2 4-1 5-2 6-4 · 問題2 1-2 2-4 3-1 4-3 · 問題3 1-1 2-1 3-2 4-3 5-3 · 問題4 1-2 2-3 3-4 |
| まとめ 文法 | 問題1 1-3 2-4 3-2 4-1 5-3 6-1 7-1 8-4 · 問題2 (★) 1-3 2-2 3-1 · 問題3 1-1 2-3 3-4 4-3 5-2 |
| まとめ 読解 | 問題1 ①2 · 問題2 ①3 · 問題3 ①4 ②1 · 問題4 ①2 |
| まとめ 聴解 | 問題1 1-4 2-3 3-2 4-4 · 問題2 1-3 2-4 3-2 · 問題3 1-1 2-2 3-2 · 問題4 1-2 2-3 3-2 |

The key gives **no explanations.** All reasoning is ours. Never change an answer; if one looks wrong, keep the book's answer and flag it in the Why note.

### 聴解スクリプト (scripts) — for our reference only, never reproduced

- 練習: 問題1 別冊 p.5–8 (PDF 75–78) · 問題2 p.8–10 (PDF 78–80) · 問題3 p.11–12 (PDF 81–82) · 問題4 p.12–14 (PDF 82–84). A 問題 header can sit mid-page.
- まとめのテスト: 問題1 p.15–16 (PDF 85–86) · 問題2 p.16–18 (PDF 86–88) · 問題3 p.18–19 (PDF 88–89) · 問題4 p.19 (PDF 89).
- Speakers are marked M (男性) / F (女性). Scripts are printed with furigana.

---

## 3. Unit table

| File | Title (hub chip) | Question types | Qs | Printed pp | PDF pp | Answer key (別冊) | Audio tracks |
|---|---|---|---|---|---|---|---|
| moji-goi-1.html | 文字・語彙 問題1 漢字読み | 漢字読み (Q1–18) | 18 | 2–4 | 3–5 | p.2 (PDF 72) | — |
| moji-goi-2.html | 文字・語彙 問題2 表記 | 表記 (Q1–12) | 12 | 5–6 | 6–7 | p.2 (PDF 72) | — |
| moji-goi-3.html | 文字・語彙 問題3–4 文脈規定・言い換え類義 | 文脈規定 (Q1–15, Q9–15 with pictures) · 言い換え類義 (Q1–7) | 22 | 7–13 | 8–14 | p.2 (PDF 72) | — |
| bunpou-1.html | 文法 問題1 文の文法1 | 文の文法1 (Q1–24) | 24 | 16–18 | 17–19 | p.2 (PDF 72) | — |
| bunpou-2.html | 文法 問題2–3 文の文法2・文章の文法 | ★ (Q1–7) · 文章の文法 (1–5, two short self-introductions) | 12 | 19–21 | 20–22 | p.2 (PDF 72) | — |
| dokkai-1.html | 読解 問題1–6 内容理解（短文） | 6 short texts; 問題5 has 2 Qs, others 1 | 7 | 24–29 | 25–30 | p.2–3 (PDF 72–73) | — |
| choukai-1.html | 聴解 問題1–2 課題理解・ポイント理解 | 課題理解 (1–7番) · ポイント理解 (1–6番) | 13 | 32–40 | 33–41 | p.3 (PDF 73) | Tracks 2–16 |
| choukai-2.html | 聴解 問題3–4 発話表現・即時応答 | 発話表現 (1–5番) · 即時応答 (1–6番) | 11 | 41–44 | 42–45 | p.3 (PDF 73) | Tracks 17–29 |
| matome-moji-goi.html | まとめ 文字・語彙 問題1–4 | 漢字読み 6 · 表記 4 · 文脈規定 5 · 言い換え類義 3 | 18 | 46–50 | 47–51 | p.3 (PDF 73) | — |
| matome-bunpou.html | まとめ 文法 問題1–3 | 文の文法1 8 · ★ 3 · 文章の文法 5 | 16 | 51–55 | 52–56 | p.3 (PDF 73) | — |
| matome-dokkai.html | まとめ 読解 問題1–4 | 短文 ×3 (問題3 has 2 Qs) · 情報検索 1 | 5 | 56–60 | 57–61 | p.3–4 (PDF 73–74) | — |
| matome-choukai.html | まとめ 聴解 問題1–4 | 課題理解 4 · ポイント理解 3 · 発話表現 3 · 即時応答 3 | 13 | 61–69 | 62–70 | p.4 (PDF 74) | Tracks 30–46 |

Page notes:
- Practice 文字・語彙 問題1: Q1–7 on PDF 3, Q8–16 on PDF 4, Q17–18 on PDF 5.
- Practice 文字・語彙 問題3: Q1–8 PDF 8; Q9–15 PDF 9–12, one picture each. 問題4 (言い換え類義) PDF 13–14: the four options are whole sentences.
- 文法 問題3 (文章の文法): passage with blanks 1–5 on PDF 21 (two short texts by ナンシー and ワン), options on PDF 22.
- 読解 問題4 (practice) is a one-paragraph family description; 問題5 has 2 questions. まとめ 読解 問題4 is 情報検索: text and question on PDF 60, the cinema schedule board and a note (友だちと会う時間 17:30) on PDF 61.
- まとめ 文法 問題1: Q1–7 PDF 52, Q8 PDF 53. 問題3 passages PDF 55 (two short texts: ロバート and チン), options PDF 56.
- 即時応答 pages (PDF 45, PDF 70) show only the instructions and a メモ box: options exist only in the audio and the script.

### Audio track map (one folder, `Tanki_Master_Drill_N5-AudioCD/NN.mp3`, 01–46, single CD)

Cite as "CD · Track N", using the listening pages' `<span class="ld-track">CD, Track N</span>` badge. **Never publish the audio, never link to the mp3, and never add `<audio>`.** Track numbers are printed in the CD icon next to each 番 on the question pages and in the 別冊 script; they agree.

| Block | Instructions track | Item tracks |
|---|---|---|
| Track 1 | (opening/title; not tied to a question) | — |
| 練習 問題1 課題理解 | 2 | 1番 3 · 2番 4 · 3番 5 · 4番 6 · 5番 7 · 6番 8 · 7番 9 |
| 練習 問題2 ポイント理解 | 10 | 1番 11 · 2番 12 · 3番 13 · 4番 14 · 5番 15 · 6番 16 |
| 練習 問題3 発話表現 | 17 | 1番–5番 = 18–22 |
| 練習 問題4 即時応答 | 23 | 1番–6番 = 24–29 |
| まとめ 問題1 課題理解 | 30 | 1番 31 · 2番 32 · 3番 33 · 4番 34 |
| まとめ 問題2 ポイント理解 | 35 | 1番 36 · 2番 37 · 3番 38 |
| まとめ 問題3 発話表現 | 39 | 1番 40 · 2番 41 · 3番 42 |
| まとめ 問題4 即時応答 | 43 | 1番 44 · 2番 45 · 3番 46 |

---

## 4. Delivery

- Pages live in `n5/multi-skill/tanki-master-drill/`, at depth 3. Assets are `../../../assets/...`. Breadcrumb links use `../../../index.html`, `../../../n5/index.html` and `../../../n5/multi-skill.html`, then the book hub `index.html`.
- Copy the chrome exactly from `moji-goi-1.html`: `auth.js` first in `<head>`, favicon, fonts, `style.css` + `day-page.css`, `body.level-page.n5`, header with the N5 `level-nav`, footer and `main.js`. `python tools/build_site.py` normalises the chrome afterwards.
- Breadcrumb: Home / JLPT N5 / All-in-one / 短期マスター N5 / <unit short title>.
- `.bp-day-nav`: prev = the previous unit in table order (the first unit links back to the hub), next = the next unit (the last unit links back to the hub). Label both with the chip title. If the next unit is not built yet, write it as plain text `<span>Next: … — coming soon</span>` (no dead link), and when you build a unit, turn the previous unit's "coming soon" span into a link.
- Reuse existing classes only (same list as the N1 guide §4). Do not edit the CSS or JS.
- **Hub update rule** (`index.html`): each unit is one chip in one of five `.week-block`s: 練習 文字・語彙 / 練習 文法 / 練習 読解 / 練習 聴解 / まとめのテスト. When a unit is built, change `<span class="day-chip soon" data-href="FILE.html">LABEL</span>` to `<a class="day-chip ready" href="FILE.html">LABEL</a>` and update the `.sample-note` text `In progress — N of 12 units built`. Keep that exact pattern. When N = 12, change it to `Complete — 12 of 12 units built` (with the ✅ icon, as in the N1 hub).

## 5. Header block (every unit)

`.bp-week` = "JLPT N5 · All-in-one · 短期マスター N5 — 練習問題 <section>" (or "まとめのテスト <section>"). `h1` = the 問題 numbers and type labels, plus romaji and an English gloss. Meta grid:
- **Source**: book, section, printed pp (PDF pp), and 問題/Q ranges.
- **Words tested / Patterns tested / Question types**: chips.
- **Answer key**: "Official, answers only — 別冊 解答 p.N (PDF M)", followed by the full answer string.
- **Notes**: the book has no explanations, so §1, all translations, Why notes and §3 are ours. The intro page that compares counts with the real exam is not in our scan, so do not quote exam counts from the book. For 聴解, the audio note (N1 guide §6d).

## 6. The three required sections

Follow N1 guide §6a–6d, with these N5 changes:
- **Keep it simple.** Readers are beginners. Short sentences in the Why notes, one idea each. Explain basic things N1 pages skip: long vowels (せんせい not せんせえ), small っ, voicing (ひゃく／びゃく／ぴゃく), counters, and the common readings of each kanji.
- **表記** (問題2, choose the kanji/katakana for the underlined hiragana): options are kanji or katakana spellings. For each wrong option say what it is (a real kanji with a different meaning, a wrong katakana such as ツ vs シ, ソ vs ン, a missing ー). Give the meaning of real kanji options in EN/HI/GU.
- **文脈規定 with pictures**: one line "Picture (described): …" in EN before the options. The picture is the book's; our description is ours.
- **言い換え類義**: the options are full sentences; give each with romaji + EN/HI/GU, and say which one keeps the meaning.
- **読解**: N5 texts are only 3–6 sentences, but still do **not** transcribe them. Summarise in 2–3 sentences (EN/HI/GU) and quote only the sentence each question needs.
- **聴解**: picture options are described in words. 発話表現: describe the picture (who the arrow points to, the situation) and give the three spoken replies as short paraphrases; they are one short line each, so quoting them is allowed (same rule as 即時応答).

## 7. Language rules

- EN + Hindi + Gujarati for every meaning, example, question and option. Use simple English.
- `<span class="romaji">` under every Japanese line: questions, options, words and confusion forms.
- Anything we add that is not from the book is labelled "(added, not in book)".

## 8. Checks before finishing a unit

- Every answer matches the key table in §2 (and the 別冊 grid at 140 dpi).
- No passage or script reproduced beyond the sentences quoted per question. No audio links.
- Tags balance (Python `html.parser`), all relative links resolve, and the file ends with `</html>`.
- Hub chip flipped and `In progress — N of 12 units built` updated.

---

**Reference implementation:** `n5/multi-skill/tanki-master-drill/moji-goi-1.html` (練習問題 文字・語彙 問題1 漢字読み).
