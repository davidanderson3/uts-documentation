title=Retrieving UMLS Atom Information from UTS SOAP API
date=2015-08-14
updated=2015-08-14
type=page
status=published
category=Retrieving UMLS Concepts
navorder=2
~~~~~~


**Method:** getAtom(String ticket,String version,String atomId)

**Returns:**AtomDTO(see javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/content/AtomDTO.html)

**Use Case:**You have a known atom and want to view how it is connected to other clusters, such as source concepts, source descriptors, and concepts, as well as the default preferred names of each of those clusters. Other properties are available in the Javadocs.

**Note:**AtomDTOs have other embedded objects such as SourceAtomClusterDTO, ConceptDTO, and TermStringDTO. These other objects and their methods are accessible via getters. You can access, for example, the CUI that the atom belongs to by using getConcept().getUi();
See Javadocs for more details.


#### Sample Input (Java):

~~~~
AtomDTO myAtom = utsContentService.getAtom(ticket, 2011AB, "A6955581");
 String atomName = myAtom.getTermString().getName();
 String source = myAtom.getRootSource();
 String sourceConceptUi = myAtom.getSourceConcept().getUi();
 String sourceConceptName = myAtom.getSourceConcept().getDefaultPreferredName();
 String sourceDescriptorUi = myAtom.getSourceDescriptor().getUi();
 String sourceDescriptorName = myAtom.getSourceDescriptor().getDefaultPreferredName();
 String conceptUi = myAtom.getConcept().getUi();
 String conceptName = myAtom.getConcept().getDefaultPreferredName();
~~~~

#### Sample Input (C#):

~~~~
content.atomDTO myAtom = utsContentService.getAtom(ticket, "2011AB","A6955581");

 string atomName = myAtom.termString.name;
 string source = myAtom.rootSource;
 string sourceConceptUi = myAtom.sourceConcept.ui;
 string sourceConceptName = myAtom.sourceConcept.defaultPreferredName;
 string sourceDescriptorUi = myAtom.sourceDescriptor.ui;
 string sourceDescriptorName = myAtom.sourceDescriptor.defaultPreferredName;
 string conceptUi = myAtom.concept.ui;
 string conceptName = myAtom.concept.defaultPreferredName;

~~~~

#### Sample Output:

~~~~
   Atom Name: Heart Hypertrophy
   Source Vocabulary: MSH
  
   Concept Id: C1383860
   Concept Preferred Name: Cardiac Hypertrophy
  
   Source Concept Id: M0453089
   Source Concept Preferred Name: Cardiac Hypertrophy
  
   Source Descriptor Id: D006332
   Source Descriptor Preferred Name: Cardiomegaly
~~~~