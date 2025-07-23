# 📚 Documentation – Multilingual Segmentation Corpus

This `docs/` folder contains the complete documentation for the multilingual segmentation dataset.  
It aims to ensure clarity, reproducibility, and transparency in the construction and usage of the segmented corpora.

---
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

