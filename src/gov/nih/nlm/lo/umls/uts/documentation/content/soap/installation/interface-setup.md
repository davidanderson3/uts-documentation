title=Interface Setup
date=2015-12-11
updated=2015-12-11
type=page
status=published
navorder=1
~~~~~~

There are 6 interfaces available in the UMLS SOAP API.  You may use as many or as few as needed in your application, although you will always need an instanace
of the UtsWsSecurityController interface to handle retrieving service tickets for each call to the API.

Interface | Use Cases | Guidance
-- | -- | --
[UtsWsSecurityController](#utswssecuritycontroller) | Retrieve Ticket Granting Tickets and Service Tickets | Retrieve **one** ticket granting ticket when starting your application. Use that same ticket granting ticket to retrieve single-use service tickets for each call to the API.
[UtsWsContentController](#utswscontentcontroller) | Retrieve information about known identifiers such as UMLS Concepts, Atoms, Relationships, Subsets, and Attributes | |
[UtsWsFinderController](#utswsfindercontroller) | Search for UMLS Concepts or codes using a term. | |
[UtsWsMetadataController](#utswsmetadatacontroller) | Retrieve information about UMLS term types and source vocabularies | |
[UtsWsHistoryController](#utswshistorycontroller) | Track merges, deletions, and bequeathals of UMLS Concepts | | 
[UtsWsSemanticNetworkController](#utswssemanticnetworkcontroller) | Retrieve information about semantic types and semantic groups | |


#### UtsWsSecurityController

Here is an example of how to set up an instance of the UtsWsSecurityController interface.

~~~~java
private UtsWsSecurityController utsSecurityService;

try {
 utsSecurityService = (new UtsWsSecurityControllerImplService()).getUtsWsSecurityControllerImplPort();
}

catch (Exception e) {
 out.println("Error!!!" + e.getMessage());
}
~~~~

#### UtsWsContentController

Here is an example of how to set up an instance of the UtsWsContentController interface.

~~~~java
private UtsWsContentController utsContentService;

try {
 utsContentService = (new UtsWsContentControllerImplService()).getUtsWsContentControllerImplPort();
}

catch (Exception e) {
 out.println("Error!!!" + e.getMessage());
}
~~~~

#### UtsWsFinderController

Here is an example of how to set up an instance of the UtsWsFinderController interface.

~~~~java
private UtsWsFinderController utsFinderService;

try {
 utsFinderService = (new UtsWsFinderControllerImplService()).getUtsWsFinderControllerImplPort();
}

catch (Exception e) {
 out.println("Error!!!" + e.getMessage());
}
~~~~

#### UtsWsMetadataController

Here is an example of how to set up an instance of the UtsWsMetadataController interface.

~~~~java
private UtsWsMetadataController utsMetadataService;

 try {
 utsMetadataService = (new UtsWsMetadataControllerImplService()).getUtsWsMetadataControllerImplPort();
 }

 catch (Exception e) {
 System.out.println("Error!!!" + e.getMessage());
 }
~~~~

#### UtsWsSemanticNetworkController
Here is an example of how to set up an instance of the UtsWsSemanticNetworkController interface.


~~~~java
 private UtsWsSemanticNetworkController utsSemanticNetworkService;

try {
 utsSemanticNetworkService = (new UtsWsSemanticNetworkControllerImplService()).getUtsWsSemanticNetworkControllerImplPort();
}

 catch (Exception e) {
 out.println("Error!!!" + e.getMessage());
 }
~~~~

#### UtsWsHistoryController
Here is an example of how to set up an instance of the UtsWsHistoryController interface.

~~~~java
 private UtsWsSemanticNetworkController utsSemanticNetworkService;

 try {
 utsHistoryService = (new UtsWsHistoryControllerImplService()).getUtsWsHistoryControllerImplPort();
 }

 catch (Exception e) {
 out.println("Error!!!" + e.getMessage());
 }
~~~~

