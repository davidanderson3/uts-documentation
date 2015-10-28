title=Retrieving UMLS Concept Information from UTS SOAP API
date=2015-08-14
updated=2015-08-14
type=page
status=unpublished
navorder=3
~~~~~~



Interface | Method | Use Case | Object or Data type Returned 
-- | -- | -- | --
**UtsWsContentController**||||
 |[getConcept](#getconcept)|Retrieve information for a known UMLS CUI, such as preferred name, number of atoms, number of definitions.|ConceptDTO
 |[getConceptAtoms](/soap/atoms/index.html#getconceptatoms)|Retrieve atoms (terms that are considered synonymous) for a known UMLS CUI|ArrayList\<AtomDTO\>
 |[getNewConcepts](#getnewconcepts)|Retrieves new Concepts for a known UMLS publication.|ArrayList\<ConceptDTO\>
 |[getNewConceptsCount](#getnewconceptscount)|Retrieves the number of new concepts for a known UMLS publication|int

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

