# 試験に出る文法と表現 N1・N2 — unit-by-unit processing guide

Standing instructions for turning `Shiken_ni_Deru_N1_N2-Bunpou.pdf` (日本語能力試験 N1・N2 試験に出る文法と表現 42日完成, 桐原書店, 2010) into the site's grammar pages under `n1/grammar/shiken-ni-deru/`. Give a unit id (e.g. "第5日", "第2章 まとめ", "N1 第1回") and follow this process.

This guide adapts the master spec [`book-source/n1/grammar/PROCESSING-GUIDE.md`](../PROCESSING-GUIDE.md). Everything in the master spec (page chrome, `bp-*` classes, three required sections, EN + Hindi + Gujarati, romaji, "(added, not in book)" marking) applies unless overridden here.

**Level note:** the book covers **both N1 and N2**. Items marked with an **N1** tag in the book's left column are N1-level; untagged items are N2-level (or shared N2/N1). Show this on each grammar point (badge text "N1" or "N2-level"). The N2 模擬試験 are still built, labelled "N2-level", because the book lives in the N1 module.

---

## 1. The PDF

- 252 PDF pages. **PDF 1–165 = the main book; PDF 166–252 = the 別冊 (separate answer + translation booklet), scanned into the same PDF.**
- **No usable text layer.** `page.get_text()` returns only the watermark `http://riyuxuexi.taobao.com/` on every page. Read everything visually: render with PyMuPDF (`import pymupdf`; `page.get_pixmap(dpi=200, clip=...)`). Cropping each page into top/middle/bottom thirds at ~200 dpi makes furigana legible. Ignore the watermark URL.
- **Offset (main book): PDF page = printed page number (offset 0).** Verified by reading the printed page stamp on rendered images at PDF 2, 6–9, 12, 13, 22, 26, 33, 38, 58, 98, 109, 118, 129, 135, 144, 155, 160. No drift.
- **Offset (別冊): PDF page = 別冊 printed page + 166.** PDF 166 = 別冊 cover, 167 = 別冊 もくじ, 168 = 別冊 p.2, …, 174 = 別冊 p.8, 176 = 別冊 p.10.
- Blank page: p.130. Chapter title pages (no content, not units): pp.11, 27, 41, 47, 59, 65, 77, 91, 103, 111, 119, 123, 131; 模擬試験 title p.143. さくいん (index) pp.160–165 is not a unit. Front matter pp.2–5 (はじめに, exam format explanation) and もくじ pp.6–9 are not units.

## 2. Answer keys

- All 練習問題, まとめの問題 and 模擬試験 answers are in the **別冊 解答 section, PDF 168–174 (別冊 pp.2–8)**. Each exercise header in the main book says where, e.g. 「(解答は別冊2ページ)」.
  - 別冊 pp.2–7 (PDF 168–173): 練習問題 by day number (headed "1 練習問題", "2 練習問題", …) and each chapter's まとめの問題, grouped under 第N章.
  - 別冊 p.8 (PDF 174): 模擬試験 answers (N2 第1回・第2回, N1 第1回・第2回).
- **基本文法 / その他の基本文法 columns print their own 解答** on the same page (bottom 解答 box on pp.26, 40, 76, 90; inline 「(解答 …)」 on pp.102, 129). The p.58 page (「〜たらすぐ」という意味を表す言葉のつづき) is a worked-correction page: model sentences are printed with the wrong versions struck through — no separate key.
- 別冊 PDF 175–252 (別冊 p.9 onward) = 主要例文 中国語・韓国語訳: Chinese/Korean translations of the first example of each item (those examples carry a superscript running number, e.g. 「…寄せられた。¹」). Useful only to double-check a meaning; not reproduced on the site.
- Always cite the 別冊 page + PDF page in the unit header. Never guess: every exercise in this book has an official key.

## 3. What a unit is

One page on the site per unit, in book order:

| Unit type | What it contains | File name |
|---|---|---|
| 第N日 (days 1–42) | grammar tables + 練習問題 (+ メモ box) — usually 2 printed pages; 第40日 is 5, 第41日 is 4, 第42日 is 7 | `day-NN.html` (`day-01` … `day-42`) |
| 第N章 まとめの問題 | chapter review, 4-choice items, 1 or 2 pages. Chapters 12 and 13 have none. §1 on these pages is a **review map** table linking each item to the day page that teaches it (see `matome-ch02.html`) | `matome-chNN.html` |
| Column (基本文法 / その他の基本文法 / p.58 つづき) | 1-page review column with its own answers | `column-NN.html` (`column-01` … `column-07`) |
| 模擬試験 | 4-page mock test (問題1 4-choice, 問題2 ★ sentence building, 問題3 文章の文法) | `mogi-n2-1.html`, `mogi-n2-2.html`, `mogi-n1-1.html`, `mogi-n1-2.html` |

**Columns are their own units** (not folded into the preceding day): they review basic grammar unrelated to the preceding day's points and carry a self-contained exercise + key. The p.58 column extends 第12日 (it says 「p.42参照」) but sits physically in Chapter 4, so it is grouped with Chapter 4 on the hub and its header links back to 第12日.

## 4. Full unit table

Printed pp = PDF pp throughout (offset 0). Answer key = PDF page(s).

| # | Unit | Title | Printed pp | PDF pp | Answer key (PDF) | File |
|---|---|---|---|---|---|---|
| | **第1章** | **助詞の働きをする言葉** | 11 (title) | | | |
| 1 | 第1日 | 〜に関して、〜に対して、〜について、〜をめぐって、〜によって など | 12–13 | 12–13 | 168 (別冊 p.2) | day-01.html |
| 2 | 第2日 | 〜にとって、〜として、〜に応じて、〜にこたえて、〜に沿って、〜に代わって、〜に比べて、〜に加えて、〜に反して | 14–15 | 14–15 | 168 | day-02.html |
| 3 | 第3日 | 〜において、〜にあたって、〜に基づいて、〜に即して、〜にしたがって、〜につれて、〜に伴って、〜に伴う、〜とともに | 16–17 | 16–17 | 168 | day-03.html |
| 4 | 第4日 | 〜あっての、〜とあって、〜とあれば、〜にあって、〜から…にかけて、〜にわたって、〜に至る、〜に至って、〜に至っては | 18–19 | 18–19 | 168 | day-04.html |
| 5 | 第5日 | 〜と相まって、〜をもって、〜を込めて、〜ときたら、〜はもちろん、〜はもとより、〜はおろか、〜というより、〜たりとも…ない | 20–21 | 20–21 | 168 | day-05.html |
| 6 | 第6日 | 〜を通じて、〜を通して、〜のもとで、〜にもまして、〜にかかわる、〜にかけては、〜にして、〜はともかく、〜とか | 22–23 | 22–23 | 168 | day-06.html |
| 7 | 第1章 まとめの問題 | 29 items | 24–25 | 24–25 | 168 | matome-ch01.html |
| 8 | 基本文法 | 変化表現 | 26 | 26 | 26 (on page) | column-01.html |
| | **第2章** | **「さえ、こそ、まで、ほど、のみ…」を使った言葉** | 27 (title) | | | |
| 9 | 第7日 | さえ、すら、こそ | 28–29 | 28–29 | 168 | day-07.html |
| 10 | 第8日 | くらい、ほど、まし | 30–31 | 30–31 | 168–169 | day-08.html |
| 11 | 第9日 | だけ、のみ | 32–33 | 32–33 | 169 | day-09.html |
| 12 | 第10日 | まで、〜どころ | 34–35 | 34–35 | 169 | day-10.html |
| 13 | 第11日 | ばかり、なんか、など、なんて、〜とは、ならでは | 36–37 | 36–37 | 169 | day-11.html |
| 14 | 第2章 まとめの問題 | 26 items | 38–39 | 38–39 | 169 | matome-ch02.html |
| 15 | 基本文法 | 自動詞、他動詞 | 40 | 40 | 40 (on page) | column-02.html |
| | **第3章** | **時を表す言葉** | 41 (title) | | | |
| 16 | 第12日 | 「〜たらすぐ」という意味を表す言葉 | 42–43 | 42–43 | 169 | day-12.html |
| 17 | 第13日 | 〜うちに、際、最中、以来 など | 44–45 | 44–45 | 169 | day-13.html |
| 18 | 第3章 まとめの問題 | 14 items | 46 | 46 | 169 | matome-ch03.html |
| | **第4章** | **「わけ、こと、もの、ところ」を使った言葉** | 47 (title) | | | |
| 19 | 第14日 | わけ、こと(1) | 48–49 | 48–49 | 169 | day-14.html |
| 20 | 第15日 | こと(2) | 50–51 | 50–51 | 169 | day-15.html |
| 21 | 第16日 | もの(1) | 52–53 | 52–53 | 169–170 | day-16.html |
| 22 | 第17日 | もの(2)、ところ | 54–55 | 54–55 | 170 | day-17.html |
| 23 | 第4章 まとめの問題 | 27 items | 56–57 | 56–57 | 170 | matome-ch04.html |
| 24 | Column | 「〜たらすぐ」という意味を表す言葉のつづき (extends 第12日) | 58 | 58 | 58 (model answers inline) | column-03.html |
| | **第5章** | **「よう、〜う／よう、まい、べき」を使った言葉** | 59 (title) | | | |
| 25 | 第18日 | 〜よう、〜べき、〜ごとき、〜たる者 | 60–61 | 60–61 | 170 | day-18.html |
| 26 | 第19日 | 〜まい、〜う／よう、〜ではあるまいし、あるまじき | 62–63 | 62–63 | 170 | day-19.html |
| 27 | 第5章 まとめの問題 | 15 items | 64 | 64 | 170 | matome-ch05.html |
| | **第6章** | **接続の言葉—その1** | 65 (title) | | | |
| 28 | 第20日 | 〜から言うと、〜からして、〜てからでないと、〜にしては、わりに など | 66–67 | 66–67 | 170 | day-20.html |
| 29 | 第21日 | 〜としたら、〜としても、〜にしても、〜にしろ、〜にせよ、〜であれ など | 68–69 | 68–69 | 170 | day-21.html |
| 30 | 第22日 | 〜からには、〜以上、〜ともなると、〜にひきかえ、〜もさることながら、なくして | 70–71 | 70–71 | 170 | day-22.html |
| 31 | 第23日 | 「限り」のつく言葉 | 72–73 | 72–73 | 170 | day-23.html |
| 32 | 第6章 まとめの問題 | 24 items | 74–75 | 74–75 | 170–171 | matome-ch06.html |
| 33 | 基本文法 | やる、あげる、もらう、くれる | 76 | 76 | 76 (on page) | column-04.html |
| | **第7章** | **接続の言葉—その2** | 77 (title) | | | |
| 34 | 第24日 | 上、上で、〜た末、あげく、〜というと、〜といえば、〜といったら | 78–79 | 78–79 | 171 | day-24.html |
| 35 | 第25日 | 〜からといって、〜といっても、〜とはいえ、〜といえども、ながら、〜つつ | 80–81 | 80–81 | 171 | day-25.html |
| 36 | 第26日 | 〜を問わず、〜にかかわらず、〜にもかかわらず、〜と思いきや、〜たが最後、〜たきり、〜につき | 82–83 | 82–83 | 171 | day-26.html |
| 37 | 第27日 | 一方、反面、〜ともなく、〜んがため、〜をよそに、〜もかまわず | 84–85 | 84–85 | 171 | day-27.html |
| 38 | 第28日 | 〜につけて、〜につけ…につけ、〜も…ば…も、〜やら…やら、〜といい…といい、〜なり…なり、〜つ…つ、〜ては | 86–87 | 86–87 | 171 | day-28.html |
| 39 | 第7章 まとめの問題 | 27 items | 88–89 | 88–89 | 171 | matome-ch07.html |
| 40 | 基本文法 | 受身、使役、使役受身 | 90 | 90 | 90 (on page) | column-05.html |
| | **第8章** | **主に文末に使われる言葉** | 91 (title) | | | |
| 41 | 第29日 | 〜ざるを得ない、しかない、ほかない、〜にすぎない、〜てしょうがない、〜てたまらない、〜てならない | 92–93 | 92–93 | 171 | day-29.html |
| 42 | 第30日 | 限りだ、〜に決まっている、〜に相違ない、〜に違いない など | 94–95 | 94–95 | 171 | day-30.html |
| 43 | 第31日 | 〜にほかならない、〜でなくてなんだろう、〜ずにはいられない、〜ずにはおかない、〜ずにはすまない、〜っけ、〜っこない | 96–97 | 96–97 | 171 | day-31.html |
| 44 | 第32日 | 〜てやまない、〜といったらない、〜にはあたらない、余儀なくされる、余儀なくさせる、〜をおいてない、〜つつある | 98–99 | 98–99 | 172 | day-32.html |
| 45 | 第8章 まとめの問題 | 25 items | 100–101 | 100–101 | 172 | matome-ch08.html |
| 46 | その他の基本文法① | particles, ということ, 〜ないといけない etc. | 102 | 102 | 102 (inline) | column-06.html |
| | **第9章** | **複合語として使われる言葉** | 103 (title) | | | |
| 47 | 第33日 | 〜得る、あり得る、〜がちだ、〜がたい、〜気味、〜げ、〜っぽい、〜めく | 104–105 | 104–105 | 172 | day-33.html |
| 48 | 第34日 | 〜かねる、〜かねない、〜きる、〜きれない、〜かける、〜かけだ | 106–107 | 106–107 | 172 | day-34.html |
| 49 | 第35日 | 〜っぱなし、〜ぬく、向き、向け、だらけ、まみれ、ずくめ | 108–109 | 108–109 | 172 | day-35.html |
| 50 | 第9章 まとめの問題 | 15 items | 110 | 110 | 172 | matome-ch09.html |
| | **第10章** | **名詞を使った言葉** | 111 (title) | | | |
| 51 | 第36日 | 一方だ、おかげだ、せいだ、故、とおりだ、始末だ | 112–113 | 112–113 | 172 | day-36.html |
| 52 | 第37日 | おそれがある、きらいがある、代わりに、くせに、なりに、あまり、ぬきで | 114–115 | 114–115 | 172 | day-37.html |
| 53 | 第38日 | 次第だ、いかんだ、かたわら、ついでに、かたがた、がてら | 116–117 | 116–117 | 172 | day-38.html |
| 54 | 第10章 まとめの問題 | 15 items | 118 | 118 | 172 | matome-ch10.html |
| | **第11章** | **〜を…として／にして** | 119 (title) | | | |
| 55 | 第39日 | 〜を…として／にして | 120–121 | 120–121 | 172–173 | day-39.html |
| 56 | 第11章 まとめの問題 | 6 items | 122 | 122 | 173 | matome-ch11.html |
| | **第12章** | **敬語** | 123 (title) | | | |
| 57 | 第40日 | 敬語 | 124–128 | 124–128 | 173 | day-40.html |
| 58 | その他の基本文法② | 〜ていた／なかったら, 〜ところだ, 〜なければ etc. | 129 (p.130 blank) | 129 | 129 (inline) | column-07.html |
| | **第13章** | **新出題形式の問題** | 131 (title) | | | |
| 59 | 第41日 | 「文の組み立て」形式の問題 (N2レベル 14 + N1レベル 16 ★ items) | 132–135 | 132–135 | 173 | day-41.html |
| 60 | 第42日 | 「文章の文法」形式の問題 (N2・N1 each 問題1–3) | 136–142 | 136–142 | 173 | day-42.html |
| | **模擬試験** | (title page p.143) | | | | |
| 61 | N2 第1回 | 模擬試験 (N2-level), 22 items | 144–147 | 144–147 | 174 (別冊 p.8) | mogi-n2-1.html |
| 62 | N2 第2回 | 模擬試験 (N2-level), 22 items | 148–151 | 148–151 | 174 | mogi-n2-2.html |
| 63 | N1 第1回 | 模擬試験, 20 items | 152–155 | 152–155 | 174 | mogi-n1-1.html |
| 64 | N1 第2回 | 模擬試験, 20 items | 156–159 | 156–159 | 174 | mogi-n1-2.html |

64 units: 42 days + 11 まとめ + 7 columns + 4 mock tests. Prev/next (`bp-day-nav`) follows this table's order; unit 1's "prev" is the book hub `index.html`, unit 64's "next" is the hub.

## 5. Delivery

- Output folder: `n1/grammar/shiken-ni-deru/`. Depth is 3, so assets are `../../../assets/...`, site home `../../../index.html`, N1 home `../../index.html`, grammar hub `../../grammar.html`, book hub `index.html`.
- Same head/header/nav/footer as `n1/grammar/week-1/day-1.html`: `auth.js` in `<head>`, `style.css` + `day-page.css`, `main.js` before `</body>`, `<body class="level-page n1">`.
- Breadcrumb: Home / JLPT N1 / Grammar / 試験に出る文法と表現 (links to `index.html`) / {unit label, e.g. 第1日}.
- Header block (`.bp-header`): `bp-week` line = "JLPT N1 · Grammar · 試験に出る文法と表現 · 第N章 — {chapter title} (romaji)"; `h1` = unit label + title; meta grid with Source (printed + PDF pages), Grammar points covered, Answer key (別冊 page + PDF page, "confirmed, not guessed"), Notes (N1/N2 tags, register, traps).

## 6. Adapting the 3 required sections

### 6.1 Grammar Points (第N日 units)
- The book's table has a left column with the form (●〜に関して) and an optional **N1** tag, and right-column sub-blocks: a short gloss (〜に関係して), optional ※ usage notes, then numbered examples. One `bp-point` per left-column ● entry. When a form has several sub-uses (e.g. によって: それぞれで違う / 手段 / 原因 / 受身の動作主), keep them in one point and label each example row with its sub-use.
- Badge: "N1" (book-tagged) or "N2-level", plus register (`.bp-badge.formal` for 硬/written).
- Include **every** example sentence. Bold the target form as the book does.
- **メモ boxes** (connection notes, e.g. 〜に対して → 〜に対する + N) are reproduced in full as a table/callout after the points.
- Formation tables: the book rarely shows formation; most points attach to nouns. Fill other word types and mark "(added, not in book)".

### 6.2 Quiz / Exercise
- **練習問題 are mostly open fill-in-the-blank** (a blank, no printed options). Some items are "a／b" choices (e.g. 第3日 ⑬⑭, 第12日 ⑪) or 「正しい方を選びなさい」 brackets. For open blanks, build the options table from the day's own forms as candidate forms (plausible distractors from the same day) and label it "Candidate forms (added, not in book — the book prints an open blank)". The correct row is the official 別冊 answer; when the key gives alternatives (「によると／によれば」), mark every accepted form correct.
- まとめの問題 and 模擬試験 問題1: printed 4 options → normal options table.
- ★ sentence building (第41日, 模擬試験 問題2): this book **does** use the official ★ format. Show tiles, `bp-order-chain` with ★ on the starred slot, assembled sentence. The key gives only the ★ tile number; work out the full order and say so.
- 文章の文法 (第42日, 模擬試験 問題3): do **not** reproduce the passage. Give a 2–3 sentence "Passage summary (not the book's text)" in EN/HI/GU in our own words, then each numbered blank as a `bp-quiz` quoting only the sentence that contains it. Do not transcribe passages into scratch notes either.
- Column units: their own exercise with the on-page 解答.

### 6.3 Confusion Pairs
- Required on every unit. Day units: compare that day's forms. まとめ/mock/column units: compare the look-alike option sets the items actually test (one `bp-confusion` table plus `bp-callout` exam traps). If nothing applies, write "*(None on this page.)*".

## 7. Hub page update rule

`n1/grammar/shiken-ni-deru/index.html` groups units by chapter (one `week-block` per 第N章, plus a 模擬試験 block). Each unit is a chip in `day-chips`. When a unit is built, flip its chip from `<span class="day-chip soon">…</span>` to `<a class="day-chip ready" href="{file}">…</a>`, and update the progress count in the `sample-note`. Do not edit `n1/grammar.html` — it already links to this hub.

## 8. Language rules (unchanged from master)

EN + Hindi + Gujarati for every meaning, example and quiz sentence; `<span class="romaji">` under every Japanese line (examples, options, tiles, formation cells); learner-friendly English notes (2–4 sentences per point).

---

**Reference implementation:** [`n1/grammar/shiken-ni-deru/day-01.html`](../../../../n1/grammar/shiken-ni-deru/day-01.html) — the first unit built under this guide.

## Page conventions settled during the build

- **まとめ pages:** §1 = review-map table (item → pattern → day page link); §2 = every item with the book's option numbers 1–4; §3 = confusion pairs. Reference: `n1/grammar/shiken-ni-deru/matome-ch02.html`.
- **Column (基本文法) pages:** the book gives only the exercise, so §1 is a short explanation built from the column's own examples and marked "(added, not in book)"; answers come from the 解答 box printed on the column page. Reference: `column-02.html`.
- **A day's key can split across 別冊 pages** (e.g. 第8日 ①–⑤ at the foot of PDF 168, ⑥–⑫ at the top of 169); cite both pages.
- **Accepted alternatives:** where the key lists several answers (／), mark every accepted form correct.
- **Long passages** (第42日, 模擬試験 文章の文法): quote only the sentence(s) containing each blank and summarise the rest in our own words, labelled "Passage summary (not the book's text)".
- **Days 36–38** are entirely printed two-choice brackets (「※正しい方を選びなさい」), not open blanks — build them as normal a/b option tables ("1st/2nd a/b" where a sentence has two brackets).
