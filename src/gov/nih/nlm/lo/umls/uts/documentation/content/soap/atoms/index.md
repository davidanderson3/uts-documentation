title=Retrieving atoms and atom information from the UMLS SOAP API
date=2015-10-22
updated=2015-10-22
type=page
status=published
navorder=3
~~~~~~

Interface | Method | Use Case | Object or Data type Returned 
-- | -- | -- | --
**UtsWsContentController**||||
 |[getConceptAtoms](#getconceptatoms)|Retrieve atoms for a known UMLS CUI. You can then filter atoms according to term type, source vocabulary, suppressibility, etc. |ArrayList\<AtomDTO\>
 |[getSourceConceptAtoms](#getsourceconceptatoms)|Retrieve atoms for a known source-asserted concept. You can then filter atoms according to term type, suppressibility, etc. |ArrayList\<AtomDTO\>
 |[getSourceDescriptorAtoms](#getsourcedescriptoratoms)|Retrieve atoms for a known source-asserted descriptor. You can then filter atoms according to term type, suppressibility, etc. |ArrayList\<AtomDTO\>
 |[getCodeAtoms](#getcodeatoms)|Retrieve atoms for a known source-asserted code. You can then filter atoms according to term type, suppressibility, etc. |ArrayList\<AtomDTO\>
 |[getAtom](#getatom)|Retrieve information for a known UMLS AUI. | AtomDTO
 |[getDefaultPreferredAtom](#getdefaultpreferredatom)|Retrieve the highest-ranking atom for a known source-asserted concept, code, or descriptor | AtomDTO
 
**Each of these examples below requires an instance of the [UtsWsContentController](/soap/installation/interface-setup.html#utswscontentcontroller), [UtsWsMetadataController](/soap/installation/interface-setup.html#utswsmetadatacontroller) and [UtsWsSecurityController](/soap/installation/interface-setup.html#utswssecuritycontroller) interfaces**.
 
### getConceptAtoms

**Method Signature:** ```getConceptAtoms(String ticket, String version, String conceptId, PSF psf)```


#### Sample Input (Java):

~~~~java

    String currentUmlsRelease = utsMetadataService.getCurrentUMLSVersion(ticket);
    Psf myPsf = new Psf();
    //exclude obsolete and suppressible atoms
    myPsf.setIncludeSuppressible(false);
    myPsf.setIncludeObsolete(false);
    
    //only include SNOMEDCT_US and OMIM source vocabularies
    myPsf.getIncludedSources().add("SNOMEDCT_US");
    myPsf.getIncludedSources().add("OMIM");
		
    List<AtomDTO> atoms = new ArrayList<AtomDTO>();
    atoms = utsContentService.getConceptAtoms(ticket, currentUmlsRelease, "C0595985", myPsf);
        
    for (AtomDTO atom:atoms) {
			
    String aui = atom.getUi();
    String tty = atom.getTermType();
    String name = atom.getTermString().getName();
    String sourceId = atom.getCode().getUi();
    String rsab = atom.getRootSource();
    

    }

~~~~


#### Sample Output

~~~~text
AUI|TTY|Name|Source-asserted identifier|Source vocabulary
A2953834|PT|Aglossia-adactyly syndrome|205817005|SNOMEDCT_US
A3527513|FN|Aglossia-adactyly syndrome (disorder)|205817005|SNOMEDCT_US
A11979234|ET|HANHART SYNDROME|103300|OMIM
A17326723|SY|Hanhart syndrome|35031005|SNOMEDCT_US
A2966719|PT|Hanhart's syndrome|35031005|SNOMEDCT_US
A3486540|FN|Hanhart's syndrome (disorder)|35031005|SNOMEDCT_US
A2972867|SY|Micrognathia with peromelia|35031005|SNOMEDCT_US

~~~~

### getSourceConceptAtoms

**Method Signature:** ```getSourceConceptAtoms(String ticket, String version, String sourceConceptId, String rootSourceAbbreviation, PSF psf)```


#### Sample Input (Java):

~~~~
 String currentUmlsRelease = utsMetadataService.getCurrentUMLSVersion(ticket);
 Psf myPsf = new Psf();
 List<AtomDTO> myAtoms = new ArrayList<AtomDTO>();
 myAtoms = utsContentService.getSourceConceptAtoms(ticket, currentUmlsRelease,"9468002","SNOMEDCT_US",myPsf);

 for (AtomDTO atom:myAtoms) {

 String aui = atom.getUi();
 String tty = atom.getTermType();
 String name = atom.getTermString().getName();
 boolean isObsolete = atom.isObsolete();

 }
~~~~

#### Sample Output

~~~~text
A3357646|PT|Closed fracture carpal bone|false
A3357644|FN|Closed fracture carpal bone (disorder)|false
A4754365|IS|Closed fracture carpal bone, NOS|true
A2889793|SY|Closed fracture of carpal bone|false
A3358392|SY|Closed fracture of wrist|false
A4754444|IS|Closed fracture of wrist, NOS|true
~~~~

### getSourceDescriptorAtoms

**Method Signature:** ```getSourceDescriptorAtoms(String ticket, String version, String sourceDescriptorId, String rootSourceAbbreviation, PSF psf)```


#### Sample Input (Java):

~~~~
 String currentUmlsRelease = utsMetadataService.getCurrentUMLSVersion(ticket);
 Psf myPsf = new Psf();
 List<AtomDTO> myAtoms = new ArrayList<AtomDTO>();
 myAtoms = utsContentService.getSourceDescriptorAtoms(ticket, currentUmlsRelease,"I63.422","ICD10CM",myPsf);

 for (AtomDTO atom:myAtoms) {

 String aui = atom.getUi();
 String tty = atom.getTermType();
 String name = atom.getTermString().getName();
 boolean isObsolete = atom.isObsolete();
 boolean isSuppressible = atom.isSuppressible();

 }
~~~~

#### Sample Output

~~~~text
AUI|TTY|Name|Obsolete|Suppressible
A17813522|PT|Cerebral infarction due to embolism of left anterior cerebral artery|false|false
A20134276|AB|Cerebral infrc due to embolism of left ant cerebral artery|false|true
~~~~


### getCodeAtoms

**Method Signature:** ```getCodeAtoms(String ticket, String version, String sourceDescriptorId, String rootSourceAbbreviation, PSF psf)```

#### Sample Input (java)

~~~~
 String currentUmlsRelease = utsMetadataService.getCurrentUMLSVersion(ticket);
 Psf myPsf = new Psf();
 List<AtomDTO> myAtoms = new ArrayList<AtomDTO>();
 myAtoms = utsContentService.getCodeAtoms(ticket, currentUmlsRelease,"53746-4","LNC",myPsf);

 for (AtomDTO atom:myAtoms) {

 String aui = atom.getUi();
 String tty = atom.getTermType();
 String name = atom.getTermString().getName();
 boolean isObsolete = atom.isObsolete();
 boolean isSuppressible = atom.isSuppressible();

 }
~~~~

#### Sample Output

~~~~text
AUI|TTY|Name|Obsolete|Suppressible
A18199351|OSN|Barbiturates Pnl Ur|false|false
A21121706|LC|Barbiturates panel - Urine|false|false
A18825952|MTH_LN|Barbiturates panel:-:Point in time:Urine:-|false|false
A18160664|LN|Barbiturates panel:-:Pt:Urine:-|false|false
~~~~
 
 
### getAtom

**Method Signature:** ```getAtom(String ticket,String version,String atomId)```

#### Sample Input (Java):

~~~~java
 String currentUmlsRelease = utsMetadataService.getCurrentUMLSVersion(ticket);
 AtomDTO myAtom = utsContentService.getAtom(ticket, currentUmlsRelease, "A6955581");
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

~~~~c#
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

~~~~text
   Atom Name: Heart Hypertrophy
   Source Vocabulary: MSH
  
   Concept Id: C1383860
   Concept Preferred Name: Cardiac Hypertrophy
  
   Source Concept Id: M0453089
   Source Concept Preferred Name: Cardiac Hypertrophy
  
   Source Descriptor Id: D006332
   Source Descriptor Preferred Name: Cardiomegaly
~~~~

### getDefaultPreferredAtom

**Method Signature**: ```utsContentService.getDefaultPreferredAtom(ticket, String version, String atomClusterId, String rootSourceAbbrevation);```

#### Sample Input (Java)

~~~~java
String currentUmlsRelease = utsMetadataService.getCurrentUMLSVersion(ticket);
AtomDTO atom = new AtomDTO();
atom = utsContentService.getDefaultPreferredAtom(ticketClient.getSingleUseTicket(tgt), currentUmlsRelease, "9468002","SNOMEDCT_US");
String aui = atom.getUi();
String tty = atom.getTermType();
String name = atom.getTermString().getName();
boolean isObsolete = atom.isObsolete();
boolean isSuppressible = atom.isSuppressible();
~~~~

#### Sample Output

~~~~text
AUI: A3357646
TTY: PT
Name: Closed fracture of carpal bone
Obsolete: False
Suppressible: False
~~~~
