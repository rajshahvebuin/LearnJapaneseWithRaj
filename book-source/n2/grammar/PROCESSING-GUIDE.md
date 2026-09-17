# N2 Grammar (文法) — day-by-day processing guide

Standing instructions for turning `Nihongo_SouMatome_N2-Bumpou.pdf` (日本語総まとめ N2 文法, 佐々木仁子・松本紀子, ASK Publishing) into the site's day-by-day grammar pages. Adapted from the N1 Grammar spec (`book-source/n1/grammar/PROCESSING-GUIDE.md`) — same delivery format and language rules, N2 source book, with the differences below called out explicitly.

The PDF is scanned/image-only (confirmed — no text layer, `get_text()` returns empty on every page checked). Render pages to PNG with PyMuPDF/`fitz` at ~2.2x zoom and read them visually. 156 pages total.

---

## 1. Unit location & verification

- A "day" (1日目, 2日目, …) is the unit of work, not a page number. Locate the day's starting page via the table of contents (printed pp.4–5), then read forward until the next 日目/実戦問題 heading begins — include every page in between, even if content or drill answers spill across a page break.
- **Page offset: none.** PDF page index (0-based, as returned by PyMuPDF) equals the printed page number exactly for this book — e.g. PDF page index 14 shows the printed stamp "14", index 25 shows "25", etc. This was cross-checked at the TOC (pages 4–6), at Week 1 Day 1 (14–15), and at Week 1's test day (26–28). Do **not** assume this holds all the way to the end without spot-checking — Week 8's TOC gap (see table below) is one page longer than the others, so re-verify the printed-page stamp on the scan itself before trusting arithmetic once you reach Week 8.
- Each week opens with a 1-page divider ("今週の表現") that is NOT itself a day — it's a checklist preview of that week's four bullet-point expressions per day (useful as a quick cross-check that you've found every expression for a given day, but it doesn't get its own HTML page).
- **Pages per day: 2 printed pages for Days 1–6, but 3 printed pages for Day 7 (実戦問題).** This is a deviation from the N1 book, where every day including the test day was 2 pages. Confirmed on Week 1: Day 7 spans printed pp.26–28 (問題1 fill-in-the-blank on p.26, 問題2 sentence-ordering on p.27, 問題3 reading-cloze passage + a bonus 敬語 column box on p.28).
- Each week totals 16 printed pages (1 divider + 6×2 content days + 3 for the test day) for Weeks 1–7 (confirmed against the TOC deltas below). Week 8's TOC delta is 17, not 16 — verify Week 8's actual day boundaries from the scan itself rather than assuming the pattern continues.
- Drill answers for Days 1–6 print at the bottom of the *second page of the following day* (same pattern as N1) — e.g. Day 1's practice answers (p.15) are printed at the bottom of p.17 (Day 2's second page). Fetch that page too and cite the confirmed answer rather than guessing.
- **実戦問題 (Day 7 test) answers — IMPORTANT, differs from N1:** the day-7 page prints "答えは別冊 p.X" (answer in the separate 別冊 booklet), but unlike the N1 scan, **the 別冊 booklet IS included in this PDF**, appended after the 索引 (index, printed pp.142–146) and the colophon/copyright page (148) and a decorative back page (149). The 別冊 answer/explanation booklet occupies roughly PDF pages 150–155 (0-indexed), with its own internal page numbering restarting near 1–6, and covers all 8 weeks' worth of 実戦問題 answers in a condensed reference-only format (just answer letter + one-line reason, no full explanation prose). **Locate and read the real answer key from the back of this same file — do not guess Day 7 answers from N2-level knowledge alone**, though you may still use your own knowledge to write the learner-facing "Why" explanation prose (the booklet only gives a terse justification).
- The small bonus 敬語 (keigo) column box that appears at the bottom of each week's Day-7 third page has its own tiny quiz whose answer is printed **in-book**, near the top of the following week's second page (not in 別冊). Its topic changes week to week — check each week's actual box when you get there.

**Week map** (printed page the week starts on, and its title, from the table of contents at pp.4–5):

| Week | Starts at | Title | Romaji | Gloss |
|---|---|---|---|---|
| 1 | p.13 | おぼえずにはいられない | Oboezu ni wa irarenai | I can't help remembering |
| 2 | p.29 | やればやるほどおぼえられる | Yareba yaru hodo oboerareru | The more you do it, the better you get |
| 3 | p.45 | おぼえないわけにはいかない | Oboenai wake ni wa ikanai | You must remember |
| 4 | p.61 | おぼえざるをえない | Oboezaru o enai | You have no choice but to remember |
| 5 | p.77 | おぼえてみようではないか | Oboete miyou de wa nai ka | Why not try to remember |
| 6 | p.93 | やるからにはおぼえよう | Yaru kara ni wa oboeyou | As long as you do it, remember |
| 7 | p.109 | がんばればおぼえられるというものだ | Ganbareba oboerareru to iu mono da | If you try hard enough, you can remember |
| 8 | p.125 | むずかしい。それでもおぼえよう。 | Muzukashii. Soredemo oboeyou. | It's difficult. Still, let's memorize it. |

Each week is 7 days (1〜6日目 = content, 7日目 = 実戦問題 test day), matching the N1 book's structure. 索引 (index) starts at p.142; the 別冊 answer booklet follows at the very end of the PDF (see above).

## 2. Content shape (sampled Week 1, Days 1–2 and the Day 7 test — not read in full depth)

- Each content day covers **3–4 grammar/expression points** (confirmed explicitly in the book's own "How to use this book" page: "1日に3つ〜4つずつ"), each presented as a full-width headline banner (large-font headword + a 1-line EN/CN/KR gloss underneath — this book's own built-in translations are English/Chinese/Korean, not Hindi/Gujarati; that's irrelevant to us since we always write our own EN+HI+GU per the site's language rule regardless of what the source offers).
- Under each headline: 1–3 example sentences with the target grammar underlined, a `(=paraphrase)` in easier Japanese, and EN/CN/KR translations — plus a boxed formation/connection-notes callout in the right margin (e.g. "Aくて / naで / Vたくて → たまらない"), sometimes tagged with small badges/icons: 硬 (formal register, same meaning as in the N1 book) and occasionally a speech-bubble or heart icon that seem to flag conversational/emotional nuance. No full legend is given for the non-硬 icons beyond what's inferable from context — note each one as encountered, same as the N2 Vocabulary spec's approach to undocumented symbols.
- **Quiz format for Days 1–6 differs from N1's blank-with-many-options style:** 練習Ⅰ is "circle the correct choice" between **two** inline options given in parentheses within a full sentence (e.g. "この牛乳は水（a. っぽくて b. 気味で）、おいしくない。"), not a blank with up to 5 separate options. 練習Ⅱ is sentence-reordering into 4 numbered blanks using plain underscores (no official ★ marker) — same as N1's non-test-day convention.
- **Quiz format for Day 7 (実戦問題) matches real JLPT formatting and has three parts, not two:** 問題1 = classic 4-option fill-in-the-blank (~15 items); 問題2 = sentence-ordering **with a real ★ blank marker** (~5 items) — the opposite of Days 1–6, which don't use ★; 問題3 = a short reading-passage cloze with ~5 numbered blanks, each with 4 options — this third exercise type is an addition versus the N1 book's Day 7 (verify if N1 also has it before treating this as certain; call it out per-day either way).

## 3. Delivery — a real page on the site, not a standalone file

- Build each day at `n2/grammar/week-{N}/day-{D}.html`, using the site's shared header/nav/footer/breadcrumb (`assets/css/style.css`) plus the dedicated `assets/css/day-page.css` stylesheet — reuse its existing classes rather than inventing new ones: `.bp-header`, `.bp-point`, `.bp-table`, `.bp-formation-table`, `.bp-examples-table`, `.bp-quiz`, `.bp-options`, `.bp-confusion`, `.bp-order-chain`, `.bp-assembled`, `.bp-day-nav`, `.bp-callout`.
- Body class `level-page n2`; nav order Home / JLPT N1 / JLPT N2 with N2 marked `active`; breadcrumb Home / JLPT N2 / Grammar / Week N / Day D. Use `n1/grammar/week-1/day-1.html` as the structural template (read it for exact markup) and swap N1→N2 paths/labels.
- Update `n2/grammar.html` (the week/day hub) so that day's chip flips from `<span class="day-chip soon">` to a linked `<a class="day-chip ready" href="...">`.
- Always include all three sections every time, even if one is empty (write "*(None on this page.)*"): (1) Grammar Point Section, (2) Quiz/Exercise Section, (3) Confusion Pairs/Nuance Notes.
- Start with a header block noting: week/day title, source file + printed page range used, grammar points covered, and notes (answer key location — cite the confirmed 別冊 page for Day 7, or the confirmed following-day page for Days 1–6; register warnings; exam traps).

## 4. Grammar Point Section format

For each grammar point: a `.bp-point` block with —
- **【N】 〜form〜** subheading with a register badge (`.bp-badge` / `.bp-badge.formal` for 硬) — plus a plain-text note for any other icon this book uses that N1 didn't (speech-bubble/heart), described in words since there's no site badge class for them yet.
- A field table: Reading / Meaning (EN) / Meaning (Hindi) / Meaning (Gujarati) / Connection (接続) / Register / Typical use
- A formation-breakdown table for verb / い-adj / な-adj / noun — this book's own sidebox usually already spells out the connection form directly (e.g. "Aくて／naで／Vたくて"), so transcribe those rather than inventing them; still mark any cell you had to add yourself as "(added, not in book)"
- An examples table (every example from the book) with columns Japanese / English / Hindi / Gujarati
- 2–4 sentence learner-friendly notes in English

## 5. Quiz/Exercise Section format

For Days 1–6 (練習Ⅰ・Ⅱ):
- Full Japanese sentence with the two inline choices spelled out + English/Hindi/Gujarati translation of the completed (correct) sentence
- An options table (Option / Japanese / English / Hindi / Gujarati) — even though the book only gives 2 choices per item, keep the table format for consistency; mark the correct row `class="correct"`
- A "Why" callout: why the correct answer fits and why the other option is wrong
- 練習Ⅱ sentence-ordering: assembled sentence, order chain (`.bp-order-chain`), and note that this book uses plain numbered blanks (not ★) for these

For Day 7 (実戦問題):
- 問題1/問題2 follow the same quiz format as above but with the book's real 4-option JLPT format; 問題2's ★ blank should be reproduced literally (unlike Days 1–6)
- 問題3 (reading cloze): present the passage once, then each numbered blank as its own `.bp-quiz` block referencing back to the passage
- Cite the **real** answer from the 別冊 booklet found at the back of this PDF (see §1) for every item — do not fall back to guessing unless the booklet page truly can't be located, and flag transparently if you do

## 6. Confusion Pairs/Nuance Notes — required every day

A `.bp-confusion` comparison table (Form / Meaning / Connection / Key difference / Use when) across the day's grammar points, flagging near-synonyms, same-form-different-meaning traps, connection traps, register traps, and positive/negative pairing traps. Add a `.bp-callout` for any trap N2 habitually tests (this book explicitly groups same-day points because they're easy to confuse — see the divider page's four-bullet list per day — so there should almost always be something to compare).

## 7. Learner level & language rules

- Intermediate learner preparing for JLPT N2; native languages Hindi and Gujarati — always give meanings/examples in both, plus English grammar explanations (simple, concise), regardless of the source book's own EN/CN/KR translations.
- **Add romaji** under every Japanese line (sentences, options, formation examples) — a standing site-wide requirement, not specific to grammar.

## 8. Optional add-on

If the user says "drill me" after a day, generate 5 fresh practice questions using that day's grammar points in the same Q-format, with answers/explanations at the bottom rather than inline.

---

**Reference implementation:** `n1/grammar/week-1/day-1.html` is the closest existing template — use it for structure, tone, and depth until an N2-specific reference day exists (none built yet as of this recon).
