<p align="center">
  <img src="assets/banner.png" alt="Multilingual Segmentation Dataset Banner" width="80%">
</p>


# ✂️ Multilingual Segmentation Dataset

> **From manuscripts to models: a multilingual corpus for sentence segmentation in historical prose.**

This dataset gathers carefully segmented excerpts from a wide range of textual genres — including narrative, didactic, legal, theological, and scholarly prose — spanning seven Romance and Latin languages (13th–16th c.).  
Segment boundaries reflect both historical syntax and editorial conventions, making the corpus suitable for training and evaluating sentence segmentation models, as well as for cross-linguistic and diachronic analysis in NLP and digital philology.



## 📖 Overview

This dataset was developed to train a multilingual sentence segmentation model used as a pre-processing step in the automatic alignment of historical texts with [**Aquilign**](https://github.com/ProMeText/aquilign), a multilingual alignment tool developed by our team.  
Once the BERT-based models are trained and selected, they are integrated into the alignment workflow to segment texts based on learned boundary recognition — a critical step preceding the alignment itself.

The segmented excerpts serve as input for Aquilign, enabling multilingual alignment across structurally and editorially diverse texts. A first study applying this pipeline — focused on *Lancelot en prose* — was presented in the 2024 article [*Textual Transmission without Borders*](https://2024.computational-humanities-research.org/papers/paper104/), published as part of the Computational Humanities Research (CHR) conference proceedings.


As the project evolved, the segmentation corpus was gradually expanded alongside the tool. Initially limited to three Romance languages — *Castilian (`es`), French (`fr`), and Italian (`it`)* — it was later enriched with **Portuguese (`pt`)**, **Catalan (`ca`)**, **Latin (`la`)**, and **English (`en`)**, increasing linguistic diversity and enhancing the robustness of cross-linguistic alignment.

To support reproducibility and multilingual evaluation, the dataset is organized by work: each text is stored in a dedicated folder containing the source (`raw/`) and segmented (`segmented/`) versions.


The corpus provides training and evaluation material for **sentence-level segmentation** in **historical prose** from the **13th to 16th centuries**. Texts were selected for their **genre diversity**, as well as their capacity to reflect **editorial**, **orthographic**, and **linguistic variation** across time, geography, and scribal practices.

## 🧾 Summary

| Category           | Details                                                                 |
|--------------------|-------------------------------------------------------------------------|
| **Languages**       | Latin (`la`), French (`fr`), English (`en`), Portuguese (`pt`), Catalan (`ca`), Italian (`it`), Castilian (`es`) |
| **Period Covered**  | 13th–16th centuries                                                    |
| **Text Formats**    | Plain text (TXT), XML, with some material converted from HTML or PDF   |
| **Segmentation**    | Manual sentence segmentation using language-specific criteria          |
| **License**         | [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) – annotations and segmentation metadata only |


## 🎯 Purpose

The primary goal of this dataset is to support the training of machine learning models capable of identifying **sentence and segment boundaries** in **non-standardized historical texts**.  
Reliable segmentation is essential for:

- downstream NLP tasks such as **parsing**, **translation**, and **alignment**,
- enhancing the **accessibility** and reusability of medieval sources,
- enabling **cross-linguistic comparison** and advancing **philological and historical-linguistic research**.


## 🔄 Processing Pipeline

The segmentation pipeline involves the following steps, from raw historical texts to segmented training data.

<p align="center">
  <img src="assets/segmentation_pipeline2.png" alt="Processing pipeline" width="50%">
</p>

See [docs/processing_pipeline.md](docs/segmentation_processing_pipeline.md) for full details on each step.



## 🌐 Data Collection Variability Across Languages

The process of text acquisition varied considerably depending on the language.

- For some languages, such as **Middle French**, acquisition was straightforward thanks to well-structured resources like the [**BFM Corpus**](https://gitlab.huma-num.fr/bfm/bfm-textes-diffusion/-/tree/main/TXT?ref_type=heads).

- For **Portuguese**, **English**, and **Italian**, we used structured corpora such as the [**CTA**](https://teitok.clul.ul.pt/teitok/cta/index.php?action=home), [**LAEME**](http://amc.ppls.ed.ac.uk/laeme/texts.html), and [**Biblioteca Italiana**](http://www.bibliotecaitaliana.it/percorsi/19). These provided valuable data, though required **more intensive preparation**.

- In contrast, resources like the **OVI** (Italian) and **CICA** (Catalan) offered limited public access, prompting recovery from **critical editions** or **web scraping** when necessary.

This variability demanded a **flexible, language-sensitive approach** to both **sourcing** and **preprocessing**.

[Jump to Source Tracking & Metadata for more detailed information ⤵️](#source-tracking--metadata)

---

## 🛠️ Data Preparation

Texts were collected in various formats—preferably **TXT** or **XML**, though **HTML** and **PDF** sources were also used.  
All files were **cleaned using regular expressions** to normalize:

- punctuation  
- whitespace and line breaks  
- markup and non-content tags

**Segmentation** was applied using a mix of **rule-based heuristics** and **manual correction**. For certain languages, **custom scripts** addressed specific editorial or typographic issues.

### 🔎 Example of Manual Segmentation

To prepare training data for segmentation models, we first **manually annotate sentence or segment boundaries** using the **pound sign (`£`)**. Each `£` indicates the end of a sentence or segment. This annotated format is then used as a reference for **model training and evaluation**. These annotations reflect syntactic and rhetorical units rather than strict modern sentence rules.

Below are examples from three languages in the corpus.

### 🇵🇹 Portuguese

**Raw annotated with `£`:**

```text
E entom se espedyo dom Lourenço del rey.£E, en se hindo,£tornou a elle£e disselhe:£- Senhor, ainda venho a vos£por vos avisar do que vos compre:£mandaae logo fazer esta noite£e as outras duas ou tres seguintes£muytos fogos batalhas contra seus Jrmããos .£e contra outros seus contrayros
```

**→ Segments:**

1. E entom se espedyo dom Lourenço del rey.  
2. E, en se hindo,  
3. tornou a elle  
4. e disselhe:  
5. -- Senhor, ainda venho a vos  
6. por vos avisar do que vos compre:  
7. mandaae logo fazer esta noite  
8. e as outras duas ou tres seguintes  
9. muytos fogos batalhas contra seus Jrmããos .  
10. e contra outros seus contrayros

### 🇮🇹 Italian

**Raw annotated with `£`:**

```text
Maus frutto, cioè musa.£Questo frutto è molto gentile e dolce,£della grandezza de' cetriuoli piccoli,£e nasce di piccola pianta,£e ha le foglie grande, larghe e lunghe un braccio.£Dicono i timore e maraviglia ne' cuori umani.£E nondimeno è a queste genti così associabile e commune£che non solamente il tengono figurato in una parte della casa,£ma ne' banchi anco dove seggono, volendo significare£che colui che siede non sta solo,£ma siede insieme con l'aversario di tutti;
```


**→ Segments:**

1. Maus frutto, cioè musa.
2. Questo frutto è molto gentile e dolce,
3. della grandezza de' cetriuoli piccoli,
4. e nasce di piccola pianta,
5. e ha le foglie grande, larghe e lunghe un braccio.
6. Dicono i timore e maraviglia ne' cuori umani.
7. E nondimeno è a queste genti così associabile e commune
8. che non solamente il tengono figurato in una parte della casa,
9.  ma ne' banchi anco dove seggono, volendo significare
10. che colui che siede non sta solo,
11. ma siede insieme con l'aversario di tutti;

### 🇪🇸 Castilian

**Raw annotated with `£`:**

```text
Por tal lo tengo yo£dixo don Duardos£& no puedo yo creer£que yo le sobrasse£pidole por merced£que me perdone que mi desseo es de seruille.£Señor£dixo la reyna£mal contado seria a tan grande hombre como vos.
```

**Segments:**

1. Por tal lo tengo yo  
2. dixo don Duardos  
3. & no puedo yo creer  
4. que yo le sobrasse  
5. pidole por merced  
6. que me perdone que mi desseo es de seruille.  
7. Señor  
8. dixo la reyna  
9. mal contado seria a tan grande hombre como vos.


## ✂️ Segmentation Criteria

The segmentation of texts in this corpus follows a hybrid approach, combining **rule-based heuristics**, **philological insight**, and **language-specific patterns**. The aim is to identify boundaries between meaningful textual units—typically clauses or sentences—without imposing rigid modern standards on medieval prose.

### ✅ Guiding Principles

Segmentation is guided by the following core principles:

- **Structural segmentation**: A new segment is created when a text introduces a new syntactic unit, often marked by punctuation (e.g. `.`, `:`, `;`, `?`, `!`, `¶`) or coordinating/subordinating markers.
- **Functional coherence**: Segments generally contain a complete verbal unit. We avoid breaking inside syntactic constituents unless justified by strong cues.
- **Philological sensitivity**: Medieval usage is respected. Editorial norms (e.g. punctuation or spacing) are interpreted cautiously, especially in texts where these features are not standardized.

### 🌍 Language-Specific Heuristics

Each language in the corpus has its own set of **typical delimiters**, drawn from recurrent **conjunctions**, **relative pronouns**, **discourse markers**, and **prepositional phrases**. These were defined empirically and encoded in [`main-word-delimiters.json`](https://github.com/ProMeText/Multilingual_Aegidius/blob/main/data/segmentation_data/no_split/main-word-delimiters.json)).

Some representative examples:

- **Latin**: `quod`, `cum`, `ut`, `et`, `sed`, `aut`  
- **French**: `car`, `mais`, `ains`, `quant`, `donc`, `si`  
- **Castilian**: `pues`, `porque`, `aunque`, `cuando`, `entonces`, `si`  
- **Italian**: `che`, `perché`, `dunque`, `anzi`, `ma`, `poi`  
- **Catalan**: `que`, `car`, `per això`, `adonchs`, `pus que`, `emperò`  
- **English**: `þat`, `and þat`, `also`, `whan`, `so þat`
- **Portuguese**: `porquuoanto`, `desy`, `todavya`, `outrossy`, `bẽ assy como` ...

### 🧠 Annotation Guidelines

We segment:

- At **conjunctions** that introduce a finite clause  
- Before **relative or interrogative pronouns** when they mark syntactic rupture  
- At **discourse openings**, especially after speech verbs  
- After **adverbs** (e.g. *tant*, *or*, *lors*, *atant* in Middle French), when they mark the beginning of a new clause
- At **prepositions** followed by a relative pronoun  

We avoid segmentation:

- Inside **enumerations** without verbal structure  
- On ambiguous markers used mid-clause (*et*, *ne*, *si*)  
- On **truncated fragments** unless the completion is clear  

> Example:  
> In “*Et quant il voit cele par cui*...”, the segment begins with “*Et*” only.  
> In “*Si tost com il la vit, il s’enfuit*”, the tokenized segment starts at “*Si*”.

### ⚠️ Edge Cases

- **Agglutinated forms** (e.g. *quil*, *sil*, *tantqu’il*) are valid triggers  
- Only the **first** of successive potential delimiters is used  
- In absence of punctuation, **syntactic cues** guide the split

---

## 🧾 Source Tracking & Metadata

An internal **application form** was created to standardize the collection process. It allowed for the **documentation, organization, and traceability** of every text included in the corpus.

**Resources:**

<!-- - 📄 Application Form (internal, not publicly released)   -->
- 📂 [Code Repository](https://github.com/carolisteia/mulada)  
- 📊 [Compiled Data CSV](https://github.com/carolisteia/mulada/blob/main/data.csv)


---

## 📁 Folder Structure

### `raw/`  
📄 **Cleaned, unsegmented texts**

- UTF-8, markup removed  
- No segmentation applied

### `no_split/`  
🧾 **Manually segmented excerpts**

- Randomly selected text chunks annotated with `£` markers
- Not split into train/dev/test

### `split/`  
🔀 **Ready for training**

- Monolingual folders (`ca/`, `fr/`, etc.)  
- Train/dev/test splits  
- `.json` files with `£`-marked segmented examples
- Multilingual versions for cross-lingual training

---
## 📊 Corpus Size

The current version of the corpus includes segmented excerpts in **seven historical languages**, prepared for sentence segmentation tasks.

Each excerpt is annotated using the pound sign (`£`) to mark **segment boundaries**, typically corresponding to sentences or syntactic units. The corpus does **not include part-of-speech tagging or syntactic annotation**—only sentence-level segmentation.

| Language         | Texts | Segmented Tokens | Segments (`£`) | Train/Dev/Test? |
|------------------|-------|------------------|----------------|-----------------|
| **Latin** (`la`)       | 557   | 85,888              | 8,366          | ✅              |
| **French** (`fr`)      | 1,526 | 160,472             | 11,774         | ✅              |
| **English** (`en`)     | 152   | 27,072              | 2,315          | ✅              |
| **Portuguese** (`pt`)  | 987   | 101,565             | 10,477         | ✅              |
| **Catalan** (`ca`)     | 388   | 38,441              | 2,879          | ✅              |
| **Italian** (`it`)     | 2,649 | 85,290              | 6,347          | ✅              |
| **Castilian** (`es`)   | 1,436 | 111,811             | 8,091          | ✅              |
| **Total**              | 7,695 | 610,539             | 50,249         | ✅              |

**Legend:**

- **Texts** = total number of annotated examples (i.e. segmented lines)  
- **Segmented Tokens** = total number of tokens (excluding `£`)  
- **Segments (`£`)** = total number of `£` delimiters → i.e. segments  
- **Train/Dev/Test?** = indicates whether `train.json`, `dev.json`, and `test.json` are all present



> ℹ️ This corpus focuses on **sentence segmentation only**. It does **not include POS tagging, syntactic trees, or named entity annotations**.


## 🚧 Project Status

This corpus is part of an **ongoing project**. While it is already being used for segmentation and alignment tasks, **further improvements, refinements, and corrections are expected**.  
We welcome feedback, error reports, and contributions to help improve the resource over time.

Please note:
- Some segmentations may be revised in future updates.
- Metadata and annotations are subject to enhancement.
- Additional languages and texts will be added as the project evolves.


## 🔮 Future Directions

- Extend language coverage  
- Evaluate segmentation models  
- Broaden genre and period diversity  
- Encourage interdisciplinary use

---

## 📄 Licensing

All annotations, segmentations, and metadata are released under [**CC BY-NC-SA 4.0**](https://creativecommons.org/licenses/by-nc-sa/4.0/).  
> ⚠️ Original textual content may be subject to source-specific licenses. Refer to the `sources` and `corpus` columns in the metadata CSV.   

[Jump to compiled data CSV ⤵️](https://github.com/carolisteia/mulada/blob/main/data.csv)



---
## 📚 How to Cite This Corpus

> **Citation (draft)**  
> Please cite as:  
> Macedo, C., Ing, L., & Gille Levenson, M. (2025). *Multilingual Segmentation Corpus for Historical Prose (13th–16th c.)*. GitHub repository, ongoing.  
> 📌 Formal publication and DOI pending.  

## 📫 Contact & Contributions
- [Open an issue or pull request](https://github.com/ProMeText/Multilingual_Aegidius/issues)

- For academic collaboration, please reach out via GitHub Discussions
