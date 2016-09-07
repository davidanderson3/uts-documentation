title=Searching the UMLS with the SOAP API
date=2015-08-14
updated=2015-08-14
type=page
status=published
navorder=2
~~~~~~


Interface|Method|Object or Data type Returned |Use Cases
:-- | :-- | :-- | --:
**UtsWsFinderController**||||
 |**[findConcepts](#findconcepts)**|ArrayList\<UiLabel\>||
 |||Accepts a term and returns UMLS CUIs|
 |||Accepts a known source-asserted identifier and returns UMLS CUIs|
 |||Extracts terms according to term type|
 |**[findAtoms](#findatoms)**|ArrayList\<UiLabel\>||
 |||Accepts a term and returns UMLS atoms (AUIs)|
 |**[findSourceConcepts](#findsourceconcepts)**|ArrayList\<UiLabelRootSource\>||
 |||Accepts a term and returns source-asserted concepts|
 |**[findSourceDescriptors](#findsourcedescriptors)**|ArrayList\<UiLabelRootSource\>||
 |||Accepts a term and returns a source-asserted descriptor|
 |**[findCodes](#findcodes)**|ArrayList\<UiLabelRootSource\>||
 |||Takes a term and returns a source-asserted code|

**Each of these examples below requires an instance of the [UtsWsFinderController](/soap/installation/interface-setup.html#utswsfindercontroller), [UtsWsMetadataController](/soap/installation/interface-setup.html#utswsmetadatacontroller) and [UtsWsSecurityController](/soap/installation/interface-setup.html#utswssecuritycontroller) interfaces**.


### findConcepts


**Method Signature:** ```findConcepts(String ticket,String version,String target,String str, String searchType,PSF psf)```

#### Additional parameters and values

Parameter name|Definition|Valid values
-- | --
target|Specifies the input type of your search, which is usually either a human-readable string or an identifer from a vocabulary.|aui,atom (used for searching by term), code, concept, sourceConcept, sourceDescriptor,tty
searchType|Type of search you're performing|exact (use this when passing codes to the finder service), approximate,leftTruncation,rightTruncation,words,normalizedWords

#### Sample Input (Java):

~~~~java
Psf myPsf = new Psf();
int pageNum = 1;
//exclude suppressible + obsolete term matches
myPsf.setIncludeObsolete(false);
myPsf.setIncludeSuppressible(false);
List<UiLabel> results = new ArrayList<UiLabel>();
String currentUmlsRelease = utsMetadataService.getCurrentUMLSVersion(ticket);
        
    do {
        //you'll need a new service ticket to retrieve each page of your call.  Here is an example.
	String ticket = utsSecurityService.getProxyTicket(tgt,"http://umlsks.nlm.nih.gov");
	myPsf.setPageNum(pageNum);
	results = utsFinderService.findConcepts(ticket, currentUmlsRelease, "atom", "aglossia", "words", myPsf);
		    
        for (UiLabel result:results) {
			
	    String ui = result.getUi();
	    String name = result.getLabel();

	}
        pageNum++;
		
    } while (results.size() > 0);
~~~~

#### Sample Output:

~~~~text
ui: C0158663
name: Tongue absent
ui: C1863203
name: Hypoglossia-Hypodactylia
ui: C0595985
name: Hanhart's syndrome
~~~~

### findAtoms

**Method Signature:** ```findAtoms(String ticket,String version,String target,String str,String searchType,PSF psf)```

Parameter name|Definition|Valid values
-- | --
target|Specifies the data type provided in your 'str' parameter|atom (used for searching by term), code, concept, sourceConcept, sourceDescriptor
searchType|Type of search you're performing|exact (use this when passing codes to the finder service), approximate,leftTruncation,rightTruncation,words,normalizedWords


#### Sample Input (Java):
~~~~java
Psf myPsf = new Psf();
int pageNum = 1;
//exclude suppressible + obsolete term matches
myPsf.setIncludeObsolete(false);
myPsf.setIncludeSuppressible(false);
//only include atoms from US Edition of SNOMED CT
myPsf.getIncludedSources().add("SNOMEDCT_US");
List<UiLabel> results = new ArrayList<UiLabel>();
String currentUmlsRelease = utsMetadataService.getCurrentUMLSVersion(ticket);

        
    do {
        //you'll need a new service ticket to retrieve each page of your call.  Here is an example.
	String ticket = utsSecurityService.getProxyTicket(tgt,"http://umlsks.nlm.nih.gov");
	myPsf.setPageNum(pageNum);
	results = utsFinderService.findAtoms(ticket, currentUmlsRelease, "atom", "aglossia", "words", myPsf);
		    
        for (UiLabel result:results) {
			
	    String ui = result.getUi();
	    String name = result.getLabel();

	}
        pageNum++;
		
    } while (results.size() > 0);
~~~~


#### Sample Output:

~~~~text
ui: A2953834
name: Aglossia-adactyly syndrome
ui: A3527513
name: Aglossia-adactyly syndrome (disorder)
~~~~


### findCodes

**Method Signature:** ```findCodes(String ticket,String version,String target,String str,String searchType,PSF psf)```

Parameter name|Definition|Valid values
-- | --
target|Specifies the data type provided in your 'str' parameter|atom (used for searching by term), aui, sourceDescriptor, sourceConcept
searchType|Type of search you're performing|exact, approximate, leftTruncation, rightTruncation, words, normalizedWords


#### Sample Input (Java):
~~~~java
List<UiLabelRootSource> results = new ArrayList<UiLabelRootSource>();
Psf myPsf = new Psf();
myPsf.setIncludeObsolete(false);
myPsf.setIncludeSuppressible(false);
int pageNum = 1;
String currentUmlsRelease = utsMetadataService.getCurrentUMLSVersion(ticket);

    
    do {
	
        //you'll need a new service ticket to retrieve each page of your call.  Here is an example.
	String ticket = utsSecurityService.getProxyTicket(tgt,"http://umlsks.nlm.nih.gov");
	myPsf.setPageNum(pageNum);
	results = utsFinderService.findCodes(ticket, currentUmlsRelease, "atom", "aglossia", "words", myPsf);
		
	for(UiLabelRootSource result:results) {
		
	    String ui = result.getUi();
	    String rsab = result.getRootSource();
	    String name = result.getLabel();
         
	    }
	pageNum++;
	
	} while (results.size() > 0);
~~~~


#### Sample Output:

~~~~text
ui: 10001501
Source:MDR
name: Aglossia
----
ui: PA11.
Source:RCD
name: Aglossia
----
ui: D4-52002
Source:SNMI
name: Aglossia
----
ui: Q38.3
Source:ICD10CM
name: Other congenital malformations of tongue
----
ui: MTHU037232
Source:OMIM
name: Aglossia
----
ui: 750.11
Source:ICD9CM
name: Aglossia
----
ui: MTHU004751
Source:ICPC2ICD10ENG
name: aglossia
----
ui: 99025
Source:MEDCIN
name: aglossia
----
ui: C566308
Source:MSH
name: Hypoglossia-Hypodactylia
----
ui: 103300
Source:OMIM
name: HYPOGLOSSIA-HYPODACTYLIA
----
ui: MTHU004752
Source:ICPC2ICD10ENG
name: aglossia-adactylia syndrome
----
ui: D-6036
Source:SNM
name: Aglossia-adactylia syndrome
----
ui: D4-01305
Source:SNMI
name: Oromandibular-limb hypogenesis spectrum
----
ui: 205817005
Source:SNOMEDCT_US
name: Aglossia-adactyly syndrome
----

~~~~

### findSourceConcepts


**Method Signature:** ```findSourceConcepts(String ticket,String version,String target,String str,String searchType,PSF psf)```

Parameter name|Definition|Valid values
-- | --
target|Specifies the data type provided in your 'str' parameter|atom (used for searching by term), aui, code, sourceDescriptor
searchType|Type of search you're performing|exact, approximate, leftTruncation, rightTruncation, words, normalizedWords


#### Sample Input (Java):
~~~~java
List<UiLabelRootSource> results = new ArrayList<UiLabelRootSource>();
Psf myPsf = new Psf();
myPsf.setIncludeObsolete(false);
myPsf.setIncludeSuppressible(false);
int pageNum = 1;
String currentUmlsRelease = utsMetadataService.getCurrentUMLSVersion(ticket);

    
    do {
	
       //you'll need a new service ticket to retrieve each page of your call.  Here is an example.
	String ticket = utsSecurityService.getProxyTicket(tgt,"http://umlsks.nlm.nih.gov");
	myPsf.setPageNum(pageNum);
	results = utsFinderService.findSourceConcepts(ticket, currentUmlsRelease, "atom", "aglossia", "words", myPsf);
		
	for(UiLabelRootSource result:results) {
		
	    String ui = result.getUi();
	    String rsab = result.getRootSource();
	    String name = result.getLabel();
         
	    }
	pageNum++;
	
	} while (results.size() > 0);
~~~~


#### Sample Output:

~~~~text
ui: 99025
Source:MEDCIN
name: aglossia
----
ui: M0566608
Source:MSH
name: Hypoglossia-Hypodactylia
----
ui: 205817005
Source:SNOMEDCT_US
name: Aglossia-adactyly syndrome
----
~~~~

### findSourceDescriptors


**Method Signature:** ```findSourceDescriptors(String ticket,String version,String target,String str,String searchType,PSF psf)```

Parameter name|Definition|Valid values
-- | --
target|Specifies the data type provided in your 'str' parameter|atom (used for searching by term), aui, code, sourceConcept
searchType|Type of search you're performing|exact, approximate, leftTruncation, rightTruncation, words, normalizedWords


#### Sample Input (Java):
~~~~java
List<UiLabelRootSource> results = new ArrayList<UiLabelRootSource>();
Psf myPsf = new Psf();
myPsf.setIncludeObsolete(false);
myPsf.setIncludeSuppressible(false);
int pageNum = 1;
String currentUmlsRelease = utsMetadataService.getCurrentUMLSVersion(ticket);

    
    do {
	
        //you'll need a new service ticket for each page of your call.  Here is an example.
	String ticket = utsSecurityService.getProxyTicket(tgt,"http://umlsks.nlm.nih.gov");
	myPsf.setPageNum(pageNum);
	results = utsFinderService.findSourceDescriptors(ticket, currentUmlsRelease, "atom", "aglossia", "words", myPsf);
		
	for(UiLabelRootSource result:results) {
		
	    String ui = result.getUi();
	    String rsab = result.getRootSource();
	    String name = result.getLabel();
         
	    }
	pageNum++;
	
	} while (results.size() > 0);
~~~~


#### Sample Output:

~~~~text
ui: 10001501
Source:MDR
name: Aglossia
----
ui: Q38.3
Source:ICD10CM
name: Other congenital malformations of tongue
----
ui: MTHU037232
Source:OMIM
name: Aglossia
----
ui: 750.11
Source:ICD9CM
name: Aglossia
----
ui: C566308
Source:MSH
name: Hypoglossia-Hypodactylia
----
ui: 103300
Source:OMIM
name: HYPOGLOSSIA-HYPODACTYLIA
----
~~~~

