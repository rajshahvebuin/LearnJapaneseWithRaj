# ドリル&ドリル N1 聴解・読解 — round-by-round processing guide

Standing instructions for turning `Drill_&_Drill_N1-Choukai_Dokkai.pdf` (ドリル&ドリル 日本語能力試験 N1 聴解・読解, 星野恵子 + 辻和子, UNICOM Inc., "CD 3枚付") into study pages under `n1/multi-skill/drill-and-drill/`. Give a section + round (e.g. "概要理解 第3回") and follow this file.

This is the sister volume of the grammar book handled in [`../../grammar/Drill_&_Drill_N1-Bunpou/PROCESSING-GUIDE.md`](../../grammar/Drill_&_Drill_N1-Bunpou/PROCESSING-GUIDE.md): same publisher, same 回 (round) structure, same kind of 【別冊】正解・解説 bound into the end of the PDF. The section specs that still apply are [`../../listening/PROCESSING-GUIDE.md`](../../listening/PROCESSING-GUIDE.md) and [`../../reading/PROCESSING-GUIDE.md`](../../reading/PROCESSING-GUIDE.md) (site chrome, CSS classes, three required sections, EN/HI/GU + romaji), **except** where this file says otherwise, especially the passage/script rules in §5.

The PDF (202 pages) is scanned/image-only, with no text layer. Render with PyMuPDF (`import pymupdf`; `doc[i-1].get_pixmap(dpi=...)`). The pages are small (about A5, 298×421 pt): 100 dpi is enough for the question pages, but use **170 dpi, split into left/right half-page crops** for the 別冊 (two dense columns of small text). Put scratch renders in your scratch folder, never in the repo.

---

## 1. What the book is

- **Pure drill book.** It has no teaching chapters. Each 回 is a timed JLPT-format set with a 日付/得点 self-scoring grid (that grid is not content). There is no 合格ライン line in this book.
- **Listening (聴解)** has 5 question types × 4 回 = 20 units. The main book prints **only the CD track label and the answer choices** (text or pictures). Scripts are **only** in the 別冊.
- **Reading (読解)** has 6 question types, 2–4 回 each, 18 units in all. The main book prints the passages, questions and options. 内容理解(短文) also has a 「解き方のヒント」 fill-in box under each passage (the 別冊 fills it in).
- **【別冊】正解・解説** is bound into the same PDF (PDF 113 cover → PDF 201):
  - **N1ことば** (別冊 pp.1–25, PDF 114–138) is a word list per question: word + reading, some with a Japanese gloss 「…」=…, plus English/Chinese/Korean columns. Use it for §1 vocab. Don't copy the Chinese/Korean, and write the English in our own words.
  - **聴解 解説** (別冊 pp.26–76, PDF 139–189): per question 正解, スクリプト (full script), ポイント (numbered key lines → what they imply), 🔑 key note, and ⚠ notes paraphrasing tricky expressions (「A」=「B」).
  - **読解 解説** (別冊 pp.77–88, PDF 190–201): per question 問1 正解… lines, ポイント, <問nのカギ> (the key sentence, paraphrased), and ⚠ notes on why options are wrong. For 短文 it also gives the 解き方のヒント blanks filled in.
- So the answer key is **official for every unit**: never guess, and cite 別冊 p.N (PDF M).

## 2. Verified page offsets

Checked on the printed page numbers in the rendered images:

- **Main book: PDF = printed + 1**, constant from front matter to the end: PDF 3 → p.2 (前書き), 12 → 11 (目次), 17 → 16, 20 → 19, 59 → 58, 107 → 106. TOC numbers match (聴解 divider p.13 = PDF 14, 読解 divider p.57 = PDF 58).
- **別冊: PDF = 別冊 page + 113**: PDF 114 → 別冊 1, 115 → 2, 139 → 26, 141 → 28, 200 → 87, 201 → 88. PDF 113 is the 別冊 cover and PDF 202 is the back cover.
- Blank/filler pages: PDF 13 (blank), 14 (聴解 divider), 15–16 (CD トラック No 一覧), 57 (blank), 58 (読解 divider), 88 (blank).
- Always write 別冊 pages as "別冊 p.N (PDF M)".

## 3. Audio (CD A / B / C)

The book ships with 3 CDs labelled **A, B, C**. Each question header in the main book shows its track (e.g. `CD A-03`). The full list is on PDF 15–16. **No audio was uploaded with this PDF**, and audio is never published anyway. Reference tracks by number only, using the listening badge: `<span class="ld-track">CD A · Track 03</span>`. Never add `<audio>`. Tracks not tied to a question (A-01/02, A-27, B-15, C-01, C-58) are presumably intros/instructions; don't list them as question tracks.

## 4. Unit table (38 units)

Unit = one 回. "Key" = the 別冊 range from that round's 第N回 box to the next box. Several rounds start mid-page or in the right-hand column, so read from box to box.

### 聴解 (listening), 20 units

| File | Title | Qs | Printed pp | PDF pp | Key 別冊 pp (PDF) | Tracks |
|---|---|---|---|---|---|---|
| l-kadai-01.html | 課題理解 第1回 | 1–6 | 16–19 | 17–20 | 26–28 (139–141) | A-03–08 |
| l-kadai-02.html | 課題理解 第2回 | 7–12 | 20–23 | 21–24 | 28–31 (141–144) | A-09–14 |
| l-kadai-03.html | 課題理解 第3回 | 13–18 | 24–27 | 25–28 | 31–34 (144–147) | A-15–20 |
| l-kadai-04.html | 課題理解 第4回 | 19–24 | 28–31 | 29–32 | 34–37 (147–150) | A-21–26 |
| l-point-01.html | ポイント理解 第1回 | 1–7 | 32–33 | 33–34 | 38–40 (151–153) | A-28–34 |
| l-point-02.html | ポイント理解 第2回 | 8–14 | 34–35 | 35–36 | 40–43 (153–156) | A-35–41 |
| l-point-03.html | ポイント理解 第3回 | 15–21 | 36–37 | 37–38 | 43–45 (156–158) | B-01–07 |
| l-point-04.html | ポイント理解 第4回 | 22–28 | 38–39 | 39–40 | 45–48 (158–161) | B-08–14 |
| l-gaiyou-01.html | 概要理解 第1回 | 1–6 | 40 | 41 | 49–51 (162–164) | B-16–21 |
| l-gaiyou-02.html | 概要理解 第2回 | 7–12 | 41 | 42 | 51–52 (164–165) | B-22–27 |
| l-gaiyou-03.html | 概要理解 第3回 | 13–18 | 42 | 43 | 52–55 (165–168) | B-28–33 |
| l-gaiyou-04.html | 概要理解 第4回 | 19–24 | 43 | 44 | 55–56 (168–169) | B-34–39 |
| l-sokuji-01.html | 即時応答 第1回 | 1–14 | 44 | 45 | 57–58 (170–171) | C-02–15 |
| l-sokuji-02.html | 即時応答 第2回 | 15–28 | 45 | 46 | 58–60 (171–173) | C-16–29 |
| l-sokuji-03.html | 即時応答 第3回 | 29–42 | 46 | 47 | 60–62 (173–175) | C-30–43 |
| l-sokuji-04.html | 即時応答 第4回 | 43–56 | 47 | 48 | 62–64 (175–177) | C-44–57 |
| l-tougou-01.html | 統合理解 第1回 | 1–4 | 48–49 | 49–50 | 65–67 (178–180) | C-59–62 |
| l-tougou-02.html | 統合理解 第2回 | 5–8 | 50–51 | 51–52 | 67–70 (180–183) | C-63–66 |
| l-tougou-03.html | 統合理解 第3回 | 9–12 | 52–53 | 53–54 | 70–73 (183–186) | C-67–70 |
| l-tougou-04.html | 統合理解 第4回 | 13–16 | 54–55 | 55–56 | 73–76 (186–189) | C-71–74 |

Question numbers run on through a type's four rounds (課題理解 1–24, ポイント理解 1–28, 概要理解 1–24, 即時応答 1–56, 統合理解 1–16). 概要理解 and 即時応答 print only `【1 2 3 4】` / `【1 2 3】` answer boxes. The choices exist only in the 別冊 script. 統合理解 has 質問1/質問2 sub-questions on some items.

### 読解 (reading), 18 units

| File | Title | Qs | Printed pp | PDF pp | Key 別冊 pp (PDF) |
|---|---|---|---|---|---|
| r-tanbun-01.html | 内容理解(短文) 第1回 | 1–5 | 58–62 | 59–63 | 77 (190) |
| r-tanbun-02.html | 内容理解(短文) 第2回 | 6–10 | 63–67 | 64–68 | 77–78 (190–191) |
| r-chuubun-01.html | 内容理解(中文) 第1回 | 1–2 | 68–71 | 69–72 | 79 (192) |
| r-chuubun-02.html | 内容理解(中文) 第2回 | 3–4 | 72–75 | 73–76 | 79–80 (192–193) |
| r-choubun-01.html | 内容理解(長文) 第1回 | 1 | 76–78 | 77–79 | 81 (194) |
| r-choubun-02.html | 内容理解(長文) 第2回 | 2 | 79–81 | 80–82 | 81 (194) |
| r-choubun-03.html | 内容理解(長文) 第3回 | 3 | 82–83 | 83–84 | 81 (194) |
| r-choubun-04.html | 内容理解(長文) 第4回 | 4 | 84–86 | 85–87 | 82 (195) |
| r-tougou-01.html | 統合理解 第1回 | 1 | 88–89 | 89–90 | 83 (196) |
| r-tougou-02.html | 統合理解 第2回 | 2 | 90–91 | 91–92 | 83 (196) |
| r-tougou-03.html | 統合理解 第3回 | 3 | 92–93 | 93–94 | 83–84 (196–197) |
| r-shuchou-01.html | 主張理解(長文) 第1回 | 1 | 94–96 | 95–97 | 85 (198) |
| r-shuchou-02.html | 主張理解(長文) 第2回 | 2 | 97–99 | 98–100 | 85 (198) |
| r-shuchou-03.html | 主張理解(長文) 第3回 | 3 | 100–102 | 101–103 | 85–86 (198–199) |
| r-shuchou-04.html | 主張理解(長文) 第4回 | 4 | 103–105 | 104–106 | 86 (199) |
| r-jouhou-01.html | 情報検索 第1回 | 1 | 106–107 | 107–108 | 87 (200) |
| r-jouhou-02.html | 情報検索 第2回 | 2 | 108–109 | 109–110 | 87 (200) |
| r-jouhou-03.html | 情報検索 第3回 | 3 | 110–111 | 111–112 | 87–88 (200–201) |

A reading "Q" is a passage. 中文/長文/統合/主張 passages carry 問1–問3 or 問1–問4, and 情報検索 has 問1–問2. 短文 第1回 holds 5 short passages, each with one question. The 別冊 reading key is compact (2 columns per round at most), so quote the 正解 lines carefully.

N1ことば: each section and 回 has its own heading in 別冊 pp.1–25 (PDF 114–138), in book order. 課題理解 第1回 is the top-left column of 別冊 p.1 (PDF 114). Find later rounds by their 第N回 box.

## 5. Copyright rules (hard)

- **No long passages or transcripts.** Never reproduce a reading passage or a listening スクリプト verbatim, in pages, scratch files, notes or messages. For each passage/script, write a 2–3 sentence **"Script summary (not the book's text)"** / **"Passage summary (not the book's text)"** in EN/HI/GU in your own words. Then quote only the line(s) each question turns on: normally the 1–3 short key lines the 別冊 ポイント already singles out. If an output is blocked by the content filter, leave that part out and report it. Don't try to work around the filter.
- Answer choices, question stems, ことば entries and the 別冊's short ⚠ paraphrases are fine to quote.
- **Audio is never published.** Track badge only (see §3).
- **Don't invent questions or answers.** Picture choices (課題理解 3/4/7/10/15/18/19/24…) are described in words (what each letter marks), and the image itself is not reproduced. If a scan page is illegible, say so on the page.

## 6. Page layout per unit

Copy chrome from `l-kadai-01.html` (depth 3: assets `../../../assets/...`, N1 `../../index.html`, module `../../multi-skill.html`, hub `index.html`). Breadcrumb: Home / JLPT N1 / All-in-one / ドリル&ドリル N1 聴解・読解 / <unit>.

**Header** (`.bp-header`): `bp-week` = "JLPT N1 · All-in-one · ドリル&ドリル N1 聴解・読解 — 聴解 (Listening)" or "— 読解 (Reading)"; `h1` = "<type> 第N回" + romaji/English gloss. Meta grid:
- **Source**: printed pp (PDF pp) + question range.
- **Skill covered**: chips.
- **Answer key**: "Official — 【別冊】正解・解説 p.X–Y (PDF A–B)".
- **Notes**: audio-not-published note + CD tracks; the copyright note that scripts/passages are summarised, not reproduced; "(added, not in book)" convention.

**§1 Key Words & Strategy.** Start with a `.rd-strategy` box giving the type's strategy. The source is the 前書き "N1「聴解」/「読解」の勉強のポイント" (PDF 4–5), paraphrased, plus our own tips marked "(added, not in book)". Follow it with a `.bp-table` of the round's N1ことば entries: Japanese + romaji / EN / HI / GU, with the book's Japanese gloss where it gives one, grouped by question number.

**§2 Exercises.** One `.bp-quiz` per question:
- *Listening*: `q-label` N番, `ld-track` badge, the setting/question line (the 別冊's opening sentence and question are short and may be quoted) + EN/HI/GU, then **Script summary (not the book's text)** in EN/HI/GU, then the key line(s) from the ポイント with romaji + EN. After that comes a `.bp-options` table (Option / Japanese / EN / HI / GU, `tr.correct` = 別冊 正解). For picture choices, the Japanese column describes what each letter marks. Close with `.bp-why`, which walks the 別冊 ポイント steps and adds why each distractor fails (ours). 即時応答: the three replies are in the script only, so quote the prompt line + the three short replies (they are one-liners, which is fine), with translations.
- *Reading*: `.rd-passage-label` + **Passage summary (not the book's text)** EN/HI/GU, then per 問: the question stem (quote) + EN/HI/GU, the quoted underlined phrase / key sentence only, options table, and `.bp-why` built from <問nのカギ> + ⚠. 短文 also gets the 解き方のヒント answers as a short list.

**§3 Confusion Pairs / Nuance Notes.** A `.bp-confusion` table built from the 別冊 ⚠ paraphrases (casual → plain meaning) and the distractor traps, plus one `.bp-callout` exam trap.

**Nav**: `.bp-day-nav`, prev/next in table order (first unit → hub as prev; l-tougou-04 → r-tanbun-01; last → hub).

## 7. Hub rules

`n1/multi-skill/drill-and-drill/index.html`: two groups of `.week-block`s (one per question type, 11 blocks). A built chip is `<a class="day-chip ready" href="FILE">第N回</a>`, and an unbuilt one is `<span class="day-chip soon" data-href="FILE">第N回</span>`. Update `.sample-note`: `In progress — N of 38 units built`.

## 8. Checks

正解 re-read at 170 dpi; tags balanced (html.parser); links resolve; file ends `</html>`; hub chip + count updated. Reference implementation: `n1/multi-skill/drill-and-drill/l-kadai-01.html`.

## Notes from the build (coordinator)
- **N1ことば pages not in the unit table:** 概要理解 第1–4回 別冊 p.7–11 (PDF 120–124); 統合理解(聴) p.11–15 (PDF 124–128, starts lower-left of p.11 after a 24番 block); 読解 短文 p.16–17 (PDF 129–130), 中文 p.17–19 (PDF 130–132), 長文 p.19–20 (PDF 132–133), 統合理解(読) p.20–22, 主張理解 p.22–24, 情報検索 p.24–25 (PDF 133–138). 即時応答 has no ことば section — those pages carry an added key-expressions table.
- **⚠ notes are not universal:** 概要理解 rounds 2–4, 短文 and 長文 keys have none; distractor analysis there is ours and labelled.
- **Numbering runs on through each type** (e.g. 短文 第2回 = 6番–10番).
- **即時応答:** the one-line prompt and three one-line replies may be quoted (they are the whole script); everything longer is summarised.
- Existing n1/listening/* (Sou-Matome) pages reproduce full scripts — do not copy that style.
