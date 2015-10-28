title=Paging and Filtering
date=2015-08-19
updated=2015-08-19
type=page
status=unpublished
category=Paging, sorting, Filtering
navorder=3
~~~~~~

The UMLS SOAP API's PSF (paging, sorting, and filtering object) allows you to customize your search results based on certain use cases.

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
Psf.setIncludeObsolete(false);
~~~~

#### setIncludeObsolete

~~~~java
Psf.setIncludeSuppressible(false);
~~~~

#### getIncludedTermTypes

~~~~java
Psf.getIncludedTermTypes().add("PT");
Psf.getIncludedTermTypes().add("FN");
~~~~

#### getIncludedRelationLabels

~~~~java
Psf.getIncludedRelationLabels().add("PAR");
Psf.getIncludedRelationLabels().add("SY");
~~~~

#### getIncludedAdditionalRelationLabels

~~~~java
Psf.getIncludedAdditionalRelationLabels().add("has_finding_site");
Psf.getIncludedAdditionalRelationLabels().add("has_procedure_site");
~~~~

#### getIncludedAttributeNames


~~~~java
Psf.getIncludedAttributeNames().add("CONCEPTSTATUS");
Psf.getIncludedAttributeNames().add("ISPRIMITIVE");
~~~~

#### setIncludedLanguage

~~~~java
 Psf.setIncludedLanguage("CZE");
~~~~


#### getIncludedSources

~~~~java
Psf.getIncludedSources().add("SNOMEDCT_US");
Psf.getIncludedSources().add("ICD10CM");
~~~~

#### setPageNum

~~~~java
Psf.setPageNum(2);
~~~~

#### setPageLn

~~~~java
Psf.setPageLn(50);
~~~~




