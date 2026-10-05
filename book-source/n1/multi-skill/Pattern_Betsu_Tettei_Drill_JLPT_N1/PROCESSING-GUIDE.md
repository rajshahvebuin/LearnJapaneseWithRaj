# パターン別徹底ドリル 日本語能力試験N1 — processing guide

Standing instructions for turning `Pattern_Betsu_Tettei_Drill_JLPT_N1.pdf` (Pattern-betsu Tettei Drill JLPT N1) into the site's unit pages under `n1/multi-skill/pattern-betsu-tettei-drill/`. Give a unit filename from the table below and follow this process.

## 1. The PDF

- 211 PDF pages. **Has a text layer, but it is low-quality OCR** (wrong kanji, scrambled furigana, mojibake on the front matter). Use it only to find pages / skim answer strings; **always render pages (PyMuPDF, 130–150 dpi, half-page clips) and read them visually** before writing anything.
- Every page carries a `facebook.com/duytrieuftu` watermark from the scanner — ignore it.
- No 別冊: **the answer key is in-scan, directly after each drill** (解答 / 解答&解説 / 基本問題解答 / 応用問題解答 boxes). Treat it as the official key. If a key page is missing from the scan (see §3), work the answer out at N1 level and flag it "not from the official key".
- Book order is **unit 1 文字・語彙 → unit 2 聴解 → unit 3 文法 → unit 4 読解** (聴解 comes before 文法). Each unit opens with a TOC page and a 問題を解くコツ page (tips) — summarise the tips (own words) in the first page of that section.

## 2. Offsets (verified on rendered pages)

Offsets drift because the scan is missing and duplicating pages in unit 2.

| PDF range | Printed = | Verified on |
|---|---|---|
| 9–59 (文字・語彙) | PDF − 1 | PDF 9 = p.8 (コツ), PDF 10 = p.9 (漢字読み①), PDF 11 = p.10, PDF 59 = p.58 |
| 61–67 (聴解 課題理解①②) | PDF − 1 then gap | PDF 61 = p.60, PDF 62 = p.61; **pp.62–63 missing**; PDF 63 = p.64, PDF 67 = p.68 |
| 68–69 | duplicates | PDF 68 = p.67 again, PDF 69 = p.68 again (skip) |
| 70–88 | PDF − 1 | PDF 70 = p.69, PDF 88 = p.87 |
| 89–94 | PDF + 1 | **pp.88–89 missing**; PDF 89 = p.90, PDF 94 = p.95 |
| 95–208 | PDF + 3 | **pp.96–97 missing**; PDF 95 = p.98, PDF 131 = p.134, PDF 179 = p.182, PDF 205 = p.208 |

Section TOC pages: PDF 8 (unit 1), PDF 60 (unit 2), PDF 130 (unit 3), PDF 178 (unit 4). PDF 209 = authors/colophon, 210 = back cover.

## 3. Missing / damaged pages (unit 2 only)

| Printed page | What it was | Effect |
|---|---|---|
| p.62 | 課題理解① 基本問題 解答 + script (CD1 T2–3) | answers for 課題① 基本 must be worked out from the 基本問題 options only — no script; mark "answer unknown — key page missing" unless clearly deducible (it usually is not for listening) |
| p.63 | 課題理解① 応用問題 (CD1 T4–5) | questions missing; the 応用 key/script page (p.64) survives — rebuild the questions from it |
| p.88 | ポイント理解③ 応用問題 解答 + script (CD1 T28–29) | answers not in scan |
| p.89 | ポイント理解④ 基本問題 (CD1 T30–31) | question page missing; the key/script page p.90 survives |
| p.96 | 概要理解① 応用問題 解答 + script (CD1 T36–37) | answers not in scan |
| p.97 | 概要理解② 基本問題 (CD1 T38–39) | question page missing; key/script p.98 survives (概要理解 options are only spoken anyway) |

## 4. Unit definition and page structure

A unit = one numbered drill in the book's TOC (漢字読み①, 文脈規定 動詞①, 課題理解①, 文の文法1①, 指示代名詞 …). 64 units.

- **文字・語彙** (2 pages): drill page (6 問 × 2 underlined words = 12 items for 漢字読み; 10 items for 文脈規定/言い換え; 5 items for 用法) + key page with 解答 (or 解答&解説) and a 「この漢字／語彙をマスターしよう！」 table.
- **聴解** (4 pages; 即時応答 2 pages): 基本問題 (2 items) → 基本問題解答 + スクリプト → 応用問題 (2 items) → 応用問題解答 + スクリプト. 即時応答 has 3+3 items on two pages. Some lessons carry a TIPS box (すぐに理解するのが難しい表現, 位置・順番に関連する表現 …) — teach those as §1 points.
- **文法**: 文の文法1 / 文の文法2 = 4 pages: 8 items, 解答 + 解説 (2 pages), 「この文法をマスターしよう！」 table (語法 / 意味・用例・接続). 文章の文法 = 2 pages: one passage with 5 blanks + 解答・解説.
- **読解** (4–6 pages): 基本問題 → 基本解答・解説 → 応用問題 → 応用解答・解説, each with 「この言葉は覚えておこう！」 word lists. 統合理解 and 情報検索 are 6 pages (problems first, keys last). PDF 196 (p.199) is a 読解のストラテジー tips page — fold into dokkai-hissha (or dokkai-tougou) as summarised notes.

## 5. Page sections (all units)

Template: `n1/multi-skill/pattern-betsu-tettei-drill/moji-kanji-yomi-1.html` (reference implementation). Use the shared CSS only (bp-*, kd-*, vd-*, ld-track …), no new CSS/JS.

- Header `.bp-header`: section + pattern, source printed pp + PDF pp, answer-key status (in-scan / missing), audio tracks (listening).
- **§1 Points** — what the book teaches: kanji table (漢字読み, `.kd-kanji-table` from この漢字をマスターしよう), word table (語彙 units, from この語彙をマスターしよう), grammar points (文法, from この文法をマスターしよう: meaning, connection, example), TIPS boxes / useful expressions (聴解), この言葉は覚えておこう word lists (読解). Plus the section's 問題を解くコツ summary on the first unit of each pattern.
- **§2 Every exercise** — every item in `.bp-quiz` cards: the sentence + romaji, full answer sentence, EN/HI/GU, `.bp-options` table with the correct row `class="correct"`, `.bp-why` (book's 解説 paraphrased where present; otherwise your own reasoning, marked "(added, not in book)").
- **§3 Confusion pairs** — `.bp-confusion` built from that unit's distractors (wrong readings, near-synonyms, similar grammar).
- `.bp-day-nav` prev/next within the hub order.

## 6. Passage / transcript / audio rules (hard)

- **Never reproduce reading passages or listening scripts verbatim** — not in pages, scratch files, notes or messages. For each passage/script give a 2–3 sentence **"Passage summary (not the book's text)"** / **"Script summary (not the book's text)"** in EN/HI/GU in your own words, then quote only the sentence(s) a question needs. 文章の文法 passages: summary + only the sentence around each blank. If a filter blocks output, drop that part and report it.
- **Audio is copyrighted and never published.** No `<audio>` elements, no links to .wma files. Refer to tracks only with the badge `<span class="ld-track">CD1 · Track 12</span>`. The .wma files stay in `book-source/` (CD folders next to the PDF).
- Never invent questions or answers. Missing scan pages are marked "missing from the scan". Answers you work out yourself are flagged "not from the official key".
- Language: EN + Hindi + Gujarati for every meaning/example/question sentence; `<span class="romaji">` under every Japanese line; "(added, not in book)" on anything you add.

## 7. Audio track map

CD1 = 41 tracks, CD2 = 48 tracks (89 total). CD1 Track 1 is not referenced by any drill (presumably a title/intro track — unverified). Tracks are listed per unit in the table (基本 tracks / 応用 tracks).

## 8. Unit table

Hub order = book order. "Key" = PDF page(s) carrying the answers.

| # | File | Title | Printed pp | PDF pp | Key PDF pp | Audio |
|---|---|---|---|---|---|---|
| 1 | moji-kanji-yomi-1.html | 漢字読み① (+ 文字・語彙 コツ p.8) | 8–10 | 9–11 | 11 | — |
| 2 | moji-kanji-yomi-2.html | 漢字読み② | 11–12 | 12–13 | 13 | — |
| 3 | moji-kanji-yomi-3.html | 漢字読み③ | 13–14 | 14–15 | 15 | — |
| 4 | moji-kanji-yomi-4.html | 漢字読み④ | 15–16 | 16–17 | 17 | — |
| 5 | moji-kanji-yomi-5.html | 漢字読み⑤ | 17–18 | 18–19 | 19 | — |
| 6 | moji-kanji-yomi-6.html | 漢字読み⑥ | 19–20 | 20–21 | 21 | — |
| 7 | moji-bunmyaku-doushi-1.html | 文脈規定 動詞① | 21–22 | 22–23 | 23 | — |
| 8 | moji-bunmyaku-doushi-2.html | 文脈規定 動詞② | 23–24 | 24–25 | 25 | — |
| 9 | moji-bunmyaku-meishi-1.html | 文脈規定 名詞① | 25–26 | 26–27 | 27 | — |
| 10 | moji-bunmyaku-meishi-2.html | 文脈規定 名詞② | 27–28 | 28–29 | 29 | — |
| 11 | moji-bunmyaku-i-keiyoushi.html | 文脈規定 イ形容詞 | 29–30 | 30–31 | 31 | — |
| 12 | moji-bunmyaku-na-keiyoushi.html | 文脈規定 ナ形容詞 | 31–32 | 32–33 | 33 | — |
| 13 | moji-bunmyaku-fukushi.html | 文脈規定 副詞 | 33–34 | 34–35 | 35 | — |
| 14 | moji-iikae-doushi-1.html | 言い換え類義 動詞① | 35–36 | 36–37 | 37 | — |
| 15 | moji-iikae-doushi-2.html | 言い換え類義 動詞② | 37–38 | 38–39 | 39 | — |
| 16 | moji-iikae-doushi-3.html | 言い換え類義 動詞③ | 39–40 | 40–41 | 41 | — |
| 17 | moji-iikae-i-keiyoushi.html | 言い換え類義 イ形容詞 | 41–42 | 42–43 | 43 | — |
| 18 | moji-iikae-na-keiyoushi.html | 言い換え類義 ナ形容詞 | 43–44 | 44–45 | 45 | — |
| 19 | moji-iikae-fukushi.html | 言い換え類義 副詞 | 45–46 | 46–47 | 47 | — |
| 20 | moji-youhou-doushi.html | 用法 動詞 | 47–48 | 48–49 | 49 | — |
| 21 | moji-youhou-meishi.html | 用法 名詞 | 49–50 | 50–51 | 51 | — |
| 22 | moji-youhou-gairaigo.html | 用法 外来語 | 51–52 | 52–53 | 53 | — |
| 23 | moji-youhou-i-keiyoushi.html | 用法 イ形容詞 | 53–54 | 54–55 | 55 | — |
| 24 | moji-youhou-na-keiyoushi.html | 用法 ナ形容詞 | 55–56 | 56–57 | 57 | — |
| 25 | moji-youhou-fukushi.html | 用法 副詞 | 57–58 | 58–59 | 59 | — |
| 26 | choukai-kadai-1.html | 課題理解① (+ 聴解 コツ p.60) | 60–64 (62–63 missing) | 61–63 | 63 (基本 key missing) | CD1 T2–3 / T4–5 |
| 27 | choukai-kadai-2.html | 課題理解② | 65–68 | 64–67 (68–69 dup) | 65, 67 | CD1 T6–7 / T8–9 |
| 28 | choukai-kadai-3.html | 課題理解③ | 69–72 | 70–73 | 71, 73 | CD1 T10–11 / T12–13 |
| 29 | choukai-kadai-4.html | 課題理解④ | 73–76 | 74–77 | 75, 77 | CD1 T14–15 / T16–17 |
| 30 | choukai-point-1.html | ポイント理解① | 77–80 | 78–81 | 79, 81 | CD1 T18–19 / T20–21 |
| 31 | choukai-point-2.html | ポイント理解② | 81–84 | 82–85 | 83, 85 | CD1 T22–23 / T24–25 |
| 32 | choukai-point-3.html | ポイント理解③ | 85–88 (88 missing) | 86–88 | 87 (応用 key missing) | CD1 T26–27 / T28–29 |
| 33 | choukai-point-4.html | ポイント理解④ | 89–92 (89 missing) | 89–91 | 89, 91 | CD1 T30–31 / T32–33 |
| 34 | choukai-gaiyou-1.html | 概要理解① | 93–96 (96 missing) | 92–94 | 93 (応用 key missing) | CD1 T34–35 / T36–37 |
| 35 | choukai-gaiyou-2.html | 概要理解② | 97–100 (97 missing) | 95–97 | 95, 97 | CD1 T38–39 / T40–41 |
| 36 | choukai-gaiyou-3.html | 概要理解③ | 101–104 | 98–101 | 99, 101 | CD2 T1–2 / T3–4 |
| 37 | choukai-gaiyou-4.html | 概要理解④ | 105–108 | 102–105 | 103, 105 | CD2 T5–6 / T7–8 |
| 38 | choukai-sokuji-1.html | 即時応答① | 109–110 | 106–107 | 107 | CD2 T9–11 / T12–14 |
| 39 | choukai-sokuji-2.html | 即時応答② | 111–112 | 108–109 | 109 | CD2 T15–17 / T18–20 |
| 40 | choukai-sokuji-3.html | 即時応答③ | 113–114 | 110–111 | 111 | CD2 T21–23 / T24–26 |
| 41 | choukai-sokuji-4.html | 即時応答④ | 115–116 | 112–113 | 113 | CD2 T27–29 / T30–32 |
| 42 | choukai-tougou-1.html | 統合理解① | 117–119 | 114–116 | 115, 116 | CD2 T33–34 / T35–36 |
| 43 | choukai-tougou-2.html | 統合理解② | 120–124 | 117–121 | 119, 120–121 | CD2 T37–38 / T39–40 |
| 44 | choukai-tougou-3.html | 統合理解③ | 125–128 | 122–125 | 123, 125 | CD2 T41–42 / T43–44 |
| 45 | choukai-tougou-4.html | 統合理解④ | 129–132 | 126–129 | 127, 129 | CD2 T45–46 / T47–48 |
| 46 | bunpou-bun1-1.html | 文の文法1① (+ 文法 コツ p.134) | 134–138 | 131–135 | 133–134 | — |
| 47 | bunpou-bun1-2.html | 文の文法1② | 139–142 | 136–139 | 137–138 | — |
| 48 | bunpou-bun1-3.html | 文の文法1③ | 143–146 | 140–143 | 141–142 | — |
| 49 | bunpou-bun1-4.html | 文の文法1④ | 147–150 | 144–147 | 145–146 | — |
| 50 | bunpou-bun1-5.html | 文の文法1⑤ | 151–154 | 148–151 | 149–150 | — |
| 51 | bunpou-bun1-6.html | 文の文法1⑥ | 155–158 | 152–155 | 153–154 | — |
| 52 | bunpou-bun1-7.html | 文の文法1⑦ | 159–162 | 156–159 | 157–158 | — |
| 53 | bunpou-bun2-1.html | 文の文法2① (★ ordering) | 163–166 | 160–163 | 161–162 | — |
| 54 | bunpou-bun2-2.html | 文の文法2② | 167–170 | 164–167 | 165–166 | — |
| 55 | bunpou-bun2-3.html | 文の文法2③ | 171–174 | 168–171 | 169–170 | — |
| 56 | bunpou-bunshou-1.html | 文章の文法① (passage cloze) | 175–176 | 172–173 | 173 | — |
| 57 | bunpou-bunshou-2.html | 文章の文法② | 177–178 | 174–175 | 175 | — |
| 58 | bunpou-bunshou-3.html | 文章の文法③ | 179–180 | 176–177 | 177 | — |
| 59 | dokkai-shiji.html | 指示代名詞 (+ 読解 コツ p.182) | 182–186 | 179–183 | 181, 183 | — |
| 60 | dokkai-riyuu.html | 理由 | 187–190 | 184–187 | 185, 187 | — |
| 61 | dokkai-naiyou.html | 内容一致 | 191–194 | 188–191 | 189, 191 | — |
| 62 | dokkai-hissha.html | 筆者の考え (+ 読解のストラテジー p.199) | 195–199 | 192–196 | 193, 195 | — |
| 63 | dokkai-tougou.html | 統合理解 | 200–205 | 197–202 | 201, 202 | — |
| 64 | dokkai-jouhou.html | 情報検索 | 206–211 | 203–208 | 207, 208 | — |

## 9. Reference pages per section

- 文字・語彙 → `n1/kanji/week-1/day-1.html`, `n1/vocabulary/week-1/day-1.html` (+ their PROCESSING-GUIDEs) and this book's `moji-kanji-yomi-1.html`.
- 聴解 → `n1/listening/chapter-1/lesson-1.html` (ld-track badges; summaries instead of scripts here).
- 文法 → `n1/grammar/shin-kanzen-master/part1-lesson-01.html`; ★ ordering → `n1/grammar/drill-and-drill/bun2-01.html`; passage cloze → `n1/grammar/shin-kanzen-master/part3-lesson-02.html`.
- 読解 → `n1/reading/week-1/day-1.html`.

## 10. Hub

`n1/multi-skill/pattern-betsu-tettei-drill/index.html`: one `.week-block` per section pattern; built chips `<a class="day-chip ready" href="FILE">`, unbuilt `<span class="day-chip soon" data-href="FILE">`; keep the `.sample-note` text `In progress — N of 64 units built` up to date when flipping a chip.

## Notes from the build (coordinator)
- **言い換え類義** drills have 8 items (1)–(8) plus an 8-word table — not 10.
- **Partial units (pages missing from the scan):** choukai-kadai-1, choukai-point-3, choukai-point-4, choukai-gaiyou-1; bunpou-bun1-1 Q8 option 3 is only partly legible.
- After the p.62–63 gap the offset is PDF + 1 (PDF 64 = p.65).
