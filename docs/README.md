# Documentation – Multilingual Segmentation Dataset

This `docs/` folder contains the full documentation for the **Multilingual Segmentation Dataset**,  
designed to support clarity, reproducibility, and transparency in its construction and usage.

The dataset includes a curated, linguistically informed collection of **raw and segmented excerpts** drawn from historical literary works in multiple medieval languages, primarily Romance.

It supports tasks such as:

- Sentence segmentation  
-  Historical linguistic analysis  
-  Cross-linguistic and diachronic comparison of medieval texts  

The documentation outlines segmentation principles, data structures, heuristics, and metadata sources used to compile the corpus.

---

##  `data/` Folder Structure

Each subcorpus (e.g. `lancelot/`, `Multilingual_Aegidius/`) includes its own `raw/` and `segmented/` directories.

### `raw/`  
 **Cleaned, unsegmented texts**  
- UTF-8 encoded, markup removed  
- Original orthography, punctuation, and spacing preserved  
- No segmentation applied

### `pre_split/`  
 **Manually or heuristically segmented excerpts**  
- Extracted from `raw/`  
- Marked with `£` for sentence/segment boundaries  
- Available in `.txt` format

### `split/`  
 **Machine learning partitions**  
- Train/dev/test sets  
- In both `.txt` and `.json`  
- Organized by language (`ca/`, `fr/`, etc.) or multilingual folders

---

##  Data Preparation

➡️ See [`segmentation_processing_pipeline.md`](segmentation_processing_pipeline.md) for the full preprocessing workflow.

---

## How to Use This Documentation

- **Researchers**: reproduce or extend the dataset using segmentation guidelines  
- **Annotators**: follow language-specific segmentation criteria  
- **Developers**: integrate the dataset into NLP pipelines with the documented structure

---

## How to Contribute

To contribute new corpora or enrich existing ones, please open an issue in the  
[mulada repository](https://github.com/carolisteia/mulada), which registers new datasets and metadata.

---

## Complete Documentation Index

### Annotation Guidelines
- [`annotation_guidelines/segmentation_criteria_en.md`](annotation_guidelines/segmentation_criteria_en.md) – Main principles and heuristics  
- [`annotation_guidelines/main-word-delimiters.json`](annotation_guidelines/main-word-delimiters.json) – Regex-based clause delimiters by language

### Processing & Examples
- [`segmentation_processing_pipeline.md`](segmentation_processing_pipeline.md) – Step-by-step preprocessing workflow  
- [`segmentation_exemples.md`](segmentation_exemples.md) – Annotated segmentation examples across languages

### Segmentation Model
- [`segmentation_model.md`](segmentation_model.md) – Description of the pretrained multilingual BERT model and training instructions for historical sentence segmentation

### Metadata
- [`data.csv`](https://github.com/carolisteia/mulada/blob/main/data.csv) – Metadata for all source texts (languages, genres, editions, etc.)  
> 📍 Maintained at the root of the `mulada` repository.

### Data Collection & Source Tracking  
- [`data_collection_and_source_tracking.md`](data_collection_notes.md) – Language-specific sourcing notes, access challenges, and metadata compilation practices across the corpus

### Repository Structure
- [`README.md`](README.md) – 📌 This file
