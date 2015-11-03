title=Retrieving UMLS Atom Cluster Information from UTS SOAP API
date=2015-08-17
updated=2015-08-17
type=page
status=published
navorder=6
~~~~~~


Interface| Method|Use Case|Object or Data type Returned 
-- | -- | -- | --
**UtsWsContentController**||||
 |[getCode](#getcode)|Retrieve information for a known source-asserted code|SourceAtomClusterDTO 
 |[getSourceConcept](#getsourceconcept)|Retrieve information for a known source-asserted concept |SourceAtomClusterDTO 
 |[getSourceDescriptor](#getsourcedescriptor)|Retrieve information for a known source-asserted descriptor|SourceAtomClusterDTO
 |[getDefaultPreferredAtom](/soap/atoms/#getdefaultpreferredatom)|Retrieve the highest-ranking atom for a known source-asserted concept, code, or descriptor | AtomDTO


**Each of these methods requires an instance of the UtsWsContentController interface, such as**:

```SourceAtomClusterDTO mySourceConcept = utsContentService.getSourceConcept(ticketClient.getSingleUseTicket(tgt), currentUmlsRelease, identifier, rsab);```

**Method:**getDefaultPreferredAtom(String ticket,String version,String atomClusterId,String rootSourceAbbreviation)

**Returns:**AtomDTO(see javadocs)(javadocs/gov/nih/nlm/umls/dto/content/AtomDTO.html)

**Use Case:** You have a source concept id (SCUI), source descriptor id (SDUI), or CODE from a known source vocabulary. You want the name and term type of the default preferred atom of the cluster, as well as the default preferred name of the CUI to which it belongs for comparison.

**Note:** AtomDTOs have other embedded objects such as SourceAtomClusterDTO, ConceptDTO, and TermStringDTO. These other objects and their methods are accessible via getters. You can access, for example, the CUI that the atom belongs to by using getConcept().getUi();
See Javadocs for more details.

#### Sample Input (Java):

~~~~
AtomDTO myAtom = utsContentService.getDefaultPreferredAtom(ticket,2011AB, "126952004", "SNOMEDCT");

 String atomName = myAtom.getTermString().getName();
 String aui = myAtom.getUi();
 String termType = myAtom.getTermType();
 String conceptUi = myAtom.getConcept().getUi();
 String conceptName = myAtom.getConcept().getDefaultPreferredName();
~~~~

#### Sample Input (C#):

~~~~
content.atomDTO myAtom = utsContentService.getDefaultPreferredAtom(ticket, "2011AB", "126952004", "SNOMEDCT");

 string atomName = myAtom.termString.name;
 string aui = myAtom.ui;
 string termType = myAtom.termType;
 string conceptUi = myAtom.concept.ui;
 string conceptName = myAtom.concept.defaultPreferredName;
~~~~


#### Sample Output:

~~~~text
  AUI: A3577659
   Atom Name: Neoplasm of brain
   Term Type: PT
  
   Concept Id: C0006118
   Concept Preferred Name: Brain Neoplasms
  
~~~~

### getCode

**Method Signature**: ```getCode(String ticket,String version,String codeId,String rootSourceAbbreviation)```

#### Sample Input (Java):

~~~~java
SourceAtomClusterDTO myCode = utsContentService.getCode(ticket, "2015AA", "53746-4", "LNC");
 String name = myCode.getDefaultPreferredName();
 int atomCount = myCode.getAtomCount();
 int codeRelationCount = myCode.getCodeRelationCount();
 int attributeCount = myCode.getAttributeCount();
~~~~

#### Sample Input (C#):

~~~~c#
content.sourceAtomClusterDTO myCode = utsContentService.getCode(ticket, "2015AA", "53746-4", "LNC");

 string name = myCode.defaultPreferredName;
 int atomCount = myCode.atomCount;
 int codeRelationCount = myCode.codeRelationCount;
 int attributeCount = myCode.attributeCount;
~~~~


#### Sample Output:

~~~~text
   Code Name: Barbiturates panel:-:Point in time:Urine:-
   Number of Atoms in this code: 4
   Number of Code relations: 14
   Number of Code attributes: 16
~~~~

### getSourceConcept

**Method Signature**: ```getSourceConcept(String ticket,String version,String sourceConceptId,String rootSourceAbbreviation)```

#### Sample Input (Java):

~~~~java
SourceAtomClusterDTO myCode = utsContentService.getSourceConcept(ticket, "2015AA", "9468002", "SNOMEDCT_US");

 String name = mySourceConcept.getDefaultPreferredName();
 int atomCount = mySourceConcept.getAtomCount();
 int codeRelationCount = mySourceConcept.getSourceConceptRelationCount();
 int attributeCount = mySourceConcept.getAttributeCount();
~~~~

#### Sample Input (C#):

~~~~c#
content.sourceAtomClusterDTO mySourceConcept = utsContentService.getSourceConcept(ticket, "2015AA", "9468002", "SNOMEDCT_US");

 string name = mySourceConcept.defaultPreferredName;
 int atomCount = mySourceConcept.atomCount;
 int codeRelationCount = mySourceConcept.sourceConceptRelationCount;
 int attributeCount = mySourceConcept.attributeCount;
~~~~

#### Sample Output:

~~~~text
Source Concept Name: Closed fracture carpal bone               
Number of Atoms in Source Concept: 6
Number of Source Concept relations: 28
Number of Source Concept attributes: 5
~~~~

### getSourceDescriptor

**Method Signature**: ```getSourceDescriptor(String ticket,String version,String sourceDescriptorId,String rootSourceAbbreviation)```


#### Sample Input (Java):

~~~~java
SourceAtomClusterDTO mySourceDescriptor = utsContentService.getSourceDescriptor(ticket, "2015AA", "D009369", "MSH");

 String name = mySourceDescriptor.getDefaultPreferredName();
 int atomCount = mySourceDescriptor.getAtomCount();
 int codeRelationCount = mySourceDescriptor.getSourceDescriptorRelationCount();
 int attributeCount = mySourceDescriptor.getAttributeCount();
~~~~

#### Sample Input (C#):

~~~~c#
content.sourceAtomClusterDTO myCode = utsContentService.getSourceDescriptor(ticket, "2015AA", "D009369", "MSH");

 string name = mySourceDescriptor.defaultPreferredName;
 int atomCount = mySourceDescriptor.atomCount;
 int codeRelationCount = mySourceDescriptor.codeRelationCount;
 int attributeCount = mySourceDescriptor.attributeCount;
~~~~


#### Sample Output:

~~~~text
Source Descriptor name: Neoplasms            
Number of atoms in Source Descriptor: 14
Number of Source Descriptor Relations: 96
Number of Source Descriptor Attributes: 22         
~~~~


**Method:**getCodeAtoms(String ticket,String version,String codeId,String rootSourceAbbreviation,PSF psf)

**Returns:**ArrayList<AtomDTO>(see javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/content/AtomDTO.html)

**Use Case:** Given a UMLS release, a specified root source abbreviation (RSAB) and code, this call returns details for the atoms in the source vocabulary that correspond to the given code. Each atom is an occurrence of the code within the source vocabulary, e.g., if there are four atoms in a source that correspond to a code, the call will return the four
atoms.


**Note:** AtomDTOs have other embedded objects such as SourceAtomClusterDTO, ConceptDTO, and TermStringDTO. These other objects and their methods are accessible via getters. You can access, for example, the CUI that the atom belongs to by using getConcept().getUi();
See Javadocs for more details.


#### Sample Input (Java):

~~~~
gov.nih.nlm.uts.webservice.content.Psf myPsf = new gov.nih.nlm.uts.webservice.content.Psf();

 java.util.List<AtomDTO> myAtoms = new ArrayList<AtomDTO>();
 myAtoms = utsContentService.getCodeAtoms(ticket, umlsRelease,"D008636","MSHFRE",myPsf);

 for (int i = 0; i < myAtoms.size(); i++) {

 AtomDTO myAtomDTO = myAtoms.get(i);

 String aui = myAtomDTO.getUi();
 String source = myAtomDTO.getRootSource();
 String name = myAtomDTO.getTermString().getName();
 String TermType = myAtomDTO.getTermType();
 int cvMemberCount = myAtomDTO.getCvMemberCount();

 }
~~~~

#### Sample Input (C#):

~~~~
content.psf myPsf = new content.psf();
 content.atomDTO[] myAtoms = utsContentService.getCodeAtoms(ticket, "2012AA", "D008636","MSHFRE", myPsf);
 for (int i = 0; i < myAtoms.Length; i++) {

 content.atomDTO myAtomDTO = myAtoms[i];
 string aui = myAtomDTO.ui;
 string source = myAtomDTO.rootSource;
 string name = myAtomDTO.termString.name;
 string TermType = myAtomDTO.termType;
~~~~


#### Sample Output:


Atom UI   |  Atom RootSRC  | Atom Name| Atom TermType |  Atom CvMemCount 
--- | --- | --- | --- | ---
A9155841  |  MSHFRE    |  Cerveau moyen  | EP    | 0 
A9160136  |  MSHFRE|  Isthme de l'encéphale |  EP  | 0
A11394057  | MSHFRE | Isthme du cerveau | EP | 0 
A7457565  |  MSHFRE| Mésencéphale |  MH |  0 

>

**Method:**getSourceConceptAtoms(String ticket,String version,String sourceConceptId,String rootSourceAbbreviation,PSF psf)

**Returns:**ArrayList<AtomDTO>(see javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/content/AtomDTO.html)

**Use Case:**Given a UMLS release, source-asserted concept identifier(SCUI) and root source abbreviation (RSAB) this call returns the details of the corresponding concept atoms in the source. Details include the concept information, default preferred name, LUI, SUI, SDUI and suppressibility of each atom.


**Note:**AtomDTOs have other embedded objects such as SourceAtomClusterDTO, ConceptDTO, and TermStringDTO. These other objects and their methods are accessible via getters. You can access, for example, the CUI that the atom belongs to by using getConcept().getUi();
See Javadocs for more details.


#### Sample Input (Java):

~~~~
gov.nih.nlm.uts.webservice.content.Psf myPsf = new gov.nih.nlm.uts.webservice.content.Psf();
 java.util.List<AtomDTO> myAtoms = new ArrayList<AtomDTO>();
 myAtoms = utsContentService.getSourceConceptAtoms(ticket, "2012AA","262790002","SNOMEDCT",myPsf);

 for (int i = 0; i < myAtoms.size(); i++) {

 AtomDTO myAtomDTO = myAtoms.get(i);

 String aui = myAtomDTO.getUi();
 String source = myAtomDTO.getRootSource();
 String name = myAtomDTO.getTermString().getName();
 String TermType = myAtomDTO.getTermType();
 int cvMemberCount = myAtomDTO.getCvMemberCount();

 }
~~~~

#### Sample Input (C#):

~~~~
content.psf myPsf = new content.psf();
 content.atomDTO[] myAtoms = utsContentService.getSourceDescriptorAtoms(ticket, "2012AA", "262790002", "SNOMEDCT", myPsf);
 for (int i = 0; i < myAtoms.Length; i++) {

 content.atomDTO myAtomDTO = myAtoms[i];
 string aui = myAtomDTO.ui;
 string source = myAtomDTO.rootSource;
 string name = myAtomDTO.termString.name;
 string TermType = myAtomDTO.termType;
}
~~~~

#### Sample Output:

~~~~
Atom UI:A3125782
Atom RootSRC:SNOMEDCT
Atom Name:Esophageal hematoma
Atom TermType:PT
Atom CvMemCount:1

Atom UI:A3437946
Atom RootSRC:SNOMEDCT
Atom Name:Esophageal hematoma (disorder)
Atom TermType:FN
Atom CvMemCount:0

Atom UI:A3171798
Atom RootSRC:SNOMEDCT
Atom Name:Oesophageal haematoma
Atom TermType:PTGB
Atom CvMemCount:1
~~~~
>

**Method:**getSourceDescriptorAtoms(String ticket,String version,String sourceDescriptorId,String rootSourceAbbreviation,PSF psf)

**Returns:**ArrayList<AtomDTO>(see javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/content/AtomDTO.html)


**Use Case:** Given a UMLS release, source-asserted descriptor identifier (SDUI) and root source abbreviation (RSAB), this call returns the details of the corresponding descriptor atoms in the source. Details include the concept information, default preferred name, LUI, SUI, SDUI and suppressibility of each atom.

**Note:** AtomDTOs have other embedded objects such as SourceAtomClusterDTO, ConceptDTO, and TermStringDTO. These other objects and their methods are accessible via getters. You can access, for example, the CUI that the atom belongs to by using getConcept().getUi();
See Javadocs for more details.


#### Sample Input (Java):

~~~~
gov.nih.nlm.uts.webservice.content.Psf myPsf = new gov.nih.nlm.uts.webservice.content.Psf();
 java.util.List<AtomDTO> myAtoms = new ArrayList<AtomDTO>();
 myAtoms = utsContentService.getSourceDescriptorAtoms(ticket, "2012AA","D000103","MSH",myPsf);

 for (int i = 0; i < myAtoms.size(); i++) {

 AtomDTO myAtomDTO = myAtoms.get(i);

 String aui = myAtomDTO.getUi();
 String source = myAtomDTO.getRootSource();
 String name = myAtomDTO.getTermString().getName();
 String TermType = myAtomDTO.getTermType();
 int cvMemberCount = myAtomDTO.getCvMemberCount();

 }
~~~~

#### Sample Input (C#):

~~~~
content.psf myPsf = new content.psf();
 content.atomDTO[] myAtoms = utsContentService.getSourceDescriptorAtoms(ticket, "2012AA", "D000103", "MSH", myPsf);
 for (int i = 0; i < myAtoms.Length; i++) {

 content.atomDTO myAtomDTO = myAtoms[i];
 string aui = myAtomDTO.ui;
 string source = myAtomDTO.rootSource;
 string name = myAtomDTO.termString.name;
 string TermType = myAtomDTO.termType;
~~~~

#### Sample Output:


Atom UI|Atom RootSRC|Atom Name|Atom TermType|Atom CvMemCount
--- | --- | --- | --- | ---
A0018389|MSH|Acetyl CoA Carboxylase|PM|0
A0018397|MSH|Acetyl Coenzyme A Carboxylase|EP|1
A0387916|MSH|Acetyl-CoA Carboxylase|MH|1
A0857385|MSH|Acetyl-CoA:carbon-dioxide ligase (ADP-forming)|N1|0
A0399181|MSH|Carboxylase, Acetyl-CoA|PM|0
