# 20日で合格 N1 文字・語彙・文法 — day-by-day processing guide

Standing instructions for turning `20_Nichi_Goukaku_N1-Moji.Goi.Bunpou.pdf` (日本語能力試験 20日で合格 N1 文字・語彙・文法［改訂版］, 国書日本語学校 編, 国書刊行会, 2012) into the site's study pages. Give a day number (e.g. "第7日") and this is the process to follow.

This is a **multi-skill drill book** (kanji reading + vocabulary + grammar in one test set). It adapts three master specs — everything in them still applies (site chrome, CSS classes, three required sections, EN/HI/GU, romaji) **except** where this file says otherwise:
- vocabulary: [`../../vocabulary/PROCESSING-GUIDE.md`](../../vocabulary/PROCESSING-GUIDE.md) (word-list table format)
- grammar: [`../../grammar/PROCESSING-GUIDE.md`](../../grammar/PROCESSING-GUIDE.md) (quiz / options / Why / confusion format)
- ★ ordering + passage cloze layout: `n1/grammar/drill-and-drill/bun2-01.html`, `n1/grammar/shin-kanzen-master/mock-test-1.html` (but see §6 — **no full passages**)

**Reference implementation:** [`n1/multi-skill/20-nichi-de-goukaku/day-01.html`](../../../../n1/multi-skill/20-nichi-de-goukaku/day-01.html) (第1日 一期一会).

---

## 1. What the book is

- 161 PDF pages. The PDF **has a text layer** (OCR, Shift-JIS-ish — read it with PyMuPDF `page.get_text()` and write it to a UTF-8 file; never print it straight to the Windows console, it mojibakes). The OCR is noisy: question numbers come out as 巨□/匝ヨ, ・ becomes 0, small っ/ゃ are often dropped (とどこおつて). **Always confirm against a rendered image** (`doc[i-1].get_pixmap(dpi=120)`) — especially underlined target words, ★ position and furigana, which the text layer loses.
- No explanations at all — only questions and a bare answer list. Every meaning, translation, "Why" and confusion note on our pages is ours.
- **Unit = one 日 (day).** 20 days, **8 printed pages per day, 45 questions per day, always the same layout** (from 本書の使い方, PDF 5):

| Page of the day | Content | Questions |
|---|---|---|
| 1 | 第N日 title banner (a number idiom + the book's English gloss) + 問題1 漢字読み | 1–6 (3 verbs + 3 nouns) |
| 2 | 問題2 文脈規定 (choose the word for the blank) | 7–13 (7–11 two-kanji words, 12–13 three-kanji compounds) |
| 3 | 問題3 言い換え類義 (closest meaning) + start of 問題4 用法 | 14–19, 20 |
| 4 | 問題4 用法 (which sentence uses the word correctly) | 21–25 |
| 5 | 問題5 文の文法1 (fill the blank, 機能語) | 26–33 |
| 6 | 問題5 cont. + 問題6 文の文法2 (★ ordering, 名詞＋助詞中心) | 34–35, 36–40 |
| 7–8 | 問題7 文章の文法 (cloze on a newspaper article) | 41–45 (one blank is split a/b) |

- Day title banners: 第1日 一期一会 · 2 二足の草鞋 · 3 三度目の正直 · 4 四苦八苦 · 5 五里霧中 · 6 一の裏は六 · 7 七不思議 · 8 八面六臂 · 9 九死に一生を得る · 10 *(title page missing from scan)* · 11 一世を風靡する · 12 二兎を追う者は一兎をも得ず · 13 三つ子の魂百まで · 14 四面楚歌 · 15 五本の指に入る · 16 六日の菖蒲十日の菊 · 17 *(title page missing from scan)* · 18 十八番 · 19 九牛の一毛 · 20 十年一日の如く. Each banner also prints an English gloss (e.g. 一期一会: "a once-in-a-lifetime chance") — quote it and add HI/GU.
- 問題5/6 sentences carry a theme per day; 問題7 is always a newspaper article (source + date printed under the passage, e.g. 「朝日新聞」2010年2月15日付).
- There is **no mock test** and no grammar/vocab explanation section.

## 2. Front/back matter and scan quirks

| PDF | Content |
|---|---|
| 1 | blank / cover |
| 2 | title page (国書日本語学校) |
| 3 | blank |
| 4 | はじめに |
| 5 | 本書の使い方 (question-type breakdown, see §1) |
| 6 | 目次 (TOC: 第1日 p.6 … 第20日 p.158; "※この問題集には別冊解答がついています") |
| 7–146 | days 1–20 (with gaps, see §3) |
| 147 | blank |
| 148 | 執筆者紹介 + colophon |
| 149 | publisher's ad (another book) |
| 150 | 別冊 解答 cover |
| 151–160 | **answer key** (2 days per page) |
| 161 | back cover |

- Every page carries a scanner watermark "facebook.com/duytrieuftu" in the top-right corner — ignore it, never reproduce it.
- Some pages have a previous owner's handwriting (e.g. PDF 8: "9/6: 24/45" — a self-score). Ignore; it is not book content.

## 3. Verified page offsets — they DRIFT (pages are missing from the scan)

The scan is missing several 2-page spreads, so **the offset changes**. Every row below was checked against the printed page number stamped on the rendered page (PDF 7 = p.6, 8 = 7, 14 = 13, 66 = 65, 67 = 68, 71 = 76, 73 = 80, 77 = 86, 79 = 92, 83 = 98, 115 = 132, 117 = 136, 139 = 158; one OCR misread: PDF 49 is stamped 48, the OCR says "43").

| Printed pages | PDF = printed + | Missing before this run |
|---|---|---|
| 6–65 | +1 | — |
| 68–71 | −1 | p.66–67 |
| 76–77 | −3 | p.72–75 |
| 80–83 | −7 | p.78–79 |
| 86–87 | −9 | p.84–85 |
| 92–95 | −13 | p.88–91 |
| 98–129 | −15 | p.96–97 |
| 132–133 | −17 | p.130–131 |
| 136–165 | −19 | p.134–135 |

## 4. Unit table

Day N's printed pages = 6 + 8(N−1) … 13 + 8(N−1). Answer key: day N is on PDF 150 + ⌈N/2⌉ (odd day = left column, even day = right column); each column header prints 第N日 + the printed page range, which matches the TOC.

| File | Title | Printed pp | PDF pp | Answer-key PDF p | Missing from scan |
|---|---|---|---|---|---|
| day-01.html | 第1日 一期一会 | 6–13 | 7–14 | 151 (left) | — |
| day-02.html | 第2日 二足の草鞋 | 14–21 | 15–22 | 151 (right) | — |
| day-03.html | 第3日 三度目の正直 | 22–29 | 23–30 | 152 (left) | — |
| day-04.html | 第4日 四苦八苦 | 30–37 | 31–38 | 152 (right) | — |
| day-05.html | 第5日 五里霧中 | 38–45 | 39–46 | 153 (left) | — |
| day-06.html | 第6日 一の裏は六 | 46–53 | 47–54 | 153 (right) | — |
| day-07.html | 第7日 七不思議 | 54–61 | 55–62 | 154 (left) | — |
| day-08.html | 第8日 八面六臂 | 62–69 | 63–68 | 154 (right) | p.66–67 → Q26–40 (問題5, 問題6) |
| day-09.html | 第9日 九死に一生を得る | 70–77 | 69–72 | 155 (left) | p.72–75 → Q14–40 (問題3–6) |
| day-10.html | 第10日 | 78–85 | 73–76 | 155 (right) | p.78–79 → Q1–13 (title, 問題1–2); p.84–85 → Q41–45 (問題7) |
| day-11.html | 第11日 一世を風靡する | 86–93 | 77–80 | 156 (left) | p.88–91 → Q14–40 (問題3–6) |
| day-12.html | 第12日 二兎を追う者は一兎をも得ず | 94–101 | 81–86 | 156 (right) | p.96–97 → Q14–25 (問題3–4) |
| day-13.html | 第13日 三つ子の魂百まで | 102–109 | 87–94 | 157 (left) | — |
| day-14.html | 第14日 四面楚歌 | 110–117 | 95–102 | 157 (right) | — |
| day-15.html | 第15日 五本の指に入る | 118–125 | 103–110 | 158 (left) | — |
| day-16.html | 第16日 六日の菖蒲十日の菊 | 126–133 | 111–116 | 158 (right) | p.130–131 → Q26–40 (問題5, 問題6) |
| day-17.html | 第17日 | 134–141 | 117–122 | 159 (left) | p.134–135 → Q1–13 (title, 問題1–2) |
| day-18.html | 第18日 十八番 | 142–149 | 123–130 | 159 (right) | — |
| day-19.html | 第19日 九牛の一毛 | 150–157 | 131–138 | 160 (left) | — |
| day-20.html | 第20日 十年一日の如く | 158–165 | 139–146 | 160 (right) | — |

PDF detail for the gappy days: day 8 = PDF 63–66 (p.62–65) + 67–68 (p.68–69); day 9 = PDF 69–70 (p.70–71) + 71–72 (p.76–77); day 10 = PDF 73–76 (p.80–83); day 11 = PDF 77–78 (p.86–87) + 79–80 (p.92–93); day 12 = PDF 81–82 (p.94–95) + 83–86 (p.98–101); day 16 = PDF 111–114 (p.126–129) + 115–116 (p.132–133); day 17 = PDF 117–122 (p.136–141).

## 5. Answer key status

**Official and complete** — the 別冊 解答 (PDF 151–160) lists all 45 answers for all 20 days, *including the questions whose pages are missing from the scan*. It gives the option number only (for 問題6 the ★ tile only; for 問題7 one number per blank, the split blank 42-a/b counts as one item). No explanations. Read it at ≥120 dpi; the text layer of these pages is unusable (□/回/国 noise). Cite as "別冊 解答 PDF 151 (第1日 column)".

For **missing questions**: list the official answer numbers in the header ("Q26–40 answers from the key: 26-x, 27-y …") and put a single note in §2 for that block — "*Pages p.66–67 (問題5 Q26–33, 問題5/6 Q34–40) are missing from this scan; the questions cannot be shown.*" Never reconstruct or invent the missing question text or options.

## 6. Page format (one file per day)

Location `n1/multi-skill/20-nichi-de-goukaku/day-NN.html` (two-digit, zero-padded). Depth 3: assets `../../../assets/...`, N1 home `../../index.html`, module hub `../../multi-skill.html`, book hub `index.html`. Copy the chrome (head with `auth.js` first, favicon, Noto Sans JP, `style.css` + `day-page.css`, `body.level-page.n1`, header/nav, footer, `main.js`) exactly from `day-01.html`.

Breadcrumb: Home / JLPT N1 / All-in-one (`../../multi-skill.html`) / 20日で合格 N1 文字・語彙・文法 (`index.html`) / 第N日.

### Header (`.bp-header`)
`bp-week` = "JLPT N1 · All-in-one · 20日で合格 N1 文字・語彙・文法 — 第N日"; `h1` = "第N日 — <title idiom>" + romaji + the book's English gloss. Meta grid: **Source** (printed pp + PDF pp + stamps checked), **Covers** (chips: 問題1 漢字読み 1–6 · 問題2 文脈規定 7–13 · 問題3 言い換え類義 14–19 · 問題4 用法 20–25 · 問題5 文の文法1 26–35 · 問題6 文の文法2 ★ 36–40 · 問題7 文章の文法 41–45), **Answer key** (all 45 numbers in compact form, "official, 別冊 PDF n; no explanations — every Why is ours"; for ★ say full orders are reasoned to fit the official tile), **Notes** (title idiom meaning in EN/HI/GU, missing pages, newspaper source of 問題7, print quirks).

### §1 Points — words, kanji and grammar for the day
1. **Kanji readings (問題1)** — `.vd-wordlist` table: Word (kanji + romaji) / Reading / English / Hindi / Gujarati / Note (on-/kun-yomi, the distractor readings and why they're wrong in one phrase, look-alike kanji).
2. **Vocabulary (問題2–4)** — `.vd-wordlist`: every target word (問題2 correct answers as the full compound, 問題3 underlined word + the correct paraphrase, 問題4 headwords) with EN/HI/GU and a Note column (collocation, ⇔, synonym). Mark katakana words (問題4 always has one or two).
3. **Grammar (問題5–7)** — one `.bp-table` (Item / Pattern / Meaning EN / HI / GU / Connection), like the summary table in `shin-kanzen-master/mock-test-1.html`. Add a full `.bp-point` (field table + formation table + examples) only for the 2–4 genuinely N1 patterns of the day (e.g. 〜ごとき, 〜わ〜わ, 〜ずにいる); formation cells and examples not in the book are `(added, not in book)`.

### §2 Quiz / Exercise — every question that exists in the scan
Section headings `問題1 — 漢字読み (1–6)` etc., each with the instruction line + romaji + English. Each question is a `.bp-quiz`:
- `q-jp` sentence with the target shown as `<u>…</u>` (問題1/3) or （　） (問題2/5) + romaji;
- "Full sentence" (completed) + EN / HI / GU;
- `.bp-options` table (Option / Japanese / English / Hindi / Gujarati; for 問題1 the "English" column = what the reading would be / mean), `tr.correct` on the 別冊 answer;
- `.bp-why`: why the answer is right, why each distractor fails.
- **問題4 用法**: four full sentences as options — table columns Option / Japanese sentence / EN / HI / GU; Why explains the misuse in each wrong sentence (what word would be correct there).
- **問題6 ★**: stem with `＿＿＿ ＿＿＿ ＿★＿ ＿＿＿`, tiles line, `.bp-order-chain`, `.bp-assembled` + romaji, EN/HI/GU, options table, Why. The 別冊 gives only the ★ tile — say the full order is reasoned.
- **問題7**: `.rd-passage-label` + a `.bp-point` with **"Passage summary (not the book's text)" — 2–3 sentences in EN/HI/GU in our own words** and the source line. **Never reproduce the article.** Then one `.bp-quiz` per blank quoting **only the sentence containing the blank** (split blanks a/b in one quiz).

### §3 Confusion Pairs / Nuance Notes
`.bp-confusion` (Form / Meaning / Connection or reading / Key difference / Use when) mixing the day's best traps: look-alike readings (懲りる/降りる), the 問題2 compound sets (検診/検事/検挙), the 問題3/4 near-synonyms, and the 問題5 grammar distractor sets (ずにいる/ざるを得ない/ずにはおかない). Plus 1–3 `.bp-callout` exam traps.

### Nav
`.bp-day-nav`: prev = previous day (day 1 → `index.html`), next = next day (day 20 → `index.html`), labelled "← Prev: 第N日 title" / "Next: 第N日 title →".

## 7. Content rules

- EN + Hindi + Gujarati for every meaning, example and question sentence; `<span class="romaji">` under every Japanese line (questions, options, tiles, table words).
- **No long passages**: 問題7 gets a summary + the blank sentences only (the API content filter blocks long verbatim text; if anything is blocked, leave it out and report it).
- Never invent questions or answers. Missing pages are marked as missing; answers for them come only from the key.
- Anything we add (example sentences, formation cells) is labelled "(added, not in book)".

## 8. Hub update rule

`index.html` has four `.week-block`s (第1日–第5日, 第6日–第10日, 第11日–第15日, 第16日–第20日). Built: `<a class="day-chip ready" href="day-NN.html">第N日 title</a>`; not built: `<span class="day-chip soon" data-href="day-NN.html">…</span>`. Update the `.sample-note` text `In progress — N of 20 units built`.

## 9. Checks before finishing a day

- All 45 answers re-read from the 別冊 image (numbers are easy to misread).
- Every ★ order actually places the official tile in the ★ slot (the ★ is usually the 3rd blank, but check the image).
- Balanced tags (Python `html.parser`), all relative links resolve, file ends with `</html>`, hub chip + count updated.

## Notes from the build (coordinator)
- **問題7 split blanks:** some days have two split blanks (Day 6 and Day 9: 43-a/b and 45-a/b), others one (42-a/b); the key gives one number per split blank.
- **Partial days (pages missing from the scan):** 8, 9, 10, 11, 12, 16, 17 — missing questions are marked "page missing from the source scan" with the key's answer numbers only; never rebuild them.
- **Titles missing:** Day 10 and Day 17 title pages are not in the scan; their h1 is just 第N日.
- **★:** in every day the ★ is the 3rd blank (the scan prints a hollow ☆).

