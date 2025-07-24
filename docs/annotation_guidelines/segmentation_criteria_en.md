# ✂️ Segmentation Guidelines

This document outlines the main segmentation principles used to mark sentence or discourse unit boundaries in the corpus. These guidelines are based on syntactic and rhetorical structures rather than purely on punctuation or orthographic features.

Each language follows language-specific patterns and exceptions. Below are the general rules and examples categorized by part of speech and function.

---

## 1. Segments Without Delimiters

Some segments may appear without any clear delimiting token. This happens when the segment is truncated or randomly extracted from a longer clause, making it difficult to determine whether it begins or ends at a valid segmentation point.

> Example: *nos couvenoit aler dusqu’a outrance, car il est preuz et vistes et...* — the final "et" may be coordinating another adjective (no mark) or another clause (mark). When uncertain, do **not** annotate.

When context clearly reconstructs the missing part of the clause, segmentation should be applied.
> Example: *qui ilz ont tant de maulx souffers* — introduced by a preposition → do **not** segment.

---

## 2. Relative Pronouns

Relative pronouns like `que`, `qui`, `cui`, `dont`, `quod`, etc. are **not** used as segmentation points unless **preceded by a preposition**. In that case, the **preposition** is annotated.

> ✅ *par ou il passoit* → mark `par`  
> ❌ *de ce que...* → do not mark `de` if followed by `ce que`

A relative clause may not initiate a new segment unless it begins a new syntactic unit or follows a strong delimiter.

> ❌ *et les hommes que il vit...* — do not segment on `que`  
> ✅ *par qui ses frères furent tués* — segment on `par`

---

## 3. Conjunctions

### 3.1 Medieval Castilian

#### Coordinating Conjunctions
Used as delimiters **except** in enumerations:
- `e`, `et`, `y`, `&`
- Negations: `ni`
- Alternatives: `o`, `u`

#### Other Conjunctions
- `pues`
- `ca`, `que` (when causal)
- `pero`, `sino`, `mas` (when adversative)

> ✅ Example: *E fuemos a surgir... / e deçendimos en tierra...* (Yes)
> ❌ Example: *pero tiene buen puerto e muchas tierras...* (No, enumeration)

### 3.2 Medieval French

#### Coordinating Conjunctions
Used when linking clauses with explicit verbs.
- `et` → *et il dient* ✅; *flatir et a debatre* ❌ (only second 'et' marked if it starts a clause)
- `ou`, `o`
- `mais`, `car`, `kar`, `quar`, `ains`, `ne`

> `ne` is marked only when coordinating full clauses, not adjectives or nouns.

#### Subordinating Conjunctions
- `que` (complement or consecutive)
- `se` (conditional with expressed verb)

### 3.3 Medieval Italian

#### Coordinating Conjunctions
- `e`, `ed`
- `o`
- `né`
- `ma`
- `ché`

#### Subordinating Conjunctions
- `che`
- `se`
- `sicché`

---

## 4. Direct Speech Introducers

### 4.1 Medieval Castilian

Verbs like `decir`, `preguntar` are segmenters, whether for direct or indirect discourse.
- If the subject is postposed, split after it.
- Embedded speech verbs: keep within segment.

> Example: *dixo el Rey: ¿Commo fue eso?* → segment after `Rey:`

### 4.2 Medieval French

Includes formulaic openers and speech verbs:
- `haa`, `hee`, `he`, `certes`, `oil`, `oy`, `voire`, `naie`
- Preposition `par` (when introducing direct speech)

### 4.3 Medieval Italian

- `vere`, `certo`
- Preposition `Per` (used similarly to French `par`)

---

## 5. Adverbs as Delimiters

### 5.1 Medieval Castilian

Examples that often begin clauses:
- `ahora`, `cuando`, `entonces`, `luego`, `otrosí`, `como`, `tanto que`, `según que`

### 5.2 Medieval French

- `si`, `or`, `ores`, `lors`, `alors`, `puis`, `après`, `ainsi`, `anci`, `devant`, `quant`, `quand`, `comment`, `comme`, `tandis`, `tant`, `atant`, `maintenant`, `orendroit`, `toutesfois`, `car`

### 5.3 Medieval Italian

- `si`, `anzi`, `altresi`, `dunque`, `poscia`, `quando`, `allor`, `atanto`, `tanto`, `or`, `inanzi`, `immantanente`, `mantanente`, `perché`, `come`

---

## 6. Prepositions

Used as delimiters **only** in specific syntactic roles:

### 6.1 Castilian
- `por`, `para` → when introducing infinitive clauses
- `hasta`

### 6.2 French
- `pour`, `par`, `de`, `a`, `en` → when preceding relative or demonstrative pronouns
- `jusque` → only when followed by relative clause

### 6.3 Italian
- `per` → when introducing infinitive or direct speech
- `de`, `a`, `per`, `in` → before relative or adverbial clauses

---

## 7. Special Cases

### 7.1 Agglutinated Forms
Tokenize compound forms like:
- `quil`, `quilz`, `quelle`, `quelles`, `sil`, `silz`, `selle`, `selles`

### 7.2 Uncertain Segmentation
If a fragment is truncated and its syntactic role is unclear, **do not mark**.
> Example: *nos couvenoit aler dusqu’a outrance...* → unclear if `et` is coordinating or not

### 7.3 Tokenization Conflicts
When two potential segmenters follow each other, mark **only the first**.
> Example: *et quant il voit cele par cui...* → mark `et`, not `quant`

### 7.4 `que` Not to be Marked
Avoid marking `que` in:
- Restrictive relative clauses
- When preceded by tokens like `si`, `devant`, `ainsi`
- Coordinating value
- Redundant `que que`
- Exclamative/interrogative uses without clause initiation

### 7.5 Complex Structures
- Prefer the **first** delimiting token in a cluster.
- For coordinated elements or embedded relatives, apply judgment based on structure.

> Example: *sera moult ioyeuse si tost comment elle laura ueu* → mark `si`, not `comment`

- Relative pronouns after prepositions: mark the **preposition**.
> Example: *par ou il passoit* ✅; *de ce que...* ❌ (do not mark if `ce` intervenes)

---

These rules aim to guide segmentation based on linguistic structure, prioritizing coherence and consistency across languages. Refer to language-specific examples and test cases in `word_delimiters.md` for further clarification.

