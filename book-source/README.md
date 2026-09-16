# Book source (upload staging area)

Drop the raw book material here — PDFs, Word docs, exported images, text, or spreadsheets. Any format is fine; nothing here gets published to the live site. Once files are in a folder, tell Claude to build that module's page and it will read these files and generate the matching `n1/…` or `n2/…` page in the site.

Folder = one module:

```
book-source/
  n1/
    vocabulary/   word lists
    kanji/        kanji lists
    grammar/      grammar point explanations
    reading/      reading passages + questions
    listening/
      audio/      mp3/m4a/wav audio clips
      (transcripts and questions go directly in listening/, not in audio/)
  n2/
    ... same 5 folders
```

No fixed naming rules — number pages/files however matches the book (e.g. `chapter1.pdf`, `unit01-05.docx`, `p12-30.png`). Multiple files per folder are fine.

## Module-specific processing guides

Some modules have a detailed standing spec for how their source material gets turned into site pages:

- [`n1/grammar/PROCESSING-GUIDE.md`](n1/grammar/PROCESSING-GUIDE.md) — day-by-day workflow for the N1 文法 (Sou-Matome) workbook: how to locate a day in the PDF, and the exact HTML section format to produce.
- [`n1/vocabulary/PROCESSING-GUIDE.md`](n1/vocabulary/PROCESSING-GUIDE.md) — day-by-day workflow for the N1 語彙 (Sou-Matome) workbook: symbol legend, word-list table format, and quiz/confusion-pair sections.
