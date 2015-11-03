title=The UtsWsContentController interface
date=2015-08-21
updated=2015-08-21
type=page
status=published
navorder=1
~~~~~~

The UtsWsContentController interface provides methods to retrieve UMLS information such as concepts, atoms, source-asserted data (codes, concepts, descriptors), terms, relationships, etc.
You should use the methods of this interface when you have a known identifer and you want additional information about it.

~~~~java
//create the reference variables
 private UtsWsContentController utsContentService;

//instantiate and handshake
 try {
 utsContentService = (new UtsWsContentControllerImplService()).getUtsWsContentControllerImplPort();
 }

 catch (Exception e) {
 out.println("Error!!!" + e.getMessage());
 }
~~~~