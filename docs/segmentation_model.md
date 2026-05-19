# Multilingual Sentence Segmenter for Historical Texts

This document introduces a pretrained **BERT-based sentence segmentation model**, fine-tuned on the *Multilingual Segmentation Dataset* (13th–16th c.).  
The model is specifically designed for **historical prose texts** in **medieval Romance languages**, **Latin**, and **Middle English**, and is used to improve segmentation quality in downstream alignment tasks (e.g. with [Aquilign](https://github.com/ProMeText/Aquilign)).

It supports **seven historical languages** — **Catalan**, **Castilian**, **English**, **French**, **Italian**, **Latin**, and **Portuguese** — and has been evaluated on two benchmark corpora:

- 📘 [**Lancelot en prose**](https://github.com/carolisteia/lancelot-par-maints-langages)  
- 📗 [**De regimine principum**](https://github.com/ProMeText/Multilingual_Aegidius)  

In both cases, the BERT-based approach outperforms regex-based segmentation baselines, substantially reducing error propagation in alignment and collation workflows.

---

### 📄 This document provides:

-  Model architecture and training setup  
-  Training instructions and command-line usage  
-  Input format and data schema  
-  Language codes and delimiter conventions  

> 📎 For annotation principles, see the [Segmentation Guidelines](https://github.com/carolisteia/multilingual-segmentation-dataset/tree/main/docs/annotation_guidelines)  
> 📎 For access to training data, consult the [Multilingual Segmentation Data repository](https://github.com/carolisteia/multilingual-segmentation-dataset/tree/main/data)

---

## Model Availability

We provide a **pretrained multilingual BERT-based sentence segmentation model**, fine-tuned on the full *Multilingual Segmentation Corpus* (13th–16th c.), covering **seven historical languages** and optimized for **prose texts**.

### 🔍 Model Architecture & Training

The model is implemented with Hugging Face’s `AutoModelForTokenClassification`, trained to predict `£` delimiters corresponding to sentence or clause boundaries.  
Initial training focused on **French**, **Castilian**, and **Italian**, and was later generalized across the full language set.

 Available on Hugging Face:  
👉 [`ProMeText/aquilign-multilingual-segmenter`](https://huggingface.co/ProMeText/aquilign-multilingual-segmenter)

> Looking for **monolingual models**?  
> 👉 See our [Hugging Face model hub](https://huggingface.co/ProMeText) for language-specific variants.

---


### Performance Highlights

Evaluations below are based on the *Lancelot en prose* corpus (used in early training stages). Results from the broader *Multilingual Aegidius* corpus will be added soon.

| Language   | Regex F1 | BERT F1 | Δ F1 |
|------------|----------|---------|------|
| French     | 0.706    | 0.906   | +0.20 |
| Italian    | 0.606    | 0.846   | +0.24 |
| Castilian  | 0.636    | 0.866   | +0.23 |

The model significantly improves **segment boundary detection** and reduces **alignment errors** in multilingual pipelines such as [Aquilign](https://github.com/ProMeText/Aquilign).

 See [*Textual Transmission without Borders* (CHR 2024)](https://ceur-ws.org/Vol-3834/paper104.pdf) for evaluation details.

---

##  Training the Segmenter

The model is trained using Hugging Face’s `BertForTokenClassification` on historical data annotated with custom sentence delimiters (`£`).

---

### Example Command

```bash
python3 train_tokenizer.py \
  -m google-bert/bert-base-multilingual-cased \
  -t multilingual-segmentation-data/data/Multilingual_Aegidius/segmented/split/multilingual/train.json \
  -d multilingual-segmentation-data/data/Multilingual_Aegidius/segmented/split/multilingual/dev.json \
  -e multilingual-segmentation-data/data/Multilingual_Aegidius/segmented/split/multilingual/test.json \
  -ep 100 \
  -b 128 \
  --device cuda:0 \
  -bf16 \
  -n multilingual_model \
  -s 2 \
  -es 10
```
**Config summary**:

- **Epochs**: 100  
- **Batch size**: 128  
- **Device**: GPU (`cuda:0`)  
- **Precision**: `bf16` (mixed)  
- **Checkpointing**: every 2 epochs  
- **Early stopping**: after 10 epochs without improvement

---

##  Input Format

Training data must follow a specific **JSON schema** with a metadata header and a list of examples:

```json
{
  "metadata": {
    "lang": ["la", "it", "es", "fr", "en", "ca", "pt"],
    "centuries": [13, 14, 15, 16],
    "delimiter": "£"
  },
  "examples": [
    {
      "example": "que mi padre me diese £por muger a un su fijo del Rey",
      "lang": "es"
    },
    {
      "example": "Per fé, disse Lion, £i v’andasse volentieri, £ma i vo vegg

```

###  Required fields

The `metadata` block must include the following fields:

- `"delimiter"` — the segmentation marker used in the corpus (e.g. `£`)
- `"lang"` — a list of ISO 639-1 language codes covered in the examples
- `"centuries"` — a list of century values for metadata purposes (e.g. `[13, 14, 15, 16]`)

Each entry in the `"examples"` list must contain:

- `"example"` — a text string with segmentation delimiters (`£`) inserted
- `"lang"` — the language of the example, matching a code from the `"lang"` array

---

##  Language Codes

Use standard **ISO 639-1** codes as identifiers for supported languages:

| Language    | Code |
|-------------|------|
| Latin       | `la` |
| Italian     | `it` |
| Castilian   | `es` |
| French      | `fr` |
| English     | `en` |
| Catalan     | `ca` |
| Portuguese  | `pt` |

These codes must **match exactly** those defined in:  
[`docs/annotation_guidelines/main-word-delimiters.json`](https://github.com/carolisteia/multilingual-segmentation-data/blob/main/docs/annotation_guidelines/main-word-delimiters.json)

This mapping is also used for the **regex-based segmentation baseline**.

---

 **Note**: This training setup assumes access to segmentation data under the following directory:

```bash
multilingual-segmentation-data/data/Multilingual_Aegidius/segmented/split/
```

## Summary

This segmentation model is designed to support robust sentence boundary detection in **historical multilingual texts**, particularly in Latin and Romance languages from the 13th–16th centuries.

It improves the quality of **downstream alignment**, **translation modeling**, and **textual analysis** by providing accurate, linguistically informed segment boundaries that go beyond what simple rule-based approaches can capture.

By using the provided training format and pretrained model, you can:

- Fine-tune new models on additional languages or text types  
- Extend to new delimiters or segmentation strategies  
- Combine with Aquilign or other alignment tools for improved multilingual processing



