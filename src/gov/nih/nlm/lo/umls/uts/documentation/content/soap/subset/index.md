title=Retrieving UMLS Subset Information from UTS SOAP API
date=2015-08-17
updated=2015-08-17
type=page
status=published
navorder=8
~~~~~~


**Method:**getSubsets(String ticket,String version,PSF psf)

**Returns:**ArrayList<SubsetDTO>(see javadocs)(javadocs/gov/nih/nlm/umls/dto/content/SubsetDTO.html)

**Use Case:** Given a UMLS release, this call returns details of the subsets of the given release. Each subset is a named collection of information that may be of specific interest. Details of each subset include its identifiers, description, e.g., Spanish Language Edition," a count of the number of atoms in each subset, and other information.

#### Sample Input (Java):

~~~~
gov.nih.nlm.uts.webservice.content.Psf myPsf = new gov.nih.nlm.uts.webservice.content.Psf();
 java.util.List<SubsetDTO> myAtoms = new ArrayList<SubsetDTO>();
 mySubsetsDTO = utsContentService.getSubsets(ticket, umlsRelease, myPsf);
 for (int i = 0; i < mySubsetsDTO.size(); i++) {
  SubsetDTO mySubsets = mySubsetsDTO.get(i);
 String ui = mySubsets.getUi();
 String name = mySubsets.getName();
 String srcui = mySubsets.getSourceUi();
 int atommemcnt = mySubsets.getAtomMemberCount();
 }
~~~~

#### Sample Input (C#):

~~~~
content.psf myPsf = new content.psf();
 content.subsetDTO[] mySubsetsDTO = utsContentService.getSubsets(ticket, "2011AB", myPsf);
 for (int i = 0; i < mySubsetsDTO.Length; i++) {
 content.subsetDTO mySubsets = mySubsetsDTO[i];
 string ui = mySubsets.ui;
 string name = mySubsets.name;
 string srcui = mySubsets.sourceUi;
 int atommemcnt = mySubsets.atomMemberCount;
~~~~

#### Sample Output:

 Subset UI |  Subset Name   |    Subset SRCUI |  Subset AtomMemCount 
 ---| --- | --- | ---
C1368722  |  Spanish Language Edition   | 1145035      |  740793   
C1321498   | US English Dialect Subset |  1146039     |   740906
C3165220  |  GB English Dialect Subset  | 1147034      |  740991 

>

**Method: **getSubset(String ticket,String version,String conceptId)

**Returns:**SubsetDTO(see javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/content/SubsetDTO.html)

**Use Case:**Given a UMLS release and a concept unique identifier (CUI) for a subset, this call returns details of the subset such as its identifiers, description, and a count of the number of atoms in the subset.

#### Sample Input (Java):

~~~~
SubsetDTO mySubsetDTO = new SubsetDTO();
 mySubsetDTO = utsContentService.getSubset(ticket, umlsRelease, "C1368722");
 String ui = mySubsetDTO.getUi();
 String name = mySubsetDTO.getName();
 String srcui = mySubsetDTO.getSourceUi();
 int atommemcnt = mySubsetDTO.getAtomMemberCount();
~~~~

#### Sample Input (C#):

~~~~
content.subsetDTO mySubsetsDTO = utsContentService.getSubset(ticket, "2011AB", "C1368722");
 string ui = mySubsetsDTO.ui;
 string name = mySubsetsDTO.name;
 string srcui = mySubsetsDTO.sourceUi;
 int atommemcnt = mySubsetsDTO.atomMemberCount;
~~~~

#### Sample Output:

Subset UI  | Subset Name   | Subset SRCUI |  Subset AtomMemCount      
 ---| --- | --- | ---                                                                |
C1368722 |   Spanish Language Edition  | 1145035  |   740793    

>

**Method:**getAtomSubsetMemberships(String ticket,String version,String conceptId,PSF psf)

**Returns:**ArrayList<AtomSubsetMemberDTO>(see javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/content/AtomSubsetMemberDTO.html)

**Use Case:** Given a UMLS release and concept unique identifier (CUI) for a subset, this call returns details of the atoms that are members of the subset.

#### Sample Input (Java):

~~~~
gov.nih.nlm.uts.webservice.content.Psf myPsf = new gov.nih.nlm.uts.webservice.content.Psf();
 java.util.List<AtomSubsetMemberDTO> myAtoms = new ArrayList<AtomSubsetMemberDTO>();
 AtomSubsetMem = utsContentService.getAtomSubsetMemberships(ticket, umlsRelease, "A6943203", myPsf);
 for (int i = 0; i < AtomSubsetMem.size(); i++) {
 AtomSubsetMemberDTO myAtomSubsetMem = AtomSubsetMem.get(i);
 String ui = myAtomSubsetMem.getAtom().getConcept().getUi();
 String defprefname = myAtomSubsetMem.getAtom().getConcept().getDefaultPreferredName();
 String contviewhandle = myAtomSubsetMem.getSubsetHandle();
 String termtype = myAtomSubsetMem.getAtom().getTermType();
 }
~~~~

#### Sample Input (C#):

~~~~
content.psf myPsf = new content.psf();
 content.atomSubsetMemberDTO[] AtomSubsetMemberDTO =
utsContentService.getAtomSubsetMemberships(ticket, "2011AB", "A6943203", myPsf);
 for (int i = 0; i < AtomSubsetMemberDTO.Length; i++) {
 content.atomSubsetMemberDTO myAtomContentViewMemberDTO = AtomSubsetMemberDTO[i];
 string ui = myAtomContentViewMemberDTO.atom.concept.ui;
 string defprefname = myAtomContentViewMemberDTO.atom.concept.defaultPreferredName;
 string contviewhandle = myAtomContentViewMemberDTO.subsetHandle;
 string termtype = myAtomContentViewMemberDTO.atom.termType;
~~~~

#### Sample Output:

Concept UI  | Concept DefaultPrefferedName  |   Subset Handle |  Atom TermType 
 ---| --- | --- | ---
C0553662   |  Arthritis, Juvenile Rheumatoid  | IC1321498  |  SY    
C0553662    | Arthritis, Juvenile Rheumatoid  | IC3165220   |    SY  

>

**Method: **getSourceConceptSubsetMemberships(String ticket,String version,String sourceConceptId,String rootSourceAbbreviation,PSF psf)

**Returns:**ArrayList<SourceConceptSubsetMemberDTO>(see javadocs)(javadocs/gov/nih/nlm/umls/dto/content/SourceConceptSubsetMemberDTO.html)

**Use Case:** Given a UMLS release and source concept Id for a subset, this call returns details of the source concept that are members of the subset.

#### Sample Input (Java):

~~~~
gov.nih.nlm.uts.webservice.content.Psf myPsf = new gov.nih.nlm.uts.webservice.content.Psf();
 java.util.List<SourceConceptSubsetMemberDTO> myAtoms = new ArrayList<SourceConceptSubsetMemberDTO>();
 mySourceConceptSubsetMember = utsContentService.getSourceConceptSubsetMemberships(securityService.getProxyTicket(ticketGrantingTicket(), serviceName), umlsRelease, "193003", "SNOMEDCT_US", myPsf));
 for (int i = 0; i < mySourceConceptSubsetMember.size(); i++) {
 SourceConceptSubsetMemberDTO mySourceConceptCont = mySourceConceptSubsetMember.get(i);
 String ui = mySourceConceptCont.getUi();
 String name = mySourceConceptCont.getSourceConcept().getDefaultPreferredName();
 }
~~~~

#### Sample Output:


Ui|Src Concept DefaultPreferredName
 ---| ---
AT188567505|Benign hypertensive renal disease
AT188485731|Benign hypertensive renal disease
AT188345133|Benign hypertensive renal disease
AT188195552|Benign hypertensive renal disease
AT188195551|Benign hypertensive renal disease
AT188025182|Benign hypertensive renal disease
AT187982299|Benign hypertensive renal disease
AT187918348|Benign hypertensive renal disease
AT187854130|Benign hypertensive renal disease
AT187832812|Benign hypertensive renal disease
AT187747644|Benign hypertensive renal disease

