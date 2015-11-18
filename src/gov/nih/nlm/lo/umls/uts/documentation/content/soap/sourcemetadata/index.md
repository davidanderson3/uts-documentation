title=Source Metadata
date=2015-08-21
updated=2015-08-21
type=page
status=published
navorder=4
~~~~~~


**Method: **getRootSource(String ticket,String version,String rootSourceAbbreviation)

**Returns:**RootSourceDTO

**Use Case:** This method returns details of a given Metathesaurus root source abbreviation (RSAB) including content contact, license contact, language, expanded form, preferred name, abbreviation, short name, context type, family, and restriction level. The example below retrieves the expanded form and restriction level for SNOMEDCT.

#### Sample Input (Java):

~~~~
RootSourceDTO myRootSource = utsMetadataService.getRootSource(ticket, "2011AB", "SNOMEDCT");
 String expandedForm = myRootSource.getExpandedForm();
 int restrictionLevel = myRootSource.getRestrictionLevel();
~~~~

#### Sample Input (C#):

~~~~
Metadata.rootSourceDTO myRootSource =utsMetadataService.getRootSource(ticket, "2011AB", "SNOMEDCT");
 string expandedForm = myRootSource.expandedForm;
 int restrictionLevel = myRootSource.restrictionLevel;
~~~~

#### Sample Output:

~~~~  
//print out the results
   Expanded Form: SNOMED Clinical Terms, 2011_07_31\
   Restriction Level: 9\
~~~~
>


**Method: **getAllRootSources(String ticket,String version)

**Returns:**ArrayList< RootSourceDTO>

**Use Case:** This method returns an array list of all sources in the UMLS for a given release. In the example below, we show only the first and last members (rather than all 161 members) of the array list returned for the sources in the 2011AB UMLS.


#### Sample Input (Java):

~~~~
List<RootSourceDTO> myRootSources = new ArrayList<RootSourceDTO>();
 myRootSources = utsMetadataService.getAllRootSources(ticket,"2011AB");
 for (int i = 0; i < myRootSources.size(); i++) {
 RootSourceDTO myRootSourcesDTO = myRootSources.get(i);
 String PreferredName = myRootSourcesDTO.getPreferredName();
 String Abbreviation = myRootSourcesDTO.getAbbreviation();
 int RestrictionLevel = myRootSourcesDTO.getRestrictionLevel();
 }
~~~~

#### Sample Input (C#):

~~~~
Metadata.rootSourceDTO[] myRootSources =utsMetadataService.getAllRootSources(ticket, "2011AB");
 for (int i = 0; i < myRootSources.Length; i++){
 Metadata.rootSourceDTO myRootSourcesDTO = myRootSources[i];
 string PreferredName = myRootSourcesDTO.preferredName;
 string Abbreviation = myRootSourcesDTO.abbreviation;
 int RestrictionLevel = myRootSourcesDTO.restrictionLevel;
 }
~~~~

#### Sample Output:

~~~~
   Preferred Name: AI/RHEUM, 1993
   Abbreviation: AIR
   Restriction Level: 0
  
   Preferred Name: WHOART, Spanish Translation, 1997
   Abbreviation: WHOSPA
   Restriction Level: 2
~~~~
>


**Method: **getAllRootSourceFamilies(String ticket,String version)

**Returns:** ArrayList< RootSourceDTO>

**Use Case:** This method retrieves all the source families present as per a given UMLS release. You can also retrieve the source restriction level and the full(expanded) form of the source name.


#### Sample Input (Java):

~~~~
myArrSrc = utsMetadataService.getUpdatedSourcesByVersion(ticket, umlsRelease);
 for (int i = 0; i < myArrSrc.size(); i++) {
 RootSourceDTO myArrSrcDTO = myArrSrc.get(i);
 String abbreviation = myArrSrcDTO.getAbbreviation();
 int restrictionLevel = myArrSrcDTO.getRestrictionLevel();
 String family = myArrSrcDTO.getFamily();
 String expForm = myArrSrcDTO.getExpandedForm();
 }
~~~~

#### Sample Output:

Abbreviation |   Restriction Level |  Family   |  Expanded Form  
--- | --- | --- | ---
AIR       |      0       |            AIR      |       AI/RHEUM, 1993 
ALT    |         3       |            ALT      |       Alternative Billing Concepts, 2009   
AOD        |     0        |           AOD      |       Alcohol and Other Drug Thesaurus, 2000             
AOT      |       0        |           AOT     |        Authorized Osteopathic Thesaurus, 2003                     
BI        |      2        |           BI       |       Beth Israel Vocabulary, 1.0                               
CCC       |      1        |           CCC      |       Clinical Care Classification, 2_5                                  
>

**Method: **getRootSourcesByFamily(String ticket,String version,String family)

**Returns:**ArrayList< RootSourceDTO>

**Use Case:** This method retrieves all the root sources for a given source family. You can also retrieve the source restriction level and the full(expanded) form of the source name.

#### Sample Input (Java):

~~~~
myArrSrc = utsMetadataService.getRootSourcesByFamily(ticket,umlsRelease, "SNOMEDCT");
 for (int i = 0; i < myArrSrc.size(); i++) {
 RootSourceDTO myArrSrcDTO = myArrSrc.get(i);
 String abbreviation = myArrSrcDTO.getAbbreviation();
 int restrictionLevel = myArrSrcDTO.getRestrictionLevel();
 String family = myArrSrcDTO.getFamily();
 String expForm = myArrSrcDTO.getExpandedForm();
 }
~~~~

#### Sample Output:

 Abbreviation  | Restriction Level |  Family  |   Expanded Form 
 --- | --- | --- | ---
SCTSPA   |    9   |   SNOMEDCT |  SNOMED Clinical Terms, Spanish Language Edition, 2012_10_31   
SCTUSX |  0  | SNOMEDCT  | US Extension to SNOMED CT(R), 2013_03_01                                                       |
SNOMEDCT |   9    |  SNOMEDCT |  SNOMED Clinical Terms, 2013_01_31            
>

**Method: **getRootSourcesByRestrictionLevel(String ticket,String version,int restrictionLevel)

**Returns:** ArrayList< RootSourceDTO>

**Use Case:** This method retrieves all the root sources for a particular restriction level.

#### Sample Input (Java):

~~~~
myArrSrc = utsMetadataService.getRootSourcesByRestrictionLevel(ticket, umlsRelease, "0");
 for (int i = 0; i < myArrSrc.size(); i++) {
 RootSourceDTO myArrSrcDTO = myArrSrc.get(i);
 String abbreviation = myArrSrcDTO.getAbbreviation();
 int restrictionLevel = myArrSrcDTO.getRestrictionLevel();
 String family = myArrSrcDTO.getFamily();
 String expForm = myArrSrcDTO.getExpandedForm();
 }
~~~~

#### Sample Output:

Abbreviation  | Restriction Level  | Family   |     Expanded Form 
--- | --- | --- | ---
AIR     |       0        |           AIR      |     AI/RHEUM, 1993 
 AOD    |        0         |          AOD      |     Alcohol and Other Drug Thesaurus, 2000                                                        |
 AOT     |       0        |           AOT      |     Authorized Osteopathic Thesaurus, 2003                                                        |
CCS      |      0         |          CCS      |     Clinical Classifications Software, 2005                                                       |
CHV       |     0          |         CHV      |     Consumer Health Vocabulary, 2011_02                                       
COSTAR    |     0         |          COSTAR   |     COSTAR, 1989-1995     |
 CSP       |     0        |           CSP     |      CRISP Thesaurus, 2006 |
>


**Method: **getVersionedSources(String ticket,String version,String rootSourceAbbreviation)

**Returns:**ArrayList< SourceDTO>

**Use Case:** This method returns all versions of a given Root Source in the Metathesaurus.

**Note:** While rare, there are certain sources that have more than one version in the Metathesaurus. This happens occasionally when mappings exist between 2 versions of a source. If the mapping is not updated along with the other source content, we maintain the metadata for that older source in the Metathesaurus.


#### Sample Input (Java):

~~~~
myArrSrc = utsMetadataService.getVersionedSources(ticket, umlsRelease,"ICD9CM");
 for (int i = 0; i < myArrSrc.size(); i++) {
 SourceDTO myArrSrcDTO = myArrSrc.get(i);
 String abbreviation = myArrSrcDTO.getAbbreviation();
 String rtSrcAbbreviation =myArrSrcDTO.getRootSource().getAbbreviation();
 String version = myArrSrcDTO.getVersion();
 }
~~~~

#### Sample Input (C#):

~~~~
Metadata.sourceDTO[] myArraySource =utsMetadataService.getVersionedSources(singleUseTicket, "2012AB","ICD9CM");
 for (int i = 0; i < myArraySource.Length; i++){
 Metadata.sourceDTO myArraySourceDTO = myArraySource[i];
 string abbreviation = myArraySourceDTO.abbreviation;
 string rootSource = myArraySourceDTO.rootSource.abbreviation;
 string version = myArraySourceDTO.version;
 }
~~~~

#### Sample Output:

~~~~
  Abbreviation: ICD9CM_2011
   RootSource Abbreviation: ICD9CM
   Version: 2011
   Abbreviation: ICD9CM_2005
   RootSource Abbreviation: ICD9CM
   Version: 2005
   Abbreviation: ICD9CM_1998
   RootSource Abbreviation: ICD9CM
   Version: 1998
   Abbreviation: ICD9CM_2012
   RootSource Abbreviation: ICD9CM
   Version: 2012
~~~~
>

**Method: **getCurrentVersionSource(String ticket,String version,String rootSourceAbbreviation)

**Returns:**SourceDTO

**Use Case:** Given a UMLS release and root source abbreviation (RSAB), this call returns details of the version of the root source contained by the given UMLS release, as well as the original version that appeared in the UMLS.


#### Sample Input (Java):

~~~~
mySrcDTO = utsMetadataService.getCurrentVersionSource(ticket,umlsRelease, "LNC");
 String abbreviation = mySrcDTO.getAbbreviation();
 String version = mySrcDTO.getVersion();
 String rtSrcAbbreviation = mySrcDTO.getRootSource().getAbbreviation();
~~~~

#### Sample Input (C#):

~~~~
Metadata.sourceDTO mySourceDTO =utsMetadataService.getCurrentVersionSource(singleUseTicket, "2012AB","LNC");
 string abbreviation = mySourceDTO.abbreviation;
 string rootSource = mySourceDTO.rootSource.abbreviation;
 string version = mySourceDTO.version;
~~~~

#### Sample Output:

~~~~
  Abbreviation: LNC215
   Version: 215
   RootSource Abbreviation: LNC
~~~~
>


**Method: **getUpdatedSourcesByVersion(String ticket,String version)

**Returns:**ArrayList< SourceDTO>

**Use Case:** This method retrieves all the sources that have been updated in a given UMLS release.

#### Sample Input (Java):

~~~~
myArrSrc = utsMetadataService.getUpdatedSourcesByVersion(ticket,umlsRelease);
 for (int i = 0; i < myArrSrc.size(); i++) {
 SourceDTO myArrSrcDTO = myArrSrc.get(i);
 String abbreviation = myArrSrcDTO.getAbbreviation();
 String rtSrcAbbr = myArrSrcDTO.getRootSource().getAbbreviation();
 String rtSrcExpForm = myArrSrcDTO.getRootSource().getExpandedForm();
 String version = myArrSrcDTO.getVersion();
 }
~~~~

#### Sample Output:

Abbreviation |   RootSource Abbreviation |  RootSource ExpandedForm  | Version     
--- | --- | --- | ---
CPT2013      |    CPT  |  Current Procedural Terminology, 2013| 2013  
GS_2013_02_01   |  GS      | Gold Standard Drug Database, 2013_02_01 2013_02_01
HCDT2013 |  HCDT     | Current Dental Terminology (CDT), 2013 | 2013          |
HCPCS2013    |  HCPCS |  Healthcare Common Procedure Coding System, 2013  | 2013    
 HCPT2013  | HCPT  |HCPCS Version of Current Procedural Terminology (CPT), 2013  |2013
ICD10CM_2013  | ICD10CM    | International Classification of Diseases, 10th Edition, Clinical Modification, 2013 |  2013 
 ICD10PCS_2013|  ICD10PCS  |  ICD-10-PCS, 2013 | 2013     
 
 >
 
 
**Method: **getSource(String ticket,String version,String versionedSourceAbbreviation)

**Returns:**SourceDTO

**Use Case:** Given a UMLS release and versioned source abbreviation (VSAB), this call returns details of the version of the root source.


#### Sample Input (Java):

~~~~
mySrcDTO = utsMetadataService.getSource(ticket, umlsRelease, "ICD9CM_1998");
 String abbreviation = mySrcDTO.getAbbreviation();
 String version = mySrcDTO.getVersion();
 String rtSrcAbbreviation = mySrcDTO.getRootSource().getAbbreviation();
~~~~

#### Sample Input (C#):

~~~~
Metadata.sourceDTO mySourceDTO =utsMetadataService.getSource(singleUseTicket, "2012AA","ICD9CM_1998");
 string abbreviation = mySourceDTO.abbreviation;
 string rootSource = mySourceDTO.rootSource.abbreviation;
 string version = mySourceDTO.version;
~~~~

#### Sample Output:

~~~~
  Abbreviation: ICD9CM_1998
   Version: 1998
   RootSource Abbreviation: ICD9CM
~~~~
>

**Method: **getAllSources(String ticket,String version)

**Returns:**ArrayList< SourceDTO>

**Use Case:** Given a UMLS release, this call returns details of all valid sources for the given release.


#### Sample Input (Java):

~~~~
myArrSrc = utsMetadataService.getAllSources(ticket, umlsRelease);
 for (int i = 0; i < myArrSrc.size(); i++) {
 SourceDTO myArrSrcDTO = myArrSrc.get(i);
 String abbreviation = myArrSrcDTO.getAbbreviation();
 String rtSrcAbbreviation =myArrSrcDTO.getRootSource().getAbbreviation();
 String version = myArrSrcDTO.getVersion();
 }
~~~~

#### Sample Input (C#):

~~~~
Metadata.sourceDTO[] myArraySource =utsMetadataService.getAllSources(singleUseTicket, "2012AB");
 for (int i = 0; i < myArraySource.Length; i++){
 Metadata.sourceDTO myArraySourceDTO = myArraySource[i];
 string abbreviation = myArraySourceDTO.abbreviation;
 string rootSource = myArraySourceDTO.rootSource.abbreviation;
 string version = myArraySourceDTO.version;
 }
~~~~

#### Sample Output:

Abbreviation    |  Root Source Abbreviation |  Version 
--- | --- | --- 
 ALT2009        |          ALT         |               2009               |
 AOD2000           |       AOD         |               2000               |
 AOT2003          |        AOT         |               2003               |
BI98              |       BI           |              1.0                |
 CCPSS99          |        CCPSS        |              1999               |
  CCS2005          |        CCS         |               2005               |
   CHV2010_10     |         CHV         |               2010_10           |
 COSTAR_89-95      |      COSTAR        |             89-95              |
  CPM2003          |        CPM          |              2003               |
  CPT01SP           |       CPTSP        |              2001               |
 CPT2005        |          CPT           |             2005               |
|   CPT2011       |          CPT         |               2011               |
>