# What do we segment ?

This guideline provides examples showing how segmentation operates in practice for a range of syntactic structures and languages.

- We segment **syntactically and semantically autonomous units** — clauses and other structures that introduce a new proposition or discourse act.


## 1. Sentence and Clause Beginnings

### General Principle

From a functional standpoint, it is essential to identify **sentence and clause openings**.  
These elements can be more challenging to recognize than conjunctions or relative pronouns, since they often appear **both at the start of a segment and within** one.

The following categories typically indicate the **beginning of a new sentence or clause**:

---

- **Personal pronouns**  
  *Example:*  
  > £Si li anoia moult li cheualliers £**Il** oste son  
  
  > £**él** e la sua muler penseren de la Verge
  
  > £**Eu** vijm a esta çidade £por hõrrar a festa .


---

- **Prepositions** introducing a new clause or sentence  
  *Example:*  
  > ne seuent nulle noueles de lancelot. £**Au** mains sil seussent celes  

  > £lo qual volch degolar £**per** fer sacrifici a Deu, £**a** significar lo sacriffici [...]

  *Prepositions* are here annotated as the beginning of a new unit.

---

- **Definite or indefinite articles**  
  > £**Le** conte dist £que quant Agloual se fust parti  

  > £**El**Rei cuidando neeste feito,£pareçerom lhe as rrazõoes boas,

  Definite articles *le* and *el* are annotated as the initial marker of a new clause.


---

## 2. Titles, Chapters, Epistles, and Other Structural Elements

### 🔹 General Principle

Structural divisions such as **titles**, **chapter headings**, **epistles**, **rubrics**, and similar paratextual elements constitute **independent segmentation units**.  
They serve organizational and rhetorical functions rather than syntactic ones, and therefore must be treated as **stand-alone segments** in the corpus.

###  Annotation Guidelines

- Each title or rubric is annotated as a **separate segment**, regardless of its punctuation or typographical layout.  
- Transitional or introductory formulas (e.g., *Here begins...*, *Explicit capitulum...*) are considered **part of the structural unit**, not of the following narrative segment.  
- When a structural marker is followed by narrative text on the same line, the **boundary is still maintained** to preserve hierarchical consistency.


### Examples



> £Delle citta di Ormuz e Bagdeth.

> £Lettera III

> £Del regno di Coulam

> £COMENCA LA PRIMERA PART DEL LIBRE DE TIRANT, £LA QUAL TRACTA DE CERTS VIRTUOSOS ACTES £QUE FÉU LO COMTE

> £Capitulo .ccxcj.


> £Capitulo .lxxvj. £como todos los caualleros fueron contentos £delo que don Quadragante propuso





## 3. Vocatives and Direct Address

### 🔹 General Principle

**Vocatives** — forms of direct address or proper names used to call upon an interlocutor — are often placed at the beginning of clauses or reported speech.  
Their position may **coincide with a segmentation point**, but they do **not automatically trigger segmentation** on their own.

Segmentation depends on whether the vocative:
1. Functions as an **independent discourse unit** (e.g., marking a shift in address or speaker turn)
2. Remains syntactically and prosodically integrated within the same clause.


### Annotation Guidelines

🔹 Segment if:
- A vocative that **introduces a new speaker turn** or **opens direct speech** is annotated as the beginning of a new segment, since it marks a distinct communicative act. 

- Exemples:
> £**Molt alt príncep e senyor**, £premesa deguda reverència a la vostra altea,

> £For Isaie seiþ, £**Lord**, £who bileuede to oure heering?

> £levantou-se hũu fillosofo d'antre os jentiios £e dise asy:"£**Raynha senhor**, £vós avedes dito £que em na esençia de Deus ha tres pesoas

 > £**Sire** £fet elle £iou men priserai de miex 

> £**Molt alt príncep e senyor**, £premesa deguda reverència a la vostra altea,

> £e disse:—£**Figliuolo mio**, hai tu veduto niente £di quello che io ti dissi?

🔹Do not segment:
- If the vocative is **embedded** within a clause, it remains **within the same segment**.  
- Similarly, interjected vocatives that do not alter the syntactic flow of the sentence are not treated as segmentation boundaries.

- Exemples:
> £**Con has, fill**, £menjat e begut covinentment,

> £e disse-lhe:– £**Por Deus, senhor,** £perdoade-me

Here *fill* is an interjected vocative, as it express an interpellation but do not introduce a new discourse unit, and therefore are not annotated as segmentation boundarie.

## 4. Parenthetical Clauses (Incises)

### 🔹 Definition and Scope

**Parenthetical clauses**, or **incises**, are short reporting structures typically embedded within direct speech or narrative flow.  
They indicate **speech attribution or narrative modality**, and are treated as **autonomous discourse segments**.

### Annotation Guidelines

-Each incise is annotated as an **independent segment**, delimited by the points where direct speech is interrupted and resumed.

Segmenting incises allows the model to clearly identify reporting clauses, maintain syntactic rhythm, and distinguish between narrative framing and speaker turns.



### Examples:

> £A non Dieu, £**fet mes sires Gauvains , 

> £Se eu cuidasse,£**disse Galvam**, £que me nom faleceríades aa primeira vez

> £whan thou wilt not do that thyng £that I requyre of thee?" £**And Taffile answerd to hym**, £“What nede have I of the frendship ...

> disse Lancelotto, £di queste lettere sapete vo' £chi- lle fece? —£Certo, £**diss’ egli**, no.

> £A non Dieu, £**fet mes sires Gauvains,** £nos avons anuit tant veu en dormant





## 5. Direct and Indirect Speech

### 🧾 Table — Main Markers of Direct Speech Onset (Medieval Corpus)

| **Type** | **Latin** | **Middle English** | **Old / Middle French** | **Medieval Italian** | **Catalan** | **Medieval Castilian** | **Medieval Portuguese** |
|-----------|------------|--------------------|--------------------------|----------------------|--------------|------------------------|--------------------------|
| **Verbs of Saying** | *dixit*, *ait*, *inquit*, *respondit*, *clamavit* | *seide*, *quoth*, *answerede*, *spak* | *dist*, *dist il*, *respondi*, *parla*, *fet* | *disse*, *parlò*, *respuose* | *digua*, *respos*, *digué* | *dixo*, *respondió*, *preguntó* | *disse*, *respondeu*, *perguntou* |
| **Interjections** | *heu*, *o*, *vae* | *lo*, *alas*, *ah* | *ha*, *haa*, *hee*, *he*, *o* | *ahi*, *oimè*, *or* | *ay*, *o*, *he* | *ay*, *o*, *ha*, *e* | *ai*, *oh*, *ora* |
| **Lexical / Adverbial Markers** | *certe*, *vere*, *nimirum* | *soothly*, *truly* | *certes*, *voire*, *naie*, *oil*, *oy* | *certo*, *vere*, *per verità* | *cert*, *verament*, *per ço* | *cierto*, *por verdad*, *así* | *certo*, *assim*, *por verdade* |
| **Prepositional / Formulaic** | *per Deum*, *inquit ille* | *forsooth*, *by God* | *par ma foi*, *par Dieu* | *per Dio*, *per mia fé* | *per ma fe*, *per Déu* | *por Dios*, *por mi fe* | *por Deus*, *per minha fé* |

---

💡 **Annotation Note:**
- The **token following a verb of saying**  is **always a segmentation boundary**, regardless of whether it introduces **direct** or **indirect** discourse.  
- **Interjections** and **adverbs of assertion** (*certes, certo, ciertamente, por verdad, etc.*) mark the **onset of a speech act** and are segmented accordingly.  
- **Formulaic expressions** (often *preposition + divine noun*, e.g. *par Dieu*, *por Dios*) are annotated as single tokens if they appear **at the start of speech**.


### 🔹 Definition and Scope

Reported speech can appear in two main forms:

1. **Direct speech**, where the words of a speaker are quoted or presented verbatim.  
   → Often introduced by verbs of saying and marked by punctuation or syntactic cues.
2. **Indirect speech**, where the speaker’s words are **paraphrased or subordinated** syntactically (typically introduced by *that*, *que*, etc.).

Both forms involve **speech markers**, i.e. lexical or verbal expressions that attribute speech or thought.

---

### Annotation Guidelines

- **Speech markers** (reporting verbs and expressions) are annotated according to **syntactic dependency**:
  - When introducing direct speech, they belong to the **same segment** as the utterance they introduce.  
  - When introducing indirect speech, segmentation occurs **before** the reported content if it represents a new propositional or rhetorical unit.

- **Direct  and indirect speech** are always segmented as an **independent discourse unit** as they stand apart syntactically and rhetorically from the narrative frame.

### Examples

#### **Direct Speech**
> .£he depois £**disse a el rey archileus** .£**bem ves tu £que nõ he rezam £que nos te tomemos en nossa merçee**

> £Et ela li disse: «£Di'-me adoncha lo vostro consegio».£Et elo disse: «£Dama, qui apresso un meyo£

> £Al quale lo can respoxe: «£Acciò che non possa offendere queli£che passa davanti la mia ca'

> £Que cousa é ?£disse el-rei. –£Esto vos direi eu, £disse el. £Vós sabedes £que nos albergastes

- *disse el-rei.* is a **speech marker**, introducing a new utterance.  
- The quoted clause is annotated as a **new segment**, representing a distinct discourse act.

#### **Indirect Speech**

> £Quando Erec entendeu £que a justar lhi convĩĨa, £**disse que lhi nom era mester**,

> £But the labourer, £that was named Papirion, £said to his maister £**that he shold denye his cause hardily**

> £And forthwyth stepte in £**and sayd that he hymself £was culpable £of the deth of this man**

> £E Jugurta, oÿt lo manament dels legats,£**respòs que a él no li ere res major ne pus** 


---














----
## 6. Finite and Circumstantial Structures

### 🔹 Definition and Scope

In segmentation, both **finite** and **circumstantial** structures are considered relevant units.  
A **finite clause** expresses a complete syntactic proposition, while a **circumstantial clause** introduces a temporal, causal, conditional, or concessive relation that often carries its own **semantic and rhetorical autonomy**.

---

### Annotation Guidelines

- **Finite clauses** mark independent syntactic and rhetorical units → **always segmented**.
- **Circumstantial and non-finite clauses** (temporal, causal, conditional, etc.) are segmented as they introduce a new **temporal**, **logical**, or **rhetorical** boundary. 
- The segmentation is **semantic and functional**, not based on subordination hierarchy.
- Circumstantial markers (e.g., *quant*, *aprés*, *si*) are annotated as **segment onsets**. (See lexical_inventory)





#### **Circumstantial structure**
> |Quant Agloual se fust parti| |il entra en la forest.|  
→ The temporal clause *Quant Agloual se fust parti* opens a new discourse frame (temporal), thus receives its own segment.

#### **Multiple circumstantial clauses**
> |Aprés ce que li rois fu venus| |et quant il ot parlé as barons| |il monta a cheval.|  
→ Each circumstantial clause is segmented, as each introduces a new temporal or sequential frame.






---


#### **6.1 Main Clauses**
Main (finite) clauses are independent and self-contained syntactic units.  
They form the backbone of discourse segmentation and always receive an independent segment.

> |Li rois monta a cheval| |et s’en ala vers la cité.|

Each finite clause (*Li rois monta...*, *et s’en ala...*) constitutes a separate segment.

---

#### **6.2 Ablative absolute and Absolute participal Clauses**
Absolute or detached constructions express a circumstance external to the syntactic frame of the main clause.  
They are segmented as autonomous discourse units because they introduce parallel or background information.

> Licenziata adunque dalla nuova reina la lieta brigata,

> £Partito meser Gianni di Guascogna,

> £**Quo facto,** £illa subito evanuit,

---

#### **6.3 Gerundive or Participial Clauses**

> £sperando di venderlo al gran Turco per molto maggior prezzo

> £Oydo todo esto por el rey Arauigo

> navegant ab pròsper vent

> £**Estando Abemaffa ẽ Vallença,** £pos seu amor cõ dous cavalleiros da vylla
---



#### **6.4 Circumstantial Clauses**

Circumstantial clauses express temporal, causal, conditional, or concessive relations between two propositions.  
Although grammatically dependent, they introduce new **discourse frames** — temporal, logical, or argumentative — and are therefore **systematically segmented**.

Typical subtypes include:

- **Temporal**  

- Exemples:

> £**Aprés que**aquestes coses foren oÿdes,

> £**depois que esto ouve feito enna Gasconha**, £ẽ hyndosse della, £chegoulhe mandado ẽ como de terra de mouros

> £quod pugnatores ordinent se £secundum formam quadrangularem, £**et postea** secundum triangularem, £**et deinde** secundum rotundam: £**et sic deinceps** debet assuefacere bellantes,

- **Causal** (*car*, *por ce que*, *porque*, *because*)  

-Exemples:

> £Pero era vilania £**ca Mordret estava desarmado e a pee**

> £él dix a la sua muler £que pugés en un caval, £**per so car avien luyn as-anar**,£per què ela tremolan puyà al caval,


> £que li soudant la firent toute araser et abatre £**pour ce qu'il avoient sorti**

- **Conditional** (*se*, *si*, *if*)  

-Exemples:

>  £**If nucha be kutt þoruȝ ouerþwert**, £þe wounde is mortal £for þe nobilte of nucha £þat comeþ fro þe brayn riȝt 

> £che,**se egli aveva commissione alcuna da Vostra Maestà**, £me la dovesse presentare,

> £**Si bonam conscientiam haberes**, £non multum mortem timeres.

- **Concessive** (*bien que*, *encore que*, *aunque*, *though*)  

- Exemples: 

> £que mucho ha que del no se supieron nueuas ningunas £**aunque muchos de sus amigos lo han buscado con grandes afanes por tierras estrañas**

> £And hit is no merveylle, £**though hyt so happen** £for that man that is disagreable 

> £e adiante screvo,£**ainda que per fundamentos desvayrados** £syntom a tristeza,

- **Consecutive**

- Examples:

> e cusiu-los £**de manera que no·s puga exir la mel.**

> brother that vyenne hath had so moche Ioye £and so grete playsyr £whan she had knowleche £that ye were a lyue £**that it is wonder to byleue**

>  £& vos señora lleuareys vna capa abrochada: £& antifazes delante del rostro: £**de guisa que a todos ver podays £& ninguno no a vos.**

- **Final** 

> et per vestras etiam literas exponentes et petentes humiliter, £**ut faciendae translationi favorem apostolicum et pium praeberemus assensum**

> £E mãdaae logo fazer as cartas £**pera que mha tirem** £e a mỹ que me saya de vossa terra.

> £mas el bien entendia £que el rrey lo fazia **£por que ele moriesse alla**


> **Cross-linguistic Note: Concessive Constructions**

> In certain languages — particularly in **Old or Medieval Romance** (e.g., Old Spanish, Occitan, Old French, or Latin) — concessive relations may appear in **coordinate form** rather than as strict subordination.  

> Examples include structures where *mas*, *pero*, *ainsi*, *empero*, or *maguer* introduce a concessive relation without an explicit subordinating conjunction (*bien que*, *aunque*, *although*).
>
> **Example (Old Castilian):**  
> > £non gelo quisso toller, **mas** £lo ferio con la lança.  
> → The clause introduced by *mas* (“but”) expresses concession or contrast, functioning semantically as a **concessive clause**, even though it is **formally coordinated**.



> 🗒️ **Cross-linguistic Note: Coordinated vs. Subordinated Circumstantial Clauses**
>
> In several **Old and Medieval Romance languages** (e.g., Old French, Old Spanish, Occitan, and Latin), circumstantial relations such as **cause**, **concession**, **condition**, or **contrast** are frequently expressed by **coordination** rather than by explicit subordination.  
> Connectors like *car*, *ca*, *que*, *mas*, *empero*, *por ende*, *et si*, or *mas si* function semantically as circumstantial markers, even though they are formally coordinating conjunctions.
>
> These constructions therefore behave like **circumstantial clauses** at the discourse level — introducing new logical, temporal, or argumentative relations — and are **segmented** accordingly.




> **Cross-linguistic Patterns**
>
> - **Latin:** frequent overlap between coordination (*nam*, *enim*) and subordination (*quia*, *cum*, *quoniam*).  
> - **Middle English:** *for*, *and if*, *though*, *when* may act as causal, conditional, or concessive markers; parataxis remains common.  
> - **Old French:** alternation between *car* (coordinating causal) and *por ce que* (subordinating causal).  
> - **Italian (Medieval):** flexible use of *che*, *però che*, *se*, *quant(e)* for temporal, causal, or conditional relations.  
> - **Castilian:** connectors such as *ca*, *mas*, *e si*, *maguer*, *aunque* often convey subordination through coordination.  
> - **Catalan:** similar patterns with *car*, *que*, *si*, *maguer*, showing high functional overlap with Occitan.  
> - **Portuguese:** *ca*, *porque*, *mas*, *se* used with variable syntactic value; semantic relation governs segmentation.

-------
### 🧾 Table — Main Prepositions and Conjunctions Introducing Circumstantial Clauses

| **Type of Clause** | **Latin** | **Middle English** | **Old French** | **Italian (Med.)** | **Catalan** | **Castilian (Med.)** | **Portuguese (Med.)** |
|--------------------|------------|--------------------|----------------|--------------------|--------------|----------------------|------------------------|
| **Causal** | *quia*, *quoniam*, *nam*, *enim*, *propter quod* | *for*, *for that*, *because* | *car*, *por ce que*, *puis que* | *però che*, *imperò che*, *poi che*, *perché* | *car*, *per ço que*, *perquè* | *ca*, *porque*, *por ende*, *pues que* | *ca*, *porque*, *por ende* |
| **Temporal** | *cum*, *postquam*, *ubi*, *quando* | *when*, *after that*, *as soon as* | *quant*, *aprés ce que*, *des que*, *lors que* | *quando*, *poi che*, *dopo che*, *mentre che* | *quan*, *aprés que*, *mentre que* | *cuando*, *aprés que*, *en quanto*, *desque* | *quando*, *depois que*, *logo que* |
| **Conditional** | *si*, *nisi*, *dum* (in some uses) | *if*, *and if*, *but if*, *unless* | *se*, *et se*, *mes se*, *s’il* | *se*, *qualora*, *purché* | *si*, *e si*, *mas si* | *si*, *e si*, *mas si* | *se*, *e se*, *caso que* |
| **Concessive** | *quamvis*, *etsi*, *licet* | *though*, *although*, *even if* | *bien que*, *encore que*, *quant que* | *benché*, *sebbene*, *ancorché* | *maguer*, *encara que*, *malgrat que* | *maguer*, *aunque*, *aun que*, *bien que* | *ainda que*, *posto que*, *embora* |
| **Resultative / Consecutive** | *ita... ut*, *sic... ut*, *adeo... ut* | *so... that*, *so that* | *si... que*, *tant... que*, *tel... que* | *tanto che*, *così che* | *tant... que*, *tan... que*, *de manera que* | *tan... que*, *de guisa que*, *de manera que* | *tão... que*, *de maneira que* |
| **Comparative** | *sicut*, *velut*, *quemadmodum* | *as*, *as if*, *like as* | *comme*, *ainsi comme*, *autant comme* | *come*, *siccome*, *quasi che* | *com*, *com així*, *així com* | *como*, *así como*, *tal como* | *como*, *assim como*, *tal como* |
| **Final (Purpose)** | *ut*, *ne*, *quo*, *ad hoc ut* | *so that*, *that*, *in order that* | *pour ce que*, *afin que*, *que* | *acciò che*, *perché*, *che* | *perquè*, *a fi que* | *porque*, *a fin que*, *que* | *para que*, *a fim que* |


#### **6.5 Completive Clauses**

Completive clauses (introduced by *que*, *that*, *quod*, etc.) function as **syntactic complements** of a matrix verb (*dire*, *penser*, *croire*, *savoir*, *respondre*, etc.).  
They express **propositional content**, often reporting speech, thought, or perception.

Although grammatically subordinate, **completive clauses are segmented** when they convey a **distinct discourse act** — for example, when they represent a full statement, report, or belief introduced by a matrix predicate.

---

### 🧩 Annotation Guidelines

- If the completive clause expresses a **full propositional content** (e.g., reported speech or assertion), it is **segmented**.  
  The segmentation reflects a shift from the reporting frame (*il dist*, *il pensa*) to the propositional content.
- If the completive clause is **semantically weak** (e.g., part of a cognitive or modal expression like *il semble que*, *il faut que*), it may remain **unsegmented**.
- Segmentation depends on **semantic autonomy** rather than syntactic dependence.

---

### 📖 Examples

> £lo qual li respòs £**que no sabia la via**

> £a significar lo sacriffici £**que Jesuchrist feu de si matex** £a morir per son poble.

---

💡 **Annotation Principle:**  
Completive clauses are segmented when they encode an **autonomous propositional act** (speech, thought, perception).  
They remain unsegmented only when serving as **modal or cognitive complements** without rhetorical independence.

#### **6.6 Infinitival Clauses**

Infinitival clauses are **non-finite verbal structures** that may function as complements, circumstantials, or adverbial expressions.  
---

### Annotation Guidelines

- When the infinitive expresses a **circumstantial relation** (purpose, result, cause, or condition), it is **segmented**, since it introduces a new rhetorical act.  

- When the infinitive phrase is **absolute or detached** (standing as an independent syntactic group), it is **segmented** as an autonomous unit.  

-  When the infinitive phrase is **introduced by a preposition**, the **preposition** itself is annotated as the segmentation marker.

### Examples

> £**por oyr** tan grandes loores del cauallero dela roca partida

> £**per possedere** l’amore de tanta donna cum legitimo nodo.

> £él e la sua muler penseren de la Verge £**a lausar** devotament,

## 7. Relative Pronouns

Relative pronouns introduce **subordinate clauses** and must be annotated as segmentation markers whenever they open a new syntactic or discourse unit.  

 **Annotation Principle:**  
All relative or interrogative pronouns — including their prepositional forms — are annotated as **segment onsets** when they introduce a new syntactic dependency or clause boundary.  
**Orthographic variation is never normalized**; annotation strictly follows the original spelling found in the corpus.

Relative pronouns are annotated as **segmentation triggers** when they introduce subordinate or relative clauses, including free relative (relative pronoun with no antecedent).


  The form **quel** in french is annotated as a segmentation token when used as a **relative**, **exclamative**, or **interrogative** pronoun,  
  but **not** when it functions as an **indefinite determiner**:  
  > fait mander la nouvele dou tornoiement et a **quel** terme → *no segmentation*  

  Nor when it appears in combination with *que*:  
  > en quel lieu £que il fust  

  When **quel** is repeated, only the **first occurrence** is annotated:  
  > £quel besoins et quel auenture lauoit la amene  

- **quantque**, **quamque**  
  *Example:*  
  > £Et elle crioit £quamque elle pooit  

---

### **Prepositional Relatives**

When a relative pronoun is **introduced by a preposition**, the **preposition** itself is annotated as the segmentation marker.  
*Example:*  
> £**de quel** tornoiement li chevalier de ceanz parloient anuit après vespres  
>hũu filho £**a que** disserom dõ frei Alvoro Gomçallvez Pereira,
(cf. Section [Prepositions](#sec:prep))

### **Free Relatives**
A substantive relative clause (also called a free relative clause) is a clause introduced by a relative word (que, quien, cual, cuanto, donde, etc.) without an explicit antecedent, which functions as a noun within the main sentence.

> £Dueña £diz Miles, £bien me nienbra £**quanto** me avedes dicho,

### **Adjectival /Adverbial Relatives**
Adjectival or Adverbial Relatives are relative clauses introduced by adverbs, which modify a noun or express circumstances of place, time, or manner related to the main clause.
> £**donde** questo gentile huomo est morto 
> della grande servitudine £**ove** noi eravàno

### ❓ **Interrogative Use**

The relative forms listed above can also function as **interrogative pronouns**.  
When used in interrogative structures, they are **always annotated** as segmentation markers, since they introduce a new syntactic and rhetorical unit.
 
*Example:*  
> £**ou** est il donques  
> £Santa Maria, £**chi** mi gitterà di qui?




### 🧾 Table — Main Relative Pronouns and Constructions (Medieval Corpus)

| **Function / Type** | **Latin** | **Middle English** | **Old / Middle French** | **Medieval Italian** | **Catalan** | **Medieval Castilian** | **Medieval Portuguese** | **Segmentation Note** |
|----------------------|------------|--------------------|-------------------------|----------------------|--------------|------------------------|--------------------------|------------------------|
| **General relative pronoun** | *qui*, *quae*, *quod* | *that*, *which*, *who*, *whom* | *qui*, *ki* | *che*, *ch*, *que* | *que*, *qui* | *que* | *que* | Always segmented when introducing a new clause. |
| **Object / Complement** | *quem* | *whom*, *that* | *que*, *ke*, *qe*, *qu* | *che*, *ch* | *que* | *que* | *que* | Segment onset for subordinate clause. |
| **Indirect / Oblique** | *cui*, *cujus* | *whom*, *whose* | *cui* | *cui* | *cui* | *cuyo*, *cui* | *cujo* | Segment onset when marking relative dependency. |
| **Partitive / Possessive** | *cujus*, *de quo* | *of whom*, *whose* | *dont*, *dunt* | *di cui*, *onde* | *d’on*, *on* | *de quien*, *donde* | *de quem*, *onde* | Segment onset for subordinate clause. |
| **Locative** | *ubi* | *where* | *ou*, *o* | *ove*, *dove* | *on*, *on que* | *donde*, *en que* | *onde*, *em que* | Segmented; introduces locative subclause. |
| **Instrumental / Prepositional** | *in quo*, *per quem* | *in which*, *by which* | *en qui*, *en que*, *par qui* | *in cui*, *con cui* | *en que*, *per que* | *en que*, *con que* | *em que*, *com que* | Preposition is the segmentation marker. |
| **Compound forms** | *quicumque*, *quisquis* | *whoever*, *whoso* | *quantque*, *quamque* | *chiunque*, *qualunque* | *qui que*, *qual que* | *quien quiera*, *qual quier* | *quem quer*, *qual quer* | Always segmented — open new dependent or free relative clause. |
| **Gendered / Agreed forms** | — | — | *(le)quel*, *(la)quelle* | *il quale*, *la quale*, *li quali* | *lo qual*, *la qual* | *el qual*, *la qual*, *los cuales*, *las cuales* | *o qual*, *a qual* | Segmented when functioning as true relative pronouns, not determiners. |
| **Adverbial relatives** | *unde*, *quo*, *ut* | *where*, *whence*, *as* | *dont*, *ou*, *quantque* | *donde*, *ove* | *d’on*, *on* | *donde*, *quando*, *como* | *onde*, *quando*, *como* | Segment onset when introducing adverbial subclause. |
| **Interrogative overlap** | *quis*, *quid* | *who*, *what* | *qui*, *que*, *(le)quel* | *chi*, *che* | *qui*, *que* | *quien*, *que*, *cual* | *quem*, *que*, *qual* | Always segmented when functioning as interrogative openers. |

---

💡 **Annotation Principle:**  
- All **relative** and **interrogative** pronouns act as **segmentation triggers** when they introduce a new syntactic or discourse unit.  
- **Prepositional forms** are segmented from the preposition (the preposition itself being the segmentation marker).  
- **Orthographic variation is preserved**; segmentation depends solely on **syntactic and functional role**, not spelling.  
- **Compound or free relatives** (*quem quer*, *quien quiera*, *chiunque*, etc.) are always segmented as they establish a new dependent clause.



### 🧾 Table — Core Relative Pronouns (Medieval Corpus)

| **Function / Type** | **Latin** | **Middle English** | **Old / Middle French** | **Medieval Italian** | **Catalan** | **Medieval Castilian** | **Medieval Portuguese** |
|----------------------|------------|--------------------|-------------------------|----------------------|--------------|------------------------|--------------------------|
| **Subject** | *qui*, *quae*, *quod* | *who*, *that*, *which* | *qui*, *ki* | *che*, *ch* | *que*, *qui* | *que* | *que* |
| **Direct Object** | *quem*, *quod* | *whom*, *that*, *which* | *que*, *ke*, *qe*, *qu* | *che*, *ch* | *que* | *que* | *que* |
| **Indirect / Oblique** | *cui*, *cujus*, *a quo* | *whom*, *whose*, *to whom* | *cui* | *cui* | *cui*, *a qui* | *a quien*, *cuyo* | *a quem*, *cujo* |
| **Possessive** | *cujus*, *cuius* | *whose* | *dont*, *dunt* | *di cui* | *d’on*, *de qui* | *de quien* | *de quem* |
| **Compound / Agreed Form** | — | — | *(le)quel*, *(la)quelle*, *(les)quels* | *il quale*, *la quale*, *li quali* | *lo qual*, *la qual*, *los quals* | *el qual*, *la qual*, *los cuales*, *las cuales* | *o qual*, *a qual*, *os quais*, *as quais*  |
| **Free / General Relative** | *quisquis*, *quicumque* | *whoever*, *whoso* | *quantque*, *quamque* | *chiunque*, *qualunque* | *qui que*, *qual que* | *quien quiera*, *qual quier* | *quem quer*, *qual quer* |




> **Observation (Portuguese):**  
> The forms *o qual, a qual, os quais, as quais* can appear in **contracted forms** with prepositions:  
> - **em + o → no qual** / **na qual** / **nos quais** / **nas quais**  
> - **de + o → do qual** / **da qual** / **dos quais** / **das quais**  
> - **por / per + o → pelo qual** / **pela qual** / **pelos quais** / **pelas quais**  
> - **para + o → para o qual** / **para a qual**  
>
> These combinations are treated as **compound relatives**, but are **not normalized** in transcription.  
> They should be annotated as **single relative markers**, since the preposition and article are morphologically bound to the relative base.


