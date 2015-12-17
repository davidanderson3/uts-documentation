title=Retrieving UMLS Attribute Information from UTS SOAP API
date=2015-08-18
updated=2015-08-18
type=page
status=published
navorder=11
~~~~~~

Interface | Method | Use Case | Object or Data type Returned 
-- | -- | -- | --
**UtsWsContentController**||||
 |[getSourceConceptAttributes](#getsourceconceptattributes)|Retrieve attributes of known source-asserted concepts|ArrayList\<AttributeDTO\>
 |[getSourceDescriptorAttributes](#getsourcedescriptorattributes)|Retrieve attributes of known source-asserted descriptors|ArrayList\<AttributeDTO\>
 |[getCodeAttributes](#getcodeattributes)|Retrieve attributes of known source-asserted codes|ArrayList\<AttributeDTO\>
 |[getAtomAttributes](#getatomattributes)|Retrieve attributes of known source-asserted atoms|ArrayList\<AttributeDTO\>

**Each of these examples below requires an instance of the [UtsWsContentController](/soap/installation/interface-setup.html#utswscontentcontroller), [UtsWsMetadataController](/soap/installation/interface-setup.html#utswsmetadatacontroller) and [UtsWsSecurityController](/soap/installation/interface-setup.html#utswssecuritycontroller) interfaces**.

### getCodeAttributes

**Method Signature:** ```getCodeAttributes(String ticket,String version,String codeId,String rootSourceAbbreviation,PSF psf)```

#### Sample Input (Java):

~~~~java
int pageNum = 1;
String currentUmlsRelease = utsMetadataService.getCurrentUMLSVersion(ticket);
List<AttributeDTO> attributes = new ArrayList<AttributeDTO>();
     
     do {
    	 myPsf.setPageNum(pageNum);
         //attributes of LOINC code 2742-5, "Angiotensin converting enzyme [Enzymatic activity/volume] in Serum or Plasma"
    	 attributes = utsContentService.getCodeAttributes(ticket, currentUmlsRelease, "2742-5", "LNC",myPsf);
    	 
    	 for(AttributeDTO attribute:attributes) {
    		 
    		 String atui = attribute.getUi();
    		 String atn = attribute.getName();
    		 String atv = attribute.getValue();
    		 System.out.println(atui+"|"+atn+"|"+atv);
    	 }
    	 pageNum++;
     }while (attributes.size() > 0);
~~~~


#### Sample Output:

~~~~
AT186723331|COMMON_ORDER_RANK|250
AT187103490|COMMON_SI_TEST_RANK|730
AT186491909|COMMON_TEST_RANK|730
AT186681377|EXAMPLE_UCUM_UNITS|U/L
AT186218127|EXAMPLE_UNITS|U/L
AT186618402|LCL|CHEM
AT186660398|LCN|1
AT186765123|LCS|ACTIVE
AT203414718|LCT|MIN
AT206772358|LLR|20150311
AT187250950|LOINC_COMPONENT|Angiotensin converting enzyme
AT186576103|LOINC_PROPERTY|CCnc
AT186555093|LOINC_SCALE_TYP|Qn
AT186744305|LOINC_SYSTEM|Ser/Plas
AT187229875|LOINC_TIME_ASPECT|Pt
AT186597386|LOR|Both
AT206802621|LRN2|ACE; AGT; Angio convert enzy; Angiotensin I converting enzyme; Carboxycathepsin; Catalytic Concentration; Chemistry; Dipeptidylcarboxypeptidase; Enz; Enzymes; Kininase II; PDPA; Peptidase P; Peptidyl dipeptidase A; Pl; Plasma; Plsm; Point in time; Proangiotensin; QNT; Quan; Quant; Quantitative; Random; SerP; SerPl; SerPlas; Serum; Serum or plasma; SR
AT186576104|LUR|Y
~~~~


### getSourceConceptAttributes

**Method Signature:** ```getSourceConceptAttributes(String ticket,String version,String sourceConceptId,String rootSourceAbbreviation,PSF psf)```

#### Sample Input (Java):

~~~~java
int pageNum = 1;
String currentUmlsRelease = utsMetadataService.getCurrentUMLSVersion(ticket);
List<AttributeDTO> attributes = new ArrayList<AttributeDTO>();
     
     do {
    	 myPsf.setPageNum(pageNum);
         //attributes of SNOMED CT concept 449161000124101, "Distention of jugular vein"
    	 attributes = utsContentService.getSourceConceptAttributes(ticket, currentUmlsRelease, "449161000124101", "SNOMEDCT_US",myPsf);
    	 
    	 for(AttributeDTO attribute:attributes) {
    		 
    		 String atui = attribute.getUi();
    		 String atn = attribute.getName();
    		 String atv = attribute.getValue();
    		 System.out.println(atui+"|"+atn+"|"+atv);
    	 }
    	 pageNum++;
     }while (attributes.size() > 0);
~~~~

#### Sample Output:

~~~~text
AT208833331|ACTIVE|1
AT208636611|DEFINITION_STATUS_ID|900000000000073002
AT208664845|EFFECTIVE_TIME|20150901
AT209059262|MODULE_ID|731000124108
~~~~

### getSourceDescriptorAttributes

**Method Signature**: ```getSourceDescriptorAttributes(String ticket,String version,String sourceDescriptorId,String rootSourceAbbreviation,PSF psf)```

#### Sample Input (Java):

~~~~java
int pageNum = 1;
String currentUmlsRelease = utsMetadataService.getCurrentUMLSVersion(ticket);
List<AttributeDTO> attributes = new ArrayList<AttributeDTO>();
     
     do {
    	 myPsf.setPageNum(pageNum);
         //attributes of MSH Descriptor D009369, "Neoplasms"
    	 attributes = utsContentService.getSourceDescriptorAttributes(ticket, currentUmlsRelease, "D009369", "MSH",myPsf);
    	 
    	 for(AttributeDTO attribute:attributes) {
    		 
    		 String atui = attribute.getUi();
    		 String atn = attribute.getName();
    		 String atv = attribute.getValue();
    		 System.out.println(atui+"|"+atn+"|"+atv);
    	 }
    	 pageNum++;
     }while (attributes.size() > 0);
~~~~


#### Sample Output:

~~~~text
AT199367652|AN|general; prefer specifics; policy: see Manual Chapter 24; familial: consider also NEOPLASTIC SYNDROMES, HEREDITARY; metastatic cancer of unknown origin: index under NEOPLASM METASTASIS
AT38096768|AQL|BL BS CF CH CI CL CN CO DH DI DT EC EH EM EN EP ET GE HI IM ME MI MO NU PA PC PP PS PX RA RH RI RT SE SU TH UL UR US VE VI
AT38110444|CX|consider also terms at CANCER, CARCINO-, ONCO-, and TUMOR
AT38119677|DC|1
AT134959705|EC|secondary:Neoplasm Metastasis
...
~~~~

### getAtomAttributes

**Method Signature:** ```getAtomAttributes(String ticket,String version,String atomId,PSF psf)```

#### Sample Input (Java):

~~~~java
int pageNum = 1;
String currentUmlsRelease = utsMetadataService.getCurrentUMLSVersion(ticket);
List<AttributeDTO> attributes = new ArrayList<AttributeDTO>();
//retrieve the highest ranking atom of a SNOMED CT Concept, then retrieve the attributes
AtomDTO atom = utsContentService.getDefaultPreferredAtom(ticket, currentUmlsRelease, "449161000124101", "SNOMEDCT_US");

     
     do {
    	 myPsf.setPageNum(pageNum);
    	 attributes = utsContentService.getAtomAttributes(ticket, currentUmlsRelease, atom.getUi(),myPsf);
    	 
    	 for(AttributeDTO attribute:attributes) {
    		 
    		 String atui = attribute.getUi();
    		 String atn = attribute.getName();
    		 String atv = attribute.getValue();
    		 System.out.println(atui+"|"+atn+"|"+atv);
    	 }
    	 pageNum++;
     }while (attributes.size() > 0);
~~~~


#### Sample Output:

~~~~text
AT208608459|CASE_SIGNIFICANCE_ID|900000000000448009
AT209143461|MODULE_ID|731000124108
AT209115558|TYPE_ID|900000000000013009
~~~~


