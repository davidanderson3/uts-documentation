title=Retrieving UMLS Term Information from UTS SOAP API
date=2015-08-14
updated=2015-08-14
type=page
status=published
navorder=4
~~~~~~


**Method:**getTerm(String ticket,String version,String termId)

**Returns:**TermDTO(see javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/content/TermDTO.html)

**Use Case:**You have a term identifier (LUI) and want to know how many strings are associated with it, as well as the normalized form of the term. Other properties are available in the Javadocs.


#### Sample Input (Java):

~~~~

TermDTO myTerm = utsContentService.getTerm(ticket, 2011AB, "L0214737");

 String name = myTerm.getDefaultPreferredName();
 String normForm = myTerm.getNormForm();
 int numberofStrings = myTerm.getTermStringCount();
 
~~~~


#### Sample Input (C#):

~~~~
content.termDTO myTerm = utsContentService.getTerm(ticket, "2011AB", "L0214737");

 string name = myTerm.defaultPreferredName;
 string normForm = myTerm.normForm;
 int numberofStrings = myTerm.termStringCount;

~~~~


#### Sample Output:

~~~~
   Term Name: Bartter Syndrome
   Normalized Form: bartter syndrome
   Number of Strings in this Term: 13
   
~~~~
>


**Method:**getTermAtoms(String ticket,String version,String termId,PSF psf)

**Returns:**ArrayList<AtomDTO>(see javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/content/AtomDTO.html)

**Use Case:**You have a LUI and want to view all the atom names associated with it, as well as the source vocabulary and term type of each atom.

**Note:**AtomDTOs have other embedded objects such as SourceAtomClusterDTO, ConceptDTO, and TermStringDTO. These other objects and their methods are accessible via getters. You can access, for example, the CUI that the atom belongs to by using getConcept().getUi();
See Javadocs for more details.

#### Sample Input (Java):

~~~~
List<AtomDTO> myAtoms = new ArrayList<AtomDTO>();
 myAtoms = utsContentService.getTermAtoms(ticket, 2011AB, "L0011880",myPsf);
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
 content.atomDTO[] myAtoms = utsContentService.getTermAtoms(ticket, "2011AB", "L0011880", myPsf);

 for (int i = 0; i < myAtoms.Length; i++){

 content.atomDTO myAtomDTO = myAtoms[i];
 string aui = myAtomDTO.ui;
 string source = myAtomDTO.rootSource;
 string name = myAtomDTO.termString.name;
 string TermType = myAtomDTO.termType;

 }
 
~~~~

#### Sample Output:

~~~~
  AUI: A10865851
   Source Vocabulary: SNOMEDCT
   Term Type:IS
   String Name: Diabetic ketoacidosis
   AUI: A4778386
   Source Vocabulary: SNOMEDCT
   Term Type:IS
   String Name: Diabetic ketoacidosis
   AUI: A4778387
   Source Vocabulary: SNOMEDCT
   Term Type:IS
   String Name: Diabetic ketoacidosis
   AUI: A10865852
   Source Vocabulary: SNOMEDCT
   Term Type:PT
   String Name: Diabetic ketoacidosis
   AUI: A5002495
   Source Vocabulary: SNOMEDCT
   Term Type:IS
   String Name: Ketoacidosis - diabetic
   AUI: A5002494
   Source Vocabulary: SNOMEDCT
   Term Type:IS
   String Name: Ketoacidosis - diabetic
~~~~
