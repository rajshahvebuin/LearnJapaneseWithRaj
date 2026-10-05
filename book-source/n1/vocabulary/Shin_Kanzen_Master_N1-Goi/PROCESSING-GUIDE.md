# 新完全マスター語彙 N1 (Shin Kanzen Master N1 Goi) — processing guide

Standing instructions for turning `Shin_Kanzen_Master_N1-Goi.pdf` (新完全マスター語彙 日本語能力試験N1, スリーエーネットワーク, 2011) into the site's unit pages under `n1/vocabulary/shin-kanzen-master/`. Give a unit filename (e.g. `part1-lesson-07.html`) and this is the process to follow.

The PDF is scanned/image-only (no text layer; 219 PDF pages, 502×719 pt). Render with PyMuPDF (`import pymupdf`), ~150 dpi in top/bottom halves (`clip=`), and ~220 dpi when you need to tell **bold** headwords from regular ones or read furigana. Scratch renders go in the session scratch folder, never in the repo.

Master spec for vocabulary pages: `book-source/n1/vocabulary/PROCESSING-GUIDE.md` (the 総まとめ book). Sibling guides in this series: `book-source/n1/kanji/Shin_Kanzen_Master_N1-Kanji/PROCESSING-GUIDE.md`, `book-source/n1/grammar/Shin_Kanzen_Master_N1-Bunpou/PROCESSING-GUIDE.md`. This book differs from 総まとめ: it is organised by **章・課 (chapter・lesson)**, not week/day; its word list is a **themed relation map** (antonyms, synonyms, collocation slots), not a flat list; and it has two drill tiers (基本練習 + scored 実践練習).

---

## 1. Unit definition

A unit = one **課** (lesson; a 章 with no 課 counts as one lesson) or one **模擬試験** (mock test). **33 units**: 第1部 15 + 第2部 16 + 模擬試験 2.

- **第1部 話題別に言葉を学ぼう** (topic-based, 9章 15課) — each 課 is exactly **4 printed pages**:
  - p.1: **I. 言葉と例文** — ❶ ウォーミングアップ (2 personal questions, no key answer) + ❷ 言葉 (boxed relation map in numbered groups 1.–4.).
  - p.2: ❸ 語形成 (prefix/suffix/compound patterns from ❷) + ❹ 例文 (5 sentences; the **bold** adverb/adverbial in each is a study point) + **II. 基本練習 ❶ 導入練習** (a short boxed text with ~9 blanks, first/last kana given as hints).
  - p.3: ❷ 連語 (line-matching) · ❸ 意味 (word bank → blanks) · ❹ 類義 (pick the closer synonym) · ❺ 語形成 (circle the right affix).
  - p.4: **III. 実践練習 /20点** — JLPT-format: 1. 語形成 cloze (2点×2) · 2. 文脈規定 (2点×2) · 3. 言い換え類義 (2点×2) · 4. 用法 (4点×2).
- **第2部 性質別に言葉を学ぼう** (property-based, 7章 16課) — 6 printed pages per 課 (8 for 1章2課 and 7章1課・2課):
  - **I. 言葉と例文** — ❶ ウォーミングアップ is a real question **with an answer in the key** (e.g. 「c」, 「かなう」, 「過密」) + ❷ 言葉 (word + meaning/collocation + example sentences, often as a table).
  - **II. 基本練習** — ❶–❹ tasks of type 連語 / 意味 / 用法 (○× correct-the-usage, a/b choice, word-form fill-ins).
  - **III. 実践練習 /25点** — 1.–3. JLPT-format sections; counts vary by 課 (e.g. 1点×14 cloze in 6章) — take point values from the banner.
- **模擬試験** 第1回・第2回 — 2 printed pages each, **/50点**: 1. 文脈規定 (2点×7) · 2. 言い換え類義 (3点×6) · 3. 用法 (3点×6) (verified for 第1回; re-check 第2回 on the scan).
- Front matter (はじめに, 目次, 本書をお使いになる方へ vi–ix), the part dividers and the 索引 (p.172–184) are **not units**. Use the 索引 to cross-reference which 課 teaches a word (it lists page numbers).

## 2. Page offsets (verified from the printed page number in every page footer, PDF 0–218)

| Printed pages | PDF = printed + | Notes |
|---|---|---|
| front matter | — | PDF 0 cover · 1 title · 2 copyright · 3 はじめに · 4–5 目次 · 6–9 本書をお使いになる方へ (vi–ix) · 10 第1部 divider |
| 2–61 | **+9** | 第1部 (PDF 11–70) |
| (62) | — | not in scan (blank); PDF 71 = 第2部 divider (printed 63, unnumbered) |
| 64–165 | **+8** | 第2部 (PDF 72–173) |
| (166) | — | not in scan (blank); PDF 174 = 模擬試験 divider (printed 167, unnumbered) |
| 168–184 | **+7** | 模擬試験 168–171 (PDF 175–178) · 索引 172–184 (PDF 179–191) |
| — | — | PDF 192 colophon (著者/奥付) · 193 series ad · 194 back cover |
| 別冊 1–24 | **+194** | PDF 195 = 別冊 cover (p.1) · **解答 p.2–24 = PDF 196–218** |

Spot-checked on renders: PDF 11 = p.2, PDF 14 = p.5, PDF 70 = p.61, PDF 72 = p.64, PDF 173 = p.165, PDF 175 = p.168, PDF 191 = p.184, PDF 196 = 別冊 p.2, PDF 218 = 別冊 p.24. The two missing pages are blanks before part dividers — **no content is believed lost** (every 課's 4/6/8 pages are present and the key has nothing unmatched).

## 3. Answer-key status — complete official key (別冊 解答, bound in)

- **Every** exercise has an official answer in the 別冊 (PDF 196–218): 第2部 I.❶ warm-up, all 基本練習, all 実践練習, both 模擬試験. Only 第1部 ウォーミングアップ questions (personal opinions) have no answer — give a short sample answer marked "(added, not in book)".
- 導入練習 answers are given as **kana (kanji)**, e.g. ②したわれ（慕われ）. 連語 answers as 「父親に—反発する」. 実践練習 as box number → option number.
- An asterisk (e.g. `3*`) means the key adds a **解説** (explanation) below. Use it for the "Why" note — paraphrase it and say "the key's note says…"; don't copy it verbatim. All other "Why" notes are ours.
- Key layout runs in book order; a 課 often spans two key pages. Per-unit key pages are in the table below.

## 4. Unit table

| filename | title | printed pp | PDF pp | answer key PDF pp (別冊 p.) |
|---|---|---|---|---|
| part1-lesson-01.html | 1章 人間 1課 性格・人柄 | 2–5 | 11–14 | 196 (2) |
| part1-lesson-02.html | 1章 人間 2課 人間関係・付き合い | 6–9 | 15–18 | 196–197 (2–3) |
| part1-lesson-03.html | 2章 生活 1課 日常生活 | 10–13 | 19–22 | 197 (3) |
| part1-lesson-04.html | 2章 生活 2課 医療・健康 | 14–17 | 23–26 | 197–198 (3–4) |
| part1-lesson-05.html | 3章 芸術・スポーツ | 18–21 | 27–30 | 198 (4) |
| part1-lesson-06.html | 4章 教育 | 22–25 | 31–34 | 199 (5) |
| part1-lesson-07.html | 5章 仕事 | 26–29 | 35–38 | 199–200 (5–6) |
| part1-lesson-08.html | 6章 メディア | 30–33 | 39–42 | 200 (6) |
| part1-lesson-09.html | 7章 社会 1課 経済・産業 | 34–37 | 43–46 | 200–201 (6–7) |
| part1-lesson-10.html | 7章 社会 2課 政治・法律・歴史 | 38–41 | 47–50 | 201 (7) |
| part1-lesson-11.html | 7章 社会 3課 社会問題（格差社会・少子高齢化） | 42–45 | 51–54 | 201–202 (7–8) |
| part1-lesson-12.html | 8章 科学 1課 自然・地形 | 46–49 | 55–58 | 202 (8) |
| part1-lesson-13.html | 8章 科学 2課 技術 | 50–53 | 59–62 | 202–203 (8–9) |
| part1-lesson-14.html | 9章 抽象概念 1課 時間・空間 | 54–57 | 63–66 | 203–204 (9–10) |
| part1-lesson-15.html | 9章 抽象概念 2課 関係・変化 | 58–61 | 67–70 | 204 (10) |
| part2-lesson-01.html | 1章 意味がたくさんある言葉 1課 名詞 | 64–69 | 72–77 | 204–205 (10–11) |
| part2-lesson-02.html | 1章 意味がたくさんある言葉 2課 動詞 | 70–77 | 78–85 | 205–206 (11–12) |
| part2-lesson-03.html | 2章 意味が似ている言葉 1課 副詞・形容詞 | 78–83 | 86–91 | 206–207 (12–13) |
| part2-lesson-04.html | 2章 意味が似ている言葉 2課 動詞・名詞 | 84–89 | 92–97 | 207–208 (13–14) |
| part2-lesson-05.html | 3章 形が似ている言葉 1課 漢語 | 90–95 | 98–103 | 208–209 (14–15) |
| part2-lesson-06.html | 3章 形が似ている言葉 2課 和語 | 96–101 | 104–109 | 209–210 (15–16) |
| part2-lesson-07.html | 4章 副詞 1課 程度、時間、頻度の副詞 | 102–107 | 110–115 | 210 (16) |
| part2-lesson-08.html | 4章 副詞 2課 後ろに決まった表現が来る副詞 | 108–113 | 116–121 | 210–211 (16–17) |
| part2-lesson-09.html | 4章 副詞 3課 まとめて覚えたい副詞・その他の副詞 | 114–119 | 122–127 | 211–212 (17–18) |
| part2-lesson-10.html | 5章 オノマトペ 1課 ものの様子・人の様子① | 120–125 | 128–133 | 212–213 (18–19) |
| part2-lesson-11.html | 5章 オノマトペ 2課 人の様子② | 126–131 | 134–139 | 213–214 (19–20) |
| part2-lesson-12.html | 6章 慣用表現 1課 体の言葉を使った慣用表現① | 132–137 | 140–145 | 214–215 (20–21) |
| part2-lesson-13.html | 6章 慣用表現 2課 体の言葉を使った慣用表現②・その他の慣用表現 | 138–143 | 146–151 | 215 (21) |
| part2-lesson-14.html | 7章 語形成 1課 複合動詞① | 144–151 | 152–159 | 215–216 (21–22) |
| part2-lesson-15.html | 7章 語形成 2課 複合動詞② | 152–159 | 160–167 | 216–217 (22–23) |
| part2-lesson-16.html | 7章 語形成 3課 接尾辞・接頭辞 | 160–165 | 168–173 | 217 (23) |
| mock-test-1.html | 模擬試験 第1回 | 168–169 | 175–176 | 217–218 (23–24) |
| mock-test-2.html | 模擬試験 第2回 | 170–171 | 177–178 | 218 (24) |

Page ranges come from the 目次 and every footer; re-check the first and last page when building a unit (e.g. the 実践練習 page carries the "/20点" or "/25点" banner).

## 5. Symbols (本書をお使いになる方へ p.viii, PDF 8) — put them in the page's `.vd-legend`

| Symbol | Meaning |
|---|---|
| A—B | A and B are antonyms (反義語) |
| A・B | A and B share a meaning/usage/property (類義語 etc.) |
| A／B | A and B are separate expressions with different meaning/usage (e.g. 反発する・反感を持つ／猛反対する) |
| A→B | B is closely related to A |
| 〔 〕 | other words can be substituted for what's inside 〔 〕 (e.g. 〔人〕に懐く) |
| [ ] | an explanation of the word's meaning |
| □ (empty box) | a collocation slot: the words listed under it fill the box (e.g. ① □人柄 → 誠実な人柄) |
| **bold** | words to learn specifically for N1 — mark them ★ in our list |

## 6. Page layout (reference implementation: `n1/vocabulary/shin-kanzen-master/part1-lesson-01.html`)

Shared CSS only (`assets/css/style.css` + `assets/css/day-page.css`); no new classes. Pages are 3 levels deep (`../../../`).

- **Breadcrumb**: Home / JLPT N1 (`../../index.html`) / Vocabulary (`../../vocabulary.html`) / 新完全マスター N1 語彙 (`index.html`) / N章 N課.
- **`.bp-header`**: `.bp-week` = book · 部 · 章; `h1` = N課 — title (+ romaji); meta grid: Source (printed + PDF pages, which page holds what), Groups (`.bp-points` chips naming the ❷ 言葉 groups), Answer key (別冊 page + PDF page), Notes (the unit's main exam traps).
- **`.vd-legend`**: the symbols above that actually occur in the unit, plus ★ = bold in book.
- **`.vd-warmup`**: ❶ ウォーミングアップ questions (JP + romaji + EN/HI/GU). 第1部: sample answer "(added, not in book)". 第2部: the key's answer.
- **§1 Words** —
  - ❷ 言葉: one `.bp-point` per book group (1. 性格, 2. 人柄 …) with `.kd-group-head` (h3 + `.bp-badge` "p.N · group N"), then a `.vd-table-wrap` > `.vd-wordlist` with columns **Japanese (★ + headword + romaji) / English / Hindi / Gujarati / Note**. One row per word, in book order; the Note column gives the book's slot (e.g. "□人柄 → 誠実な人柄") and relations (⇔ antonym, ・ synonym, ／ different), each related word with romaji. 第2部 lists add the book's example sentences in the Note cell (JP + romaji + EN/HI/GU), like the kanji book's example column.
  - ❸ 語形成: a `.bp-table` (Pattern | Words | Meaning EN | HI | GU).
  - ❹ 例文: one `.bp-quiz`-style block per sentence (no options) — JP + romaji + EN/HI/GU, with the bold adverb glossed.
- **§2 Exercises** — every item, in book order, section headers with the book's instruction (JP + romaji + EN/HI/GU) and point values:
  - 導入練習: a **"Passage summary (not the book's text)"** (2–3 sentences, EN/HI/GU), then per blank only the short clause containing it (JP + romaji), the answer (kana + kanji), EN/HI/GU of the clause, and a one-line Why. Never reproduce the whole boxed text.
  - 連語 matching: a `.bp-options` table per set (Left | Right (key) | completed phrase + romaji | EN | HI | GU).
  - 意味 / 類義 / 語形成 / 実践練習: one `.bp-quiz` per item — `q-jp` sentence + romaji, `q-translations` with the completed sentence, `.bp-options` (Option / Japanese / EN / HI / GU, `tr.correct`), `.bp-why`. For 用法 items each option is a full sentence — translate each one, mark the correct row.
  - Label official answers "Key: 別冊 p.N"; mark any explanation drawn from a `*` note as "the key's note".
- **§3 Confusion pairs** — `.bp-confusion` built from the unit's own near-synonyms and distractors + one `.bp-callout` "Exam trap" (often straight from a `*` key note: e.g. 温和 can't describe one day's weather; 中傷 needs a falsehood).
- **`.bp-day-nav`**: back to contents + next unit (link it even if not built yet).

## 7. Content rules

- EN + Hindi + Gujarati for every meaning, example and question sentence; `<span class="romaji">` under every Japanese line (Hepburn, long vowels as ou/uu, ん before vowel as n').
- Mark anything not in the book "(added, not in book)".
- Never invent questions or answers. The key is complete; if a scan is ever illegible, say so on the page.
- **No long passages**: 導入練習 boxes and any multi-sentence text → 2–3 sentence "Passage summary (not the book's text)" in EN/HI/GU + only the clause each blank needs. If an output is blocked by the content filter, omit that part and report it.
- No audio in this book.

## 8. Hub

`n1/vocabulary/shin-kanzen-master/index.html` — `.week-list` with blocks 第1部 話題別 / 第2部 性質別 / 模擬試験. Built chip `<a class="day-chip ready" href="FILE">LABEL</a>`; unbuilt `<span class="day-chip soon" data-href="FILE">LABEL</span>`. Keep `.sample-note` text `In progress — N of 33 units built` updated.
