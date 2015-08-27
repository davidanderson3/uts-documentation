title=Attribute Metadata
date=2015-08-21
updated=2015-08-21
type=page
status=unpublished
category=Metadata
navorder=4
~~~~~~


**Method: **getAttributeName(String ticket,String version,String attributeName)

**Returns:** AttributeNameDTO

**Use Case:** Given a UMLS release and an attribute name abbreviation (ATN), this call returns the expanded form of the attribute name.

#### Sample Input (Java):

~~~~
myAttributeName = utsMetadataService.getAttributeName(ticket, umlsRelease, "TH");
 String abbreviation = myAttributeName.getAbbreviation();
 String expandedForm = myAttributeName.getExpandedForm();
~~~~

#### Sample Input (C#):

~~~~
Metadata.attributeNameDTO myAttributeName =utsMetadataService.getAttributeName(singleUseTicket, "2012AB", "TH");
 string abbreviation = myAttributeName.abbreviation;
 string expandedForm = myAttributeName.expandedForm;
~~~~

#### Sample Output:

~~~~
  Abbreviation:TH
   ExpandedForm:MeSH Thesaurus ID - identifies thesauri other than MeSH in which the MeSH heading or cross-reference is included.
~~~~
>


**Method: **getAllAttributeNames(String ticket,String version)

**Returns:** ArrayList<AttributeNameDTO>

**Use Case:** Given a UMLS release, this call returns all attribute names for the release. Each attribute is returned in abbreviated form and expanded form.

#### Sample Input (Java):
~~~~
myarrAttributeName = utsMetadataService.getAllAttributeNames(ticket, umlsRelease);
 for (int i = 0; i < myarrAttributeName.size(); i++) {
 AttributeNameDTO myarrAttributeNameDTO = myarrAttributeName.get(i);
 String abbreviation = myarrAttributeNameDTO.getAbbreviation();
 String expandedForm = myarrAttributeNameDTO.getExpandedForm();
 }
~~~~

#### Sample Input (C#):
~~~~
Metadata.attributeNameDTO[] myAttributeNameDTO = utsMetadataService.getAllAttributeNames(singleUseTicket, "2012AB");
 for (int i = 0; i < myAttributeNameDTO.Length; i++) {
 Metadata.attributeNameDTO myArrayAttributeNameDTO =myAttributeNameDTO[i];
 string abbreviation = myArrayAttributeNameDTO.abbreviation;
 string expandedForm = myArrayAttributeNameDTO.expandedForm;
}
~~~~


#### Sample Output:

~~~~
   Abbreviation:AAL_TERM
   ExpandedForm:AAL term
   Abbreviation:ACCEPTED_THERAPEUTIC_USE_FOR
   ExpandedForm:Accepted therapeutic use for
   Abbreviation:ACCESSION_NO
   ExpandedForm:Accession number
   Abbreviation:ADJACENT
   ExpandedForm:Adjacent
   Abbreviation:ALT_SORT_CODE
   ExpandedForm:Alt sort code
   Abbreviation:AMBIGUITY_FLAG
   ExpandedForm:Source atom ambiguity flag
   Abbreviation:AMT
   ExpandedForm:AOT uses MeSH term
   Abbreviation:AN
   ExpandedForm:MeSH Annotation - an informative MeSH note written primarily for indexers or catalogers that may also be useful in explaining the use of a MeSH term to online searchers.
   Abbreviation:ANADA
   ExpandedForm:Abbreviated New Animal Drug application number for the generic drug for MTHSPL
   Abbreviation:ANATOMICAL_COORDINATE
   ExpandedForm:Anatomical coordinate
   Abbreviation:ANATOMICAL_OR_ARBITRARY
   ExpandedForm:Anatomical or Arbitrary
   Abbreviation:ANDA
   ExpandedForm:Abbreviated New (Generic) Drug application number for the MTHSPL drug
   Abbreviation:AQ
   ExpandedForm:SNOMED CT "allowable qualifier" attribute for representing certain relationships (those having a characteristic type of "Qualifier" and a refinability of "Mandatory") which indicate one of several allowable types of qualifiers, such as laterality or severity, that a concept may have
   Abbreviation:AQL
   ExpandedForm:MeSH Allowable Qualifier - list of allowable qualifier abbreviations for MeSH main headings (e.g. AA, CL, CS, DF, DU, IM, I,P ME, PK)
   Abbreviation:BIOCARTA_ID
   ExpandedForm:BioCarta online maps of molecular pathways, adapted for NCI use ID
   Abbreviation:BLA
   ExpandedForm:Therapeutic Biologic Applications number for the MTHSPL drug
   Abbreviation:BLOCK
   ExpandedForm:Block code
   Abbreviation:CAS_REGISTRY
   ExpandedForm:CAS Registry
   Abbreviation:CCDS_ID
   ExpandedForm:CCDS ID
   Abbreviation:CCF
   ExpandedForm:Canonical Clinical Problem Statement System (CCPSS) frequency - the number of times a CCPSS term appears in a patient record.
   Abbreviation:CCI
   ExpandedForm:ICD-9-CM code(s) clusters in a Clinical Classifications Software (CCS) category - individual ICD-9-CM codes (or ranges of such codes) classified into CCS categories.
   Abbreviation:CELL_APPENDAGE_TYPE
   ExpandedForm:Cell appendage type
   Abbreviation:CELL_LAYER
   ExpandedForm:Cell layer
   Abbreviation:CFR
   ExpandedForm:Code of Federal Regulation Number (e.g. 862.3220, 892.1610)
   Abbreviation:CHANGE_REASON_PUBLIC
   ExpandedForm:Detailed explanation about special changes to the term over time.
   Abbreviation:CHAPTER
   ExpandedForm:Chapter code
   Abbreviation:CHAPTER_NOTE
   ExpandedForm:Chapter note
   Abbreviation:CHARACTERISTICTYPE
   ExpandedForm:SNOMED CT indication of whether a relationship specifies a defining characteristic of the source concept or a possible qualification of that Concept.
   Abbreviation:CHEMICAL_FORMULA
   ExpandedForm:Chemical Formula
   Abbreviation:CHROMOSOME
   ExpandedForm:Chromosome
   Abbreviation:CHROMOSOME_PAIRS_PER_NUCLEUS
   ExpandedForm:Chromosome pairs per nucleus
   Abbreviation:CITE
   ExpandedForm:Citation or edition information
   Abbreviation:CNU
   ExpandedForm:ISO 3166-1 standard country code in numeric (three-digit) format
   Abbreviation:COATING
   ExpandedForm:FDA Structured Product Label imprint attribute for coating
   Abbreviation:CODE
   ExpandedForm:Code
   Abbreviation:CODE_ALSO
   ExpandedForm:Instructs that 2 codes may be required to fully describe a condition but the sequencing of the two codes is discretionary, depending on the severity of the conditions and the reason for the encounter.
   Abbreviation:CODE_FIRST
   ExpandedForm:Certain conditions have both an underlying etiology and multiple body system manifestations due to the underlying etiology. ICD-10-CM has a coding convention that requires the underlying condition be sequenced first followed by the manifestation. Wherever such a combination exists there is a "code first" note at the manifestation code. These instructional notes indicate the proper sequencing order of the codes, etiology followed by manifestation. In most cases the manifestation codes will have in the code title, "in diseases classified elsewhere." Codes with this title are a component of the etiology/manifestation convention. The code title indicates that it is a manifestation code. "In diseases classified elsewhere" codes are never permitted to be used as first listed or principle diagnosis codes. They must be used in conjunction with an underlying condition code and they must be listed following the underlying condition.
   Abbreviation:COLOR
   ExpandedForm:FDA Structured Product Label imprint attribute for color
   Abbreviation:COLORTEXT
   ExpandedForm:FDA Structured Product Label imprint attribute for color text
   Abbreviation:COMBO_SCORE
   ExpandedForm:Combo Score
   Abbreviation:COMBO_SCORE_NO_TOP_WORDS
   ExpandedForm:Combo Score that has no top words
   Abbreviation:COMMON_TEST_RANK
   ExpandedForm:Numeric ranking of approximately 2,000 common tests performed by hospitals
   Abbreviation:CONCEPTSTATUS
   ExpandedForm:SNOMED CT status which indicates whether a concept is in active use and, if not, indicates the reason it is inactive.
   Abbreviation:CONNECTED_TO
   ExpandedForm:Connected to
   Abbreviation:CONNECTION_TYPE
   ExpandedForm:Connection type
   Abbreviation:CONSIDER
   ExpandedForm:Codes to consider before definitive diagnosis
   Abbreviation:CONSUMER_NAME
   ExpandedForm:An experimental (beta) consumer friendly name
~~~~