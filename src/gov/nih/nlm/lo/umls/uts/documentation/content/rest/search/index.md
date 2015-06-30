title=Searching the UMLS
date=2015-06-08
updated=2015-06-25
type=page
status=published
~~~~~~


**API Version:** 0.1 alpha

[URIs](#uris) | [Query Parameters](#parameters) | [Sample Output](#samples)

URIs with /search support the following use cases

*  Return a list of CUIs and their names when searching a human readable term.
*  Return a list of CUIs and their names when searching a source-asserted identifier (code).
*  Return a list of source-asserted identifiers (codes) and their names when searching a human readable term.

Note that 'current' in the URI can always be used to search against the latest UMLS publication.
You may use any valid UMLS release back to 2008AA in your URI if you would like to search against a particular version of the UMLS.


<a name = "uris"></a>
### URIs

*The base URI is https://uts-ws.nlm.nih.gov/rest*

Sample URI|Description
--- | ---
/search/current/?string=fracture of carpal bone | Retrieves CUIs for a search term
/search/current/?string=fracture of carpal bone&searchType=exact | Uses 'exact' searching
/search/current/?string=fracture of carpal bone&sabs=SNOMEDCT_US&returnType=codes | Returns SNOMEDCT concepts associated with a search term.
/search/current/?string=82065001&inputType=code&searchType=exact&sabs=SNOMEDCT_US | Returns UMLS CUIs associated with a SNOMEDCT_US concept.

<a name = "parameters"></a>
### Available query parameters in /search

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
ticket | Y | A single-use service ticket is required for each call to the API. See [authentication](../authentication.html) for more information | n/a | n/a | n/a
string | Y|  A human readable term, such as 'gestatational diabetes', or a code from a source vocabulary, such as 11687002 from SNOMEDCT_US. | Any term or code in the UMLS. | n/a | n/a
inputType | N | Specifies the data type you are using as your search parameter.  | 'atom', 'code','sourceConcept','sourceDescriptor' | 'atom' | n/a
returnIdType | N | Specifies the type of identifier you wish to retrieve. | 'aui','concept','code','sourceConcept','sourceDescriptor' | 'concept' | Use 'code','sourceConcept', or 'sourceDescriptor' if you prefer source-asserted identifiers rather than CUIs in your search results.
sabs | N | Comma-separated list of source vocabularies to include in your search | Any [root source abbreviation](http://www.nlm.nih.gov/research/umls/sourcereleasedocs/index.html) in the UMLS. | All UMLS sources | n/a
searchType | N | Type of search you wish to use | 'exact','words','leftTruncation', 'rightTruncation','approximate' | 'words' | Use 'exact' when using inputType = 'code', 'sourceConcept', or 'sourceDescriptor'.
page | N | Whole number that specifies which page of results to fetch. | 1,2,3, etc | 1 | n/a
pageSize | N | Whole number that specifies the number of results to include per page. | 1,2,3, etc | 25 | n/a
<a name = "samples"></a>
### Sample Output

Calls under /search will return a JSON object of classType 'searchResults'.
The default search parameters will return CUIs and their names.  If you ask for codes, sourceConcept, or sourceDescriptor as your returnIdType,
you will get back source-asserted identifiers instead of CUIs.

**The default for calls under /search is to return UMLS CUIs.**

~~~~json
{

    "results": 

[

{

    "name": "Closed fracture carpal bone",
    "ui": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/CUI/C0009044/"

},
{

    "name": "Fracture of carpal bone",
    "ui": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/CUI/C0016644/"

},
{

    "name": "Open fracture of carpal bone, unspecified",
    "ui": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/CUI/C0159765/"

},
...
    ],
    "classType": "searchResults"

}
~~~~

**Specifying returnIdType = 'code','sourceConcept',or 'sourceDescriptor' will result in output as follows:**

~~~~json
{

    "results": 

[

{

    "name": "Closed fracture carpal bone",
    "ui": "https://uts-ws-qa.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/9468002/",
    "rootSource": "SNOMEDCT_US"

},
{

    "name": "Fracture of carpal bone",
    "ui": "https://uts-ws-qa.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/157222007/",
    "rootSource": "SNOMEDCT_US"

},
{

    "name": "Fracture of carpal bone",
    "ui": "https://uts-ws-qa.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/82065001/",
    "rootSource": "SNOMEDCT_US"

},
...
    ],
    "classType": "searchResults"

}

~~~~
