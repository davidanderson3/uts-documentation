title=UMLS SOAP API Home Page
date=2015-08-18
updated=2015-12-17
type=page
status=published
navorder=1
~~~~~~

### Use cases and methods

**Note:** Most of the sample code displayed in the SOAP API is in Java.

Section (Interface)|Use Case
--- | ---:
**Installation**||
[Installation using Maven](/soap/installation/maven-installation.html)|Install the API
[Set up instances of the UMLS SOAP API interfaces](/soap/installation/interface-setup.html)|Install the API
**Authentication** ([UtsWsSecurityController](/soap/installation/interface-setup.html#utswssecuritycontroller))||
[Request authentication tickets](/soap/installation/authentication.html)|Request ticket granting tickets and single-use service tickets
**PSF (Paging, sorting, and filtering)**||
[Using the PSF object](/soap/paging-sorting-filtering/index.html)|Page and Filter Results
**Searching the UMLS** ([UtsWsFinderController](/soap/installation/interface-setup.html#utswsfindercontroller))||
[Using the Finder Service](/soap/search/index.html)|Find CUIs, codes, source-asserted concepts/descriptors from human readable terms.
**Retrieving UMLS Content** ([UtsWsContentController](/soap/installation/interface-setup.html#utswscontentcontroller))||
[Concept](/soap/concept/index.html)|Retrieve UMLS Concept Information 
[Atoms](/soap/atoms/index.html)|Retrieve UMLS Atoms 
[Definitions](/soap/definitions/index.html)|Retrieve UMLS Definitions  
[Atom Cluster](/soap/atomcluster/index.html)|Retrieve source-asserted concepts,descriptors, and codes
[Content View](/soap/contentview/index.html)|Retrieve UMLS content views
[Subset](/soap/subset/index.html)|Retrieve UMLS subsets
[Relationships](/soap/relationships/index.html)|Retrieve UMLS relationships
[Attributes](/soap/attributes/index.html)|Retrieve CUI and code attributes
**Retrieving UMLS Metadata** ([UtsWsMetadataController](/soap/installation/interface-setup.html#utswsmetadatacontroller))||
[UMLS Metadata](/soap/umlsmetadata/index.html)|Retrieve UMLS Metadata such as updated vocabluaries within a UMLS version


