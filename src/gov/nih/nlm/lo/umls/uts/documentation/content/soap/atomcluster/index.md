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

**Each of these examples below requires an instance of the [UtsWsContentController](/soap/installation/content.html) and [UtsWsSecurityController](/soap/installation/authentication.html) interfaces**.


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
