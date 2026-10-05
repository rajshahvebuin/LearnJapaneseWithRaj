# Book source (local only)

Raw textbook material lives here. **Nothing in this folder is published** — `.gitignore` excludes every file under `book-source/` except `.md` docs and `.gitkeep` placeholders, so PDFs and audio stay on this machine.

## Layout

```
book-source/<level>/<module>/<Book_Name>/   one folder per book (PDF + any CD audio folders)
```

- **Levels:** `n1` … `n5`. A book covering two levels sits under the higher one (N1–N2 books in `n1`, N4–N5 books in `n4`).
- **Modules:** `vocabulary` (語彙/文字), `kanji`, `grammar` (文法), `reading` (読解), `listening` (聴解), plus
  `multi-skill` (one book covering several sections), `mock-tests` (模試 / 予想問題 / official question books) and `textbooks` (general course books).
- **Exception:** the original Sou-Matome N1/N2 books stay as flat PDFs directly in `n1/<module>/` and `n2/<module>/` (audio in `<module>/listening/audio/`), because existing site pages and the `PROCESSING-GUIDE.md` files reference those paths.

## Processing guides

Modules with a standing spec for turning a book into site pages have a `PROCESSING-GUIDE.md` next to the book (currently the Sou-Matome N1/N2 modules). New books will get their own guide when their pages are built.

## Catalogue

### N1

**vocabulary**

- `Drill_&_Drill_N1-Moji_Goi/` — 1 PDF
- `Nihongo_Power_Drill_N1-Goi/` — 1 PDF
- `Nihongo_SouMatome_N1-Goi.pdf` (Sou-Matome, flat file — used by existing site pages)
- `Pattern_de_Manabu_JLPT_N1-Moji.Goi/` — 1 PDF
- `Shiken_ni_Deru_N1_N2-Moji_Goi/` — 1 PDF
- `Shin_Kanzen_Master_N1-Goi/` — 1 PDF

**kanji**

- `Nihongo_SouMatome_N1-Kanji.pdf` (Sou-Matome, flat file — used by existing site pages)
- `Shin_Kanzen_Master_N1-Kanji/` — 1 PDF

**grammar**

- `Drill_&_Drill_N1-Bunpou/` — 1 PDF
- `Mimi_Kara_Oboeru_N1-Bunpou/` — no PDF, 10 audio tracks
- `Nihongo_Power_Drill_N1-Bunpou/` — 1 PDF
- `Nihongo_Soumatome_N1-Bunpou.pdf` (Sou-Matome, flat file — used by existing site pages)
- `Shiken_ni_Deru_N1_N2-Bunpou/` — 1 PDF
- `Shin_Kanzen_Master_N1-Bunpou/` — 1 PDF

**reading**

- `Jitsuryoku_Appu_JLPT_N1-Yomu/` — 1 PDF
- `Nihongo_Soumatome_N1-Dokkai.pdf` (Sou-Matome, flat file — used by existing site pages)
- `Shiken_ni_Deru_N1_N2-Dokkai/` — 1 PDF
- `Shin_Kanzen_Master_N1-Dokkai/` — 1 PDF
- `Speed_Master_N1-Dokkai/` — 1 PDF

**listening**

- `Jitsuryoku_Appu_JLPT_N1-Kiku/` — 1 PDF, 143 audio tracks
- `Nihongo_SouMatome_N1-Choukai.pdf` (Sou-Matome, flat file — used by existing site pages)
- `Shin_Kanzen_Master_N1-Choukai/` — 2 PDF, 149 audio tracks
- `audio/` (Sou-Matome CD tracks)

**multi-skill**

- `20_Nichi_Goukaku_N1-Moji.Goi.Bunpou/` — 1 PDF
- `Drill_&_Drill_N1-Choukai_Dokkai/` — 1 PDF
- `Pattern_Betsu_Tettei_Drill_JLPT_N1/` — 1 PDF, 89 audio tracks
- `Tanki_Master_Drill_N1/` — 1 PDF, 67 audio tracks

**mock-tests**

- `JLPT_N1_Kanzen_Moshi/` — 2 PDF, 144 audio tracks
- `JLPT_N1_Moshi_to_Taisaku/` — 1 PDF, 81 audio tracks
- `JLPT_Super_Moshi_N1/` — 1 PDF, 123 audio tracks
- `JLPT_Yosou_Mondaishuu_N1/` — 1 PDF


### N2

**vocabulary**

- `Drill_&_Drill_N2-Moji_Goi/` — 1 PDF
- `Nihongo_SouMatome_N2-Goi.pdf` (Sou-Matome, flat file — used by existing site pages)
- `Shin_Kanzen_Master_N2-Goi/` — 1 PDF
- `Speed_Master_N2-Goi/` — 1 PDF

**kanji**

- `Nihongo_SouMatome_N2-Kanji.pdf` (Sou-Matome, flat file — used by existing site pages)
- `Shin_Kanzen_Master_N2-Kanji/` — 1 PDF, 54 audio tracks

**grammar**

- `Drill_&_Drill_N2-Bunpou/` — 1 PDF
- `Mimi_Kara_Oboeru_N2-Bunpou/` — 1 PDF, 10 audio tracks
- `Nihongo_SouMatome_N2-Bumpou.pdf` (Sou-Matome, flat file — used by existing site pages)
- `Shin_Kanzen_Master_N2-Bunpou/` — 1 PDF
- `Speed_Master_N2-Bunpou/` — 1 PDF

**reading**

- `Jitsuryoku_Appu_JLPT_N2-Yomu/` — 1 PDF
- `Nihongo_SouMatome_N2-Dokkai.pdf` (Sou-Matome, flat file — used by existing site pages)
- `Shin_Kanzen_Master_N2-Dokkai/` — 1 PDF
- `Speed_Master_N2-Dokkai/` — 1 PDF

**listening**

- `Mimi_Kara_Oboeru_N2-Choukai/` — 1 PDF, 93 audio tracks
- `Nihongo_Soumatome_N2-Choukai.pdf` (Sou-Matome, flat file — used by existing site pages)
- `Shin_Kanzen_Master_N2-Choukai/` — 1 PDF, 163 audio tracks
- `Speed_Master_N2-Choukai/` — 1 PDF, 156 audio tracks
- `audio/` (Sou-Matome CD tracks)

**multi-skill**

- `Drill_&_Drill_N2-Choukai_Dokkai/` — 1 PDF, 156 audio tracks
- `JLPT_Goukaku_Dekiru_N2/` — 1 PDF, 113 audio tracks
- `Pattern_Betsu_Tettei_Drill_N2/` — 1 PDF, 89 audio tracks

**mock-tests**

- `Anata_no_Jakuten_ga_Wakaru_2kyuu_Mogishiken/` — 1 PDF, 79 audio tracks
- `JLPT_N2_Kanzen_Moshi/` — 2 PDF, 129 audio tracks
- `JLPT_Super_Moshi_N2/` — 1 PDF
- `Yosou_Mondaishuu_N2/` — 1 PDF, 56 audio tracks

**textbooks**

- `Bunka_Chukyu_Nihongo_1/` — 1 PDF


### N3

**vocabulary**

- `Mimi_Kara_Oboeru_N3-Goi/` — 1 PDF, 62 audio tracks
- `Nihongo_Soumatome_N3-Goi/` — 1 PDF
- `Shin_Kanzen_Master_N3-Goi/` — 1 PDF
- `Speed_Master_N3-Goi/` — 1 PDF, 45 audio tracks

**kanji**

- `Kanji_Master_N3/` — 1 PDF
- `Nihongo_Soumatome_N3-Kanji/` — 1 PDF
- `Shin_Kanzen_Master_N3-Kanji/` — 1 PDF

**grammar**

- `Mimi_Kara_Oboeru_N3-Bunpou/` — 1 PDF, 11 audio tracks
- `Nihongo_Soumatome_N3-Bunpou/` — 1 PDF
- `Shin_Kanzen_Master_N3-Bunpou/` — 1 PDF
- `Speed_Master_N3-Bunpou/` — 1 PDF

**reading**

- `55_Reading_Comprehension_Level_3/` — 1 PDF
- `Nihongo_Soumatome_N3-Dokkai/` — 1 PDF
- `Speed_Master_N3-Dokkai/` — 1 PDF

**listening**

- `Mimi_Kara_Oboeru_N3-Choukai/` — 1 PDF, 90 audio tracks
- `Nihongo_Soumatome_N3-Choukai/` — 1 PDF, 117 audio tracks
- `Shin_Kanzen_Master_N3-Choukai/` — 1 PDF, 133 audio tracks
- `Speed_Master_N3-Choukai/` — 1 PDF, 140 audio tracks

**multi-skill**

- `20_Nichi_de_Goukaku_N3/` — 1 PDF
- `Goukaku_Dekiru_N3/` — 1 PDF, 122 audio tracks
- `JLPT_N3_Taisaku_Mondai&Yoten_Seiri/` — 1 PDF
- `JLPT_Taisaku_N3-Bunpou-Goi-Kanji/` — 1 PDF
- `Pattern_Betsu_Tettei_Drill_N3/` — 1 PDF, 97 audio tracks
- `Tanki_Master_Drill_N3/` — 1 PDF, 54 audio tracks

**mock-tests**

- `JLPT_N3_Kanzen_Moshi/` — 1 PDF, 123 audio tracks
- `JLPT_Super_Moshi_N3/` — 1 PDF
- `N3_Mondai/` — 1 PDF
- `Yosou_Mondaishuu_N3/` — 1 PDF, 52 audio tracks


### N4

**vocabulary**

- `Kirari_Nihongo_N4_Goi/` — 1 PDF
- `Nihongo_Challenge_Kotoba_N4/` — 1 PDF

**kanji**

- `Nihongo_Challenge_Kanji_N4-N5/` — 1 PDF

**grammar**

- `Mimi_Kara_Oboeru_N4-Bunpou/` — 1 PDF, 11 audio tracks

**reading**

- `Jitsuryoku_Appu_JLPT_N4-Yomu/` — 1 PDF

**multi-skill**

- `Goukaku_Dekiru_N4-N5/` — 2 PDF, 133 audio tracks
- `Nihongo_Challenge_Bunpo_to_Yomu_N4/` — 1 PDF

**mock-tests**

- `JLPT_Koushiki_Mondaishuu_N4/` — 1 PDF, 39 audio tracks
- `JLPT_Super_Moshi_N4-N5/` — 2 PDF, 120 audio tracks
- `The_Official_Guide_Book_JLPT_N4-N5/` — 1 PDF, 26 audio tracks


### N5

**multi-skill**

- `Tanki_Master_Drill_N5/` — 1 PDF, 46 audio tracks

**mock-tests**

- `JLPT_Koushiki_Mondaishuu_N5/` — 1 PDF, 35 audio tracks

**textbooks**

- `Chukyu_Honsatsu/` — 1 PDF
- `Shochukyu_Honsatsu/` — 1 PDF
- `Shokyu_Honsatsu/` — 1 PDF

