title=Retrieving UMLS Metadata
date=2015-08-21
updated=2015-08-21
type=page
status=published
navorder=4
~~~~~~

Interface | Method | Use Case | Object or Data type Returned 
-- | -- | -- | --
**UtsWsMetadataController**||||
 |[getCurrentUMLSVersion](#getcurrentumlsversion)|Retrieves the current version of UMLS|String
 |[getAllUMLSVersions](#getallumlsversions)|Retrieves a list of all UMLS versions available in the UMLS Terminology Services web service|String[]
 |[getUpdatedSourcesByVersion](#getupdatedsourcesbyversion)|Retrieve a list of vocabularies that were updated for a known UMLS version|ArrayList\<SourceDTO\>
 |[getAllSources](#getallsources)|Retrieve a list of vocabularies that are included in a known UMLS version|ArrayList\<SourceDTO\>


**Each of these examples requires an instance of the [UtsWsMetadataController](/soap/installation/content.html) and [UtsWsSecurityController](/soap/installation/authentication.html) interfaces**.

### getCurrentUMLSVersion

**Method Signature**: ```getCurrentUMLSVersion(String ticket)```

#### Sample Input

~~~~java
String currentUmlsRelease = utsMetadataService.getCurrentUMLSVersion(ticket);
~~~~

#### Sample Output

~~~~text
2015AB
~~~~

### getAllUMLSVersions

**Method Signature**: ```getAllUMLSVersions(String ticket)```

#### Sample Input

~~~~java
String[] umlsReleases = utsMetadataService.getAllUMLSVersions(ticket);
~~~~

#### Sample Output

~~~~text
2015AB
2015AA
2014AB
...
~~~~

### getUpdatedSourcesByVersion

**Method Signature**: ```getUpdatedSourcesByVersion(String ticket,String version)```


#### Sample Input

~~~~java
//find updated sources in the latest UMLS version
String currentUmlsRelease = utsMetadataService.getCurrentUMLSVersion(ticket);
List<SourceDTO> sources = utsMetadataService.getUpdatedSourcesByVersion(ticket, currentUmlsRelease);

    for (SourceDTO source:sources) {
			
	System.out.println(source.getRootSource()
			  .getPreferredName());
    }

~~~~

#### Sample Output

~~~~text
Anatomical Therapeutic Chemical Classification System, ATC_2015_15_09_08
Code on Dental Procedures and Nomenclature, 2016
Vaccines Administered, 2015_07_27
Gene Ontology, 2015_04_04
Gold Standard Drug Database, 2015_08_07
...
~~~~

### getAllSources

**Method Signature**: ```getAllSources(String ticket,String version)```


#### Sample Input

~~~~java
String currentUmlsRelease = utsMetadataService.getCurrentUMLSVersion(ticket);
List<SourceDTO> sources = utsMetadataService.getAllSources(ticket, currentUmlsRelease);

    for (SourceDTO source:sources) {
			
	System.out.println(source.getRootSource()
			  .getPreferredName());
    }

~~~~

#### Sample Output

~~~~text
AI/RHEUM, 1993
Alternative Billing Concepts, 2009
Alcohol and Other Drug Thesaurus, 2000
Authorized Osteopathic Thesaurus, 2003
Anatomical Therapeutic Chemical Classification System, ATC_2015_15_09_08
Beth Israel Vocabulary, 1.0
Clinical Care Classification, 2_5
Canonical Clinical Problem Statement System, 1999
Clinical Classifications Software, 2005
Code on Dental Procedures and Nomenclature, 2016
...
~~~~

