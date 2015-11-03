title=Relationship Metadata
date=2015-08-25
updated=2015-08-25
type=page
status=published
navorder=4
~~~~~~


**Method: **getRelationLabel(String ticket,String version,String relationLabel)

**Returns:**RelationLabelDTO

**Use Case:** Given a UMLS release and abbreviated form of a relation label (REL), this call returns the expanded form of the relation label as well as the abbreviation.

#### Sample Input (Java):

~~~~
myRelationLabel = utsMetadataService.getRelationLabel(ticket, umlsRelease, "RN");
 String abbreviation = myRelationLabel.getAbbreviation();
 String expandedForm = myRelationLabel.getExpandedForm();
 String inverseAbbr = myRelationLabel.getInverse().getAbbreviation();
 String inverseExpandedForm = myRelationLabel.getInverse().getExpandedForm();
~~~~

#### Sample Input (C♯):

~~~~
Metadata.relationLabelDTO myRelationLabel =utsMetadataService.getRelationLabel(singleUseTicket, "2012AB", "RN");
 string abbreviation = myRelationLabel.abbreviation;
 string expandedForm = myRelationLabel.expandedForm;
 string inverseAbbreviation = myRelationLabel.inverse.abbreviation;
 string inverseExpandedForm = myRelationLabel.inverse.expandedForm;
~~~~

#### Sample Output:

~~~~  
   Abbreviation:RN
   ExpandedForm:has a narrower relationship
   inverseAbbr:RB
   inverseExpandedForm:has a broader relationship
~~~~
>

**Method: **getAllRelationLabels(String ticket,String version)
**Returns:**ArrayList<RelationLabelDTO>

**Use Case:** Given a UMLS release, this call returns all the valid relation labels (REL) for the release. Each relation label is returned with its expanded form and its abbreviation.

#### Sample Input (Java):

~~~~
myarrRelationLabel = utsMetadataService.getAllRelationLabels(ticket,umlsRelease);
 for (int i = 0; i < myarrRelationLabel.size(); i++) {
 RelationLabelDTO myRelationLabelDTO = myarrRelationLabel.get(i);
 String expandedForm = myRelationLabelDTO.getAbbreviation();
 String abbreviation = myRelationLabelDTO.getExpandedForm();
 }
~~~~

#### Sample Input (C♯):

~~~~
Metadata.relationLabelDTO[] myRelationLabels =utsMetadataService.getAllRelationLabels(singleUseTicket, "2012AB");
 for (int i = 0; i < myRelationLabels.Length; i++) {
 Metadata.relationLabelDTO myRelationLabelDTO = myRelationLabels[i];
 string expandedForm = myRelationLabelDTO.expandedForm;
 string abbreviation = myRelationLabelDTO.abbreviation;
 }
~~~~

#### Sample Output:

~~~~
  Abbreviation:Allowed qualifier
   ExpandedForm:AQ
   Abbreviation:has child relationship in a Metathesaurus source vocabulary
   ExpandedForm:CHD
   Abbreviation:Deleted concept
   ExpandedForm:DEL
   Abbreviation:has parent relationship in a Metathesaurus source vocabulary
   ExpandedForm:PAR
   Abbreviation:can be qualified by.
   ExpandedForm:QB
   Abbreviation:has a broader relationship
   ExpandedForm:RB
   Abbreviation:the relationship is similar or "alike". the two concepts are similar or "alike". In the current edition of the Metathesaurus, most relationships with this attribute are mappings provided by a source, named in SAB and SL; hence concepts linked by this relationship may be synonymous, i.e. self-referential: CUI1 = CUI2. In previous releases, some MeSH Supplementary Concept relationships were represented in this way.
   ExpandedForm:RL
   Abbreviation:has a narrower relationship
   ExpandedForm:RN
   Abbreviation:has relationship other than synonymous, narrower, or broader
   ExpandedForm:RO
   Abbreviation:related and possibly synonymous.
   ExpandedForm:RQ
   Abbreviation:Related, unspecified
   ExpandedForm:RU
   Abbreviation:has sibling relationship in a Metathesaurus source vocabulary.
   ExpandedForm:SIB
   Abbreviation:source asserted synonymy.
   ExpandedForm:SY
   Abbreviation:Not related, no mapping
   ExpandedForm:XR
~~~~
> 


**Method: **getAdditionalRelationLabel(String ticket,String version,String additionalrelationLabel)

**Returns:**AdditionalRelationLabelDTO

**Use Case:** Given a UMLS release and an abbreviation for an additional relation (RELA), this call returns the expanded name of the additional relation as well as the supplied abbreviation. Additional relations are asserted by the source vocabulary and not all terms have an additional relation. The abbreviations are very similar to the expanded forms for most additional relations with slight differences in capitalization or word-delimiting (e.g., spaces versus underlines).

#### Sample Input (Java):

~~~~
myAdditionalRelationLabel =utsMetadataService.getAdditionalRelationLabel(ticket, umlsRelease,"origin_of");
 String expandedForm = myAdditionalRelationLabel.getExpandedForm();
 String abbreviation = myAdditionalRelationLabel.getAbbreviation();
 String inverseExpForm =myAdditionalRelationLabel.getInverse().getExpandedForm();
 String inverseExpForm =myAdditionalRelationLabel.getInverse().getAbbreviation();
~~~~

#### Sample Input (C♯):

~~~~
Metadata.additionalRelationLabelDTO myAdditionalRelationLabel =utsMetadataService.getAdditionalRelationLabel(singleUseTicket, "2012AB","origin_of");
string expandedForm = myAdditionalRelationLabel.expandedForm;
 string abbreviation = myAdditionalRelationLabel.abbreviation;
 string inverseExpandedForm =myAdditionalRelationLabel.inverse.expandedForm;
 string inverseAbbreviation =myAdditionalRelationLabel.inverse.abbreviation;
~~~~

#### Sample Output:

~~~~  
   ExpandedForm:Origin of
   Abbreviation:origin_of
   InverseExpandedForm:Has origin
   InverseAbbreviationForm:Has origin
~~~~
>


**Method: **getAllAdditionalRelationLabels(String ticket,String version)

**Returns:**ArrayList<AdditionalRelationLabelDTO>

**Use Case:** Given a UMLS release, this call returns all the valid additional relations (RELA) for the release. Additional relations are asserted by the source vocabulary and not all terms have an additional
relation. The abbreviations are very similar to the expanded forms for most additional relations with slight differences in capitalization or word-delimiting (e.g., spaces versus underlines).


#### Sample Input (Java):

~~~~
myarrAdditionalRelationLabel =utsMetadataService.getAllAdditionalRelationLabels(ticket, umlsRelease);
 for (int i = 0; i < myarrAdditionalRelationLabel.size(); i++) {
 String expandedForm = myarrAdditionalRelationLabel.getExpandedForm();
 String abbreviation = myarrAdditionalRelationLabel.getAbbreviation();
 String inverseExpForm =myarrAdditionalRelationLabel.getInverse().getExpandedForm();
 String inverseExpForm =myarrAdditionalRelationLabel.getInverse().getAbbreviation();
 }
~~~~

#### Sample Input (C♯):

~~~~
Metadata.additionalRelationLabelDTO[] myAdditionalRelationLabelDTO =utsMetadataService.getAllAdditionalRelationLabels(singleUseTicket,"2012AB");
 for (int i = 0; i < myAdditionalRelationLabelDTO.Length; i++) {
 Metadata.additionalRelationLabelDTO myArrayAdditionalRelationLabel =myAdditionalRelationLabelDTO[i];
 string expandedForm = myArrayAdditionalRelationLabel.expandedForm;
 string abbreviation = myArrayAdditionalRelationLabel.abbreviation;
 string inverseExpandedForm =myArrayAdditionalRelationLabel.inverse.expandedForm;
 string inverseAbbreviation =myArrayAdditionalRelationLabel.inverse.abbreviation;
~~~~

#### Sample Output:

~~~~
   ExpandedForm:abnormal cell affected by chemical or drug
   Abbreviation:abnormal_cell_affected_by_chemical_or_drug
   Inverse ExpandedForm:chemical or drug affects abnormal cell
   Inverse Abbreviation:chemical_or_drug_affects_abnormal_cell
   ExpandedForm:abnormality associated with allele
   Abbreviation:abnormality_associated_with_allele
   Inverse ExpandedForm:allele has abnormality
   Inverse Abbreviation:allele_has_abnormality
   ExpandedForm:Access device used by
   Abbreviation:access_device_used_by
   Inverse ExpandedForm:Uses access device
   Inverse Abbreviation:uses_access_device
   ExpandedForm:Access of
   Abbreviation:access_of
   Inverse ExpandedForm:Has access
   Inverse Abbreviation:has_access
   ExpandedForm:Active ingredient of
   Abbreviation:active_ingredient_of
   Inverse ExpandedForm:Has active ingredient
   Inverse Abbreviation:has_active_ingredient
   and so on..\
~~~~

  