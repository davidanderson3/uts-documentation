title=Setting up a Semantic Network object
date=2015-08-21
updated=2015-08-21
type=page
status=published
navorder=1
~~~~~~

The UtsWsSemanticNetworkController object allows you to query the UMLS Semantic Network.

~~~~java
 private UtsWsSemanticNetworkController utsSemanticNetworkService;

 try {
 utsSemanticNetworkService = (new UtsWsSemanticNetworkControllerImplService()).getUtsWsSemanticNetworkControllerImplPort();
 }

 catch (Exception e) {
 out.println("Error!!!" + e.getMessage());
 }
~~~~