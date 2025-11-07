# What do we segment ?

This guideline provides examples showing how segmentation operates in practice for a range of syntactic structures and languages.

- We segment **syntactically and semantically autonomous units** — clauses and other structures that introduce a new proposition or discourse act.


## 1. Sentence and Clause Beginnings

### General Principle

From a functional standpoint, it is essential to identify **sentence and clause openings**.  
These elements can be more challenging to recognize than conjunctions or relative pronouns, since they often appear **both at the start of a segment and within** one.

The following categories typically indicate the **beginning of a new sentence or clause**:


- **Personal pronouns**  
  > £Si li anoia moult li cheualliers £**Il** oste son  
  
  > £**él** e la sua muler penseren de la Verge
  
  > £**Eu** vijm a esta çidade £por hõrrar a festa .


- **Prepositions** introducing a new clause or sentence   
  > ne seuent nulle noueles de lancelot. £**Au** mains sil seussent celes
  
  > £vengono a qualche contesa £**con** qualche altro uccello di passaggio,

  > £lo qual volch degolar £**per** fer sacrifici a Deu, £**a** significar lo sacriffici [...]

  *Prepositions* are here annotated as the beginning of a new unit.


- **Definite or indefinite articles**  
  > £**Le** conte dist £que quant Agloual se fust parti  

  > £**El**Rei cuidando neeste feito,£pareçerom lhe as rrazõoes boas,
  
  > £Essendosi tre giorni riposato l'esercito, £**il** Turco deliberò di tornare adietro
  
  > £**vn** Donzel muy hermoso £caçando con vna leona 

  Definite articles *le* and *el* are annotated as the initial marker of a new clause.


---

## 2. Titles, Chapters, Epistles, and Other Structural Elements

### 🔹 General Principle

Structural divisions such as **titles**, **chapter headings**, **epistles**, **rubrics**, and similar paratextual elements constitute **independent segmentation units**. They serve organizational and rhetorical functions rather than syntactic ones, and therefore must be treated as **stand-alone segments** in the corpus.

###  Annotation Guidelines

- Each title or rubric is annotated as a **separate segment**, regardless of its punctuation or typographical layout.  
- Transitional or introductory formulas (e.g., *Here begins...*, *Explicit capitulum...*) are considered **part of the structural unit**, not of the following narrative segment. 
- When a structural marker is followed by narrative text on the same line, the **boundary is still maintained** to preserve hierarchical consistency.


### *Examples*

> £Delle citta di Ormuz e Bagdeth.

> £Lettera III

> £Del regno di Coulam

> £COMENCA LA PRIMERA PART DEL LIBRE DE TIRANT, £LA QUAL TRACTA DE CERTS VIRTUOSOS ACTES £QUE FÉU LO COMTE

> £Capitulo .ccxcj.

> £Capitulo .lxxvj. £como todos los caualleros fueron contentos £delo que don Quadragante propuso

---

## 3. Vocatives and Direct Address

### 🔹 General Principle

**Vocatives** — forms of direct address or proper names used to call upon an interlocutor — are often placed at the beginning of clauses or reported speech. Their position may **coincide with a segmentation point**, but they do **not automatically trigger segmentation** on their own.

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

---
## 4. Parenthetical Clauses (Incises)

### 🔹 Definition and Scope

**Parenthetical clauses**, or **incises**, are short reporting structures typically embedded within direct speech or narrative flow. They indicate **speech attribution or narrative modality**, and are treated as **autonomous discourse segments**.

### Annotation Guidelines

-Each incise is annotated as an **independent segment**, delimited by the points where direct speech is interrupted and resumed.

Segmenting incises allows the model to clearly identify reporting clauses, maintain syntactic rhythm, and distinguish between narrative framing and speaker turns.


### Examples:

> £Se eu cuidasse, £**disse Galvam**, £que me nom faleceríades aa primeira vez

> £whan thou wilt not do that thyng £that I requyre of thee?" £**And Taffile answerd to hym**, £“What nede have I of the frendship ...

> disse Lancelotto, £di queste lettere sapete vo' £chi- lle fece? —£Certo, £**diss’ egli**, no.

> £A non Dieu, £**fet mes sires Gauvains,** £nos avons anuit tant veu en dormant

> £'Alexander,' £**quod̛ he,** £'es a warrer man̛ & a wyse,

## 5. Reported Speech

Reported speech appears in two main forms:

1. **Direct speech** – the speaker’s words are quoted verbatim.  
   → Typically introduced by a *reporting verb*.  
2. **Indirect speech** – the speaker’s words are paraphrased or subordinated, usually introduced by *that* / *que*.

Both forms involve **speech markers** — lexical or verbal cues that attribute speech or thought.


### Annotation Notes

- The **token following a verb of saying** systematically functions as a **delimiter**, whether it introduces **direct** or **indirect** discourse.  
  > £A la postremería *dixo* : £“**Yo hire a Iherusalem la çibdat.”**  
  > £E despues que esto ovo fecho, *dixo* £**que se queria tornar para su tierra.**

- When the **subject** follows the reporting verb, segmentation occurs **after the subject**:  
  > *£E dixo el Rey : £¿**Commo fue eso ?**

- When the verb of saying occurs parenthetically (in incise), it is kept within the same segment:
  > **£señor, £dixo Bores, £yo no puedo agora alla tornar.”**
  
- **Interjections**, **adverbs of assertion** (*certes, certo, ciertamente, por verdad*, etc.) and **formulaic invocations** (*par Dieu*, *por Dios*, etc.) mark the **onset of a speech act** and are segmented as separate discourse units.


*Examples*

#### **Direct Speech**
> .£he depois *disse* a el rey archileus .£**bem ves tu £que nõ he rezam £que nos te tomemos en nossa merçee**

> £Et ela li *disse*: «**£Di'-me adoncha lo vostro consegio**». £Et elo disse: «**£Dama, £qui apresso un meyo**

> £Al quale lo can *respoxe*: «£**Acciò che non possa offendere queli £che passa davanti la mia ca'**

> £**Que cousa é ?** £*disse* el-rei. –£**Esto vos direi eu**, £*disse* el. **£Vós sabedes £que nos albergastes**


#### **Indirect Speech**

> £Quando Erec entendeu £que a justar lhi convĩĨa,  £*disse* £**que lhi nom era mester**,

> £But the labourer, £that was named Papirion, £*said* to his maister £**that he shold denye his cause hardily**

> £And forthwyth stepte in £and *sayd* £**that he hymself was culpable of the deth of this man**

> £E Jugurta, oÿt lo manament dels legats, £*respòs*  £**que a él no li ere res major ne pus** 



###  Main Markers of Direct Speech Onset 

| **Type** | **Latin** | **Middle English** | **Old / Middle French** | **Medieval Italian** | **Catalan** | **Medieval Castilian** | **Medieval Portuguese** |
|-----------|------------|--------------------|--------------------------|----------------------|--------------|------------------------|--------------------------|
| **Verbs of Saying** | *dixit*, *ait*, *inquit*, *respondit*, *clamavit*, *proclamans* | *seide*, *quoth*, *answerede*, *spak*, *bad* | *dist*, *dist il*, *respondi*, *parla*, *fet* | *disse*, *parlò*, *respuose* | *digua*, *respos*, *digué* | *dixo*, *respondió*, *preguntó* | *disse*, *respondeu*, *perguntou*, *afirmou* |
| **Interjections** | *O*, *Oh*, *ecce* | *O*, *A*, *Ah*, *Lo* | *fi*, *ha*, *haa*, *helas*| *ahi*, *oimè*, *o* | *O*, *O mísera de mi!*, *O trista de mi!*, *Ay* | *ay*, *o*, *ha*, *e* | *ai*, *oh*, *haa* |
| **Lexical / Adverbial Markers** | *Age vero*, *Nam* | *soothly*, *truly* | *certes*, *de voir*, *voire*,*oil*, *oy*, *naie* | *certo*, *vere*, *per verità* | *cert*, *verament* | *verdaderamente*,  | *certas*, *verdadeiramente*, *ora* |
| **Prepositional / Formulaic** | *Pater mi*, *Deo voveo*, *per dominum deum*, *in Dei nomine* | *forsoþe*, *by his worde* | *Par ma foy*, *si m’aït Diex*, *(de)par Dieu*, *En non Dieu*, *par mon chief* | *per Dio*, *per lo corpo di Cristo* | *per Déu*, *ho Maria* | *por dios*, *ay sancta maria val*, *a dios merced* | *par/por Deus*, *per minha fé*, *Santa Maria* , *Deus me valha*, *Senhor deos*|




----
## 6. Finite and Circumstantial Structures

In segmentation, both **finite** and **circumstantial** structures are treated as relevant discourse units.
A **finite clause**  expresses a complete syntactic proposition, whereas a  **circumstantial clause** introduces a temporal, causal, conditional, or concessive relation that often bears its own **semantic and rhetorical autonomy** within the discourse.


### Annotation Guidelines

- **Finite clauses** represent **independent syntactic and rhetorical units** and are therefore **always segmented**.  
- **Circumstantial** and **non-finite clauses** (temporal, causal, conditional, concessive, etc.) are **segmented** when they introduce a new **temporal**, **logical**, or **rhetorical boundary** in the discourse.  
- **Circumstantial markers** (e.g., *quant*, *aprés*, *si*) are annotated as **onset tokens** of the corresponding discourse segment ([see the table below](#main-conjunctions-and-conjunctive-phrases-introducing-circumstantial-clauses)).


### 6.1. Main Clauses

Main (finite) clauses are **independent and self-contained syntactic units**.  
They form the structural backbone of discourse segmentation and are and are always assigned an **independent segment**.

> £**E il conte di Fondi**, £nipote che·ffu di papa Bonifazio VIII,

> £**entrò in San Germano colle 'nsegne del re d'Ungheria** £e con gente d'arme.

- When a main clause is **interrupted or split** by subordinate or embedded material,
each **discontinuous segment** of the main clause should be **annotated as a separate discourse unit**.

> £**E dom Lopo Diaz** £que era dentro, £quando vyo que se non podia sayr, £**tomou hũũ froque e hũa aguilhada** £e, descalço come lavrador, £**e assi se sayu da villa £e se foy per antr'elles** £que o non conheceo nẽ hũũ.

> £E, quando o alaão assi he bem trilhado £e, às vegadas, quando o cavalo empeça en elle, £**caae.**
---
### 6.2. Ablative Absolute and Absolute Participial Clauses

**Absolute** or **detached constructions** express a circumstance that is **external to the syntactic frame** of the main clause.  
They are segmented as **autonomous discourse units** because they convey **background** or **parallel information**, often setting the temporal, causal, or situational context for the main event.

>  £**Licenziata adunque dalla nuova reina la lieta brigata,**

> £**Partito meser Gianni di Guascogna**

> £**Quo facto,** £illa subito evanuit,

> £**Oydo todo esto por el rey Arauigo**

---
### 6.3. Gerundive or Participial Clauses

**Gerundive** or **participial clauses** are **always segmented**, as they introduce **simultaneous**, **causal**, or other **circumstantial** information distinct from the main predication. Although their **subject** is usually **shared with the main clause**, they convey an **independent semantic event** that specifies **manner**, **time**, or **reason** relative to the main action.

*Examples*
> £**havyng pety and compassyon of hys handwerke and hys creatur** £turnyd helth into sekenesse...

> £**largiente et te laborante**, £perducta est usus tibi pallii concessio.

> £**sperando di venderlo al gran Turco per molto maggior prezzo**

>  £**navegant ab pròsper vent**

> £**Estando Abemaffa ẽ Vallença,** £pos seu amor cõ dous cavalleiros da vylla
---

### 6.4. Infinitival Clauses

Infinitival clauses are **non-finite verbal structures** that may function as complements, circumstantials, or adverbial expressions.  

### Annotation Guidelines

-  When the infinitive phrase is **introduced by a preposition**, the **preposition** itself is annotated as the **segment onset**.

- **Latin-specific cues for identification:**  
  - An infinitival clause often **begins with an accusative subject**, or  
  - **directly with an infinitive verb** when the subject is implicit.  

*Examples*
> £Coepit enim £**veterem Urbis gloriam deperditam deplorare,** £**et temporum injurias detestari,**

> £**por oyr** tan grandes loores del cauallero dela roca partida

> £**per possedere** l’amore de tanta donna cum legitimo nodo.

> £él e la sua muler penseren de la Verge £**a lausar** devotament,

> £**Et oÿ chanter les clers et sonner les cloches**, £si fu moult esmeus de pitié.

### 6.5. Circumstantial Clauses

Circumstantial clauses express temporal, causal, conditional, or concessive relations between two propositions.  
Although grammatically dependent, they introduce new **discourse frames** — temporal, logical, or argumentative — and are therefore **systematically segmented**.

Typical subtypes include:

- ### 6.5.1.**Temporal**  

  *Examples*

> £**Aprés que** aquestes coses foren oÿdes,

> £**depois que esto ouve feito enna Gasconha**, £ẽ hyndosse della, £chegoulhe mandado ẽ como de terra de mouros

> £quod pugnatores ordinent se £secundum formam quadrangularem, £**et postea** secundum triangularem, £**et deinde** secundum rotundam: £**et sic deinceps** debet assuefacere bellantes,

- ### 6.5.2. **Causal** 

*Examples*

> £Pero era vilania £**ca Mordret estava desarmado e a pee**

> £él dix a la sua muler £que pugés en un caval, £**per so car avien luyn as-anar**,£per què ela tremolan puyà al caval,

> £que li soudant la firent toute araser et abatre £**pour ce qu'il avoient sorti**

- ### 6.5.3. **Conditional** 

*Examples*

>  £**If nucha be kutt þoruȝ ouerþwert**, £þe wounde is mortal £for þe nobilte of nucha £þat comeþ fro þe brayn riȝt 

> £che,**se egli aveva commissione alcuna da Vostra Maestà**, £me la dovesse presentare,

> £**Si bonam conscientiam haberes**, £non multum mortem timeres.

> £Et dautre part £**se il li otroie samor**

- ### 6.5.4. **Concessive**  

  *Examples*

> £que mucho ha que del no se supieron nueuas ningunas £**aunque muchos de sus amigos lo han buscado con grandes afanes por tierras estrañas**

> £And hit is no merveylle, £**though hyt so happen** £for that man that is disagreable 

> £e adiante screvo, £**ainda que per fundamentos desvayrados** £syntom a tristeza,

- ### 6.5.5. Consecutive

  *Examples*

> e cusiu-los £**de manera que no·s puga exir la mel.**

> brother that vyenne hath had so moche Ioye £and so grete playsyr £whan she had knowleche £that ye were a lyue £**that it is wonder to byleue**

>  £& vos señora lleuareys vna capa abrochada: £& antifazes delante del rostro: £**de guisa que a todos ver podays £& ninguno no a vos.**

- ### 6.5.6. **Final**

  
  *Examples*

> et per vestras etiam literas exponentes et petentes humiliter, £**ut faciendae translationi favorem apostolicum et pium praeberemus assensum**

> £E mãdaae logo fazer as cartas £**pera que mha tirem** £e a mỹ que me saya de vossa terra.

> £mas el bien entendia £que el rrey lo fazia **£por que ele moriesse alla**

-------
### Main Conjunctions and Conjunctive Phrases Introducing Circumstantial Clauses 

| **Type of Clause** | **Latin** | **English** | **French** | **Italian** | **Catalan** | **Castilian** | **Portuguese** |
|--------------------|------------|--------------------|----------------|--------------------|--------------|----------------------|------------------------|
| **Causal** | *quia*, *quoniam*, *nam*, *et/enim*, *(propter) quod* | *for*, *for that*, *because* | *car*, *por ce que*, *puis que* |*conciosiaché*, *però che*, *imperò che*, *poi che*, *perché* | *car/cor*, *per ço que*, *perquè*, *pus que / pux que* | *ca*, *porque*, *por ende*, *pues (que)*, *por quanto* | *ca*, *porque*, *pois*, *por ende*, *porquuoanto* |
| **Temporal** | *cum*, *post/antequam*, *dum*, *quando(cumque)*, *cumque* | *when*, *after that*, *as soon as* | *tantost que*, *aprés ce que*, *tant que*, *depuis que* | *quando*, *poi che*, *dopo che*, *mentre che* , *indi*| *tantost*, *can*, *fins que*, *tro que*, *mentre que* | *cuando*, *aprés que*, *en quanto*, *desque*, *mientra*, *h/fasta (que)* | *quando*, *depois que*, *logo que*, *mentre que*, *des hora* |
| **Conditional** | *si*, *nisi*, *dummodo*, *etiamsi* | *if*, *and if*, *but if*, *unless* | *si/se/s'*, *mes se* | *se*, *qualora*, *purché* | *can*, *si*, *e si*, *mas si* | *si*, *sin que*, *sino* | *se*, *se nom*, *fora que* |
| **Concessive** | *quamvis*, *etsi*, *licet* | *though*, *although*, *even if* | *nonpourquant*, *combien que*, *quant que*| *benché*, *sebbene*, *ancorché*, *quantunque*, ** | *jatsie que*, *si bé (que)*, *encara que*, *malgrat que* | *comoquier que*, *aunque (bien)*, *maguer*, *bien que* | *ainda que*, *posto que* ,*todavia*, *conquanto* |
| **Adversative / Contrastive** | *sed*, *verum*, *tamen*, *autem* | *but*, *however*, *yet*, *nevertheless* | *mais/mes*, *fors que*, *toutefois*, *neantmoins* | *ma*, *però*, *tuttavia*, *nondimeno*, *anzi* | *mas/mes*, *emperó*, *entin*, *nogensmenys* | *mas*, *sino*, *pero*, *empero*  | *mas*, *porém*, *todavia*, *salvo (que)*, *antes* |
| **Resultative / Consecutive** | *ita... ut*, *sic... ut*, *ideo(que)*, *sicque* | *so... that*, *so that* | *siques*, *tant... que*, *en telle maniere que* | *laonde*, *imperciò*, *sicché*, *tanto che*, *così che*, *talché* | *tant... que*, *tan... que*, *de manera que*, *doncs / adonchs* | *tanto... que*, *por/en/de manera que* | *tão... que*, *assi que*, *de maneira que*, *de guisa que* |
| **Comparative** | *sicut*, *velut*, *quemadmodum*, *quam* | *as*, *as if*, *like as* | *comme*, *ainsi comme*, *si comme* | *come*, *siccome*, *quasi che* | *com*, *segons*, *axí com*, *aytant (que)* | *como*, *así como*, *tal como*| *como*, *assim como*, *bem como* |
| **Final (Purpose)** | *ut*, *ne*, *ad hoc quod* | *so that*, *that*, *in order that* | *pour ce que*, *a ce que* | *affinché*,*acciocché*, *perché*, *che* | *perquè*, *per/a asó que*  | *porque*, *para que* | *para que*, *por que* |

---
## 7. Completive and Relative Clauses

This section includes **finite subordinate clauses** that function as **syntactic dependents** of a matrix element (verb, noun, or pronoun).  
Unlike circumstantial clauses, these do not express temporal or causal relations but rather **fill syntactic roles** within the higher clause — either as **complements (completive clauses)** or as **modifiers (relative clauses)**.


- ### 7.1. Completive Clauses

Completive clauses (introduced by *que*, *that*, *quod*, etc.) function as **syntactic complements** of a matrix verb (*dire*, *penser*, *croire*, *savoir*, *respondre*, etc.).  
They express **propositional content**, often reporting speech, thought, or perception. Although grammatically subordinate, **completive clauses are segmented** as they convey a **distinct discourse act** — for example, when they represent a full statement, report, or belief introduced by a matrix predicate.

### Annotation Guidelines

- If the completive clause expresses a **full propositional content** (e.g., reported speech or assertion), it is **segmented**.  
- If the completive clause is **semantically weak** (e.g., part of a cognitive or modal expression like *il semble que*, *il faut que*), it may remain **unsegmented**.

*Examples*

> £lo qual li respòs £**que no sabia la via**

> £a significar lo sacriffici £**que Jesuchrist feu de si matex** £a morir per son poble.

> £Quando começou a anoitecer, £aveo £**que rei Mars passou per ante a câmara** £u Galaaz jazia


---

- ### 7.2. Relative Clauses

Relative clauses introduce **subordinate clauses** and act as **segmentation markers** whenever they open a new syntactic or discourse unit.  

### **Annotation Principle**

- All **relative** and **interrogative** pronouns — including their **prepositional or compound forms** — are annotated as **segmentation onsets** when they introduce a new clause or syntactic dependency.  

---

### **Special Cases**

#### **The form _quel_ (Old / Middle French)**  
The form **_quel_** is annotated as a segmentation token when used as a **relative**, **exclamative**, or **interrogative** pronoun,  
but **not** when it functions as an **indefinite determiner**:

> fait mander la nouvele dou tornoiement et a **quel** terme → 🚫 *no segmentation*

Nor when it appears in combination with *que*:  
> en **quel lieu £que** il fust  

When **_quel_** is repeated, only the **first occurrence** is annotated:  
> £**quel** besoins et **quel** auenture lauoit la amene  

Also includes **quantque**, **quamque**, etc.:  
> £Et elle crioit £**quamque** elle pooit  

---

- ### 7.2.1. Prepositional Relatives

When a relative pronoun is **introduced by a preposition**, the **preposition itself** is the segmentation marker.

> £**de quel** tornoiement li chevalier de ceanz parloient anuit après vespres  
> hũu filho £**a que** disserom dõ frei Alvoro Gomçallvez Pereira  

(See also [Prepositions](#sec:prep))

---

- ### 7.2.2. Free Relatives

A **free relative** (or substantive relative clause) is introduced by a relative word (*que, quien, cual, cuanto, donde*, etc.)  
**without an explicit antecedent**. It functions as a noun phrase within the main clause.

> £Dueña £diz Miles, £bien me nienbra £**quanto** me avedes dicho  

---

- ### 7.2.3. Adjectival / Adverbial Relatives

These are relative clauses introduced by adverbs that modify a noun,  
or express **circumstances of place, time, or manner** related to the main clause.

> £**donde** questo gentile huomo est morto  
> della grande servitudine £**ove** noi eravàno  

---

- ### **❓ Interrogative Use**

The same relative forms can function as **interrogative pronouns**.  
In interrogative contexts, they **always trigger segmentation**, since they introduce a new syntactic and rhetorical unit.

> £**ou** est il donques
> £Santa Maria, £**chi** mi gitterà di qui?


### **Summary Table: Main Relative and Interrogative Forms**


| **Function / Type** | **Latin** | **English** | **French** | **Italian** | **Catalan** | **Castilian** | **Portuguese** |
|----------------------|------------|--------------------|-------------------------|----------------------|--------------|------------------------|--------------------------|
| **General relative pronoun** | *qui*, *quae*, *quod* | *that*, *which*, *who*, *whom* | *qui*, *ki* | *che*, *ch*, *que* | *que*, *qui* | *que* | *que* |
| **Object / Complement** | *quem* | *whom*, *that* | *que*, *ke*, *qe*, *qu* | *che*, *ch* | *que* | *que* | *que* |
| **Indirect / Oblique** | *cui*, *cujus*, *a quo*  | *whom*, *whose* | *cui* | *cui* | *cui* | *cuyo*, *cui* | *cujo* |
| **Partitive / Possessive** | *cujus*, *de quo* | *of whom*, *whose* | *dont*, *dunt* | *di cui*, *onde* | *d’on*, *on* | *de quien*, *donde* | *de quem*, *onde* |
| **Locative** | *ubi* | *where* | *ou*, *o* | *ove*, *dove* | *on*, *on que* | *donde*, *en que* | *onde*, *em que* |
| **Instrumental / Prepositional** | *in quo*, *per quem* | *in which*, *by which* | *en qui*, *en que*, *par qui* | *in cui*, *con cui* | *en que*, *per que* | *en que*, *con que* | *em que*, *com que* |
| **Compound forms** | *quicumque*, *quisquis* | *whoever*, *whoso* | *quantque*, *quamque* | *chiunque*, *qualunque* | *qui que*, *qual que* | *quien quiera*, *qual quier* | *quem quer*, *qual quer* |
| **Gendered / Agreed forms** | — | — | *(le)quel*, *(la)quelle* | *il quale*, *la quale*, *li quali* | *lo qual*, *la qual* | *el qual*, *la qual*, *los cuales*, *las cuales* | *o qual*, *a qual*, *os quais*, *as quais*(*)|
| **Adverbial relatives** | *unde*, *quo*, *ut* | *where*, *whence*, *as* | *dont*, *ou*, *quantque* | *donde*, *ove* | *d’on*, *on* | *donde*, *quando*, *como* | *donde*, *onde*, *quando*, *como* |
| **Interrogative overlap** | *quis*, *quid* | *who*, *what* | *qui*, *que*, *(le)quel* | *chi*, *che* | *qui*, *que* | *quien*, *que*, *cual* | *quem*, *que*, *qual* |

---

> **Observation (Portuguese):**  
> The forms *o qual, a qual, os quais, as quais* can appear in **contracted forms** with prepositions:  
> - **em + o → no qual** / **na qual** / **nos quais** / **nas quais**  
> - **de + o → do qual** / **da qual** / **dos quais** / **das quais**  
> - **por / per + o → pelo qual** / **pela qual** / **pelos quais** / **pelas quais**  
> - **para + o → para o qual** / **para a qual**  

> These combinations are treated as **compound relatives**, but are **not normalized** in transcription.  
> They should be annotated as **single relative markers**, since the preposition and article are morphologically bound to the relative base.


---

> **Cross-linguistic Patterns**
>
> - **Latin:** frequent overlap between coordination (*nam*, *enim*) and subordination (*quia*, *cum*, *quoniam*).  
> - **English:** *for*, *and if*, *though*, *when* may act as causal, conditional, or concessive markers; parataxis remains common.  
> - **French:** alternation between *car* (coordinating causal) and *por ce que* (subordinating causal), with *quant* often bridging temporal and causal uses.  
> - **Italian:** flexible use of *che*, *però che*, *se*, *quando* for temporal, causal, or conditional relations.  
> - **Castilian:** *ca*, *mas*, *e si* often convey subordination through coordination, while *maguer* and *aunque* mark concessive subordination.  
> - **Catalan:** similar patterns with *car*, *que*, *si*, *maguer*, showing high functional overlap with Occitan.  
> - **Portuguese:** *ca*, *porque*, *mas*, *se* used with variable syntactic value; semantic relation governs segmentation.
