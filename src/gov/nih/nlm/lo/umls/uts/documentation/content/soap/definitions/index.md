title=Retrieving UMLS Definitions from UTS SOAP API
date=2015-08-14
updated=2015-08-14
type=page
status=unpublished
navorder=3
~~~~~~

The sample methods below would be run on an object similar to the utsContentService object.


**Method: **getAtomDefinitions(String ticket,String version,String atomId,PSF psf)

**Returns:**ArrayList<DefinitionDTO>(javadocs/gov/nih/nlm/umls/dto/content/DefinitionDTO.html)

**Use Case:** You want to retrieve a source-asserted definition for a known atom. Not all sources in the Metathesaurus provide definitions for their atoms. Other DefinitionDTO properties are available in the Javadocs

**Note:** The following sources may have definitions attached to atoms:

 **CCC, CHV, HL7V3.0, MEDLINEPLUS, NCI.**

Users should use the getDefinitionCount() method on the AtomDTO object to determine whether or not a given code has a definition associated with it.


#### Sample Input (Java):
~~~~
UtsMetathesaurusContent.Psf myPsf = new UtsMetathesaurusContent.Psf();
 List<DefintionDTO> myDefinitions = new ArrayList<DefinitionDTO>();
 myDefinitions = utsContentService.getAtomDefinitions(ticket, 2011AB, "A7572722", myPsf);

 for (int i = 0; i < myDefinitions.size(); i++) {
 DefinitionDTO myDefinition = myDefinitions.get(i);
 String source = myDefinition.getRootSource();
 String definitionValue = myDefinition.getValue();
 }
~~~~

#### Sample Input (C♯):
~~~~
content.psf myPsf = new content.psf();
content.definitionDTO[] myDefinitions = utsContentService.getAtomDefinitions(ticket, "2011AB", "A7572722", myPsf);

 for (int i = 0; i < myDefinitions.Length; i++){

 content.definitionDTO myDefinition = myDefinitions[0];
 string source = myDefinition.rootSource;
 string definitionValue = myDefinition.value;
 }
~~~~

#### Sample Output:
~~~~
//print out the results
   Source Vocabulary: NCI
   Definition: A condition of reduced bone mass, with decreased cortical thickness and a decrease in the number and size of the trabeculae of cancellous bone (but normal chemical composition), resulting in increased fracture incidence. Osteoporosis is classified as primary (Type 1, postmenopausal osteoporosis; Type 2, age-associated osteoporosis; and idiopathic, which can affect juveniles, premenopausal women, and middle-aged men) and secondary osteoporosis (which results from an identifiable cause of bone mass loss).
~~~~
>

**Method: **getConceptDefinitions(String ticket,String version,String conceptId,PSF psf)

**Returns:**ArrayList<DefinitionDTO>(see javadocs)](javadocs/gov/nih/nlm/umls/dto/content/DefinitionDTO.html)

**Use Case:**  This method retrieves definitions for a given conceptId, when the conceptId is passed as a parameter in the method.


#### Sample Input (Java):
~~~~
myDefinition = utsContentService.getConceptDefinitions(ticket, umlsRelease, "C0004775", myPsf);

 for (int i = 0; i < myDefinition.size(); i++) {
 gov.nih.nlm.uts.webservice.content.DefinitionDTO myDefDTO = myDefinition.get(i);
 String rootSource = myDefDTO.getRootSource();
 String value = myDefDTO.getValue();
 }
~~~~

#### Sample Output:
~~~~
 Root Source: NCI 
 Definition/Value: A rare inherited syndrome characterized by juxtaglomerular cell hyperplasia, hyperaldosteronism, hypokalemia, and alkalosis. Patients have high levels of plasma renin concentration which is not associated with hypertension.  
~~~~
>

**Method: **getSourceConceptDefinitions(String ticket,String version,String sourceConcept,String rootSourceAbbreviation,Psf psf)

**Returns:** ArrayList<DefinitionDTO>(see javadocs)](javadocs/gov/nih/nlm/umls/dto/content/DefinitionDTO.html)

**Use Case:** Gets the source concept definitions.

**Note:** The following sources may have definitions attached to source concepts:

 **ALT, FMA, ICF, ICF-CY, MSH, NDFRT, SNOMEDCT, SPN**.

 Users should use the getDefinitionCount() method on the SourceAtomClusterDTO object to determine whether or not a given source concept has a definition associated with it.


#### Sample Input (Java):

~~~~
myarrDefDTOClient = utsContentService.getSourceConceptDefinitions(ticket, umlsRelease, "M0014340", "MSH", myPsf);
 for (int i = 0; i < myarrDefDTOClient.size(); i++) {
 DefinitionDTO myDefDTO = myarrDefDTOClient.get(i); String definition = myDefDTO.getValue();
 String rootSource = myDefDTO.getRootSource();
 }
~~~~

#### Sample Output:

~~~~
  Definition: NECROSIS of the MYOCARDIUM caused by an obstruction of the blood supply to the heart (CORONARY CIRCULATION).
  Root Source: MSH
~~~~
>

**Method: **getSourceDescriptorDefinitions(String ticket,String version,String sourceDescriptor,String rootSourceAbbreviation,Psf psf)

**Returns:**ArrayList<DefinitionDTO>(see javadocs)](javadocs/gov/nih/nlm/umls/dto/content/DefinitionDTO.html)

**Use Case:** Gets the source descriptor definitions.

**Note:** The following sources may have definitions attached to source
descriptors:

 **GO, MDR (and MDR foreign sources).**
Users should use the getDefinitionCount() method on the SourceAtomClusterDTO object to determine whether or not a given source descriptor has a definition associated with it.

#### Sample Input (Java):

~~~~
myarrDefDTOClient = utsContentService.getSourceDescriptorDefinitions(ticket, umlsRelease,"GO:0005634", "GO", myPsf);
 for (int i = 0; i < myarrDefDTOClient.size(); i++) {
  DefinitionDTO myDefDTO = myarrDefDTOClient.get(i); String definition = myDefDTO.getValue();
 String rootSource = myDefDTO.getRootSource();
 }

~~~~
 
 
#### Sample Output:

~~~~
  Definition: A membrane-bounded organelle of eukaryotic cells in which chromosomes are housed and replicated. In most cells, the nucleus contains all of the cells chromosomes except the organellar chromosomes, and is the site of RNA synthesis and processing. In some species, or in specialized cell types, RNA metabolism or DNA replication may be absent. [GOC:go_curators]
   Root Source: GO
~~~~

