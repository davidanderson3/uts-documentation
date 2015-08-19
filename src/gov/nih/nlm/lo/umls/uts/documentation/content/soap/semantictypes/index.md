title=Semantic Network
date=2015-08-13
updated=2015-08-13
type=page
status=unpublished
navorder=5
~~~~~~


The UtsWsSemanticNetworkController object allows you to query the UMLS
Semantic Network. You can use this object to get information on:

-   What is the name of a Semantic Type for a given Semantic Term Unique
    Identifer (TUI)?
-   What are the relations between two Semantic Types?
-   What are all the Semantic Types is a given Semantic Group?

To make query the Semantic Network, create an instance of a
UtsWsSemanticNetworkController object, as well as the
UtsWsSecurityController object (if not already created).
<div class="code rounded-content-block">

<span class="code-comment">//create the reference variables</span>\
 private UtsWsSemanticNetworkController utsSemanticNetworkService;\
 private UtsWsSecurityController utsSecurityService;\
\
<span class="code-comment">//instantiate and handshake</span>\
 try {\
 utsSemanticNetworkService = (new
UtsWsSemanticNetworkControllerImplService())\
 .getUtsWsSemanticNetworkControllerImplPort();\
\
 utsSecurityService = (new UtsWsSecurityControllerImplService())\
 .getUtsWsSecurityControllerImplPort();\
 }\
\
 catch (Exception e) {\
 out.println("Error!!!" + e.getMessage());\
 }\
<span class="code-comment">//note that PSF objects are not passed as
parameters to methods associated with UtsWsSemanticNetworkController
objects.</span>\

</div>

\
### Semantic Type

<div class="group rounded-content-block">

<div id="getSemanticType" class="method rounded-content-block">

**Method: **<span class="method-name">getSemanticType</span><span
class="method-parameters">(String ticket,String version,String
semanticTypeId)</span>
**Returns:** <span class="method-return-type">SemanticTypeDTO </span>

<div class="method-description">

**Use Case:** This method takes a Semantic Type Unique Identifier (TUI)
as an argument, and returns information such as the Semantic Type's
definition, Tree Number, number of children, etc. In the example below
we use the identifier for the Semantic Type "Medical Device"

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

mySemTyRelDTO = utsSemanticNetworkService.getSemanticType(ticket,
umlsRelease, "T121");\
\
 String abbreviation = mySemTyRelDTO.getAbbreviation();\
 String definition = mySemTyRelDTO.getDefinition();\
 int childCnt = mySemTyRelDTO.getChildCount();\
 int relCnt = mySemTyRelDTO.getRelationCount();\
 String treeNum = mySemTyRelDTO.getTreeNumber();\
 String ui = mySemTyRelDTO.getUi();\
 String value = mySemTyRelDTO.getValue();\

</div>

#### Sample Input (C♯):

<div class="input rounded-content-block">

utsSemanticNetwork.getSemanticType(ticket, "2011AB", "T121");

</div>

#### Sample Output:

+--------------------------------------------------------------------------+
|   Abbreviation   Definition                                              |
|                                                                          |
|                                             Child Count   Relation Count |
|    Tree Number   Ui     Value                                            |
|   -------------- ------------------------------------------------------- |
| ------------------------------------------------------------------------ |
| ------------------------------------------- ------------- -------------- |
| -- ------------- ------ -------------------------                        |
|   phsu           A substance used in the treatment or prevention of path |
| ologic disorders. This includes substances that occur naturally in the b |
| ody and are administered therapeutically.   1             13             |
|    A1.4.1.1.1    T121   Pharmacologic Substance                          |
+--------------------------------------------------------------------------+

</div>

<div id="getAllSemanticTypes" class="method rounded-content-block">

**Method: **<span class="method-name">getAllSemanticTypes</span><span
class="method-parameters">(String ticket,String version)</span>
**Returns:** <span
class="method-return-type">ArrayList&lt;SemanticTypeDTO&gt; </span>

<div class="method-description">

**Use Case:** This method returns all Semantic Types for a given UMLS
release. In the example below, we show only the output for the first and
last member of the ArrayList returned (since there are over 130 Semantic
Types in the UMLS).

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

myarrSemTyRelDTO = utsSemanticNetworkService.getAllSemanticTypes
(ticket, umlsRelease);\
\
 for (int i = 0; i &lt; myarrSemTyRelDTO.size(); i++) {\
\
 SemanticTypeDTO mySemTyRel = myarrSemTyRelDTO.get(i);\
 String abbreviation = mySemTyRel.getAbbreviation();\
 String definition = mySemTyRel.getDefinition();\
 int childCnt = mySemTyRel.getChildCount();\
 int relCnt = mySemTyRel.getRelationCount();\
 String example = mySemTyRel.getExample();\
 String nonHuman = mySemTyRel.getNonHuman();\
 String treeNum = mySemTyRel.getTreeNumber();\
 String ui = mySemTyRel.getUi();\
 String value = mySemTyRel.getValue();\
 }\

</div>

#### Sample Input (C♯):

<div class="input rounded-content-block">

utsSemanticNetwork.getAllSemanticTypeGroups(ticket, "2011AB");

</div>

#### Sample Output:

+--------------------------------------------------------------------------+
|   Abbreviation   Definition                                              |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 Child Count   Relation C |
| ount   Tree Number      Ui     Value                                     |
|   -------------- ------------------------------------------------------- |
| ------------------------------------------------------------------------ |
| ------------------------------------------------------------------------ |
| ------------------------------------------------------------------------ |
| ------------------------------------------------------------------------ |
| ------------------------------------------------------------------------ |
| ------------------------------------------------------------------------ |
| ----------------------------------------------- ------------- ---------- |
| ------ ---------------- ------ ----------------------------------------- |
| --                                                                       |
|   aapp           Amino acids and chains of amino acids connected by pept |
| ide linkages.                                                            |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             2          |
|        A1.4.1.2.1.7     T116   Amino Acid, Peptide, or Protein           |
|   acab           An abnormal structure, or one that is abnormal in size  |
| or location, found in or deriving from a previously normal structure. Ac |
| quired abnormalities are distinguished from diseases even though they ma |
| y result in pathological functioning (e.g., "hernias incarcerate").      |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             3          |
|        A1.2.2.2         T020   Acquired Abnormality                      |
|   acty           An operation or series of operations that an organism o |
| r machine carries out or participates in.                                |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 4             1          |
|        B1               T052   Activity                                  |
|   aggp           An individual or individuals classified according to th |
| eir age.                                                                 |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             1          |
|        A2.9.4           T100   Age Group                                 |
|   amas           The sequence of amino acids as arrayed in chains, sheet |
| s, etc., within the protein molecule. It is of fundamental importance in |
|  determining protein structure.                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             3          |
|        A2.1.5.3.2       T087   Amino Acid Sequence                       |
|   amph           A cold-blooded, smooth-skinned vertebrate which charact |
| eristically hatches as an aquatic larva, breathing by gills. When mature |
| , the amphibian breathes with lungs.                                     |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             1          |
|        A1.1.3.1.1.1     T011   Amphibian                                 |
|   anab           An abnormal structure, or one that is abnormal in size  |
| or location.                                                             |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 2             12         |
|        A1.2.2           T190   Anatomical Abnormality                    |
|   anim           An organism with eukaryotic cells, and lacking stiff ce |
| ll walls, plastids and photosynthetic pigments.                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 1             2          |
|        A1.1.3.1         T008   Animal                                    |
|   anst           A normal or pathological part of the anatomy or structu |
| ral organization of an organism.                                         |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 3             5          |
|        A1.2             T017   Anatomical Structure                      |
|   antb           A pharmacologically active compound produced by growing |
|  microorganisms which kill or inhibit growth of other microorganisms.    |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             1          |
|        A1.4.1.1.1.1     T195   Antibiotic                                |
|   arch           A member of one of the three domains of life, formerly  |
| called Archaebacteria under the taxon Bacteria, but now considered separ |
| ate and distinct. Archaea are characterized by: 1) the presence of chara |
| cteristic tRNAs and ribosomal RNAs; 2) the absence of peptidoglycan cell |
|  walls; 3) the presence of ether-linked lipids built from branched-chain |
|  subunits; and 4) their occurrence in unusual habitats. While archaea re |
| semble bacteria in morphology and genomic organization, they resemble eu |
| karya in their method of genomic replication.   0             1          |
|        A1.1.1           T194   Archaeon                                  |
|   bacs           A generally endogenous substance produced or required b |
| y an organism, of primary interest because of its role in the biologic f |
| unctioning of the organism that produces it.                             |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 6             8          |
|        A1.4.1.1.3       T123   Biologically Active Substance             |
|   bact           A small, typically one-celled, prokaryotic micro-organi |
| sm.                                                                      |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             3          |
|        A1.1.2           T007   Bacterium                                 |
|   bdsu           Extracellular material, or mixtures of cells and extrac |
| ellular material, produced, excreted, or accreted by the body. Included  |
| here are substances such as saliva, dental enamel, sweat, and gastric ac |
| id.                                                                      |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             8          |
|        A1.4.2           T031   Body Substance                            |
|   bdsy           A complex of anatomical structures that performs a comm |
| on function.                                                             |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             3          |
|        A2.1.4.1         T022   Body System                               |
|   bhvr           Any of the psycho-social activities of humans or animal |
| s that can be observed directly by others or can be made systematically  |
| observable by the use of special strategies.                             |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 2             11         |
|        B1.1             T053   Behavior                                  |
|   biof           A state, activity or process of the body or one of its  |
| systems or parts.                                                        |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 2             5          |
|        B2.2.1           T038   Biologic Function                         |
|   bird           A vertebrate having a constant body temperature and cha |
| racterized by the presence of feathers.                                  |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             1          |
|        A1.1.3.1.1.2     T012   Bird                                      |
|   blor           An area, subdivision, or region of the body demarcated  |
| for the purpose of topographical description.                            |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             17         |
|        A2.1.5.2         T029   Body Location or Region                   |
|   bmod           A vocation, academic discipline, or field of study rela |
| ted to biomedicine.                                                      |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             1          |
|        A2.6.1           T091   Biomedical Occupation or Discipline       |
|   bodm           A substance used in biomedicine or dentistry predominan |
| tly for its physical, as opposed to chemical, properties. Included here  |
| are biocompatible materials, tissue adhesives, bone cements, resins, too |
| thpastes, etc.                                                           |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             1          |
|        A1.4.1.1.2       T122   Biomedical or Dental Material             |
|   bpoc           A collection of cells and tissues which are localized t |
| o a specific area or combine and carry out one or more specialized funct |
| ions of an organism. This ranges from gross structures to small componen |
| ts of complex organs. These structures are relatively localized in compa |
| rison to tissues.                                                        |
|                                                                          |
|                                                                          |
|                                                 0             24         |
|        A1.2.3.1         T023   Body Part, Organ, or Organ Component      |
|   bsoj           An area enclosed or surrounded by body parts or organs  |
| or the place where two anatomical structures meet or connect.            |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             20         |
|        A2.1.5.1         T030   Body Space or Junction                    |
|   carb           A generic term that includes monosaccharides, oligosacc |
| harides, and polysaccharides as well as substances derived from monosacc |
| harides by reduction of the carbonyl group (alditols), by oxidation of o |
| ne or more terminal group to carboxylic acids, or by replacement of one  |
| or more hydroxy groups by a hydrogen atom, an amino group, a thiol group |
|  or similar heteroatomic groups. It also includes derivatives of these c |
| ompounds. Included here are sugar phosphates. Excluded are glycolipids a |
| nd glycoproteins.                               0             1          |
|        A1.4.1.2.1.8     T118   Carbohydrate                              |
|   celc           A part of a cell or the intercellular matrix, generally |
|  visible by light microscopy.                                            |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             13         |
|        A1.2.3.4         T026   Cell Component                            |
|   celf           A physiologic function inherent to cells or cell compon |
| ents.                                                                    |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             1          |
|        B2.2.1.1.3       T043   Cell Function                             |
|   cell           The fundamental structural and functional unit of livin |
| g organisms.                                                             |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             11         |
|        A1.2.3.3         T025   Cell                                      |
|   cgab           An abnormal structure, or one that is abnormal in size  |
| or location, present at birth or evolving over time as a result of a def |
| ect in embryogenesis.                                                    |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             1          |
|        A1.2.2.1         T019   Congenital Abnormality                    |
|   chem           Compounds or substances of definite molecular compositi |
| on. Chemicals are viewed from two distinct perspectives in the network,  |
| functionally and structurally. Almost every chemical concept is assigned |
|  at least two types, generally one from the structure hierarchy and at l |
| east one from the function hierarchy.                                    |
|                                                                          |
|                                                                          |
|                                                 2             3          |
|        A1.4.1           T103   Chemical                                  |
|   chvf           A chemical viewed from the perspective of its functiona |
| l characteristics or pharmacological activities.                         |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 5             1          |
|        A1.4.1.1         T120   Chemical Viewed Functionally              |
|   chvs           A chemical or chemicals viewed from the perspective of  |
| their structural characteristics. Included here are concepts which can m |
| ean either a salt, an ion, or a compound (e.g., "Bromates" and "Bromides |
| ").                                                                      |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 3             1          |
|        A1.4.1.2         T104   Chemical Viewed Structurally              |
|   clas           A term or system of terms denoting an arrangement by cl |
| ass or category.                                                         |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             1          |
|        A2.4.1           T185   Classification                            |
|   clna           An observable or measurable property or state of an org |
| anism of clinical interest.                                              |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             1          |
|        A2.3.1           T201   Clinical Attribute                        |
|   clnd           A pharmaceutical preparation as produced by the manufac |
| turer. The name usually includes the substance, its strength, and the fo |
| rm, but may include the substance and only one of the other two items.   |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             1          |
|        A1.3.3           T200   Clinical Drug                             |
|   cnce           A broad type for grouping abstract entities or concepts |
| .                                                                        |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 9             1          |
|        A2               T077   Conceptual Entity                         |
|   comd           A pathologic function inherent to cells, parts of cells |
| , or molecules.                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             1          |
|        B2.2.1.2.2       T049   Cell or Molecular Dysfunction             |
|   crbs           The sequence of carbohydrates within polysaccharides, g |
| lycoproteins, and glycolipids.                                           |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             1          |
|        A2.1.5.3.3       T088   Carbohydrate Sequence                     |
|   diap           A procedure, method, or technique used to determine the |
|  nature or identity of a disease or disorder. This excludes procedures w |
| hich are primarily carried out on specimens in a laboratory.             |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             18         |
|        B1.3.1.2         T060   Diagnostic Procedure                      |
|   dora           An activity carried out for recreation or exercise, or  |
| as part of daily life.                                                   |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             4          |
|        B1.2             T056   Daily or Recreational Activity            |
|   drdd           A medical device that contains a clinical drug or drugs |
| .                                                                        |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             2          |
|        A1.3.1.1         T203   Drug Delivery Device                      |
|   dsyn           A condition which alters or interferes with a normal pr |
| ocess, state, or activity of an organism. It is usually characterized by |
|  the abnormal functioning of one or more of the host's systems, parts, o |
| r organs. Included here is a complex of symptoms descriptive of a disord |
| er.                                                                      |
|                                                                          |
|                                                                          |
|                                                 2             3          |
|        B2.2.1.2.1       T047   Disease or Syndrome                       |
|   edac           An activity related to the organization and provision o |
| f education.                                                             |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             1          |
|        B1.3.4           T065   Educational Activity                      |
|   eehu           A change in the natural environment that is a result of |
|  the activities of human beings.                                         |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             1          |
|        B2.1.1           T069   Environmental Effect of Humans            |
|   eico           An oxygenated metabolite from polyunsaturated 20 carbon |
|  fatty acids including lipoxygenase and cyclooxygenase products and thei |
| r synthetic analogs. This includes the prostaglandins and thromboxanes.  |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             1          |
|        A1.4.1.2.1.9.2   T111   Eicosanoid                                |
|   elii           One of the 109 presently known fundamental substances t |
| hat comprise all matter at and above the atomic level. This includes ele |
| mental metals, rare gases, and most abundant naturally occurring radioac |
| tive elements, as well as the ionic counterparts of elements (NA+, Cl-), |
|  and the less abundant isotopic forms. This does not include organic ion |
| s such as iodoacetate to which the type 'Organic Chemical' is assigned.  |
|                                                                          |
|                                                 0             1          |
|        A1.4.1.2.3       T196   Element, Ion, or Isotope                  |
|   emod           A representation in a non-human organism of a human dis |
| ease for the purpose of research into its mechanism or treatment.        |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             1          |
|        B2.2.1.2.3       T050   Experimental Model of Disease             |
|   emst           An anatomical structure that exists only before the org |
| anism is fully formed; in mammals, for example, a structure that exists  |
| only prior to the birth of the organism. This structure may be normal or |
|  abnormal.                                                               |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             12         |
|        A1.2.1           T018   Embryonic Structure                       |
|   enty           A broad type for grouping physical and conceptual entit |
| ies.                                                                     |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 2             1          |
|        A                T071   Entity                                    |
|   enzy           A complex chemical, usually a protein, that is produced |
|  by living cells and which catalyzes specific biochemical reactions. The |
| re are six main types of enzymes: oxidoreductases, transferases, hydrola |
| ses, lyases, isomerases, and ligases.                                    |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             1          |
|        A1.4.1.1.3.3     T126   Enzyme                                    |
|   euka           One of the three domains of life (the others being Bact |
| eria and Archaea), also called Eukarya. These are organisms whose cells  |
| are enclosed in membranes and possess a nucleus. They comprise almost al |
| l multicellular and many unicellular organisms, and are traditionally di |
| vided into groups (sometimes called kingdoms) including Animals, Plants, |
|  Fungi, various Algae, and other taxa that were previously part of the o |
| ld kingdom Protista.                                                     |
|                                                 3             1          |
|        A1.1.3           T204   Eukaryote                                 |
|   evnt           A broad type for grouping activities, processes and sta |
| tes.                                                                     |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 2             1          |
|        B                T051   Event                                     |
|   famg           An individual or individuals classified according to th |
| eir family relationships or relative position in the family unit.        |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             1          |
|        A2.9.3           T099   Family Group                              |
|   ffas           An anatomical structure in a fully formed organism; in  |
| mammals, for example, a structure in the body after the birth of the org |
| anism.                                                                   |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 5             8          |
|        A1.2.3           T021   Fully Formed Anatomical Structure         |
|   fish           A cold-blooded aquatic vertebrate characterized by fins |
|  and breathing by gills. Included here are fishes having either a bony s |
| keleton, such as a perch, or a cartilaginous skeleton, such as a shark,  |
| or those lacking a jaw, such as a lamprey or hagfish.                    |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             1          |
|        A1.1.3.1.1.3     T013   Fish                                      |
|   fndg           That which is discovered by direct observation or measu |
| rement of an organism attribute or condition, including the clinical his |
| tory of the patient. The history of the presence of a disease is a 'Find |
| ing' and is distinguished from the disease itself.                       |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 2             10         |
|        A2.2             T033   Finding                                   |
|   fngs           A eukaryotic organism characterized by the absence of c |
| hlorophyll and the presence of a rigid cell wall. Included here are both |
|  slime molds and true fungi such as yeasts, molds, mildews, and mushroom |
| s.                                                                       |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             3          |
|        A1.1.3.2         T004   Fungus                                    |
|   food           Any substance generally containing nutrients, such as c |
| arbohydrates, proteins, and fats, that can be ingested by a living organ |
| ism and metabolized into energy and body tissue. Some foods are naturall |
| y occurring, others are either partially or entirely made by humans.     |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             2          |
|        A1.4.3           T168   Food                                      |
|   ftcn           A concept which is of interest because it pertains to t |
| he carrying out of a process or activity.                                |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 1             1          |
|        A2.1.4           T169   Functional Concept                        |
|   genf           Functions of or related to the maintenance, translation |
|  or expression of the genetic material.                                  |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             2          |
|        B2.2.1.1.4.1     T045   Genetic Function                          |
|   geoa           A geographic location, generally having definite bounda |
| ries.                                                                    |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             4          |
|        A2.1.5.4         T083   Geographic Area                           |
|   gngm           A specific sequence, or in the case of the genome the c |
| omplete sequence, of nucleotides along a molecule of DNA or RNA (in the  |
| case of some viruses) which represent the functional units of heredity.  |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             8          |
|        A1.2.3.5         T028   Gene or Genome                            |
|   gora           An activity carried out by officially constituted gover |
| nments, or an activity related to the creation or enforcement of the rul |
| es or regulations governing some field of endeavor.                      |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             1          |
|        B1.3.3           T064   Governmental or Regulatory Activity       |
|   grpa           A conceptual entity which refers to the frequency or di |
| stribution of certain characteristics or phenomena in certain groups.    |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             2          |
|        A2.8             T102   Group Attribute                           |
|   grup           A conceptual entity referring to the classification of  |
| individuals according to certain shared characteristics.                 |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 5             8          |
|        A2.9             T096   Group                                     |
|   hcpp           A phenomenon or process that is a result of the activit |
| ies of human beings.                                                     |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 1             1          |
|        B2.1             T068   Human-caused Phenomenon or Process        |
|   hcro           An established organization which carries out specific  |
| functions related to health care delivery or research in the life scienc |
| es.                                                                      |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             2          |
|        A2.7.1           T093   Health Care Related Organization          |
|   hlca           An activity of or relating to the practice of medicine  |
| or involving the care of patients.                                       |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 3             2          |
|        B1.3.1           T058   Health Care Activity                      |
|   hops           A substance of concern because of its potentially hazar |
| dous or toxic effects. This would include most drugs of abuse, as well a |
| s agents that require special handling because of their toxicity.        |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             7          |
|        A1.4.1.1.5       T131   Hazardous or Poisonous Substance          |
|   horm           In animals, a chemical usually secreted by an endocrine |
|  gland whose products are released into the circulating fluid. Hormones  |
| act as chemical messengers and regulate various physiologic processes su |
| ch as growth, reproduction, metabolism, etc. They usually fall into two  |
| broad classes, steroid hormones and peptide hormones.                    |
|                                                                          |
|                                                                          |
|                                                 0             1          |
|        A1.4.1.1.3.2     T125   Hormone                                   |
|   humn           Modern man, the only remaining species of the Homo genu |
| s.                                                                       |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             1          |
|        A1.1.3.1.1.4.1   T016   Human                                     |
|   idcn           An abstract concept, such as a social, religious or phi |
| losophical concept.                                                      |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 5             3          |
|        A2.1             T078   Idea or Concept                           |
|   imft           A biologically active substance whose activities affect |
|  or play a role in the functioning of the immune system.                 |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             4          |
|        A1.4.1.1.3.5     T129   Immunologic Factor                        |
|   inbe           Behavior exhibited by a human or an animal that is not  |
| a direct result of interaction with other members of the species, but wh |
| ich may have an effect on others.                                        |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             6          |
|        B1.1.2           T055   Individual Behavior                       |
|   inch           Chemical elements and their compounds, excluding the hy |
| drocarbons and their derivatives (except carbides, carbonates, cyanides, |
|  cyanates and carbon disulfide). Generally inorganic compounds contain i |
| onic bonds. Included here are inorganic acids and salts, alloys, alkalie |
| s, and minerals.                                                         |
|                                                                          |
|                                                                          |
|                                                 0             1          |
|        A1.4.1.2.2       T197   Inorganic Chemical                        |
|   inpo           A traumatic wound, injury, or poisoning caused by an ex |
| ternal agent or force.                                                   |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             11         |
|        B2.3             T037   Injury or Poisoning                       |
|   inpr           A conceptual entity resulting from human endeavor. Conc |
| epts assigned to this type generally refer to information created by hum |
| ans for some purpose.                                                    |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 2             3          |
|        A2.4             T170   Intellectual Product                      |
|   irda           A substance primarily of interest for its use in labora |
| tory or diagnostic tests and procedures to detect, measure, examine, or  |
| analyze other chemicals, processes, or conditions.                       |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             1          |
|        A1.4.1.1.4       T130   Indicator, Reagent, or Diagnostic Aid     |
|   lang           The system of communication used by a particular nation |
|  or people.                                                              |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             1          |
|        A2.5             T171   Language                                  |
|   lbpr           A procedure, method, or technique used to determine the |
|  composition, quantity, or concentration of a specimen, and which is car |
| ried out in a clinical laboratory. Included here are procedures which me |
| asure the times and rates of reactions.                                  |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             17         |
|        B1.3.1.1         T059   Laboratory Procedure                      |
|   lbtr           The outcome of a specific test to measure an attribute  |
| or to determine the presence, absence, or degree of a condition.         |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             9          |
|        A2.2.1           T034   Laboratory or Test Result                 |
|   lipd           An inclusive group of fat or fat-derived substances tha |
| t are soluble in nonpolar solvents related to fatty acid esters, fatty a |
| lcohols, sterols, waxes, etc. Included in this group are the saponifiabl |
| e lipids such as glycerides (fats and oils), essential (volatile) oils,  |
| and phospholipids.                                                       |
|                                                                          |
|                                                                          |
|                                                 2             1          |
|        A1.4.1.2.1.9     T119   Lipid                                     |
|   mamm           A vertebrate having a constant body temperature and cha |
| racterized by the presence of hair, mammary glands and sweat glands.     |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 1             1          |
|        A1.1.3.1.1.4     T015   Mammal                                    |
|   mbrt           Any of the techniques used in the study of or the direc |
| ted modification of the gene complement of a living organism.            |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             3          |
|        B1.3.2.1         T063   Molecular Biology Research Technique      |
|   mcha           An activity carried out primarily or exclusively by mac |
| hines.                                                                   |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             4          |
|        B1.4             T066   Machine Activity                          |
|   medd           A manufactured object used primarily in the diagnosis,  |
| treatment, or prevention of physiologic or anatomic disorders.           |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 1             7          |
|        A1.3.1           T074   Medical Device                            |
|   menp           A physiologic function involving the mind or cognitive  |
| processing.                                                              |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             7          |
|        B2.2.1.1.1.1     T041   Mental Process                            |
|   mnob           A physical object made by human beings.                 |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 3             4          |
|        A1.3             T073   Manufactured Object                       |
|   mobd           A clinically significant dysfunction whose major manife |
| station is behavioral or psychological. These dysfunctions may have iden |
| tified or presumed biological etiologies or manifestations.              |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             6          |
|        B2.2.1.2.1.1     T048   Mental or Behavioral Dysfunction          |
|   moft           A physiologic function occurring at the molecular level |
| .                                                                        |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 1             1          |
|        B2.2.1.1.4       T044   Molecular Function                        |
|   mosq           A broad type for grouping the collected sequences of am |
| ino acids, carbohydrates, and nucleotide sequences. Descriptions of thes |
| e sequences are generally reported in the published literature and/or ar |
| e deposited in and maintained by databanks such as GenBank, European Mol |
| ecular Biology Laboratory (EMBL), National Biomedical Research Foundatio |
| n (NBRF), or other sequence repositories.                                |
|                                                                          |
|                                                 3             1          |
|        A2.1.5.3         T085   Molecular Sequence                        |
|   neop           A new and abnormal growth of tissue in which the growth |
|  is uncontrolled and progressive. The growths may be malignant or benign |
| .                                                                        |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             1          |
|        B2.2.1.2.1.2     T191   Neoplastic Process                        |
|   nnon           A complex compound of high molecular weight occurring i |
| n living cells. These are basically of two types, ribonucleic (RNA) and  |
| deoxyribonucleic (DNA) acids. Nucleic acids are made of nucleotides (nit |
| rogen-containing base, a 5-carbon sugar, and one or more phosphate group |
| ) linked together by a phosphodiester bond between the 5' and 3' carbon  |
| atoms. Nucleosides are compounds composed of a purine or pyrimidine base |
|  (usually adenine, cytosine, guanine, thymine, uracil) linked to either  |
| a ribose or a deoxyribose sugar.                0             1          |
|        A1.4.1.2.1.5     T114   Nucleic Acid, Nucleoside, or Nucleotide   |
|   npop           A phenomenon or process that occurs irrespective of the |
|  activities of human beings.                                             |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 1             3          |
|        B2.2             T070   Natural Phenomenon or Process             |
|   nsba           An endogenous substance whose activities affect or play |
|  an important role in the functioning of the nervous system. Included he |
| re are catecholamines, neuroregulators, neurophysins, etc.               |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             1          |
|        A1.4.1.1.3.1     T124   Neuroreactive Substance or Biogenic Amine |
|   nusq           The sequence of purines and pyrimidines in nucleic acid |
| s and polynucleotides. Included here are nucleotide-rich regions, conser |
| ved sequence, and DNA transforming region.                               |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             4          |
|        A2.1.5.3.1       T086   Nucleotide Sequence                       |
|   ocac           An activity carried out as part of an occupation or job |
| .                                                                        |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 4             5          |
|        B1.3             T057   Occupational Activity                     |
|   ocdi           A vocation, academic discipline, or field of study, or  |
| a subpart of an occupation or discipline.                                |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 1             2          |
|        A2.6             T090   Occupation or Discipline                  |
|   opco           An organic compound containing phosphorus as a constitu |
| ent. Included here are organic phosphinic, phosphonic and phosphoric aci |
| d derivatives and their thiophosphorus counterparts. Excluded are phosph |
| olipids, sugar phosphates, phosphoproteins, nucleotides, and nucleic aci |
| ds.                                                                      |
|                                                                          |
|                                                                          |
|                                                 0             1          |
|        A1.4.1.2.1.6     T115   Organophosphorus Compound                 |
|   orch           The general class of carbon-containing compounds, usual |
| ly based on carbon chains or rings, and also containing hydrogen (hydroc |
| arbons), with or without nitrogen, oxygen, or other elements in which th |
| e bonding between elements is generally covalent.                        |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 5             1          |
|        A1.4.1.2.1       T109   Organic Chemical                          |
|   orga           A property of the organism or its major parts.          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 1             7          |
|        A2.3             T032   Organism Attribute                        |
|   orgf           A physiologic function of the organism as a whole, of m |
| ultiple organ systems, or of multiple organs or tissues.                 |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 1             5          |
|        B2.2.1.1.1       T040   Organism Function                         |
|   orgm           Generally, a living individual, including all plants an |
| d animals.                                                               |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 4             2          |
|        A1.1             T001   Organism                                  |
|   orgt           The result of uniting for a common purpose or function. |
|  The continued existence of an organization is not dependent on any of i |
| ts members, its location, or particular facility. Components or subparts |
|  of organizations are also included here. Although the names of organiza |
| tions are sometimes used to refer to the buildings in which they reside, |
|  they are not inherently physical in nature.                             |
|                                                                          |
|                                                 3             4          |
|        A2.7             T092   Organization                              |
|   ortf           A physiologic function of a particular organ, organ sys |
| tem, or tissue.                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             4          |
|        B2.2.1.1.2       T042   Organ or Tissue Function                  |
|   patf           A disordered process, activity, or state of the organis |
| m as a whole, of a body system or systems, or of multiple organs or tiss |
| ues. Included here are normal responses to a negative stimulus as well a |
| s patholologic conditions or states that are less specific than a diseas |
| e. Pathologic functions frequently have systemic effects.                |
|                                                                          |
|                                                                          |
|                                                 3             19         |
|        B2.2.1.2         T046   Pathologic Function                       |
|   phob           An object perceptible to the sense of vision or touch.  |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 4             1          |
|        A1               T072   Physical Object                           |
|   phpr           A process or state which occurs naturally or as a resul |
| t of an activity.                                                        |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 3             3          |
|        B2               T067   Phenomenon or Process                     |
|   phsf           A normal process, activity, or state of the body.       |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 4             5          |
|        B2.2.1.1         T039   Physiologic Function                      |
|   phsu           A substance used in the treatment or prevention of path |
| ologic disorders. This includes substances that occur naturally in the b |
| ody and are administered therapeutically.                                |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 1             13         |
|        A1.4.1.1.1       T121   Pharmacologic Substance                   |
|   plnt           An organism having cellulose cell walls, growing by syn |
| thesis of inorganic substances, generally distinguished by the presence  |
| of chlorophyll, and lacking the power of locomotion. Plant parts are inc |
| luded here as well.                                                      |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             2          |
|        A1.1.3.3         T002   Plant                                     |
|   podg           An individual or individuals classified according to a  |
| disability, disease, condition or treatment.                             |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             1          |
|        A2.9.5           T101   Patient or Disabled Group                 |
|   popg           An indivdual or individuals classified according to the |
| ir sex, racial origin, religion, common place of living, financial or so |
| cial status, or some other cultural or behavioral attribute.             |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             4          |
|        A2.9.2           T098   Population Group                          |
|   prog           An individual or individuals classified according to th |
| eir vocation.                                                            |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             5          |
|        A2.9.1           T097   Professional or Occupational Group        |
|   pros           An organization uniting those who have a common vocatio |
| n or who are involved with a common field of study.                      |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             1          |
|        A2.7.2           T094   Professional Society                      |
|   qlco           A concept which is an assessment of some quality, rathe |
| r than a direct measurement.                                             |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             2          |
|        A2.1.2           T080   Qualitative Concept                       |
|   qnco           A concept which involves the dimensions, quantity or ca |
| pacity of something using some unit of measure, or which involves the qu |
| antitative comparison of entities.                                       |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             4          |
|        A2.1.3           T081   Quantitative Concept                      |
|   rcpt           A specific structure or site on the cell surface or wit |
| hin its cytoplasm that recognizes and binds with other specific molecule |
| s. These include the proteins on the surface of an immunocompetent cell  |
| that binds with antigens, or proteins found on the surface molecules tha |
| t bind with hormones or neurotransmitters and react with other molecules |
|  that respond in a specific way.                                         |
|                                                                          |
|                                                 0             1          |
|        A1.4.1.1.3.6     T192   Receptor                                  |
|   rept           A cold-blooded vertebrate having an external covering o |
| f scales or horny plates. Reptiles breathe by means of lungs and are gen |
| erally egg-laying.                                                       |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             1          |
|        A1.1.3.1.1.5     T014   Reptile                                   |
|   resa           An activity carried out as part of research or experime |
| ntation.                                                                 |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 1             9          |
|        B1.3.2           T062   Research Activity                         |
|   resd           A manufactured object used primarily in carrying out sc |
| ientific research or experimentation.                                    |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             1          |
|        A1.3.2           T075   Research Device                           |
|   rnlw           An intellectual product resulting from legislative or r |
| egulatory activity.                                                      |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             3          |
|        A2.4.2           T089   Regulation or Law                         |
|   sbst           A material with definite or fairly definite chemical co |
| mposition.                                                               |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 3             5          |
|        A1.4             T167   Substance                                 |
|   shro           An organization whose purpose and function is to provid |
| e assistance to the needy or to offer support to those sharing similar p |
| roblems.                                                                 |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             2          |
|        A2.7.3           T095   Self-help or Relief Organization          |
|   socb           Behavior that is a direct result or function of the int |
| eraction of humans or animals with their fellows. This includes behavior |
|  that may be considered anti-social.                                     |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             2          |
|        B1.1.1           T054   Social Behavior                           |
|   sosy           An observable manifestation of a disease or condition b |
| ased on clinical judgment, or a manifestation of a disease or condition  |
| which is experienced by the patient and reported as a subjective observa |
| tion.                                                                    |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             5          |
|        A2.2.2           T184   Sign or Symptom                           |
|   spco           A location, region, or space, generally having definite |
|  boundaries.                                                             |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 4             1          |
|        A2.1.5           T082   Spatial Concept                           |
|   strd           One of a group of polycyclic, 17-carbon-atom, fused-rin |
| g compounds occurring both in natural and synthetic forms. Included here |
|  are naturally occurring and synthetic steroids, bufanolides, cardanolid |
| es, homosteroids, norsteroids, and secosteroids.                         |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             1          |
|        A1.4.1.2.1.9.1   T110   Steroid                                   |
|   tisu           An aggregation of similarly specialized cells and the a |
| ssociated intercellular substance. Tissues are relatively non-localized  |
| in comparison to body parts, organs or organ components.                 |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             17         |
|        A1.2.3.2         T024   Tissue                                    |
|   tmco           A concept which pertains to time or duration.           |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             5          |
|        A2.1.1           T079   Temporal Concept                          |
|   topp           A procedure, method, or technique designed to prevent a |
|  disease or a disorder, or to improve physical function, or used in the  |
| process of treating a disease or injury.                                 |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             12         |
|        B1.3.1.3         T061   Therapeutic or Preventive Procedure       |
|   virs           An organism consisting of a core of a single nucleic ac |
| id enclosed in a protective coat of protein. A virus may replicate only  |
| inside a host living cell. A virus exhibits some but not all of the usua |
| l characteristics of living things.                                      |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             3          |
|        A1.1.4           T005   Virus                                     |
|   vita           A substance, usually an organic chemical complex, prese |
| nt in natural products or made synthetically, which is essential in the  |
| diet of man or other higher animals. Included here are vitamin precursor |
| s, provitamins, and vitamin supplements.                                 |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 0             1          |
|        A1.4.1.1.3.4     T127   Vitamin                                   |
|   vtbt           An animal which has a spinal column.                    |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                 5             1          |
|        A1.1.3.1.1       T010   Vertebrate                                |
+--------------------------------------------------------------------------+

</div>

<div id="getSemanticTypeRelations" class="method rounded-content-block">

**Method: **<span
class="method-name">getSemanticTypeRelations</span><span
class="method-parameters">(String ticket,String version,String
semanticTypeId)</span>
**Returns:** <span
class="method-return-type">ArrayList&lt;SemanticTypeRelationDTO&gt; </span>

<div class="method-description">

**Use Case:** Given a UMLS release and a semantic type unique identifier
(TUI), this call returns the semantic type relations that relate the
given semantic type with other semantic types.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

myarrSemTyRelDTO = utsSemanticNetworkService.getSemanticTypeRelations
(ticket, umlsRelease, "T005");\
\
 for (int i = 0; i &lt; myarrSemTyRelDTO.size(); i++) {\
 SemanticTypeRelationDTO mySemTyRel = myarrSemTyRelDTO.get(i);\
 String relAbbr = mySemTyRel.getRelationLabel().getAbbreviation();\
 String relDef = mySemTyRel.getRelationLabel().getDefinition();\
 String relInvLabel = mySemTyRel.getRelationLabel().getInverseLabel();\
 String relTreeNum = mySemTyRel.getRelationLabel().getTreeNumber();\
 String relUi = mySemTyRel.getRelationLabel().getUi();\
 int relChildCnt = mySemTyRel.getRelationLabel().getChildCount();\
 int relRelCnt = mySemTyRel.getRelationLabel().getRelationCount();\
\
 String SemTypeAbbr =
mySemTyRel.getRelatedSemanticType().getAbbreviation();\
 String SemTypeDef =
mySemTyRel.getRelatedSemanticType().getDefinition();\
 String SemTypeTreeNum =
mySemTyRel.getRelatedSemanticType().getTreeNumber();\
 String SemTypeUi = mySemTyRel.getRelatedSemanticType().getUi();\
 String SemTypeVal = mySemTyRel.getRelatedSemanticType().getValue();\
 String SemTypeUsage =
mySemTyRel.getRelatedSemanticType().getUsageNote();\
 int SemTypeChildCnt =
mySemTyRel.getRelatedSemanticType().getChildCount();\
 int SemTypeRelCnt =
mySemTyRel.getRelatedSemanticType().getRelationCount();\
 }\

</div>

#### Sample Output:

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  RelationLabel Abbreviation: CA\
   RelationLabel Definition: Brings about a condition or an effect. Implied here is that an agent, such as for example, a pharmacologic substance or an organism, has brought about the effect. This includes induces, effects, evokes, and etiology.\
   RelationLabel InverseLabel: caused\_by\
   RelationLabel Tree Number: R3.2.2\
   RelationLabel Ui: T147\
   RelationLabel UsageNote: null\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: patf\
   RelatedSemanticType Definition: A disordered process, activity, or state of the organism as a whole, of a body system or systems, or of multiple organs or tissues. Included here are normal responses to a negative stimulus as well as patholologic conditions or states that are less specific than a disease. Pathologic functions frequently have systemic effects.\
   RelatedSemanticType Tree Number: B2.2.1.2\
   RelatedSemanticType Ui: T046\
   RelatedSemanticType Value: Pathologic Function\
   RelatedSemanticType UsageNote: If the process is specific, for example to a site or substance, then 'Disease or Syndrome' will be assigned and not 'Pathologic Function'. For example, "cerebral anoxia", "brain edema", and "milk hypersensitivity" will all be assigned to 'Disease or Syndrome' only.\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 19\
  \
   RelationLabel Abbreviation: IS\
   RelationLabel Definition: The basic hierarchical link in the Network. If one item "isa" another item then the first item is more specific in meaning than the second item.\
   RelationLabel InverseLabel: inverse\_isa\
   RelationLabel Tree Number: H\
   RelationLabel Ui: T186\
   RelationLabel UsageNote: null\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: orgm\
   RelatedSemanticType Definition: Generally, a living individual, including all plants and animals.\
   RelatedSemanticType Tree Number: A1.1\
   RelatedSemanticType Ui: T001\
   RelatedSemanticType Value: Organism\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 4\
   RelatedSemanticType Relation Count: 2\
  \
   RelationLabel Abbreviation: LO\
   RelationLabel Definition: The position, site, or region of an entity or the site of a process.\
   RelationLabel InverseLabel: has\_location\
   RelationLabel Tree Number: R2.1\
   RelationLabel Ui: T135\
   RelationLabel UsageNote: null\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: bacs\
   RelatedSemanticType Definition: A generally endogenous substance produced or required by an organism, of primary interest because of its role in the biologic functioning of the organism that produces it.\
   RelatedSemanticType Tree Number: A1.4.1.1.3\
   RelatedSemanticType Ui: T123\
   RelatedSemanticType Value: Biologically Active Substance\
   RelatedSemanticType UsageNote: If a substance is both endogenous and typically used as a drug, then this type and the type 'Pharmacologic Substance' are assigned.\
   RelatedSemanticType Child Count: 6\
   RelatedSemanticType Relation Count: 8\
  \
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

</div>

<div id="getSemanticTypeRelationsForPair"
class="method rounded-content-block">

**Method: **<span
class="method-name">getSemanticTypeRelationsForPair</span><span
class="method-parameters">(String ticket,String version,String
semanticTypeId,String relatedSemanticTypeId)</span>
**Returns:** <span
class="method-return-type">ArrayList&lt;SemanticTypeRelationDTO&gt; </span>

<div class="method-description">

**Use Case:** This method returns all the relations between a pair of
Semantic Types. In the example below, we extract the 2 relations -
"analyzes" and "measures" - between T059 ("Laboratory Procedure") and
T031 ("Body Substance").

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

myarrSemTyRelDTO =
utsSemanticNetworkService.getSemanticTypeRelationsForPair (ticket,
umlsRelease, "T059", "T031");\
\
 for (int i = 0; i &lt; myarrSemTyRelDTO.size(); i++) {\
 SemanticTypeRelationDTO mySemTyRel = myarrSemTyRelDTO.get(i);\
 String relAbbr = mySemTyRel.getRelationLabel().getAbbreviation();\
 String relDef = mySemTyRel.getRelationLabel().getDefinition();\
 String relInvLabel = mySemTyRel.getRelationLabel().getInverseLabel();\
 String relTreeNum = mySemTyRel.getRelationLabel().getTreeNumber();\
 String relUi = mySemTyRel.getRelationLabel().getUi();\
 String relUsageNote = mySemTyRel.getRelationLabel().getUsageNote();\
 int relChildCnt = mySemTyRel.getRelationLabel().getChildCount();\
 int relRelCnt = mySemTyRel.getRelationLabel().getRelationCount();\
\
 String SemTypeAbbr =
mySemTyRel.getRelatedSemanticType().getAbbreviation();\
 String SemTypeDef =
mySemTyRel.getRelatedSemanticType().getDefinition();\
 String SemTypeTreeNum =
mySemTyRel.getRelatedSemanticType().getTreeNumber();\
 String SemTypeUi = mySemTyRel.getRelatedSemanticType().getUi();\
 String SemTypeVal = mySemTyRel.getRelatedSemanticType().getValue();\
 String SemTypeUsage =
mySemTyRel.getRelatedSemanticType().getUsageNote();\
 int SemTypeChildCnt =
mySemTyRel.getRelatedSemanticType().getChildCount();\
 int SemTypeRelCnt =
mySemTyRel.getRelatedSemanticType().getRelationCount();\
 }\

</div>

#### Sample Input (C♯):

<div class="input rounded-content-block">

utsSemanticNetwork.getSemanticTypeRelationsForPair(ticket, "2011AB",
"T059", "T031");

</div>

#### Sample Output:

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  RelationLabel Abbreviation: AN\
   RelationLabel Definition: Studies or examines using established quantitative or qualitative methods.\
   RelationLabel InverseLabel: analyzed\_by\
   RelationLabel Tree Number: R5.3\
   RelationLabel Ui: T193\
   RelationLabel Child Count: 1\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: bdsu\
   RelatedSemanticType Definition: Extracellular material, or mixtures of cells and extracellular material, produced, excreted, or accreted by the body. Included here are substances such as saliva, dental enamel, sweat, and gastric acid.\
   RelatedSemanticType Tree Number: A1.4.2\
   RelatedSemanticType Ui: T031\
   RelatedSemanticType Value: Body Substance\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 8\
  \
   RelationLabel Abbreviation: MS\
   RelationLabel Definition: Ascertains or marks the dimensions, quantity, degree, or capacity of.\
   RelationLabel InverseLabel: measured\_by\
   RelationLabel Tree Number: R5.5\
   RelationLabel Ui: T162\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: bdsu\
   RelatedSemanticType Definition: Extracellular material, or mixtures of cells and extracellular material, produced, excreted, or accreted by the body. Included here are substances such as saliva, dental enamel, sweat, and gastric acid.\
   RelatedSemanticType Tree Number: A1.4.2\
   RelatedSemanticType Ui: T031\
   RelatedSemanticType Value: Body Substance\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 8\
  \
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

</div>

<div id="getInverseSemanticTypeRelations"
class="method rounded-content-block">

**Method: **<span
class="method-name">getInverseSemanticTypeRelations</span><span
class="method-parameters">(String ticket,String version,String
semanticTypeId)</span>
**Returns:** <span
class="method-return-type">ArrayList&lt;SemanticTypeRelationDTO&gt; </span>

<div class="method-description">

**Use Case:** Given a UMLS release and a semantic type unique identifier
(TUI), this call returns the inverse semantic type relations that relate
other semantic types to the given semantic type. For example, the
semantic type "Pathologic Function" (TUI=T046) has several inverse
semantic type relations, one of which is "has\_manifestation," as in
"Injury or Poisoning has\_manifestation Pathologic Function."

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

myarrSemTyRelDTO =
utsSemanticNetworkService.getInverseSemanticTypeRelations (ticket,
umlsRelease, "T046");\
\
 for (int i = 0; i &lt; myarrSemTyRelDTO.size(); i++) {\
 SemanticTypeRelationDTO mySemTyRel = myarrSemTyRelDTO.get(i);\
 String relAbbr = mySemTyRel.getRelationLabel().getAbbreviation();\
 String relDef = mySemTyRel.getRelationLabel().getDefinition();\
 String relInvLabel = mySemTyRel.getRelationLabel().getInverseLabel();\
 String relTreeNum = mySemTyRel.getRelationLabel().getTreeNumber();\
 String relUi = mySemTyRel.getRelationLabel().getUi();\
 String relUsageNote = mySemTyRel.getRelationLabel().getUsageNote();\
 int relChildCnt = mySemTyRel.getRelationLabel().getChildCount();\
 int relRelCnt = mySemTyRel.getRelationLabel().getRelationCount();\
\
 String SemTypeAbbr =
mySemTyRel.getRelatedSemanticType().getAbbreviation();\
 String SemTypeDef =
mySemTyRel.getRelatedSemanticType().getDefinition();\
 String SemTypeTreeNum =
mySemTyRel.getRelatedSemanticType().getTreeNumber();\
 String SemTypeUi = mySemTyRel.getRelatedSemanticType().getUi();\
 String SemTypeVal = mySemTyRel.getRelatedSemanticType().getValue();\
 String SemTypeUsage =
mySemTyRel.getRelatedSemanticType().getUsageNote();\
 int SemTypeChildCnt =
mySemTyRel.getRelatedSemanticType().getChildCount();\
 int SemTypeRelCnt =
mySemTyRel.getRelatedSemanticType().getRelationCount();\
 }\

</div>

#### Sample Output:

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  RelationLabel Abbreviation: IN\
   RelationLabel Definition: Gives evidence for the presence at some time of an entity or process.\
   RelationLabel InverseLabel: indicated\_by\
   RelationLabel Tree Number: R3.7\
   RelationLabel Ui: T156\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: patf\
   RelatedSemanticType Definition: A disordered process, activity, or state of the organism as a whole, of a body system or systems, or of multiple organs or tissues. Included here are normal responses to a negative stimulus as well as patholologic conditions or states that are less specific than a disease. Pathologic functions frequently have systemic effects.\
   RelatedSemanticType Tree Number: B2.2.1.2\
   RelatedSemanticType Ui: T046\
   RelatedSemanticType Value: Pathologic Function\
   RelatedSemanticType UsageNote: If the process is specific, for example to a site or substance, then 'Disease or Syndrome' will be assigned and not 'Pathologic Function'. For example, "cerebral anoxia", "brain edema", and "milk hypersensitivity" will all be assigned to 'Disease or Syndrome' only.\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 19\
  \
   RelationLabel Abbreviation: CA\
   RelationLabel Definition: Brings about a condition or an effect. Implied here is that an agent, such as for example, a pharmacologic substance or an organism, has brought about the effect. This includes induces, effects, evokes, and etiology.\
   RelationLabel InverseLabel: caused\_by\
   RelationLabel Tree Number: R3.2.2\
   RelationLabel Ui: T147\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: patf\
   RelatedSemanticType Definition: A disordered process, activity, or state of the organism as a whole, of a body system or systems, or of multiple organs or tissues. Included here are normal responses to a negative stimulus as well as patholologic conditions or states that are less specific than a disease. Pathologic functions frequently have systemic effects.\
   RelatedSemanticType Tree Number: B2.2.1.2\
   RelatedSemanticType Ui: T046\
   RelatedSemanticType Value: Pathologic Function\
   RelatedSemanticType UsageNote: If the process is specific, for example to a site or substance, then 'Disease or Syndrome' will be assigned and not 'Pathologic Function'. For example, "cerebral anoxia", "brain edema", and "milk hypersensitivity" will all be assigned to 'Disease or Syndrome' only.\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 19\
  \
   RelationLabel Abbreviation: DI\
   RelationLabel Definition: Distinguishes or identifies the nature or characteristics of.\
   RelationLabel InverseLabel: diagnosed\_by\
   RelationLabel Tree Number: R5.6\
   RelationLabel Ui: T163\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: patf\
   RelatedSemanticType Definition: A disordered process, activity, or state of the organism as a whole, of a body system or systems, or of multiple organs or tissues. Included here are normal responses to a negative stimulus as well as patholologic conditions or states that are less specific than a disease. Pathologic functions frequently have systemic effects.\
   RelatedSemanticType Tree Number: B2.2.1.2\
   RelatedSemanticType Ui: T046\
   RelatedSemanticType Value: Pathologic Function\
   RelatedSemanticType UsageNote: If the process is specific, for example to a site or substance, then 'Disease or Syndrome' will be assigned and not 'Pathologic Function'. For example, "cerebral anoxia", "brain edema", and "milk hypersensitivity" will all be assigned to 'Disease or Syndrome' only.\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 19\
  \
   RelationLabel Abbreviation: LO\
   RelationLabel Definition: The position, site, or region of an entity or the site of a process.\
   RelationLabel InverseLabel: has\_location\
   RelationLabel Tree Number: R2.1\
   RelationLabel Ui: T135\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: patf\
   RelatedSemanticType Definition: A disordered process, activity, or state of the organism as a whole, of a body system or systems, or of multiple organs or tissues. Included here are normal responses to a negative stimulus as well as patholologic conditions or states that are less specific than a disease. Pathologic functions frequently have systemic effects.\
   RelatedSemanticType Tree Number: B2.2.1.2\
   RelatedSemanticType Ui: T046\
   RelatedSemanticType Value: Pathologic Function\
   RelatedSemanticType UsageNote: If the process is specific, for example to a site or substance, then 'Disease or Syndrome' will be assigned and not 'Pathologic Function'. For example, "cerebral anoxia", "brain edema", and "milk hypersensitivity" will all be assigned to 'Disease or Syndrome' only.\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 19\
  \
   RelationLabel Abbreviation: CA\
   RelationLabel Definition: Brings about a condition or an effect. Implied here is that an agent, such as for example, a pharmacologic substance or an organism, has brought about the effect. This includes induces, effects, evokes, and etiology.\
   RelationLabel InverseLabel: caused\_by\
   RelationLabel Tree Number: R3.2.2\
   RelationLabel Ui: T147\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: patf\
   RelatedSemanticType Definition: A disordered process, activity, or state of the organism as a whole, of a body system or systems, or of multiple organs or tissues. Included here are normal responses to a negative stimulus as well as patholologic conditions or states that are less specific than a disease. Pathologic functions frequently have systemic effects.\
   RelatedSemanticType Tree Number: B2.2.1.2\
   RelatedSemanticType Ui: T046\
   RelatedSemanticType Value: Pathologic Function\
   RelatedSemanticType UsageNote: If the process is specific, for example to a site or substance, then 'Disease or Syndrome' will be assigned and not 'Pathologic Function'. For example, "cerebral anoxia", "brain edema", and "milk hypersensitivity" will all be assigned to 'Disease or Syndrome' only.\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 19\
  \
   RelationLabel Abbreviation: CA\
   RelationLabel Definition: Brings about a condition or an effect. Implied here is that an agent, such as for example, a pharmacologic substance or an organism, has brought about the effect. This includes induces, effects, evokes, and etiology.\
   RelationLabel InverseLabel: caused\_by\
   RelationLabel Tree Number: R3.2.2\
   RelationLabel Ui: T147\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: patf\
   RelatedSemanticType Definition: A disordered process, activity, or state of the organism as a whole, of a body system or systems, or of multiple organs or tissues. Included here are normal responses to a negative stimulus as well as patholologic conditions or states that are less specific than a disease. Pathologic functions frequently have systemic effects.\
   RelatedSemanticType Tree Number: B2.2.1.2\
   RelatedSemanticType Ui: T046\
   RelatedSemanticType Value: Pathologic Function\
   RelatedSemanticType UsageNote: If the process is specific, for example to a site or substance, then 'Disease or Syndrome' will be assigned and not 'Pathologic Function'. For example, "cerebral anoxia", "brain edema", and "milk hypersensitivity" will all be assigned to 'Disease or Syndrome' only.\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 19\
  \
   RelationLabel Abbreviation: CA\
   RelationLabel Definition: Brings about a condition or an effect. Implied here is that an agent, such as for example, a pharmacologic substance or an organism, has brought about the effect. This includes induces, effects, evokes, and etiology.\
   RelationLabel InverseLabel: caused\_by\
   RelationLabel Tree Number: R3.2.2\
   RelationLabel Ui: T147\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: patf\
   RelatedSemanticType Definition: A disordered process, activity, or state of the organism as a whole, of a body system or systems, or of multiple organs or tissues. Included here are normal responses to a negative stimulus as well as patholologic conditions or states that are less specific than a disease. Pathologic functions frequently have systemic effects.\
   RelatedSemanticType Tree Number: B2.2.1.2\
   RelatedSemanticType Ui: T046\
   RelatedSemanticType Value: Pathologic Function\
   RelatedSemanticType UsageNote: If the process is specific, for example to a site or substance, then 'Disease or Syndrome' will be assigned and not 'Pathologic Function'. For example, "cerebral anoxia", "brain edema", and "milk hypersensitivity" will all be assigned to 'Disease or Syndrome' only.\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 19\
  \
   RelationLabel Abbreviation: AW\
   RelationLabel Definition: has a significant or salient relationship to.\
   RelationLabel InverseLabel: associated\_with\
   RelationLabel Tree Number: R\
   RelationLabel Ui: T166\
   RelationLabel Child Count: 5\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: patf\
   RelatedSemanticType Definition: A disordered process, activity, or state of the organism as a whole, of a body system or systems, or of multiple organs or tissues. Included here are normal responses to a negative stimulus as well as patholologic conditions or states that are less specific than a disease. Pathologic functions frequently have systemic effects.\
   RelatedSemanticType Tree Number: B2.2.1.2\
   RelatedSemanticType Ui: T046\
   RelatedSemanticType Value: Pathologic Function\
   RelatedSemanticType UsageNote: If the process is specific, for example to a site or substance, then 'Disease or Syndrome' will be assigned and not 'Pathologic Function'. For example, "cerebral anoxia", "brain edema", and "milk hypersensitivity" will all be assigned to 'Disease or Syndrome' only.\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 19\
  \
   RelationLabel Abbreviation: CM\
   RelationLabel Definition: Causes to become more severe or complex or results in adverse effects.\
   RelationLabel InverseLabel: complicated\_by\
   RelationLabel Tree Number: R3.1.4\
   RelationLabel Ui: T149\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: patf\
   RelatedSemanticType Definition: A disordered process, activity, or state of the organism as a whole, of a body system or systems, or of multiple organs or tissues. Included here are normal responses to a negative stimulus as well as patholologic conditions or states that are less specific than a disease. Pathologic functions frequently have systemic effects.\
   RelatedSemanticType Tree Number: B2.2.1.2\
   RelatedSemanticType Ui: T046\
   RelatedSemanticType Value: Pathologic Function\
   RelatedSemanticType UsageNote: If the process is specific, for example to a site or substance, then 'Disease or Syndrome' will be assigned and not 'Pathologic Function'. For example, "cerebral anoxia", "brain edema", and "milk hypersensitivity" will all be assigned to 'Disease or Syndrome' only.\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 19\
  \
   RelationLabel Abbreviation: PC\
   RelationLabel Definition: Occurs earlier in time. This includes antedates, comes before, is in advance of, predates, and is prior to.\
   RelationLabel InverseLabel: follows\
   RelationLabel Tree Number: R4.2\
   RelationLabel Ui: T138\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: patf\
   RelatedSemanticType Definition: A disordered process, activity, or state of the organism as a whole, of a body system or systems, or of multiple organs or tissues. Included here are normal responses to a negative stimulus as well as patholologic conditions or states that are less specific than a disease. Pathologic functions frequently have systemic effects.\
   RelatedSemanticType Tree Number: B2.2.1.2\
   RelatedSemanticType Ui: T046\
   RelatedSemanticType Value: Pathologic Function\
   RelatedSemanticType UsageNote: If the process is specific, for example to a site or substance, then 'Disease or Syndrome' will be assigned and not 'Pathologic Function'. For example, "cerebral anoxia", "brain edema", and "milk hypersensitivity" will all be assigned to 'Disease or Syndrome' only.\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 19\
  \
   RelationLabel Abbreviation: MF\
   RelationLabel Definition: That part of a phenomenon which is directly observable or concretely or visibly expressed, or which gives evidence to the underlying process. This includes expression of, display of, and exhibition of.\
   RelationLabel InverseLabel: has\_manifestation\
   RelationLabel Tree Number: R3.6\
   RelationLabel Ui: T150\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: patf\
   RelatedSemanticType Definition: A disordered process, activity, or state of the organism as a whole, of a body system or systems, or of multiple organs or tissues. Included here are normal responses to a negative stimulus as well as patholologic conditions or states that are less specific than a disease. Pathologic functions frequently have systemic effects.\
   RelatedSemanticType Tree Number: B2.2.1.2\
   RelatedSemanticType Ui: T046\
   RelatedSemanticType Value: Pathologic Function\
   RelatedSemanticType UsageNote: If the process is specific, for example to a site or substance, then 'Disease or Syndrome' will be assigned and not 'Pathologic Function'. For example, "cerebral anoxia", "brain edema", and "milk hypersensitivity" will all be assigned to 'Disease or Syndrome' only.\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 19\
  \
   RelationLabel Abbreviation: DE\
   RelationLabel Definition: The relative intensity of a process or the relative intensity or amount of a quality or attribute.\
   RelationLabel InverseLabel: has\_degree\
   RelationLabel Tree Number: R5.2\
   RelationLabel Ui: T180\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: patf\
   RelatedSemanticType Definition: A disordered process, activity, or state of the organism as a whole, of a body system or systems, or of multiple organs or tissues. Included here are normal responses to a negative stimulus as well as patholologic conditions or states that are less specific than a disease. Pathologic functions frequently have systemic effects.\
   RelatedSemanticType Tree Number: B2.2.1.2\
   RelatedSemanticType Ui: T046\
   RelatedSemanticType Value: Pathologic Function\
   RelatedSemanticType UsageNote: If the process is specific, for example to a site or substance, then 'Disease or Syndrome' will be assigned and not 'Pathologic Function'. For example, "cerebral anoxia", "brain edema", and "milk hypersensitivity" will all be assigned to 'Disease or Syndrome' only.\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 19\
  \
   RelationLabel Abbreviation: CM\
   RelationLabel Definition: Causes to become more severe or complex or results in adverse effects.\
   RelationLabel InverseLabel: complicated\_by\
   RelationLabel Tree Number: R3.1.4\
   RelationLabel Ui: T149\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: patf\
   RelatedSemanticType Definition: A disordered process, activity, or state of the organism as a whole, of a body system or systems, or of multiple organs or tissues. Included here are normal responses to a negative stimulus as well as patholologic conditions or states that are less specific than a disease. Pathologic functions frequently have systemic effects.\
   RelatedSemanticType Tree Number: B2.2.1.2\
   RelatedSemanticType Ui: T046\
   RelatedSemanticType Value: Pathologic Function\
   RelatedSemanticType UsageNote: If the process is specific, for example to a site or substance, then 'Disease or Syndrome' will be assigned and not 'Pathologic Function'. For example, "cerebral anoxia", "brain edema", and "milk hypersensitivity" will all be assigned to 'Disease or Syndrome' only.\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 19\
  \
   RelationLabel Abbreviation: CW\
   RelationLabel Definition: Occurs at the same time as, together with, or jointly. This includes is co-incident with, is concurrent with, is contemporaneous with, accompanies, coexists with, and is concomitant with.\
   RelationLabel InverseLabel: co-occurs\_with\
   RelationLabel Tree Number: R4.1\
   RelationLabel Ui: T137\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: patf\
   RelatedSemanticType Definition: A disordered process, activity, or state of the organism as a whole, of a body system or systems, or of multiple organs or tissues. Included here are normal responses to a negative stimulus as well as patholologic conditions or states that are less specific than a disease. Pathologic functions frequently have systemic effects.\
   RelatedSemanticType Tree Number: B2.2.1.2\
   RelatedSemanticType Ui: T046\
   RelatedSemanticType Value: Pathologic Function\
   RelatedSemanticType UsageNote: If the process is specific, for example to a site or substance, then 'Disease or Syndrome' will be assigned and not 'Pathologic Function'. For example, "cerebral anoxia", "brain edema", and "milk hypersensitivity" will all be assigned to 'Disease or Syndrome' only.\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 19\
  \
   RelationLabel Abbreviation: AW\
   RelationLabel Definition: has a significant or salient relationship to.\
   RelationLabel InverseLabel: associated\_with\
   RelationLabel Tree Number: R\
   RelationLabel Ui: T166\
   RelationLabel Child Count: 5\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: patf\
   RelatedSemanticType Definition: A disordered process, activity, or state of the organism as a whole, of a body system or systems, or of multiple organs or tissues. Included here are normal responses to a negative stimulus as well as patholologic conditions or states that are less specific than a disease. Pathologic functions frequently have systemic effects.\
   RelatedSemanticType Tree Number: B2.2.1.2\
   RelatedSemanticType Ui: T046\
   RelatedSemanticType Value: Pathologic Function\
   RelatedSemanticType UsageNote: If the process is specific, for example to a site or substance, then 'Disease or Syndrome' will be assigned and not 'Pathologic Function'. For example, "cerebral anoxia", "brain edema", and "milk hypersensitivity" will all be assigned to 'Disease or Syndrome' only.\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 19\
  \
   RelationLabel Abbreviation: IS\
   RelationLabel Definition: The basic hierarchical link in the Network. If one item "isa" another item then the first item is more specific in meaning than the second item.\
   RelationLabel InverseLabel: inverse\_isa\
   RelationLabel Tree Number: H\
   RelationLabel Ui: T186\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: patf\
   RelatedSemanticType Definition: A disordered process, activity, or state of the organism as a whole, of a body system or systems, or of multiple organs or tissues. Included here are normal responses to a negative stimulus as well as patholologic conditions or states that are less specific than a disease. Pathologic functions frequently have systemic effects.\
   RelatedSemanticType Tree Number: B2.2.1.2\
   RelatedSemanticType Ui: T046\
   RelatedSemanticType Value: Pathologic Function\
   RelatedSemanticType UsageNote: If the process is specific, for example to a site or substance, then 'Disease or Syndrome' will be assigned and not 'Pathologic Function'. For example, "cerebral anoxia", "brain edema", and "milk hypersensitivity" will all be assigned to 'Disease or Syndrome' only.\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 19\
  \
   RelationLabel Abbreviation: IS\
   RelationLabel Definition: The basic hierarchical link in the Network. If one item "isa" another item then the first item is more specific in meaning than the second item.\
   RelationLabel InverseLabel: inverse\_isa\
   RelationLabel Tree Number: H\
   RelationLabel Ui: T186\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: patf\
   RelatedSemanticType Definition: A disordered process, activity, or state of the organism as a whole, of a body system or systems, or of multiple organs or tissues. Included here are normal responses to a negative stimulus as well as patholologic conditions or states that are less specific than a disease. Pathologic functions frequently have systemic effects.\
   RelatedSemanticType Tree Number: B2.2.1.2\
   RelatedSemanticType Ui: T046\
   RelatedSemanticType Value: Pathologic Function\
   RelatedSemanticType UsageNote: If the process is specific, for example to a site or substance, then 'Disease or Syndrome' will be assigned and not 'Pathologic Function'. For example, "cerebral anoxia", "brain edema", and "milk hypersensitivity" will all be assigned to 'Disease or Syndrome' only.\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 19\
  \
   RelationLabel Abbreviation: IS\
   RelationLabel Definition: The basic hierarchical link in the Network. If one item "isa" another item then the first item is more specific in meaning than the second item.\
   RelationLabel InverseLabel: inverse\_isa\
   RelationLabel Tree Number: H\
   RelationLabel Ui: T186\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: patf\
   RelatedSemanticType Definition: A disordered process, activity, or state of the organism as a whole, of a body system or systems, or of multiple organs or tissues. Included here are normal responses to a negative stimulus as well as patholologic conditions or states that are less specific than a disease. Pathologic functions frequently have systemic effects.\
   RelatedSemanticType Tree Number: B2.2.1.2\
   RelatedSemanticType Ui: T046\
   RelatedSemanticType Value: Pathologic Function\
   RelatedSemanticType UsageNote: If the process is specific, for example to a site or substance, then 'Disease or Syndrome' will be assigned and not 'Pathologic Function'. For example, "cerebral anoxia", "brain edema", and "milk hypersensitivity" will all be assigned to 'Disease or Syndrome' only.\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 19\
  \
   RelationLabel Abbreviation: AW\
   RelationLabel Definition: has a significant or salient relationship to.\
   RelationLabel InverseLabel: associated\_with\
   RelationLabel Tree Number: R\
   RelationLabel Ui: T166\
   RelationLabel Child Count: 5\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: patf\
   RelatedSemanticType Definition: A disordered process, activity, or state of the organism as a whole, of a body system or systems, or of multiple organs or tissues. Included here are normal responses to a negative stimulus as well as patholologic conditions or states that are less specific than a disease. Pathologic functions frequently have systemic effects.\
   RelatedSemanticType Tree Number: B2.2.1.2\
   RelatedSemanticType Ui: T046\
   RelatedSemanticType Value: Pathologic Function\
   RelatedSemanticType UsageNote: If the process is specific, for example to a site or substance, then 'Disease or Syndrome' will be assigned and not 'Pathologic Function'. For example, "cerebral anoxia", "brain edema", and "milk hypersensitivity" will all be assigned to 'Disease or Syndrome' only.\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 19\
  \
   RelationLabel Abbreviation: AW\
   RelationLabel Definition: has a significant or salient relationship to.\
   RelationLabel InverseLabel: associated\_with\
   RelationLabel Tree Number: R\
   RelationLabel Ui: T166\
   RelationLabel Child Count: 5\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: patf\
   RelatedSemanticType Definition: A disordered process, activity, or state of the organism as a whole, of a body system or systems, or of multiple organs or tissues. Included here are normal responses to a negative stimulus as well as patholologic conditions or states that are less specific than a disease. Pathologic functions frequently have systemic effects.\
   RelatedSemanticType Tree Number: B2.2.1.2\
   RelatedSemanticType Ui: T046\
   RelatedSemanticType Value: Pathologic Function\
   RelatedSemanticType UsageNote: If the process is specific, for example to a site or substance, then 'Disease or Syndrome' will be assigned and not 'Pathologic Function'. For example, "cerebral anoxia", "brain edema", and "milk hypersensitivity" will all be assigned to 'Disease or Syndrome' only.\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 19\
  \
   RelationLabel Abbreviation: AW\
   RelationLabel Definition: has a significant or salient relationship to.\
   RelationLabel InverseLabel: associated\_with\
   RelationLabel Tree Number: R\
   RelationLabel Ui: T166\
   RelationLabel Child Count: 5\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: patf\
   RelatedSemanticType Definition: A disordered process, activity, or state of the organism as a whole, of a body system or systems, or of multiple organs or tissues. Included here are normal responses to a negative stimulus as well as patholologic conditions or states that are less specific than a disease. Pathologic functions frequently have systemic effects.\
   RelatedSemanticType Tree Number: B2.2.1.2\
   RelatedSemanticType Ui: T046\
   RelatedSemanticType Value: Pathologic Function\
   RelatedSemanticType UsageNote: If the process is specific, for example to a site or substance, then 'Disease or Syndrome' will be assigned and not 'Pathologic Function'. For example, "cerebral anoxia", "brain edema", and "milk hypersensitivity" will all be assigned to 'Disease or Syndrome' only.\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 19\
  \
   RelationLabel Abbreviation: DI\
   RelationLabel Definition: Distinguishes or identifies the nature or characteristics of.\
   RelationLabel InverseLabel: diagnosed\_by\
   RelationLabel Tree Number: R5.6\
   RelationLabel Ui: T163\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: patf\
   RelatedSemanticType Definition: A disordered process, activity, or state of the organism as a whole, of a body system or systems, or of multiple organs or tissues. Included here are normal responses to a negative stimulus as well as patholologic conditions or states that are less specific than a disease. Pathologic functions frequently have systemic effects.\
   RelatedSemanticType Tree Number: B2.2.1.2\
   RelatedSemanticType Ui: T046\
   RelatedSemanticType Value: Pathologic Function\
   RelatedSemanticType UsageNote: If the process is specific, for example to a site or substance, then 'Disease or Syndrome' will be assigned and not 'Pathologic Function'. For example, "cerebral anoxia", "brain edema", and "milk hypersensitivity" will all be assigned to 'Disease or Syndrome' only.\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 19\
  \
   RelationLabel Abbreviation: DI\
   RelationLabel Definition: Distinguishes or identifies the nature or characteristics of.\
   RelationLabel InverseLabel: diagnosed\_by\
   RelationLabel Tree Number: R5.6\
   RelationLabel Ui: T163\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: patf\
   RelatedSemanticType Definition: A disordered process, activity, or state of the organism as a whole, of a body system or systems, or of multiple organs or tissues. Included here are normal responses to a negative stimulus as well as patholologic conditions or states that are less specific than a disease. Pathologic functions frequently have systemic effects.\
   RelatedSemanticType Tree Number: B2.2.1.2\
   RelatedSemanticType Ui: T046\
   RelatedSemanticType Value: Pathologic Function\
   RelatedSemanticType UsageNote: If the process is specific, for example to a site or substance, then 'Disease or Syndrome' will be assigned and not 'Pathologic Function'. For example, "cerebral anoxia", "brain edema", and "milk hypersensitivity" will all be assigned to 'Disease or Syndrome' only.\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 19\
  \
   RelationLabel Abbreviation: TS\
   RelationLabel Definition: Applies a remedy with the object of effecting a cure or managing a condition.\
   RelationLabel InverseLabel: treated\_by\
   RelationLabel Tree Number: R3.1.2\
   RelationLabel Ui: T154\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: patf\
   RelatedSemanticType Definition: A disordered process, activity, or state of the organism as a whole, of a body system or systems, or of multiple organs or tissues. Included here are normal responses to a negative stimulus as well as patholologic conditions or states that are less specific than a disease. Pathologic functions frequently have systemic effects.\
   RelatedSemanticType Tree Number: B2.2.1.2\
   RelatedSemanticType Ui: T046\
   RelatedSemanticType Value: Pathologic Function\
   RelatedSemanticType UsageNote: If the process is specific, for example to a site or substance, then 'Disease or Syndrome' will be assigned and not 'Pathologic Function'. For example, "cerebral anoxia", "brain edema", and "milk hypersensitivity" will all be assigned to 'Disease or Syndrome' only.\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 19\
  \
   RelationLabel Abbreviation: PV\
   RelationLabel Definition: Stops, hinders or eliminates an action or condition.\
   RelationLabel InverseLabel: prevented\_by\
   RelationLabel Tree Number: R3.1.6\
   RelationLabel Ui: T148\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: patf\
   RelatedSemanticType Definition: A disordered process, activity, or state of the organism as a whole, of a body system or systems, or of multiple organs or tissues. Included here are normal responses to a negative stimulus as well as patholologic conditions or states that are less specific than a disease. Pathologic functions frequently have systemic effects.\
   RelatedSemanticType Tree Number: B2.2.1.2\
   RelatedSemanticType Ui: T046\
   RelatedSemanticType Value: Pathologic Function\
   RelatedSemanticType UsageNote: If the process is specific, for example to a site or substance, then 'Disease or Syndrome' will be assigned and not 'Pathologic Function'. For example, "cerebral anoxia", "brain edema", and "milk hypersensitivity" will all be assigned to 'Disease or Syndrome' only.\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 19\
  \
   RelationLabel Abbreviation: CA\
   RelationLabel Definition: Brings about a condition or an effect. Implied here is that an agent, such as for example, a pharmacologic substance or an organism, has brought about the effect. This includes induces, effects, evokes, and etiology.\
   RelationLabel InverseLabel: caused\_by\
   RelationLabel Tree Number: R3.2.2\
   RelationLabel Ui: T147\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: patf\
   RelatedSemanticType Definition: A disordered process, activity, or state of the organism as a whole, of a body system or systems, or of multiple organs or tissues. Included here are normal responses to a negative stimulus as well as patholologic conditions or states that are less specific than a disease. Pathologic functions frequently have systemic effects.\
   RelatedSemanticType Tree Number: B2.2.1.2\
   RelatedSemanticType Ui: T046\
   RelatedSemanticType Value: Pathologic Function\
   RelatedSemanticType UsageNote: If the process is specific, for example to a site or substance, then 'Disease or Syndrome' will be assigned and not 'Pathologic Function'. For example, "cerebral anoxia", "brain edema", and "milk hypersensitivity" will all be assigned to 'Disease or Syndrome' only.\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 19\
  \
   RelationLabel Abbreviation: TS\
   RelationLabel Definition: Applies a remedy with the object of effecting a cure or managing a condition.\
   RelationLabel InverseLabel: treated\_by\
   RelationLabel Tree Number: R3.1.2\
   RelationLabel Ui: T154\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: patf\
   RelatedSemanticType Definition: A disordered process, activity, or state of the organism as a whole, of a body system or systems, or of multiple organs or tissues. Included here are normal responses to a negative stimulus as well as patholologic conditions or states that are less specific than a disease. Pathologic functions frequently have systemic effects.\
   RelatedSemanticType Tree Number: B2.2.1.2\
   RelatedSemanticType Ui: T046\
   RelatedSemanticType Value: Pathologic Function\
   RelatedSemanticType UsageNote: If the process is specific, for example to a site or substance, then 'Disease or Syndrome' will be assigned and not 'Pathologic Function'. For example, "cerebral anoxia", "brain edema", and "milk hypersensitivity" will all be assigned to 'Disease or Syndrome' only.\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 19\
  \
   RelationLabel Abbreviation: PV\
   RelationLabel Definition: Stops, hinders or eliminates an action or condition.\
   RelationLabel InverseLabel: prevented\_by\
   RelationLabel Tree Number: R3.1.6\
   RelationLabel Ui: T148\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: patf\
   RelatedSemanticType Definition: A disordered process, activity, or state of the organism as a whole, of a body system or systems, or of multiple organs or tissues. Included here are normal responses to a negative stimulus as well as patholologic conditions or states that are less specific than a disease. Pathologic functions frequently have systemic effects.\
   RelatedSemanticType Tree Number: B2.2.1.2\
   RelatedSemanticType Ui: T046\
   RelatedSemanticType Value: Pathologic Function\
   RelatedSemanticType UsageNote: If the process is specific, for example to a site or substance, then 'Disease or Syndrome' will be assigned and not 'Pathologic Function'. For example, "cerebral anoxia", "brain edema", and "milk hypersensitivity" will all be assigned to 'Disease or Syndrome' only.\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 19\
  \
   RelationLabel Abbreviation: AW\
   RelationLabel Definition: has a significant or salient relationship to.\
   RelationLabel InverseLabel: associated\_with\
   RelationLabel Tree Number: R\
   RelationLabel Ui: T166\
   RelationLabel Child Count: 5\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: patf\
   RelatedSemanticType Definition: A disordered process, activity, or state of the organism as a whole, of a body system or systems, or of multiple organs or tissues. Included here are normal responses to a negative stimulus as well as patholologic conditions or states that are less specific than a disease. Pathologic functions frequently have systemic effects.\
   RelatedSemanticType Tree Number: B2.2.1.2\
   RelatedSemanticType Ui: T046\
   RelatedSemanticType Value: Pathologic Function\
   RelatedSemanticType UsageNote: If the process is specific, for example to a site or substance, then 'Disease or Syndrome' will be assigned and not 'Pathologic Function'. For example, "cerebral anoxia", "brain edema", and "milk hypersensitivity" will all be assigned to 'Disease or Syndrome' only.\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 19\
  \
   RelationLabel Abbreviation: DI\
   RelationLabel Definition: Distinguishes or identifies the nature or characteristics of.\
   RelationLabel InverseLabel: diagnosed\_by\
   RelationLabel Tree Number: R5.6\
   RelationLabel Ui: T163\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: patf\
   RelatedSemanticType Definition: A disordered process, activity, or state of the organism as a whole, of a body system or systems, or of multiple organs or tissues. Included here are normal responses to a negative stimulus as well as patholologic conditions or states that are less specific than a disease. Pathologic functions frequently have systemic effects.\
   RelatedSemanticType Tree Number: B2.2.1.2\
   RelatedSemanticType Ui: T046\
   RelatedSemanticType Value: Pathologic Function\
   RelatedSemanticType UsageNote: If the process is specific, for example to a site or substance, then 'Disease or Syndrome' will be assigned and not 'Pathologic Function'. For example, "cerebral anoxia", "brain edema", and "milk hypersensitivity" will all be assigned to 'Disease or Syndrome' only.\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 19\
  \
   RelationLabel Abbreviation: AW\
   RelationLabel Definition: has a significant or salient relationship to.\
   RelationLabel InverseLabel: associated\_with\
   RelationLabel Tree Number: R\
   RelationLabel Ui: T166\
   RelationLabel Child Count: 5\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: patf\
   RelatedSemanticType Definition: A disordered process, activity, or state of the organism as a whole, of a body system or systems, or of multiple organs or tissues. Included here are normal responses to a negative stimulus as well as patholologic conditions or states that are less specific than a disease. Pathologic functions frequently have systemic effects.\
   RelatedSemanticType Tree Number: B2.2.1.2\
   RelatedSemanticType Ui: T046\
   RelatedSemanticType Value: Pathologic Function\
   RelatedSemanticType UsageNote: If the process is specific, for example to a site or substance, then 'Disease or Syndrome' will be assigned and not 'Pathologic Function'. For example, "cerebral anoxia", "brain edema", and "milk hypersensitivity" will all be assigned to 'Disease or Syndrome' only.\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 19\
  \
   RelationLabel Abbreviation: TS\
   RelationLabel Definition: Applies a remedy with the object of effecting a cure or managing a condition.\
   RelationLabel InverseLabel: treated\_by\
   RelationLabel Tree Number: R3.1.2\
   RelationLabel Ui: T154\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: patf\
   RelatedSemanticType Definition: A disordered process, activity, or state of the organism as a whole, of a body system or systems, or of multiple organs or tissues. Included here are normal responses to a negative stimulus as well as patholologic conditions or states that are less specific than a disease. Pathologic functions frequently have systemic effects.\
   RelatedSemanticType Tree Number: B2.2.1.2\
   RelatedSemanticType Ui: T046\
   RelatedSemanticType Value: Pathologic Function\
   RelatedSemanticType UsageNote: If the process is specific, for example to a site or substance, then 'Disease or Syndrome' will be assigned and not 'Pathologic Function'. For example, "cerebral anoxia", "brain edema", and "milk hypersensitivity" will all be assigned to 'Disease or Syndrome' only.\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 19\
  \
   RelationLabel Abbreviation: PV\
   RelationLabel Definition: Stops, hinders or eliminates an action or condition.\
   RelationLabel InverseLabel: prevented\_by\
   RelationLabel Tree Number: R3.1.6\
   RelationLabel Ui: T148\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: patf\
   RelatedSemanticType Definition: A disordered process, activity, or state of the organism as a whole, of a body system or systems, or of multiple organs or tissues. Included here are normal responses to a negative stimulus as well as patholologic conditions or states that are less specific than a disease. Pathologic functions frequently have systemic effects.\
   RelatedSemanticType Tree Number: B2.2.1.2\
   RelatedSemanticType Ui: T046\
   RelatedSemanticType Value: Pathologic Function\
   RelatedSemanticType UsageNote: If the process is specific, for example to a site or substance, then 'Disease or Syndrome' will be assigned and not 'Pathologic Function'. For example, "cerebral anoxia", "brain edema", and "milk hypersensitivity" will all be assigned to 'Disease or Syndrome' only.\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 19\
  \
   RelationLabel Abbreviation: DI\
   RelationLabel Definition: Distinguishes or identifies the nature or characteristics of.\
   RelationLabel InverseLabel: diagnosed\_by\
   RelationLabel Tree Number: R5.6\
   RelationLabel Ui: T163\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: patf\
   RelatedSemanticType Definition: A disordered process, activity, or state of the organism as a whole, of a body system or systems, or of multiple organs or tissues. Included here are normal responses to a negative stimulus as well as patholologic conditions or states that are less specific than a disease. Pathologic functions frequently have systemic effects.\
   RelatedSemanticType Tree Number: B2.2.1.2\
   RelatedSemanticType Ui: T046\
   RelatedSemanticType Value: Pathologic Function\
   RelatedSemanticType UsageNote: If the process is specific, for example to a site or substance, then 'Disease or Syndrome' will be assigned and not 'Pathologic Function'. For example, "cerebral anoxia", "brain edema", and "milk hypersensitivity" will all be assigned to 'Disease or Syndrome' only.\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 19\
  \
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

</div>

<div id="getInheritedSemanticTypeRelations"
class="method rounded-content-block">

**Method: **<span
class="method-name">getInheritedSemanticTypeRelations</span><span
class="method-parameters">(String ticket,String version,String
semanticTypeId)</span>
**Returns:** <span
class="method-return-type">ArrayList&lt;SemanticTypeRelationDTO&gt; </span>

<div class="method-description">

**Use Case:** A relation between two semantic types often holds true for
the relation between the children of those two semantic types. Given a
UMLS release and a semantic type unique identifier (TUI), this call
returns the semantic type relations inherited by the given TUI.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

myarrSemTyRelDTO =
utsSemanticNetworkService.getInheritedSemanticTypeRelations (ticket,
umlsRelease, "T037");\
\
 for (int i = 0; i &lt; myarrSemTyRelDTO.size(); i++) {\
 SemanticTypeRelationDTO mySemTyRel = myarrSemTyRelDTO.get(i);\
 String relAbbr = mySemTyRel.getRelationLabel().getAbbreviation();\
 String relDef = mySemTyRel.getRelationLabel().getDefinition();\
 String relInvLabel = mySemTyRel.getRelationLabel().getInverseLabel();\
 String relTreeNum = mySemTyRel.getRelationLabel().getTreeNumber();\
 String relUi = mySemTyRel.getRelationLabel().getUi();\
 int relChildCnt = mySemTyRel.getRelationLabel().getChildCount();\
 int relRelCnt = mySemTyRel.getRelationLabel().getRelationCount();\
\
 String SemTypeAbbr =
mySemTyRel.getRelatedSemanticType().getAbbreviation();\
 String SemTypeDef =
mySemTyRel.getRelatedSemanticType().getDefinition();\
 String SemTypeTreeNum =
mySemTyRel.getRelatedSemanticType().getTreeNumber();\
 String SemTypeUi = mySemTyRel.getRelatedSemanticType().getUi();\
 String SemTypeVal = mySemTyRel.getRelatedSemanticType().getValue();\
 String SemTypeUsage =
mySemTyRel.getRelatedSemanticType().getUsageNote();\
 int SemTypeChildCnt =
mySemTyRel.getRelatedSemanticType().getChildCount();\
 int SemTypeRelCnt =
mySemTyRel.getRelatedSemanticType().getRelationCount();\
 }\

</div>

#### Sample Output:

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  RelationLabel Abbreviation: AW\
   RelationLabel Definition: has a significant or salient relationship to.\
   RelationLabel InverseLabel: associated\_with\
   RelationLabel Tree Number: R\
   RelationLabel Ui: T166\
   RelationLabel Child Count: 5\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: sosy\
   RelatedSemanticType Definition: An observable manifestation of a disease or condition based on clinical judgment, or a manifestation of a disease or condition which is experienced by the patient and reported as a subjective observation.\
   RelatedSemanticType Tree Number: A2.2.2\
   RelatedSemanticType Ui: T184\
   RelatedSemanticType Value: Sign or Symptom\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 5\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: anab\
   RelatedSemanticType Definition: An abnormal structure, or one that is abnormal in size or location.\
   RelatedSemanticType Tree Number: A1.2.2\
   RelatedSemanticType Ui: T190\
   RelatedSemanticType Value: Anatomical Abnormality\
   RelatedSemanticType UsageNote: Use this type if the abnormality in question can be either an acquired or congenital abnormality. Neoplasms are not included here. These are given the type 'Neoplastic Process'. If an anatomical abnormality has a pathologic manifestation, then it will additionally be given the type 'Disease or Syndrome', e.g., "Diabetic Cataract" will be double-typed for this reason.\
   RelatedSemanticType Child Count: 2\
   RelatedSemanticType Relation Count: 12\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: neop\
   RelatedSemanticType Definition: A new and abnormal growth of tissue in which the growth is uncontrolled and progressive. The growths may be malignant or benign.\
   RelatedSemanticType Tree Number: B2.2.1.2.1.2\
   RelatedSemanticType Ui: T191\
   RelatedSemanticType Value: Neoplastic Process\
   RelatedSemanticType UsageNote: All neoplasms are assigned to this type. Do not also assign a type from the 'Anatomical Abnormality' hierarchy.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 1\
  \
   RelationLabel Abbreviation: CM\
   RelationLabel Definition: Causes to become more severe or complex or results in adverse effects.\
   RelationLabel InverseLabel: complicated\_by\
   RelationLabel Tree Number: R3.1.4\
   RelationLabel Ui: T149\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: neop\
   RelatedSemanticType Definition: A new and abnormal growth of tissue in which the growth is uncontrolled and progressive. The growths may be malignant or benign.\
   RelatedSemanticType Tree Number: B2.2.1.2.1.2\
   RelatedSemanticType Ui: T191\
   RelatedSemanticType Value: Neoplastic Process\
   RelatedSemanticType UsageNote: All neoplasms are assigned to this type. Do not also assign a type from the 'Anatomical Abnormality' hierarchy.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 1\
  \
   RelationLabel Abbreviation: CW\
   RelationLabel Definition: Occurs at the same time as, together with, or jointly. This includes is co-incident with, is concurrent with, is contemporaneous with, accompanies, coexists with, and is concomitant with.\
   RelationLabel InverseLabel: co-occurs\_with\
   RelationLabel Tree Number: R4.1\
   RelationLabel Ui: T137\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: neop\
   RelatedSemanticType Definition: A new and abnormal growth of tissue in which the growth is uncontrolled and progressive. The growths may be malignant or benign.\
   RelatedSemanticType Tree Number: B2.2.1.2.1.2\
   RelatedSemanticType Ui: T191\
   RelatedSemanticType Value: Neoplastic Process\
   RelatedSemanticType UsageNote: All neoplasms are assigned to this type. Do not also assign a type from the 'Anatomical Abnormality' hierarchy.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 1\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: cgab\
   RelatedSemanticType Definition: An abnormal structure, or one that is abnormal in size or location, present at birth or evolving over time as a result of a defect in embryogenesis.\
   RelatedSemanticType Tree Number: A1.2.2.1\
   RelatedSemanticType Ui: T019\
   RelatedSemanticType Value: Congenital Abnormality\
   RelatedSemanticType UsageNote: If the congenital abnormality involves multiple defects then the type 'Disease or Syndrome' will also be assigned.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 1\
  \
   RelationLabel Abbreviation: CM\
   RelationLabel Definition: Causes to become more severe or complex or results in adverse effects.\
   RelationLabel InverseLabel: complicated\_by\
   RelationLabel Tree Number: R3.1.4\
   RelationLabel Ui: T149\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: cgab\
   RelatedSemanticType Definition: An abnormal structure, or one that is abnormal in size or location, present at birth or evolving over time as a result of a defect in embryogenesis.\
   RelatedSemanticType Tree Number: A1.2.2.1\
   RelatedSemanticType Ui: T019\
   RelatedSemanticType Value: Congenital Abnormality\
   RelatedSemanticType UsageNote: If the congenital abnormality involves multiple defects then the type 'Disease or Syndrome' will also be assigned.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 1\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: acab\
   RelatedSemanticType Definition: An abnormal structure, or one that is abnormal in size or location, found in or deriving from a previously normal structure. Acquired abnormalities are distinguished from diseases even though they may result in pathological functioning (e.g., "hernias incarcerate").\
   RelatedSemanticType Tree Number: A1.2.2.2\
   RelatedSemanticType Ui: T020\
   RelatedSemanticType Value: Acquired Abnormality\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 3\
  \
   RelationLabel Abbreviation: CM\
   RelationLabel Definition: Causes to become more severe or complex or results in adverse effects.\
   RelationLabel InverseLabel: complicated\_by\
   RelationLabel Tree Number: R3.1.4\
   RelationLabel Ui: T149\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: acab\
   RelatedSemanticType Definition: An abnormal structure, or one that is abnormal in size or location, found in or deriving from a previously normal structure. Acquired abnormalities are distinguished from diseases even though they may result in pathological functioning (e.g., "hernias incarcerate").\
   RelatedSemanticType Tree Number: A1.2.2.2\
   RelatedSemanticType Ui: T020\
   RelatedSemanticType Value: Acquired Abnormality\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 3\
  \
   RelationLabel Abbreviation: DS\
   RelationLabel Definition: Alters or influences an already existing condition, state, or situation. Produces a negative effect on.\
   RelationLabel InverseLabel: disrupted\_by\
   RelationLabel Tree Number: R3.1.3\
   RelationLabel Ui: T146\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: bpoc\
   RelatedSemanticType Definition: A collection of cells and tissues which are localized to a specific area or combine and carry out one or more specialized functions of an organism. This ranges from gross structures to small components of complex organs. These structures are relatively localized in comparison to tissues.\
   RelatedSemanticType Tree Number: A1.2.3.1\
   RelatedSemanticType Ui: T023\
   RelatedSemanticType Value: Body Part, Organ, or Organ Component\
   RelatedSemanticType UsageNote: When assigning this type, consider whether 'Body Location or Region' might be the correct choice.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 24\
  \
   RelationLabel Abbreviation: DS\
   RelationLabel Definition: Alters or influences an already existing condition, state, or situation. Produces a negative effect on.\
   RelationLabel InverseLabel: disrupted\_by\
   RelationLabel Tree Number: R3.1.3\
   RelationLabel Ui: T146\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: tisu\
   RelatedSemanticType Definition: An aggregation of similarly specialized cells and the associated intercellular substance. Tissues are relatively non-localized in comparison to body parts, organs or organ components.\
   RelatedSemanticType Tree Number: A1.2.3.2\
   RelatedSemanticType Ui: T024\
   RelatedSemanticType Value: Tissue\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 17\
  \
   RelationLabel Abbreviation: DS\
   RelationLabel Definition: Alters or influences an already existing condition, state, or situation. Produces a negative effect on.\
   RelationLabel InverseLabel: disrupted\_by\
   RelationLabel Tree Number: R3.1.3\
   RelationLabel Ui: T146\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: cell\
   RelatedSemanticType Definition: The fundamental structural and functional unit of living organisms.\
   RelatedSemanticType Tree Number: A1.2.3.3\
   RelatedSemanticType Ui: T025\
   RelatedSemanticType Value: Cell\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: DS\
   RelationLabel Definition: Alters or influences an already existing condition, state, or situation. Produces a negative effect on.\
   RelationLabel InverseLabel: disrupted\_by\
   RelationLabel Tree Number: R3.1.3\
   RelationLabel Ui: T146\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: celc\
   RelatedSemanticType Definition: A part of a cell or the intercellular matrix, generally visible by light microscopy.\
   RelatedSemanticType Tree Number: A1.2.3.4\
   RelatedSemanticType Ui: T026\
   RelatedSemanticType Value: Cell Component\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 13\
  \
   RelationLabel Abbreviation: DS\
   RelationLabel Definition: Alters or influences an already existing condition, state, or situation. Produces a negative effect on.\
   RelationLabel InverseLabel: disrupted\_by\
   RelationLabel Tree Number: R3.1.3\
   RelationLabel Ui: T146\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: gngm\
   RelatedSemanticType Definition: A specific sequence, or in the case of the genome the complete sequence, of nucleotides along a molecule of DNA or RNA (in the case of some viruses) which represent the functional units of heredity.\
   RelatedSemanticType Tree Number: A1.2.3.5\
   RelatedSemanticType Ui: T028\
   RelatedSemanticType Value: Gene or Genome\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 8\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: biof\
   RelatedSemanticType Definition: A state, activity or process of the body or one of its systems or parts.\
   RelatedSemanticType Tree Number: B2.2.1\
   RelatedSemanticType Ui: T038\
   RelatedSemanticType Value: Biologic Function\
   RelatedSemanticType UsageNote: Few concepts will be assigned to this broad type.\
   RelatedSemanticType Child Count: 2\
   RelatedSemanticType Relation Count: 5\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: phsf\
   RelatedSemanticType Definition: A normal process, activity, or state of the body.\
   RelatedSemanticType Tree Number: B2.2.1.1\
   RelatedSemanticType Ui: T039\
   RelatedSemanticType Value: Physiologic Function\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 4\
   RelatedSemanticType Relation Count: 5\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: orgf\
   RelatedSemanticType Definition: A physiologic function of the organism as a whole, of multiple organ systems, or of multiple organs or tissues.\
   RelatedSemanticType Tree Number: B2.2.1.1.1\
   RelatedSemanticType Ui: T040\
   RelatedSemanticType Value: Organism Function\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 1\
   RelatedSemanticType Relation Count: 5\
  \
   RelationLabel Abbreviation: DS\
   RelationLabel Definition: Alters or influences an already existing condition, state, or situation. Produces a negative effect on.\
   RelationLabel InverseLabel: disrupted\_by\
   RelationLabel Tree Number: R3.1.3\
   RelationLabel Ui: T146\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: orgf\
   RelatedSemanticType Definition: A physiologic function of the organism as a whole, of multiple organ systems, or of multiple organs or tissues.\
   RelatedSemanticType Tree Number: B2.2.1.1.1\
   RelatedSemanticType Ui: T040\
   RelatedSemanticType Value: Organism Function\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 1\
   RelatedSemanticType Relation Count: 5\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: menp\
   RelatedSemanticType Definition: A physiologic function involving the mind or cognitive processing.\
   RelatedSemanticType Tree Number: B2.2.1.1.1.1\
   RelatedSemanticType Ui: T041\
   RelatedSemanticType Value: Mental Process\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 7\
  \
   RelationLabel Abbreviation: DS\
   RelationLabel Definition: Alters or influences an already existing condition, state, or situation. Produces a negative effect on.\
   RelationLabel InverseLabel: disrupted\_by\
   RelationLabel Tree Number: R3.1.3\
   RelationLabel Ui: T146\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: menp\
   RelatedSemanticType Definition: A physiologic function involving the mind or cognitive processing.\
   RelatedSemanticType Tree Number: B2.2.1.1.1.1\
   RelatedSemanticType Ui: T041\
   RelatedSemanticType Value: Mental Process\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 7\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: ortf\
   RelatedSemanticType Definition: A physiologic function of a particular organ, organ system, or tissue.\
   RelatedSemanticType Tree Number: B2.2.1.1.2\
   RelatedSemanticType Ui: T042\
   RelatedSemanticType Value: Organ or Tissue Function\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 4\
  \
   RelationLabel Abbreviation: DS\
   RelationLabel Definition: Alters or influences an already existing condition, state, or situation. Produces a negative effect on.\
   RelationLabel InverseLabel: disrupted\_by\
   RelationLabel Tree Number: R3.1.3\
   RelationLabel Ui: T146\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: ortf\
   RelatedSemanticType Definition: A physiologic function of a particular organ, organ system, or tissue.\
   RelatedSemanticType Tree Number: B2.2.1.1.2\
   RelatedSemanticType Ui: T042\
   RelatedSemanticType Value: Organ or Tissue Function\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 4\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: celf\
   RelatedSemanticType Definition: A physiologic function inherent to cells or cell components.\
   RelatedSemanticType Tree Number: B2.2.1.1.3\
   RelatedSemanticType Ui: T043\
   RelatedSemanticType Value: Cell Function\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 1\
  \
   RelationLabel Abbreviation: DS\
   RelationLabel Definition: Alters or influences an already existing condition, state, or situation. Produces a negative effect on.\
   RelationLabel InverseLabel: disrupted\_by\
   RelationLabel Tree Number: R3.1.3\
   RelationLabel Ui: T146\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: celf\
   RelatedSemanticType Definition: A physiologic function inherent to cells or cell components.\
   RelatedSemanticType Tree Number: B2.2.1.1.3\
   RelatedSemanticType Ui: T043\
   RelatedSemanticType Value: Cell Function\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 1\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: moft\
   RelatedSemanticType Definition: A physiologic function occurring at the molecular level.\
   RelatedSemanticType Tree Number: B2.2.1.1.4\
   RelatedSemanticType Ui: T044\
   RelatedSemanticType Value: Molecular Function\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 1\
   RelatedSemanticType Relation Count: 1\
  \
   RelationLabel Abbreviation: DS\
   RelationLabel Definition: Alters or influences an already existing condition, state, or situation. Produces a negative effect on.\
   RelationLabel InverseLabel: disrupted\_by\
   RelationLabel Tree Number: R3.1.3\
   RelationLabel Ui: T146\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: moft\
   RelatedSemanticType Definition: A physiologic function occurring at the molecular level.\
   RelatedSemanticType Tree Number: B2.2.1.1.4\
   RelatedSemanticType Ui: T044\
   RelatedSemanticType Value: Molecular Function\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 1\
   RelatedSemanticType Relation Count: 1\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: genf\
   RelatedSemanticType Definition: Functions of or related to the maintenance, translation or expression of the genetic material.\
   RelatedSemanticType Tree Number: B2.2.1.1.4.1\
   RelatedSemanticType Ui: T045\
   RelatedSemanticType Value: Genetic Function\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 2\
  \
   RelationLabel Abbreviation: DS\
   RelationLabel Definition: Alters or influences an already existing condition, state, or situation. Produces a negative effect on.\
   RelationLabel InverseLabel: disrupted\_by\
   RelationLabel Tree Number: R3.1.3\
   RelationLabel Ui: T146\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: genf\
   RelatedSemanticType Definition: Functions of or related to the maintenance, translation or expression of the genetic material.\
   RelatedSemanticType Tree Number: B2.2.1.1.4.1\
   RelatedSemanticType Ui: T045\
   RelatedSemanticType Value: Genetic Function\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 2\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: patf\
   RelatedSemanticType Definition: A disordered process, activity, or state of the organism as a whole, of a body system or systems, or of multiple organs or tissues. Included here are normal responses to a negative stimulus as well as patholologic conditions or states that are less specific than a disease. Pathologic functions frequently have systemic effects.\
   RelatedSemanticType Tree Number: B2.2.1.2\
   RelatedSemanticType Ui: T046\
   RelatedSemanticType Value: Pathologic Function\
   RelatedSemanticType UsageNote: If the process is specific, for example to a site or substance, then 'Disease or Syndrome' will be assigned and not 'Pathologic Function'. For example, "cerebral anoxia", "brain edema", and "milk hypersensitivity" will all be assigned to 'Disease or Syndrome' only.\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 19\
  \
   RelationLabel Abbreviation: CW\
   RelationLabel Definition: Occurs at the same time as, together with, or jointly. This includes is co-incident with, is concurrent with, is contemporaneous with, accompanies, coexists with, and is concomitant with.\
   RelationLabel InverseLabel: co-occurs\_with\
   RelationLabel Tree Number: R4.1\
   RelationLabel Ui: T137\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: patf\
   RelatedSemanticType Definition: A disordered process, activity, or state of the organism as a whole, of a body system or systems, or of multiple organs or tissues. Included here are normal responses to a negative stimulus as well as patholologic conditions or states that are less specific than a disease. Pathologic functions frequently have systemic effects.\
   RelatedSemanticType Tree Number: B2.2.1.2\
   RelatedSemanticType Ui: T046\
   RelatedSemanticType Value: Pathologic Function\
   RelatedSemanticType UsageNote: If the process is specific, for example to a site or substance, then 'Disease or Syndrome' will be assigned and not 'Pathologic Function'. For example, "cerebral anoxia", "brain edema", and "milk hypersensitivity" will all be assigned to 'Disease or Syndrome' only.\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 19\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: dsyn\
   RelatedSemanticType Definition: A condition which alters or interferes with a normal process, state, or activity of an organism. It is usually characterized by the abnormal functioning of one or more of the host's systems, parts, or organs. Included here is a complex of symptoms descriptive of a disorder.\
   RelatedSemanticType Tree Number: B2.2.1.2.1\
   RelatedSemanticType Ui: T047\
   RelatedSemanticType Value: Disease or Syndrome\
   RelatedSemanticType UsageNote: Any specific disease or syndrome that is modified by such modifiers as "acute", "prolonged", etc. will also be assigned to this type. If an anatomic abnormality has a pathologic manifestation, then it will be given this type as well as a type from the 'Anatomical Abnormality' hierarchy, e.g., "Diabetic Cataract" will be double-typed for this reason.\
   RelatedSemanticType Child Count: 2\
   RelatedSemanticType Relation Count: 3\
  \
   RelationLabel Abbreviation: CM\
   RelationLabel Definition: Causes to become more severe or complex or results in adverse effects.\
   RelationLabel InverseLabel: complicated\_by\
   RelationLabel Tree Number: R3.1.4\
   RelationLabel Ui: T149\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: dsyn\
   RelatedSemanticType Definition: A condition which alters or interferes with a normal process, state, or activity of an organism. It is usually characterized by the abnormal functioning of one or more of the host's systems, parts, or organs. Included here is a complex of symptoms descriptive of a disorder.\
   RelatedSemanticType Tree Number: B2.2.1.2.1\
   RelatedSemanticType Ui: T047\
   RelatedSemanticType Value: Disease or Syndrome\
   RelatedSemanticType UsageNote: Any specific disease or syndrome that is modified by such modifiers as "acute", "prolonged", etc. will also be assigned to this type. If an anatomic abnormality has a pathologic manifestation, then it will be given this type as well as a type from the 'Anatomical Abnormality' hierarchy, e.g., "Diabetic Cataract" will be double-typed for this reason.\
   RelatedSemanticType Child Count: 2\
   RelatedSemanticType Relation Count: 3\
  \
   RelationLabel Abbreviation: CW\
   RelationLabel Definition: Occurs at the same time as, together with, or jointly. This includes is co-incident with, is concurrent with, is contemporaneous with, accompanies, coexists with, and is concomitant with.\
   RelationLabel InverseLabel: co-occurs\_with\
   RelationLabel Tree Number: R4.1\
   RelationLabel Ui: T137\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: dsyn\
   RelatedSemanticType Definition: A condition which alters or interferes with a normal process, state, or activity of an organism. It is usually characterized by the abnormal functioning of one or more of the host's systems, parts, or organs. Included here is a complex of symptoms descriptive of a disorder.\
   RelatedSemanticType Tree Number: B2.2.1.2.1\
   RelatedSemanticType Ui: T047\
   RelatedSemanticType Value: Disease or Syndrome\
   RelatedSemanticType UsageNote: Any specific disease or syndrome that is modified by such modifiers as "acute", "prolonged", etc. will also be assigned to this type. If an anatomic abnormality has a pathologic manifestation, then it will be given this type as well as a type from the 'Anatomical Abnormality' hierarchy, e.g., "Diabetic Cataract" will be double-typed for this reason.\
   RelatedSemanticType Child Count: 2\
   RelatedSemanticType Relation Count: 3\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: mobd\
   RelatedSemanticType Definition: A clinically significant dysfunction whose major manifestation is behavioral or psychological. These dysfunctions may have identified or presumed biological etiologies or manifestations.\
   RelatedSemanticType Tree Number: B2.2.1.2.1.1\
   RelatedSemanticType Ui: T048\
   RelatedSemanticType Value: Mental or Behavioral Dysfunction\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 6\
  \
   RelationLabel Abbreviation: CM\
   RelationLabel Definition: Causes to become more severe or complex or results in adverse effects.\
   RelationLabel InverseLabel: complicated\_by\
   RelationLabel Tree Number: R3.1.4\
   RelationLabel Ui: T149\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: mobd\
   RelatedSemanticType Definition: A clinically significant dysfunction whose major manifestation is behavioral or psychological. These dysfunctions may have identified or presumed biological etiologies or manifestations.\
   RelatedSemanticType Tree Number: B2.2.1.2.1.1\
   RelatedSemanticType Ui: T048\
   RelatedSemanticType Value: Mental or Behavioral Dysfunction\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 6\
  \
   RelationLabel Abbreviation: CW\
   RelationLabel Definition: Occurs at the same time as, together with, or jointly. This includes is co-incident with, is concurrent with, is contemporaneous with, accompanies, coexists with, and is concomitant with.\
   RelationLabel InverseLabel: co-occurs\_with\
   RelationLabel Tree Number: R4.1\
   RelationLabel Ui: T137\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: mobd\
   RelatedSemanticType Definition: A clinically significant dysfunction whose major manifestation is behavioral or psychological. These dysfunctions may have identified or presumed biological etiologies or manifestations.\
   RelatedSemanticType Tree Number: B2.2.1.2.1.1\
   RelatedSemanticType Ui: T048\
   RelatedSemanticType Value: Mental or Behavioral Dysfunction\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 6\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: comd\
   RelatedSemanticType Definition: A pathologic function inherent to cells, parts of cells, or molecules.\
   RelatedSemanticType Tree Number: B2.2.1.2.2\
   RelatedSemanticType Ui: T049\
   RelatedSemanticType Value: Cell or Molecular Dysfunction\
   RelatedSemanticType UsageNote: This is not intended to be a repository for diseases whose molecular basis has been established.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 1\
  \
   RelationLabel Abbreviation: CM\
   RelationLabel Definition: Causes to become more severe or complex or results in adverse effects.\
   RelationLabel InverseLabel: complicated\_by\
   RelationLabel Tree Number: R3.1.4\
   RelationLabel Ui: T149\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: comd\
   RelatedSemanticType Definition: A pathologic function inherent to cells, parts of cells, or molecules.\
   RelatedSemanticType Tree Number: B2.2.1.2.2\
   RelatedSemanticType Ui: T049\
   RelatedSemanticType Value: Cell or Molecular Dysfunction\
   RelatedSemanticType UsageNote: This is not intended to be a repository for diseases whose molecular basis has been established.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 1\
  \
   RelationLabel Abbreviation: CW\
   RelationLabel Definition: Occurs at the same time as, together with, or jointly. This includes is co-incident with, is concurrent with, is contemporaneous with, accompanies, coexists with, and is concomitant with.\
   RelationLabel InverseLabel: co-occurs\_with\
   RelationLabel Tree Number: R4.1\
   RelationLabel Ui: T137\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: comd\
   RelatedSemanticType Definition: A pathologic function inherent to cells, parts of cells, or molecules.\
   RelatedSemanticType Tree Number: B2.2.1.2.2\
   RelatedSemanticType Ui: T049\
   RelatedSemanticType Value: Cell or Molecular Dysfunction\
   RelatedSemanticType UsageNote: This is not intended to be a repository for diseases whose molecular basis has been established.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 1\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: emod\
   RelatedSemanticType Definition: A representation in a non-human organism of a human disease for the purpose of research into its mechanism or treatment.\
   RelatedSemanticType Tree Number: B2.2.1.2.3\
   RelatedSemanticType Ui: T050\
   RelatedSemanticType Value: Experimental Model of Disease\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 1\
  \
   RelationLabel Abbreviation: CM\
   RelationLabel Definition: Causes to become more severe or complex or results in adverse effects.\
   RelationLabel InverseLabel: complicated\_by\
   RelationLabel Tree Number: R3.1.4\
   RelationLabel Ui: T149\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: emod\
   RelatedSemanticType Definition: A representation in a non-human organism of a human disease for the purpose of research into its mechanism or treatment.\
   RelatedSemanticType Tree Number: B2.2.1.2.3\
   RelatedSemanticType Ui: T050\
   RelatedSemanticType Value: Experimental Model of Disease\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 1\
  \
   RelationLabel Abbreviation: CW\
   RelationLabel Definition: Occurs at the same time as, together with, or jointly. This includes is co-incident with, is concurrent with, is contemporaneous with, accompanies, coexists with, and is concomitant with.\
   RelationLabel InverseLabel: co-occurs\_with\
   RelationLabel Tree Number: R4.1\
   RelationLabel Ui: T137\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: emod\
   RelatedSemanticType Definition: A representation in a non-human organism of a human disease for the purpose of research into its mechanism or treatment.\
   RelatedSemanticType Tree Number: B2.2.1.2.3\
   RelatedSemanticType Ui: T050\
   RelatedSemanticType Value: Experimental Model of Disease\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 1\
  \
   RelationLabel Abbreviation: IS\
   RelationLabel Definition: The basic hierarchical link in the Network. If one item "isa" another item then the first item is more specific in meaning than the second item.\
   RelationLabel InverseLabel: inverse\_isa\
   RelationLabel Tree Number: H\
   RelationLabel Ui: T186\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: evnt\
   RelatedSemanticType Definition: A broad type for grouping activities, processes and states.\
   RelatedSemanticType Tree Number: B\
   RelatedSemanticType Ui: T051\
   RelatedSemanticType Value: Event\
   RelatedSemanticType UsageNote: Few concepts will be assigned to this broad type.\
   RelatedSemanticType Child Count: 2\
   RelatedSemanticType Relation Count: 1\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: socb\
   RelatedSemanticType Definition: Behavior that is a direct result or function of the interaction of humans or animals with their fellows. This includes behavior that may be considered anti-social.\
   RelatedSemanticType Tree Number: B1.1.1\
   RelatedSemanticType Ui: T054\
   RelatedSemanticType Value: Social Behavior\
   RelatedSemanticType UsageNote: 'Social Behavior' requires the direct participation of others and is, thus, distinguished from 'Individual Behavior' which is carried out by an individual, though others may be present.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 2\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inbe\
   RelatedSemanticType Definition: Behavior exhibited by a human or an animal that is not a direct result of interaction with other members of the species, but which may have an effect on others.\
   RelatedSemanticType Tree Number: B1.1.2\
   RelatedSemanticType Ui: T055\
   RelatedSemanticType Value: Individual Behavior\
   RelatedSemanticType UsageNote: 'Individual Behavior' is carried out by an individual, though others may be present, and is, thus, distinguished from 'Social Behavior' which requires the direct participation of others.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 6\
  \
   RelationLabel Abbreviation: AW\
   RelationLabel Definition: has a significant or salient relationship to.\
   RelationLabel InverseLabel: associated\_with\
   RelationLabel Tree Number: R\
   RelationLabel Ui: T166\
   RelationLabel Child Count: 5\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inbe\
   RelatedSemanticType Definition: Behavior exhibited by a human or an animal that is not a direct result of interaction with other members of the species, but which may have an effect on others.\
   RelatedSemanticType Tree Number: B1.1.2\
   RelatedSemanticType Ui: T055\
   RelatedSemanticType Value: Individual Behavior\
   RelatedSemanticType UsageNote: 'Individual Behavior' is carried out by an individual, though others may be present, and is, thus, distinguished from 'Social Behavior' which requires the direct participation of others.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 6\
  \
   RelationLabel Abbreviation: AW\
   RelationLabel Definition: has a significant or salient relationship to.\
   RelationLabel InverseLabel: associated\_with\
   RelationLabel Tree Number: R\
   RelationLabel Ui: T166\
   RelationLabel Child Count: 5\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: dora\
   RelatedSemanticType Definition: An activity carried out for recreation or exercise, or as part of daily life.\
   RelatedSemanticType Tree Number: B1.2\
   RelatedSemanticType Ui: T056\
   RelatedSemanticType Value: Daily or Recreational Activity\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 4\
  \
   RelationLabel Abbreviation: AW\
   RelationLabel Definition: has a significant or salient relationship to.\
   RelationLabel InverseLabel: associated\_with\
   RelationLabel Tree Number: R\
   RelationLabel Ui: T166\
   RelationLabel Child Count: 5\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: ocac\
   RelatedSemanticType Definition: An activity carried out as part of an occupation or job.\
   RelatedSemanticType Tree Number: B1.3\
   RelatedSemanticType Ui: T057\
   RelatedSemanticType Value: Occupational Activity\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 4\
   RelatedSemanticType Relation Count: 5\
  \
   RelationLabel Abbreviation: AW\
   RelationLabel Definition: has a significant or salient relationship to.\
   RelationLabel InverseLabel: associated\_with\
   RelationLabel Tree Number: R\
   RelationLabel Ui: T166\
   RelationLabel Child Count: 5\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: hlca\
   RelatedSemanticType Definition: An activity of or relating to the practice of medicine or involving the care of patients.\
   RelatedSemanticType Tree Number: B1.3.1\
   RelatedSemanticType Ui: T058\
   RelatedSemanticType Value: Health Care Activity\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 2\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: lbpr\
   RelatedSemanticType Definition: A procedure, method, or technique used to determine the composition, quantity, or concentration of a specimen, and which is carried out in a clinical laboratory. Included here are procedures which measure the times and rates of reactions.\
   RelatedSemanticType Tree Number: B1.3.1.1\
   RelatedSemanticType Ui: T059\
   RelatedSemanticType Value: Laboratory Procedure\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 17\
  \
   RelationLabel Abbreviation: AW\
   RelationLabel Definition: has a significant or salient relationship to.\
   RelationLabel InverseLabel: associated\_with\
   RelationLabel Tree Number: R\
   RelationLabel Ui: T166\
   RelationLabel Child Count: 5\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: lbpr\
   RelatedSemanticType Definition: A procedure, method, or technique used to determine the composition, quantity, or concentration of a specimen, and which is carried out in a clinical laboratory. Included here are procedures which measure the times and rates of reactions.\
   RelatedSemanticType Tree Number: B1.3.1.1\
   RelatedSemanticType Ui: T059\
   RelatedSemanticType Value: Laboratory Procedure\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 17\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: diap\
   RelatedSemanticType Definition: A procedure, method, or technique used to determine the nature or identity of a disease or disorder. This excludes procedures which are primarily carried out on specimens in a laboratory.\
   RelatedSemanticType Tree Number: B1.3.1.2\
   RelatedSemanticType Ui: T060\
   RelatedSemanticType Value: Diagnostic Procedure\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 18\
  \
   RelationLabel Abbreviation: AW\
   RelationLabel Definition: has a significant or salient relationship to.\
   RelationLabel InverseLabel: associated\_with\
   RelationLabel Tree Number: R\
   RelationLabel Ui: T166\
   RelationLabel Child Count: 5\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: diap\
   RelatedSemanticType Definition: A procedure, method, or technique used to determine the nature or identity of a disease or disorder. This excludes procedures which are primarily carried out on specimens in a laboratory.\
   RelatedSemanticType Tree Number: B1.3.1.2\
   RelatedSemanticType Ui: T060\
   RelatedSemanticType Value: Diagnostic Procedure\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 18\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: topp\
   RelatedSemanticType Definition: A procedure, method, or technique designed to prevent a disease or a disorder, or to improve physical function, or used in the process of treating a disease or injury.\
   RelatedSemanticType Tree Number: B1.3.1.3\
   RelatedSemanticType Ui: T061\
   RelatedSemanticType Value: Therapeutic or Preventive Procedure\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 12\
  \
   RelationLabel Abbreviation: AW\
   RelationLabel Definition: has a significant or salient relationship to.\
   RelationLabel InverseLabel: associated\_with\
   RelationLabel Tree Number: R\
   RelationLabel Ui: T166\
   RelationLabel Child Count: 5\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: topp\
   RelatedSemanticType Definition: A procedure, method, or technique designed to prevent a disease or a disorder, or to improve physical function, or used in the process of treating a disease or injury.\
   RelatedSemanticType Tree Number: B1.3.1.3\
   RelatedSemanticType Ui: T061\
   RelatedSemanticType Value: Therapeutic or Preventive Procedure\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 12\
  \
   RelationLabel Abbreviation: AW\
   RelationLabel Definition: has a significant or salient relationship to.\
   RelationLabel InverseLabel: associated\_with\
   RelationLabel Tree Number: R\
   RelationLabel Ui: T166\
   RelationLabel Child Count: 5\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: resa\
   RelatedSemanticType Definition: An activity carried out as part of research or experimentation.\
   RelatedSemanticType Tree Number: B1.3.2\
   RelatedSemanticType Ui: T062\
   RelatedSemanticType Value: Research Activity\
   RelatedSemanticType UsageNote: In some cases, a concept may be assigned to both this type and the type 'Intellectual Product'. For example, the concept "Comparative Study" might be viewed as both an activity and the result, or product, of that activity.\
   RelatedSemanticType Child Count: 1\
   RelatedSemanticType Relation Count: 9\
  \
   RelationLabel Abbreviation: AW\
   RelationLabel Definition: has a significant or salient relationship to.\
   RelationLabel InverseLabel: associated\_with\
   RelationLabel Tree Number: R\
   RelationLabel Ui: T166\
   RelationLabel Child Count: 5\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: mbrt\
   RelatedSemanticType Definition: Any of the techniques used in the study of or the directed modification of the gene complement of a living organism.\
   RelatedSemanticType Tree Number: B1.3.2.1\
   RelatedSemanticType Ui: T063\
   RelatedSemanticType Value: Molecular Biology Research Technique\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 3\
  \
   RelationLabel Abbreviation: AW\
   RelationLabel Definition: has a significant or salient relationship to.\
   RelationLabel InverseLabel: associated\_with\
   RelationLabel Tree Number: R\
   RelationLabel Ui: T166\
   RelationLabel Child Count: 5\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: gora\
   RelatedSemanticType Definition: An activity carried out by officially constituted governments, or an activity related to the creation or enforcement of the rules or regulations governing some field of endeavor.\
   RelatedSemanticType Tree Number: B1.3.3\
   RelatedSemanticType Ui: T064\
   RelatedSemanticType Value: Governmental or Regulatory Activity\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 1\
  \
   RelationLabel Abbreviation: AW\
   RelationLabel Definition: has a significant or salient relationship to.\
   RelationLabel InverseLabel: associated\_with\
   RelationLabel Tree Number: R\
   RelationLabel Ui: T166\
   RelationLabel Child Count: 5\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: edac\
   RelatedSemanticType Definition: An activity related to the organization and provision of education.\
   RelatedSemanticType Tree Number: B1.3.4\
   RelatedSemanticType Ui: T065\
   RelatedSemanticType Value: Educational Activity\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 1\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: phpr\
   RelatedSemanticType Definition: A process or state which occurs naturally or as a result of an activity.\
   RelatedSemanticType Tree Number: B2\
   RelatedSemanticType Ui: T067\
   RelatedSemanticType Value: Phenomenon or Process\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 3\
   RelatedSemanticType Relation Count: 3\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: hcpp\
   RelatedSemanticType Definition: A phenomenon or process that is a result of the activities of human beings.\
   RelatedSemanticType Tree Number: B2.1\
   RelatedSemanticType Ui: T068\
   RelatedSemanticType Value: Human-caused Phenomenon or Process\
   RelatedSemanticType UsageNote: If the concept refers to the activity itself, rather than the result of that activity, a type from the 'Activity' hierarchy will be assigned instead.\
   RelatedSemanticType Child Count: 1\
   RelatedSemanticType Relation Count: 1\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: eehu\
   RelatedSemanticType Definition: A change in the natural environment that is a result of the activities of human beings.\
   RelatedSemanticType Tree Number: B2.1.1\
   RelatedSemanticType Ui: T069\
   RelatedSemanticType Value: Environmental Effect of Humans\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 1\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: npop\
   RelatedSemanticType Definition: A phenomenon or process that occurs irrespective of the activities of human beings.\
   RelatedSemanticType Tree Number: B2.2\
   RelatedSemanticType Ui: T070\
   RelatedSemanticType Value: Natural Phenomenon or Process\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 1\
   RelatedSemanticType Relation Count: 3\
  \
   RelationLabel Abbreviation: AW\
   RelationLabel Definition: has a significant or salient relationship to.\
   RelationLabel InverseLabel: associated\_with\
   RelationLabel Tree Number: R\
   RelationLabel Ui: T166\
   RelationLabel Child Count: 5\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: geoa\
   RelatedSemanticType Definition: A geographic location, generally having definite boundaries.\
   RelatedSemanticType Tree Number: A2.1.5.4\
   RelatedSemanticType Ui: T083\
   RelatedSemanticType Value: Geographic Area\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 4\
  \
   RelationLabel Abbreviation: II\
   RelationLabel Definition: Is an issue in or a point of discussion, study, debate, or dispute.\
   RelationLabel InverseLabel: has\_issue\
   RelationLabel Tree Number: R5.12\
   RelationLabel Ui: T165\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: ocdi\
   RelatedSemanticType Definition: A vocation, academic discipline, or field of study, or a subpart of an occupation or discipline.\
   RelatedSemanticType Tree Number: A2.6\
   RelatedSemanticType Ui: T090\
   RelatedSemanticType Value: Occupation or Discipline\
   RelatedSemanticType UsageNote: If the concept refers to the individuals who have the vocation, the type 'Professional or Occupational Group' will be assigned instead.\
   RelatedSemanticType Child Count: 1\
   RelatedSemanticType Relation Count: 2\
  \
   RelationLabel Abbreviation: II\
   RelationLabel Definition: Is an issue in or a point of discussion, study, debate, or dispute.\
   RelationLabel InverseLabel: has\_issue\
   RelationLabel Tree Number: R5.12\
   RelationLabel Ui: T165\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: bmod\
   RelatedSemanticType Definition: A vocation, academic discipline, or field of study related to biomedicine.\
   RelatedSemanticType Tree Number: A2.6.1\
   RelatedSemanticType Ui: T091\
   RelatedSemanticType Value: Biomedical Occupation or Discipline\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 1\
  \
   RelationLabel Abbreviation: OC\
   RelationLabel Definition: Takes place in or happens under given conditions, circumstances, or time periods, or in a given location or population. This includes appears in, transpires, comes about, is present in, and exists in.\
   RelationLabel InverseLabel: has\_occurrence\
   RelationLabel Tree Number: R3.4\
   RelationLabel Ui: T152\
   RelationLabel Child Count: 1\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: prog\
   RelatedSemanticType Definition: An individual or individuals classified according to their vocation.\
   RelatedSemanticType Tree Number: A2.9.1\
   RelatedSemanticType Ui: T097\
   RelatedSemanticType Value: Professional or Occupational Group\
   RelatedSemanticType UsageNote: If the concept refers to the discipline or vocation itself, rather than to the individuals who have the vocation, then the type 'Occupation or Discipline' will be assigned instead.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 5\
  \
   RelationLabel Abbreviation: OC\
   RelationLabel Definition: Takes place in or happens under given conditions, circumstances, or time periods, or in a given location or population. This includes appears in, transpires, comes about, is present in, and exists in.\
   RelationLabel InverseLabel: has\_occurrence\
   RelationLabel Tree Number: R3.4\
   RelationLabel Ui: T152\
   RelationLabel Child Count: 1\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: popg\
   RelatedSemanticType Definition: An indivdual or individuals classified according to their sex, racial origin, religion, common place of living, financial or social status, or some other cultural or behavioral attribute.\
   RelatedSemanticType Tree Number: A2.9.2\
   RelatedSemanticType Ui: T098\
   RelatedSemanticType Value: Population Group\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 4\
  \
   RelationLabel Abbreviation: AW\
   RelationLabel Definition: has a significant or salient relationship to.\
   RelationLabel InverseLabel: associated\_with\
   RelationLabel Tree Number: R\
   RelationLabel Ui: T166\
   RelationLabel Child Count: 5\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: popg\
   RelatedSemanticType Definition: An indivdual or individuals classified according to their sex, racial origin, religion, common place of living, financial or social status, or some other cultural or behavioral attribute.\
   RelatedSemanticType Tree Number: A2.9.2\
   RelatedSemanticType Ui: T098\
   RelatedSemanticType Value: Population Group\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 4\
  \
   RelationLabel Abbreviation: OC\
   RelationLabel Definition: Takes place in or happens under given conditions, circumstances, or time periods, or in a given location or population. This includes appears in, transpires, comes about, is present in, and exists in.\
   RelationLabel InverseLabel: has\_occurrence\
   RelationLabel Tree Number: R3.4\
   RelationLabel Ui: T152\
   RelationLabel Child Count: 1\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: famg\
   RelatedSemanticType Definition: An individual or individuals classified according to their family relationships or relative position in the family unit.\
   RelatedSemanticType Tree Number: A2.9.3\
   RelatedSemanticType Ui: T099\
   RelatedSemanticType Value: Family Group\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 1\
  \
   RelationLabel Abbreviation: OC\
   RelationLabel Definition: Takes place in or happens under given conditions, circumstances, or time periods, or in a given location or population. This includes appears in, transpires, comes about, is present in, and exists in.\
   RelationLabel InverseLabel: has\_occurrence\
   RelationLabel Tree Number: R3.4\
   RelationLabel Ui: T152\
   RelationLabel Child Count: 1\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: aggp\
   RelatedSemanticType Definition: An individual or individuals classified according to their age.\
   RelatedSemanticType Tree Number: A2.9.4\
   RelatedSemanticType Ui: T100\
   RelatedSemanticType Value: Age Group\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 1\
  \
   RelationLabel Abbreviation: OC\
   RelationLabel Definition: Takes place in or happens under given conditions, circumstances, or time periods, or in a given location or population. This includes appears in, transpires, comes about, is present in, and exists in.\
   RelationLabel InverseLabel: has\_occurrence\
   RelationLabel Tree Number: R3.4\
   RelationLabel Ui: T152\
   RelationLabel Child Count: 1\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: podg\
   RelatedSemanticType Definition: An individual or individuals classified according to a disability, disease, condition or treatment.\
   RelatedSemanticType Tree Number: A2.9.5\
   RelatedSemanticType Ui: T101\
   RelatedSemanticType Value: Patient or Disabled Group\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 1\
  \
   RelationLabel Abbreviation: AW\
   RelationLabel Definition: has a significant or salient relationship to.\
   RelationLabel InverseLabel: associated\_with\
   RelationLabel Tree Number: R\
   RelationLabel Ui: T166\
   RelationLabel Child Count: 5\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: clna\
   RelatedSemanticType Definition: An observable or measurable property or state of an organism of clinical interest.\
   RelatedSemanticType Tree Number: A2.3.1\
   RelatedSemanticType Ui: T201\
   RelatedSemanticType Value: Clinical Attribute\
   RelatedSemanticType UsageNote: These are the attributes that are being evaluated or measured, not the results of the evaluation.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 1\
  \
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

</div>

<div id="getInverseInheritedSemanticTypeRelations"
class="method rounded-content-block">

**Method: **<span
class="method-name">getInverseInheritedSemanticTypeRelations</span><span
class="method-parameters">(String ticket,String version,String
semanticTypeId)</span>
**Returns:** <span
class="method-return-type">ArrayList&lt;SemanticTypeRelationDTO&gt; </span>

<div class="method-description">

**Use Case:** Given a UMLS release and a semantic type unique identifier
(TUI), this call returns all of the inverse semantic type relations
inherited by the TUI. Inverse semantic type relations are those that
relate other semantic types to the given semantic type.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

myarrSemTyRelDTO =
utsSemanticNetworkService.getInverseInheritedSemanticTypeRelations
(ticket, umlsRelease, "T037");\
\
 for (int i = 0; i &lt; myarrSemTyRelDTO.size(); i++) {\
 SemanticTypeRelationDTO mySemTyRel = myarrSemTyRelDTO.get(i);\
 String relAbbr = mySemTyRel.getRelationLabel().getAbbreviation();\
 String relDef = mySemTyRel.getRelationLabel().getDefinition();\
 String relInvLabel = mySemTyRel.getRelationLabel().getInverseLabel();\
 String relTreeNum = mySemTyRel.getRelationLabel().getTreeNumber();\
 String relUi = mySemTyRel.getRelationLabel().getUi();\
 int relChildCnt = mySemTyRel.getRelationLabel().getChildCount();\
 int relRelCnt = mySemTyRel.getRelationLabel().getRelationCount();\
\
 String SemTypeAbbr =
mySemTyRel.getRelatedSemanticType().getAbbreviation();\
 String SemTypeDef =
mySemTyRel.getRelatedSemanticType().getDefinition();\
 String SemTypeTreeNum =
mySemTyRel.getRelatedSemanticType().getTreeNumber();\
 String SemTypeUi = mySemTyRel.getRelatedSemanticType().getUi();\
 String SemTypeVal = mySemTyRel.getRelatedSemanticType().getValue();\
 String SemTypeUsage =
mySemTyRel.getRelatedSemanticType().getUsageNote();\
 int SemTypeChildCnt =
mySemTyRel.getRelatedSemanticType().getChildCount();\
 int SemTypeRelCnt =
mySemTyRel.getRelatedSemanticType().getRelationCount();\
 }\

</div>

#### Sample Output:

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  RelationLabel Abbreviation: CA\
   RelationLabel Definition: Brings about a condition or an effect. Implied here is that an agent, such as for example, a pharmacologic substance or an organism, has brought about the effect. This includes induces, effects, evokes, and etiology.\
   RelationLabel InverseLabel: caused\_by\
   RelationLabel Tree Number: R3.2.2\
   RelationLabel Ui: T147\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CM\
   RelationLabel Definition: Causes to become more severe or complex or results in adverse effects.\
   RelationLabel InverseLabel: complicated\_by\
   RelationLabel Tree Number: R3.1.4\
   RelationLabel Ui: T149\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CA\
   RelationLabel Definition: Brings about a condition or an effect. Implied here is that an agent, such as for example, a pharmacologic substance or an organism, has brought about the effect. This includes induces, effects, evokes, and etiology.\
   RelationLabel InverseLabel: caused\_by\
   RelationLabel Tree Number: R3.2.2\
   RelationLabel Ui: T147\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CM\
   RelationLabel Definition: Causes to become more severe or complex or results in adverse effects.\
   RelationLabel InverseLabel: complicated\_by\
   RelationLabel Tree Number: R3.1.4\
   RelationLabel Ui: T149\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CA\
   RelationLabel Definition: Brings about a condition or an effect. Implied here is that an agent, such as for example, a pharmacologic substance or an organism, has brought about the effect. This includes induces, effects, evokes, and etiology.\
   RelationLabel InverseLabel: caused\_by\
   RelationLabel Tree Number: R3.2.2\
   RelationLabel Ui: T147\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CM\
   RelationLabel Definition: Causes to become more severe or complex or results in adverse effects.\
   RelationLabel InverseLabel: complicated\_by\
   RelationLabel Tree Number: R3.1.4\
   RelationLabel Ui: T149\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CA\
   RelationLabel Definition: Brings about a condition or an effect. Implied here is that an agent, such as for example, a pharmacologic substance or an organism, has brought about the effect. This includes induces, effects, evokes, and etiology.\
   RelationLabel InverseLabel: caused\_by\
   RelationLabel Tree Number: R3.2.2\
   RelationLabel Ui: T147\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CM\
   RelationLabel Definition: Causes to become more severe or complex or results in adverse effects.\
   RelationLabel InverseLabel: complicated\_by\
   RelationLabel Tree Number: R3.1.4\
   RelationLabel Ui: T149\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CA\
   RelationLabel Definition: Brings about a condition or an effect. Implied here is that an agent, such as for example, a pharmacologic substance or an organism, has brought about the effect. This includes induces, effects, evokes, and etiology.\
   RelationLabel InverseLabel: caused\_by\
   RelationLabel Tree Number: R3.2.2\
   RelationLabel Ui: T147\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CM\
   RelationLabel Definition: Causes to become more severe or complex or results in adverse effects.\
   RelationLabel InverseLabel: complicated\_by\
   RelationLabel Tree Number: R3.1.4\
   RelationLabel Ui: T149\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CA\
   RelationLabel Definition: Brings about a condition or an effect. Implied here is that an agent, such as for example, a pharmacologic substance or an organism, has brought about the effect. This includes induces, effects, evokes, and etiology.\
   RelationLabel InverseLabel: caused\_by\
   RelationLabel Tree Number: R3.2.2\
   RelationLabel Ui: T147\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CA\
   RelationLabel Definition: Brings about a condition or an effect. Implied here is that an agent, such as for example, a pharmacologic substance or an organism, has brought about the effect. This includes induces, effects, evokes, and etiology.\
   RelationLabel InverseLabel: caused\_by\
   RelationLabel Tree Number: R3.2.2\
   RelationLabel Ui: T147\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CA\
   RelationLabel Definition: Brings about a condition or an effect. Implied here is that an agent, such as for example, a pharmacologic substance or an organism, has brought about the effect. This includes induces, effects, evokes, and etiology.\
   RelationLabel InverseLabel: caused\_by\
   RelationLabel Tree Number: R3.2.2\
   RelationLabel Ui: T147\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CA\
   RelationLabel Definition: Brings about a condition or an effect. Implied here is that an agent, such as for example, a pharmacologic substance or an organism, has brought about the effect. This includes induces, effects, evokes, and etiology.\
   RelationLabel InverseLabel: caused\_by\
   RelationLabel Tree Number: R3.2.2\
   RelationLabel Ui: T147\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: MF\
   RelationLabel Definition: That part of a phenomenon which is directly observable or concretely or visibly expressed, or which gives evidence to the underlying process. This includes expression of, display of, and exhibition of.\
   RelationLabel InverseLabel: has\_manifestation\
   RelationLabel Tree Number: R3.6\
   RelationLabel Ui: T150\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: OC\
   RelationLabel Definition: Takes place in or happens under given conditions, circumstances, or time periods, or in a given location or population. This includes appears in, transpires, comes about, is present in, and exists in.\
   RelationLabel InverseLabel: has\_occurrence\
   RelationLabel Tree Number: R3.4\
   RelationLabel Ui: T152\
   RelationLabel Child Count: 1\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: MF\
   RelationLabel Definition: That part of a phenomenon which is directly observable or concretely or visibly expressed, or which gives evidence to the underlying process. This includes expression of, display of, and exhibition of.\
   RelationLabel InverseLabel: has\_manifestation\
   RelationLabel Tree Number: R3.6\
   RelationLabel Ui: T150\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CM\
   RelationLabel Definition: Causes to become more severe or complex or results in adverse effects.\
   RelationLabel InverseLabel: complicated\_by\
   RelationLabel Tree Number: R3.1.4\
   RelationLabel Ui: T149\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CM\
   RelationLabel Definition: Causes to become more severe or complex or results in adverse effects.\
   RelationLabel InverseLabel: complicated\_by\
   RelationLabel Tree Number: R3.1.4\
   RelationLabel Ui: T149\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CA\
   RelationLabel Definition: Brings about a condition or an effect. Implied here is that an agent, such as for example, a pharmacologic substance or an organism, has brought about the effect. This includes induces, effects, evokes, and etiology.\
   RelationLabel InverseLabel: caused\_by\
   RelationLabel Tree Number: R3.2.2\
   RelationLabel Ui: T147\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: LO\
   RelationLabel Definition: The position, site, or region of an entity or the site of a process.\
   RelationLabel InverseLabel: has\_location\
   RelationLabel Tree Number: R2.1\
   RelationLabel Ui: T135\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: LO\
   RelationLabel Definition: The position, site, or region of an entity or the site of a process.\
   RelationLabel InverseLabel: has\_location\
   RelationLabel Tree Number: R2.1\
   RelationLabel Ui: T135\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: LO\
   RelationLabel Definition: The position, site, or region of an entity or the site of a process.\
   RelationLabel InverseLabel: has\_location\
   RelationLabel Tree Number: R2.1\
   RelationLabel Ui: T135\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: LO\
   RelationLabel Definition: The position, site, or region of an entity or the site of a process.\
   RelationLabel InverseLabel: has\_location\
   RelationLabel Tree Number: R2.1\
   RelationLabel Ui: T135\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: LO\
   RelationLabel Definition: The position, site, or region of an entity or the site of a process.\
   RelationLabel InverseLabel: has\_location\
   RelationLabel Tree Number: R2.1\
   RelationLabel Ui: T135\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CA\
   RelationLabel Definition: Brings about a condition or an effect. Implied here is that an agent, such as for example, a pharmacologic substance or an organism, has brought about the effect. This includes induces, effects, evokes, and etiology.\
   RelationLabel InverseLabel: caused\_by\
   RelationLabel Tree Number: R3.2.2\
   RelationLabel Ui: T147\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: AW\
   RelationLabel Definition: has a significant or salient relationship to.\
   RelationLabel InverseLabel: associated\_with\
   RelationLabel Tree Number: R\
   RelationLabel Ui: T166\
   RelationLabel Child Count: 5\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: MF\
   RelationLabel Definition: That part of a phenomenon which is directly observable or concretely or visibly expressed, or which gives evidence to the underlying process. This includes expression of, display of, and exhibition of.\
   RelationLabel InverseLabel: has\_manifestation\
   RelationLabel Tree Number: R3.6\
   RelationLabel Ui: T150\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: AW\
   RelationLabel Definition: has a significant or salient relationship to.\
   RelationLabel InverseLabel: associated\_with\
   RelationLabel Tree Number: R\
   RelationLabel Ui: T166\
   RelationLabel Child Count: 5\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: OC\
   RelationLabel Definition: Takes place in or happens under given conditions, circumstances, or time periods, or in a given location or population. This includes appears in, transpires, comes about, is present in, and exists in.\
   RelationLabel InverseLabel: has\_occurrence\
   RelationLabel Tree Number: R3.4\
   RelationLabel Ui: T152\
   RelationLabel Child Count: 1\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: MF\
   RelationLabel Definition: That part of a phenomenon which is directly observable or concretely or visibly expressed, or which gives evidence to the underlying process. This includes expression of, display of, and exhibition of.\
   RelationLabel InverseLabel: has\_manifestation\
   RelationLabel Tree Number: R3.6\
   RelationLabel Ui: T150\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CM\
   RelationLabel Definition: Causes to become more severe or complex or results in adverse effects.\
   RelationLabel InverseLabel: complicated\_by\
   RelationLabel Tree Number: R3.1.4\
   RelationLabel Ui: T149\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: OC\
   RelationLabel Definition: Takes place in or happens under given conditions, circumstances, or time periods, or in a given location or population. This includes appears in, transpires, comes about, is present in, and exists in.\
   RelationLabel InverseLabel: has\_occurrence\
   RelationLabel Tree Number: R3.4\
   RelationLabel Ui: T152\
   RelationLabel Child Count: 1\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: MF\
   RelationLabel Definition: That part of a phenomenon which is directly observable or concretely or visibly expressed, or which gives evidence to the underlying process. This includes expression of, display of, and exhibition of.\
   RelationLabel InverseLabel: has\_manifestation\
   RelationLabel Tree Number: R3.6\
   RelationLabel Ui: T150\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CM\
   RelationLabel Definition: Causes to become more severe or complex or results in adverse effects.\
   RelationLabel InverseLabel: complicated\_by\
   RelationLabel Tree Number: R3.1.4\
   RelationLabel Ui: T149\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: OC\
   RelationLabel Definition: Takes place in or happens under given conditions, circumstances, or time periods, or in a given location or population. This includes appears in, transpires, comes about, is present in, and exists in.\
   RelationLabel InverseLabel: has\_occurrence\
   RelationLabel Tree Number: R3.4\
   RelationLabel Ui: T152\
   RelationLabel Child Count: 1\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: MF\
   RelationLabel Definition: That part of a phenomenon which is directly observable or concretely or visibly expressed, or which gives evidence to the underlying process. This includes expression of, display of, and exhibition of.\
   RelationLabel InverseLabel: has\_manifestation\
   RelationLabel Tree Number: R3.6\
   RelationLabel Ui: T150\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CM\
   RelationLabel Definition: Causes to become more severe or complex or results in adverse effects.\
   RelationLabel InverseLabel: complicated\_by\
   RelationLabel Tree Number: R3.1.4\
   RelationLabel Ui: T149\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: OC\
   RelationLabel Definition: Takes place in or happens under given conditions, circumstances, or time periods, or in a given location or population. This includes appears in, transpires, comes about, is present in, and exists in.\
   RelationLabel InverseLabel: has\_occurrence\
   RelationLabel Tree Number: R3.4\
   RelationLabel Ui: T152\
   RelationLabel Child Count: 1\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: MF\
   RelationLabel Definition: That part of a phenomenon which is directly observable or concretely or visibly expressed, or which gives evidence to the underlying process. This includes expression of, display of, and exhibition of.\
   RelationLabel InverseLabel: has\_manifestation\
   RelationLabel Tree Number: R3.6\
   RelationLabel Ui: T150\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CM\
   RelationLabel Definition: Causes to become more severe or complex or results in adverse effects.\
   RelationLabel InverseLabel: complicated\_by\
   RelationLabel Tree Number: R3.1.4\
   RelationLabel Ui: T149\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CA\
   RelationLabel Definition: Brings about a condition or an effect. Implied here is that an agent, such as for example, a pharmacologic substance or an organism, has brought about the effect. This includes induces, effects, evokes, and etiology.\
   RelationLabel InverseLabel: caused\_by\
   RelationLabel Tree Number: R3.2.2\
   RelationLabel Ui: T147\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CA\
   RelationLabel Definition: Brings about a condition or an effect. Implied here is that an agent, such as for example, a pharmacologic substance or an organism, has brought about the effect. This includes induces, effects, evokes, and etiology.\
   RelationLabel InverseLabel: caused\_by\
   RelationLabel Tree Number: R3.2.2\
   RelationLabel Ui: T147\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CA\
   RelationLabel Definition: Brings about a condition or an effect. Implied here is that an agent, such as for example, a pharmacologic substance or an organism, has brought about the effect. This includes induces, effects, evokes, and etiology.\
   RelationLabel InverseLabel: caused\_by\
   RelationLabel Tree Number: R3.2.2\
   RelationLabel Ui: T147\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CA\
   RelationLabel Definition: Brings about a condition or an effect. Implied here is that an agent, such as for example, a pharmacologic substance or an organism, has brought about the effect. This includes induces, effects, evokes, and etiology.\
   RelationLabel InverseLabel: caused\_by\
   RelationLabel Tree Number: R3.2.2\
   RelationLabel Ui: T147\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CA\
   RelationLabel Definition: Brings about a condition or an effect. Implied here is that an agent, such as for example, a pharmacologic substance or an organism, has brought about the effect. This includes induces, effects, evokes, and etiology.\
   RelationLabel InverseLabel: caused\_by\
   RelationLabel Tree Number: R3.2.2\
   RelationLabel Ui: T147\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CA\
   RelationLabel Definition: Brings about a condition or an effect. Implied here is that an agent, such as for example, a pharmacologic substance or an organism, has brought about the effect. This includes induces, effects, evokes, and etiology.\
   RelationLabel InverseLabel: caused\_by\
   RelationLabel Tree Number: R3.2.2\
   RelationLabel Ui: T147\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CA\
   RelationLabel Definition: Brings about a condition or an effect. Implied here is that an agent, such as for example, a pharmacologic substance or an organism, has brought about the effect. This includes induces, effects, evokes, and etiology.\
   RelationLabel InverseLabel: caused\_by\
   RelationLabel Tree Number: R3.2.2\
   RelationLabel Ui: T147\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CA\
   RelationLabel Definition: Brings about a condition or an effect. Implied here is that an agent, such as for example, a pharmacologic substance or an organism, has brought about the effect. This includes induces, effects, evokes, and etiology.\
   RelationLabel InverseLabel: caused\_by\
   RelationLabel Tree Number: R3.2.2\
   RelationLabel Ui: T147\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CA\
   RelationLabel Definition: Brings about a condition or an effect. Implied here is that an agent, such as for example, a pharmacologic substance or an organism, has brought about the effect. This includes induces, effects, evokes, and etiology.\
   RelationLabel InverseLabel: caused\_by\
   RelationLabel Tree Number: R3.2.2\
   RelationLabel Ui: T147\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CA\
   RelationLabel Definition: Brings about a condition or an effect. Implied here is that an agent, such as for example, a pharmacologic substance or an organism, has brought about the effect. This includes induces, effects, evokes, and etiology.\
   RelationLabel InverseLabel: caused\_by\
   RelationLabel Tree Number: R3.2.2\
   RelationLabel Ui: T147\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CA\
   RelationLabel Definition: Brings about a condition or an effect. Implied here is that an agent, such as for example, a pharmacologic substance or an organism, has brought about the effect. This includes induces, effects, evokes, and etiology.\
   RelationLabel InverseLabel: caused\_by\
   RelationLabel Tree Number: R3.2.2\
   RelationLabel Ui: T147\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CA\
   RelationLabel Definition: Brings about a condition or an effect. Implied here is that an agent, such as for example, a pharmacologic substance or an organism, has brought about the effect. This includes induces, effects, evokes, and etiology.\
   RelationLabel InverseLabel: caused\_by\
   RelationLabel Tree Number: R3.2.2\
   RelationLabel Ui: T147\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CA\
   RelationLabel Definition: Brings about a condition or an effect. Implied here is that an agent, such as for example, a pharmacologic substance or an organism, has brought about the effect. This includes induces, effects, evokes, and etiology.\
   RelationLabel InverseLabel: caused\_by\
   RelationLabel Tree Number: R3.2.2\
   RelationLabel Ui: T147\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CA\
   RelationLabel Definition: Brings about a condition or an effect. Implied here is that an agent, such as for example, a pharmacologic substance or an organism, has brought about the effect. This includes induces, effects, evokes, and etiology.\
   RelationLabel InverseLabel: caused\_by\
   RelationLabel Tree Number: R3.2.2\
   RelationLabel Ui: T147\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CA\
   RelationLabel Definition: Brings about a condition or an effect. Implied here is that an agent, such as for example, a pharmacologic substance or an organism, has brought about the effect. This includes induces, effects, evokes, and etiology.\
   RelationLabel InverseLabel: caused\_by\
   RelationLabel Tree Number: R3.2.2\
   RelationLabel Ui: T147\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: TS\
   RelationLabel Definition: Applies a remedy with the object of effecting a cure or managing a condition.\
   RelationLabel InverseLabel: treated\_by\
   RelationLabel Tree Number: R3.1.2\
   RelationLabel Ui: T154\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CM\
   RelationLabel Definition: Causes to become more severe or complex or results in adverse effects.\
   RelationLabel InverseLabel: complicated\_by\
   RelationLabel Tree Number: R3.1.4\
   RelationLabel Ui: T149\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CA\
   RelationLabel Definition: Brings about a condition or an effect. Implied here is that an agent, such as for example, a pharmacologic substance or an organism, has brought about the effect. This includes induces, effects, evokes, and etiology.\
   RelationLabel InverseLabel: caused\_by\
   RelationLabel Tree Number: R3.2.2\
   RelationLabel Ui: T147\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CA\
   RelationLabel Definition: Brings about a condition or an effect. Implied here is that an agent, such as for example, a pharmacologic substance or an organism, has brought about the effect. This includes induces, effects, evokes, and etiology.\
   RelationLabel InverseLabel: caused\_by\
   RelationLabel Tree Number: R3.2.2\
   RelationLabel Ui: T147\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CA\
   RelationLabel Definition: Brings about a condition or an effect. Implied here is that an agent, such as for example, a pharmacologic substance or an organism, has brought about the effect. This includes induces, effects, evokes, and etiology.\
   RelationLabel InverseLabel: caused\_by\
   RelationLabel Tree Number: R3.2.2\
   RelationLabel Ui: T147\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CA\
   RelationLabel Definition: Brings about a condition or an effect. Implied here is that an agent, such as for example, a pharmacologic substance or an organism, has brought about the effect. This includes induces, effects, evokes, and etiology.\
   RelationLabel InverseLabel: caused\_by\
   RelationLabel Tree Number: R3.2.2\
   RelationLabel Ui: T147\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: RO\
   RelationLabel Definition: The condition, product, or state occurring as a consequence, effect, or conclusion of an activity or process. This includes product of, effect of, sequel of, outcome of, culmination of, and completion of.\
   RelationLabel InverseLabel: has\_result\
   RelationLabel Tree Number: R3.8\
   RelationLabel Ui: T157\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: TS\
   RelationLabel Definition: Applies a remedy with the object of effecting a cure or managing a condition.\
   RelationLabel InverseLabel: treated\_by\
   RelationLabel Tree Number: R3.1.2\
   RelationLabel Ui: T154\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: PV\
   RelationLabel Definition: Stops, hinders or eliminates an action or condition.\
   RelationLabel InverseLabel: prevented\_by\
   RelationLabel Tree Number: R3.1.6\
   RelationLabel Ui: T148\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
   RelationLabel Abbreviation: CA\
   RelationLabel Definition: Brings about a condition or an effect. Implied here is that an agent, such as for example, a pharmacologic substance or an organism, has brought about the effect. This includes induces, effects, evokes, and etiology.\
   RelationLabel InverseLabel: caused\_by\
   RelationLabel Tree Number: R3.2.2\
   RelationLabel Ui: T147\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

</div>

<div id="getSemanticTypeRelation" class="method rounded-content-block">

**Method: **<span
class="method-name">getSemanticTypeRelation</span><span
class="method-parameters">(String ticket,String version,String
semanticTypeId ,String semanticRelationLabelId,String
relatedSemanticTypeId)</span>
**Returns:** <span
class="method-return-type">SemanticTypeRelationDTO </span>

<div class="method-description">

**Use Case:** Given a UMLS release, semantic type unique identifier
(TUI), semantic type relation label identifier (RUI), and related
semantic type unique identifier (TUI), this call returns the details of
the semantic type, the relation, and the related semantic type.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

mySemTyRelDTO = utsSemanticNetworkService.getSemanticTypeRelation
(ticket, umlsRelease, "T046", "T152","T037");\
\
 String relAbbr = mySemTyRelDTO.getRelationLabel().getAbbreviation();\
 String relDef = mySemTyRelDTO.getRelationLabel().getDefinition();\
 String relInvLabel =
mySemTyRelDTO.getRelationLabel().getInverseLabel();\
 String relTreeNum = mySemTyRelDTO.getRelationLabel().getTreeNumber();\
 String relUi = mySemTyRelDTO.getRelationLabel().getUi();\
 int relChildCnt = mySemTyRelDTO.getRelationLabel().getChildCount();\
 int relRelCnt = mySemTyRelDTO.getRelationLabel().getRelationCount();\
\
 String SemTypeAbbr =
mySemTyRelDTO.getRelatedSemanticType().getAbbreviation();\
 String SemTypeDef =
mySemTyRelDTO.getRelatedSemanticType().getDefinition();\
 String SemTypeTreeNum =
mySemTyRelDTO.getRelatedSemanticType().getTreeNumber();\
 String SemTypeUi = mySemTyRelDTO.getRelatedSemanticType().getUi();\
 String SemTypeVal = mySemTyRelDTO.getRelatedSemanticType().getValue();\
 String SemTypeUsage =
mySemTyRelDTO.getRelatedSemanticType().getUsageNote();\
 int SemTypeChildCnt =
mySemTyRelDTO.getRelatedSemanticType().getChildCount();\
 int SemTypeRelCnt =
mySemTyRelDTO.getRelatedSemanticType().getRelationCount();\

</div>

#### Sample Output:

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  RelationLabel Abbreviation: OC\
   RelationLabel Definition: Takes place in or happens under given conditions, circumstances, or time periods, or in a given location or population. This includes appears in, transpires, comes about, is present in, and exists in.\
   RelationLabel InverseLabel: has\_occurrence\
   RelationLabel Tree Number: R3.4\
   RelationLabel Ui: T152\
   RelationLabel Child Count: 1\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: inpo\
   RelatedSemanticType Definition: A traumatic wound, injury, or poisoning caused by an external agent or force.\
   RelatedSemanticType Tree Number: B2.3\
   RelatedSemanticType Ui: T037\
   RelatedSemanticType Value: Injury or Poisoning\
   RelatedSemanticType UsageNote: An \`Injury or Poisoning' is distinguished from a 'Disease or Syndrome' that may be a result of prolonged exposure to toxic materials.\
   RelatedSemanticType Child Count: 0\
   RelatedSemanticType Relation Count: 11\
  \
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

</div>

<div id="getAllSemanticTypeRelations"
class="method rounded-content-block">

**Method: **<span
class="method-name">getAllSemanticTypeRelations</span><span
class="method-parameters">(String ticket,String version)</span>
**Returns:** <span
class="method-return-type">ArrayList&lt;SemanticTypeRelationDTO&gt; </span>

<div class="method-description">

**Use Case:** Given a UMLS release, this call returns the details of all
semantic type relations that are valid for the release.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

myarrSemTyRelDTO = utsSemanticNetworkService.getAllSemanticTypeRelations
(ticket, umlsRelease);\
\
 for (int i = 0; i &lt; myarrSemTyRelDTO.size(); i++) {\
 SemanticTypeRelationDTO mySemTyRel = myarrSemTyRelDTO.get(i);\
 String relAbbr = mySemTyRel.getRelationLabel().getAbbreviation();\
 String relDef = mySemTyRel.getRelationLabel().getDefinition();\
 String relInvLabel = mySemTyRel.getRelationLabel().getInverseLabel();\
 String relTreeNum = mySemTyRel.getRelationLabel().getTreeNumber();\
 String relUi = mySemTyRel.getRelationLabel().getUi();\
 int relChildCnt = mySemTyRel.getRelationLabel().getChildCount();\
 int relRelCnt = mySemTyRel.getRelationLabel().getRelationCount();\
\
 String SemTypeAbbr =
mySemTyRel.getRelatedSemanticType().getAbbreviation();\
 String SemTypeDef =
mySemTyRel.getRelatedSemanticType().getDefinition();\
 String SemTypeTreeNum =
mySemTyRel.getRelatedSemanticType().getTreeNumber();\
 String SemTypeUi = mySemTyRel.getRelatedSemanticType().getUi();\
 String SemTypeVal = mySemTyRel.getRelatedSemanticType().getValue();\
 String SemTypeUsage =
mySemTyRel.getRelatedSemanticType().getUsageNote();\
 int SemTypeChildCnt =
mySemTyRel.getRelatedSemanticType().getChildCount();\
 int SemTypeRelCnt =
mySemTyRel.getRelatedSemanticType().getRelationCount();\
 }\

</div>

#### Sample Output:

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  RelationLabel Abbreviation: EV\
   RelationLabel Definition: Judgment of the value or degree of some attribute or process.\
   RelationLabel InverseLabel: has\_evaluation\
   RelationLabel Tree Number: R5.1\
   RelationLabel Ui: T161\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: acty\
   RelatedSemanticType Definition: An operation or series of operations that an organism or machine carries out or participates in.\
   RelatedSemanticType Tree Number: B1\
   RelatedSemanticType Ui: T052\
   RelatedSemanticType Value: Activity\
   RelatedSemanticType UsageNote: Few concepts will be assigned to this broad type. Wherever possible, one of the more specific types from this hierarchy will be chosen. For concepts assigned to this type, the focus of interest is on the activity. When the focus of interest is the individual or group that is carrying out the activity, then a type from the 'Behavior' hierarchy will be chosen. In general, concepts will not receive a type from both the 'Activity' and the 'Behavior' hierarchies.\
   RelatedSemanticType Child Count: 4\
   RelatedSemanticType Relation Count: 1\
  \
   RelationLabel Abbreviation: IS\
   RelationLabel Definition: The basic hierarchical link in the Network. If one item "isa" another item then the first item is more specific in meaning than the second item.\
   RelationLabel InverseLabel: inverse\_isa\
   RelationLabel Tree Number: H\
   RelationLabel Ui: T186\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: idcn\
   RelatedSemanticType Definition: An abstract concept, such as a social, religious or philosophical concept.\
   RelatedSemanticType Tree Number: A2.1\
   RelatedSemanticType Ui: T078\
   RelatedSemanticType Value: Idea or Concept\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 5\
   RelatedSemanticType Relation Count: 3\
  \
   RelationLabel Abbreviation: ME\
   RelationLabel Definition: The dimension, quantity, or capacity determined by measuring.\
   RelationLabel InverseLabel: has\_measurement\
   RelationLabel Tree Number: R5.4\
   RelationLabel Ui: T182\
   RelationLabel Child Count: 0\
   RelationLabel Relation Count: 0\
   RelatedSemanticType Abbreviation: phsf\
   RelatedSemanticType Definition: A normal process, activity, or state of the body.\
   RelatedSemanticType Tree Number: B2.2.1.1\
   RelatedSemanticType Ui: T039\
   RelatedSemanticType Value: Physiologic Function\
   RelatedSemanticType UsageNote: NULL\
   RelatedSemanticType Child Count: 4\
   RelatedSemanticType Relation Count: 5\
  \
   and so on....
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

</div>

<div id="getSemanticNetworkRelationLabel"
class="method rounded-content-block">

**Method: **<span
class="method-name">getSemanticNetworkRelationLabel</span><span
class="method-parameters">(String ticket,String version,String
semanticTypeId)</span>
**Returns:** <span
class="method-return-type">SemanticNetworkRelationLabelDTO </span>

<div class="method-description">

**Use Case:** Given a UMLS release and semantic network relation unique
identifier (UI), this call returns the name (label) of the semantic
network relation. In addition, returns child count, inverse label,
relation count, tree number, identifier (ui), abbreviation, and
definition for the given semantic network relation.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

mySemTyRelDTO =
utsSemanticNetworkService.getSemanticNetworkRelationLabel (ticket,
umlsRelease, "T172");\
\
 String abbreviation = mySemTyRelDTO.getAbbreviation();\
 String definition = mySemTyRelDTO.getDefinition();\
 int childCnt = mySemTyRelDTO.getChildCount();\
 int relCnt = mySemTyRelDTO.getRelationCount();\
 String treeNum = mySemTyRelDTO.getTreeNumber();\
 String ui = mySemTyRelDTO.getUi();\
 String value = mySemTyRelDTO.getValue();\

</div>

#### Sample Input (C♯):

<div class="input rounded-content-block">

utsSemanticNetwork.getSemanticType(ticket, "2011AB", "T121");

</div>

#### Sample Output:

+--------------------------------------------------------------------------+
|   Abbreviation   Definition                                              |
|                                                                          |
|  Child Count   Inverse Label   Ui     Label                              |
|   -------------- ------------------------------------------------------- |
| ------------------------------------------------------------------------ |
|  ------------- --------------- ------ --------------                     |
|   CS             Is structurally made up of in whole or in part of some  |
| material or matter. This includes composed of, made of, and formed of.   |
|  0             constitutes     T172   consists\_of                       |
+--------------------------------------------------------------------------+

</div>

<div id="getAllSemanticNetworkRelationLabels "
class="method rounded-content-block">

**Method: **<span
class="method-name">getAllSemanticNetworkRelationLabels </span><span
class="method-parameters">(String ticket,String version)</span>
**Returns:** <span
class="method-return-type">ArrayList&lt;SemanticNetworkRelationLabelDTO&gt; </span>

<div class="method-description">

**Use Case:** Given a UMLS release, this call returns all the semantic
network relation labels for the release. For each semantic network
relation, this call returns an object with fields for child count,
definition, inverse label, relation count, tree number, identifier (ui),
and abbreviation for each semantic network relation.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

myarrSemTyRelDTO =
utsSemanticNetworkService.getAllSemanticNetworkRelationLabels ticket,
umlsRelease);\
\
 for (int i = 0; i &lt; myarrSemTyRelDTO.size(); i++) {\
 SemanticNetworkRelationLabelDTO mySemTyRel = myarrSemTyRelDTO.get(i);\
 String abbreviation = mySemTyRel.getAbbreviation();\
 String definition = mySemTyRel.getDefinition();\
 int childCnt = mySemTyRel.getChildCount();\
 int relCnt = mySemTyRel.getRelationCount();\
 String example = mySemTyRel.getExample();\
 String inverseLabel = mySemTyRel.getInverseLabel();\
 String treeNum = mySemTyRel.getTreeNumber();\
 String ui = mySemTyRel.getUi();\
 String label = mySemTyRel.getLabel();\
 }\

</div>

#### Sample Input (C♯):

<div class="input rounded-content-block">

utsSemanticNetwork.getSemanticType(ticket, "2011AB", "T121");

</div>

#### Sample Output:

+--------------------------------------------------------------------------+
|   Abbreviation   Definition                                              |
|                                                                          |
|                                                                          |
|                                                                          |
|                          Child Count   Inverse Label               Ui    |
|   Label                                                                  |
|   -------------- ------------------------------------------------------- |
| ------------------------------------------------------------------------ |
| ------------------------------------------------------------------------ |
| ------------------------------------------------------------------------ |
| ------------------------ ------------- --------------------------- ----- |
| - ---------------------------                                            |
|   AD             Close to, near or abutting another physical unit with n |
| o other structure of the same kind intervening. This includes adjoins, a |
| buts, is contiguous to, is juxtaposed, and is close to.                  |
|                                                                          |
|                          0             adjacent\_to                T173  |
|   adjacent\_to                                                           |
|   AE             Analyzes the influence or consequences of the function  |
| or action of.                                                            |
|                                                                          |
|                                                                          |
|                          0             assessed\_for\_effect\_by   T164  |
|   assesses\_effect\_of                                                   |
|   AF             Produces a direct effect on. Implied here is the alteri |
| ng or influencing of an existing condition, state, situation, or entity. |
|  This includes has a role in, alters, influences, predisposes, catalyzes |
| , stimulates, regulates, depresses, impedes, enhances, contributes to, l |
| eads to, and modifies.   6             affected\_by                T151  |
|   affects                                                                |
|   AN             Studies or examines using established quantitative or q |
| ualitative methods.                                                      |
|                                                                          |
|                                                                          |
|                          1             analyzed\_by                T193  |
|   analyzes                                                               |
|   AW             has a significant or salient relationship to.           |
|                                                                          |
|                                                                          |
|                                                                          |
|                          5             associated\_with            T166  |
|   associated\_with                                                       |
|   BA             Acts on or influences an entity.                        |
|                                                                          |
|                                                                          |
|                                                                          |
|                          2             brought\_about\_by          T187  |
|   brings\_about                                                          |
|   BR             Arises from the division of. For example, the arborizat |
| ion of arteries.                                                         |
|                                                                          |
|                                                                          |
|                          0             has\_branch                 T198  |
|   branch\_of                                                             |
|   CA             Brings about a condition or an effect. Implied here is  |
| that an agent, such as for example, a pharmacologic substance or an orga |
| nism, has brought about the effect. This includes induces, effects, evok |
| es, and etiology.                                                        |
|                          0             caused\_by                  T147  |
|   causes                                                                 |
|   CM             Causes to become more severe or complex or results in a |
| dverse effects.                                                          |
|                                                                          |
|                                                                          |
|                          0             complicated\_by             T149  |
|   complicates                                                            |
|   CN             Directly attached to another physical unit as tendons a |
| re connected to muscles. This includes attached to and anchored to.      |
|                                                                          |
|                                                                          |
|                          0             connected\_to               T174  |
|   connected\_to                                                          |
|   CO             Executes a function or performs a procedure or activity |
| . This includes transacts, operates on, handles, and executes.           |
|                                                                          |
|                                                                          |
|                          0             carried\_out\_by            T141  |
|   carries\_out                                                           |
|   CP             Conceptually a portion, division, or component of some  |
| larger whole.                                                            |
|                                                                          |
|                                                                          |
|                          0             has\_conceptual\_part       T160  |
|   conceptual\_part\_of                                                   |
|   CR             Related by some abstract concept, thought, or idea.     |
|                                                                          |
|                                                                          |
|                                                                          |
|                          12            conceptually\_related\_to   T158  |
|   conceptually\_related\_to                                              |
|   CS             Is structurally made up of in whole or in part of some  |
| material or matter. This includes composed of, made of, and formed of.   |
|                                                                          |
|                                                                          |
|                          0             constitutes                 T172  |
|   consists\_of                                                           |
|   CT             Holds or is the receptacle for fluids or other substanc |
| es. This includes is filled with, holds, and is occupied by.             |
|                                                                          |
|                                                                          |
|                          0             contained\_in               T134  |
|   contains                                                               |
|   CW             Occurs at the same time as, together with, or jointly.  |
| This includes is co-incident with, is concurrent with, is contemporaneou |
| s with, accompanies, coexists with, and is concomitant with.             |
|                                                                          |
|                          0             co-occurs\_with             T137  |
|   co-occurs\_with                                                        |
|   DE             The relative intensity of a process or the relative int |
| ensity or amount of a quality or attribute.                              |
|                                                                          |
|                                                                          |
|                          0             has\_degree                 T180  |
|   degree\_of                                                             |
|   DF             An earlier stage in the individual maturation of.       |
|                                                                          |
|                                                                          |
|                                                                          |
|                          0             has\_developmental\_form    T179  |
|   developmental\_form\_of                                                |
|   DI             Distinguishes or identifies the nature or characteristi |
| cs of.                                                                   |
|                                                                          |
|                                                                          |
|                          0             diagnosed\_by               T163  |
|   diagnoses                                                              |
|   DO             In chemistry, a substance structurally related to anoth |
| er or that can be made from the other substance. This is used only for s |
| tructural relationships. This does not include functional relationships  |
| such as metabolite of, by product of, nor analog of.                     |
|                          0             has\_derivative             T178  |
|   derivative\_of                                                         |
|   DS             Alters or influences an already existing condition, sta |
| te, or situation. Produces a negative effect on.                         |
|                                                                          |
|                                                                          |
|                          0             disrupted\_by               T146  |
|   disrupts                                                               |
|   EV             Judgment of the value or degree of some attribute or pr |
| ocess.                                                                   |
|                                                                          |
|                                                                          |
|                          0             has\_evaluation             T161  |
|   evaluation\_of                                                         |
|   EX             Shows or demonstrates.                                  |
|                                                                          |
|                                                                          |
|                                                                          |
|                          0             exhibited\_by               T145  |
|   exhibits                                                               |
|   FR             Related by the carrying out of some function or activit |
| y.                                                                       |
|                                                                          |
|                                                                          |
|                          8             functionally\_related\_to   T139  |
|   functionally\_related\_to                                              |
|   IC             Serves to link or join together two or more other physi |
| cal units. This includes joins, links, conjoins, articulates, separates, |
|  and bridges.                                                            |
|                                                                          |
|                          0             interconnected\_by          T175  |
|   interconnects                                                          |
|   IG             Is a component of, as in a constituent of a preparation |
| .                                                                        |
|                                                                          |
|                                                                          |
|                          0             has\_ingredient             T202  |
|   ingredient\_of                                                         |
|   II             Is an issue in or a point of discussion, study, debate, |
|  or dispute.                                                             |
|                                                                          |
|                                                                          |
|                          0             has\_issue                  T165  |
|   issue\_in                                                              |
|   IN             Gives evidence for the presence at some time of an enti |
| ty or process.                                                           |
|                                                                          |
|                                                                          |
|                          0             indicated\_by               T156  |
|   indicates                                                              |
|   IS             The basic hierarchical link in the Network. If one item |
|  "isa" another item then the first item is more specific in meaning than |
|  the second item.                                                        |
|                                                                          |
|                          0             inverse\_isa                T186  |
|   isa                                                                    |
|   IW             Acts, functions, or operates together with.             |
|                                                                          |
|                                                                          |
|                                                                          |
|                          0             interacts\_with             T142  |
|   interacts\_with                                                        |
|   LO             The position, site, or region of an entity or the site  |
| of a process.                                                            |
|                                                                          |
|                                                                          |
|                          0             has\_location               T135  |
|   location\_of                                                           |
|   ME             The dimension, quantity, or capacity determined by meas |
| uring.                                                                   |
|                                                                          |
|                                                                          |
|                          0             has\_measurement            T182  |
|   measurement\_of                                                        |
|   MF             That part of a phenomenon which is directly observable  |
| or concretely or visibly expressed, or which gives evidence to the under |
| lying process. This includes expression of, display of, and exhibition o |
| f.                                                                       |
|                          0             has\_manifestation          T150  |
|   manifestation\_of                                                      |
|   MN             Administers, or contributes to the care of an individua |
| l or group of individuals.                                               |
|                                                                          |
|                                                                          |
|                          0             managed\_by                 T153  |
|   manages                                                                |
|   MS             Ascertains or marks the dimensions, quantity, degree, o |
| r capacity of.                                                           |
|                                                                          |
|                                                                          |
|                          0             measured\_by                T162  |
|   measures                                                               |
|   MT             The manner and sequence of events in performing an act  |
| or procedure.                                                            |
|                                                                          |
|                                                                          |
|                          0             has\_method                 T183  |
|   method\_of                                                             |
|   OC             Takes place in or happens under given conditions, circu |
| mstances, or time periods, or in a given location or population. This in |
| cludes appears in, transpires, comes about, is present in, and exists in |
| .                                                                        |
|                          1             has\_occurrence             T152  |
|   occurs\_in                                                             |
|   PA             Performs habitually or customarily.                     |
|                                                                          |
|                                                                          |
|                                                                          |
|                          0             practiced\_by               T143  |
|   practices                                                              |
|   PC             Occurs earlier in time. This includes antedates, comes  |
| before, is in advance of, predates, and is prior to.                     |
|                                                                          |
|                                                                          |
|                          0             follows                     T138  |
|   precedes                                                               |
|   PE             Executes, accomplishes, or achieves an activity.        |
|                                                                          |
|                                                                          |
|                                                                          |
|                          3             performed\_by               T188  |
|   performs                                                               |
|   PO             Action, function, or state of.                          |
|                                                                          |
|                                                                          |
|                                                                          |
|                          0             has\_process                T140  |
|   process\_of                                                            |
|   PP             Characteristic of, or quality of.                       |
|                                                                          |
|                                                                          |
|                                                                          |
|                          0             has\_property               T159  |
|   property\_of                                                           |
|   PR             Related by virtue of some physical attribute or charact |
| eristic.                                                                 |
|                                                                          |
|                                                                          |
|                          8             physically\_related\_to     T132  |
|   physically\_related\_to                                                |
|   PS             Brings forth, generates or creates. This includes yield |
| s, secretes, emits, biosynthesizes, generates, releases, discharges, and |
|  creates.                                                                |
|                                                                          |
|                          0             produced\_by                T144  |
|   produces                                                               |
|   PT             Composes, with one or more other physical units, some l |
| arger whole. This includes component of, division of, portion of, fragme |
| nt of, section of, and layer of.                                         |
|                                                                          |
|                          0             has\_part                   T133  |
|   part\_of                                                               |
|   PV             Stops, hinders or eliminates an action or condition.    |
|                                                                          |
|                                                                          |
|                                                                          |
|                          0             prevented\_by               T148  |
|   prevents                                                               |
|   RO             The condition, product, or state occurring as a consequ |
| ence, effect, or conclusion of an activity or process. This includes pro |
| duct of, effect of, sequel of, outcome of, culmination of, and completio |
| n of.                                                                    |
|                          0             has\_result                 T157  |
|   result\_of                                                             |
|   SP             Related by place or region.                             |
|                                                                          |
|                                                                          |
|                                                                          |
|                          4             spatially\_related\_to      T189  |
|   spatially\_related\_to                                                 |
|   SR             Establishes the boundaries for, or defines the limits o |
| f another physical structure. This includes limits, bounds, confines, en |
| closes, and circumscribes.                                               |
|                                                                          |
|                          0             surrounded\_by              T176  |
|   surrounds                                                              |
|   TB             Merges with. For example, the confluence of veins.      |
|                                                                          |
|                                                                          |
|                                                                          |
|                          0             has\_tributary              T199  |
|   tributary\_of                                                          |
|   TR             Related in time by preceding, co-occuring with, or foll |
| owing.                                                                   |
|                                                                          |
|                                                                          |
|                          2             temporally\_related\_to     T136  |
|   temporally\_related\_to                                                |
|   TS             Applies a remedy with the object of effecting a cure or |
|  managing a condition.                                                   |
|                                                                          |
|                                                                          |
|                          0             treated\_by                 T154  |
|   treats                                                                 |
|   TV             Crosses or extends across another physical structure or |
|  area. This includes crosses over and crosses through.                   |
|                                                                          |
|                                                                          |
|                          0             traversed\_by               T177  |
|   traverses                                                              |
|   US             Employs in the carrying out of some activity. This incl |
| udes applies, utilizes, employs, and avails.                             |
|                                                                          |
|                                                                          |
|                          0             used\_by                    T155  |
|   uses                                                                   |
+--------------------------------------------------------------------------+

</div>

<div id="getSemanticNetworkRelationLabelRelations"
class="method rounded-content-block">

**Method: **<span
class="method-name">getSemanticNetworkRelationLabelRelations</span><span
class="method-parameters">(String ticket,String version,String
semanticTypeId)</span>
**Returns:** <span
class="method-return-type">ArrayList&lt;SemanticNetworkRelationLabelRelationDTO&gt; </span>

<div class="method-description">

**Use Case:** Given a UMLS release and a semantic network relation label
identifier (ui or handle), this call returns the semantic network
relations to which the given semantic network relation is related, as
well as the relation that links the related semantic network relations.
For example, the semantic network relation "affects" is related to the
semantic network relation "functionally\_related\_to" by the "isa"
relation. In other words: affects isa functionally\_related\_to.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

myarrSemNetRelLabel =
utsSemanticNetworkService.getSemanticNetworkRelationLabelRelations
(ticket, umlsRelease, "T151");\
\
 for (int i = 0; i &lt; myarrSemNetRelLabel.size(); i++) {\
 SemanticNetworkRelationLabelRelationDTO mySemTyRel =
myarrSemNetRelLabel.get(i);\
 String handle = mySemTyRel.getHandle();\
 String SnRelLabAbbr =
mySemTyRel.getSnRelationLabel().getAbbreviation();\
 String SNRelLabAbbr =
mySemTyRel.getRelatedSNRelationLabel().getAbbreviation();\
 String abbreviation = mySemTyRel.getRelationLabel().getAbbreviation();\
 String definition = mySemTyRel.getRelationLabel().getDefinition();\
 String InvLabel = mySemTyRel.getRelationLabel().getInverseLabel();\
 String Ui = mySemTyRel.getRelationLabel().getUi();\
 int ChildCnt = mySemTyRel.getRelationLabel().getChildCount();\
 }\

</div>

#### Sample Input (C♯):

<div class="input rounded-content-block">

utsSemanticNetwork.getSemanticType(ticket, "2011AB", "T121");

</div>

#### Sample Output:

+--------------------------------------------------------------------------+
|   Handle                             SN RelationLabel Abbreviation   Rel |
| ated SN RelationLabel Abbreviation   Abbreviation   Definition           |
|                                                                          |
|                                                        Inverse Label   U |
| i     Child Count                                                        |
|   ---------------------------------- ------------------------------- --- |
| ------------------------------------ -------------- -------------------- |
| ------------------------------------------------------------------------ |
| ------------------------------------------------------ --------------- - |
| ----- -------------                                                      |
|   71499d9a764563ac2f031df67b82e901   AF                              FR  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
+--------------------------------------------------------------------------+

</div>

<div id="getSemanticNetworkRelationLabelRelationsForPair"
class="method rounded-content-block">

**Method: **<span
class="method-name">getSemanticNetworkRelationLabelRelationsForPair</span><span
class="method-parameters">(String ticket,String version,String
semanticTypeId,String relatedSemanticTypeId)</span>
**Returns:** <span
class="method-return-type">ArrayList&lt;SemanticNetworkRelationLabelRelationDTO&gt; </span>

<div class="method-description">

**Use Case:** Given a UMLS release and semantic network relation label
identifiers for a pair of semantic network relations, this call returns
details for the semantic network links between the two given semantic
network relations as well as details for each given semantic network
relation.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

myarrSemNetRelLabel =
utsSemanticNetworkService.getSemanticNetworkRelationLabelRelationsForPair
(ticket, umlsRelease, "T151", "T139");\
\
 for (int i = 0; i &lt; myarrSemNetRelLabel.size(); i++) {\
 SemanticNetworkRelationLabelRelationDTO mySemTyRel =
myarrSemNetRelLabel.get(i);\
 String handle = mySemTyRel.getHandle();\
 String SnRelLabAbbr =
mySemTyRel.getSnRelationLabel().getAbbreviation();\
 String SNRelLabAbbr =
mySemTyRel.getRelatedSNRelationLabel().getAbbreviation();\
 String abbreviation = mySemTyRel.getRelationLabel().getAbbreviation();\
 String definition = mySemTyRel.getRelationLabel().getDefinition();\
 String InvLabel = mySemTyRel.getRelationLabel().getInverseLabel();\
 String Ui = mySemTyRel.getRelationLabel().getUi();\
 int ChildCnt = mySemTyRel.getRelationLabel().getChildCount();\
 }\

</div>

#### Sample Input (C♯):

<div class="input rounded-content-block">

utsSemanticNetwork.getSemanticType(ticket, "2011AB", "T121");

</div>

#### Sample Output:

+--------------------------------------------------------------------------+
|   Handle                             SN RelationLabel Abbreviation   Rel |
| ated SN RelationLabel Abbreviation   Abbreviation   Definition           |
|                                                                          |
|                                                        Inverse Label   U |
| i     Child Count                                                        |
|   ---------------------------------- ------------------------------- --- |
| ------------------------------------ -------------- -------------------- |
| ------------------------------------------------------------------------ |
| ------------------------------------------------------ --------------- - |
| ----- -------------                                                      |
|   71499d9a764563ac2f031df67b82e901   AF                              FR  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
+--------------------------------------------------------------------------+

</div>

<div id="getInverseSemanticNetworkRelationLabelRelations"
class="method rounded-content-block">

**Method: **<span
class="method-name">getInverseSemanticNetworkRelationLabelRelations</span><span
class="method-parameters">(String ticket,String version,String
semanticTypeId)</span>
**Returns:** <span
class="method-return-type">ArrayList&lt;SemanticNetworkRelationLabelRelationDTO&gt; </span>

<div class="method-description">

**Use Case:** Given a UMLS release and a semantic network relation
identifier (ui or handle), this call returns details for the semantic
network inverse relation that connects the specified semantic network
relation with some other semantic network relation.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

myarrSemNetRelLabel =
utsSemanticNetworkService.getInverseSemanticNetworkRelationLabelRelations
(ticket, umlsRelease, "T151");\
\
 for (int i = 0; i &lt; myarrSemNetRelLabel.size(); i++) {\
 SemanticNetworkRelationLabelRelationDTO mySemTyRel =
myarrSemNetRelLabel.get(i);\
 String handle = mySemTyRel.getHandle();\
 String SnRelLabAbbr =
mySemTyRel.getSnRelationLabel().getAbbreviation();\
 String SNRelLabAbbr =
mySemTyRel.getRelatedSNRelationLabel().getAbbreviation();\
 String abbreviation = mySemTyRel.getRelationLabel().getAbbreviation();\
 String definition = mySemTyRel.getRelationLabel().getDefinition();\
 String InvLabel = mySemTyRel.getRelationLabel().getInverseLabel();\
 String Ui = mySemTyRel.getRelationLabel().getUi();\
 int ChildCnt = mySemTyRel.getRelationLabel().getChildCount();\
 }\

</div>

#### Sample Input (C♯):

<div class="input rounded-content-block">

utsSemanticNetwork.getSemanticType(ticket, "2011AB", "T121");

</div>

#### Sample Output:

+--------------------------------------------------------------------------+
|   Handle                             SN RelationLabel Abbreviation   Rel |
| ated SN RelationLabel Abbreviation   Abbreviation   Definition           |
|                                                                          |
|                                                        Inverse Label   U |
| i     Child Count                                                        |
|   ---------------------------------- ------------------------------- --- |
| ------------------------------------ -------------- -------------------- |
| ------------------------------------------------------------------------ |
| ------------------------------------------------------ --------------- - |
| ----- -------------                                                      |
|   b44702522eca54df20ff780adbc1cc17   CM                              AF  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   c13827e3fb42b0dcb272a40fd949ae22   DS                              AF  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   aa2f1ea24dad61c9f8cb91c0d2775daa   IW                              AF  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   cb7e3d604d0b5b7f5a4dcb29ba83fd5c   MN                              AF  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   a69e5fe71c8f41672af6d680a25bd71f   PV                              AF  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   afd778a733e0da310bcc141a1314c1fa   TS                              AF  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
+--------------------------------------------------------------------------+

</div>

<div id="getInheritedSemanticNetworkRelationLabelRelations"
class="method rounded-content-block">

**Method: **<span
class="method-name">getInheritedSemanticNetworkRelationLabelRelations</span><span
class="method-parameters">(String ticket,String version,String
semanticTypeId)</span>
**Returns:** <span
class="method-return-type">ArrayList&lt;SemanticNetworkRelationLabelRelationDTO&gt; </span>

<div class="method-description">

**Use Case:** Given a UMLS release and a semantic network relation
identifier (ui or handle), this call returns details for the inherited
semantic network relations that connect the given relation with some
other semantic network relation.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

myarrSemNetRelLabel =
utsSemanticNetworkService.getInheritedSemanticNetworkRelationLabelRelations
(ticket, umlsRelease, "T143");\
\
 for (int i = 0; i &lt; myarrSemNetRelLabel.size(); i++) {\
 SemanticNetworkRelationLabelRelationDTO mySemTyRel =
myarrSemNetRelLabel.get(i);\
 String handle = mySemTyRel.getHandle();\
 String SnRelLabAbbr =
mySemTyRel.getSnRelationLabel().getAbbreviation();\
 String SNRelLabAbbr =
mySemTyRel.getRelatedSNRelationLabel().getAbbreviation();\
 String abbreviation = mySemTyRel.getRelationLabel().getAbbreviation();\
 String definition = mySemTyRel.getRelationLabel().getDefinition();\
 String InvLabel = mySemTyRel.getRelationLabel().getInverseLabel();\
 String Ui = mySemTyRel.getRelationLabel().getUi();\
 int ChildCnt = mySemTyRel.getRelationLabel().getChildCount();\
 }\

</div>

#### Sample Input (C♯):

<div class="input rounded-content-block">

utsSemanticNetwork.getSemanticType(ticket, "2011AB", "T121");

</div>

#### Sample Output:

+--------------------------------------------------------------------------+
|   Handle                             SN RelationLabel Abbreviation   Rel |
| ated SN RelationLabel Abbreviation   Abbreviation   Definition           |
|                                                                          |
|                                                        Inverse Label   U |
| i     Child Count                                                        |
|   ---------------------------------- ------------------------------- --- |
| ------------------------------------ -------------- -------------------- |
| ------------------------------------------------------------------------ |
| ------------------------------------------------------ --------------- - |
| ----- -------------                                                      |
|   c63f6997ee39040d8d9fe733ce5d4ec2   PA                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   be24d16ca1801addc06305e6fc985d71   PA                              FR  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
+--------------------------------------------------------------------------+

</div>

<div id="getInverseInheritedSemanticNetworkRelationLabelRelations"
class="method rounded-content-block">

**Method: **<span
class="method-name">getInverseInheritedSemanticNetworkRelationLabelRelations</span><span
class="method-parameters">(String ticket,String version,String
semanticTypeId)</span>
**Returns:** <span
class="method-return-type">ArrayList&lt;SemanticNetworkRelationLabelRelationDTO&gt; </span>

<div class="method-description">

**Use Case:** Given a UMLS release and a semantic network relation
identifier (ui or handle), this call returns details for inverse
inherited semantic network relations that connect the given relation
with some other semantic network relation.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

myarrSemNetRelLabel =
utsSemanticNetworkService.getInverseInheritedSemanticNetworkRelationLabelRelations
(ticket, umlsRelease, "T166");\
\
 for (int i = 0; i &lt; myarrSemNetRelLabel.size(); i++) {\
 SemanticNetworkRelationLabelRelationDTO mySemTyRel =
myarrSemNetRelLabel.get(i);\
 String handle = mySemTyRel.getHandle();\
 String SnRelLabAbbr =
mySemTyRel.getSnRelationLabel().getAbbreviation();\
 String SNRelLabAbbr =
mySemTyRel.getRelatedSNRelationLabel().getAbbreviation();\
 String abbreviation = mySemTyRel.getRelationLabel().getAbbreviation();\
 String definition = mySemTyRel.getRelationLabel().getDefinition();\
 String InvLabel = mySemTyRel.getRelationLabel().getInverseLabel();\
 String Ui = mySemTyRel.getRelationLabel().getUi();\
 int ChildCnt = mySemTyRel.getRelationLabel().getChildCount();\
 }\

</div>

#### Sample Input (C♯):

<div class="input rounded-content-block">

utsSemanticNetwork.getSemanticType(ticket, "2011AB", "T121");

</div>

#### Sample Output:

+--------------------------------------------------------------------------+
|   Handle                             SN RelationLabel Abbreviation   Rel |
| ated SN RelationLabel Abbreviation   Abbreviation   Definition           |
|                                                                          |
|                                                        Inverse Label   U |
| i     Child Count                                                        |
|   ---------------------------------- ------------------------------- --- |
| ------------------------------------ -------------- -------------------- |
| ------------------------------------------------------------------------ |
| ------------------------------------------------------ --------------- - |
| ----- -------------                                                      |
|   78dc3f612de046758bf7256a1901e448   PT                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   c31bbdfdb0ca68ff22448e7194235904   CT                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   3474989f9d43d0c24e5c414325cd696e   LO                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   7f11af6f612d2f22c0ec858aebcdfb54   CW                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   0b5fad6b2d812079b1aad932409219bd   PC                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   bce5177af45b51baab22f3876bbcb3cb   PO                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   a26521f0ddba69ce35b3a7b15f88625c   CO                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   96cbade160f6b305e0faf4f242b168f9   IW                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   c63f6997ee39040d8d9fe733ce5d4ec2   PA                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   878a160b1c22112f87b62f435ec05d68   PS                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   9fa14606d03b33878170bdb658d14849   EX                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   6654c22a93b68d9c09cd7c0ac0625360   DS                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   0cf3947dc51d9730805e3a8b9d0283ef   CA                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   d52aae2fde97e2e6a931214f24f5ddb9   PV                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   4e7738e3598bda4425b48171504a747e   CM                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   d0b2f41c066e87c91239ceda34f11aa0   MF                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   95db43ee5aeed0b8334a1b6c802cc5a9   AF                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   bbc711cbbb65cbdbc483d48902530c17   OC                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   96390509b7ac973425b08b013e7fc301   MN                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   531da4526406a54860d27d00da463b08   TS                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   44c79f97d40f6288bc6a0a17044c684d   US                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   b83e9bc9bb8f7221b14ea40aced81104   IN                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   704002dca0285afbb806939e991001c8   RO                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   b49a0b57be0cf75623ef5a81306bffe2   PP                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   0582f7e6dac54c4b9de6f61c49f06c57   CP                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   abdd8217c0f0e3eb03192bd0688eec75   EV                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   91cb106b55eb1a28dfa505f07ca82e9d   MS                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   1267f300b4a6383f7ec5cb8585be4f1a   DI                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   fe5cc5e1a73d3a721a67cd6d2ef24a99   AE                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   eb3140606fe773625686aa68e4cf5e8d   II                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   2eb32433db19fb74e476b041dc962d97   CS                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   88dcba9d4f7c999c0290ad2c1d49ab09   AD                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   50466fa6832a2918ec25f34dff202565   CN                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   3046e2d0d726612e69192df952d9adf4   IC                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   d65280dc24c9c44e59280066770472e9   SR                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   ede1215379ae0001a0536a03b122ed0a   TV                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   f41366e22783674a7ff1d3ee2b662586   DO                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   9fea0b78a42c8f5167572cca82b564ff   DF                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   b0b365a3e9df9407db4ac98e3aaf6803   DE                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   833ee41587aeda71d6aa7e309bd85c36   ME                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   36d840464a2514eabc8a89db64193df2   MT                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   dd11ec23f604dc6c376ebc3054c56e09   BA                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   e49a54b6e760eb5323fdb12e66754119   PE                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   679abbb93256ab98ad689fdb20f4742a   AN                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   1020000c4a91fd3f49be9b249a5c1f1b   BR                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   5a8b09d93441c9c758c28d6a71deafff   TB                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   6a35ba6be05c99c7e0ba3a4d5d334072   IG                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
+--------------------------------------------------------------------------+

</div>

<div id="getSemanticNetworkRelationLabelRelation"
class="method rounded-content-block">

**Method: **<span
class="method-name">getSemanticNetworkRelationLabelRelation</span><span
class="method-parameters">(String ticket,String version,String
semanticTypeId,String semanticRelationLabelId,String
relatedSemanticTypeId)</span>
**Returns:** <span
class="method-return-type">SemanticNetworkRelationLabelRelationDTO </span>

<div class="method-description">

**Use Case:** Given a UMLS release and a pair of semantic network
relation identifiers and a relation identifier that links the two given
semantic network relations, this call returns the details of the pair of
semantic network relations as well as details of the relation that links
the two semantic network relations.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

mySemNetRelLabel =
utsSemanticNetworkService.getSemanticNetworkRelationLabelRelation
(ticket, umlsRelease, "T151", "T186", "T139");\
\
 String handle = mySemNetRelLabel.getHandle();\
 String SnRelLabAbbr =
mySemNetRelLabel.getSnRelationLabel().getAbbreviation();\
 String SNRelLabAbbr =
mySemNetRelLabel.getRelatedSNRelationLabel().getAbbreviation();\
 String abbreviation =
mySemNetRelLabel.getRelationLabel().getAbbreviation();\
 String definition =
mySemNetRelLabel.getRelationLabel().getDefinition();\
 String InvLabel =
mySemNetRelLabel.getRelationLabel().getInverseLabel();\
 String Ui = mySemNetRelLabel.getRelationLabel().getUi();\
 int ChildCnt = mySemNetRelLabel.getRelationLabel().getChildCount();\

</div>

#### Sample Input (C♯):

<div class="input rounded-content-block">

utsSemanticNetwork.getSemanticType(ticket, "2011AB", "T121");

</div>

#### Sample Output:

+--------------------------------------------------------------------------+
|   Handle                             SN RelationLabel Abbreviation   Rel |
| ated SN RelationLabel Abbreviation   Abbreviation   Definition           |
|                                                                          |
|                                                        Inverse Label   U |
| i     Child Count                                                        |
|   ---------------------------------- ------------------------------- --- |
| ------------------------------------ -------------- -------------------- |
| ------------------------------------------------------------------------ |
| ------------------------------------------------------ --------------- - |
| ----- -------------                                                      |
|   71499d9a764563ac2f031df67b82e901   AF                              FR  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
+--------------------------------------------------------------------------+

</div>

<div id="getAllSemanticNetworkRelationLabelRelations "
class="method rounded-content-block">

**Method: **<span
class="method-name">getAllSemanticNetworkRelationLabelRelations
</span><span class="method-parameters">(String ticket,String
version)</span>
**Returns:** <span
class="method-return-type">ArrayList&lt;SemanticNetworkRelationLabelRelationDTO&gt; </span>

<div class="method-description">

**Use Case:** Given a UMLS release, this call returns all the sets of
semantic network relation triples for the release. A triple of semantic
network relations contains details for two semantic network relations
that are linked by a third semantic network relation. For example,
\["adjacent\_to" isa "spatially\_related\_to,"\] where "isa" is the
linking semantic relation. Another example: \["analyzes" isa
"assesses\_effect\_of"\] where "isa" is the linking semantic relation.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

myarrSemNetRelLabel =
utsSemanticNetworkService.getAllSemanticNetworkRelationLabelRelations
(ticket, umlsRelease);\
\
 for (int i = 0; i &lt; myarrSemNetRelLabel.size(); i++) {\
 SemanticNetworkRelationLabelRelationDTO mySemTyRel =
myarrSemNetRelLabel.get(i);\
 String handle = mySemTyRel.getHandle();\
 String SnRelLabAbbr =
mySemTyRel.getSnRelationLabel().getAbbreviation();\
 String SNRelLabAbbr =
mySemTyRel.getRelatedSNRelationLabel().getAbbreviation();\
 String abbreviation = mySemTyRel.getRelationLabel().getAbbreviation();\
 String definition = mySemTyRel.getRelationLabel().getDefinition();\
 String InvLabel = mySemTyRel.getRelationLabel().getInverseLabel();\
 String Ui = mySemTyRel.getRelationLabel().getUi();\
 int ChildCnt = mySemTyRel.getRelationLabel().getChildCount();\
 }\

</div>

#### Sample Input (C♯):

<div class="input rounded-content-block">

utsSemanticNetwork.getSemanticType(ticket, "2011AB", "T121");

</div>

#### Sample Output:

+--------------------------------------------------------------------------+
|   Handle                             SN RelationLabel Abbreviation   Rel |
| ated SN RelationLabel Abbreviation   Abbreviation   Definition           |
|                                                                          |
|                                                        Inverse Label   U |
| i     Child Count                                                        |
|   ---------------------------------- ------------------------------- --- |
| ------------------------------------ -------------- -------------------- |
| ------------------------------------------------------------------------ |
| ------------------------------------------------------ --------------- - |
| ----- -------------                                                      |
|   0e8e4c3625252a258987308567f24224   AD                              SP  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   4f0ff99d2bb08e5f4ecdb8a2db4b2b22   AE                              AN  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   71499d9a764563ac2f031df67b82e901   AF                              FR  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   efab43f1ea5320954f22abe0fda31f38   AN                              CR  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   b01081fc200c12fba5f90e2984f1216b   BA                              FR  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   ff1a3ba192aada741f41c1c5af679528   BR                              PR  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   731a2fbff31004d05832549812e7f04b   CA                              BA  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   b44702522eca54df20ff780adbc1cc17   CM                              AF  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   c873460d1098693e2d8eb9b2e05294df   CN                              PR  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   3fbbbcd24a429756ad54340c7ec93a10   CO                              PE  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   a5c4db0e1f6c35f337bec9840e974af0   CP                              CR  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   19cc0a44df2a86cb157e0201fc841621   CR                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   d7357f1458fb7201f2028ebc1eb8e190   CS                              PR  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   0cc2c965404c9204b9af8d21071ca9e6   CT                              PR  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   9c708ae9ec512b9dc002300b6d8b5cdb   CW                              TR  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   e33caf9a4732d7c05d94872cd984bd64   DE                              CR  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   113e009e56109bdc12035102fa3dccca   DF                              CR  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   213b36398803fb4f9ff25626b95b429a   DI                              CR  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   53b15363b865f929879f8e862773f3c7   DO                              CR  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   c13827e3fb42b0dcb272a40fd949ae22   DS                              AF  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   e162a79afdd8580bb18c9740fa6546fa   EV                              CR  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   596c03c8c88db0f16a606712e233f8e7   EX                              PE  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   6117619eac4a1f13c281501113c307d3   FR                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   fd20da610fe83d1de58dd84d3d697812   IC                              PR  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   a2b4103f3abae06feb9ec238529206b9   IG                              PR  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   fe7e07e263adb5a7795fbbb3f9379ee0   II                              CR  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   28ea1d7960e77bbc85be471000251d8e   IN                              FR  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   aa2f1ea24dad61c9f8cb91c0d2775daa   IW                              AF  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   a31c3b08ab0f4575389c155f901fc811   LO                              SP  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   f70f73d1cdcfa846e15114797ed12e0a   ME                              CR  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   da5e0f283343b7b858e97d910fad77c7   MF                              FR  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   cb7e3d604d0b5b7f5a4dcb29ba83fd5c   MN                              AF  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   05220e4ec52a887c461339f3c6c078fb   MS                              CR  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   593c45def031ee5e033991f5d825646f   MT                              CR  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   71c57e20b5463f0ea2457b6cabcb3b9c   OC                              FR  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   aeecae2dbad1f4aabbbe51ec3e6ad706   PA                              PE  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   489ed3beca9f8b466b9a7a8c4da1b279   PC                              TR  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   6afb74fe1dfee8e16fd470a4fc5b2db5   PE                              FR  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   1f628f00283a6805770e218d7b4a71f4   PO                              OC  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   cf5f637cde43b32c6cb79edad59a0276   PP                              CR  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   82a1301d01162ba800b2d9df6b500828   PR                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   271c4f5681fe6874842949bae678ac69   PS                              BA  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   52433b208e516be6d352e78303bad162   PT                              PR  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   a69e5fe71c8f41672af6d680a25bd71f   PV                              AF  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   49a9bcb7e293fbe2a3485bf04091529c   RO                              FR  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   0cd38a9b709959f5df06b81d7c2def3c   SP                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   b3fddc1131b50eff2858564b8c3927b6   SR                              SP  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   9423a8688c99f76f9d27d4fae49dd353   TB                              PR  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   1e69d4c77ece06dccac4adbf8c7f8ede   TR                              AW  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   afd778a733e0da310bcc141a1314c1fa   TS                              AF  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   432b03564372fab13f752ab9b0cb0bcd   TV                              SP  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
|   755de722191dbe493d0ec03e9991b4b0   US                              FR  |
|                                      IS             The basic hierarchic |
| al link in the Network. If one item "isa" another item then the first it |
| em is more specific in meaning than the second item.   inverse\_isa    T |
| 186   0                                                                  |
+--------------------------------------------------------------------------+

</div>

</div>

\
### Semantic Group <span class="nav">[return to top of page](#semtype)</span>

<div class="group rounded-content-block">

<div id="getSemanticTypeGroup" class="method rounded-content-block">

**Method: **<span class="method-name">getSemanticTypeGroup</span><span
class="method-parameters">(String ticket,String version,String
semanticGroup)</span>
**Returns:** <span
class="method-return-type">SemanticTypeGroupDTO </span>

<div class="method-description">

**Use Case:** Given a UMLS release and a semantic type group
abbreviation, this call returns the expanded form and abbreviation of
the semantic type group, and the semantic type count for the group.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

mySemTyRelDTO = utsSemanticNetworkService.getSemanticTypeGroup (ticket,
umlsRelease, "GEOG");\
\
 String abbreviation = mySemTyRelDTO.getAbbreviation();\
 String expandedForm = mySemTyRelDTO.getExpandedForm();\
 int semTypeCnt = mySemTyRelDTO.getSemanticTypeCount();\

</div>

#### Sample Output:

  -----------------------------------
  Abbreviation: GEOG\
   Expanded Form: Geographic Areas\
   Semantic Type Count: 1\
  -----------------------------------

</div>

<div id="getSemanticTypeByGroup" class="method rounded-content-block">

**Method: **<span class="method-name">getSemanticTypeByGroup</span><span
class="method-parameters">(String ticket,String version,String
semanticGroup)</span>
**Returns:** <span
class="method-return-type">ArrayList&lt;SemanticTypeDTO&gt; </span>

<div class="method-description">

**Use Case:** Given a UMLS release and a semantic type group
abbreviation, this call returns all the semantic types in the given
group.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

myarrSemTyRelDTO = utsSemanticNetworkService.getSemanticTypeByGroup
(ticket, umlsRelease, "DISO");\
\
 for (int i = 0; i &lt; myarrSemTyRelDTO.size(); i++) {\
\
 SemanticTypeDTO mySemTyRel = myarrSemTyRelDTO.get(i);\
 String abbreviation = mySemTyRel.getAbbreviation();\
 String definition = mySemTyRel.getDefinition();\
 int childCnt = mySemTyRel.getChildCount();\
 int relCnt = mySemTyRel.getRelationCount();\
 String example = mySemTyRel.getExample();\
 String nonHuman = mySemTyRel.getNonHuman();\
 String treeNum = mySemTyRel.getTreeNumber();\
 String ui = mySemTyRel.getUi();\
 String value = mySemTyRel.getValue();\
 }\

</div>

#### Sample Output:

+--------------------------------------------------------------------------+
|   Abbreviation   Definition                                              |
|                                                                          |
|                                                                          |
|                                                                          |
|                                                             Child Count  |
|   Relation Count   Tree Number    Ui     Value                           |
|   -------------- ------------------------------------------------------- |
| ------------------------------------------------------------------------ |
| ------------------------------------------------------------------------ |
| ------------------------------------------------------------------------ |
| ----------------------------------------------------------- ------------ |
| - ---------------- -------------- ------ ------------------------------- |
| ---                                                                      |
|   sosy           An observable manifestation of a disease or condition b |
| ased on clinical judgment, or a manifestation of a disease or condition  |
| which is experienced by the patient and reported as a subjective observa |
| tion.                                                                    |
|                                                             0            |
|   5                A2.2.2         T184   Sign or Symptom                 |
|   anab           An abnormal structure, or one that is abnormal in size  |
| or location.                                                             |
|                                                                          |
|                                                                          |
|                                                             2            |
|   12               A1.2.2         T190   Anatomical Abnormality          |
|   neop           A new and abnormal growth of tissue in which the growth |
|  is uncontrolled and progressive. The growths may be malignant or benign |
| .                                                                        |
|                                                                          |
|                                                             0            |
|   1                B2.2.1.2.1.2   T191   Neoplastic Process              |
|   cgab           An abnormal structure, or one that is abnormal in size  |
| or location, present at birth or evolving over time as a result of a def |
| ect in embryogenesis.                                                    |
|                                                                          |
|                                                             0            |
|   1                A1.2.2.1       T019   Congenital Abnormality          |
|   acab           An abnormal structure, or one that is abnormal in size  |
| or location, found in or deriving from a previously normal structure. Ac |
| quired abnormalities are distinguished from diseases even though they ma |
| y result in pathological functioning (e.g., "hernias incarcerate").      |
|                                                             0            |
|   3                A1.2.2.2       T020   Acquired Abnormality            |
|   fndg           That which is discovered by direct observation or measu |
| rement of an organism attribute or condition, including the clinical his |
| tory of the patient. The history of the presence of a disease is a 'Find |
| ing' and is distinguished from the disease itself.                       |
|                                                             2            |
|   10               A2.2           T033   Finding                         |
|   inpo           A traumatic wound, injury, or poisoning caused by an ex |
| ternal agent or force.                                                   |
|                                                                          |
|                                                                          |
|                                                             0            |
|   11               B2.3           T037   Injury or Poisoning             |
|   patf           A disordered process, activity, or state of the organis |
| m as a whole, of a body system or systems, or of multiple organs or tiss |
| ues. Included here are normal responses to a negative stimulus as well a |
| s patholologic conditions or states that are less specific than a diseas |
| e. Pathologic functions frequently have systemic effects.   3            |
|   19               B2.2.1.2       T046   Pathologic Function             |
|   dsyn           A condition which alters or interferes with a normal pr |
| ocess, state, or activity of an organism. It is usually characterized by |
|  the abnormal functioning of one or more of the host's systems, parts, o |
| r organs. Included here is a complex of symptoms descriptive of a disord |
| er.                                                         2            |
|   3                B2.2.1.2.1     T047   Disease or Syndrome             |
|   mobd           A clinically significant dysfunction whose major manife |
| station is behavioral or psychological. These dysfunctions may have iden |
| tified or presumed biological etiologies or manifestations.              |
|                                                                          |
|                                                             0            |
|   6                B2.2.1.2.1.1   T048   Mental or Behavioral Dysfunctio |
| n                                                                        |
|   comd           A pathologic function inherent to cells, parts of cells |
| , or molecules.                                                          |
|                                                                          |
|                                                                          |
|                                                             0            |
|   1                B2.2.1.2.2     T049   Cell or Molecular Dysfunction   |
|   emod           A representation in a non-human organism of a human dis |
| ease for the purpose of research into its mechanism or treatment.        |
|                                                                          |
|                                                                          |
|                                                             0            |
|   1                B2.2.1.2.3     T050   Experimental Model of Disease   |
+--------------------------------------------------------------------------+

</div>


**Method: **<span
class="method-name">getAllSemanticTypeGroups</span><span
class="method-parameters">(String ticket,String version)</span>
**Returns:** <span
class="method-return-type">ArrayList&lt;SemanticTypeGroupDTO&gt; </span>


**Use Case:** Given a UMLS release, this call returns all the semantic
type groups used in the version. Each returned object specifies a
semantic type group, including the name and semantic type count for the
group.


#### Sample Input (Java):

myarrSemTyRelDTO = utsSemanticNetworkService.getAllSemanticTypeGroups
(ticket, umlsRelease);\
\
 for (int i = 0; i &lt; myarrSemTyRelDTO.size(); i++) {\
 SemanticTypeGroupDTO mySemTyRel = myarrSemTyRelDTO.get(i);\
 String abbreviation = mySemTyRel.getAbbreviation();\
 String expandedForm = mySemTyRel.getExpandedForm();\
 int semTypeCnt = mySemTyRel.getSemanticTypeCount();\
 }\



#### Sample Output:

+--------------------------------------------------------------------------+
|   Abbreviation   Expanded Form                 Semantic Type Count       |
|   -------------- ----------------------------- ---------------------     |
|   ACTI           Activities & Behaviors        9                         |
|   ANAT           Anatomy                       11                        |
|   CHEM           Chemicals & Drugs             26                        |
|   CONC           Concepts & Ideas              12                        |
|   DEVI           Devices                       3                         |
|   DISO           Disorders                     12                        |
|   GENE           Genes & Molecular Sequences   5                         |
|   GEOG           Geographic Areas              1                         |
|   LIVB           Living Beings                 21                        |
|   OBJC           Objects                       5                         |
|   OCCU           Occupations                   2                         |
|   ORGA           Organizations                 4                         |
|   PHEN           Phenomena                     6                         |
|   PHYS           Physiology                    9                         |
|   PROC           Procedures                    7                         |
+--------------------------------------------------------------------------+
