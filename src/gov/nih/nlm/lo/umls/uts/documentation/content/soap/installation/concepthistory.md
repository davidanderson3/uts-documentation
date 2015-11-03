title=Setting up a Concept History object
date=2015-08-21
updated=2015-08-21
type=page
status=published
navorder=1
~~~~~~

The UtsWsHistoryController object allows you to query UMLS Metathesaurus history. You can use methods associated with this object to track things such as:

-   Has an atom moved from one concept to another in the UMLS at some point in time?
-   Has a given UMLS concept been bequeathed to another, and what is the
    new Concept?
-   When did a given UMLS concept die?

To query UMLS Metathesaurus history, create an instance of a UtsWsHistoryController object, as well as the UtsWsSecurityController object (if not already created).

~~~~
//create the reference variables
 private UtsWsHistoryController utsHistoryService;

 try {
 utsHistoryService = (new UtsWsHistoryControllerImplService()).getUtsWsHistoryControllerImplPort();

 utsSecurityService = (new UtsWsSecurityControllerImplService()).getUtsWsSecurityControllerImplPort();
 }

 catch (Exception e) {
 out.println("Error!!!" + e.getMessage());
 }
~~~~
