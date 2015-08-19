title=Filtering
date=2015-08-19
updated=2015-08-19
type=page
status=unpublished
category=Paging, sorting, Filtering
navorder=3
~~~~~~

**Method: **setIncludeObsolete( boolean value )

**Use Case:**  This method allows you to set a true/false flag on the PSF object to include or exclude atoms flagged obsolete (by either the source or NLM). Obsolete atoms are included by default.


#### Sample Input (Java):

~~~~
psfMetaContent.setIncludeObsolete(false);
~~~~
>

**Method: **setIncludeSuppressible( boolean value )

**Use Case:**  This method allows you to set a true/false flag on the PSF object to include or exclude atoms flagged suppressible by NLM editors. Suppressible content in the Metathesaurus can be either flagged "E", suppressed by NLM editors, or "Y", suppressed upon source inversion (pre-editing). Suppressible atoms are included by default.


#### Sample Input (Java):

~~~~
psfMetaContent.setIncludeSuppressible(false);
~~~~
>

**Method: **getIncludedRelationLabels().add()( String value )

**Use Case:** This method lets you specify which Relation Labels you would like to include in your result set. This is useful for filtering RelationDTOs.


#### Sample Input (Java):

~~~~
//Running getAllRelationLabels on a UtsWsMetadataController object will return all available relation labels for a given release.
//see the Metathesaurus Metadata tab above for more details

 psfMetaContent.getIncludedRelationLabels().add("PAR");
 psfMetaContent.getIncludedRelationLabels().add("SY");
~~~~
>

**Method: **getIncludedAdditionalRelationLabels().add()( String value )

**Use Case:** This method lets you specify which Additional Relation Labels (relas) you would like to include in your result set. This is useful for filtering RelationDTOs.


#### Sample Input (Java):

~~~~
//Running getAllAdditionalRelationLabels on a UtsWsMetadataController object will return all available additional relation labels for a given release.
//see the Metathesaurus Metadata tab above for more details

psfMetaContent.getIncludedAdditionalRelationLabels().add("has\_finding\_site");
psfMetaContent.getIncludedAdditionalRelationLabels().add("has\_procedure\_site");
~~~~

**Method: **getIncludedAttributeNames().add()( String value )

**Use Case:** This method lets you specify which Attribute Names you would like to include in your result set. This is useful for filtering AttributeDTOs.

#### Sample Input (Java):

~~~~
//Running getAllAttributeNames on a UtsWsMetadataController object will return all available attribute names for a given release.
//see the Metathesaurus Metadata tab above for more details

 psfMetaContent.getIncludedAttributeNames().add("CONCEPTSTATUS");
 psfMetaContent.getIncludedAttributeNames().add("ISPRIMITIVE");
~~~~
>

**Method: **setIncludedLanguage( String value )


**Use Case:** This method lets you specify which language you would like to include in your result set. This is useful for filtering TermDTOs and AtomDTOs.


#### Sample Input (Java):

~~~~
//the returned ArrayList &lt;AtomDTO&gt; will return only Czech language terms
//Running getAllLanguages on a UtsWsMetadataController object will return all available languages for a given release.
//see the Metathesaurus Metadata tab above for more details

 psfMetaContent.setIncludedLanguage("CZE");
~~~~
>

**Method: **getIncludedSources().add()( String value )

**Use Case:** This method lets you specify which sources you would like to include in your result set. This is useful for filtering SourceDataDTOs.


#### Sample Input (Java):

~~~~
//Running getAllSources on a UtsWsMetadataController object will return all available sources for a given release.
//see the Metathesaurus Metadata tab above for more details

 psfMetaContent.getIncludedSources().add("SNOMEDCT");
 psfMetaContent.getIncludedSources().add("ICD10CM");
~~~~
>

**Method: **getIncludedTermTypes().add()( String value )

**Use Case:** This method lets you specify which term types you would like to include in your result set. This is useful for filtering AtomDTOs.


#### Sample Input (Java):

~~~~
//Running getAllTermTypes on a UtsWsMetadataController object will return all available term types for a given release.
//see the Metathesaurus Metadata tab above for more details

 psfMetaContent.getIncludedTermTypes().add("PT");
 psfMetaContent.getIncludedTermTypes().add("FN");
~~~~
