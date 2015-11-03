title=Setting up a Metadata object
date=2015-08-21
updated=2015-08-21
type=page
status=published
navorder=1
~~~~~~


The UtsWsMetadataController object allows access to UMLS Metadata. This can be very useful for answering questions such as:

-   What kind of term types, attributes or relationships are associated with a given source?
-   What foreign languages are in this version (or previous version) of the UMLS Metathesaurus?
-   What are all the sources associated with a given UMLS Metathesaurus release?
-   What are the expanded forms (human readable) of term type and attribute abbreviations?

In order to make calls on Metathesaurus Metadata, you must create reference variables, and instantiate them, for the UtsWsMetadataController and UtsWsSecurityController objects somewhere in your code.

~~~~java
private UtsWsMetadataController utsMetadataService;

 try {
 utsMetadataService = (new UtsWsMetadataControllerImplService()).getUtsWsMetadataControllerImplPort();
 }

 catch (Exception e) {
 System.out.println("Error!!!" + e.getMessage());
 }
~~~~ 

All the methods in metadata are called on the utsMetadataService object created in the code sample above.