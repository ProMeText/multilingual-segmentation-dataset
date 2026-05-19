# Data Collection and Source Tracking

This document summarizes key notes on **text acquisition**, **language-specific sourcing variability**, and **metadata management** across the Multilingual Segmentation Corpus.

---

## Data Collection Variability Across Languages

The process of text acquisition varied considerably depending on the language.

- For some languages, such as **French**, acquisition was straightforward thanks to well-structured resources like the [**BFM Corpus**](https://gitlab.huma-num.fr/bfm/bfm-textes-diffusion/-/tree/main/TXT?ref_type=heads).

- For **Portuguese**, **English**, and **Italian**, we used structured corpora such as the:
  - [**CTA** – Corpus de Textos Antigos](https://teitok.clul.ul.pt/teitok/cta/index.php?action=home)
  - [**LAEME** – Linguistic Atlas of Early Middle English](http://amc.ppls.ed.ac.uk/laeme/texts.html)
  - [**Biblioteca Italiana**](http://www.bibliotecaitaliana.it/percorsi/19)  
  These provided valuable data, though required **more intensive preparation**.

- In contrast, resources like the **OVI** (Italian) and **CICA** (Catalan) offered limited public access, prompting recovery from **critical editions** or **web scraping** when necessary.

This variability required a **flexible, language-sensitive approach** to both **sourcing** and **preprocessing**.

---

## Source Tracking & Metadata

To ensure **transparency**, **consistency**, and **reproducibility**, an internal application form was created to standardize metadata collection for each text in the segmentation corpus.

This form captured key details such as:

-  **Source type** (digital edition, manuscript, OCR, etc.)  
-  **Edition or manuscript reference** (bibliographic citation)  
-  **Linguistic variety** and **chronological range**  
-  **Format and structure** of the original file  
-  **Reuse/licensing conditions**

Although the form itself is not public, we provide access to the **processed metadata** and the **scripts used during compilation**.

---

## 🔗 Resources

- **Data Processing Repository – [`Corpus Temporis App`](https://github.com/ProMeText/CorpusTemporis)**  
  Streamlit app and scripts used to structure, validate, and convert incoming texts and metadata.

- **Compiled Metadata Table – [`data.csv`](https://github.com/ProMeText/CorpusTemporis/blob/main/data.csv)**  
  A centralized CSV listing all processed texts with:
  - Language  
  - Title  
  - Edition or source  
  - Format  
  - License/reuse status  
  - File location references

---

 For contributions or metadata corrections, feel free to open an issue or pull request.
