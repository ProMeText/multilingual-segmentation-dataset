
# Segmentation Criteria
> ⚠️ **Note:** This is **version 1.0** of the segmentation guidelines. These rules may evolve as the dataset grows and new languages are incorporated.


This document outlines the core principles for segmenting clauses or discourse boundaries in the corpus. Segmentation is based on **syntactic structure** and **rhetorical cues**, rather than punctuation alone.


The following sections present the main segmentation cases, showing how the **general principles** apply to different syntactic structures and contexts. They are organized by grammatical category and sentence function, and each case is illustrated with examples.

- [What do we segment?](do_segment.md)
- [When not to segment](not_segment.md)

## Annotation Mark for Clause Segmentation
During the annotation process, **clause boundaries** are marked with a dedicated delimiter. The symbol **£** is employed for this purpose, as it does not occur in the original source texts and therefore avoids any interference with the transcription. The delimiter is **placed immediately before** (i.e., attached to) **the element that triggers segmentation**. The following Portuguese example illustrates the use and placement of the annotation mark:

> £que Eu he huũ primo meu £que había nome José ab aramatia £o deçemos da cruz £quãdo lhe derõ o corpo. £he tomou muy honrradamẽte £he poo lo en huũ seu moymento £o cual tinha feito pera si. £de que os judeus ouuerõ muy grande enveja.

## **Editorial Note:** 
- **Orthography and Tokenization**

Segmentation follows the **orthographic conventions** of the source text and the **initial tokenization** adopted in the edition or corpus.  
All **attested spellings** are preserved according to their historical graphical form; no normalization is applied.

- **Agglutinated forms**
  
Certain **agglutinated forms** — such as french *quil, sil, selle, quelles*— result from the fusion of a **subordinating conjunction and a personal pronoun**.  
These are **retained as single tokens**, respecting manuscript orthography and ensuring consistent tokenization across the corpus.

- **Initial tokenization**
  
The **initial tokenization of the source text** determines which elements are segmented or tagged.  
When a form appears as two tokens but represents a single lexical or grammatical unit, the **attested editorial segmentation** is followed.

> **Example:**  
> *A tans sen taist le* → *A tans*, written as two tokens, actually corresponds to the adverb *Atant*.  
> Only the first token (*A*) is tagged, following the attested form.


- **Textual Irregularities, OCR Artifacts, and Abbreviations**

Some source materials contain **noisy or partially corrected transcriptions**, including **OCR-generated errors**, **typos**, or **undeveloped abbreviations** that have not been expanded.  
These irregular forms — whether arising from **automatic recognition**, **editorial transmission**, or **the original witness** — are **preserved as attested**, in accordance with the editorial principle of **non-normalization**.  


> **Examples of OCR or typographical noise:**  
> `l = I` — in the Italian corpus, *lnsi* is retained for *Insi*.  
> `1 = l` — in the Catalan corpus, *1 milor* reflects OCR confusion.  
> `,£no falira £tro que•1 milor chavaler del mon e•1 pus beyl hi vengua`

> **Examples of unexpanded abbreviations:**  
> `£q fizesse rogaria por ele a nosso snor jhesu`  
> `£que se elle rogasse a ds por elle`  


> **Example of a noisy raw transcription:**  
> nada qu'entorn eyla agues tot jorn aytal bayla, e gran plaser n'auria, e si o dix aysi at que•1 clergue qui pres li era, qui molt se prenia guarda d'eyla, o entes e si s'acosta ad eyla, e li dix :o(Donzela, si vos ho vol{etz, encara•yc seria mayor e







