title=Retrieving UMLS Atom Information from UTS SOAP API
date=2015-08-14
updated=2015-08-14
type=page
status=published
navorder=3
~~~~~~



**Method: **getConceptAtoms(String ticket,String version,String conceptId,PSF psf)

**Returns:**ArrayList< AtomDTO>

**Use Case:** You have a CUI and want to look at its individual atoms and their properties. Use the psf object to exclude sources, term types, relations, etc., that are not of interest to you Look at properties of the AtomDTO such as its identifier (AUI), term type, originating source vocabulary, and name. Also see the number of Content Views to which the atom belongs. Other properties are listed in the AtomDTO Javadocs.

**Note:** AtomDTOs have other embedded objects such as SourceAtomClusterDTO, ConceptDTO, and TermStringDTO. These other objects and their methods are accessible via getters. You can access, for example, the CUI that the atom belongs to by using getConcept().getUi();
See Javadocs for more details.


#### Sample Input (Java):

~~~~
//create a variable to hold the
//build a psf object 
//iterate through the array list
 List<AtomDTO> myAtoms = new ArrayList<AtomDTO>();
 myAtoms = utsContentService.getConceptAtoms(ticket, "2011AB","C0004775",myPsf);
 UtsMetathesaurusContent.Psf myPsf = new UtsMetathesaurusContent.Psf();
 myPsf.getIncludedSources().add("SNOMEDCT");
 myPsf.getIncludedTermTypes().add("FSN");
 myPsf.getIncludedTermTypes().add("SY");
 myPsf.getIncludedTermTypes().add("PT");

 for (int i = 0; i < myAtoms.size(); i++) {

 AtomDTO myAtomDTO = myAtoms.get(i);

 String aui = myAtomDTO.getUi();
 String source = myAtomDTO.getRootSource();
 String name = myAtomDTO.getTermString().getName();
 String TermType = myAtomDTO.getTermType();

 }
~~~~

#### Sample Input (C#):

~~~~
content.psf myPsf = new content.psf();
 string[] tmpSources = new string[1];
 tmpSources[0] = "SNOMEDCT";
 string[] tmpTermTypes = new string[3];
 tmpTermTypes[0] ="FSN";
 tmpTermTypes[1] ="SY";
 tmpTermTypes[2] ="PT";
 myPsf.includedSources = tmpSources;;
 myPsf.includedTermTypes = tmpTermTypes;

 content.atomDTO[] myAtoms = utsContentService.getConceptAtoms(ticket,"2011AB", "C0004775", myPsf);
 for (int i = 0; i < myAtoms.Length; i++){

 content.atomDTO myAtomDTO = myAtoms[i];
 string aui = myAtomDTO.ui;
 string source = myAtomDTO.rootSource;
 string name = myAtomDTO.termString.name;
 string termType = myAtomDTO.termType;
 }
 
~~~~


#### Sample Output:
~~~~
 //print out the results
   AUI: A2944080
     Source Vocabulary SNOMEDCT
     Term Type:SY
     Atom Name: Rib cage
  
   AUI: A3322451
     Source Vocabulary SNOMEDCT
     Term Type:SY
     Atom Name: Thoracic cage
  
   AUI: A3753371
     Source Vocabulary SNOMEDCT
     Term Type:PT
     Atom Name: Thoracic cage structure
  
   AUI: A3753370
     Source Vocabulary SNOMEDCT
     Term Type:FN
     Atom Name: Thoracic cage structure (body structure)
~~~~
>

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