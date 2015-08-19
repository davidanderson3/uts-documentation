title=Retrieving UMLS Attribute Information from UTS SOAP API
date=2015-08-18
updated=2015-08-18
type=page
status=unpublished
category=Retrieving UMLS Concepts in SOAP API
navorder=11
~~~~~~


**Method: **getRelationAttributes(String ticket,String version,String relationId,PSF psf)

**Returns:** ArrayList< AttributeDTO>

**Use Case:** Given a UMLS release and a relation identifier (RUI), this call returns the attributes of the relation.

#### Sample Input (Java):

~~~~
UtsMetathesaurusContent.Psf myPsf = new UtsMetathesaurusContent.Psf();
 List<AttributeDTO> myAttributes = new ArrayList<AttributeDTO>();
 myAttributes = utsContentService.getRelationAttributes(ticket, umlsRelease, "R74224153",myPsf);
 for (int i = 0; i < myAttributes.size(); i++) {
 AttributeDTO myAttributeDTO = myAttributes.get(i);
 String attributeName = myAttributeDTO.getName();
 String attributeValue = myAttributeDTO.getValue();
 }
~~~~

#### Sample Input (C#):

~~~~
content.psf myPsf = new content.psf();
 content.attributeDTO[] myAttributes =utsContentService.getRelationAttributes(ticket, "2012AA", "R74224153",myPsf);
 for (int i = 0; i < myAttributes.Length; i++){
 content.attributeDTO myAttributeDTO = myAttributes[i];
 string attributeName = myAttributeDTO.name;
 string attributeValue = myAttributeDTO.value;
~~~~

#### Sample Output:

~~~~
   Attribute Name: CHARACTERISTICTYPE
   Attribute Value: 3
  
   Attribute Name: REFINABILITY
   Attribute Value: 0
~~~~
>

**Method: **getCodeAttributes(String ticket,String version,String codeId,String rootSourceAbbreviation,PSF psf)

**Returns:** ArrayList< AttributeDTO>

**Use Case:** Given a UMLS release, a root source abbreviation (RSAB) and a codeId, this call returns the attributes of the supplied code.

#### Sample Input (Java):

~~~~
UtsMetathesaurusContent.Psf myPsf = new UtsMetathesaurusContent.Psf();
 List<AttributeDTO> myAttributes = new ArrayList<AttributeDTO>();
 myAttributes = utsContentService.getCodeAttributes(ticket, umlsRelease, "10042784","MDR",myPsf);
 for (int i = 0; i < myAttributes.size(); i++) {
 AttributeDTO myAttributeDTO = myAttributes.get(i);
 String attributeName = myAttributeDTO.getName();
 String attributeValue = myAttributeDTO.getValue();
 }
~~~~

#### Sample Input (C#):

~~~~
content.psf myPsf = new content.psf();
 content.attributeDTO[] myAttributes =utsContentService.getCodeAttributes(ticket, "2012AA", "10042784","MDR",myPsf);
 for (int i = 0; i < myAttributes.Length; i++) {
 content.attributeDTO myAttributeDTO = myAttributes[i];
 string attributeName = myAttributeDTO.name;
 string attributeValue = myAttributeDTO.value;
~~~~

#### Sample Output:

~~~~
   Attribute Name: SMQ_TERM_LEVEL
   Attribute Value: 5
~~~~
>

**Method: **getSourceConceptAttributes(String ticket,String version,String sourceConceptId,String rootSourceAbbreviation,PSF psf)

**Returns:** ArrayList< AttributeDTO>

**Use Case:** Given a UMLS release, a root source abbreviation (RSAB) and a source concept identifier (SCUI), this call returns the attributes of the supplied source concept identifier.

#### Sample Input (Java):

~~~~
UtsMetathesaurusContent.Psf myPsf = new UtsMetathesaurusContent.Psf();
 List<AttributeDTO> myAttributes = new ArrayList<AttributeDTO>();
 myAttributes = utsContentService.getSourceConceptAttributes(ticket, umlsRelease, "102735002","SNOMEDCT",myPsf);
 for (int i = 0; i < myAttributes.size(); i++) {
 AttributeDTO myAttributeDTO = myAttributes.get(i);
 String attributeName = myAttributeDTO.getName();
 String attributeValue = myAttributeDTO.getValue();
 }
~~~~

#### Sample Input (C#):

~~~~
content.psf myPsf = new content.psf();
 content.attributeDTO[] myAttributes =utsContentService.getSourceConceptAttributes(ticket, "2012AA", "102735002", "SNOMEDCT", myPsf);
 for (int i = 0; i < myAttributes.Length; i++) {
 content.attributeDTO myAttributeDTO = myAttributes[i];
 string attributeName = myAttributeDTO.name;
 string attributeValue = myAttributeDTO.value;
~~~~

#### Sample Output:

~~~~
   Attribute Name: CONCEPTSTATUS
   Attribute Value: 2
  
   Attribute Name: CTV3ID
   Attribute Value: XU0kZ
  
   Attribute Name: ISPRIMITIVE
   Attribute Value: 1
  
   Attribute Name: SNOMEDID
   Attribute Value: F-63675
~~~~
>

**Method: **getSourceDescriptorAttributes(String ticket,String version,String sourceDescriptorId,String rootSourceAbbreviation,PSF psf)
**Returns:** ArrayList< AttributeDTO>

**Use Case:** Given a UMLS release, a root source abbreviation (RSAB) and a source descriptor identifier (SDUI), this call returns the attributes of the supplied source descriptor.

#### Sample Input (Java):

~~~~
UtsMetathesaurusContent.Psf myPsf = new UtsMetathesaurusContent.Psf();
 List<AttributeDTO> myAttributes = new ArrayList<AttributeDTO>();
 myAttributes = utsContentService.getSourceDescriptorAttributes(ticket, umlsRelease, "D015060","MSH",myPsf);
 for (int i = 0; i < myAttributes.size(); i++) {
 AttributeDTO myAttributeDTO = myAttributes.get(i);
 String attributeName = myAttributeDTO.getName();
 String attributeValue = myAttributeDTO.getValue();
 }
~~~~

#### Sample Input (C#):

~~~~
content.psf myPsf = new content.psf();
 content.attributeDTO[] myAttributes = utsContentService.getSourceDescriptorAttributes(ticket, "2012AA", "D015060", "MSH", myPsf);
 for (int i = 0; i < myAttributes.Length; i++) {
 content.attributeDTO myAttributeDTO = myAttributes[i];
 string attributeName = myAttributeDTO.name;
 string attributeValue = myAttributeDTO.value;
 }
~~~~

#### Sample Output:

~~~~
   Attribute Name: AN
   Attribute Value: "a major constituent of pulmonary surfactants"; /biosyn /physiol permitted; DF: DPPC
 
   Attribute Name: AQL
   Attribute Value: AA AD AE AG AI AN BI BL CF CH CL CS CT DF DU EC GE HI IM IP ME PD PH PK PO RE SD SE ST TO TU UR
  
   Attribute Name: DC
   Attribute Value: 1
  
   Attribute Name: DX
   Attribute Value: 19870101
  
   Attribute Name: HN
   Attribute Value: 87
  
   Attribute Name: MDA
   Attribute Value: 19860612
  
   Attribute Name: MMR
   Attribute Value: 20030709
  
   Attribute Name: MN
   Attribute Value: D10.570.755.375.760.400.800.224
  
   Attribute Name: OL
   Attribute Value: search PULMONARY SURFACTANTS 1977-86
  
   Attribute Name: PM
   Attribute Value: 87; was DIPALMITOYL PHOSPHATIDYLCHOLINE see PULMONARY SURFACTANT 1977-86
~~~~
>

**Method: **getAtomAttributes(String ticket,String version,String atomId,PSF psf)

**Returns:** ArrayList< AttributeDTO>

**Use Case:** Given a UMLS release and an atom unique identifier (AUI), this call returns the attributes of the supplied atom.

#### Sample Input (Java):

~~~~
UtsMetathesaurusContent.Psf myPsf = new UtsMetathesaurusContent.Psf();
 List<AttributeDTO> myAttributes = new ArrayList<AttributeDTO>();
 myAttributes = utsContentService.getAtomAttributes(ticket, umlsRelease, "A7755565",myPsf);
 for (int i = 0; i < myAttributes.size(); i++) {
 AttributeDTO myAttributeDTO = myAttributes.get(i);
 String attributeName = myAttributeDTO.getName();
 String attributeValue = myAttributeDTO.getValue();
 }
~~~~

#### Sample Input (C#):

~~~~
content.psf myPsf = new content.psf();
 content.attributeDTO[] myAttributes =utsContentService.getAtomAttributes(ticket, "2012AA", "A7755565",myPsf);
 for (int i = 0; i < myAttributes.Length; i++) {
 content.attributeDTO myAttributeDTO = myAttributes[i];
 string attributeName = myAttributeDTO.name;
 string attributeValue = myAttributeDTO.value;
 }
~~~~

#### Sample Output:

~~~~
   Attribute Name: TERMUI
   Attribute Value: T037573
  
   Attribute Name: TH
   Attribute Value: UNK (19XX)
~~~~
>

**Method: **getSubsetMemberAttributes(String ticket,String version,String id,PSF psf)

**Returns:** ArrayList< AttributeDTO>

**Use Case:** Given a UMLS release and an identifier for a specified subset member, this call returns the attributes of the subset member.

#### Sample Input (Java):

~~~~
UtsMetathesaurusContent.Psf myPsf = new UtsMetathesaurusContent.Psf();
 List<AttributeDTO> myAttributes = new ArrayList<AttributeDTO>();
 myAttributes = utsContentService.getSubsetMemberAttributes(ticket, umlsRelease, "AT188025182",myPsf);
 for (int i = 0; i < myAttributes.size(); i++) {
 AttributeDTO myAttributeDTO = myAttributes.get(i);
 String attributeName = myAttributeDTO.getName();
 String attributeValue = myAttributeDTO.getValue();
 }
~~~~

#### Sample Input (C#):

~~~~
content.psf myPsf = new content.psf();
 content.attributeDTO[] myAttributes = utsContentService.getSubsetMemberAttributes(ticket, "2012AA", "AT139571931", myPsf);
 for (int i = 0; i < myAttributes.Length; i++) {
 content.attributeDTO myAttributeDTO = myAttributes[i];
 string attributeName = myAttributeDTO.name;
 string attributeValue = myAttributeDTO.value;
 }
~~~~

#### Sample Output:

~~~~
   Attribute Name: MAPTARGET
   Attribute Value: 403.10
~~~~
>

**Method: **getMapSetAttributes(String ticket,String version,String id,PSF psf)

**Returns:** ArrayList<AttributeDTO>

**Use Case:** Given a UMLS release and a mapset identifier, this call returns the attributes of each member of the map set.

#### Sample Input (Java):

~~~~
UtsMetathesaurusContent.Psf myPsf = new UtsMetathesaurusContent.Psf();
 List<AttributeDTO> myAttributes = new ArrayList<AttributeDTO>();
 myAttributes = utsContentService.getMapSetAttributes(ticket, umlsRelease, "C2963202",myPsf);
 for (int i = 0; i < myAttributes.size(); i++) {
 AttributeDTO myAttributeDTO = myAttributes.get(i);
 String attributeName = myAttributeDTO.getName();
 String attributeValue = myAttributeDTO.getValue();
 }
~~~~

#### Sample Input (C#):

~~~~
content.psf myPsf = new content.psf();
 content.attributeDTO[] myAttributes =utsContentService.getMapSetAttributes(ticket, "2011AB", "C2963202",myPsf);
 for (int i = 0; i < myAttributes.Length; i++) {
 content.attributeDTO myAttributeDTO = myAttributes[i];
 string attributeName = myAttributeDTO.name;
 string attributeValue = myAttributeDTO.value;
 }
~~~~

#### Sample Output:

~~~~
   Attribute Name: CODE
   Attribute Value: MTHU000002
  
   Attribute Name: SOS
   Attribute Value: This set maps ICD-10-PCS codes to ICD-9-CM. These are "General Equivalence Mappings" (GEMs) and are rule-based.
  
   Attribute Name: LANG
   Attribute Value: ENG
~~~~
>

**Method: **getSubsetAttributes(String ticket,String version,String id,PSF psf)

**Returns:** ArrayList<AttributeDTO>

**Use Case:** Given a UMLS release and a subset identifier, this call returns the attributes of the supplied subset CUI.

#### Sample Input (Java):

~~~~
UtsMetathesaurusContent.Psf myPsf = new UtsMetathesaurusContent.Psf();
 List<AttributeDTO> myAttributes = new ArrayList<AttributeDTO>();
 myAttributes = utsContentService.getSubsetAttributes(ticket, umlsRelease, "IC1321498",myPsf);
 for (int i = 0; i < myAttributes.size(); i++) {
 AttributeDTO myAttributeDTO = myAttributes.get(i);
 String attributeName = myAttributeDTO.getName();
 String attributeValue = myAttributeDTO.getValue();
 }
~~~~

#### Sample Input (C#):

~~~~
content.psf myPsf = new content.psf();
 content.attributeDTO[] myAttributes =utsContentService.getSubsetAttributes(ticket, "2011AB", "IC1321498",myPsf);
 for (int i = 0; i < myAttributes.Length; i++) {
 content.attributeDTO myAttributeDTO = myAttributes[i];
 string attributeName = myAttributeDTO.name;
 string attributeValue = myAttributeDTO.value;
 }
~~~~

#### Sample Output:

~~~~
   Attribute Name: LANG
   Attribute Value: ENG
  
   Attribute Name: SUBSETCONTEXTID
   Attribute Value: 0
  
   Attribute Name: SUBSETORIGINALID
   Attribute Value: 100033
  
   Attribute Name: SUBSETREALMID
   Attribute Value: 0
  
   Attribute Name: SUBSETTYPE
   Attribute Value: 1
  
   Attribute Name: SUBSETVERSION
   Attribute Value: 21
~~~~

