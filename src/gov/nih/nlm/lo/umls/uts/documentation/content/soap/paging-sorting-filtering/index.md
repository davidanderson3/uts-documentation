title=Paging, Sorting and Filtering
date=2015-08-19
updated=2015-08-19
type=page
status=published
navorder=3
~~~~~~

The Paging, Sorting, and Filtering (PSF) object of the UMLS SOAP allows you to customize the results of your Web service calls in a variety of ways. The PSF object allows a great deal of flexibility in customizing your view of returned data.
You can:

* include or exclude criteria such as source vocabularies, language, term types, obsolescence, and suppressibilty
* sort your results by different fields, depending on the return type
* choose the number of results displayed per page
* choose number of pages of results returned

You can create a PSF object in java as follows:
```Psf psf = new Psf();```

Method | Use With | Use Case | Permitted Values | Default Value
-- | -- | -- | --
[setIncludeObsolete](#setincludeobsolete) | UiLabel, UiLabelRootSource, AtomDTO | Include or exclude search results based on source-asserted obsolscence. | True, False | True
[setIncludeSuppressible](#setincludesuppressible)| UiLabel, UiLabelRootSource, AtomDTO | Include or exclude search results based on source-asserted obsolscence. | True, False | True
[setIncludedLanguage](#setincludedlanguage) | AtomDTO | Limit results to only include terms that meet the specified language abbreviation provided | Any valid language abbreviation in the UMLS | All languages are included by default
[getIncludedTermTypes](#getincludedtermtypes) | AtomDTO | Limit results to include only atoms that match the specified term types | Any vaid term type in the UMLS | All term types are include by default
[getIncludedSources](#getincludedsources) | AtomDTO | Limit results to only include specific source vocabularies | Any valid source abbreviation (rsab) in the UMLS | All source vocabularies are included by default
[getIncludedRelationLabels](#getincludedrelationlabels) | AtomClusterRelationDTO | Limit results to include only relationships that meet the provided criteria | Any relation label in the UMLS | All relation labels are included by default
[getIncludedAdditionalRelationLabels](#getincludedrelationlabels)| AtomClusterRelationDTO | Limit results to include only additional relation labels that meet the provided criteria | Any additional relation label | All additional relation labels are included by default
[getIncludedAttributeNames](#getincludedattributenames)| AttributeDTO | Limit results to include only attributes that match the specified names | Any valid attribute name in the UMLS | All attribute names are included by default
[setPageNum](#setpagenum) | any | Specify page number to retrieve | Any positive integer | 1
[setPageLn](#setpageln) | any | Specify number of objects returned per page | Any positive integer between 25 - 1000 | 25


#### setIncludeSuppressible

~~~~java
psf.setIncludeObsolete(false);
~~~~

#### setIncludeObsolete

~~~~java
psf.setIncludeSuppressible(false);
~~~~

#### getIncludedTermTypes

~~~~java
psf.getIncludedTermTypes().add("PT");
psf.getIncludedTermTypes().add("FN");
~~~~

#### getIncludedRelationLabels

~~~~java
psf.getIncludedRelationLabels().add("PAR");
psf.getIncludedRelationLabels().add("SY");
~~~~

#### getIncludedAdditionalRelationLabels

~~~~java
psf.getIncludedAdditionalRelationLabels().add("has_finding_site");
psf.getIncludedAdditionalRelationLabels().add("has_procedure_site");
~~~~

#### getIncludedAttributeNames


~~~~java
psf.getIncludedAttributeNames().add("CONCEPTSTATUS");
psf.getIncludedAttributeNames().add("ISPRIMITIVE");
~~~~

#### setIncludedLanguage

~~~~java
psf.setIncludedLanguage("CZE");
~~~~


#### getIncludedSources

~~~~java
psf.getIncludedSources().add("SNOMEDCT_US");
psf.getIncludedSources().add("ICD10CM");
~~~~

#### setPageNum

~~~~java
psf.setPageNum(2);
~~~~

#### setPageLn

~~~~java
psf.setPageLn(50);
~~~~




