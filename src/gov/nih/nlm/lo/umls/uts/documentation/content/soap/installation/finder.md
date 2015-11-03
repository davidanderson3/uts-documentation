title=Setting up a Finder object
date=2015-08-21
updated=2015-08-21
type=page
status=published
navorder=1
~~~~~~

The Finder service provides methods to fetch CUIs, codes, as well as source-asserted concepts/descriptors when searching by term. 
To use the finder service, create an instance of a UtsWsFinderController object.  

~~~~java
 private UtsWsFinderController utsFinderService;

//instantiate and handshake
 try {
 utsFinderService = (new UtsWsFinderControllerImplService()).getUtsWsFinderControllerImplPort();
 }

 catch (Exception e) {
 out.println("Error!!!" + e.getMessage());
 }
~~~~
