title=UTS SOAP API Updates
date=2015-08-18
updated=2015-08-18
type=page
status=unpublished
navorder=8
~~~~~~


### Web Service Updates

Date|Issue|Description|WSDL
--- | --- | --- | ---
December 2014|Deprecation|The following methods of the UTS API 2.0 are deprecated and will be removed from the service as of the 2015AA Spring UMLS Release.-   getAtomCooccurrences-getCoccurrenceSubheadingFrequencies
-   getCooccurrenceType
-   getAllCooccurrenceTypes
Users who are using these methods should begin removing them from their
code. Cooccurrence data are now available from the [MEDLINE Baseline
Repository.](http://mbr.nlm.nih.gov/MRCOC.shtml)|
October 2014|New Method|New method introduced- getNewConcepts(): Retrives all new concepts for a given UMLS release.|Content
October 2014|New Method|New method introduced- getNewConceptsCount(): Retrives the count of all new concepts for a given UMLS release.|Content
September 2013|New Method|New method introduced- getConceptDefinitions(): Retrieves|source-provided definition(s) for a given conceptId.|Content
September 2013|New Method|New method introduced- getUpdatedSourcesByVersion(): Retrieves all the sources that have been updated in a given UMLS release.|Metadata
September 2013|New Method|New method introduced- getAllRootSourceFamilies(): Retrieves all the source families present as per a given UMLS release.|Metadata
September 2013|New Method|New method introduced- getRootSourcesByFamily(): Gets all the sources associated with a source family.|Metadata
September 2013|New Method|New method introduced- getRootSourcesByRestrictionLevel(): Retrieves all the root sources given a restriction level.|Metadata
September 2013|New Method|New method introduced- getRootSourcesByLanguage(): Retrieves all the sources that are provided in a particular language.|Metadata
September 2013|Additional Functionalities|Additional Functionalities added to method getConceptBequeathals(): See documentation for added functionality associated with this method.|Concept History
September 2013|Additional Functionalities|Additional Functionalities added to method getConceptDeletions(): Seedocumentation for added functionality associated with this method.|Concept History
September 2013|Additional Functionalities|Additional Functionalities added to method getConceptMerges(): Seedocumentation for added functionality associated with this method.|Concept History|April 2013|New Method|New method introduced- getCurrentUMLSVersion(): This method allows the user to retrieve the current UMLS release.|Metadata
April 2013|New Method|New method introduced- getAllUMLSVersions(): This method allows the user to retrieve a list of all UMLS releases available.|Metadata



### Bug Fixes

Date|Issue|Description|Status
--- | --- | --- | ---
November 2012|Bug|Using setIncludeObsolete(true) and setIncludeSuppressible(true) are not filtering out obsolete/suppressible atoms|Fixed
October 2012|Bug|In the finder service, searching on metadata codes such as "V-SNOMEDCT"returned no results. This has been corrected. Users should recompile their content wsdl to obtain the update.|Fixed
June 2012|Bug|In the finder service PSF, specifying a source vocabulary through getIncludedSources().add("SNOMEDCT") caused a NULL result set. This has been fixed.|Fixed

