title=Setting up a Semantic Network object
date=2015-08-21
updated=2015-08-21
type=page
status=unpublished
navorder=1
~~~~~~

The UtsWsSemanticNetworkController object allows you to query the UMLS Semantic Network. You can use this object to get information on:

-   What is the name of a Semantic Type for a given Semantic Term Unique Identifer (TUI)?
-   What are the relations between two Semantic Types?
-   What are all the Semantic Types is a given Semantic Group?

To make query the Semantic Network, create an instance of a UtsWsSemanticNetworkController object, as well as the UtsWsSecurityController object (if not already created).

~~~~
//create the reference variables
 private UtsWsSemanticNetworkController utsSemanticNetworkService;
 private UtsWsSecurityController utsSecurityService;

//instantiate and handshake
 try {
 utsSemanticNetworkService = (new UtsWsSemanticNetworkControllerImplService()).getUtsWsSemanticNetworkControllerImplPort();

 utsSecurityService = (new UtsWsSecurityControllerImplService()).getUtsWsSecurityControllerImplPort();
 }

 catch (Exception e) {
 out.println("Error!!!" + e.getMessage());
 }
//note that PSF objects are not passed as parameters to methods associated with UtsWsSemanticNetworkController objects.
~~~~