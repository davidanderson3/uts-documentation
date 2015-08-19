title=Retrieving UMLS SUI Information from UTS SOAP API
date=2015-08-14
updated=2015-08-14
type=page
status=published
category=Retrieving UMLS Concepts
navorder=5
~~~~~~

>

**Method:**getTermStrings(String ticket,String version,String termId,PSF psf)

**Returns:**ArrayList<TermStringDTO>(see javadocs)(javadocs/gov/nih/nlm/umls/dto/content/TermStringDTO.html)

**Use Case:**You have a known term identifier (LUI), and want to see all the strings included in the term, including the identifier of the strings (SUI), name of the string, and the number of atoms in each SUI.


**Note:**TermDTOs are sorted by default on the Name field.


#### Sample Input (Java):

~~~~
UtsMetathesaurusContent.Psf myPsf = new UtsMetathesaurusContent.Psf();

 List<TermStringDTO> myTermStrings = new ArrayList<TermStringDTO>();
 myTermStrings = utsContentService.getTermStrings(ticket, 2011AB,"L0001339",myPsf);

 for (int i = 0; i < myTermStrings.size(); i++) {

 TermStringDTO myTermStringDTO = myTermStrings.get(i);
 String sui = myTermStringDTO.getUi();
 String name = myTermStringDTO.getName();
 int numberOfAtoms = myTermStringDTO.getAtomCount();

 }
~~~~

#### Sample Input (Câ™¯):

~~~~
content.psf myPsf = new content.psf();
 content.termStringDTO[] myTermStrings = utsContentService.getTermStrings (ticket, "2011AB", "L0001339", myPsf);

 for (int i = 0; i < myTermStrings.Length; i++)
 {
 content.termStringDTO myTermStringDTO = myTermStrings[i];
 string sui = myTermStringDTO.ui;
 string name = myTermStringDTO.name;
 int numberOfAtom = myTermStringDTO.atomCount;

 }
~~~~

#### Sample Output:

~~~~
   SUI: S0468716
   String Name: Acute Pancreatitis
   Number of atoms in this string: 2
  
   SUI: S0218486
   String Name: Acute pancreatitis
   Number of atoms in this string: 14
  
   SUI: S0585418
   String Name: Acute pancreatitis NOS
   Number of atoms in this string: 3
  
   SUI: S0392863
   String Name: PANCREATITIS ACUTE
   Number of atoms in this string: 4
  
   SUI: S0223833
   String Name: PANCREATITIS, ACUTE
   Number of atoms in this string: 1
  
   SUI: S3464991
   String Name: Pancreatitis (& [acute NOS])
   Number of atoms in this string: 2
  
   SUI: S1619379
   String Name: Pancreatitis acute
   Number of atoms in this string: 2
  
   SUI: S0394883
   String Name: Pancreatitis, acute
   Number of atoms in this string: 1
  
   SUI: S1425454
   String Name: acute pancreatitis
   Number of atoms in this string: 4
  
   SUI: S4103199
   String Name: acute; pancreatitis
   Number of atoms in this string: 1
  
   SUI: S4109436
   String Name: pancreatitis; acute
   Number of atoms in this string: 1
~~~~



**Method:Â **getTermString(String ticket,String version,String
termStringId)

**Returns:**TermStringDTO(see
javadocs)(javadocs/gov/nih/nlm/umls/dto/content/TermStringDTO.html)


**Use Case:**Â You have a known string identifier (SUI) and you want to know its name, as well as the term associated with it, as well as the normalized name of the term.


#### Sample Input (Java):

~~~~
TermStringDTO myTermString = utsContentService.getTermString(ticket, 2011AB, "S11846460");

 String name = myTermString.getName();
 int atomCount = myTermString.getAtomCount();
 String lui = myTermString.getTerm().getUi();
 String luiName = myTermString.getTerm().getDefaultPreferredName();
~~~~

#### Sample Input (C#):

~~~~
content.termStringDTO myTermString = utsContentService.getTermString(ticket, "2011AB", "S11846460");
 content.termStringDTO temp = myTermString;

 string name = myTermString.name;
 int atomCount = myTermString.atomCount;
 string lui = myTermString.term.ui;
 string luiName = myTermString.term.defaultPreferredName;
~~~~


#### Sample Output:

~~~~
   String name: age related osteoporosis
   Number of atoms in this string: L0001787
   LUI associated with this string: 1
   Normalized Term associated with this string: Osteoporosis, Age-Related
~~~~

>

**Method:**getTermStringAtoms(String ticket,String version,String termStringId,PSF psf)
**Returns:**ArrayList<AtomDTO>(see
javadocs)(javadocs/gov/nih/nlm/umls/dto/content/AtomDTO.html)


**Use Case:**Â You have string identifier (SUI) and want to see which sources contribute atoms to that string, along with the AUI and the term type of each atom.


**Note:**Â AtomDTOs have other embedded objects such as SourceAtomClusterDTO, ConceptDTO, and TermStringDTO. These other objects and their methods are accessible via getters. You can access, for example, the CUI that the atom belongs to by using getConcept().getUi();
See Javadocs for more details.



#### Sample Input (Java):

~~~~

UtsMetathesaurusContent.Psf myPsf = new UtsMetathesaurusContent.Psf();
 List<AtomDTO> myAtoms = new ArrayList<AtomDTO>();
 myAtoms = utsContentService.getTermStringAtoms(ticket, 2011AB,"S0020337",myPsf);

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
 content.atomDTO[] myAtoms = utsContentService.getTermStringAtoms(ticket, "2011AB", "S0020337", myPsf);

 for (int i = 0; i < myAtoms.Length; i++){

 content.atomDTO myAtomDTO = myAtoms [i];
 string aui = myAtomDTO.ui;
 string source = myAtomDTO.rootSource;
 string name = myAtomDTO.termString.name;
 string TermType = myAtomDTO.termType;
 }
~~~~

#### Sample Output:

~~~~
   AUI: A15661454
   Source Vocabulary: MEDLINEPLUS
   Term Type:ET
   String Name: Bovine Spongiform Encephalopathy
   AUI: A18013382
   Source Vocabulary: NDFRT
   Term Type:SY
   String Name: Bovine Spongiform Encephalopathy
   AUI: A0032344
   Source Vocabulary: MSH
   Term Type:EP
   String Name: Bovine Spongiform Encephalopathy
~~~~

