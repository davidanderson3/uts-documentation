title=Semantic Group
date=2015-08-26
updated=2015-08-26
type=page
status=unpublished
navorder=5
~~~~~~


**Method: **getSemanticTypeGroup(String ticket,String version,String semanticGroup)

**Returns:**SemanticTypeGroupDTO

**Use Case:** Given a UMLS release and a semantic type group abbreviation, this call returns the expanded form and abbreviation of the semantic type group, and the semantic type count for the group.


#### Sample Input (Java):

~~~~
mySemTyRelDTO = utsSemanticNetworkService.getSemanticTypeGroup (ticket,umlsRelease, "GEOG");
 String abbreviation = mySemTyRelDTO.getAbbreviation();
 String expandedForm = mySemTyRelDTO.getExpandedForm();
 int semTypeCnt = mySemTyRelDTO.getSemanticTypeCount();
~~~~

#### Sample Output:

~~~~
   Abbreviation: GEOG
   Expanded Form: Geographic Areas
   Semantic Type Count: 1
~~~~
>

**Method: **getSemanticTypeByGroup(String ticket,String version,String semanticGroup)

**Returns:**ArrayList<SemanticTypeDTO>

**Use Case:** Given a UMLS release and a semantic type group abbreviation, this call returns all the semantic types in the given group.


#### Sample Input (Java):

~~~~
myarrSemTyRelDTO = utsSemanticNetworkService.getSemanticTypeByGroup(ticket, umlsRelease, "DISO"); 
for (int i = 0; i < myarrSemTyRelDTO.size(); i++) {
 SemanticTypeDTO mySemTyRel = myarrSemTyRelDTO.get(i);
 String abbreviation = mySemTyRel.getAbbreviation();
 String definition = mySemTyRel.getDefinition();
 int childCnt = mySemTyRel.getChildCount();
 int relCnt = mySemTyRel.getRelationCount();
 String example = mySemTyRel.getExample();
 String nonHuman = mySemTyRel.getNonHuman();
 String treeNum = mySemTyRel.getTreeNumber();
 String ui = mySemTyRel.getUi();
 String value = mySemTyRel.getValue();
 }
~~~~

#### Sample Output:

Abbreviation |  Definition |Child Count  | Relation Count |  Tree Number |   Ui  |   Value
--- | --- | ---  | --- | --- | --- | ---
 sosy   |  An observable manifestation of a disease or condition based on clinical judgment, or a manifestation of a disease or condition which is experienced by the patient and reported as a subjective observation.   |  0  | 5  | A2.2.2  |  T184 |  Sign or Symptom    
 anab  | An abnormal structure, or one that is abnormal in size or location. |  2  | 12  |   A1.2.2      |   T190  | Anatomical Abnormality     
  neop   |   A new and abnormal growth of tissue in which the growth is uncontrolled and progressive. The growths may be malignant or benign |  0    |  1   |B2.2.1.2.1.2 |T191 |  Neoplastic Process   
cgab    |   An abnormal structure, or one that is abnormal in size or location, present at birth or evolving over time as a result of a defect in embryogenesis.  | 0 |  1  |A1.2.2.1    |   T019 |  Congenital Abnormality 
>

**Method: **getAllSemanticTypeGroups(String ticket,String version)

**Returns:**ArrayList<SemanticTypeGroupDTO>

**Use Case:** Given a UMLS release, this call returns all the semantic type groups used in the version. Each returned object specifies a semantic type group, including the name and semantic type count for the group.


#### Sample Input (Java):

~~~~
myarrSemTyRelDTO = utsSemanticNetworkService.getAllSemanticTypeGroups (ticket, umlsRelease);
 for (int i = 0; i < myarrSemTyRelDTO.size(); i++) {
 SemanticTypeGroupDTO mySemTyRel = myarrSemTyRelDTO.get(i);
 String abbreviation = mySemTyRel.getAbbreviation();
 String expandedForm = mySemTyRel.getExpandedForm();
 int semTypeCnt = mySemTyRel.getSemanticTypeCount();
 }
~~~~

#### Sample Output:

 Abbreviation |  Expanded Form  | Semantic Type Count 
--- | --- | --- 
 ACTI    |       Activities & Behaviors   |     9      
 ANAT    |       Anatomy                   |    11       
 CHEM    |       Chemicals & Drugs          |   26          
CONC      |     Concepts & Ideas            |  12                  
 DEVI      |     Devices                    |   3                   
 DISO       |    Disorders                   |  12             
 GENE      |     Genes & Molecular Sequences |  5               
GEOG       |    Geographic Areas             | 1                    

