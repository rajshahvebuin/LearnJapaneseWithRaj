# N1 Reading (読解) — day-by-day processing guide

Standing instructions for turning `Nihongo_Soumatome_N1-Dokkai.pdf` (日本語総まとめ N1 読解) into the site's day-by-day reading pages. Give a week + day (e.g. "Week 1, Day 2") and this is the process to follow.

The PDF is scanned/image-only (no text layer) — render pages to PNG (e.g. with PyMuPDF/`fitz`) and read them visually. This is a **bilingual JP/Chinese edition**: explanatory prose (section intros, strategy tips) is printed in simplified Chinese, while the actual Japanese passages, questions and answer options are all genuine Japanese. Translate the Chinese explanatory text into English/Hindi/Gujarati for the site — don't reproduce it in Chinese.

---

## 1. Unit location & verification

- A "day" (1日目, 2日目, …) is the unit of work, not a page number. Locate it via the TOC (PDF page index 5, printed p.4–5), then read forward until the next 日目/実戦問題 heading begins.
- **PDF index = printed page + 1** for this scan (confirmed: printed page "3" is at PDF index 4). Front matter (title, はじめに, 目次, book usage guide) runs printed p.1–10; content starts at printed p.11 (PDF index 12).
- Week anchors (printed page, from TOC): Week1 p.11 注意する言葉はどれ？, Week2 p.29 いつ・だれ・何のこと？, Week3 p.47 答えは文章の中にある！, Week4 p.65 違いを見つけよう！, Week5 p.83 情報を正しく読み取ろう！, Week6 p.101 長文を読もう！. **6 weeks only** (not 8, unlike grammar/vocab/kanji) — confirmed from TOC, which ends with 第6週 and then `[別冊] 解答・解説`.
- Each week is 7 days (1〜6日目 = passage practice, 7日目 = 実戦問題 test day + a `[コラム]` (column) reading passage). 1日2ページ (2 printed pages per day) — confirmed for Week 1 Day 1 (p.12–13) and Day 2 starting cleanly at p.14.
- **Correction (found while building Week 6): the answer key is NOT missing from this scan.** The TOC's final line reads `[別冊] 解答・解説`, which was originally (incorrectly) assumed to mean the answer booklet was bound separately and excluded from the scan — same assumption made for the N1 Kanji book. In fact this PDF's own back matter contains a full `解答・解説` (Answers and Explanations) section starting at printed p.120 (confirmed via its title page). **Always render and check that section for the days you're building before writing a day's answers** — reason the answer out first from passage logic (still good practice and worth showing your work in `.bp-why`), then cross-check it against the real key and correct the "Answer key" caveat text on the page to say the answer was confirmed against the book's own 解答・解説 section (cite the answer-key page), rather than reusing the older "no official key in this scan" phrasing. Weeks 1–6 as originally built used the old (incorrect) caveat throughout and should be revisited to verify/update against pp.120+ if accuracy matters for that pass.
- Footnote translations at the bottom of each page (English, plus Chinese/Korean in this edition) translate the *harder full sentence*, not necessarily the blank itself — use them to sanity-check your reasoning, not as a direct answer key.

## 2. What a "day" actually contains

Early weeks (Week 1 at least) are **not full multi-paragraph passages** — they're short 1–4 sentence excerpts, each with one or more blanks `（　）`, testing a specific reading sub-skill (e.g. Day 1: figuring out what belongs in a blank from context; Day 2: recognizing rhetorical questions that mean strong negation). Later weeks (per TOC: Week 4 on comparing texts, Week 5 on notices/graphs/lists, Week 6 explicitly "長文を読もう" long-passage reading) shift toward longer, more traditional reading passages — confirm each week's actual format as you reach it rather than assuming Week 1's short-excerpt style continues throughout.

## 3. Delivery — a real page on the site, not a standalone file

- Build each day at `n1/reading/week-{N}/day-{D}.html`, using the site's shared header/nav/footer/breadcrumb (`assets/css/style.css`) plus the shared `assets/css/day-page.css` stylesheet — the same file grammar/vocabulary/kanji day pages use. Reuse `.bp-header`, `.bp-meta-grid`, `.bp-note`, `.bp-section-title`, `.bp-quiz`, `.q-jp`, `.q-translations`, `.bp-options`, `.bp-why`, `.bp-confusion`, `.bp-callout`, `.bp-day-nav`, plus the reading-specific `.rd-strategy` (the day's strategy/tip box) and `.rd-passage-label`.
- Update `n1/reading.html` (the week/day hub) so that day's chip flips from `day-chip soon` (a plain `<span>`) to `<a class="day-chip ready" href="...">` once built.
- Header block should note: week/day title, source file + printed/PDF page range, the skill/strategy covered, and an explicit answer-key caveat (separate [別冊], not included).

## 4. Reading Strategy section format

Every day opens with a strategy/tip box (in this edition's Chinese prose) explaining the reading sub-skill for that day. Translate it into a `.rd-strategy` block: a short key-idea line, then each bullet point with its English explanation plus Hindi/Gujarati translation lines (`.rd-tr`).

## 5. Passage Questions section format

For each passage/question that day, a `.bp-quiz` block with:
- The Japanese passage text (with `（　）` blank(s) marked) + romaji, labeled `.rd-passage-label`
- Any footnote (注) definitions, with romaji + English gloss
- The full/completed sentence with the blank filled in, + English/Hindi/Gujarati translation of the whole passage (`.q-translations`)
- An options table (`.bp-options`) — Option / Japanese (+ romaji) / English / Hindi / Gujarati, correct row marked `class="correct"`; for multi-blank (A/B/C-style) questions, use one column per blank instead of a single Japanese column
- A `.bp-why` callout explaining the reasoning, referencing which strategy from section 1 applies and explicitly ruling out the wrong options

## 6. Confusion Pairs / Nuance Notes — required every day

Unlike grammar/vocabulary (near-synonym word clusters) or kanji (same-reading kanji clusters), reading days don't have an obvious vocabulary cluster. Instead, use this section to compare **which strategy unlocks each question** that day (a `.bp-confusion` table: Question / Strategy used / What the blank does / Trap to avoid) plus a `.bp-callout` flagging the day's answer-key caveat (no official key in this scan).

## 7. Learner level & language rules

- Same as the rest of the site: Hindi and Gujarati meanings alongside English, and **romaji under every Japanese line** — see the site-wide romaji requirement in memory.

---

**Reference implementation:** `n1/reading/week-1/day-1.html` (Week 1 Day 1, （　）の中に入るのは？) is the first day built under this spec.
