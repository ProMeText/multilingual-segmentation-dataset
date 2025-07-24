
# ✂️ Segmentation Criteria

This document outlines the core principles for segmenting sentence or discourse boundaries in the corpus. Segmentation is based on **syntactic structure** and **rhetorical cues**, rather than punctuation alone.

Each language follows its own specific conventions, with exceptions and language-specific adaptations. The general segmentation logic is organized below by **grammatical category** and **function in the sentence**, accompanied by examples.

> ⚠️ **Note:** This is **version 0** of the segmentation guidelines. These rules may evolve as the dataset grows and new languages are incorporated.

--

## 🚫 1. Segments Without Delimiters

Some segments do **not contain any valid segmentation marker**. For example:

> *fut filz au plus recreant homme. et au plus failli de cueur.*

To avoid adding noise to the dataset, **do not mark** elements that often appear at the beginning of a sentence **but also frequently occur mid-sentence**, such as:

- 👤 **Personal pronouns**  
  _Ex: `Si li anoia moult li cheualliers Il oste son` → `Si` is not marked._

- 📍 **Prepositions** at the beginning of a segment  
  _Ex: `Au mains sil seussent celes` → `Au` is not marked._

- 🗣️ **Speech markers / vocatives**  
  _Ex: `Sire fet elle iou men priserai de miex...` → `Sire` is not marked._

Some segments, particularly at the beginning or end of randomly extracted passages, may lack a clear delimiter due to truncation. If the syntactic structure cannot be confidently completed, **do not mark** segmentation.

> ⚠️ Example: *nos couvenoit aler dusqu’a outrance, car il est preuz et vistes et...* → Last `et` is ambiguous (adjective or clause? → no segmentation)


## 🔗 2. Relative Pronouns

Relative pronouns are **not marked** unless they are preceded by a **preposition**, in which case the **preposition is the segmentation marker**.

| Structure                        | Segment? | Notes                              |
|----------------------------------|----------|------------------------------------|
| `par ou il passoit au chastel`   | ✅ `par`  | Preposition + relative             |
| `de ce que...`                  | ❌ No     | Intervening demonstrative `ce`     |

A relative clause may not initiate a new segment unless it begins a new syntactic unit or follows a strong delimiter.

> ❌ *et les hommes que il vit...* — do not segment on `que`  
> ✅ *par qui ses frères furent tués* — segment on `par`

> **que**, **qui**, **dont**, **où**, **(le)quel** can also function as **interrogative pronouns**.  
> In such cases, they are **also used as segmentation markers**.  
> *Ex: —où est-il donc ?*

---
# 🔁 3. Conjunctions

### 🇪🇸 3.1 Medieval Castilian

**Coordinating conjunctions** are used as delimiters, except in **enumerations**:

- `e`, `et`, `y`, `&`, `ni`, `o`, `u`
- `pues`, `ca`, `que` (causal), `pero`, `sino`, `mas` (adversative)

> ✅ *E fuemos a surgir... / e deçendimos en tierra...*\
> ❌ *pero tiene buen puerto e muchas tierras...*

### 🇫🇷 3.2 Medieval French

Used **only when linking full clauses with verbs**:

- `et`, `ou`, `o`, `mais`, `car`, `kar`, `quar`, `ains`, `ne`
- Subordinating: `que`, `se`

> ❗ `ne` is marked **only when coordinating clauses**, not phrases or adjectives.

### 🇮🇹 3.3 Medieval Italian

- Coordinating: `e`, `ed`, `o`, `né`, `ma`, `ché`
- Subordinating: `che`, `se`, `sicché`

---

## 🗣️ 4. Direct Speech Introducers

Speech verbs and discourse initiators.

### 🇪🇸 Castilian

- Verbs like `decir`, `preguntar` → segment **after** subject if postposed\
  *Ex: **`dixo el Rey: ¿Commo fue eso?`*

### 🇫🇷 French

- Openers: `haa`, `hee`, `he`, `certes`, `oil`, `oy`, `voire`, `naie`, `par`

### 🇮🇹 Italian

- Openers: `vere`, `certo`, `Per` (used as in French `par`)

---

## 🕰️ 5. Adverbs as Delimiters

Adverbs at the beginning of new clauses or discourse units.

### 🇪🇸 Castilian

- `ahora`, `cuando`, `entonces`, `luego`, `otrosí`, `como`, `tanto que`, `según que`

### 🇫🇷 French

- `si`, `or`, `ores`, `lors`, `alors`, `puis`, `après`, `ainsi`, `devant`, `quant`, `quand`, `comment`, `comme`, `tandis`, `tant`, `atant`, `maintenant`, `orendroit`, `toutesfois`, `car`

### 🇮🇹 Italian

- `si`, `anzi`, `altresi`, `dunque`, `poscia`, `quando`, `allor`, `atanto`, `tanto`, `or`, `inanzi`, `immantanente`, `mantanente`, `perché`, `come`

---

## 📍 6. Prepositions

Used **only in specific clause-introducing contexts**.

### 🇪🇸 Castilian

- `por`, `para`, `hasta` → introduce infinitive clauses

### 🇫🇷 French

- `pour`, `par`, `de`, `a`, `en`, `jusque` → only when preceding relative or demonstrative pronouns

### 🇮🇹 Italian

- `per`, `de`, `a`, `in` → same rules as above

---

## ⚠️ 7. Special Cases

### 7.1 Agglutinated Forms

Always segment compounds like:

- `quil`, `quilz`, `quelle`, `sil`, `selle`

### 7.2 Uncertain Boundaries

When unsure due to truncation, **do not segment**.

> Ex: *nos couvenoit aler dusqu’a outrance...*

### 7.3 Marker Clashes

When multiple segmentation markers follow each other, mark **only the first**.

> Ex: *et quant il voit cele par cui...* → ✅ `et`, ❌ `quant`

### 7.4 `que` Not to Segment

| Usage                     | Segment? | Reason                 |
| ------------------------- | -------- | ---------------------- |
| Restrictive clause        | ❌        | Too embedded           |
| Preceded by `si`, `ainsi` | ❌        | Structural dependency  |
| `que que` (redundant)     | ❌        | Collapse redundancy    |
| Exclamatory/interrogative | ❌        | Not a clause initiator |

### 7.5 Complex Sequences

Segment **only the leading marker** in clusters or embedded relatives.

> Ex: *sera moult ioyeuse si tost comment elle laura ueu* → mark `si`, not `comment`

---

## 📊 Visual Summary

### 🔄 Segmentation Flow

```
[Clause Start?] 
   ↓
[Verb Present?] → Yes → ✓ Segment
                 → No  → Check if it's an enumeration → ✗
```

### ✅ Proper Segmentation

```diff
+ E dixo el Rey£
+ ¿Commo fue eso ?
```

### ❌ Enumeration (No segmentation)

```
Incorrect:
Il prit du pain£, du vin£, et du miel£.

Correct:
Il prit du pain, du vin, et du miel£.
```

---
## 🧠 Tip

Focus on **syntactic ruptures**, **speech verbs**, and **clause-openers** — not just punctuation.

These rules aim to guide segmentation based on linguistic structure, prioritizing coherence and consistency across languages.

For implementation details and language-specific heuristics, see the companion file:  
[`word_delimiters.md`](word_delimiters.md).


