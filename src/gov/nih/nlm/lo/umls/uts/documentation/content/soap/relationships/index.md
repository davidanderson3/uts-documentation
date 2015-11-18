title=Retrieving UMLS Relationship Information from UTS SOAP API
date=2015-08-18
updated=2015-08-18
type=page
status=published
navorder=10
~~~~~~

**Method: **getConceptConceptRelations(String ticket,String version,String conceptId,PSF psf)

**Returns:**ArrayList< ConceptRelationDTO>

**Use Case:** You have a known CUI and want to see if there are any NLM-asserted concept relations to other CUIs. In the example below we display a few results for the CUI-CUI relationships that exist for C0014591, the concept for "epistaxis".

**Note:** RelationDTOs have default sorting on the RootSource field. You can use the PSF object to sort on UI or RelationLabel.

#### Sample Input (Java):

~~~~
gov.nih.nlm.uts.webservice.content.Psf myPsf = new gov.nih.nlm.uts.webservice.content.Psf();
 List<ConceptRelationDTO> myConceptRelationsDTO = new ArrayList<ConceptRelationDTO>();
 myConceptRelationsDTO = utsContentService.getConceptConceptRelations(ticket, 2011AB, "C0014591", myPsf);
 for (int i = 0; i < myConceptRelationsDTO.size(); i++) {
 ConceptRelationDTO myConceptRelationDTO = myConceptRelationsDTO.get(i);
 String otherConceptUi = myConceptRelationDTO.getRelatedConcept().getUi();
 String otherConceptName = myConceptRelationDTO.getRelatedConcept().getDefaultPreferredName();
 String otherConceptRel = myConceptRelationDTO.getRelationLabel();
 String otherConceptRela = myConceptRelationDTO.getAdditionalRelationLabel();
 }
~~~~

#### Sample Input (C#):

~~~~
content.psf myPsf = new content.psf();
 content.conceptRelationDTO[] myConceptRelationsDTO = utsContentService.getConceptConceptRelations(ticket, "2011AB", "C0014591", myPsf);
 for (int i = 0; i < myConceptRelationsDTO.Length; i++){
 content.conceptRelationDTO temp = myConceptRelationsDTO[i];
 string otherConceptUi = temp.relatedConcept.ui;
 string otherConceptName = temp.relatedConcept.defaultPreferredName;
 string otherConceptRel = temp.relationLabel;
 string otherConceptRela = temp.additionalRelationLabel;
 }
~~~~

#### Sample Output:

Concept UI |  Concept Name  | Concept Rel 
--- |--- | --- 
 C1963103  |   Nose Hemorrhage Adverse Event   |RO  
C0426466  |  Nosebleed symptom |  RO     
 C0189064  | Control of epistaxis by cauterization and packing      | RO 
C0188972    | Epistaxis control |RO   
C0189041   |  Transantral ligation of internal maxillary artery for epistaxis   | RO    
C0176350   |  Control of epistaxis by anterior nasal packing  |RO 
C0176354| Control of epistaxis by ligation of the external carotidartery  | RO 
>


**Method: **getCodeCodeRelations(String ticket,String version,String codeId,String rootSourceAbbreviation,PSF psf)

**Returns:**ArrayList< AtomClusterRelationDTO>

**Use Case:** You have a known code from a source and want to see if there are relations to other codes within the source. Below we use an example of the LOINC code 'LP7769-5', the code for 'BDYHGT.MOLEC', or pre-coordinated measurements for body height in LOINC.

#### Sample Input (Java):

~~~~
gov.nih.nlm.uts.webservice.content.Psf myPsf = new gov.nih.nlm.uts.webservice.content.Psf();
 List<AtomClusterRelationDTO> myAtomClusterRelations = new ArrayList<AtomClusterRelationDTO>();
 myAtomClusterRelations = utsContentService.getCodeCodeRelations(ticket, 2011AB, "LP7769-5", "LNC", myPsf);
 for (int i = 0; i < myAtomClusterRelations.size(); i++) {
 AtomClusterRelationDTO myAtomClusterRelationDTO = myAtomClusterRelations.get(i);
 String otherAtomClusterUi = myAtomClusterRelationDTO.getRelatedAtomCluster().getUi();
 String otherAtomClusterName = myAtomClusterRelationDTO.getRelatedAtomCluster().getDefaultPreferredName();
 String otherAtomClusterRel = myAtomClusterRelationDTO.getRelationLabel();
 String otherAtomClusterRela = myAtomClusterRelationDTO.getAdditionalRelationLabel();
 }
~~~~

#### Sample Input (C#):

~~~~
content.psf myPsf = new content.psf();
 content.atomClusterRelationDTO[] myAtomClusterRelations = utsContentService.getCodeCodeRelations(ticket, "2011AB", "LP7769-5","LNC", myPsf);
 for (int i = 0; i < myAtomClusterRelations.Length; i++){
 content.atomClusterRelationDTO temp = myAtomClusterRelations[i];
 string otherAtomClusterUi = temp.relatedAtomCluster.ui;
 string otherAtomClusterName = temp.relatedAtomCluster.defaultPreferredName;
 string otherAtomClusterRel = temp.relationLabel;
 string otherAtomClusterRela = temp.additionalRelationLabel;
 }
~~~~

#### Sample Output:

 CODE REL |  CODE Rela |  CODE Name   | CODE UI 
 --- |--- | --- | --- 
RO      |   class_of |  Body height\^standing:Length:Point in time:\^Patient:Quantitative  |    8308-9  
RO       |  class_of  | Body height\^pre surgery:Length:Point in time:^Patient:Quantitative | 8307-1   
RO      |   class_of |  Body height\^post partum:Length:Point in time:^Patient:Quantitative  | 8305-5 
RO       |  class_of |  Body height\^lying:Length:Point in time:\^Patient:Quantitative  | 8306-3     
RO       |  class_of  | Body height:Percentile:Point in time:\^Patient:Quantitative  |  8303-0    
>

**Method: **getCodeSourceConceptRelations(String ticket,String version,String codeId,String rootSourceAbbreviation,PSF psf)

**Returns:**ArrayList< AtomClusterRelationDTO>

**Use Case:** Given a UMLS release, a root source abbreviation (RSAB) and a code, this call returns relations that link the code to a source concept (SCUI).

#### Sample Input (Java):

~~~~
gov.nih.nlm.uts.webservice.content.Psf myPsf = new gov.nih.nlm.uts.webservice.content.Psf();
 List<AtomClusterRelationDTO> myAtomClusterRelations = new ArrayList<AtomClusterRelationDTO>();
 myAtomClusterRelations = utsContentService.getCodeSourceConceptRelations(ticket, umlsRelease, "579.0", "ICD9CM", myPsf);
 for (int i = 0; i < myAtomClusterRelations.size(); i++) {
 AtomClusterRelationDTO myAtomClusterRelationDTO = myAtomClusterRelations.get(i);
 String otherAtomClusterUi = myAtomClusterRelationDTO.getRelatedAtomCluster().getUi();
 String otherAtomClusterName = myAtomClusterRelationDTO.getRelatedAtomCluster().getDefaultPreferredName();
 String otherAtomClusterRel = myAtomClusterRelationDTO.getRelationLabel();
 String otherAtomClusterRela = myAtomClusterRelationDTO.getAdditionalRelationLabel();
 }
~~~~

#### Sample Input (C#):

~~~~
content.psf myPsf = new content.psf();
 content.atomClusterRelationDTO[] myAtomClusterRelations = utsContentService.getCodeSourceConceptRelations (ticket, "2011AB","579.0", "ICD9CM", myPsf);
 for (int i = 0; i < myAtomClusterRelations.Length; i++){

 content.atomClusterRelationDTO myAtomClusterRelationDTO = myAtomClusterRelations[i];
 string otherAtomClusterUi = myAtomClusterRelationDTO.relatedAtomCluster.ui;
 string otherAtomClusterName = myAtomClusterRelationDTO.relatedAtomCluster.defaultPreferredName;
 string otherAtomClusterRel = myAtomClusterRelationDTO.relationLabel;
 string otherAtomClusterRela = myAtomClusterRelationDTO.additionalRelationLabel;
 }
~~~~

#### Sample Output:

SourceConceptName   | SourceConceptUi  | SourceConceptRel |  SourceConceptRela
--- |--- | --- | ---    
Adult form of celiac disease|  91867008 | RB    | mapped_from              
Transient gluten sensitivity  | 61712006 |    RB | mapped_from            
Acquired celiac disease | 197479008  | RB   |  mapped_from
Celiac infantilism  | 45259000 | RQ    |  mapped_from                                                               |
>

**Method: **getCodeSourceDescriptorRelations(String ticket,String version,String codeId,String rootSourceAbbreviation,PSF psf)

**Returns:** ArrayList< AtomClusterRelationDTO>

**Use Case:** Given a UMLS release, root source abbreviation (RSAB) and a code, this call returns relations that link the code to a source descriptor (SDUI).


#### Sample Input (Java):

~~~~
gov.nih.nlm.uts.webservice.content.Psf myPsf = new gov.nih.nlm.uts.webservice.content.Psf();
 List<AtomClusterRelationDTO> myAtomClusterRelations = new ArrayList<AtomClusterRelationDTO>();
 myAtomClusterRelations = utsContentService.getCodeSourceDescriptorRelations(ticket, umlsRelease, "U000005", "MSH", myPsf);
 for (int i = 0; i < myAtomClusterRelations.size(); i++) {
 AtomClusterRelationDTO myAtomClusterRelationDTO = myAtomClusterRelations.get(i);
 String otherAtomClusterUi = myAtomClusterRelationDTO.getRelatedAtomCluster().getUi();
 String otherAtomClusterName = myAtomClusterRelationDTO.getRelatedAtomCluster().getDefaultPreferredName();
 String otherAtomClusterRel = myAtomClusterRelationDTO.getRelationLabel();
 String otherAtomClusterRela = myAtomClusterRelationDTO.getAdditionalRelationLabel();
 }
~~~~

#### Sample Input (C#):

~~~~
content.psf myPsf = new content.psf();
 content.atomClusterRelationDTO[] myAtomClusterRelations = utsContentService.getCodeSourceDescriptorRelations ticket, "2011AB", "U000005", "MSH", myPsf);
 for (int i = 0; i < myAtomClusterRelations.Length; i++){
 content.atomClusterRelationDTO myAtomClusterRelationDTO = myAtomClusterRelations[i];
 string otherAtomClusterUi = myAtomClusterRelationDTO.relatedAtomCluster.ui;
 string otherAtomClusterName = myAtomClusterRelationDTO.relatedAtomCluster.defaultPreferredName;
 string otherAtomClusterRel = myAtomClusterRelationDTO.relationLabel;
 string otherAtomClusterRela = myAtomClusterRelationDTO.additionalRelationLabel;
~~~~

#### Sample Output:

SourceDescriptorUi| SourceDescriptorName| SourceDescriptorRel| SourceDescriptorRela    
 --- |--- | --- | ---                                                                 |
D001697  |Biomedical and Dental Materials    |PAR
D020164 | Chemical Actions   and Uses  |PAR      
D045424  |Complex Mixtures |  PAR 
D045762  | Enzymes and Coenzymes    |   PAR 
D009706    |  Nucleic Acids,  Nucleotides, and  Nucleosides     | PAR
D000602  | Amino Acids,   Peptides, and Proteins    | PAR 
>


**Method: **getCodeAtomRelations(String ticket,String version,String codeId,String rootSourceAbbreviation,PSF psf)

**Returns:** ArrayList< AtomRelationDTO>

**Use Case:** Given a UMLS release, root source abbreviation (RSAB) and  a code, this call returns relations between the code and atoms, as well as details of the atoms.

#### Sample Input (Java):

~~~~
gov.nih.nlm.uts.webservice.content.Psf myPsf = new gov.nih.nlm.uts.webservice.content.Psf();
 List<AtomRelationDTO> myAtomsRel = new ArrayList<AtomRelationDTO>();
 myAtomsRel = utsContentService.getCodeAtomRelations(ticket, "2012AA","CDR0000039759","PDQ",myPsf);
 for (int i = 0; i < myAtomsRel.size(); i++) {
 AtomRelationDTO myAtomDTO = myAtomsRel.get(i);
 String ui = myAtomDTO.getRelatedAtom().getUi();
 String name = myAtomDTO.getRelatedAtom().getTermString().getName();
 String rellabel = myAtomDTO.getRelationLabel();
 String arellabel = myAtomDTO.getAdditionalRelationLabel();
 }
~~~~

#### Sample Input (C#):

~~~~
content.psf myPsf = new content.psf();
 content.atomRelationDTO[] myAtomsRel = utsContentService.getCodeAtomRelations(ticket, "2011AB", "CDR0000039759", "PDQ", myPsf);
 for (int i = 0; i < myAtomsRel.Length; i++){
 content.atomRelationDTO myAtomDTO = myAtomsRel[i];
 string ui = myAtomDTO.relatedAtom.ui;
 string name = myAtomDTO.relatedAtom.termString.name;
 string rellabel = myAtomDTO.relationLabel;
 string arellabel = myAtomDTO.additionalRelationLabel;
~~~~

#### Sample Output:

Atom UI|Atom Name|Atom RelLabel|Atom AddRelLabel
--- |--- | --- | --- 
A4357097|cisplatin/ifosfamide/mesna/mitomycin|RO|component_of
A4356583|etoposide/ifosfamide/mesna|RO|component_of
A4356606|ifosfamide/mesna/mitoxantrone|RO|component_of
A4358160|carboplatin/ifosfamide/mesna|RO|component_of
A4358158|carboplatin/filgrastim/ifosfamide/mesna|RO|component_of
A4357213|etoposide/ifosfamide/mesna/topotecan|RO|component_of

>

**Method: **getSourceConceptCodeRelations(String ticket,String version,String sourceConceptId,String rootSourceAbbreviation,PSF psf)

**Returns:**ArrayList< AtomClusterRelationDTO>

**Use Case:** This method takes a source-asserted concept and retrieves its relationship to a code. In the example below, we use the SNOMED CT concept id 32337007, or "microdontia" In this case, a mapping is revealed between the SNOMED CT Concept Id and ICD10CM code 520.2, "Abnormalities of size and form of teeth" code

#### Sample Input (Java):

~~~~
gov.nih.nlm.uts.webservice.content.Psf myPsf = new gov.nih.nlm.uts.webservice.content.Psf();
 List<AtomClusterRelationDTO> myAtomClusterRelations = new ArrayList<AtomClusterRelationDTO>();
 myAtomClusterRelations = utsContentService.getSourceConceptCodeRelations(ticket, 2011AB, "32337007", "SNOMEDCT", myPsf);
 for (int i = 0; i < myAtomClusterRelations.size(); i++) {
 AtomClusterRelationDTO myAtomClusterRelationDTO =myAtomClusterRelations.get(i);
 String otherAtomClusterUi =myAtomClusterRelationDTO.getRelatedAtomCluster().getUi();
 String otherAtomClusterName =myAtomClusterRelationDTO.getRelatedAtomCluster().getDefaultPreferredName();
 String otherAtomClusterRel =myAtomClusterRelationDTO.getRelationLabel();
 String otherAtomClusterRela =myAtomClusterRelationDTO.getAdditionalRelationLabel();
 }
~~~~

#### Sample Input (C#):

~~~~
content.psf myPsf = new content.psf();
 content.atomClusterRelationDTO[] myAtomClusterRelations = utsContentService.getSourceConceptCodeRelations (ticket, "2011AB","32337007", "SNOMEDCT", myPsf);
 for (int i = 0; i < myAtomClusterRelations.Length; i++){
 content.atomClusterRelationDTO temp = myAtomClusterRelations[i];
 string otherAtomClusterUi = temp.relatedAtomCluster.ui;
 string otherAtomClusterName =temp.relatedAtomCluster.defaultPreferredName;
 string otherAtomClusterRel = temp.relationLabel;
 string otherAtomClusterRela = temp.additionalRelationLabel;
 }
~~~~


#### Sample Output:

CODE REL |  CODE Rela |   CODE Name  |  CODE UI   
--- |--- | --- | ---       
 RQ  | mapped_to |  Abnormalities of size and form of teeth |  520.2    
     
>

**Method: **getSourceConceptSourceConceptRelations(String ticket,String version,String sourceConceptId,String rootSourceAbbreviation,PSF psf)

**Returns:** ArrayList< AtomClusterRelationDTO>

**Use Case:** You have a source concept from a known source vocabulary and want to see all of the source-asserted relations to other source concepts within that source. Below we see all the relations between the SNOMED CT ConceptId "262790002" (for "Esophogeal hematoma") and other SNOMED CT source concepts.


#### Sample Input (Java):

~~~~
gov.nih.nlm.uts.webservice.content.Psf myPsf = new gov.nih.nlm.uts.webservice.content.Psf();
 List<AtomClusterRelationDTO> myAtomClusterRelations = new ArrayList<AtomClusterRelationDTO>();
 myAtomClusterRelations =utsContentService.getSourceConceptSourceConceptRelations(ticket, 2011AB,"262790002", "SNOMEDCT", myPsf);
 for (int i = 0; i < myAtomClusterRelations.size(); i++) {
 AtomClusterRelationDTO myAtomClusterRelationDTO =myAtomClusterRelations.get(i);
 String otherAtomClusterUi =myAtomClusterRelationDTO.getRelatedAtomCluster().getUi();
 String otherAtomClusterName =myAtomClusterRelationDTO.getRelatedAtomCluster().getDefaultPreferredName();
 String otherAtomClusterRel =myAtomClusterRelationDTO.getRelationLabel();
 String otherAtomClusterRela =myAtomClusterRelationDTO.getAdditionalRelationLabel();
 }
~~~~


#### Sample Input (C#):

~~~~
content.psf myPsf = new content.psf();
 content.atomClusterRelationDTO[] myAtomClusterRelations =utsContentService.getSourceConceptSourceConceptRelations (ticket,"2011AB", "262790002", "SNOMEDCT", myPsf);
 for (int i = 0; i < myAtomClusterRelations.Length; i++){
 string otherAtomClusterUi =myAtomClusterRelationDTO.relatedAtomCluster.ui;
 string otherAtomClusterName =myAtomClusterRelationDTO.relatedAtomCluster.defaultPreferredName;
 string otherAtomClusterRel = myAtomClusterRelationDTO.relationLabel;
 string otherAtomClusterRela =myAtomClusterRelationDTO.additionalRelationLabel;
 }
~~~~


#### Sample Output:

 Source Concept REL  | Source Concept Rela | Source Concept Name |  Source Concept UI 
 --- |--- | --- | --- 
CHD    |  isa     |  Hematoma    | 385494008       
RO  | has_associated_morphology  | Hematoma   | 35566002      
RO  |  has_severity | Severities    | 272141005         
CHD |  isa    |  Esophageal bleeding | 15238002    
CHD |   isa | Mass of digestive structure  |  300855001   
RO  |  has_finding_site   |    Esophageal structure |    32849002       
RO   |has_episodicity | Episodicities  | 288526004                
 PAR    |    inverse_isa     |  Intramural esophageal hematoma |  15970005              
 RO  |  has_clinical_course   |     Courses   |288524001 
>

**Method: **getSourceConceptAtomRelations(String ticket,String version,String sourceConceptId,String rootSourceAbbreviation,PSF psf)

**Returns:**ArrayList< AtomRelationDTO>

**Use Case:** Given a UMLS release, root source abbreviation (RSAB) and a source concept identifier (SCUI), this call returns the relations that link the supplied source concept identifier to an atom, and gives details about the atom.

#### Sample Input (Java):

~~~~

gov.nih.nlm.uts.webservice.content.Psf myPsf = new gov.nih.nlm.uts.webservice.content.Psf();
 List<AtomRelationDTO> myAtomsRel = new ArrayList<AtomRelationDTO>();
 myAtomsRel = utsContentService.getSourceConceptAtomRelations(ticket,umlsRelease,"441806004","SNOMEDCT",myPsf);
 for (int i = 0; i < myAtomsRel.size(); i++) {
 AtomRelationDTO myAtomDTO = myAtomsRel.get(i);
 String ui = myAtomDTO.getRelatedAtom().getUi();
 String name = myAtomDTO.getRelatedAtom().getTermString().getName();
 String rellabel = myAtomDTO.getRelationLabel();
 String arellabel = myAtomDTO.getAdditionalRelationLabel();
 }
~~~~


#### Sample Input (C#):

~~~~
content.psf myPsf = new content.psf();
 content.atomRelationDTO[] myAtomsRel =
utsContentService.getSourceConceptAtomRelations(ticket, "2012AA","441806004", "SNOMEDCT", myPsf);
 for (int i = 0; i < myAtomsRel.Length; i++){
 content.atomRelationDTO myAtomDTO = myAtomsRel[i];
 string ui = myAtomDTO.relatedAtom.ui;
 string name = myAtomDTO.relatedAtom.termString.name;
 string rellabel = myAtomDTO.relationLabel;
 string arellabel = myAtomDTO.additionalRelationLabel;
~~~~


#### Sample Output:

Atom UI   |  Atom Name  |   Atom RelLabel |  Atom AddRelLabel   
--- |--- | --- | --- 
A16953870 |  Brain abscess  | RO   |  refers_to       
>


**Method: **getSourceDescriptorCodeRelations(String ticket,String version,String sourceDescriptorId,String rootSourceAbbreviation,PSF psf)

**Returns:** ArrayList< AtomClusterRelationDTO>

**Use Case:** Given a UMLS release, root source abbreviation (RSAB) and source descriptor identifier (SDUI), this call returns the relations that link the supplied source descriptor identifier to a code, and gives details of the code.

#### Sample Input (Java):

~~~~
gov.nih.nlm.uts.webservice.content.Psf myPsf = new gov.nih.nlm.uts.webservice.content.Psf();
 List<AtomClusterRelationDTO> myAtomClusterRelations = new ArrayList<AtomClusterRelationDTO>();
 myAtomClusterRelations =utsContentService.getSourceDescriptorCodeRelations(ticket, umlsRelease,"D001419", "MSH", myPsf);
 for (int i = 0; i < myAtomClusterRelations.size(); i++) {
 AtomClusterRelationDTO myAtomClusterRelationDTO =myAtomClusterRelations.get(i);
 String otherAtomClusterUi =myAtomClusterRelationDTO.getRelatedAtomCluster().getUi();
 String otherAtomClusterName =myAtomClusterRelationDTO.getRelatedAtomCluster().getDefaultPreferredName();
 String otherAtomClusterRel =myAtomClusterRelationDTO.getRelationLabel();
 String otherAtomClusterRela =myAtomClusterRelationDTO.getAdditionalRelationLabel();
 }
~~~~


#### Sample Input (C#):

~~~~
content.psf myPsf = new content.psf();
 content.atomClusterRelationDTO[] myAtomClusterRelations =utsContentService.getSourceDescriptorCodeRelations (ticket, "2011AB","D001419", "MSH", myPsf);
 for (int i = 0; i < myAtomClusterRelations.Length; i++){
 content.atomClusterRelationDTO myAtomClusterRelationDTO =myAtomClusterRelations[i];
 string otherAtomClusterUi =myAtomClusterRelationDTO.relatedAtomCluster.ui;
 string otherAtomClusterName =myAtomClusterRelationDTO.relatedAtomCluster.defaultPreferredName;
 string otherAtomClusterRel = myAtomClusterRelationDTO.relationLabel;
 string otherAtomClusterRela =myAtomClusterRelationDTO.additionalRelationLabel;
 }
~~~~


#### Sample Output:

Source Descriptor Code UI | Source Descriptor Code Name | Source Descriptor Code Rel |  Source Descri Code Rela  
--- |--- | --- | ---     
U000012    | Organisms (MeSH Category)    |CHD|
>

**Method: **getSourceDescriptorSourceDescriptorRelations(String ticket,String version,String sourceDescriptorId,String rootSourceAbbreviation,PSF psf)

**Returns:** ArrayList< AtomClusterRelationDTO>

**Use Case:** You have a known Source Descriptor UI from a known source vocabulary, and want to retrieve all of its relations to other Source Descriptors. The example below uses the MeSH Descriptor for 'Cardiomegaly', D006332. We also set the PSF object to only include sibling and parent relationships.

#### Sample Input (Java):

~~~~
UtsMetathesaurusContent.Psf myPsf = new UtsMetathesaurusContent.Psf();
 myPsf.getIncludedRelationLabels().add("SIB");
 myPsf.getIncludedRelationLabels().add("PAR");
 List<AtomClusterRelationDTO> myAtomClusterRelations = new ArrayList<AtomClusterRelationDTO>();
 myAtomClusterRelations =utsContentService.getSourceDescriptorSourceDescriptorRelations(ticket,2011AB, "D006332", "MSH", myPsf);
 for (int i = 0; i < myAtomClusterRelations.size(); i++) {
 AtomClusterRelationDTO myAtomClusterRelationDTO =myAtomClusterRelations.get(i);
 String otherAtomClusterUi =myAtomClusterRelationDTO.getRelatedAtomCluster().getUi();
 String otherAtomClusterName =myAtomClusterRelationDTO.getRelatedAtomCluster().getDefaultPreferredName();
 String otherAtomClusterRel =myAtomClusterRelationDTO.getRelationLabel();
 String otherAtomClusterRela =myAtomClusterRelationDTO.getAdditionalRelationLabel();
 }
~~~~

#### Sample Input (C#):

~~~~
content.psf myPsf = new content.psf();
 string[] tempRelation = new string[2];
 tempRelation[0] = "SIB";
 tempRelation[1] = "PAR";
 myPsf.includedRelationLabels = tempRelation;
 content.atomClusterRelationDTO[] myAtomClusterRelations =utsContentService.getSourceDescriptorSourceDescriptorRelations (ticket,"2011AB", "D006332", "MSH", myPsf);
 for (int i = 0; i < myAtomClusterRelations.Length; i++){
 content.atomClusterRelationDTO myAtomClusterRelationDTO =myAtomClusterRelations[i];
 string otherAtomClusterUi =myAtomClusterRelationDTO.relatedAtomCluster.ui;
 string otherAtomClusterName =myAtomClusterRelationDTO.relatedAtomCluster.defaultPreferredName;
 string otherAtomClusterRel = myAtomClusterRelationDTO.relationLabel;
 string otherAtomClusterRela =myAtomClusterRelationDTO.additionalRelationLabel;
 }

~~~~

#### Sample Output:

 Source Descriptor REL|  Source Descriptor RELA| Source Descriptor Name| Source Descriptor Ui    
 --- |--- | --- | --- 
SIB  |  | Pericardial  | Effusion   |D010490
SIB |     | Cardiac Tamponade         |    D002305      
SIB  |  | Cardiac OutputLow  |D002303
SIB |  | Ventricular   Outflow Obstruction |  D014694      
>

**Method: **getSourceDescriptorAtomRelations(String ticket,String version,String sourceDescriptorId,String rootSourceAbbreviation,PSF psf)

**Returns:** ArrayList< AtomRelationDTO>

**Use Case:** Given a UMLS release, root source abbreviation (RSAB) and source descriptor identifier (SDUI), this call returns the relations that link the supplied source descriptor identifier to its related atoms.


#### Sample Input (Java):

~~~~
gov.nih.nlm.uts.webservice.content.Psf myPsf = new gov.nih.nlm.uts.webservice.content.Psf();
 List<AtomRelationDTO> myAtomsRel = new ArrayList<AtomRelationDTO>();
 myAtomsRel = utsContentService.getSourceDescriptorAtomRelations(ticket, "2012AA","D014028","MSH",myPsf);
 for (int i = 0; i < myAtomsRel.size(); i++) {
 AtomRelationDTO myAtomDTO = myAtomsRel.get(i);
 String ui = myAtomDTO.getRelatedAtom().getUi();
 String name = myAtomDTO.getRelatedAtom().getTermString().getName();
 String rellabel = myAtomDTO.getRelationLabel();
 String arellabel = myAtomDTO.getAdditionalRelationLabel();
 }
~~~~

#### Sample Input (C#):

~~~~
content.psf myPsf = new content.psf();
 content.atomRelationDTO[] myAtomsRel = utsContentService.getSourceDescriptorAtomRelations(ticket, "2012AA","D014028", "MSH", myPsf);
 for (int i = 0; i < myAtomsRel.Length; i++){
 content.atomRelationDTO myAtomDTO = myAtomsRel[i];
 string ui = myAtomDTO.relatedAtom.ui;
 string name = myAtomDTO.relatedAtom.termString.name;
 string rellabel = myAtomDTO.relationLabel;
 string arellabel = myAtomDTO.additionalRelationLabel;
~~~~

#### Sample Output:

Atom UI|Atom Name|Atom RelLabel|Atom AddRelLabel
 --- |--- | --- | --- 
A15660981|Secondhand Smoke|RQ|mapped_from
A15662282|Environmental Tobacco Smoke|RQ|mapped_from
A15662283|Passive Smoking|RQ|mapped_from
A15662628|Smoking, Passive|RQ|mapped_from
>

**Method: **(String ticket,String version,String atomId,PSF psf)

**Returns:** ArrayList< AtomRelationDTO>

**Use Case:** Given a UMLS release and an atom unique identifier (AUI), this call returns relations that link the supplied atom to other atoms.

#### Sample Input (Java):

~~~~
gov.nih.nlm.uts.webservice.content.Psf myPsf = new gov.nih.nlm.uts.webservice.content.Psf();
 List<AtomRelationDTO> myAtomsRel = new ArrayList<AtomRelationDTO>();
 myAtomsRel = utsContentService.getAtomAtomRelations(ticket, "2012AA","A1317707",myPsf);
 for (int i = 0; i < myAtomsRel.size(); i++) {
 AtomRelationDTO myAtomDTO = myAtomsRel.get(i);
 String ui = myAtomDTO.getRelatedAtom().getUi();
 String name = myAtomDTO.getRelatedAtom().getTermString().getName();
 String rellabel = myAtomDTO.getRelationLabel();
 String arellabel = myAtomDTO.getAdditionalRelationLabel();
 }
~~~~

#### Sample Input (C#):

~~~~
content.psf myPsf = new content.psf();
 content.atomRelationDTO[] myAtomsRel = utsContentService.getAtomAtomRelations(ticket, "2012AA", "A1317707",myPsf);
 for (int i = 0; i < myAtomsRel.Length; i++){
 content.atomRelationDTO myAtomDTO = myAtomsRel[i];
 string ui = myAtomDTO.relatedAtom.ui;
 string name = myAtomDTO.relatedAtom.termString.name;
 string rellabel = myAtomDTO.relationLabel;
 string arellabel = myAtomDTO.additionalRelationLabel;
~~~~

#### Sample Output:

Atom UI  |  Atom Name   | Atom RelLabel  | Atom AddRelLabel  
 --- |--- | --- | --- 
A0016514 |  1,2-Dipalmitoyl-Glycerophosphocholine  | SY   |  permuted_term_of          
>


**Method: **getAtomCodeRelations(String ticket,String version,String atomId,PSF psf)

**Returns:** ArrayList< AtomClusterRelationDTO>

**Use Case:** Given a UMLS release and an atom unique identifier (AUI), this call returns relations that link the supplied atom to codes, and gives details of the codes.

#### Sample Input (Java):

~~~~
gov.nih.nlm.uts.webservice.content.Psf myPsf = new gov.nih.nlm.uts.webservice.content.Psf();
 List<AtomClusterRelationDTO> myAtomClusterRelations = new ArrayList<AtomClusterRelationDTO>();
 myAtomClusterRelations = utsContentService.getAtomCodeRelations(ticket,umlsRelease, "A4356606", myPsf);
 for (int i = 0; i < myAtomClusterRelations.size(); i++) {
 AtomClusterRelationDTO myAtomClusterRelationDTO = myAtomClusterRelations.get(i);
 String otherAtomClusterUi =myAtomClusterRelationDTO.getRelatedAtomCluster().getUi();
 String otherAtomClusterName =myAtomClusterRelationDTO.getRelatedAtomCluster().getDefaultPreferredName();
 String otherAtomClusterRel =myAtomClusterRelationDTO.getRelationLabel();
 String otherAtomClusterRela =myAtomClusterRelationDTO.getAdditionalRelationLabel();
}
~~~~

#### Sample Input (C#):

~~~~
content.psf myPsf = new content.psf();
 content.atomClusterRelationDTO[] myAtomClusterRelations =utsContentService.getAtomCodeRelations (ticket, "2011AB", "A4356606",myPsf);
 for (int i = 0; i < myAtomClusterRelations.Length; i++){
 content.atomClusterRelationDTO myAtomClusterRelationDTO =myAtomClusterRelations[i];
 string otherAtomClusterUi =myAtomClusterRelationDTO.relatedAtomCluster.ui;
 string otherAtomClusterName =myAtomClusterRelationDTO.relatedAtomCluster.defaultPreferredName;
 string otherAtomClusterRel = myAtomClusterRelationDTO.relationLabel;
 string otherAtomClusterRela =myAtomClusterRelationDTO.additionalRelationLabel;
 }
~~~~

#### Sample Output:

Code Name  |   Code UI  |  Code Rel |  Code Rela   
 --- |--- | --- | --- 
mitoxantrone hydrochloride |  CDR0000039219 |  RO  |  has_component
mesna        | CDR0000039759   |RO    |  has_component 
ifosfamide   | CDR0000040024   |RO    |has_component

>

**Method: **getAtomSourceConceptRelations(String ticket,String version,String atomId,PSF psf)

**Returns:** ArrayList< AtomClusterRelationDTO>

**Use Case:** Given a UMLS release and an atom unique identifier (AUI), this call returns relations that link the supplied atom to source concepts (SCUI).


#### Sample Input (Java):

~~~~
gov.nih.nlm.uts.webservice.content.Psf myPsf = new gov.nih.nlm.uts.webservice.content.Psf();
 List<AtomClusterRelationDTO> myAtomClusterRelations = new ArrayList<AtomClusterRelationDTO>();
 myAtomClusterRelations =utsContentService.getAtomSourceConceptRelations(ticket, umlsRelease, "A16344698", myPsf);
 for (int i = 0; i < myAtomClusterRelations.size(); i++) {
 AtomClusterRelationDTO myAtomClusterRelationDTO =myAtomClusterRelations.get(i);
 String otherAtomClusterUi =myAtomClusterRelationDTO.getRelatedAtomCluster().getUi();
 String otherAtomClusterName =myAtomClusterRelationDTO.getRelatedAtomCluster().getDefaultPreferredName();
 String otherAtomClusterRel =myAtomClusterRelationDTO.getRelationLabel();
 String otherAtomClusterRela =myAtomClusterRelationDTO.getAdditionalRelationLabel();
 }
~~~~

#### Sample Input (C#):

~~~~
content.psf myPsf = new content.psf();
 content.atomClusterRelationDTO[] myAtomClusterRelations =utsContentService.getAtomSourceConceptRelations (ticket, "2011AB","A16344698", myPsf);
 for (int i = 0; i < myAtomClusterRelations.Length; i++){
 content.atomClusterRelationDTO myAtomClusterRelationDTO =myAtomClusterRelations[i];
 string otherAtomClusterUi =myAtomClusterRelationDTO.relatedAtomCluster.ui;
 string otherAtomClusterName =myAtomClusterRelationDTO.relatedAtomCluster.defaultPreferredName;
 string otherAtomClusterRel = myAtomClusterRelationDTO.relationLabel;
 string otherAtomClusterRela =myAtomClusterRelationDTO.additionalRelationLabel;
 }
~~~~

#### Sample Output:

>

**Method: **getAtomSourceDescriptorRelations(String ticket,String version,String atomId,PSF psf)

**Returns:** ArrayList< AtomClusterRelationDTO>

**Use Case:** Given a UMLS release and an atom unique identifier (AUI), this call returns relations that link the supplied atom to source descriptor unique identifiers (SDUI).

#### Sample Input (Java):

~~~~
gov.nih.nlm.uts.webservice.content.Psf myPsf = new gov.nih.nlm.uts.webservice.content.Psf();
 List<AtomClusterRelationDTO> myAtomClusterRelations = new ArrayList<AtomClusterRelationDTO>();
 myAtomClusterRelations =utsContentService.getAtomSourceDescriptorRelations(ticket, umlsRelease,"A17775421", myPsf);
  for (int i = 0; i < myAtomClusterRelations.size(); i++) {
 AtomClusterRelationDTO myAtomClusterRelationDTO =myAtomClusterRelations.get(i);
 String otherAtomClusterUi =myAtomClusterRelationDTO.getRelatedAtomCluster().getUi();
 String otherAtomClusterName =myAtomClusterRelationDTO.getRelatedAtomCluster().getDefaultPreferredName();
 String otherAtomClusterRel =myAtomClusterRelationDTO.getRelationLabel();
 String otherAtomClusterRela =myAtomClusterRelationDTO.getAdditionalRelationLabel();
 }
~~~~

#### Sample Input (C#):

~~~~
content.psf myPsf = new content.psf();
 content.atomClusterRelationDTO[] myAtomClusterRelations =utsContentService.getAtomSourceDescriptorRelations (ticket, "2011AB","A17775421", myPsf);
 for (int i = 0; i < myAtomClusterRelations.Length; i++){
 content.atomClusterRelationDTO myAtomClusterRelationDTO =myAtomClusterRelations[i];
 string otherAtomClusterUi =myAtomClusterRelationDTO.relatedAtomCluster.ui;
 string otherAtomClusterName =myAtomClusterRelationDTO.relatedAtomCluster.defaultPreferredName;
 string otherAtomClusterRel = myAtomClusterRelationDTO.relationLabel;
 string otherAtomClusterRela =myAtomClusterRelationDTO.additionalRelationLabel;
 }
~~~~

#### Sample Output:

 Source Descriptor Name   |  Source Descriptor UI  | Source Descriptor Rel  | Source Descriptor Rela
  --- |--- | --- | --- 
Abnormalities of size and form of teeth |  K00.2   |     R     |  Q          

>

**Method: **getAtomConceptRelations(String ticket,String version,String atomId,PSF psf)

**Returns:** ArrayList< AtomClusterRelationDTO>

**Use Case:** Given a UMLS release and an atom unique identifier (AUI), this call returns relations that link the supplied atom to atoms in other concepts (CUI).

#### Sample Input (Java):

~~~~
gov.nih.nlm.uts.webservice.content.Psf myPsf = new gov.nih.nlm.uts.webservice.content.Psf();
 List<AtomClusterRelationDTO> myAtomClusterRelations = new ArrayList<AtomClusterRelationDTO>();
 myAtomClusterRelations =utsContentService.getAtomConceptRelations(ticket, umlsRelease,"A0851653", myPsf);
 for (int i = 0; i < myAtomClusterRelations.size(); i++) {
 AtomClusterRelationDTO myAtomClusterRelationDTO =myAtomClusterRelations.get(i);
 String otherAtomClusterUi =myAtomClusterRelationDTO.getRelatedAtomCluster().getUi();
 String otherAtomClusterName =myAtomClusterRelationDTO.getRelatedAtomCluster().getDefaultPreferredName();
 String otherAtomClusterRel =myAtomClusterRelationDTO.getRelationLabel();
 String otherAtomClusterRela =myAtomClusterRelationDTO.getAdditionalRelationLabel();
 }
~~~~

#### Sample Input (C#):

~~~~
content.psf myPsf = new content.psf();
 content.atomClusterRelationDTO[] myAtomClusterRelations =utsContentService.getAtomConceptRelations (ticket, "2011AB", "A0851653",myPsf);
 for (int i = 0; i < myAtomClusterRelations.Length; i++){
 content.atomClusterRelationDTO myAtomClusterRelationDTO =myAtomClusterRelations[i];
 string otherAtomClusterUi =myAtomClusterRelationDTO.relatedAtomCluster.ui;
 string otherAtomClusterName =myAtomClusterRelationDTO.relatedAtomCluster.defaultPreferredName;
 string otherAtomClusterRel = myAtomClusterRelationDTO.relationLabel;
 string otherAtomClusterRela =myAtomClusterRelationDTO.additionalRelationLabel;
 }
~~~~

#### Sample Output:

Concept UI  | Concept Name  | Concept Rel  | Concept Rela 
 --- |--- | --- | --- 
C0343521 |    Hepatic actinomycosis  |    RQ    | clinically_similar  
C0343522   |  Ileocecal actinomycosis      |      RQ  |clinically_similar                 
C0348134   |  Other forms of actinomycosis      |     RQ |clinically_similar                      
C0275558    | Actinomycosis due to Actinomyces israelii   |     RQ  |clinically_similar                     
C0275559    | Actinomycosis due to Actinomyces naeslundii  |    RQ | clinically_similar                           
C1261283  |   Actinomycetoma   |     RQ       |clinically_similar
