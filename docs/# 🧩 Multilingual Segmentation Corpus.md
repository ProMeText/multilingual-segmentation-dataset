# 🧩 Multilingual Segmentation Corpus

This repository provides a curated and linguistically-informed dataset of segmented textual excerpts from multiple historical and literary works, in multiple languages (French, Latin, Spanish, Italian).

The corpus is designed for use in sentence segmentation tasks, linguistic analysis, and comparative studies across languages and textual traditions.

---

## 📚 Repository Structure

```plaintext
data/
├── lancelot/
│   ├── raw/               # Cleaned source excerpts
│   └── segmented/
│       ├── pre_split/     # Fully segmented, before ML splitting
│       └── split/         # Segmented and split into train/dev/test
├── Multilingual_Aegidius/
│   ├── raw/
│   └── segmented/
│       ├── pre_split/
│       └── split/

docs/
├── README.md                      # This file
├── metadata/
│   └── corpora_overview.csv       # Summary of all corpora
├── annotation_guidelines/
│   ├── segmentation_criteria.md   # Sentence segmentation strategy
│   └── word_delimiters.md         # Rules for token-level boundaries
├── sources/
│   └── editions_used.md           # Bibliographic sources for excerpts
└── changelog.md                   # History of changes

## 🌍 Languages Covered

- **French** (`fr`)
- **Latin** (`la`)
- **Spanish** (`es`)
- **Italian** (`it`)

Each corpus may contain excerpts in one or more of these languages, depending on its source material.

---

## 🧪 Segmentation Structure

Each work (e.g. `lancelot`, `Multilingual_Aegidius`) includes:

- `raw/`: Cleaned textual excerpts selected from manuscripts or editions.
- `segmented/pre_split/`: Fully segmented at the sentence level, but **not yet split** into training/dev/test sets.
- `segmented/split/`: Same content as `pre_split/`, but partitioned for machine learning purposes:
  - `train/`
  - `dev/`
  - `test/`

> 💡 **Note**: `pre_split` texts are **already segmented**. The name refers only to their state before data partitioning.

---

## 📖 Documentation

See the [`docs/`](docs/) folder for detailed guidelines:

- [`segmentation_criteria.md`](docs/annotation_guidelines/segmentation_criteria.md): How segmentation was done
- [`word_delimiters.md`](docs/annotation_guidelines/word_delimiters.md): Word boundary conventions
- [`corpora_overview.csv`](docs/metadata/corpora_overview.csv): List of corpora, languages, and sources
- [`editions_used.md`](docs/sources/editions_used.md): Editions and manuscripts used
- [`changelog.md`](docs/changelog.md): Log of structural and data updates

---

## 🧰 Usage

This dataset can be used for:

- Training and evaluating sentence segmentation models
- Cross-linguistic comparison of syntactic structures
- Digital philology and historical linguistics research
- Pedagogical use in linguistics and NLP courses

---

## 🧾 License

**[Specify your license here]**  
We recommend [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) for academic reuse.

---

## 👥 Credits

This dataset was developed by the **ProMeText Project**  
Contributions from researchers in NLP, digital philology, and computational linguistics.

Visit [https://github.com/ProMeText](https://github.com/ProMeText) for more related projects.

---

## 🛠 How to Contribute

- Add new corpora in `data/<your_corpus>/`
- Follow existing directory and file conventions
- Document your corpus in `docs/`
- Update `docs/metadata/corpora_overview.csv` and `docs/sources/editions_used.md`
- Add a note in `docs/changelog.md`
