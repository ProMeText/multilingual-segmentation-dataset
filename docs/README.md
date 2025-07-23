# 📚 Documentation – Multilingual Segmentation Corpus

This `docs/` folder contains the complete documentation for the multilingual segmentation dataset.  
It aims to ensure clarity, reproducibility, and transparency in the construction and usage of the segmented corpora.

---

## 📁 Structure of `docs/`

### `metadata/`
Contains general information about the included corpora.

- `corpora_overview.csv`:  
  Summary table listing all corpora, languages, segmentation types, sources, and notes.

### `annotation_guidelines/`
Describes how sentence segmentation and tokenization were handled across languages.

- `segmentation_criteria.md`:  
  Guidelines for sentence-level segmentation, including language-specific rules and examples.

- `word_delimiters.md`:  
  Conventions used to define word boundaries (e.g. treatment of elisions, hyphenation, apostrophes).

### `sources/`
Provides bibliographic and textual references for the source materials used.

- `editions_used.md`:  
  A cross-corpus list of editions and manuscripts from which excerpts were extracted for segmentation.

### `changelog.md`
Log of major changes to the documentation and data structure.

---

## 📌 Notes

- Each corpus (e.g. `lancelot/`, `Multilingual_Aegidius/`) has its own `raw/` and `segmented/` folders under `data/`.
- Segmented data is split into:
  - `pre_split/`: Fully segmented, before train/dev/test partitioning
  - `split/`: Standard ML-ready format (`train/`, `dev/`, `test`)
- This documentation is maintained in English to facilitate international collaboration.

---

## ✍️ Contributing

If you add or modify a corpus, please update:
- `metadata/corpora_overview.csv`
- `sources/editions_used.md`
- `changelog.md` with a clear summary of changes

