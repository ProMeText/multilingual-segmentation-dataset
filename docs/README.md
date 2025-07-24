# 📚 Documentation – Multilingual Segmentation Dataset

This `docs/` folder contains the complete documentation for the multilingual segmentation dataset.  
It is designed to support **clarity, reproducibility, and transparency** in the construction and use of the segmented corpora.

The dataset provides a curated, linguistically informed **collection of raw texts and segmented excerpts** drawn from historical and literary works in multiple medieval languages, primarily Romance.

It is intended for tasks such as:

- ✂️ Sentence segmentation
- 📜 Historical linguistic analysis
- 🌍 Cross-linguistic and diachronic comparison of medieval textual traditions

The following documentation provides guidelines on segmentation principles, data structure, language-specific heuristics, and metadata sources used to compile the dataset.

## 📁 `data/` Folder Structure
- Each corpus (e.g. `lancelot/`, `Multilingual_Aegidius/`) corresponds to a specific phase or case study within the project, and includes its own `raw/` and `segmented/` folders under `data/`.

### `raw/`  
📄 **Cleaned, unsegmented texts**

- UTF-8 encoded, markup removed  
- Original orthography, punctuation, and spacing preserved  
- No segmentation applied

### `pre_split/` 
🧾 **Segmented excerpts before dataset partitioning**

- Randomly selected text chunks from `raw/`  
- Manually or heuristically segmented using `£` markers  
- Available in `.txt` 

### `split/`  
🔀 **Ready for machine learning**

- Train/dev/test partitions  
- Provided in both `.txt` and `.json` format  
- Organized by language (`ca/`, `fr/`, etc.), with some multilingual folders for cross-lingual models

## 🛠️ Data Preparation

See [segmentation_processing_pipeline.md](docs/segmentation_processing_pipeline.md) for the full workflow.

## 🧭 How to Use This Documentation

- Researchers can consult segmentation guidelines to reproduce or extend the dataset.
- Annotators can refer to language-specific rules when preparing new corpora.
- Developers can integrate the dataset into NLP pipelines by following the structure described here.

## 📫 How to Contribute

If you wish to add a new corpus or enrich an existing one with additional texts,  
please open an issue in the [application form repository](https://github.com/carolisteia/mulada).
This ensures proper metadata registration and traceability of new materials.

## 📁 Available Documentation

### 📝 Annotation Guidelines
- [`annotation_guidelines/segmentation_criteria_en.md`](annotation_guidelines/segmentation_criteria_en.md) – Main principles and heuristics for sentence segmentation  
- [`annotation_guidelines/main-word-delimiters.json`](annotation_guidelines/main-word-delimiters.json) – Language-specific clause delimiters (used in rule-based preprocessing)

### ⚙️ Processing & Examples
- [`segmentation_processing_pipeline.md`](segmentation_processing_pipeline.md) – Step-by-step description of the preprocessing and data formatting pipeline  
- [`segmentation_exemples.md`](segmentation_exemples.md) – Annotated segmentation examples across languages

### 📊 Metadata
- [`data.csv`](https://github.com/carolisteia/mulada/blob/main/data.csv) – Centralized summary of all source texts, including language, date, genre, edition, and other metadata
> 📍 This file is maintained at the root of the main repository (`mulada/`) and not in the `docs/` folder.

### 🏷️ Repository Structure
- [`README.md`](README.md) – Main documentation index for `docs/`
