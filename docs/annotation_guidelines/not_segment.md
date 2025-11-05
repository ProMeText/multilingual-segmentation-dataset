# 🚫  When **not** to segment

This section specifies cases where segmentation **should be avoided** to prevent over-fragmentation or the introduction of noise into the dataset.

## 1. Delimiters at the end of the chunk without context

To prevent noise and ambiguity, **do not mark** segmentation when the surrounding context is incomplete.

- Some segments, particularly those at the beginning or end of **randomly extracted passages**, may lack a clear delimiter due to truncation. If the syntactic structure cannot be confidently completed, **do not mark** segmentation.


>  Example: *nos couvenoit aler dusqu’a outrance, car il est preuz et vistes et...* → Last `et` is ambiguous (enumeration or new clause? → 🚫 no segmentation)

## 2.  Delimiter Sequences

Delimiter sequences are characteristic of paratactic languages, in which clauses are often intricately embedded within one another. In such contexts, a logical unit is frequently suspended to introduce a new clause, and the initial discourse thread is later reactivated through a residual delimiter or connective left earlier in the sequence.

- To avoid over-segmentation and semantic fragmentation, **only the first delimiter in a sequence of delimiters** should be marked as a segmentation point.

> £**E**, *em quanto* elle esto fazia,

> « £**ca,** *pois* Deus he ẽ nossa ajuda, £todos venceremos.

> *& venja Urian delante de todos £**mas** *por mucho que* ellos se cujtaron*


In these examples, although multiple elements could suggest a break, **only the first delimiter** (shown in bold) **is annotated** as a segment boundary — even when subsequent markers also introduce distinct clauses.

### 2.1. Handling ambiguous delimiter sequences

The following medieval Catalan excerpt illustrates an ambiguous case:
> £los parens del jovencel, **emperò**, **aprés** •!• dies mortz, £en - i - moniment foren cebelitz. 
(Literal English translation: The parents of the young man, however, after •!• days dead, were buried in a tomb.)


This example also illustrates a **sequence of discourse markers**. Following the segmentation principle for **delimiter sequences**, **only the first delimiter** — here, *emperò* —
would normally be marked as a segmentation point.
However, this case presents a more complex segmentation scenario.

Although **emperò** functions as a discourse connector and appears first in the sequence, it remains **structurally integrated** with the preceding clause (*los parens del jovencel*) and does not, **semantically**, trigger segmentation.

By contrast, **aprés** introduces a new clause and thus constitutes the appropriate segmentation point.
Consequently, segmentation should be applied at *aprés*, not at *emperò*.


 **Rule reminder:**  In ambiguous cases, the annotator should prioritize segmentation on **syntactic dependency** and **semantic continuity** over mere sequential position. 

## 3. Coordinating Conjunctions

**Annotation Principle:**  
Segmentation depends on the **syntactic scope** of coordination.

- **Simple coordination** (word-level or short phrase) → **no segmentation**.  
- **Complex coordination** (verbal, nominal, or clausal units) → **segmentation**.

Coordinating conjunctions do **not** trigger segmentation when linking **short elements** (typically one or two words) within an enumeration. However, when coordination connects **longer syntactic units**—such as **verbal groups**, **nominal groups**, or **full clauses**—it marks a **segmentation boundary**.

> [...] *espandire sobre casado de Jacob **e** de David £**e** sobre los estageros de Jherusalem spiritu*

In this example:  
- The **first _e_** coordinates two complements (*de Jacob e de David*) within a single noun phrase, and therefore **does not trigger segmentation**.  
- The **second _e_** introduces a new clause (*e sobre los estageros de Jherusalem spiritu*) and thus **marks a segmentation boundary**.

> E fuemos a surgir sobre Çepta, £**e** deçendimos en tierra; £**e** luego tomaron una caravela £**e** escrivieron a Caliz a fazerlo saber,
> non vo guarentisce, £**né** ella non vo puote guarire
> se prenenta flatir et a debatre. £**et** il commence

## 4. Enumerations (with or without coordinating conjunctions)

Enumerations remain **unsegmented** unless their internal structure becomes **complex enough** to hinder syntactic readability or semantic cohesion. Enumerative sequences — whether coordinated by conjunctions or simply juxtaposed — are **not segmented** by default. They are considered part of a single syntactic and rhetorical unit, even when they include several coordinated items.


### 4.1 With Coordinating Conjunctions

**Examples:**
> pero tiene buen puerto **e** muchas tierras, **e** frutas, **e** aguas. 🚫 *no segmentation applied*

> del molt noble **et** molt alt **et** molt poderos Seynor Don Sancho 🚫 *no segmentation applied*  

> £que seia sospenso **ou** emtridito **ou** escomungado  🚫 *no segmentation applied*  

> £o quall foi mui honrrado, avomdoso de rriquezas **e** boas comdiçoões. 🚫 *no segmentation applied*

> £E partio logo o reyno cõ seus irmããos £que foron estes: £Eribeto **e** Gruntano **e** Sigaberto. 🚫 *no segmentation applied*
 
> Tribulacion, **or** angwiȝss, **or** hungir, **or** nakidnesse, **or** persecucion, **or** perel, **or** swerd? 🚫 *no segmentation applied*   



### 4.2 With juxtaposed elements

**Examples:**
> £per logica sabrás conexer los jenres, les especies, les differencies, les proprietats e los accidents, 🚫 *no segmentation applied*  

> £ne burguezes, cavalers, princeps, prelats £no purien viure sens [...] 🚫 *no segmentation applied*  

### 4.3. Very long enumerations

Exceptionally, **very long or structurally complex enumerations** may be segmented **for clarity or syntactic disambiguation**: 

> [...] £per gracia de Deu Rey de Castella, de Toledo, de Leo, de Galicia, **£**de Sibília, de Cordova, de Murcia, de Jayen et del Algarbe,

## 5. Appositions

Appositive structures are **not segmented** when they form a **continuous syntactic and prosodic unit** with the noun they modify.  
They remain within the same clause or nominal phrase.

**Annotation Principle:**  
Appositions are segmented only when they display **syntactic detachment** or **prosodic independence**,  
even if their referential anchor remains implicit or distant.  
In embedded or interrupted structures, **syntactic separation** overrides the appositive link.


*Example*  
> £E dona Orraca, **sua filha del rey**, lhe fazia muyta honrra.. 🚫 *no segmentation applied*  

> £Mas, da desaveença £que ouve antre mĩ e Moluca, **o senhor de Calçom,** 🚫 *no segmentation applied*

> £E estableçio el cardenal legado don frey Gillem, **obispo de Sabina,** 🚫 *no segmentation applied*

#### Exceptions:

Appositions **are segmented** in the following cases:

- **Detached appositions in embedded or interrupted clauses**  
   When the apposition is **syntactically separated from its head noun** by another clause or by intervening material, making it **prosodically and structurally autonomous**.  
   
> £Mas **jo**, malastruch e desaventurat, £embalçat e caüt en tants de mals, £foragitat del regne de mon pare, £**don mirayl de les coses humanals.**

> jo ─ malastruch e desaventurat └─ close apposition 🚫
> (embalçat... foragitat...)  └─ intervening clause 
> ─ don mirayl de les coses humanals  └─ detached / segmented apposition ✅
     
      

---




### 6. Cases Where *que* (and equivalents) Should **Not** Be Annotated

The form **_que_** — whether functioning as a **relative**, **interrogative**, **exclamative pronoun**, or as a **subordinating conjunction** — usually serves as a segmentation trigger. However, a number of specific contexts require that it **not** be annotated. These exceptions prevent over-segmentation in cases where *que* **does not introduce an autonomous syntactic or rhetorical unit.**


**Annotation Principle:**  
*que*, *comme*, and *comment* are **not annotated** when they:
- are part of fixed or pleonastic expressions,  
- serve a purely coordinating or comparative function, or  
- lack an explicit subordinate verb.  


#### ⚠️ Cases of Non-Annotation


1. **When _que_ has a coordinating value**

   *que* here joins two syntactically parallel elements rather than introducing a dependent clause.  
   *Example:*  
   > £quil ert las et traueillies. **que** del combatre **que** del cheualchier  🚫 *no segmentation applied* 
   → Both *que*’s are coordinating and do not trigger segmentation.

---

3. **When _que_ plays a redundant or pleonastic value**

   Common in medieval French, this construction does not mark a new syntactic boundary.  
   *Example:*  
   > les dens £que a pou **qu** il ne les luy a brisiees  🚫 *no segmentation applied* 
   → second *que* is redundant .

---

4. **When _que_ has a restrictive value**

   *que* is then equivalent to *“only”*, *“except”*, or *“save”*, and does not introduce a clause.  
   *Example:*  
   > ne se relieue **que** a grans peine et si estoit il  
   → Restrictive use, not segmenting.

---

5. **When _que_ appears in a comparative structure without an expressed verb**

   In elliptical comparatives, *que* links nominal or adjectival terms rather than clauses.  
   *Example*  
   > cheualiers et preus £et plus pris sa cheualerie **que** la monseignor Gauuain  
   → No segmentation: comparative linker *que*.

   *Example (annotated):*  
   > a censeiller mieulx £**que** ung aultre ne fera  
   → Segmentation occurs: *que* introduces a subordinate comparative clause.


    5.1. **_comme_ or _comment_ behave similarly**

   In comparative or idiomatic uses, *comme* and *comment* are **not** annotated as segment markers.  
   *Example:*  
   > comme li lievres devant les chiens  
   → No segmentation.


 **Practical Reminder:**  
Annotators should verify whether *que*, *comme*, or *comment* introduce a **verbal predicate**.  
If **no verb follows**, or if the element belongs to a **frozen or comparative phrase**, it must **not** be treated as a segmentation marker.
