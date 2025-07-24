# 🔎 Annotated Segmentation Examples

This page presents representative examples of sentence segmentation using the `£` delimiter across multiple languages included in the corpus.

To prepare training data for segmentation models, we first **manually annotate sentence or segment boundaries** using the **pound sign (`£`)**. Each occurrence of `£` marks the **end of a sentence or discourse unit**.  
These annotations serve as the **ground truth** for model training and evaluation, and reflect **syntactic and rhetorical structure** rather than strictly modern sentence conventions.

Below are representative examples from three languages in the corpus.

> 🔍 *The examples below are shortened excerpts selected for illustration purposes only. They do not represent full source texts.*

---

## 🇵🇹 Portuguese

**Raw with `£`:**
```
E entom se espedyo dom Lourenço del rey.£E, en se hindo,£tornou a elle£e disselhe:£- Senhor, ainda venho a vos£por vos avisar do que vos compre:£mandaae logo fazer esta noite£e as outras duas ou tres seguintes£muytos fogos batalhas contra seus Jrmããos .£e contra outros seus contrayros
```

**Segmented:**
- E entom se espedyo dom Lourenço del rey.
- E, en se hindo,
- tornou a elle
- e disselhe:
- Senhor, ainda venho a vos
- por vos avisar do que vos compre:
- mandaae logo fazer esta noite
- e as outras duas ou tres seguintes
- muytos fogos batalhas contra seus Jrmããos .
- e contra outros seus contrayros

---

## 🇮🇹 Italian

**Raw with `£`:**
```
Maus frutto, cioè musa.£Questo frutto è molto gentile e dolce,£della grandezza de' cetriuoli piccoli,£e nasce di piccola pianta,£e ha le foglie grande, larghe e lunghe un braccio.£Dicono i timore e maraviglia ne' cuori umani.£E nondimeno è a queste genti così associabile e commune£che non solamente il tengono figurato in una parte della casa,£ma ne' banchi anco dove seggono, volendo significare£che colui che siede non sta solo,£ma siede insieme con l'aversario di tutti;
```

**Segmented:**
- Maus frutto, cioè musa.
- Questo frutto è molto gentile e dolce,
- della grandezza de' cetriuoli piccoli,
- e nasce di piccola pianta,
- e ha le foglie grande, larghe e lunghe un braccio.
- Dicono i timore e maraviglia ne' cuori umani.
- E nondimeno è a queste genti così associabile e commune
- che non solamente il tengono figurato in una parte della casa,
- ma ne' banchi anco dove seggono, volendo significare
- che colui che siede non sta solo,
- ma siede insieme con l'aversario di tutti;

---

## 🇪🇸 Castilian

**Raw with `£`:**
```
Por tal lo tengo yo£dixo don Duardos£& no puedo yo creer£que yo le sobrasse£pidole por merced£que me perdone que mi desseo es de seruille.£Señor£dixo la reyna£mal contado seria a tan grande hombre como vos.
```

**Segmented:**
- Por tal lo tengo yo
- dixo don Duardos
- & no puedo yo creer
- que yo le sobrasse
- pidole por merced
- que me perdone que mi desseo es de seruille.
- Señor
- dixo la reyna
- mal contado seria a tan grande hombre como vos

---
These examples illustrate how segmentation reflects **internal syntactic cues** and **rhetorical structuring**, rather than relying on punctuation alone.

See [segmentation_criteria.md](annotation_guidelines/segmentation_criteria.md) for full guidelines.


