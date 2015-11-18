title=Concept History
date=2015-08-13
updated=2015-08-13
type=page
status=published
navorder=6
~~~~~~

**Method: **getBequeathedToConceptCuis(String ticket,String newerVersion,String conceptId,String olderVersion)

**Returns:** ArrayList< String>

**Use Case:** Given a UMLS release and a retired concept identifier (CUI or handle), this call returns the new CUI (or CUIs) to which the retired concept was bequeathed. In other words, if a CUI has been retired, the retired CUI is mapped as a synonym to a new CUI. The retired CUI can be mapped to a single CUI or to multiple CUIs.

#### Sample Input (Java):

~~~~
myarrString = utsHistoryService.getBequeathedToConceptCuis(ticket, umlsRelease, "C2962996", "2011AA");
 for (int i = 0; i < myarrString.size(); i++) {
 String myarrstr = myarrString.get(i);
 String intern = myarrstr.intern();
 int hashcode = myarrstr.intern().hashCode();
 }
~~~~

#### Sample Output:

Intern    | Intern-Hashcode   
--- | --- 
C0012522 |  1875673041      
C0020268  | 1876534227   
C0028741  | 1876777291       
 C0039644  | 1877729645   
>

**Method: **getConceptBequeathals(String ticket,String newerVersion,String conceptId,String olderVersion)

**Returns:** ArrayList< ConceptBequeathalDTO>

**Use Case:** **There are four ways to run this method:**
 **1. Default case:** When valid values are provided for all parameters, this method returns all conceptIds bequeathed to the conceptId given as a parameter, the olderVersion being the UMLS release in which the bequeathals became effective.
 The sample code and output for the default case as given in the "Input" and "Output" sections below.

 **2.** When valid values are provided for all parameters, this method returns all conceptIds bequeathed to the conceptId given as a parameter, the olderVersion being the UMLS release in which the bequeathals became effective.
 **Example:** getConceptBequeathals(ticket, newerVersion, "", "");

 **3.** When valid values are provided for all parameters, this method returns all conceptIds bequeathed to the conceptId given as a parameter, the olderVersion being the UMLS release in which the bequeathals became effective.
 **Example:** getConceptBequeathals(ticket, newerVersion, "C0020268", "");

 **4.** When valid values are provided for all parameters, this method returns all conceptIds bequeathed to the conceptId given as a parameter, the olderVersion being the UMLS release in which the bequeathals became effective.
 **Example:** getConceptBequeathals(ticket, newerVersion, "", "2009");


#### Sample Input (Java):

~~~~
myconceptBeqDTO = utsHistoryService.getConceptBequeathals(ticket, umlsRelease, "C0074722", "2010AA");
 for (int i = 0; i < myconceptBeqDTO.size(); i++) {
 ConceptBequeathalDTO myConceptBeq = myconceptBeqDTO.get(i);
 String label = myConceptBeq.getLabel();
 String ui = myConceptBeq.getUi();
 String relConceptUi = myConceptBeq.getRelatedConceptUi();
 String version = myConceptBeq.getVersion();
 }
~~~~

#### Sample Output:

Label |  Ui   |  Related Concept Ui |  Version  
--- | --- | --- | ---
 RB   |   C0914572  | C0074722      |       2010AA     
 RB    |  C0914573 |  C0074722      |       2010AA  
RB     | C1138362  | C0074722      |       2010AA       
 RB    |  C1565767  | C0074722      |       2010AA   
 RO    |  C2364795 |  C0074722     |        2010AA    
RO    |  C2242421  | C0074722      |       2010AA     
RO     | C2345679  | C0074722     |        2010AA    
 RO  |    C2345680 |  C0074722     |        2010AA    
RO    |  C2700791  | C0074722      |       2010AA    
 RO    |  C2710681  | C0074722     |        2010AA    
 RO   |   C2710687 |  C0074722      |       2010AA    
 
>

**Method: **getConceptDeletions(String ticket,String newerVersion,String conceptId,String olderVersion)

**Returns:** ArrayList< ConceptDeathDTO>

**Use Case:** **There are four ways to run this method:**
 **1. Default case:**When valid values are provided for all parameters, this method returns the concepts that were deleted, effective in the olderVersion.
 The sample code and output for the default case as given in the "Input" and "Output" sections below.

 **2.**ConceptId and olderVersion holding empty values, this method returns all the deleted concepts as per the newer version, along with  the concepts that were deleted and the release of deletion.
 **Example:**getConceptDeletions(ticket, newerVersion, "", "");

 **3.**The method returns the concepts that were deleted in the newer version, the conceptId given as a parameter, and olderVersion being optional.
 **Example:**getConceptDeletions(ticket, newerVersion, "C0066997", "");

 **4.**ConceptId being optional, this method returns the concepts that were merged to the given conceptId, effective in the olderVersion.
 **Example:**getConceptDeletions(ticket, newerVersion, " ", "2007AC");


#### Sample Input (Java):

~~~~
myConceptDeathDTO = utsHistoryService.getConceptDeletions(ticket, umlsRelease, "C0066997", "1993AA");
 for (int i = 0; i < myConceptDeathDTO.size(); i++) {
 ConceptDeathDTO myConceptDeath = myConceptDeathDTO.get(i);
 String ui = myConceptDeath.getUi();
 String version = myConceptDeath.getVersion();
 }
~~~~

#### Sample Output:

Ui      |   Version    
--- | ---
C0066997 |  1993AA    
>

**Method: **getConceptMerges(String ticket,String newerVersion,String conceptId,String olderVersion)

**Returns:** ArrayList< ConceptMergeDTO>

**Use Case:** **There are four ways to run this method:**
 **1. Default case:** When valid values are provided for all parameters, this method will return all conceptIds merged to the conceptId given as a parameter, the older version being the UMLS release in which the merges became effective.
 The sample code and output for the default case as given in the "Input" and "Output" sections below.

 **2.**Keeping conceptId and olderVersion optional(using empty values), this method returns all the concepts merged as per the newer version, but effective in the older version, along with the concepts they were merged to and the UMLS release of merging.
 **Example:**getConceptMerges(ticket, newerVersion, " ", "");

 **3.**This method returns the concepts that were merged to the conceptId given as a parameter, as per the newer version, but effective in the older version, olderVersion being optional.
 **Example:**getConceptMerges(ticket, newerVersion, " C0000258", "");

 **4.**ConceptId being optional, this method returns the concepts that were merged to the given conceptId, effective in the olderVersion.
 **Example:**getConceptMerges(ticket, newerVersion, " ", "1993AA");


#### Sample Input (Java):

~~~~
myConceptMergeDTO = utsHistoryService.getConceptMerges(ticket, umlsRelease, "C0000258", "1993AA");
 for (int i = 0; i < myConceptMergeDTO.size(); i++) {
 ConceptMergeDTO myConceptMer = myConceptMergeDTO.get(i);
 String newUi = myConceptMer.getNewConceptUi();
 String ui = myConceptMer.getUi();
 String version = myConceptMer.getVersion();
 String reason = myConceptMer.getReason();
 }
~~~~

#### Sample Output:

New Concept Ui |  Ui    |     Version  
--- | --- | --- 
C0016904   | C0000258  | 1993AA     

>

**Method: **getAtomMovements(String ticket,String version,String atomId)

**Returns:** ArrayList< AtomMovementDTO>

**Use Case:** Given a UMLS release and atom identifier (AUI or handle), this call gives details about atom movements from one concept (OldConceptUi) to another concept (NewConceptUi) and the UMLS release in which the atom movement took place.


#### Sample Input (Java):

~~~~
myAtomMovementDTO = utsHistoryService.getAtomMovements(ticket, umlsRelease, "A0000230");
 for (int i = 0; i < myAtomMovementDTO.size(); i++) {
 AtomMovementDTO myAtomMov = myAtomMovementDTO.get(i);
 String newUi = myAtomMov.getNewConceptUi();
 String oldUi = myAtomMov.getOldConceptUi();
 String ui = myAtomMov.getUi();
 String version = myAtomMov.getVersion();
 }
~~~~

#### Sample Output:

Label    |  Ui    |     Related Concept Ui  | Version   
--- | --- | --- | ---
C0236748 |  C0029220  | A0000230      |       2007AA     

>

**Method: **getSourceAtomChanges(String ticket,String version,String conceptId,String rootSourceAbbreviation,String sourceAtomId)

**Returns:** ArrayList< SourceAtomChangeDTO>

**Use Case:** Given a UMLS release, concept identifier (CUI), root source abbreviation (RSAB) and source-asserted atom identifier(SAUI) this call returns the set of changes that affected the source-asserted
atom.


#### Sample Input (Java):

~~~~
mySrcAtomChange = utsHistoryService.getSourceAtomChanges(ticket, umlsRelease, "C1264709", "SNOMEDCT", "");
 for (int i = 0; i < mySrcAtomChange.size(); i++) {
 SourceAtomChangeDTO myAtomCh = mySrcAtomChange.get(i);
 String key = myAtomCh.getKey();
 String rtSource = myAtomCh.getRootSource();
 String ui = myAtomCh.getUi();
 String srcUi = myAtomCh.getSourceUi();
 String value = myAtomCh.getValue();
 String version = myAtomCh.getVersion();
 }
~~~~

#### Sample Output:

Key     |    Root Source |  Ui |   SourceUi |    Value |  Version         
--- | --- | --- | --- | --- | ---
CONCEPTSTATUS  |     SNOMEDCT   |   C1264709   |117070007  |  0   |    20001101     
CONCEPTSTATUS  |     SNOMEDCT   |   C1264709|   117070007  |  0  |     20020131      
CONCEPTSTATUS   |    SNOMEDCT   |   C1264709  | 117070007 |   0   |    20030731                                                                     |
DESCRIPTIONSTATUS  | SNOMEDCT    |  C1264709 |  1762415011 |  0    |   20030731                                                                     |
DESCRIPTIONSTATUS  | SNOMEDCT    |  C1264709  | 181166019 |   0   |    20001101                                                                     |
DESCRIPTIONSTATUS  | SNOMEDCT    |  C1264709  | 685181012   | 0   |    20020131                                                                     |
DESCRIPTIONSTATUS  | SNOMEDCT    |  C1264709  | 685181012  |  1   |    20030731                                                                     |

