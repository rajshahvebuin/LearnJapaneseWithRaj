# PROCESSING GUIDE — 日本語能力試験 公式問題集 N5 (JLPT Official Practice Workbook N5)

Site hub: `n5/mock-tests/official-workbook/index.html` · Reference unit: `n5/mock-tests/official-workbook/moji-goi.html`

## 1. The source files

| File | Pages | What it is |
|---|---|---|
| `JLPT_Koushiki_Mondaishuu_N5.pdf` | 56 | One complete N5 practice test (問題用紙 for the three papers), 解答用紙 (answer sheets), 正答表 (answer key) and 聴解スクリプト (listening scripts). **No explanations (解説)** anywhere in the book. |
| `JLPT_Koushiki_Mondaishuu_N5-AudioCD/` | 35 tracks | `01-ちょうかいーせつめい.mp3` … `35-おわり.mp3` (one CD). **Never publish.** |

The PDF is an image-only scan (no text layer). Render with PyMuPDF (`import pymupdf`; `fitz` still works but warns), 90–150 dpi for whole pages. The 文字 問題2 options use look-alike / made-up kanji shapes — render those lines at 220–300 dpi (clip) before describing them. Python on this machine wants Windows paths (`C:/...`).

**Book type:** this is the official JLPT workbook — ONE full test, in the current N5 paper layout but with the older item counts (文字・語彙 33 items, 文法・読解 32 items, 聴解 24 items + 4 例). Page headers name the paper and its page, e.g. 「言語知識（文字・語彙）－ 3」.

## 2. Page offsets (verified on the printed page stamps)

| PDF range | printed = | checked on |
|---|---|---|
| 1–27 | PDF + 2 | PDF 1 = p.3 (文字・語彙 cover), 3 = p.5, 4 = p.6, 10 = p.12, 11 = p.13 (文法・読解 cover), 13 = p.15, 20 = p.22, 23 = p.25, 27 = p.29 |
| 28–43 | PDF + 3 (printed p.30 not scanned) | PDF 28 = p.31 (聴解 cover), 30 = p.33, 31 = p.34, 34 = p.37, 35 = p.38, 36 = p.39, 39 = p.42, 40 = p.43, 43 = p.46 |
| 44–46 | PDF + 4 (printed p.47 not scanned) | PDF 44 = p.48, 45 = p.49, 46 = p.50 (解答用紙 ×3) |
| 47–56 | PDF + 5 (printed p.51 not scanned) | PDF 47 = p.52 (正答表), 48 = p.53, 49 = p.54 (聴解スクリプト), 51 = p.56, 54 = p.59, 55 = p.60, 56 = p.61 |

Not in the scan: printed p.1–2 (front matter / title — content unknown), p.30, p.47, p.51 (each falls right after a section's last page, so almost certainly blank versos). The scan ends at p.61 (last script page, 聴解 問題4 6番). **No question, key or script page is missing.**

Blank / filler pages that ARE scanned (grey pattern, no content): PDF 2 (p.4), PDF 12 (p.14), PDF 29 (p.32) — versos of the three covers; PDF 23 (p.25, header 「言語知識（文法）・読解－11」) — a patterned filler page inside 読解. Not scan gaps.

## 3. Structure of the test

| Paper | Time | 問題 (item numbers) | PDF pp (printed) |
|---|---|---|---|
| 言語知識（文字・語彙） | 25分 | cover PDF 1 (p.3), blank PDF 2 · 問題1 漢字読み 1–10 (PDF 3–4) · 問題2 表記 11–18 (PDF 5–6) · 問題3 文脈規定 19–28 (PDF 7–8; 27–28 have pictures) · 問題4 言い換え類義 29–33 (PDF 9–10) | 1–10 (3–12) |
| 言語知識（文法）・読解 | 50分 | cover PDF 11 (p.13), blank PDF 12 · 文法: 問題1 文法形式の判断 1–16 (PDF 13–15) · 問題2 文の組み立て ★ 17–21 (PDF 16–17) · 問題3 文章の文法 22–26 (two short student essays, PDF 18–19) · 読解: 問題4 内容理解（短文） 27–29 (three texts (1)(2)(3), PDF 20–22; 28 = choose the room picture) · 問題5 内容理解（中文） 30–31 (PDF 24–25) · 問題6 情報検索 32 (question PDF 26, shop flyer あらきや PDF 27) | 11–27 (13–29) |
| 聴解 | 30分 | cover PDF 28 (p.31), blank PDF 29 · 問題1 課題理解 例+1–7 (PDF 30–34; pictures or printed options) · 問題2 ポイント理解 例+1–6 (PDF 35–38; printed options) · 問題3 発話表現 例+1–5 (PDF 39–42; one picture each, options only on the audio) · 問題4 即時応答 例+1–6 (PDF 43, "メモ" page only) | 28–43 (31–46) |

解答用紙: PDF 44 文字・語彙, 45 文法・読解, 46 聴解 (printed rotated). Not units.

The book's instruction lines (もんだい1 「＿＿の ことばは ひらがなで どう かきますか…」 etc.) and the 例 items with their filled-in answer bubbles are printed on the test pages and may be quoted.

## 4. Answer key status

**Official and complete** — 正答表 PDF 47–48 (p.52–53). There are **no 解説**: every "Why" on our pages is our own explanation and must be worded as such (e.g. "Official answer 2 (正答表 p.52). Why (our explanation): …"). Keep explanations simple — this is a beginner level.

言語知識（文字・語彙） (PDF 47): 問題1 1-2 2-4 3-1 4-2 5-2 6-3 7-4 8-2 9-2 10-3 · 問題2 11-1 12-2 13-3 14-4 15-4 16-1 17-3 18-1 · 問題3 19-4 20-3 21-1 22-1 23-3 24-2 25-1 26-4 27-2 28-4 · 問題4 29-3 30-1 31-2 32-3 33-4.

言語知識（文法）・読解 (PDF 47–48): 問題1 1-2 2-3 3-2 4-4 5-3 6-2 7-3 8-1 9-3 10-3 11-1 12-1 13-4 14-2 15-4 16-1 · 問題2 17-4 18-1 19-4 20-2 21-2 · 問題3 22-4 23-2 24-4 25-3 26-1 · 問題4 27-2 28-3 29-4 · 問題5 30-4 31-1 · 問題6 32-2.

聴解 (PDF 48): 問題1 例3, 1-2 2-2 3-3 4-3 5-1 6-4 7-4 · 問題2 例3, 1-4 2-3 3-2 4-4 5-1 6-3 · 問題3 例3, 1-1 2-3 3-2 4-3 5-2 · 問題4 例2, 1-1 2-1 3-2 4-3 5-3 6-1.

問題2 (文の組み立て ★): the key gives only the ★ number; the full order is ours — work it out and say "(order worked out by us; the book gives only the ★ answer)".

Print quirk to watch: 文字・語彙 問題2 wrong options are often look-alike kanji that do not exist (e.g. Q13 options 2 and 4, Q15 options 2–3, Q18 options 3–4). Do not try to type a non-existent glyph — describe it ("look-alike shape, not a real kanji") and type the real kanji only where the option really is one (Q12 飯／餃, Q13 卓, Q15 羊, Q18 回).

## 5. Audio — track map (by number only; never publish or embed)

The test pages carry no track badges; the map comes from the CD file names (one CD):

| Section | Tracks |
|---|---|
| 聴解 opening announcement | 01 |
| 問題1 | 02 instructions · 例 03 · 1番 04 · 2番 05 · 3番 06 · 4番 07 · 5番 08 · 6番 09 · 7番 10 |
| 問題2 | 11 instructions · 例 12 · 1番 13 · 2番 14 · 3番 15 · 4番 16 · 5番 17 · 6番 18 |
| break | 19 (ちょっと やすみましょう) |
| 問題3 | 20 instructions · 例 21 · 1番 22 · 2番 23 · 3番 24 · 4番 25 · 5番 26 |
| 問題4 | 27 instructions · 例 28 · 1番 29 · 2番 30 · 3番 31 · 4番 32 · 5番 33 · 6番 34 |
| end | 35 (おわり) |

On pages use the badge `<span class="ld-track">CD · Track 04</span>`. **No `<audio>` elements, no file names or paths.**

聴解スクリプト (PDF 49–56 = p.54–61; M／F speaker labels, furigana): 問題1 PDF 49–51 (例–2番 start PDF 49, up to 5番 PDF 50, 6番–7番 PDF 51) · 問題2 PDF 51–54 (例 starts bottom of PDF 51) · 問題3 PDF 54–55 · 問題4 PDF 55–56. Confirm each 番 on the rendered page.

## 6. Unit definition and table

One unit = one paper, except that 文法・読解 is split at the 文法 / 読解 boundary (its two halves need different page templates). **4 units.**

| # | File | Title | Items | Printed pp | PDF pp | Key PDF (printed) | Script PDF | Audio |
|---|---|---|---|---|---|---|---|---|
| 1 | moji-goi.html | 言語知識（文字・語彙） | 問題1–4, Q1–33 | 5–12 (cover 3) | 3–10 (cover 1) | 47 (52) | — | — |
| 2 | bunpou.html | 言語知識（文法） | 問題1–3, Q1–26 | 15–21 (cover 13) | 13–19 (cover 11) | 47 (52) | — | — |
| 3 | dokkai.html | 読解 | 問題4–6, Q27–32 | 22–29 | 20–27 (23 filler) | 47–48 (52–53) | — | — |
| 4 | choukai.html | 聴解 | 問題1–4 (例 + 7/6/5/6) | 33–46 (cover 31) | 30–43 (cover 28) | 48 (53) | 49–56 (54–61) | CD · Tracks 01–35 |

Hub order and prev/next: moji-goi → bunpou → dokkai → choukai (first unit's prev = the hub; last unit's next = the hub).

## 7. How each paper maps to the page sections

All pages: `bp-header` (Source with printed + PDF pages and the offset, question types, answer key line, Notes) → §1 Points → §2 Every question → §3 Confusion pairs → `bp-day-nav`. EN + Hindi + Gujarati for every meaning, question sentence and option; `<span class="romaji">` under every Japanese line; anything we add is marked "(added, not in book)" — and since the book has no 解説, say once in the header that all explanations are ours. Headings carry the 問題 type and item range. Keep language simple (N5 learners).

### 文字・語彙 (reference: moji-goi.html)
- §1: kanji table (`kd-kanji-table`) for every kanji tested in 問題1–2 (reading in the item + common other reading, our additions); vocabulary table (`bp-table`) for 問題3–4 words; for 問題4 show the underlined phrase and its paraphrase.
- §2: 問題1 漢字読み — sentence + underlined word, options = readings (mark long-vowel / small っ / dakuten traps). 問題2 表記 — options = written forms; describe made-up kanji. 問題3 文脈規定 — sentence with （　）, options with meanings; Q27/28 describe the picture in words. 問題4 言い換え類義 — each option is a full sentence with EN/HI/GU.
- §3: `bp-confusion` from the trap sets (long vowels, っ, dakuten, look-alike kanji, counter readings, time words) + 2–3 `bp-callout`.

### 文法 (template: n1/mock-tests/kanzen-moshi/r1-gengo.html §問題5–7)
- §1: particle / pattern table (pattern → meaning EN/HI/GU → example).
- §2: 問題1 each item with options; 問題2 ★ tiles + `bp-order-chain` + `bp-assembled` (order ours); 問題3 the two essays — **summary only** (EN/HI/GU) + the sentence around each blank.
- §3: particle pairs (は／が, に／で, へ／に, も／と, より／のほうが, まえに／あとで …).

### 読解 (template: n1/mock-tests/kanzen-moshi/r1-dokkai.html)
- §1: strategy box (`rd-strategy`) for 短文 / 中文 / 情報検索 + key words.
- §2: per text: **Passage summary (not the book's text)** EN/HI/GU, the question + options (EN/HI/GU), quote only the key sentence, answer + why. Q28: describe the four room pictures. Q32: summarise the flyer's relevant rows (dates + goods) — a short table of the facts needed is fine; do not reproduce the whole flyer.
- §3: distractor patterns.

### 聴解 (template: n1/mock-tests/kanzen-moshi/r1-choukai.html)
- §1: strategy per 問題 type (課題理解, ポイント理解, 発話表現, 即時応答) + useful expressions (greetings, requests, shopping/time words).
- §2: per item `ld-track` badge, printed options (問題1–2) or picture description (問題1 picture items, 問題3), **Script summary (not the book's text)** EN/HI/GU, quote only the key line(s), official answer + why. 問題3–4 options exist only on the audio: they are short one-line replies and may be quoted as options (they are the answer choices), with EN/HI/GU.
- §3: confusable set phrases (いただきます／ごちそうさま, いってきます／ただいま, どうぞ／どうも …) and number/time traps.

## 8. Passage, script and audio rules (hard)

- **Never reproduce reading passages or listening scripts** — not in pages, scratch files, notes or messages. Summarise in 2–3 sentences (own words, EN/HI/GU) and quote only the sentence(s) a question needs. If any output is blocked by the content filter, drop that part and report it.
- Question stems, printed options, instructions and 例 items may be quoted.
- Audio by track number only. Never link, embed or copy the mp3 files.
- Never invent questions or answers — the 正答表 is official; cite PDF/printed page.

## 9. File naming & hub

- Files flat in `n5/mock-tests/official-workbook/`: `moji-goi.html`, `bunpou.html`, `dokkai.html`, `choukai.html`.
- Hub (`index.html`): one `.week-block` per paper (文字・語彙 / 文法・読解 / 聴解). Built chip `<a class="day-chip ready" href="…">`, unbuilt `<span class="day-chip soon" data-href="…">`. Update `In progress — N of 4 units built`; when all are built, change the note to `✅ Complete — 4 of 4 units built` (build_site.py then marks the book ready).
- After building a unit: flip its chip, check balanced tags (html.parser), every relative link resolves, no `<audio>`, no passage/script text beyond quoted key lines, then run `python tools/build_site.py`.
