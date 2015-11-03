title=Retrieving UMLS Tree Position Information from UTS SOAP API
date=2015-08-18
updated=2015-08-18
type=page
status=published
navorder=12
~~~~~~


**Method: **getRootAtomTreePositions(String ticket,String version,PSF psf)

**Returns:**ArrayList< AtomTreePositionDTO>

**Use Case:** This method is useful to expose atoms that are at the root of a source vocabulary's hieararchy. Not all sources provide hierarchies, and depending on how NLM interprets and processes the source, hierarchies may exist through atoms or source atom clusters (source concepts, source descriptors, etc).

#### Sample Input (Java):

~~~~
myarrAtmTreePos = utsContentService.getRootAtomTreePositions(ticket,umlsRelease,myPsf);
 for (int i = 0; i < myarrAtmTreePos.size(); i++) {
 AtomTreePositionDTO myAtmTreePosDTO = myarrAtmTreePos.get(i);
 String defPrefName = myAtmTreePosDTO.getDefaultPreferredName();
 String atomUi = myAtmTreePosDTO.getAtom().getUi();
 String ui = myAtmTreePosDTO.getUi();
 int childCnt = myAtmTreePosDTO.getChildCount();
 }
~~~~


#### Sample Output:

Default Preferred Name| Atom Ui    | Ui   |Child Count 
--- |--- | --- |--- 
MedlinePlus | A15660722 |  7cb8fbf29289b2cced4a03317948e748 |  1    
Online Mendelian Inheritance in Man |A11979784  | 7419cd7cbc5f2214fda5c560de57157e  | 25       
MEDCIN|A13943116  | be075d6aeadada1d996b23335606dcb1 |  6  
LOINC Root  | A6321000   | fb755c2b68dde5a873c80b786eecb06d  | 2        
Traditional Korean Medical Terms |A18427843 |  165187d256e9b4b7655fe770e89b2bec |  14     
AI/RHEUM  |A0385785  |  50813c7da77884b0ee31866e4f3e3a75|  65 
COSTART: coding symbols for thesaurus of adverse reaction terms  |A0398286   | 55fcbd1c673e1c507ef700948a3ec8a4 |  29      
Systematized Nomenclature of Medicine. 2nd ed.    |A0463527   | 6d8996fa21eee9f52b2795f0d1a26410  | 7      
SNOMED International|A0455478   | ac27a6d9cb0eb24f0986083db3825c72  | 12  
WHO Adverse Reaction Terminology  | A0471291 |   4850c7314bbc79611f7716e843c62916 |  32     
Neuronames Brain Hierarchy  | A0570143   | cdbb160009948fb89f8d12061764c784 |  1     
International Statistical Classification of Diseases and Related Health Problems, Tenth Revision (ICD-10)  | A0974962   | eb45347889dd42fc496685c76b9dc7fa |  21    

>

**Method: **getAtomTreePositions(String ticket,String version,String atomId,PSF psf)

**Returns:**ArrayList< AtomTreePositionDTO>

**Use Case:** This method exposes all positions within a source vocabulary's context for which an atom could be found. Once you have the tree positions for a given atom, you can expose the siblings, parents,and children of that atom within the context of that tree position using other methods. Many sources provide more than one way to find a given term within a source, to acommodate the different ways the term may be searched by users.


#### Sample Input (Java):

~~~~
myarrAtmTreePosClient = utsContentService.getAtomTreePositions(ticket, umlsRelease, "A0483719", myPsf);
 for (int i = 0; i < myarrAtmTreePosClient.size(); i++) {
 AtomTreePositionDTO myAtmTreePosDTO = myarrAtmTreePosClient.get(i);
 String defPrefName = myAtmTreePosDTO.getDefaultPreferredName();
 String ui = myAtmTreePosDTO.getUi();
 int pathsToRootSrc = myAtmTreePosDTO.getPathsToRootCount();
 int siblingCount = myAtmTreePosDTO.getSiblingCount();
 int childCnt = myAtmTreePosDTO.getChildCount();
 String rootSource = myAtmTreePosDTO.getRootSource();
 String atomUi = myAtmTreePosDTO.getAtom().getUi();
 }
~~~~


#### Sample Output:


Default Preferred Name |  Ui | Paths to Root Count  | Sibling Count |  Child Count |  Root Source |  Atom Ui 
--- |--- | --- |--- | --- | --- | ---
methamphetamine   |  d911cd41343040aaa9888c72ab26cc41  | 1  |  4    |   2  |    AOD |   A0483719    

>

**Method: **getAtomTreePositionPathsToRoot(String ticket,String version,String atomPosId,PSF psf)

**Returns:** ArrayList< AtomTreePositionPathDTO>

**Use Case:** This method exposes all the paths back up to the root atom for a given atom's position within a hierarchy. Many sources provide more than one way to find a given term within a source, to acommodate the different ways the term may be searched by users.

#### Sample Input (Java):

~~~~
myarrAtmTreePosPathClient =utsContentService.getAtomTreePositionPathsToRoot(ticket, umlsRelease, "d911cd41343040aaa9888c72ab26cc41", myPsf);
 for (int i = 0; i < myarrAtmTreePosPathClient.size(); i++) {
 AtomTreePositionPathDTO myAtmTreePosPathDTO =myarrAtmTreePosPathClient.get(i);
 List<AtomTreePositionDTO> treepos =myAtmTreePosPathDTO.getTreePositions();
 for (int j = 0; j < treepos.size(); j++) {
 AtomTreePositionDTO getj = treepos.get(j);
 String defPrefName = getj.getDefaultPreferredName();
 String ui = getj.getUi();
 String atomUi = getj.getAtom().getUi();
 String rootSrc = getj.getRootSource();
 String termType = getj.getAtom().getTermType();
 }
~~~~

#### Sample Output:

Default Preferred Name  |  Ui    |Atom Ui  |  Root Source |  Term Type 
--- |--- | --- |--- | --- 
primary stimulants of abuse  |   f6e8b8c641afc1483d6ac35c97ba9cf5    | A1384816  | AOD |   DE  
CNS stimulants of abuse  |  645acb5e6a08094694a4e12ba6170402    | A1384801 |  AOD   |   DE     
AOD substance or product  |  05535b8e502ecdbbaa429e3945aa0671  |A1387055  | AOD   |   DS         
Alcohol and Other Drug Thesaurus  | e41ca0561bfcbe7a642c3ce0f8f87473    |A1386158  | AOD  |RHT    
>

**Method: **getAtomTreePositionChildren(String ticket,String version,String atomPosId,PSF psf)

**Returns:** ArrayList< AtomTreePositionDTO>

**Use Case:** This method exposes all the children given an atom's position within a hierarchy.

#### Sample Input (Java):

~~~~
myarrAtmTreePosClient = utsContentService.getAtomTreePositionChildren(ticket, umlsRelease, "d911cd41343040aaa9888c72ab26cc41", myPsf);
 for (int i = 0; i < myarrAtmTreePosClient.size(); i++) {
 AtomTreePositionDTO myAtmTreePosDTO = myarrAtmTreePosClient.get(i);
 String defPrefName = myAtmTreePosDTO.getDefaultPreferredName();
 String ui = myAtmTreePosDTO.getUi();
 int pathsToRootCnt = myAtmTreePosDTO.getPathsToRootCount();
 int siblingCount = myAtmTreePosDTO.getSiblingCount();
 int childCnt = myAtmTreePosDTO.getChildCount();
 String rootSource = myAtmTreePosDTO.getRootSource();
 String atomUi = myAtmTreePosDTO.getAtom().getUi();
 }
~~~~

#### Sample Output:

Default Preferred Name |  Ui  | Paths to Root Count |  Sibling Count |  Child Count |  Root Source |  Atom Ui  
--- |--- | --- |--- | --- | --- | ---
chlormethamphetamine   |  54810f11729bebbebe62fe7be6208c1d |  1   |  1     |  0   |  AOD   | A0038155  
benzphetamine    | aaf335622ead33e538712005f097f46e |  1    | 1    | 0   |  AOD  |A1388157  
>

**Method: **getAtomTreePositionSiblings(String ticket,String version,String atomPosId,PSF psf)

**Returns:** ArrayList< AtomTreePositionDTO>

**Use Case:** This method exposes all siblings given an atom's position within a hierarchy.

#### Sample Input (Java):

~~~~
myarrAtmTreePosClient = utsContentService.getAtomTreePositionSiblings(ticket, umlsRelease, "d911cd41343040aaa9888c72ab26cc41", myPsf);
 for (int i = 0; i < myarrAtmTreePosClient.size(); i++) {
 AtomTreePositionDTO myAtmTreePosDTO = myarrAtmTreePosClient.get(i);
 String defPrefName = myAtmTreePosDTO.getDefaultPreferredName();
 String ui = myAtmTreePosDTO.getUi();
 int pathsToRootSrc = myAtmTreePosDTO.getPathsToRootCount();
 int siblingCount = myAtmTreePosDTO.getSiblingCount();
 int childCnt = myAtmTreePosDTO.getChildCount();
 String rootSource = myAtmTreePosDTO.getRootSource();
 String atomUi = myAtmTreePosDTO.getAtom().getUi();
 }
~~~~

#### Sample Output:

Default Preferred Name |  Ui   |Paths to Root Count  | Sibling Count  | Child Count  | Root Source  | Atom Ui
--- |--- | --- |--- | --- | --- | ---
MDMA   |  140b26fc5d45228e34c933daedbc1be8 |  1    | 4     |  0    |  AOD |  A0202522  
amphetamines  | 87fd5f7931dbcc43bd7e0a07cfa5ba63|   1   | 4    | 2    | AOD   | A1386500   
DOM  | af222cd30e1e0608a045561ba1e58c32 |  1   | 4   |  0  | AOD  | A0051020  
dextroamphetamine | 29584e602e69bc46a6e3432c3c827b6b |  1    |4   |   0  | AOD   | A0477636 
>

**Method: **getRootSourceConceptTreePositions(String ticket,String version,PSF psf)

**Returns:** ArrayList< SourceAtomClusterTreePositionDTO>

**Use Case:** This method is useful to expose source-asserted concepts that are at the root of a source vocabulary's hieararchy. Not all sources provide hierarchies, and depending on how NLM interprets and processes the source, hierarchies may exist through atoms or source atom clusters (source concepts, source descriptors, etc).


#### Sample Input (Java):

~~~~
myarrAtomClustTrPosClient = utsContentService.getRootSourceConceptTreePositions(ticket, umlsRelease, myPsf);
 for (int i = 0; i < myarrAtomClustTrPosClient.size(); i++) {
 SourceAtomClusterTreePositionDTO myAtmClustTreePosDTO = myarrAtomClustTrPosClient.get(i);
 String defaultPrefName = myAtmClustTreePosDTO.getCluster().getDefaultPreferredName();
 String clusterUi = myAtmClustTreePosDTO.getCluster().getUi();
 String ui = myAtmClustTreePosDTO.getUi();
 int childCnt = myAtmClustTreePosDTO.getChildCount();
 int siblingCnt = myAtmClustTreePosDTO.getSiblingCount();
 String rootSrc = myAtmClustTreePosDTO.getRootSource();
 }
~~~~


#### Sample Output:

Default Preferred Name  |Cluster Ui  | Ui | Child Count |  Sibling Count  | Root Source  
--- |--- | --- |--- | --- | ---
ICD-10-PCS | V-ICD10PCS |  d67171a8e3ef1a7b4fc40e8c2b73dd17 |  16 |  0  | ICD10PCS       
Metathesaurus CPT Hierarchical Terms|V-MTHCH  |  75ca8ce0a8536c02f7bf1816bb9a20bc |  8  |0    | MTHCH   
Metathesaurus HCPCS Hierarchical Terms  | V-MTHHH |  8cca114ecdfbdcb3aea1153d78b2c107 |  4  | 0    | MTHHH   
NCI Thesaurus  | V-NCI  |cde741746767401ca36b7de2aee7d404  | 19 |  0 | NCI    
root (of NCBI Taxonomy)  |1    | 362f3604b62a5605215cfabf31865f7a |  4  | 0   |NCBI  
>

**Method: **getSourceConceptTreePositions(String ticket,String version,String sourceConceptId,String rootSourceAbbreviation,PSF psf)

**Returns:** ArrayList< SourceAtomClusterTreePositionDTO>

**Use Case:** This method exposes all positions within a source vocabulary's context for which an source concept could be found. Once you have the tree positions for a given source concept, you can expose the siblings, parents, and children of that source concept within the context of that tree position using other methods. Many sources provide more than one way to find a given term within a source, to acommodate the different ways the term may be searched by users.


#### Sample Input (Java):

~~~~
myarrAtomClustTrPosClient = utsContentService.getSourceConceptTreePositions(ticket, umlsRelease, "84757009", "SNOMEDCT", myPsf);
 for (int i = 0; i < myarrAtomClustTrPosClient.size(); i++) {
 SourceAtomClusterTreePositionDTO myAtmClustTreePosDTO =myarrAtomClustTrPosClient.get(i);
 String defaultPrefName =myAtmClustTreePosDTO.getCluster().getDefaultPreferredName();
 String clusterUi = myAtmClustTreePosDTO.getCluster().getUi();
 String ui = myAtmClustTreePosDTO.getUi();
 int childCnt = myAtmClustTreePosDTO.getChildCount();
 int siblingCnt = myAtmClustTreePosDTO.getSiblingCount();
 String rootSrc = myAtmClustTreePosDTO.getRootSource();
 }
~~~~

#### Sample Output:

 Default Preferred Name |  Cluster Ui |  Ui  |Child Count  | Sibling Count  | Root Source 
 --- |--- | --- |--- | --- | ---
Epilepsy   | 84757009 | 5959f85e98b14c7e351970d87809b613 | 18   | 0   | SNOMEDCT     
>

**Method: **getSourceConceptTreePositionPathsToRoot(String ticket,String version,String scuiPosId,PSF psf)

**Returns:** ArrayList< SourceAtomClusterTreePositionPathDTO>

**Use Case:** This method exposes all the paths back up to the root source concept for a given source concept's position within a hierarchy. Many sources provide more than one way to find a given term within a source, to acommodate the different ways the term may be searched by users.

#### Sample Input (Java):

~~~~
myarrSrcConcTreePosPathDTOClient = utsContentService.getSourceConceptTreePositionPathsToRoot(ticket, umlsRelease, "5959f85e98b14c7e351970d87809b613", myPsf);
 for (int i = 0; i < myarrSrcConcTreePosPathDTOClient.size(); i++) {
 SourceAtomClusterTreePositionPathDTO myAtmClustTreePosDTO =myarrSrcConcTreePosPathDTOClient.get(i);
 List<SourceAtomClusterTreePositionDTO> treepos =myAtmClustTreePosDTO.getTreePositions();
 for (int j = 0; j < treepos.size(); j++) {
 SourceAtomClusterTreePositionDTO getj = treepos.get(j);
 String defPrefName = getj.getDefaultPreferredName();
 String ui = getj.getUi();
 String clusterUi = getj.getCluster().getUi();
 String rootSrc = getj.getRootSource();
 int pathsToRootCnt = getj.getAtom().getPathsToRootCount();
 }
~~~~


#### Sample Input (C#):

~~~~
utsContentService.getSourceConceptTreePositionPathsToRoot(ticket,"2011AB", "d0490ffa72367cbb0f4db4864fb02b3f", myPsf);
~~~~

#### Sample Output:

Default Preferred Name|Ui|Cluster Ui|Root Source|Paths to Root Count
--- |--- | --- |--- | --- 
Seizure disorder|3fe4bfb81028eb51b614ec23ecc7586d|128613002|SNOMEDCT|10
Disorder of brain|2a2e30869c4b5130728e1259218597ce|81308009|SNOMEDCT|10
Disorder of body cavity|277d3f0d21e9b4f9b08f0352aed4745b|399902003|SNOMEDCT|2
Disorder by body site|a81ddd3cf10a25e8d11633fa574a8c3f|123946008|SNOMEDCT|2
Finding by site|8634bd86427b0b314309a810648b61f7|118234003|SNOMEDCT|1
Clinical finding|df26dc6c2ba321499edce7293b47dd74|404684003|SNOMEDCT|1
SNOMED CT Concept|eb71ee85949c8cb0e6e215bbcb63ded7|138875005|SNOMEDCT|0
>

**Method: **getSourceConceptTreePositionChildren(String ticket,String version,String scuiPosId,PSF psf)

**Returns:** ArrayList< SourceAtomClusterTreePositionDTO>

**Use Case:** This method exposes all the children given a source concept's position within a hierarchy.

#### Sample Input (Java):

~~~~
myarrAtomClustTrPosClient =utsContentService.getSourceConceptTreePositionChildren(ticket,umlsRelease, "5959f85e98b14c7e351970d87809b613", myPsf);
 for (int i = 0; i < myarrAtomClustTrPosClient.size(); i++) {
 SourceAtomClusterTreePositionDTO myAtmClustTreePosDTO =myarrAtomClustTrPosClient.get(i);
 String defaultPrefName =myAtmClustTreePosDTO.getCluster().getDefaultPreferredName();
 String clusterUi = myAtmClustTreePosDTO.getCluster().getUi();
 String ui = myAtmClustTreePosDTO.getUi();
 int childCnt = myAtmClustTreePosDTO.getChildCount();
 int siblingCnt = myAtmClustTreePosDTO.getSiblingCount();
 String rootSrc = myAtmClustTreePosDTO.getRootSource();
 }
~~~~

#### Sample Output:

Default Preferred Name  | Cluster Ui |  Ui   | Child Count |  Sibling Count |  Root Source
--- |--- | --- |--- | --- | ---
Benign neonatal convulsions  | 38281008 | c4ee1234d4ac6c5a4e243a1ebf99ee90  | 2      |       0  |      SNOMEDCT  
Status epilepticus|  230456007   | 86142112a0b1037af188d12bdcaa9d22 |  3 | 0  |  SNOMEDCT 
Reflex epilepsy | 79745005   |  116557ee5f3cee1ea107595c0e770548  | 14     |   0   |SNOMEDCT 
Epilepsy, not refractory  |422513000  |  9a7497d61964c0c4c4aca2ad3134cc5c|   0  |   0   | SNOMEDCT
Visceral epilepsy | 2198002    |  1b2786c04da10000a350ab0fd47e78b4  | 0  |   0   | SNOMEDCT 
Cursive seizure   | 71427006   |  dda7fa3ea10259010e8a596295d84919 |  0    |  0   |SNOMEDCT 
>


**Method: **getSourceConceptTreePositionSiblings(String ticket,String version,String scuiPosId,PSF psf)

**Returns:** ArrayList< SourceAtomClusterTreePositionDTO>

**Use Case:** This method exposes all the siblings given a source concept's position within a hierarchy.

#### Sample Input (Java):

~~~~
myarrAtomClustTrPosClient =utsContentService.getSourceConceptTreePositionSiblings(ticket,umlsRelease, "5959f85e98b14c7e351970d87809b613", myPsf);
 for (int i = 0; i < myarrAtomClustTrPosClient.size(); i++) {
 SourceAtomClusterTreePositionDTO myAtmClustTreePosDTO =myarrAtomClustTrPosClient.get(i);
 String defaultPrefName =myAtmClustTreePosDTO.getCluster().getDefaultPreferredName();
 String clusterUi = myAtmClustTreePosDTO.getCluster().getUi();
 String ui = myAtmClustTreePosDTO.getUi();
 int childCnt = myAtmClustTreePosDTO.getChildCount();
 int siblingCnt = myAtmClustTreePosDTO.getSiblingCount();
 String rootSrc = myAtmClustTreePosDTO.getRootSource();
 }
~~~~

#### Sample Output:

Default Preferred Name |  Cluster Ui |  Ui  | Child Count  | Sibling Count  | Root Source 
--- |--- | --- |--- | --- | --- 
Seizures due to metabolic disorder |  371022006  |  5ac2e9eccfc06b559cfefc913a4b0346 |  0   |   0   | SNOMEDCT 
Generalized-onset seizures  |  4619009 |  e973d2fbcc2c4d477aad4651e7979911 |  4   |  0   |SNOMEDCT   
Convulsions in the newborn   |87476004  |   175049801d6d21dc41fb33233d7cc2a5|   5    |   0    |    SNOMEDCT  
Partial seizure   | 29753000    | 5a171fc2121d5484ee7aacd397bbf758  | 24    |    0   |  SNOMEDCT   
Epileptic vertigo     |  68761002   |  980ffd05da1921082261f8d6fb0e54a8  | 0   |   0   |   SNOMEDCT  
>


**Method: **getRootSourceDescriptorTreePositions(String ticket,String version,PSF psf)

**Returns:** ArrayList< SourceAtomClusterTreePositionDTO>

**Use Case:** This method is useful to expose source-asserted descriptors that are at the root of a source vocabulary's hieararchy. Not all sources provide hierarchies, and depending on how NLM interprets and processes the source, hierarchies may exist through atoms or source atom clusters (source concepts, source descriptors, etc).


#### Sample Input (Java):

~~~~
myarrAtomClustTrPosClient =utsContentService.getRootSourceDescriptorTreePositions(ticket,umlsRelease, myPsf);
 for (int i = 0; i < myarrAtomClustTrPosClient.size(); i++) {
 SourceAtomClusterTreePositionDTO myAtmClustTreePosDTO =myarrAtomClustTrPosClient.get(i);
 String defaultPrefName =myAtmClustTreePosDTO.getCluster().getDefaultPreferredName();
 String clusterUi = myAtmClustTreePosDTO.getCluster().getUi();
 String ui = myAtmClustTreePosDTO.getUi();
 int childCnt = myAtmClustTreePosDTO.getChildCount();
 int siblingCnt = myAtmClustTreePosDTO.getSiblingCount();
 String rootSrc = myAtmClustTreePosDTO.getRootSource();
 }
~~~~

#### Sample Output:


Default Preferred Name    | Cluster Ui |  Ui | Child Count |  Sibling Count |  Root Source     
--- |--- | --- |--- | --- | ---
 French MeSH Root    |  V-MSHFRE  |   ddfd9b0ec1f6d07f613d4852f3fb4ac8  | 119 |     0  | MSHFRE       
Portuguese MeSH Root |V-MSHPOR  |   1fe49c4de455d3045e27579f3e2db9b4 |  39     | 0  | MSHPOR        
Russian MeSH Root |  V-MSHRUS  |   a386d69f08bbc75e9bef2808205bdd4d  | 117   |  0    | MSHRUS  
Spanish MeSH Root| V-MSHSPA  |   0742704a2a2041bcd43e5b886071e217 |  41 | 0     | MSHSPA  
Czech MeSH Root|  V-MSHCZE | 615c28df93f019cd9f367f642fc51fc9  | 119  | 0  |   MSHCZE   
Polish MeSH Root | V-MSHPOL  |   17bc5bbcaeacf23d8194e456ee714f71 |  117 |  0   |MSHPOL    
>

**Method: **getSourceDescriptorTreePositions(String ticket,String version,String sourceDescriptorId,String rootSourceAbbreviation,PSF psf)

**Returns:** ArrayList< SourceAtomClusterTreePositionDTO>

**Use Case:** This method exposes all positions within a source vocabulary's context for which an source descriptor could be found. Once you have the tree positions for a given source descriptor, you can expose the siblings, parents, and children of that source descriptor within the context of that tree position using other methods. Many sources provide more than one way to find a given term within a source, to acommodate the different ways the term may be searched by users.


#### Sample Input (Java):

~~~~
myarrAtomClustTrPosClient = utsContentService.getSourceDescriptorTreePositions(ticket, umlsRelease, "D004697", "MSH", myPsf);
 for (int i = 0; i < myarrAtomClustTrPosClient.size(); i++) {
 SourceAtomClusterTreePositionDTO myAtmClustTreePosDTO =myarrAtomClustTrPosClient.get(i);
 String defaultPrefName =myAtmClustTreePosDTO.getCluster().getDefaultPreferredName();
 String clusterUi = myAtmClustTreePosDTO.getCluster().getUi();
 String ui = myAtmClustTreePosDTO.getUi();
 int childCnt = myAtmClustTreePosDTO.getChildCount();
 int siblingCnt = myAtmClustTreePosDTO.getSiblingCount();
 String rootSrc = myAtmClustTreePosDTO.getRootSource();
 }
~~~~

#### Sample Output:

Default Preferred Name  |  Cluster Ui  | Ui    |Child Count|  Sibling Count  | Root Source  
--- |--- | --- |--- | --- | ---
Endocarditis, Bacterial  | D004697   |  7639f37ffe101f688c7e7ad8bd0c3740 |  1  |   1     |  MSH    
Endocarditis, Bacterial  | D004697   |  ba13bd02b35581a28b3d74536cae39fd  | 1    |  2   |        MSH  
Endocarditis, Bacterial  | D004697   |   5a63dc1297a8ce598a31602e4c1c813f  | 1   |  11    | MSH        
Endocarditis, Bacterial  | D004697   |   0bece2de10968cd8e21ad45e6c5e039b |  1   |    2  |MSH   
>


**Method: **getSourceDescriptorTreePositionPathsToRoot(String ticket,String version,String sduiPosId,PSF psf)

**Returns:** ArrayList< SourceAtomClusterTreePositionPathDTO>

**Use Case:** This method exposes all the paths back up to the root source descriptor for a given source descriptor's position within a hierarchy. Many sources provide more than one way to find a given term within a source, to acommodate the different ways the term may be searched by users.

#### Sample Input (Java):

~~~~
myarrSrcDescTreePosPathDTOClient =utsContentService.getSourceDescriptorTreePositionPathsToRoot(ticket,umlsRelease, "7639f37ffe101f688c7e7ad8bd0c3740", myPsf);
 for (int i = 0; i < myarrSrcDescTreePosPathDTOClient.size(); i++) {
 SourceAtomClusterTreePositionPathDTO myAtmClustTreePosDTO =myarrSrcDescTreePosPathDTOClient.get(i);
 List<SourceAtomClusterTreePositionDTO> treepos =myAtmClustTreePosDTO.getTreePositions();
 for (int j = 0; j < treepos.size(); j++) {
 SourceAtomClusterTreePositionDTO getj = treepos.get(j);
 String defPrefName = getj.getDefaultPreferredName();
 String ui = getj.getUi();
 String clusterUi = getj.getCluster().getUi();
 String rootSrc = getj.getRootSource();
 int pathsToRootCnt = getj.getAtom().getPathsToRootCount();
 }
~~~~

#### Sample Output:

Default Preferred Name  |   Ui |  Cluster Ui  | Root Source |  Paths to Root Count
--- |--- | --- |--- | ---   
Endocarditis |  362a2bbe35ccdfe12381f5ed1d064856  | D004696  | MSH    |   1       
Heart Diseases  |a6cc3c8f699863797d791f6271f85976 |  D006331  | MSH   |  1     
Cardiovascular Diseases  |  16ddb15f553c5470e25e4e645066cc69 |  D002318 | MSH   |   1      
Diseases (MeSH Category) |  1c48af0a419a143cde14f0edf1ab52fc  | U000006  |MSH  | 1    
Topical Descriptor   |  53656e4b1670ec72050f674aaf519db1 |  U000019  | MSH    |    1 
MeSH Descriptors    |  e073e6c4b7283715e9858eb75e0b0abf  | U000017  |MSH | 1     
 MeSH      |7cc1c01a57df5ff1ac7bfa76d2991024 |  V-MSH    | MSH   |  0   
>


**Method: **getSourceDescriptorTreePositionChildren(String ticket,String version,String sduiPosId,PSF psf)

**Returns:** ArrayList< SourceAtomClusterTreePositionDTO>

**Use Case:** This method exposes all the children given a source descriptor's position within a hierarchy.


#### Sample Input (Java):

~~~~
myarrAtomClustTrPosClient = utsContentService.getSourceDescriptorTreePositionChildren(ticket, umlsRelease, "5a63dc1297a8ce598a31602e4c1c813f", myPsf);
 for (int i = 0; i < myarrAtomClustTrPosClient.size(); i++) {
 SourceAtomClusterTreePositionDTO myAtmClustTreePosDTO =myarrAtomClustTrPosClient.get(i);
 String defaultPrefName =myAtmClustTreePosDTO.getCluster().getDefaultPreferredName();
 String clusterUi = myAtmClustTreePosDTO.getCluster().getUi();
 String ui = myAtmClustTreePosDTO.getUi();
 int childCnt = myAtmClustTreePosDTO.getChildCount();
 int siblingCnt = myAtmClustTreePosDTO.getSiblingCount();
 String rootSrc = myAtmClustTreePosDTO.getRootSource();
 }
~~~~

#### Sample Output:

Default Preferred Name  |    Cluster Ui |  Ui     | Child Count | Sibling Count |  Root Source 
--- |--- | --- |--- | --- | ---
Endocarditis, Subacute Bacterial|   D004698  | 2a4772f9186d1842222a7fc1700e8091  | 0    |   0    |  MSH  
>

**Method: **getSourceDescriptorTreePositionSiblings(String ticket,String version,String sduiPosId,PSF psf)

**Returns:** ArrayList< SourceAtomClusterTreePositionDTO>

**Use Case:** This method exposes all the siblings given a source descriptor's position within a hierarchy.


#### Sample Input (Java):

~~~~
myarrAtomClustTrPosClient =utsContentService.getSourceDescriptorTreePositionSiblings(ticket,umlsRelease, "5a63dc1297a8ce598a31602e4c1c813f", myPsf);
 for (int i = 0; i < myarrAtomClustTrPosClient.size(); i++) {
 SourceAtomClusterTreePositionDTO myAtmClustTreePosDTO =myarrAtomClustTrPosClient.get(i);
 String defaultPrefName =myAtmClustTreePosDTO.getCluster().getDefaultPreferredName();
 String clusterUi = myAtmClustTreePosDTO.getCluster().getUi();
 String ui = myAtmClustTreePosDTO.getUi();
 int childCnt = myAtmClustTreePosDTO.getChildCount();
 int siblingCnt = myAtmClustTreePosDTO.getSiblingCount();
 String rootSrc = myAtmClustTreePosDTO.getRootSource();
 }
~~~~


#### Sample Output:

Default Preferred Name  | Cluster Ui |  Ui  |Child Count|  Sibling Count|   Root Source 
--- |--- | --- |--- | --- | ---
Pneumonia, Bacterial |   D018410    |  a7e9555ee0d653ada9e6154201ba1333 |  7    |  11    |    MSH 
Central Nervous System Bacterial Infections |  D020806| fe43818e28ab28934e5445ef1a2782e5  | 6  | 11  |  MSH 
 Gram-Positive Bacterial Infections |  D016908  |ccf45daed7d16d2a5494715d114843ca  | 8   |  11  |   MSH 
Fournier Gangrene  |    D018934 |     01b1e7cc3d507c9a29dce9934cfe71f8 |  0    |  11   |   MSH     
Skin Diseases, Bacterial   |D017192   |   f34abcd43a910aaae2731824d2112658 |  17  |     11   | MSH   
Eye Infections, Bacterial    | D015818 |   584fc425010f89c042c84e04c52965c9|   5   |   11  |    MSH   


