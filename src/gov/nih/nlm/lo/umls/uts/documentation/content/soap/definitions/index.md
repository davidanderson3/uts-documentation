title=Retrieving Definitions from the UMLS SOAP API
date=2015-08-14
updated=2015-08-14
type=page
status=published
navorder=3
~~~~~~

The sample methods below would be run on an object similar to the utsContentService object.

Interface | Method | Use Case | Object or Data type Returned | Guidance
-- | -- | -- | --
**UtsWsContentController**||||
 |[getConceptDefinitions](#getconceptdefinitions) | Retrieve definitions for a known UMLS CUI | List\<DefinitionDTO\> | Use ```getDefinitionCount``` on your ConceptDTO to see if there are definitions for the CUI before making this call.
 |[getSourceConceptDefinitions](#getsourceconceptdefinitions) | Retrieve definitions for a known source-asserted concept | List\<DefinitionDTO\> | Use ```getDefinitionCount``` on your SourceAtomClusterDTO to see if there are definitions for the atom cluster before making this call.
 |[getSourceDescriptorDefinitions](#getsourcedescriptordefinitions) | Retrieve definitions for a known source-asserted descriptor | List\<DefinitionDTO\> | Use ```getDefinitionCount``` on your SourceAtomClusterDTO to see if there are definitions for the atom cluster before making this call.
 |[getAtomDefinitions](#getatomdefinitions) | Retrieve definitions for a known UMLS AUI | List\<DefinitionDTO\> | Use ```getDefinitionCount``` on your AtomDTO to see if there are definitions for the AUI before making this call.

**Each of these examples below requires an instance of the [UtsWsContentController](/soap/installation/content.html) and [UtsWsSecurityController](/soap/installation/authentication.html) interfaces**.

### getConceptDefinitions

**Method Signature**: ```getConceptDefinitions(String ticket, String version, String conceptId, Psf psf) ```

#### Sample Input (Java):

~~~~java

//definition for Benign Paroxysmal Positional Vertigo
List<DefinitionDTO> definitions = new ArrayList<DefinitionDTO>();
definitions = utsContentService.getConceptDefinitions(ticket, "2015AB", "C0155502", myPsf);

 for (DefinitionDTO definition:definitions) {
 String rootSource = definition.getRootSource();
 String value = definition.getValue();
 
 }
 
~~~~

#### Sample Output:

~~~~text
Definition: Idiopathic recurrent VERTIGO associated with POSITIONAL NYSTAGMUS. It is associated with a vestibular loss without other neurological or auditory signs. Unlike in LABYRINTHITIS and VESTIBULAR NEURONITIS inflammation in the ear is not observed.

Source Vocabulary: MSH 
~~~~

### getSourceConceptDefinitions

**Method Signature:** ```getSourceConceptDefinitions(String ticket,String version,String sourceConcept,String rootSourceAbbreviation,Psf psf)```


#### Sample Input (Java):

~~~~java
List<DefinitionDTO> definitions = new ArrayList<DefinitionDTO>();
definitions = utsContentService.getSourceConceptDefinitions(ticket, "2015AB", "M0014340", "MSH", myPsf);
 
 for (DefinitionDTO:definitions) {
 
 String rootSource = definition.getRootSource();
 String value = definition.getValue();
 
 }
~~~~

#### Sample Output:

~~~~text
Definition: NECROSIS of the MYOCARDIUM caused by an obstruction of the blood supply to the heart (CORONARY CIRCULATION).

Source Vocabulary: MSH
~~~~

### getSourceDescriptorDefinitions

**Method Signature: ** ```getSourceDescriptorDefinitions(String ticket,String version,String sourceDescriptor,String rootSourceAbbreviation,Psf psf)```


#### Sample Input (Java):

~~~~java
List<DefinitionDTO> definitions = new ArrayList<DefinitionDTO>();
definitions = utsContentService.getSourceConceptDefinitions(ticket, "2015AB","GO:0005634", "GO", myPsf));
 
 for (DefinitionDTO:definitions) {
 
 String rootSource = definition.getRootSource();
 String value = definition.getValue();
 
 }
~~~~
 
 
#### Sample Output:

~~~~text
Definition: A membrane-bounded organelle of eukaryotic cells in which chromosomes are housed and replicated. In most cells, the nucleus contains all of the cells chromosomes except the organellar chromosomes, and is the site of RNA synthesis and processing. In some species, or in specialized cell types, RNA metabolism or DNA replication may be absent. [GOC:go_curators]

Source Vocabulary: GO
~~~~

### getAtomDefinitions

**Method Signature:** ```getAtomDefinitions(String ticket,String version,String atomId,PSF psf)```

#### Sample Input (Java):

~~~~java
UtsMetathesaurusContent.Psf myPsf = new UtsMetathesaurusContent.Psf();
List<DefintionDTO> definitions = new ArrayList<DefinitionDTO>();
definitions = utsContentService.getAtomDefinitions(ticket, 2011AB, "A7572722", myPsf);

 for (DefinitionDTO definition:definition) {
    String source = myDefinition.getRootSource();
    String value = myDefinition.getValue();
 }
~~~~

#### Sample Output:

~~~~text
Definition: A condition of reduced bone mass, with decreased cortical thickness and a decrease in the number and size of the trabeculae of cancellous bone (but normal chemical composition), resulting in increased fracture incidence. Osteoporosis is classified as primary (Type 1, postmenopausal osteoporosis; Type 2, age-associated osteoporosis; and idiopathic, which can affect juveniles, premenopausal women, and middle-aged men) and secondary osteoporosis (which results from an identifiable cause of bone mass loss).

Source Vocabulary: NCI
~~~~
