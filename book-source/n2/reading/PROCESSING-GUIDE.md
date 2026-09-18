# N2 Reading (読解) — day-by-day processing guide

Standing instructions for turning `Nihongo_SouMatome_N2-Dokkai.pdf` (日本語総まとめ N2 読解, by 佐々木仁子・松本紀子, Ask Publishing) into the site's day-by-day reading pages.

The PDF is scanned/image-only — render pages to PNG (PyMuPDF/`fitz`, ~2.2x zoom) and read visually.

## 1. Unit location & verification — CONFIRMED

- **PDF index = printed page − 1** (equivalently printed = index + 1), confirmed empirically at multiple week dividers (index27→printed28, index59→printed60, index77→printed78, index95→printed96). Front-matter pages before content (TOC etc.) print at index=printed directly; the +1 offset begins at Week 1's content.
- **Only 6 weeks** (not 8, like N1 Reading) — confirmed full TOC:
  - 第1週 身の回りの文書を読もう (everyday documents) — printed p.11–26 — 1割引券・クーポン／2ダイレクトメール／3アルバイト情報／4アパート・マンション情報／5利用案内／6レシピ／7実戦問題
  - 第2週 お知らせや通知を読もう (notices/announcements) — printed p.27–42 — 1お知らせ①／2お知らせ②／3お知らせ③／4通知①／5通知②／6通知③／7実戦問題
  - 第3週 意見文や説明文を読もう (opinions/explanations) — printed p.43–58 — 1意見文①／2意見文②／3意見文③／4意見文④／5説明文①／6説明文②／7実戦問題
  - 第4週 エッセイや小説を読もう (essays/novels) — printed p.59–76 (18pp, longer week) — 1エッセイ①／2エッセイ②／3エッセイ③／4エッセイ④／5小説①／6小説②／7実戦問題 [コラム]統合問題に慣れよう!①
  - 第5週 新聞を読もう (newspapers) — printed p.77–94 (18pp, longer week) — 1見出し①／2見出し②／3記事／4グラフ①／5グラフ②／6書評／7実戦問題 [コラム]統合問題に慣れよう!②
  - 第6週 論説文を読もう (editorials) — printed p.95–110 — 1言語に関する文章／2化学に関する文章／3生物に関する文章／4物理に関する文章／5医学に関する文章／6数学に関する文章／7実戦問題
- **Cadence confirmed**: 1日2ページ for Days 1–6 in every week. Day 7 (実戦問題) is normally 3 pages, EXCEPT Weeks 4 and 5 where Day 7 runs 4 pages AND an extra 1-page [コラム] (column/tip) closes the week — this is why Weeks 4–5 are 18 printed pages instead of 16.
- **Exact confirmed page anchors (printed page numbers; subtract 1 for PDF index)**:
  - Week1 (divider p.11): D1 12–13, D2 14–15, D3 16–17, D4 18–19, D5 20–21, D6 22–23, D7 24–26
  - Week2 (divider p.27): D1 28–29, D2 30–31, D3 32–33, D4 34–35, D5 36–37, D6 38–39, D7 40–42
  - Week3 (divider p.43): D1 44–45, D2 46–47, D3 48–49, D4 50–51, D5 52–53, D6 54–55, D7 56–58
  - Week4 (divider p.59): D1 60–61, D2 62–63, D3 64–65, D4 66–67, D5 68–69, D6 70–71, D7 72–75 (4pp), [コラム] p.76
  - Week5 (divider p.77): D1 78–79, D2 80–81, D3 82–83, D4 84–85, D5 86–87, D6 88–89, D7 90–93 (4pp), [コラム] p.94
  - Week6 (divider p.95): D1 96–97, D2 98–99, D3 100–101, D4 102–103, D5 104–105, D6 106–107, D7 108–110
- Days 1–6 print furigana under every kanji; Day 7 (実戦問題) only furigana kanji above JLPT N1 level, simulating real exam conditions — irrelevant to our site output since we always add full romaji regardless, but worth noting in Day 7's header as a book-fidelity note.

## 2. ANSWER KEY — fully present in this scan (great news, same as N2 Kanji)

- The book's [別冊] 解答・解説 (separate answer/explanation booklet) **is included in this PDF scan**, immediately after the main book's colophon/credits page. Formula: **PDF index = week_number + 112** (e.g. Week 1's answers → index 113, Week 4's → index 116). Each week's answers are compact — typically ONE booklet page per week, showing every day's 問題 answers (問1/問2/etc.) plus occasional starred explanatory notes for trickier items. Confirmed anchors: Week 1 → index 113 ("第1週" header, all 7 days' answers on one page), Week 4 → index 116 ("第4週" header, including Day 7's 問題1/問題2 answers with explanatory notes).
- **Always cite the confirmed answer from the booklet — never guess or reason out any answer in this book**, regular day or test day alike.
- Regular days (1–6) also have their own in-book 練習 (a short warm-up exercise, not the main reading passage) whose answer is noted as "(答えは次のページ)" — printed on the very next page — confirm from there directly; only the main 問題 (reading comprehension) sections need the answer booklet.

## 3. Structural format — CONFIRMED, closer to N1 Reading than N2 Vocabulary/Kanji

Each regular day (1–6) has two parts:
1. A **strategy/skill-focus box** (marked with a ✿ heart-flower bullet) teaching one reading sub-skill relevant to that week's theme (e.g. Week1 Day1: how coupon/discount language works; Week4 Day1: "answers are usually paraphrased nearby — read the question first"; Week6 Day1: "split long sentences with a slash (/) to parse them"). Include this as `.rd-strategy` (reuse from N1 Reading), with the strategy's own short 練習 (a dialogue-based comprehension check, 5 true/false-style items, answer on the next page — cite it from there).
2. The main **問題** reading-comprehension exercise: one or more passages (of the week's theme — coupon, notice, opinion piece, essay, newspaper headline, editorial, etc.) each followed by 問1/問2/... comprehension questions with 4 numbered options. Cite the confirmed answer from the answer booklet (see §2).

Day 7 (実戦問題) is a full mock-test day: multiple passages under 問題1/問題2/(問題3/4 in the longer Weeks 4–5), JLPT-style, harder kanji only get furigana. Weeks 4 and 5 additionally close with a `[コラム] 統合問題に慣れよう!` tip box about the 統合理解-style "integrated" question type — include this as a `.bp-callout` on Day 7's page for those two weeks only.

## 4. Delivery — a real page on the site

- Build each day at `n2/reading/week-{N}/day-{D}.html`, using `assets/css/style.css` + `assets/css/day-page.css`. Reuse N1 Reading's classes: `.rd-strategy`, `.rd-strategy-label`, `.rd-passage-label`, plus the standard `.bp-header`, `.bp-meta-grid`, `.bp-section-title`, `.bp-quiz`, `.q-jp`, `.q-translations`, `.bp-options`, `.bp-why`, `.bp-confusion`, `.bp-callout`, `.bp-day-nav`. Use `n1/reading/week-1/day-1.html` as the structural reference; body class `level-page n2`, N2 breadcrumb/nav (Home / JLPT N1 / JLPT N2 active).
- Update `n2/reading.html` (hub) so each day's chip flips from `day-chip soon` to a linked `day-chip ready`, and week titles get the real Japanese title + romaji. Consolidated separately after all build agents finish — individual day-builders should NOT touch the hub page.
- Header block: week/day title, source + printed page range used, reading skill/theme covered, where the confirmed answer was found (booklet page/index).

## 5. Confusion Pairs / Nuance Notes — required every day

No vocabulary cluster to draw on here (same situation as N1 Reading) — instead compare which reading strategy unlocks each of that day's questions (Question / Strategy used / What the answer choice tests / Trap to avoid), reusing the N1 Reading pattern.

## 6. Learner level & language rules

Same site-wide rule: English + Hindi + Gujarati translations (book gives EN/Chinese/Korean — add Hindi/Gujarati yourself), romaji under every Japanese sentence/passage line/option.

---

**Reference implementation:** none yet — Week 1 Day 1 (割引券・クーポン) is the first day to be built under this spec.
