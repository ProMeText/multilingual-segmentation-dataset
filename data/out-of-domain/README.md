# Out-of-Domain (OOD) Data

To assess generalization across domains and languages, evaluations are conducted on HTR-derived transcripts and on languages not included in the training corpus.

This folder contains the dataset for **out-of-domain (OOD) evaluation**, designed to test the model’s **robustness** and **generalization capacity** beyond the training languages.

It includes:
- **Languages not represented in the training data**, but closely related to those in the core dataset. These are used exclusively to evaluate cross-lingual generalization (e.g., Occitan for Catalan).
- **HTR-derived outputs**, used to evaluate robustness to differences in **input modality**, since HTR data systematically diverge from curated editions.  
  Typical sources of variation include:
  - lineation and foliation artifacts  
  - hyphenation at line breaks  
  - sparse or irregular punctuation  
  - character confusions  
  - merged or split word boundaries  
  - diacritic inconsistencies  
  - abbreviation-expansion issues  
  - minimal normalization  



# Textual sources
## Evaluation on Closely Related Languages

### Medieval Occitan
- **Legenda aurea (Sanh Julia Martir), Giacomo da Varazze (Iacobus de Voragine)**  
  Religious prose, Occitan translation (Version B), 15th century.
  Monika Tausend (ed.), *Die altokzitanische Version B der «Legenda aurea» (Ms. Paris, Bibl. Nat., n. acq. fr. 6504)*, Tübingen, Niemeyer, 1995 (Beihefte zur Zeitschrift für romanische Philologie, 262), pp. 291-295.  
  Available online: [RIALTO – Prosa religiosa](https://www.rialto.unina.it/prosa_religiosa/la73/)  

- **Viage al Purgatory, Ramon de Perellos**  
  A narrative prose work, originally composed in Occitan at the end of the 14th century.
  Margherita Boretti (ed.), based on ms. Auch, Archives Départementales du Gers, I, 4066 (formerly Bibliothèque du Grand Séminaire d’Auch, n. 12942).  
  Available online: [RIALTO – Prosa narrativa](https://www.rialto.unina.it/prosa_narrativa/viage-al-purgatory/)  

- **Las vertutz de las herbas** (anonymous)  
  A pharmaco-medical treatise originally composed in Occitan at the end of the 13th and beginning of the 14th century.  
  Maria Sofia Corradini, Online edition based on Princeton, Garrett MS 80 (ff. 15v–21v).  
  Available online: [RIALTO – Testi pratici](https://www.rialto.unina.it/testi_pratici/las-vertutz-de-las-herbas/#princeton)

  
- **Roman de Philomena**, *manuscript P* (anonymous)  
  Religious and heroic prose — *BnF, Ms. fr. 2232*, late 13th or early 14th century.  
  The text corresponds to the Occitan *Volgarizzamento provenzale della Gesta Caroli Magni*. Text automatically transcribed, with post-normalization.  
  Available online: Wiedner, Marinus (ed.) (2025), **COMETA: Corpus de l’occitan médiéval comparatif et annoté — Provence et Languedoc**, *BnF, Français 2232*. [Zenodo record](https://zenodo.org/records/15300719)  

## Evaluation on HTR Outputs

### **De regimine principium, Giles of Rome**
- Biblioteca de Catalunya, Ms. 739, 14ᵗʰ–15ᵗʰ century, catalan
- BNF Arsenal 5062 (1444), french
- Genève, Bibliothèque de Genève, Ms. lat. 92, 460–1480, latin

### **Lancelot en prose** (anonymous)  
  French, 13th–15th century.  
  Chunks randomly sampled from different manuscript witnesses, notably *BnF, Ms. fr. 751* and *BnF, Ms. fr. 111*.  
  Language: Old French.

### **Ab Urbe Condita**, Livy — *Castilian translation by Pero López de Ayala*  
  Castilian, late 14th century.  
 *El Escorial, Real Biblioteca, Ms. h-I-11*   
