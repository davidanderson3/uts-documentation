title=Retrieving UMLS Concept Information from UTS SOAP API
date=2015-08-14
updated=2015-08-14
type=page
status=unpublished
navorder=3
~~~~~~



Method | Use Case | Object or Data type Returned | Interface
-- | --
[getConcept](#getconcept) | Retrieve information for a known UMLS CUI, such as preferred name, number of atoms, number of definitions. | ConceptDTO | UtsWsContentController
[getConceptAtoms](#getconceptatoms) | Retrieve atoms (terms that are considered synonymous) for a known UMLS CUI | ArrayList<AtomDTO> | UtsWsContentController
[getNewConcepts](#getnewconcepts) | Retrieves new Concepts for a known UMLS publication. | ArrayList<ConceptDTO> | UtsWsContentController
[getNewConceptsCount](#getnewconceptscount) | Retrieves the number of new concepts for a known UMLS publication | int | UtsWsContentController

**Each of these methods requires an instance of the UtsWsContentController interface, such as**:

```ConceptDTO concept = utsContentService.getConcept(ticket, "2015AA", "C0018787");```


### getConcept

**Method Signature: **getConcept(String ticket,String version,String conceptId)

#### Sample Input (Java):

~~~~java

ConceptDTO concept = utsContentService.getConcept(ticket, "2011AB", "C0004057");
String name = concept.getDefaultPreferredName();
List<String> semanticTypes = concept.getSemanticTypes();
int numberofAtoms = concept.getAtomCount();
 
~~~~


#### Sample Input (C♯):

~~~~java
 ConceptDTO concept = utsContentService.getConcept(ticket,"2011AB", "C0004057");
 string name = concept.defaultPreferredName;
 string[] semanticTypes = concept.semanticTypes;
 int numberofAtoms = concept.atomCount;
~~~~

#### Sample Output:

~~~~
//print out the results
   Concept Preferred Name: Aspirin
   Semantic Types: [T109, T121]
   # of Atoms in this Concept: 140
~~~~

### getConceptAtoms

**Method Signature:** getConceptAtoms(String ticket,String version,String conceptId,PSF psf)

#### Sample Input (Java):

~~~~java

 List<AtomDTO> atoms = new ArrayList<AtomDTO>();
 atoms = utsContentService.getConceptAtoms(ticket, "2011AB","C0004775",myPsf);
 UtsMetathesaurusContent.Psf myPsf = new UtsMetathesaurusContent.Psf();
 myPsf.getIncludedSources().add("SNOMEDCT");
 myPsf.getIncludedTermTypes().add("FSN");
 myPsf.getIncludedTermTypes().add("SY");
 myPsf.getIncludedTermTypes().add("PT");

 for (AtomDTO atom:atoms) {

   String aui = atom.getUi();
   String source = atom.getRootSource();
   String name = atom.getTermString().getName();
   String tty = atom.getTermType();

 }
~~~~

#### Sample Input (C#):

~~~~c#
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

~~~~text
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


### getNewConcepts

**Method Signature: **getNewConcepts(String ticket,String version,PSF psf)

#### Sample Input (Java):

~~~~java
  
 UtsMetathesaurusContent.Psf myPsf = new UtsMetathesaurusContent.Psf();
 List<ConceptDTO> concepts = new ArrayList<ConceptDTO>();

 concepts = utsContentService.getNewConcepts(ticket, "2014AA", myPsf);

 for (ConceptDTO concept:concepts) {
 
   String ui = concept.getUi();
   String name = concept.getDefaultPreferredName();
   List semanticTypes = concept.getSemanticTypes();

 }

~~~~


#### Sample Output:

~~~~text
 Concept|DefaultPreferredName|Status|DateAdded|SemanticType
 C3667110|Betamethasone 0.284 MG/ML / Gentamicin Sulfate (USP) 0.57 M G/ML Topical Spray [Gentaspray]|R|2014-05-01T00:00:00-04:00 |[T200]
 C3667111|octyl sulfate|R|2014-05-01T00:00:00-04:00|[T109, T121]  
 C3667112|Menthol 6 MG/ML|R|2014-05-01T00:00:00-04:00|[T200]       
 C3667113|Colloidal oatmeal / Menthol Topical Product||R|2014-05-01T00:00:00-04:00|[T200]
 C3667114|Colloidal oatmeal / Menthol Topical Cream|R|2014-05-01T00:00:00-04:00|[T200]
 C3667115|Colloidal oatmeal / Menthol|R|2014-05-01T00:00:00-04:00|[T121]
 ...
~~~~


### getNewConceptsCount

**Method Signature: **getNewConceptsCount(String ticket,String version)

#### Sample Input (Java):

~~~~java
 int numberOfConcepts = utsContentService.getNewConceptsCount(ticket, "2014AA");
~~~~

#### Sample Output:

~~~~text
  Total new concepts for 2014AA: 49090
~~~~

