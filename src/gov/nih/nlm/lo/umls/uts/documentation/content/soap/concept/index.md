title=Retrieving UMLS Concept Information from UTS SOAP API
date=2015-08-14
updated=2015-08-14
type=page
status=unpublished
navorder=3
~~~~~~


**Method: **getConcept(String ticket,String version,String conceptId)

**Returns:**ConceptDTO

**Use Case:** Get the properties of a UMLS Concept, such as the preferred name, semantic types, and the number of atoms included in a concept. Other properties are included in the ConceptDTO Javadocs. In the example below, we retrieve information about C0004057, the UMLS concept for "aspirin".

#### Sample Input (Java):
~~~~
ConceptDTO myConcept = utsContentService.getConcept(ticket, "2011AB", "C0004057");
String preferredName = myConcept.getDefaultPreferredName();
List<String> semanticTypes = myConcept.getSemanticTypes();
int numberofAtoms = myConcept.getAtomCount();
 
~~~~


#### Sample Input (C♯):

~~~~
content.conceptDTO myConcept = utsContentService.getConcept(ticket,"2011AB", "C0004057");
 string preferredName = myConcept.defaultPreferredName;
 string[] semanticTypes = myConcept.semanticTypes;
 int numberofAtoms = myConcept.atomCount;
~~~~

#### Sample Output:
~~~~
//print out the results
   Concept Preferred Name: Aspirin
   Semantic Types: [T109, T121]
   # of Atoms in this Concept: 140
~~~~
>

**Method: **(String ticket,String version,PSF psf)

**Returns:**ArrayList< ConceptDTO>

**Use Case:** Get all new UMLS Concepts for a given release, and it's related properties such as the preferred name, semantic types, date added, status etc.


#### Sample Input (Java):

~~~~
UtsMetathesaurusContent.Psf myPsf = new UtsMetathesaurusContent.Psf();
 java.util.List<ConceptDTO> myConcept = new ArrayList<ConceptDTO>();

 ConceptDTO myConcept = utsContentService.getNewConcepts(ticket, "2014AA", myPsf);

 for (int i = 0; i < myConcepts.size(); i++) {
 ConceptDTO con = myConcepts.get(i);
 String ui = con.getUi();
 String defaultPrfName = con.getDefaultPreferredName();
 String status = con.getStatus();
 XMLGregorianCalendar dateAdded = con.getDateAdded();
 java.util.List semType = con.getSemanticTypes();
 }

~~~~


#### Sample Output:

 Concept|DefaultPreferredName|Status|DateAdded|SemanticType
 --- | --- | --- | --- | ---
C3667110|Betamethasone 0.284 MG/ML / Gentamicin Sulfate (USP) 0.57 M G/ML Topical Spray [Gentaspray]|R|2014-05-01T00:00:00-04:00 |[T200]
C3667111|octyl sulfate|R|2014-05-01T00:00:00-04:00|[T109, T121]  
C3667112|Menthol 6 MG/ML|R|2014-05-01T00:00:00-04:00|[T200]       
C3667113|Colloidal oatmeal / Menthol Topical Product||R|2014-05-01T00:00:00-04:00|[T200]
C3667114|Colloidal oatmeal / Menthol Topical Cream|R|2014-05-01T00:00:00-04:00|[T200]
C3667115|Colloidal oatmeal / Menthol|R|2014-05-01T00:00:00-04:00|[T121]

>

**Method: **getNewConceptsCount(String ticket,String version)

**Returns:**ArrayList< ConceptDTO>

**Use Case:** Get all new UMLS Concepts for a given release, and it's related properties such as the preferred name, semantic types, date added, status etc.

#### Sample Input (Java):

~~~~
BigDecimal myConcept = new BigDecimal(0);
 ConceptDTO myConcept = utsContentService.getNewConceptsCount(ticket, "2014AA");
 int intValue = myConcept.intValue();
~~~~

#### Sample Output:

~~~~
  Total concepts for 2014AA: 49090
~~~~

>

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

**Method: **getConceptAttributes(String ticket,String version,String conceptId,PSF psf)

**Returns:**ArrayList< AttributeDTO>

**Use Case:** You have a known UMLS CUI and want to see attributes suchas the name/value pair of the attribute. Other properties are available (see the Javadocs).


**Note:** AttributeDTOs are sorted by default on the Name field. You can use a PSF object to sort by UI or RootSource.


#### Sample Input (Java):

~~~~
UtsMetathesaurusContent.Psf myPsf = new UtsMetathesaurusContent.Psf();
 List<AttributeDTO> myAttributes = new ArrayList<AttributeDTO>();
 myAttributes = utsContentService.getConceptAttributes(ticket, 2011AB, "C2711988",myPsf);
 for (int i = 0; i < myAttributes.size(); i++) {

 AttributeDTO myAttributeDTO = myAttributes.get(i);
 String attributeName = myAttributeDTO.getName();
 String attributeValue = myAttributeDTO.getValue();

 }
 
~~~~

#### Sample Input (C♯):

~~~~
content.psf myPsf = new content.psf();
 content.attributeDTO[] myAttributes = utsContentService.getConceptAttributes(ticket, "2011AB", "C2711988", myPsf);

 for (int i = 0; i < myAttributes.Length; i++){

 content.attributeDTO myAttributeDTO = myAttributes[i];
 string attributeName = myAttributeDTO.name;
 string attributeValue = myAttributeDTO.value;
 
 }
~~~~
 
 

#### Sample Output:

~~~~
   Attribute Name: CV_ALGORITHM
   Attribute Value: The creation of this content view is based on the list of SNOMED CT concept IDs in the latest release of the CORE Problem List Subset of SNOMED CT, excluding those that are retired from the Subset. It contains all atoms linked to that SNOMED CT concept with LAT=ENG and SUPPRESS=N.
  
   Attribute Name: CV_CATEGORY
   Attribute Value: Problem List
  
   Attribute Name: CV_CLASS
   Attribute Value: COMPLETE
  
   Attribute Name: CV_CODE
   Attribute Value: 2048
 
   Attribute Name: CV_CONTRIBUTOR
   Attribute Value: National Library of Medicine
  
   Attribute Name: CV_CONTRIBUTOR_DATE
   Attribute Value: 20110802
  
   Attribute Name: CV_CONTRIBUTOR_URL
   Attribute Value: http://www.nlm.nih.gov/research/umls/Snomed/core_subset.html
  
   Attribute Name: CV_CONTRIBUTOR_VERSION
   Attribute Value: 201108
  
   Attribute Name: CV_DESCRIPTION
   Attribute Value: This content view contains the subset of SNOMED CT concepts that are most frequently used in problem lists. The subset is derived from datasets from large health care institutions. The most commonly used problem list terms are mapped to SNOMED CT and the UMLS. The use of SNOMED CT contents in this subset is subject to the SNOMED CT license requirements. The use of SNOMED CT is free in IHTSDO member countries (including the U.S.) and low income countries.
  
   Attribute Name: CV_INCLUDE_OBSOLETE
   Attribute Value: N
  
   Attribute Name: CV_IS_GENERATED
   Attribute Value: N
  
   Attribute Name: CV_MAINTAINER
   Attribute Value: National Library of Medicine
  
   Attribute Name: CV_MAINTAINER_DATE
   Attribute Value: 20110802
  
   Attribute Name: CV_MAINTAINER_URL
   Attribute Value: http://www.nlm.nih.gov/research/umls/Snomed/core_subset.html
  
   Attribute Name: CV_MAINTAINER_VERSION
   Attribute Value: 201108
  
~~~~
