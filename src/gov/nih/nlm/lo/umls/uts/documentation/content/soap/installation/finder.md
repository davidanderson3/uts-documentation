title=Setting up a Finder object
date=2015-08-21
updated=2015-08-21
type=page
status=unpublished
navorder=1
~~~~~~


The Finder Service allows you to retrieve identifiers, for words or codes, and pass these retrieved identifiers to other methods to retrieve more granular data (especially using the methods associated with the UtsWsContentController object). You can perform searches such as:

-   starting with a search term, retrieve CUIs, SDUIs, SCUIs, and atoms
-   starting with a code, retrieve CUIs, SDUIs, SCUIs and atoms

To use the finder service, create an instance of a UtsWsFinderController object, as well as the UtsWsSecurityController object (if not already created).

~~~~
//create the reference variables
 private UtsWsFinderController utsFinderService;
 private UtsWsSecurityController utsSecurityService;

//instantiate and handshake
 try {
 utsFinderService = (new UtsWsFinderControllerImplService()).getUtsWsFinderControllerImplPort();

 utsSecurityService = (new UtsWsSecurityControllerImplService()).getUtsWsSecurityControllerImplPort();
 }

 catch (Exception e) {
 out.println("Error!!!" + e.getMessage());
 }
~~~~
