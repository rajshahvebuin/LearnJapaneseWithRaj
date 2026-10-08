# 合格できる日本語能力試験 N4・N5 — unit-by-unit processing guide

This guide covers turning the 合格できる N4・N5 scans in this folder into the site's pages under `n4/multi-skill/goukaku-dekiru/`. To build a unit, name it by its filename from the table in §3, then follow the steps below.

Where this file is silent, follow the guide of the closest built drill book, then the general guides:
- `book-source/n5/multi-skill/Tanki_Master_Drill_N5/PROCESSING-GUIDE.md` (short N5 drill book: same question types, same page format)
- `book-source/n1/multi-skill/Tanki_Master_Drill_N1/PROCESSING-GUIDE.md` (the full §6a–6d rules for each section)
- 読解 → `book-source/n1/reading/PROCESSING-GUIDE.md`
- 聴解 → `book-source/n1/listening/PROCESSING-GUIDE.md`

---

## 0. The book and the two PDFs (read this first)

**Book:** 合格できる日本語能力試験 N4・N5 (Goukaku Dekiru Nihongo Nouryoku Shiken N4・N5), 市川綾子・瀬戸口彩・松本隆 著, 株式会社アルク (ALC), 初版 2010-12-14. Two CDs. One volume covers **both** N5 and N4. The 別冊 (separate booklet) holds 解答 (answers), 聴解スクリプト (scripts) and 解答用紙 (answer sheets).

The folder has **two scans of the same edition** (初版). The page layout and every printed page are the same; only the printing (刷) and the scan differ.

| File | Pages | Printing (from 奥付) | What it contains | Text layer | Use it for |
|---|---|---|---|---|---|
| `Goukaku_Dekiru_N4.5.pdf` | 260 | 第2刷, 2011-06-30 | Front cover, main book p.1–223, back cover, **and the 別冊** (cover, 解答 p.2–7, スクリプト p.8–29, 解答用紙 p.30–33) | none (image only) | **Primary source.** Questions, pictures, answer key and scripts. Clean grey scan |
| `合格できる N4・N5.pdf` | 228 | 第11刷, 2019-08-08 | Main book p.1–223 only. Covers moved to the end (PDF 226–227), PDF 228 blank. **No 別冊** | yes, OCR (patchy: furigana mixed into lines, some kanji wrong) | Cross-check a faint or unclear page; search the OCR text to find which page a question is on. Never copy the OCR text into a page without checking the render |

So the 228-page PDF is not a different edition or a separate booklet: it is a later printing of the main book without the answer booklet. Everything needed (answers and scripts) is only in `Goukaku_Dekiru_N4.5.pdf`.

**Audio:** `Goukaku_Dekiru_N4.5-AudioCD1/1-01.mp3 … 1-67.mp3` (67 tracks) and `Goukaku_Dekiru_N4.5-AudioCD2/2-01.mp3 … 2-66.mp3` (66 tracks), 133 in all. CD1 = 第1部 (practice), CD2 = 第2部 (review test). **Never publish the audio, never link to an mp3, and never add `<audio>`.**

---

## 1. Scan notes and page offsets

Render with PyMuPDF (`import pymupdf; doc[i-1].get_pixmap(dpi=130)`). Keep scratch renders out of the repo. The file name of the second PDF has Japanese characters; on Windows open it with `glob` rather than typing the name.

**`Goukaku_Dekiru_N4.5.pdf` (primary):**
- **Main book: PDF page = printed page + 1.** PDF 1 is the front cover. Verified on footers: PDF 5 → p.4 (目次), PDF 13 → p.12, PDF 14 → p.13, PDF 34 → p.33, PDF 47 → p.46, PDF 52 → p.51, PDF 94 → p.93, PDF 147 → p.146, PDF 191 → p.190, PDF 213 → p.212, PDF 223 → p.222.
- PDF 224 = p.223 (blank), PDF 225 = 奥付 (colophon), PDF 226 = back cover.
- **別冊: PDF page = 別冊 page + 226.** PDF 227 = 別冊 cover (p.1). PDF 228 → 別冊 p.2 (解答 starts), PDF 233 → p.7, PDF 234 → p.8 (スクリプト starts), PDF 255 → p.29, PDF 256–259 → p.30–33 (解答用紙, answer sheets for the review test), PDF 260 blank.
- Always cite answers as "別冊 p.N (PDF M)" and questions as "p.N (PDF M)".

**`合格できる N4・N5.pdf` (second scan):** **PDF page = printed page** (PDF 1 = title page p.1, PDF 4 = 目次 p.4, PDF 222 = p.222). Slight yellow tint; same content.

Reading:
- 文字・語彙 and 文法 pages: 130 dpi is enough. The underline under the tested word is clear at 130 dpi; crop at 250 dpi if a short underline (one kanji) is unclear.
- Furigana on N4 pages and in the 別冊 scripts: 150 dpi, or a 250 dpi crop.
- 聴解 pictures: 110–130 dpi.
- The 別冊 key grid: 130 dpi.

Nothing is missing from the primary scan: the 目次, はじめに, the 改定の概要 pages (p.6–8, about the 2010 exam change), every 問題 page, the full key and every script are present.

---

## 2. What this book is

- **第1部 練習問題 (practice), p.9–158**, by level and by exam section. Each section follows the real JLPT 大問 order:
  - **N5** (p.11–60). N5 pages say **もんだい** in hiragana.
    - 言語知識（文字・語彙）: もんだい1 文字 漢字の読み方 · もんだい2 文字 文字の書き方 · もんだい3 語彙「正しい意味」の文 · もんだい4 語彙「同じ意味」の文
    - 言語知識（文法）・読解: もんだい1 文法「正しい文法」の文 · もんだい2 文法 ことばの順番 (★) · もんだい3 文法 文章の中のことば · もんだい4 読解 短い文章を読む · もんだい5 読解 すこし長い文章を読む · もんだい6 読解「必要なこと」をさがす
    - 聴解: もんだい1「どうするか」を聞く · もんだい2「必要なところ」を聞く · もんだい3 自分から話す · もんだい4 すぐ返事をする
  - **N4** (p.61–158). N4 pages say **問題** in kanji. Same sections, plus 問題5 語彙 ことばの使い方 (用法). The N4 language-knowledge drills are very long (問題1 has 86 questions, 問題2 ★ has 84).
- **第2部 総復習問題 (review = mock test), p.159–222**: one full-length mock paper for N5 (p.161–190) and one for N4 (p.191–222). The question numbers run on through each paper ([1]–[35] in 文字・語彙, [1]–[36]/[35] in 文法・読解) and restart at 1ばん in each 聴解 問題, exactly like the real exam. 別冊 p.30–33 are the matching mark sheets.
- **Column「これが たいせつ！」①–⑤** (p.33, 51, 93, 119, 125): one-page mini drills (clothing verbs, particles of movement, number readings, set greetings, adverbs, etc.). Their answers are printed **upside down at the bottom of the same page**. Each one goes at the end of the unit it sits in (see §3).
- The book itself has **no explanations, no word lists and no translations.** Everything except the question sentences and options is ours: the word / pattern tables, every translation, every "Why" note and the confusion section. Say so in each unit's header Notes.
- The 改定の概要 pages (p.6–8) give the N4/N5 test sections and times; use them only for the hub's "How to use" notes.

### Unit = one or more 問題 of one section, never splitting a question

N5 units hold 15–30 items. The very long N4 drills are split **at page boundaries** into parts of about 20 items (17–24). Reading units hold 3–4 texts. Listening units hold two 問題 (13–16 items). Each review-test section is its own unit, except 聴解, which is split in two. That gives **50 units**:

- 第1部 N5: 11 units (`n5-…`)
- 第1部 N4: 29 units (`n4-…`)
- 第2部 総復習 N5: 5 units (`sofuku-n5-…`)
- 第2部 総復習 N4: 5 units (`sofuku-n4-…`)

---

## 3. Unit table

PDF pages are for `Goukaku_Dekiru_N4.5.pdf`. Answer pages are in its 別冊.

### 第1部 練習問題 — N5

| # | File | Title (hub chip) | Romaji / English | Qs | Printed pp | PDF pp | Answer key (別冊) |
|---|---|---|---|---|---|---|---|
| 1 | n5-moji-goi-1.html | もんだい1 漢字の読み方 | Kanji no yomikata — reading kanji | 20 | 12–13 | 13–14 | p.2 (PDF 228) |
| 2 | n5-moji-goi-2.html | もんだい2 文字の書き方 | Moji no kakikata — writing words (表記) | 15 | 14–15 | 15–16 | p.2 (PDF 228) |
| 3 | n5-moji-goi-3.html | もんだい3–4 「正しい意味」の文・「同じ意味」の文 | Tadashii imi / onaji imi — context words & paraphrase | 18 + 10 | 16–19 | 17–20 | p.2 (PDF 228) |
| 4 | n5-bunpou-1.html | もんだい1 「正しい文法」の文 (1) | Tadashii bunpou no bun — grammar form, Q1–16 | 16 | 20–21 | 21–22 | p.2 (PDF 228) |
| 5 | n5-bunpou-2.html | もんだい1 「正しい文法」の文 (2) | Q17–34 | 18 | 22–23 | 23–24 | p.2 (PDF 228) |
| 6 | n5-bunpou-3.html | もんだい2–3 ことばの順番・文章の中のことば | Kotoba no junban (★) / bunshou no naka no kotoba | 12 + 15 | 24–29 | 25–30 | p.2 (PDF 228) |
| 7 | n5-dokkai-1.html | もんだい4 短い文章を読む | Mijikai bunshou — short texts (+ Column ①) | 4 | 30–33 | 31–34 | p.2 (PDF 228) |
| 8 | n5-dokkai-2.html | もんだい5 すこし長い文章を読む | Sukoshi nagai bunshou — mid-length texts | 7 | 34–37 | 35–38 | p.2 (PDF 228) |
| 9 | n5-dokkai-3.html | もんだい6 「必要なこと」をさがす | Hitsuyou na koto o sagasu — information search | 3 | 38–45 | 39–46 | p.2 (PDF 228) |
| 10 | n5-choukai-1.html | もんだい1–2 「どうするか」・「必要なところ」を聞く | Task / point comprehension (+ Column ②) | 8 + 7 | 46–55 | 47–56 | p.3 (PDF 229) |
| 11 | n5-choukai-2.html | もんだい3–4 自分から話す・すぐ返事をする | Utterances / quick response | 7 + 6 | 56–60 | 57–61 | p.3 (PDF 229) |

### 第1部 練習問題 — N4

| # | File | Title (hub chip) | Romaji / English | Qs | Printed pp | PDF pp | Answer key (別冊) |
|---|---|---|---|---|---|---|---|
| 12 | n4-moji-goi-1.html | 問題1 漢字の読み方 (1) | Kanji reading, Q1–20 | 20 | 62–63 | 63–64 | p.3 (PDF 229) |
| 13 | n4-moji-goi-2.html | 問題1 漢字の読み方 (2) | Q21–44 | 24 | 64–65 | 65–66 | p.3 (PDF 229) |
| 14 | n4-moji-goi-3.html | 問題1 漢字の読み方 (3) | Q45–68 | 24 | 66–67 | 67–68 | p.3 (PDF 229) |
| 15 | n4-moji-goi-4.html | 問題1 漢字の読み方 (4) | Q69–86 | 18 | 68–69 | 69–70 | p.3 (PDF 229) |
| 16 | n4-moji-goi-5.html | 問題2 文字の書き方 (1) | Writing words (表記), Q1–21 | 21 | 70–71 | 71–72 | p.3 (PDF 229) |
| 17 | n4-moji-goi-6.html | 問題2 文字の書き方 (2) | Q22–45 | 24 | 72–73 | 73–74 | p.3 (PDF 229) |
| 18 | n4-moji-goi-7.html | 問題2 文字の書き方 (3) | Q46–65 | 20 | 74–75 | 75–76 | p.3 (PDF 229) |
| 19 | n4-moji-goi-8.html | 問題3 「正しい意味」の文 (1) | Context words (文脈規定), Q1–23 | 23 | 76–77 | 77–78 | p.3 (PDF 229) |
| 20 | n4-moji-goi-9.html | 問題3 「正しい意味」の文 (2) | Q24–47 | 24 | 78–79 | 79–80 | p.3 (PDF 229) |
| 21 | n4-moji-goi-10.html | 問題3 「正しい意味」の文 (3) | Q48–70 | 23 | 80–81 | 81–82 | p.3 (PDF 229) |
| 22 | n4-moji-goi-11.html | 問題4 「同じ意味」の文 (1) | Paraphrase (言い換え類義), Q1–19 | 19 | 82–85 | 83–86 | p.4 (PDF 230) |
| 23 | n4-moji-goi-12.html | 問題4 「同じ意味」の文 (2) | Q20–39 | 20 | 86–89 | 87–90 | p.4 (PDF 230) |
| 24 | n4-moji-goi-13.html | 問題4 「同じ意味」の文 (3) | Q40–54 (+ Column ③) | 15 | 90–93 | 91–94 | p.4 (PDF 230) |
| 25 | n4-moji-goi-14.html | 問題5 ことばの使い方 (1) | Word usage (用法), Q1–14 | 14 | 94–96 | 95–97 | p.4 (PDF 230) |
| 26 | n4-moji-goi-15.html | 問題5 ことばの使い方 (2) | Q15–26 | 12 | 97–99 | 98–100 | p.4 (PDF 230) |
| 27 | n4-bunpou-1.html | 文法 問題1 「正しい文法」の文 (1) | Grammar form, Q1–23 | 23 | 100–102 | 101–103 | p.4 (PDF 230) |
| 28 | n4-bunpou-2.html | 文法 問題1 「正しい文法」の文 (2) | Q24–41 | 18 | 103–105 | 104–106 | p.4 (PDF 230) |
| 29 | n4-bunpou-3.html | 文法 問題1 「正しい文法」の文 (3) | Q42–64 | 23 | 106–109 | 107–110 | p.4 (PDF 230) |
| 30 | n4-bunpou-4.html | 文法 問題2 ことばの順番 (1) | Sentence order (★), Q1–23 | 23 | 110–112 | 111–113 | p.4 (PDF 230) |
| 31 | n4-bunpou-5.html | 文法 問題2 ことばの順番 (2) | Q24–45 | 22 | 113–114 | 114–115 | p.4 (PDF 230) |
| 32 | n4-bunpou-6.html | 文法 問題2 ことばの順番 (3) | Q46–67 | 22 | 115–116 | 116–117 | p.4 (PDF 230) |
| 33 | n4-bunpou-7.html | 文法 問題2 ことばの順番 (4) | Q68–84 (+ Column ④) | 17 | 117–119 | 118–120 | p.4 (PDF 230) |
| 34 | n4-bunpou-8.html | 文法 問題3 文章の中のことば | Text grammar: 3 passages, 5+4+5 blanks (+ Column ⑤) | 14 | 120–125 | 121–126 | p.5 (PDF 231) |
| 35 | n4-dokkai-1.html | 問題4 短い文章を読む | Short texts | 4 | 126–129 | 127–130 | p.5 (PDF 231) |
| 36 | n4-dokkai-2.html | 問題5 すこし長い文章を読む (1) | Mid-length texts [1]–[2] | 6 | 130–133 | 131–134 | p.5 (PDF 231) |
| 37 | n4-dokkai-3.html | 問題5 すこし長い文章を読む (2) | Mid-length texts [3]–[4] | 7 | 134–137 | 135–138 | p.5 (PDF 231) |
| 38 | n4-dokkai-4.html | 問題6 「必要なこと」をさがす | Information search: 3 tasks, 2 Qs each | 6 | 138–145 | 139–146 | p.5 (PDF 231) |
| 39 | n4-choukai-1.html | 問題1–2 「どうするか」・「必要なところ」を聞く | Task / point comprehension | 9 + 7 | 146–155 | 147–156 | p.5 (PDF 231) |
| 40 | n4-choukai-2.html | 問題3–4 自分から話す・すぐ返事をする | Utterances / quick response | 5 + 8 | 156–158 | 157–159 | p.5 (PDF 231) |

### 第2部 総復習問題 (mock tests)

| # | File | Title (hub chip) | Content | Qs | Printed pp | PDF pp | Answer key (別冊) |
|---|---|---|---|---|---|---|---|
| 41 | sofuku-n5-moji-goi.html | N5 文字・語彙 もんだい1–4 | 漢字読み [1]–[12] · 表記 [13]–[20] · 文脈規定 [21]–[30] · 言い換え [31]–[35] | 35 | 162–167 | 163–168 | p.5 (PDF 231) |
| 42 | sofuku-n5-bunpou.html | N5 文法 もんだい1–3 | 文法形式 [1]–[16] · ★ [17]–[21] · 文章の文法 [22]–[26] | 26 | 168–171 | 169–172 | p.6 (PDF 232) |
| 43 | sofuku-n5-dokkai.html | N5 読解 もんだい4–6 | 短文 [27]–[29] · 中文 [30]–[33] · 情報検索 [34]–[36] | 10 | 172–177 | 173–178 | p.6 (PDF 232) |
| 44 | sofuku-n5-choukai-1.html | N5 聴解 もんだい1–2 | 課題理解 1–8ばん · ポイント理解 1–7ばん | 15 | 178–186 | 179–187 | p.6 (PDF 232) |
| 45 | sofuku-n5-choukai-2.html | N5 聴解 もんだい3–4 | 発話表現 1–7ばん · 即時応答 1–6ばん | 13 | 187–190 | 188–191 | p.6 (PDF 232) |
| 46 | sofuku-n4-moji-goi.html | N4 文字・語彙 問題1–5 | 漢字読み [1]–[9] · 表記 [10]–[15] · 文脈規定 [16]–[25] · 言い換え [26]–[30] · 用法 [31]–[35] | 35 | 192–199 | 193–200 | p.6–7 (PDF 232–233) |
| 47 | sofuku-n4-bunpou.html | N4 文法 問題1–3 | 文法形式 [1]–[15] · ★ [16]–[20] · 文章の文法 [21]–[25] | 25 | 200–204 | 201–205 | p.7 (PDF 233) |
| 48 | sofuku-n4-dokkai.html | N4 読解 問題4–6 | 短文 [26]–[29] · 中文 [30]–[33] · 情報検索 [34]–[35] | 10 | 205–211 | 206–212 | p.7 (PDF 233) |
| 49 | sofuku-n4-choukai-1.html | N4 聴解 問題1–2 | 課題理解 1–8ばん · ポイント理解 1–7ばん | 15 | 212–218 | 213–219 | p.7 (PDF 233) |
| 50 | sofuku-n4-choukai-2.html | N4 聴解 問題3–4 | 発話表現 1–5ばん · 即時応答 1–8ばん | 13 | 219–222 | 220–223 | p.7 (PDF 233) |

Page notes:
- N5 文字・語彙 もんだい1: Q1–8 on p.12, Q9–20 on p.13.
- N5 文法 もんだい1: Q1–6 p.20, Q7–16 p.21, Q17–25 p.22, Q26–34 p.23. もんだい2 (★) begins with a worked れい (example) that explains how to answer; give it in short in the unit's intro.
- N5 文法 もんだい3: three passages (1ばん, 2ばん, 3ばん), five blanks each; the key lists them as 1ばん [1]–[5] etc.
- N5 読解 もんだい5: [1] and [2] have 1 question, [3] has 2 (とい1–2), [4] has 3 (とい1–3). もんだい6 has 3 separate tasks, each with 1 question, on p.38–45 (a postage price list, a community-centre class poster, a rubbish-sorting notice; the texts often take a full page).
- N4 問題1: p.62 Q1–8, p.63 Q9–20, p.64 Q21–32, p.65 Q33–44, p.66 Q45–56, p.67 Q57–68, p.68 Q69–80, p.69 Q81–86.
- N4 問題2: p.70 Q1–9, p.71 Q10–21, p.72 Q22–33, p.73 Q34–45, p.74 Q46–57, p.75 Q58–65.
- N4 問題3: p.76 Q1–10, p.77 Q11–23, p.78 Q24–35, p.79 Q36–47, p.80 Q48–60, p.81 Q61–70.
- N4 問題4 (5 per page, options are full sentences): p.82 Q1–4, p.83 Q5–9, p.84 Q10–14, p.85 Q15–19, p.86 Q20–24, p.87 Q25–29, p.88 Q30–34, p.89 Q35–39, p.90 Q40–44, p.91 Q45–49, p.92 Q50–54. Column ③ p.93.
- N4 問題5 (用法, the headword is given and the four options are full sentences): p.94 Q1–4, p.95 Q5–9, p.96 Q10–14, p.97 Q15–19, p.98 Q20–24, p.99 Q25–26.
- N4 文法 問題1: p.100 Q1–7, p.101 Q8–17, p.102 Q18–23, p.103 Q24–29, p.104 Q30–35, p.105 Q36–41, p.106 Q42–48, p.107 Q49–54, p.108 Q55–61, p.109 Q62–64.
- N4 文法 問題2: p.110 instructions + れい only; p.111 Q1–12, p.112 Q13–23, p.113 Q24–34, p.114 Q35–45, p.115 Q46–56, p.116 Q57–67, p.117 Q68–78, p.118 Q79–84. Column ④ p.119.
- N4 文法 問題3: 1ばん [1]–[5], 2ばん [1]–[4], 3ばん [1]–[5] on p.120–124. Column ⑤ p.125.
- N4 読解 問題5: [1] p.130–131 (問1–3), [2] p.132–133 (問1–3), [3] p.134–135 (問1–3), [4] p.136–137 (問1–4). 問題6: [1] p.138–141, [2] p.142–143, [3] p.144–145 (問1–2 each).
- Columns: ① p.33 → n5-dokkai-1 · ② p.51 → n5-choukai-1 · ③ p.93 → n4-moji-goi-13 · ④ p.119 → n4-bunpou-7 · ⑤ p.125 → n4-bunpou-8. Read the upside-down answer line by rotating the crop 180°.

---

## 4. Answer key — official, answers only

**別冊 解答 p.2–7 (PDF 228–233).** Answers only, no explanations. Read at 130 dpi.

- p.2 (PDF 228): 第1部 N5 言語知識 もんだい1–4; 文法・読解 もんだい1–6
- p.3 (PDF 229): 第1部 N5 聴解 もんだい1–4; 第1部 N4 問題1–3
- p.4 (PDF 230): 第1部 N4 問題4–5; 文法 問題1–2
- p.5 (PDF 231): 第1部 N4 文法 問題3; 読解 問題4–6; 聴解 問題1–4; 第2部 N5 文字・語彙 もんだい1–4
- p.6 (PDF 232): 第2部 N5 文法・読解 もんだい1–6; 聴解 もんだい1–4; 第2部 N4 文字・語彙 問題1–3
- p.7 (PDF 233): 第2部 N4 文字・語彙 問題4–5; 文法・読解 問題1–6; 聴解 問題1–4

**★ (ことばの順番) answers are given as the full order with the star**, e.g. `[1] 3→2→★4→1`. The answer to the question is the number after ★; quote the full order in the Why note so the learner can rebuild the sentence.

Transcribed so far (checked at 130 dpi). Add each block here when its unit is built.

| Block | Answers |
|---|---|
| 第1部 N5 もんだい1 (p.12) | 1-1 2-4 3-2 4-3 5-2 6-1 7-4 8-4 9-3 10-4 11-2 12-2 13-1 14-3 15-4 16-2 17-2 18-4 19-4 20-2 |
| 第1部 N5 もんだい2 (p.14) | 1-4 2-3 3-2 4-1 5-2 6-1 7-1 8-4 9-2 10-3 11-1 12-3 13-1 14-3 15-1 |
| 第1部 N5 もんだい3 (p.16) | 1-1 2-1 3-2 4-2 5-3 6-4 7-1 8-2 9-2 10-4 11-3 12-4 13-1 14-1 15-3 16-3 17-1 18-4 |
| 第1部 N5 もんだい4 (p.18) | 1-3 2-4 3-1 4-1 5-3 6-2 7-1 8-3 9-2 10-1 |

Never change an answer. If one looks wrong, keep the book's answer and flag it in the Why note.

### 聴解スクリプト (scripts) — for our reference only, never reproduced

| Block | 別冊 pages | PDF |
|---|---|---|
| 第1部 N5 聴解 もんだい1–4 | p.8–12 | 234–238 |
| 第1部 N4 聴解 問題1–4 | p.13–18 | 239–244 |
| 第2部 N5 聴解 もんだい1–4 | p.19–23 | 245–249 |
| 第2部 N4 聴解 問題1–4 | p.24–29 | 250–255 |

Each 問題 starts with a box "もんだい N (p.XX)" naming the question page; a box can sit mid-page or in the right column. Speakers are marked M (男の人) / F (女の人). Scripts have furigana (read at 150 dpi). The script also gives the れい (example) and its answer.

### Audio track map

Cite as "CD1 · Track N" / "CD2 · Track N" with the `<span class="ld-track">CD1, Track 3</span>` badge. Track numbers are printed in the CD badge beside each ばん and in the 別冊 script.

| Block | Instructions + れい | Item tracks |
|---|---|---|
| CD1 Track 1 | opening (no printed badge) | — |
| 第1部 N5 もんだい1 | CD1 02 | 1–8ばん = 03–10 |
| 第1部 N5 もんだい2 | CD1 11 | 1–7ばん = 12–18 |
| 第1部 N5 もんだい3 | CD1 19 | 1–7ばん = 20–26 |
| 第1部 N5 もんだい4 | CD1 27 | 1–6ばん = 28–33 |
| CD1 Track 34 | no printed badge (between N5 and N4; probably a section announcement) | — |
| 第1部 N4 問題1 | CD1 35 | 1–9ばん = 36–44 |
| 第1部 N4 問題2 | CD1 45 | 1–7ばん = 46–52 |
| 第1部 N4 問題3 | CD1 53 | 1–5ばん = 54–58 |
| 第1部 N4 問題4 | CD1 59 | 1–8ばん = 60–67 |
| CD2 Track 1 | opening (no printed badge) | — |
| 第2部 N5 もんだい1 | CD2 02 | 1–8ばん = 03–10 |
| 第2部 N5 もんだい2 | CD2 11 | 1–7ばん = 12–18 |
| 第2部 N5 もんだい3 | CD2 19 | 1–7ばん = 20–26 |
| 第2部 N5 もんだい4 | CD2 27 | 1–6ばん = 28–33 |
| CD2 Track 34 | no printed badge (probably a section announcement) | — |
| 第2部 N4 問題1 | CD2 35 | 1–8ばん = 36–43 |
| 第2部 N4 問題2 | CD2 44 | 1–7ばん = 45–51 |
| 第2部 N4 問題3 | CD2 52 | 1–5ばん = 53–57 |
| 第2部 N4 問題4 | CD2 58 | 1–8ばん = 59–66 |

**Misprint:** on p.190 (第2部 N5 もんだい4) and p.222 (第2部 N4 問題4) the item badges say **CD①** although the instructions badge on the same page says CD② and the numbers continue the CD2 sequence. They are CD2 tracks (CD1 28–33 and 59–66 are 第1部 items). Cite them as CD2 and add a one-line note on the page.

---

## 5. Delivery

- Pages live in `n4/multi-skill/goukaku-dekiru/`, at depth 3. Assets are `../../../assets/...`. Breadcrumb links: `../../../index.html`, `../../../n4/index.html`, `../../../n4/multi-skill.html`, then the course hub `index.html`.
- The course is filed under **N4** on the site even when a unit is N5 material. Use the **N4 chrome** on every page: `body class="level-page n4"`, the N4 `level-nav` (`lv-n4`, All-in-one active, no Textbooks link), and the N4 active link in the main nav. Copy the chrome exactly from `n5-moji-goi-1.html`.
- Breadcrumb: Home / JLPT N4 / All-in-one / 合格できる N4・N5 / <unit short title>.
- `.bp-week` says which level the material is, e.g. "JLPT N4 · All-in-one · 合格できる N4・N5 — 第1部 練習問題 N5 言語知識（文字・語彙）".
- `.bp-day-nav`: prev = previous unit in table order (unit 1 links back to the hub), next = next unit (unit 50 links back to the hub). Label both with the chip title. If the next unit is not built yet, write `<span>Next: … — coming soon</span>` (no dead link); when you build a unit, turn the previous unit's "coming soon" span into a link.
- Reuse existing classes only (`.bp-header`, `.bp-meta-grid`, `.bp-points`, `.bp-note`, `.bp-section-title`, `.vd-table-wrap`/`.vd-wordlist`, `.bp-quiz`, `.q-label`, `.q-jp`, `.q-translations`, `.bp-options` with `tr.correct`, `.bp-why`, `.bp-point`, `.bp-confusion`, `.bp-callout`, `.bp-notes`, `.ld-track`, `.bp-day-nav`). Do not edit the CSS or JS.
- **Hub update rule** (`index.html`): every unit is one chip in one of nine `.week-block`s (第1部 N5 文字・語彙 / 文法 / 読解 / 聴解; 第1部 N4 文字・語彙 / 文法 / 読解・聴解; 第2部 N5; 第2部 N4). When a unit is built, change `<span class="day-chip soon" data-href="FILE.html">LABEL</span>` to `<a class="day-chip ready" href="FILE.html">LABEL</a>` and update `<strong>In progress — N of 50 units built</strong>`. When N = 50, change it to `Complete — 50 of 50 units built` with the ✅ icon, as in the Tanki Master hubs.
- Do not touch `n4/multi-skill.html` or other hub pages; the book card there is regenerated by the site build.

## 6. Page format (every unit)

### Header block
- `.bp-week` as above. `h1` = 問題 numbers and the book's section title, plus romaji and an English gloss with the question count.
- Meta grid:
  - **Source**: book, 第1部/第2部, level, section, printed pp (PDF pp), Q range.
  - **Words tested / Patterns tested / Question types**: chips (`.bp-points`).
  - **Answer key**: "Official, answers only — 別冊 解答 p.N (PDF M)", then the full answer string for the unit.
  - **Notes**: the book has no explanations, so the tables, translations, Why notes and confusion section are ours; for N5 material filed under N4, say it is the N5 half of the book; for 聴解, the audio note (copyrighted CD, not published, play your own copy by track number).

### Section 1 — Key Words / Key Patterns / Text overview
- 文字・語彙 units: **Key Words** table (`.vd-wordlist`: Japanese + romaji, EN, HI, GU, Note) of the correct answer of every question, with other common readings of the kanji in the Note.
- 文法 units: **Key Patterns** table: each tested pattern, its form (connection), meaning EN/HI/GU and one short example with romaji + EN/HI/GU (added, not in book).
- 読解 units: a **text overview** table: text number, type (letter, notice, memo…), 2–3-line summary in EN/HI/GU, and the questions it carries. Words to know for the texts (Japanese + romaji + EN/HI/GU).
- 聴解 units: **question-type explanation** (what the task asks, where the answer comes in the talk) and a list of key words heard in the scripts.

### Section 2 — Quiz / Exercise Section
- One `.bp-quiz` per question, in book order, with the book's instruction line first (Japanese + romaji + EN/HI/GU).
- Each question: `.q-label` (e.g. "もんだい1 Q3", "問題2 Q14", "総復習 [27]"), the sentence with the tested part in `<u>` and romaji, `.q-translations` EN/HI/GU, a `.bp-options` table (Option / Japanese + romaji / English / Hindi / Gujarati) with the book's answer row `class="correct"` and ✓, then `.bp-why`.
- **★ (ことばの順番)**: show the four pieces, then the full correct sentence with romaji + EN/HI/GU and the order from the key ("3→2→★4→1"); the answer is the ★ piece.
- **文章の中のことば**: do not reproduce the passage. Summarise it in 2–3 sentences (EN/HI/GU), then for each blank quote only the sentence with the blank.
- **読解**: do not transcribe the texts. Summarise each text (EN/HI/GU) and quote only the one or two short sentences a question needs. Information-search tables (prices, timetables) may be described as a small table of the facts the question needs, in our own layout.
- **聴解**: `.ld-track` badge on each item. Describe picture options in words ("Picture 1: a vase of flowers on a table"). Summarise the conversation in 2–3 lines (EN/HI/GU) and quote only the key line that decides the answer. 即時応答 options exist only in the audio and the script; give each reply as a short one-line paraphrase with romaji + EN/HI/GU (short replies may be quoted, as in the Tanki Master N5 pages). Never write out a full script.
- Columns: a final `.bp-quiz` group "Column これが たいせつ！ ①" with each item, the answer printed upside down on the page (cite "answer printed on p.N"), and a short Why.

### Section 3 — Confusion Pairs / Nuance Notes
- `.bp-point` with one or two `.bp-confusion` tables (Form + romaji / Meaning / Key difference / Use when) built from the traps in this unit, plus one `.bp-callout` "Exam trap" box. All labelled "(added, not in book)".

### Footer nav
- `.bp-day-nav` as in §5.

## 7. Hard rules

- **Romaji on every Japanese line**: questions, options, words, patterns, quoted lines, confusion forms (`<span class="romaji">`).
- **EN + Hindi + Gujarati** for every meaning, example, question and option. Simple English; N5 units are for beginners.
- **Every question with the book's answer**, citing 別冊 p.N (PDF M). Never change an answer. If a question ever has no key entry, give a worked answer labelled "(our answer, not in book)".
- Anything we add that is not from the book is labelled "(added, not in book)".
- **No long passages or scripts.** Summarise; quote only short key lines.
- **Never publish or link audio.** Track numbers only.
- **Never embed the book's pictures.** Describe them in words.
- No emoji glyphs in body text (✓ in the correct option row and the hub's status icon are the only symbols used).
- Do not edit CSS, JS, `tools/`, other courses or hub pages. Do not run `build_site.py` or git from a unit task.

## 8. Checks before finishing a unit

- Every answer matches the 別冊 grid at 130 dpi (and the table in §4).
- No passage or script reproduced beyond the quoted lines. No audio links, no images.
- Tags balance (Python `html.parser`), all relative links resolve, the file ends with `</html>`.
- Hub chip flipped and `In progress — N of 50 units built` updated; previous unit's "coming soon" next-link turned into a link.

---

**Reference implementation:** `n4/multi-skill/goukaku-dekiru/n5-moji-goi-1.html` (第1部 N5 もんだい1 漢字の読み方, 20 questions), built 2026-10-08.
