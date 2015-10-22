title=Retrieving UMLS atoms from the UTS SOAP API
date=2015-10-22
updated=2015-10-22
type=page
status=unpublished
navorder=3
~~~~~~

Interface | Method | Use Case | Object or Data type Returned 
-- | -- | -- | --
**UtsWsContentController**|||
 |[getConceptAtoms](#getconceptatoms)|Retrieve atoms for a known UMLS CUI. You can then filter atoms according to term type, source vocabulary, suppressibility, etc. |ArrayList\<AtomDTO\>
 |[getSourceConceptAtoms](#getsourceconceptatoms)|Retrieve atoms for a known source-asserted concept. You can then filter atoms according to term type, source vocabulary, suppressibility, etc. |ArrayList\<AtomDTO\>
 |[getSourceDescriptorAtoms](#getsourcedescriptoratoms)|Retrieve atoms for a known source-asserted descriptor. You can then filter atoms according to term type, source vocabulary, suppressibility, etc. |ArrayList\<AtomDTO\>
 |[getCodeAtoms](#getsourcedescriptoratoms)|Retrieve atoms for a known source-asserted code. You can then filter atoms according to term type, source vocabulary, suppressibility, etc. |ArrayList\<AtomDTO\>
 
 
 
### getConceptAtoms


### getSourceConceptAtoms

**Method Signature:** ```getSourceConceptAtoms(String ticket, String version, String sourceConceptId, String rootSourceAbbreviation, PSF psf)```


#### Sample Input (Java):

~~~~
 gov.nih.nlm.uts.webservice.content.Psf myPsf = new gov.nih.nlm.uts.webservice.content.Psf();
 List<AtomDTO> myAtoms = new ArrayList<AtomDTO>();
 myAtoms = utsContentService.getSourceConceptAtoms(ticket, "2015AA","9468002","SNOMEDCT_US",myPsf);

 for (AtomDTO atom:myAtoms) {

 String aui = atom.getUi();
 String tty = atom.getTermType();
 String name = atom.getTermString().getName();
 boolean isObsolete = atom.isObsolete();

 }
~~~~

#### Sample Output

~~~~text
A3357646|PT|Closed fracture carpal bone|false
A3357644|FN|Closed fracture carpal bone (disorder)|false
A4754365|IS|Closed fracture carpal bone, NOS|true
A2889793|SY|Closed fracture of carpal bone|false
A3358392|SY|Closed fracture of wrist|false
A4754444|IS|Closed fracture of wrist, NOS|true
~~~~

### getSourceDescriptorAtoms


### getCodeAtoms