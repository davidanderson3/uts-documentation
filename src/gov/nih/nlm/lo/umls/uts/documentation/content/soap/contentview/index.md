title=Retrieving UMLS Content View Information from UMLS SOAP API
date=2015-08-17
updated=2015-08-17
type=page
status=published
navorder=7
~~~~~~

Interface | Method | Use Case | Object or Data type Returned 
-- | -- | -- | --
**UtsWsContentController**||||
 |[getContentViews](#getcontentviews)|Retrieve a list of all content views available in the UMLS|ArrayList\<ContentViewDTO\>
 |[getContentView](#getcontentview)|Retrieve information about a particular content view given its identifier|ContentViewDTO
 |[getContentViewSourceConceptMembers]|Retrieve all source concepts (and perhaps store them locally) that belong to a particular content view|ArrayList\<SourceConceptContentViewMemberDTO\>
 |[getContentViewAtomMembers]|Retrieve all atoms (and perhaps store them locally) that belong to a particular content view|ArrayList\<AtomContentViewMemberDTO\>
 
 
**Method Signature:** ```getContentViews(String ticket,String version,PSF psf)```

#### Sample Input (Java):

~~~~
gov.nih.nlm.uts.webservice.content.Psf myPsf = new gov.nih.nlm.uts.webservice.content.Psf();
 java.util.List<ContentViewDTO> myAtoms = new ArrayList<ContentViewDTO>();
 myContentViews = utsContentService.getContentViews(ticket, umlsRelease, myPsf);

 for (int i = 0; i < myContentViews.size(); i++) {
 ContentViewDTO myContentViewDTO = myContentViews.get(i);
 String name = myContentViewDTO.getName();
 int atommembercnt = myContentViewDTO.getAtomMemberCount();
 String contributor = myContentViewDTO.getContributor();
 String contributorurl = myContentViewDTO.getContributorURL();
 }
 
~~~~

#### Sample Input (C#):

~~~~
content.psf myPsf = new content.psf();
 content.contentViewDTO[] myContentViews =  utsContentService.getContentViews(ticket, "2012AA", myPsf);
 for (int i = 0; i < myContentViews.Length; i++) {
 content.contentViewDTO myContentViewDTO = myContentViews[i];
 string name = myContentViewDTO.name;
 int atommembercnt = myContentViewDTO.atomMemberCount;
 string contributor = myContentViewDTO.contributor;\
 string contributorurl = myContentViewDTO.contributorURL;
  }
~~~~

#### Sample Output:


Content Name|Content AtomMemCount|Content Contributer|Content ContributerURL
--- |--- | --- | --- 
MetaMap NLP View|3494896|Dr. Alan (Lan) R. Aronson|http://ii-public.nlm.nih.gov/Xfer/ContentView/
UMLS enhanced VA/KP Problem List Subset of SNOMED (Level 0+SNOMED)|192014|Veterans Health Administration, Kaiser Permanente|ftp://ftp1.nci.nih.gov/pub/cacore/EVS/FDA/ProblemList/
UMLS enhanced VA/KP Problem List Subset of SNOMED (Level 0+SNOMED+MDR)|213615|Veterans Health Administration, Kaiser Permanente|ftp://ftp1.nci.nih.gov/pub/cacore/EVS/FDA/ProblemList/
CORE Problem List Subset of SNOMED CT|0|National Library of Medicine|http://www.nlm.nih.gov/research/umls/Snomed/core_subset.html


>


**Method:**getContentView(String ticket,String version,String conceptId)

**Returns:**ArrayList<ContentViewDTO>(see javadocs)(javadocs/gov/nih/nlm/umls/dto/content/ContentViewDTO.html)


**Use Case:**Given a UMLS release and a concept unique identifier (CUI) for a content view, this call returns meta-data about the queried content view in the specified release, such as the name CUI of the content view, the atom member count, contributer, and a description of the content view.

#### Sample Input (Java):

~~~~
ContentViewDTO myContentView = new ContentViewDTO();
 myContentView = utsContentService.getContentView(ticket, umlsRelease, "C2711988");

 String name = myContentView.getName();
 int atommembercnt = myContentView.getAtomMemberCount();
 String contributor = myContentView.getContributor();
 String contributorurl = myContentView.getContributorURL();
~~~~

#### Sample Input (C#):

~~~~
content.contentViewDTO myContentView = utsContentService.getContentView(ticket, "2011AB", "C2711988");
 string name = myContentView.name;
 int atommembercnt = myContentView.atomMemberCount; 
 string contributor = myContentView.contributor;
 string contributorurl = myContentView.contributorURL;
~~~~

#### Sample Output:

~~~~
Content Name | Content AtomMemCount  | Content Contributer  | Content ContributerURL  
CORE Problem List Subset of SNOMED CT |  0   |  National Library of Medicine |  http://www.nlm.nih.gov/research/umls/Snomed/core_subset.html          
~~~~
>

**Method:**getAtomContentViewMemberships(String ticket,String version,String atomId,PSF psf)

**Returns:**ArrayList<AtomContentViewMemberDTO>(see javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/content/AtomContentViewMemberDTO.html)

**Use Case:** Given a UMLS release and an atom unique identifier (AUI), this call returns details of the supplied atom identifier and all content view identifiers for content views that contain the atom as a member.

#### Sample Input (Java):

~~~~
gov.nih.nlm.uts.webservice.content.Psf myPsf = new gov.nih.nlm.uts.webservice.content.Psf();
 java.util.List<AtomContentViewMemberDTO> myAtoms = new ArrayList<AtomContentViewMemberDTO>();
 myAtomContentViewMember = utsContentService.getAtomContentViewMemberships(ticket, umlsRelease, "A2878777", myPsf);

 for (int i = 0; i < myAtomContentViewMember.size(); i++) {
 AtomContentViewMemberDTO myAtomContentViewMemberDTO = myAtomContentViewMember.get(i);
 String ui = myAtomContentViewMemberDTO.getAtom().getConcept().getUi();
 String defprefname = myAtomContentViewMemberDTO.getAtom().getConcept().getDefaultPreferredName();
 String contviewhandle = myAtomContentViewMemberDTO.getContentViewHandle();
 String termtype = myAtomContentViewMemberDTO.getAtom().getTermType();
 }
~~~~

#### Sample Input (C#):

~~~~
content.psf myPsf = new content.psf();
 content.atomContentViewMemberDTO[] myAtomContentViewMember= utsContentService.getAtomContentViewMemberships(ticket, "2011AB", "A2878777", myPsf);
 for (int i = 0; i < myAtomContentViewMember.Length; i++) {
 content.atomContentViewMemberDTO myAtomContentViewMemberDTO = myAtomContentViewMember[i];
 string ui = myAtomContentViewMemberDTO.atom.concept.ui;
 string defprefname = myAtomContentViewMemberDTO.atom.concept.defaultPreferredName;
 string contviewhandle = myAtomContentViewMemberDTO.contentViewHandle;
 string termtype = myAtomContentViewMemberDTO.atom.termType;
 }
~~~~

#### Sample Output:

Content UI |  Content DefPrefName |  Content ContentViewHandle |  Content TermType 
--- | --- | --- | --- 
C0004096   |  Asthma  |  IC1964027   | PT   
C0004096   |  Asthma |IC1964028  | PT     
C0004096  |   Asthma | IC1700357  | PT  

>

**Method:**getSourceConceptContentViewMemberships(String ticket,String version,String sourceConceptId,String rootSourceAbbreviation,PSF psf)

**Returns:**ArrayList<SourceConceptContentViewMemberDTO>(see javadocs)(javadocs/gov/nih/nlm/umls/dto/content/SourceConceptContentViewMemberDTO.html)

**Use Case:** Given a UMLS release and a source-asserted concept unique identifier (SCUI), a release and a root source abbreviation (RSAB), this call returns the content view identifier information for the content view of which the SCUI is a member.


#### Sample Input (Java):

~~~~
gov.nih.nlm.uts.webservice.content.Psf myPsf = new gov.nih.nlm.uts.webservice.content.Psf();
 java.util.List<SourceConceptContentViewMemberDTO> myAtoms = new ArrayList<SourceConceptContentViewMemberDTO>();
 mySourceConceptContentViewMember = utsContentService.getSourceConceptContentViewMemberships(ticket, umlsRelease, "195967001", "SNOMEDCT", myPsf);

 for (int i = 0; i < mySourceConceptContentViewMember.size(); i++) {
 SourceConceptContentViewMemberDTO mySourceConceptCont = mySourceConceptContentViewMember.get(i);
 String ui = mySourceConceptCont.getSourceConcept().getUi();
 String name = mySourceConceptCont.getSourceConcept().getDefaultPreferredName();
 String contviewhandle = mySourceConceptCont.getContentViewHandle();
 int attributeCount = mySourceConceptCont.getSourceConcept().getCVMemberCount();
 }
~~~~

#### Sample Input (C#):

~~~~
content.psf myPsf = new content.psf();
content.sourceConceptContentViewMemberDTO[] mySourceConceptContentViewMember = utsContentService.getSourceConceptContentViewMemberships(ticket, "2012AA", "195967001", "SNOMEDCT", myPsf);
 for (int i = 0; i < mySourceConceptContentViewMember.Length; i++) {
 content.sourceConceptContentViewMemberDTO mySourceConceptContentViewMemberDTO = mySourceConceptContentViewMember[i];
 string ui = mySourceConceptContentViewMemberDTO.sourceConcept.ui;
 string name = mySourceConceptContentViewMemberDTO.sourceConcept.defaultPreferredName;
 string contviewhandle = mySourceConceptContentViewMemberDTO.contentViewHandle;
 int attributeCount = mySourceConceptContentViewMemberDTO.sourceConcept.cVMemberCount;
 }
~~~~

#### Sample Output:

Content Ui |  Content Name | ContentView Handle  | ContentView Member count              
--- | --- | --- | ---        
195967001   |   Asthma | IC2711988   |  1  
>

**Method:**getContentViewAtomMembers(String ticket,String version,String conceptId,PSF psf)

**Returns:**ArrayList<AtomContentViewMemberDTO>(see javadocs)(javadocs/gov/nih/nlm/umls/dto/content/AtomContentViewMemberDTO.html)

**Use Case:** Given a release and a concept unique identifier (CUI) for a content view, this call returns all the atoms that are members of the supplied content view.

#### Sample Input (Java):

~~~~
gov.nih.nlm.uts.webservice.content.Psf myPsf = new gov.nih.nlm.uts.webservice.content.Psf();
 java.util.List<AtomContentViewMemberDTO> myAtoms = new ArrayList<AtomContentViewMemberDTO>();
 myAtomContentViewMember = utsContentService.getContentViewAtomMembers(ticket, umlsRelease, "C1700357", myPsf);

 for (int i = 0; i < myAtomContentViewMember.size(); i++) {
 AtomContentViewMemberDTO myAtomContentViewMemberDTO = myAtomContentViewMember.get(i);
 String ui = myAtomContentViewMemberDTO.getAtom().getConcept().getUi();
 String defprefname = myAtomContentViewMemberDTO.getAtom().getConcept().getDefaultPreferredName();
 String contviewhandle = myAtomContentViewMemberDTO.getContentViewHandle();
 String termtype = myAtomContentViewMemberDTO.getAtom().getTermType();
 }
~~~~

#### Sample Input (C#):

~~~~
content.psf myPsf = new content.psf();
 content.atomContentViewMemberDTO[] myAtomContentViewMember = utsContentService.getContentViewAtomMembers(ticket, "2011AB", "C1700357", myPsf);
 for (int i = 0; i < myAtomContentViewMember.Length; i++) {

 content.atomContentViewMemberDTO myAtomContentViewMemberDTO = myAtomContentViewMember[i];
 string ui = myAtomContentViewMemberDTO.atom.concept.ui;
 string defprefname = myAtomContentViewMemberDTO.atom.concept.defaultPreferredName;
 string contviewhandle = myAtomContentViewMemberDTO.contentViewHandle;
 string termtype = myAtomContentViewMemberDTO.atom.termType;
 }
~~~~

#### Sample Output:

Content UI |  Content DefPrefName | Content ContentViewHandle  | Content TermType    
--- | --- | --- | --- 
C2212218  |   adenocarcinoma of scrotum with squamous metaplasia  | IC1700357 |   SY  
C2212220    | adenocarcinoma of scrotum with spindle cell metaplasia| IC1700357  | PT
 C2212220   |  adenocarcinoma of scrotum with spindle cell metaplasia    |IC1700357|   SY
 C2212221    | adenocarcinoma of scrotum with apocrine metaplasia        |IC1700357  |  PT        
C2212221 |   adenocarcinoma of scrotum with apocrine metaplasia        |IC1700357 |SY 
C2212223  |   nodular melanoma of scrotum     |IC1700357| PT 
C2212224  |   balloon cell melanoma of scrotum   | IC1700357  | PT
>


**Method:**getContentViewSourceConceptMembers(String ticket,String version,String conceptId,PSF psf)

**Returns:**ArrayList<SourceConceptContentViewMemberDTO>(see javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/content/SourceConceptContentViewMemberDTO.html)

**Use Case:** Given a release and a concept unique identifier (CUI) for a content view, this call returns the source-asserted concept identifiers (SCUI) that are members of the supplied content view.

#### Sample Input (Java):

~~~~
gov.nih.nlm.uts.webservice.content.Psf myPsf = new gov.nih.nlm.uts.webservice.content.Psf();
 java.util.List<SourceConceptContentViewMemberDTO> myAtoms = new ArrayList<SourceConceptContentViewMemberDTO>();
 mySourceConceptContentViewMember = utsContentService.getContentViewSourceConceptMembers(ticket, umlsRelease, "C2711988", myPsf);
 for (int i = 0; i < mySourceConceptContentViewMember.size(); i++) {
 SourceConceptContentViewMemberDTO mySourceConceptCont = mySourceConceptContentViewMember.get(i);
 String ui = mySourceConceptCont.getSourceConcept().getUi();
 String name = mySourceConceptCont.getSourceConcept().getDefaultPreferredName();
 String contviewhandle = mySourceConceptCont.getContentViewHandle();
 int attributeCount = mySourceConceptCont.getSourceConcept().getCVMemberCount();
 }
~~~~

#### Sample Input (C#):

~~~~
content.psf myPsf = new content.psf();
 content.sourceConceptContentViewMemberDTO[] mySourceConceptContentViewMember = utsContentService.getContentViewSourceConceptMembers(ticket, "2011AB", "C2711988", myPsf);
 for (int i = 0; i < mySourceConceptContentViewMember.Length; i++) {
 content.sourceConceptContentViewMemberDTO mySourceConceptContentViewMemberDTO = mySourceConceptContentViewMember[i];
 string ui = mySourceConceptContentViewMemberDTO.sourceConcept.ui;
 string name = mySourceConceptContentViewMemberDTO.sourceConcept.defaultPreferredName;
 string contviewhandle = mySourceConceptContentViewMemberDTO.contentViewHandle;
 int attributeCount = mySourceConceptContentViewMemberDTO.sourceConcept.cVMemberCount;
 }
~~~~

#### Sample Output:

Content Source Concept Ui  | Content Name   | ContentView Hanlde |  ContentView Member count 
--- | --- | --- | ---|
414581006   |   Laryngopharyngeal reflux   |IC2711988   |   1 
197377009  |Gallbladder calculus with acute cholecystitis and no obstruction   |  IC2711988    |  1    
301913002  |Lesion of eyelid    | IC2711988   |   1    
62120000 |  Unilateral recurrent inguinal hernia     |IC2711988    |    1
52278004  | Unilateral inguinal hernia     | IC2711988    |   1     
