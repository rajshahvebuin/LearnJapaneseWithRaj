# 新完全マスター漢字 N1 (Shin Kanzen Master N1 Kanji) — processing guide

Standing instructions for turning `Shin_Kanzen_Master_N1-Kanji.pdf` (新完全マスター漢字 日本語能力試験N1, スリーエーネットワーク, 2010) into the site's unit pages under `n1/kanji/shin-kanzen-master/`. Give a unit filename (e.g. `kai-07.html`) and this is the process to follow.

The PDF is scanned/image-only (no text layer, 220 PDF pages, mostly 595×775 pt). Render pages with PyMuPDF (`import pymupdf`), ~130–150 dpi; render top/bottom halves separately so furigana is legible. Scratch renders go in the session scratch folder, never in the repo.

Master spec for kanji pages: `book-source/n1/kanji/PROCESSING-GUIDE.md` (the 総まとめ book). This book differs: it is organised by **回 (lessons)** grouped by word class, not by week/day, and its kanji list is a **word list** (word · reading · example sentence), not a component cluster table.

---

## 1. Unit definition

A unit = one **第N回** (lesson), one **広がる広げる漢字の知識** (knowledge column), one **模擬問題** (mock test), or one **チャレンジ** section. 42 units in total.

- 第1部 訓読み (第1–11回): each 回 = 2–4 study pages (one per "レベル(n)" / sub-theme). Every study page = **練習 I** (picture or fill-in exercise, top) + **漢字リスト** (numbered word list, bottom) + **answers printed upside-down along the page foot**. Then a 2-page **テスト** (/40点, sections I–V or so).
  - 動詞Aレベル: word is N2-or-below vocabulary but the kanji is N1. 動詞Bレベル: word N1, kanji N2-or-below. 動詞Cレベル: both N1. (本書の使い方 p.vi)
- 第2部 音読み・特別な読み方 (第12–31回): same shape — study pages (練習 + list of kanji with on-yomi and N1 compounds) + テスト.
- 広がる広げる漢字の知識 ①–④: 1–2 page columns (rule box + クイズ), answers in a 答え box at the page foot.
- 第3部 力試し: 模擬問題 第1–5回 (one page each, /15点), チャレンジ 漢字の意味 (2 pp), チャレンジ 読解 (10 pp).
- 付録 (訓読み・音読みが2つ以上ある漢字, 索引) p.169–197 are reference lists — **not units**; consult them only to check readings.

## 2. Page offsets (verified from printed page numbers on every page footer)

The offset **drifts** because blank printed pages were not scanned and a back-cover image was inserted mid-scan:

| Printed pages | PDF = printed + | Notes |
|---|---|---|
| i–vii (front matter) | — | PDF 0 cover, 1 title, 2 copyright, 3 はじめに, 4–5 目次, 6–7 本書の使い方 (vi–vii), 8 漢字リストについて (viii), 9 第1部 divider |
| 3–13 | +7 | |
| (14) | — | not in scan (blank) |
| 15–19 | +6 | |
| (20) | — | not in scan (blank) |
| 21–25 | +5 | |
| (26) | — | not in scan (blank) |
| 27–31 | +4 | |
| (32) | — | not in scan (blank) |
| 33–89 | +3 | PDF 64 = 第2部 divider (p.61, unnumbered) |
| (90) | — | not in scan (blank) |
| 91–146 | +2 | |
| 147–165 | +1 | PDF 149 = 第3部 divider (p.147); p.148 not in scan |
| (166) | — | PDF 167 is the **back cover**, inserted here |
| 167–197 | 0 | PDF 168 = 付録 divider (p.167); p.168 not in scan; 付録/索引 to p.197 = PDF 197 |
| — | — | PDF 198 colophon, PDF 199 series ad |
| 別冊 p.3–21 | +198 | PDF 200 = 別冊 cover; **テストの解答 p.3–7 = PDF 201–205**; 教師用手引き p.8–21 = PDF 206–219 |

The missing pages all fall right after a テスト or column and before a 回 that starts on a fresh page; checked against the 別冊 key (e.g. 第2回 test sections I–V and 第3回 test I–IV are all present), so **no content is believed lost**. If a unit's content ever looks truncated at one of these gaps, say so on the page.

## 3. Answer-key status

- **練習 (study-page exercises)**: answers are printed **upside-down at the foot of the same page** (the book says so on p.vi). Rotate or read the strip (render the bottom ~84–90% band at 200 dpi). These are official.
- **テスト / 模擬問題 / チャレンジ**: official answers in the **別冊 テストの解答, bound into this scan at PDF 201–205** (p.3–7). Layout: p.3 (PDF 201) 第1–6回 · p.4 (PDF 202) 第7–15回 · p.5 (PDF 203) 第15回 tail–第23回 · p.6 (PDF 204) 第23回 tail–第31回 · p.7 (PDF 205) 第31回 tail, 模擬問題 第1–5回, チャレンジ 漢字の意味, チャレンジ 読解.
- **広がる広げる漢字の知識 クイズ**: answers in the 答え box at the foot of each column page.
- The key gives letters/numbers/readings only. "Why" explanations are ours — word them as explanations, not as quotes from the key.
- 教師用手引き (PDF 206–219) is a teacher's guide: useful background for "Why" notes and confusion pairs; do not copy it verbatim.

## 4. Unit table

| filename | title | printed pp | PDF pp | answer key PDF pp |
|---|---|---|---|---|
| kai-01.html | 第1回 動詞Aレベル(1)〜(3) | 3–7 | 10–14 | 練習: page feet · テスト: 201 |
| kai-02.html | 第2回 動詞Aレベル(4)〜(7) | 8–13 | 15–20 | feet · 201 |
| kai-03.html | 第3回 動詞Bレベル(1)〜(3) | 15–19 | 21–25 | feet · 201 |
| kai-04.html | 第4回 動詞Bレベル(4)〜(6) | 21–25 | 26–30 | feet · 201 |
| kai-05.html | 第5回 動詞Cレベル(1)〜(3) | 27–31 | 31–35 | feet · 201 |
| kai-06.html | 第6回 動詞Cレベル(4)〜(6) | 33–37 | 36–40 | feet · 201 |
| kai-07.html | 第7回 い形容詞(1)・(2) | 38–41 | 41–44 | feet · 202 |
| kai-08.html | 第8回 な形容詞・副詞・その他 | 42–45 | 45–48 | feet · 202 |
| kai-09.html | 第9回 名詞(1)道具 (2)人・衣服 (3)身体・感情 | 46–49 | 49–52 | feet · 202 |
| chishiki-1.html | 広がる広げる漢字の知識① 音の濁り | 50 | 53 | page foot |
| kai-10.html | 第10回 名詞(4)自然 (5)植物・食物 (6)建造物・形状 | 51–54 | 54–57 | feet · 202 |
| kai-11.html | 第11回 名詞(7)野生・生活 (8)経済・生活 (9)時・空間 | 55–58 | 58–61 | feet · 202 |
| chishiki-2.html | 広がる広げる漢字の知識② 言葉の構成 | 59–60 | 62–63 | page feet |
| kai-12.html | 第12回 「する」がつく名詞(1) | 62–65 | 65–68 | feet · 202 |
| kai-13.html | 第13回 多くの言葉を作る漢字 | 66–69 | 69–72 | feet · 202 |
| chishiki-3.html | 広がる広げる漢字の知識③ 音の変化 | 70–71 | 73–74 | page feet |
| kai-14.html | 第14回 「する」がつく名詞(2) | 72–75 | 75–78 | feet · 202 |
| kai-15.html | 第15回 「する」がつく名詞(3) | 76–79 | 79–82 | feet · 202–203 |
| kai-16.html | 第16回 「する」がつく名詞(4) | 80–83 | 83–86 | feet · 203 |
| kai-17.html | 第17回 な形容詞(1) | 84–87 | 87–90 | feet · 203 |
| chishiki-4.html | 広がる広げる漢字の知識④ 形声文字 | 88–89 | 91–92 | page feet |
| kai-18.html | 第18回 な形容詞(2)・副詞 | 91–95 | 93–97 | feet · 203 |
| kai-19.html | 第19回 名詞(1)身体・健康 | 96–99 | 98–101 | feet · 203 |
| kai-20.html | 第20回 名詞(2)建造物・日用品 | 100–103 | 102–105 | feet · 203 |
| kai-21.html | 第21回 名詞(3)人間関係・生涯 | 104–107 | 106–109 | feet · 203 |
| kai-22.html | 第22回 名詞(4)数量・範囲 | 108–111 | 110–113 | feet · 203 |
| kai-23.html | 第23回 名詞(5)言語・教育 | 112–115 | 114–117 | feet · 203–204 |
| kai-24.html | 第24回 名詞(6)犯罪・災害 | 116–119 | 118–121 | feet · 204 |
| kai-25.html | 第25回 名詞(7)政治・行政・国際関係 | 120–123 | 122–125 | feet · 204 |
| kai-26.html | 第26回 名詞(8)産業・交通 | 124–127 | 126–129 | feet · 204 |
| kai-27.html | 第27回 名詞(9)経済・流通 | 128–131 | 130–133 | feet · 204 |
| kai-28.html | 第28回 名詞(10)自然・科学・地理 | 132–135 | 134–137 | feet · 204 |
| kai-29.html | 第29回 名詞(11)思想・歴史 | 136–139 | 138–141 | feet · 204 |
| kai-30.html | 第30回 名詞(12)IT関連・娯楽 | 140–143 | 142–145 | feet · 204 |
| kai-31.html | 第31回 特別な読み方をする漢字の言葉 | 144–146 | 146–148 | feet · 204–205 |
| mogi-1.html | 模擬問題 第1回 | 149 | 150 | 205 |
| mogi-2.html | 模擬問題 第2回 | 150 | 151 | 205 |
| mogi-3.html | 模擬問題 第3回 | 151 | 152 | 205 |
| mogi-4.html | 模擬問題 第4回 | 152 | 153 | 205 |
| mogi-5.html | 模擬問題 第5回 | 153 | 154 | 205 |
| challenge-imi.html | チャレンジ 漢字の意味 | 154–155 | 155–156 | 205 |
| challenge-dokkai.html | チャレンジ 読解 | 156–165 | 157–166 | 205 |

Exact page split between a 回's study pages and its テスト: the テスト pages carry a "テスト /40点" banner. Within-回 boundaries above were read from TOC + footers; re-check the first/last page of each unit when building it.

## 5. Page layout (reference implementation: `n1/kanji/shin-kanzen-master/kai-01.html`)

Shared CSS only (`assets/css/style.css` + `assets/css/day-page.css`); no new classes. Pages live 3 levels deep (`../../../`).

- **Breadcrumb**: Home / JLPT N1 / Kanji (`../../kanji.html`) / 新完全マスター N1 漢字 (`index.html`) / 第N回.
- **`.bp-header`**: `.bp-week` = book · 部 name; `h1` = 第N回 — title (+ romaji); meta grid: Source (printed + PDF pages), Words covered (`.bp-points` chips), Answer key (練習 = page feet, テスト = 別冊 page + PDF page), Notes.
- **`.kd-legend`**: the book's own symbols — (自)/(他) = paired intransitive/transitive verb, `/` = a second example, small furigana in examples.
- **§1 Kanji list** — one `.bp-point` per study page (レベル(n)); `.kd-group-head` naming the sub-group (e.g. 「〜う」の動詞) with the book's item-number range as `.bp-badge`. `.kd-kanji-table` columns: **No. | Word (td.kanji) | Reading | Book's example (JP + romaji + EN/HI/GU) | English | Hindi | Gujarati**. Keep the book's numbering. Put (自)/(他) partners and alternate examples in the row's example cell. Add a `.bp-notes` under any group containing same-reading traps.
- **§2 Exercises** — every exercise, in book order:
  - 練習 I (picture tasks): the illustrations are **not reproduced** — describe each picture in one line in your own words, then the prompt (JP + romaji), answer (kanji + reading), completed phrase with EN/HI/GU, and a short "Why". Mark answers "from the book's own key at the page foot".
  - テスト: one `.bp-quiz` per item. Multiple choice → `.bp-options` with `tr.correct`. Reading-writing / word-bank items → a small Blank/Answer/Reading/EN/HI/GU table. Give section headers with the book's point values (e.g. "I (1点×7)").
  - Second-half part 2 (音読み) pages: same shape; the list columns become **Kanji | On/kun | Compound | Reading | EN | HI | GU** (closer to the master spec).
- **§3 Confusion pairs** — `.bp-confusion` built from the unit's own traps (same reading/different kanji such as 撃つ/討つ, 吐く/履く; look-alike distractors from the テスト) + one `.bp-callout` "Exam trap".
- **`.bp-day-nav`**: prev / next unit links (next may not be built yet — still link it).

## 6. Content rules

- EN + Hindi + Gujarati for every meaning, example and question sentence; `<span class="romaji">` under every Japanese line (Hepburn, long vowels as ou/uu).
- Mark anything not in the book "(added, not in book)".
- Never invent questions or answers. Where the key is silent, work it out and flag "not from the official key".
- No long passages: チャレンジ 読解 and any long text → a 2–3 sentence **"Passage summary (not the book's text)"** in EN/HI/GU, then quote only the sentence(s) each question needs. If output is blocked by the content filter, omit that part and report it.
- No audio in this book.

## 7. Hub

`n1/kanji/shin-kanzen-master/index.html` — `.week-list` with blocks 第1部 訓読み / 第2部 音読み・特別な読み方 / 第3部 力試し. Built chip `<a class="day-chip ready" href="FILE">LABEL</a>`; unbuilt `<span class="day-chip soon" data-href="FILE">LABEL</span>`. Keep `.sample-note` text `In progress — N of 42 units built` updated.

## Notes from the build (coordinator)
- **テスト totals vary** (15–40点) and some テスト are one page (e.g. 第9, 10, 11, 31回) — always take counts from the scan.
- **練習 tasks vary by level:** 練習 II (read aloud) appears from 第6回; 第7–8回 練習 I is matching; B-level pages have 練習 I–III.
- **Practice answers are not always on the exercise page** — in 第2部 they are often at the foot of the following kanji-list page; cite the actual page.
- **別冊 PDF 202 is two columns** (第7–11回 left, 第12–15回 right).
- **＊ after a kanji = N2-level kanji** (p.viii); 第2部 lists use No. | Kanji | On/kun | Compound | Reading | EN | HI | GU.
- The 索引 (p.182–197) gives the 回 that teaches each kanji — use it for cross-references.
