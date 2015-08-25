title=Setting up a Content object
date=2015-08-21
updated=2015-08-21
type=page
status=unpublished
navorder=1
~~~~~~

The UtsWsContentController object allows access to the "meat and bones" of the Metathesaurus:

-   Concepts (CUIs), Terms (LUIs), Strings (SUIs), Atoms (AUIs), etc.

One of the features of the new UTS API 2.0 is the ability to view other data "clusters" that come into the Metathesuarus through its source vocabularies:

-   SUIs (string unique identifiers), LUIs (lexical unique identifiers), SCUIs (source-asserted concepts), SDUIs (source-asserted descriptors), SAUIs (source-asserted atoms)

Although the UMLS Metathesaurus is concept (CUI)-oriented database, you can use the UTS API 2.0 to aggregate data at levels other than the CUI from the diverse set of source vocabularies.

For example, you can see all the SCUI-SCUI relations (parent/child or qualifying) between two SNOMED CT® concept identifiers.

In order to make calls on Metathesaurus content, you must create/instantiate reference variables for UtsWsContentController and UtsWsSecurityController objects somewhere in your code:

~~~~
//create the reference variables
 private UtsWsContentController utsContentService;
 private UtsWsSecurityController utsSecurityService;

//instantiate and handshake
 try {
 utsContentService = (new UtsWsContentControllerImplService()).getUtsWsContentControllerImplPort();

 utsSecurityService = (new UtsWsSecurityControllerImplService()).getUtsWsSecurityControllerImplPort();
 }

 catch (Exception e) {
 out.println("Error!!!" + e.getMessage());
 }
~~~~


The sample methods in content would be run on an object similar to the utsContentService object that we just created.