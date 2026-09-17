# N2 Vocabulary (語彙) — day-by-day processing guide

Standing instructions for turning `Nihongo_SouMatome_N2-Goi.pdf` (日本語総まとめ N2 語彙) into the site's day-by-day vocabulary pages. Adapted from the N1 Vocabulary spec (`book-source/n1/vocabulary/PROCESSING-GUIDE.md`) — same process, N2 book.

The PDF is likely scanned/image-only (verify first) — if so, render pages to PNG (PyMuPDF/`fitz`) and read visually; if it has a text layer, extract text directly instead.

---

## 1. Unit location & verification — CONFIRMED

- This scan **has a full TOC** (printed p.4–5, PDF index 4–5): 8 weeks, 7 days each (56 days total), week titles and day sub-titles all listed up front. Full map:
  - 第1週 楽しく暮らしていますか？(Tanoshiku kurashite imasu ka?) — p.11–26 — 1日目 アパートを探しています／2日目 引っ越しは大変です／3日目 友人を招きました／4日目 家事・子育ては大変です／5日目 夏休みを海で過ごしています／6日目 お金を使いすぎました／7日目 実戦問題
  - 第2週 仕事は順調ですか？(Shigoto wa junchou desu ka?) — p.27–42 — 1仕事を探しています／2仕事をしています①／3仕事をしています②／4パソコンを使っています①／5パソコンを使っています②／6パソコンを使っています③／7実戦問題
  - 第3週 いろいろ表現しましょう (Iroiro hyougen shimashou) — p.43–58 — 1どんな人ですか？／2どんな様子ですか？／3どんな動作ですか？／4どんな気持ち・態度ですか？①／5どんな気持ち・態度ですか？②／6体の具合はどうですか？／7実戦問題
  - 第4週 副詞をたっぷり覚えましょう (Fukushi o tappuri oboemashou) — p.59–74 — 1なんとか覚えよう！／2いずれ覚えられる！／3せっせと覚えよう！／4さらに覚えよう！／5取りあえず覚えよう！／6いったん覚えたら忘れない！／7実戦問題
  - 第5週 やさしい漢字で書きますが… (Yasashii kanji de kakimasu ga...) — p.75–90 — 1物事・日中・年月／2夜中・世間・作業／3一生・用心・見事／4土地・名字・発売／5手品・合図・強気／6本気・気楽・目安／7実戦問題
  - 第6週 まとめて覚えましょう① — p.91–106 — 1カタカナで書く言葉①／2②／3③／4似ている言葉①／5②／6③／7実戦問題
  - 第7週 まとめて覚えましょう② — p.107–122 — 1意味がたくさんある言葉①／2②／3③／4言葉の前につく語／5言葉の後ろにつく語①／6②／7実戦問題
  - 第8週 まとめて覚えましょう③ — p.123–138 — 1組み合わせの言葉①／2②／3よく使われる表現①／4②／5③／6④／7実戦問題
  - さくいん (index) at p.139 onward; no separate answer booklet is present in this scan (see below).
- **Printed page number = PDF page index directly** (0-based `fitz`/PyMuPDF index — page printed "12" is `doc[12]`), unlike N1 which had an 11-page offset. Cover/front matter occupy index 0–10; content starts at index 11.
- Cadence **confirmed**: 1日2ページ (2 printed pages per day), same as N1, for the 6 regular days; the 7日目 実戦問題 test day runs longer (verify per week, roughly 4 pages based on Week 1's total page count).
- Drill answers are printed at the **bottom of the page-2 spread two days later** — confirmed identical pattern to N1 (Day 1's exercises on p.13 are answered in the "13ページの答え：…" box at the bottom of p.15). Always fetch that later page and cite the confirmed answer.
- **No separate answer booklet included in this scan.** The TOC lists `[別冊] 解答・解説` (a separate answer/explanation booklet) as accompanying the physical book, but it is not part of this PDF. Two different situations result:
  - Regular days' 練習Ⅰ/Ⅱ exercises ARE confirmable: their answers print in-book, in an "○ページの答え" box at the bottom of the page-2 spread two days later (e.g. Day 1's p.13 exercises are answered at the bottom of p.15). Use these — they are official, not guessed.
  - Each week's 7日目 実戦問題 (test day, ~3 pages, 25 questions, 100 points) is different: its own page explicitly says "答えは別冊p.1" (answer in the separate booklet, p.1), and that booklet isn't in this scan. For test days, work out each answer yourself from that week's vocabulary and cross-check for internal consistency, and flag clearly in the day's header/notes that these are reasoned answers, not an official key (mirrors how N1's test days were already handled).

## 2. Symbols used in this book — CONFIRMED (legend page, unnumbered, right after the cover/title pages)

| Symbol | Meaning |
|---|---|
| ⊙ (circled arrow) | 関連する語彙 (related vocabulary) — a related word/expression follows |
| ⇔ | 反対の意味 (antonym) |
| ❶ (exclamation mark in a circle) | 注意しましょう (pay attention — a usage caution) |
| "ダメ" stamp icon | このような使い方はだめです (this usage is NOT correct — a wrong-usage warning) |
| (N) | 名詞 (noun) |
| (V) | 動詞 (verb) |
| ☞ p.X | see page X |

Does **not** reuse N1's ※/→/・ symbols. A directional bent-arrow variant (visually pointing to a related term, e.g. 真後ろ next to 真ん前) was also seen — treat as the same ⊙ "related term" relationship unless context shows otherwise.

## 3. Structural format differs from N1 — CONFIRMED, template adjusted accordingly

Unlike N1's one-continuous-word-list days, N2 days are **situational**: each day opens with an illustrated 2-character dialogue/comic establishing a real-life scene (e.g. apartment-hunting, moving), then presents several small **thematically-grouped** vocabulary tables under their own "おぼえましょう" (let's memorize) or "絵をみておぼえましょう" (look at the picture and memorize) sub-headers — do NOT flatten these into one table; preserve the book's own sub-groupings, each as its own `.vd-wordlist` table with a preceding `<h3>` label. Then 練習Ⅰ (choose the correct of 2 options, a/b) and 練習Ⅱ (choose 1 of 4 numbered options) exercises, then a "きょうの一言" (today's saying) one-line takeaway phrase using the day's key vocabulary.

Reuse `.vd-warmup` for the opening dialogue/scene (label it "Scene" instead of "Warm-up"), reproducing each speaker's line with romaji + English gloss, plus any flyer/realia box shown (e.g. the apartment listing on Day 1) as a small table or note.

## 4. Delivery — a real page on the site, not a standalone file

- Build each day at `n2/vocabulary/week-{N}/day-{D}.html`, using `assets/css/style.css` + shared `assets/css/day-page.css` (same classes as N1 day pages: `.bp-header`, `.bp-meta-grid`, `.bp-note`, `.bp-section-title`, `.bp-quiz`, `.bp-options`, `.bp-why`, `.bp-confusion`, `.bp-callout`, `.bp-day-nav`, `.vd-legend`, `.vd-warmup`, `.vd-wordlist`). Use `n1/vocabulary/week-1/day-1.html` as the structural template but update nav/breadcrumb/body-class to N2 (`level-page n2`, nav order Home/N1/N2 active).
- Update `n2/vocabulary.html` (the week/day hub) so each day's chip flips from `day-chip soon` to a linked `day-chip ready`, and each week's `(title TBD)` gets replaced with the real Japanese title + romaji once discovered. Replace the current placeholder sample-note/card-grid content entirely once real content starts landing.
- Header block: week/day title, source file + page range used, theme, notes (answer key location).

## 5. Vocabulary List section format

Multiple `.vd-wordlist` tables per day, one per book sub-group (see §3), each under its own `<h3>` heading matching the book's own group label (translated/romanized). Columns: **Japanese** (headword + romaji) / **English** / **Hindi** / **Gujarati** / **Note** (for ⊙/⇔/❶/ダメ annotations, with romaji + gloss).

## 6. Warm-up / Scene section

Reproduce the day's opening dialogue/illustration as `.vd-warmup` (see §3): each spoken line with romaji + English gloss, plus any realia (flyer, form, etc.) shown in the illustration as a small supporting table.

## 7. Quiz/Exercise section format

For every 練習Ⅰ/Ⅱ/… item: full Japanese sentence with blank + romaji, then completed sentence + English/Hindi/Gujarati; an options table (correct row `class="correct"`); a "Why" callout. Cite the confirmed answer from the "○ページの答え" box 2 pages later (§1) — do not guess.

## 8. Confusion Pairs/Nuance Notes — required every day

A `.bp-confusion` table grouping near-synonyms from that day's word list that English/Hindi/Gujarati glosses would wrongly flatten together, plus `.bp-callout` for fixed-idiom/usage traps (e.g. anything flagged ❶ or "ダメ" in the book).

## 9. Learner level & language rules

Same site-wide rule: English + Hindi + Gujarati meanings, romaji under every Japanese word/sentence/option.

---

**Reference implementation:** `n1/vocabulary/week-1/day-1.html` for CSS/structural conventions; `n2/vocabulary/week-1/day-1.html` (once built) for the N2-specific situational-day template.
