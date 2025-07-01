title=Searching the UMLS
date=2015-06-08
updated=2021-03-03
type=page
status=published
navorder=3
~~~~~~


[URIs](#uris) | [Query Parameters](#query-parameters) | [Sample Output](#sample-output) | [Paging through results](#paging-through-results)

URIs with /search support the following use cases:

*  Return a list of CUIs and their names when searching a human readable term.
*  Return a list of source-asserted identifiers (codes) and their names when searching a human readable term.
*  Map source-asserted identifiers to UMLS CUIs.

Note that 'current' in the URI can always be used to search against the latest UMLS publication.
You may use any valid UMLS release back to 2008AA in your URI if you would like to search against a particular version of the UMLS.


### URIs

**The base URI is https://uts-ws.nlm.nih.gov/rest**

Sample URI|Description|Returned JSON Object classType
--- | ---
/search/current?string=fracture of carpal bone | Retrieves CUIs for a search term - [python example](/rest/rest-api-cookbook/python-scripts.html#get-concepts-for-a-list-of-strings)| searchResults
/search/current?string=fracture of carpal bone&searchType=exact | Uses 'exact' searching | searchResults
/search/current?string=fracture of carpal bone&sabs=SNOMEDCT_US&returnIdType=code | Returns SNOMEDCT concepts associated with a search term  | searchResults
/search/current?string=9468002&inputType=sourceUi&searchType=exact&sabs=SNOMEDCT_US | Returns UMLS CUIs associated with a SNOMEDCT_US concept  - [python example](/rest/rest-api-cookbook/python-scripts.html#get-concepts-for-a-list-of-codes) | searchResults
/search/current?string=C0009044&sabs=SNOMEDCT_US&returnIdType=code | Returns SNOMED CT concepts associated with a UMLS CUI - [python example](/rest/rest-api-cookbook/python-scripts.html#get-codes-for-a-list-of-concepts) | searchResults

### Query Parameters

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
apiKey | Y | An API key is required for each call to the API. Visit [your UTS profile](https://uts.nlm.nih.gov/uts/profile) to obtain your API key. | n/a | n/a | n/a
string | Y|  A human readable term, such as 'gestational diabetes', or a code from a source vocabulary, such as 11687002 from SNOMEDCT_US. | Any term or code in the UMLS. | n/a | n/a
inputType | N | Specifies the data type you are using as your search parameter.  | 'atom', 'code','sourceConcept','sourceDescriptor','sourceUi','tty' | 'atom' | Use 'sourceUi' if you aren't sure if the identifier you're providing is a code, source concept, or source descriptor.  Using 'tty' is for advanced use cases and will extract codes from a specified vocabulary according to [term type](https://www.nlm.nih.gov/research/umls/knowledge_sources/metathesaurus/release/precedence_suppressibility.html).
includeObsolete | N | Return content that is a result of matches on obsolete terms. | true or false | false | n/a
includeSuppressible | N | Return content that is a result of matches on suppressible terms. | true or false | false | n/a
returnIdType | N | Specifies the type of identifier you wish to retrieve. | 'aui','concept','code','sourceConcept','sourceDescriptor', 'sourceUi' | 'concept' | Use 'code','sourceConcept', 'sourceDescriptor', or 'sourceUi' if you prefer source-asserted identifiers rather than CUIs in your search results.
sabs | N | Comma-separated list of source vocabularies to include in your search | Any root source abbreviation in the UMLS. See the "Abbreviation" column for a list of [UMLS source vocabulary abbreviations](https://www.nlm.nih.gov/research/umls/sourcereleasedocs/).  | All UMLS source vocabularies | Use a comma between each source abbreviation to specify more than one.
searchType | N | Type of search you wish to use. | 'exact','words','leftTruncation', 'rightTruncation', 'normalizedString', 'normalizedWords' | 'words' | Use 'exact' when using inputType = 'code', 'sourceConcept', 'sourceDescriptor', or 'sourceUi'. [More information...](#searchType)
partialSearch | N | Return partial matches for your query. | true or false | false | n/a
pageNumber | N | Whole number that specifies which page of results to fetch. | 1,2,3, etc | 1 | n/a
pageSize | N | Whole number that specifies the number of results to include per page. | 1,2,3, etc | 25 | n/a

<a name="searchType"></a>
#### Expected Behaviors for the searchType Parameter

* **words**: default searchType. Retrieves results where all words in the query appear in a particular name. 
* **exact**: retrieves only concepts that include a synonym that exactly matches the search term.
* **normalizedString**: use with English language terms only. Removes lexical variations such as plural and upper case text and compares search terms to the Metathesaurus normalized string index to retrieve relevant concepts.
* **normalizedWords**: use with English language terms only. Removes lexical variations such as plural and upper case text, and compares search terms to the Metathesaurus normalized word index to retrieve relevant concepts.
* **rightTruncation**: retrieves concepts with synonyms that begin with the letters of the search term. For example, a right truncation search for "bronch" retrieves concepts that contain synonyms such as bronchitis, bronchiole, bronchial artery.
* **leftTruncation**: retrieves concepts with synonyms that end with the letters of the search term. For example, a left truncation search for "itis" retrieves concepts that contain synonyms such as colitis, bronchitis, pancreatitis.
* **approximate [DEPRECATED]**: <span style="color:red">This searchType is deprecated. We are no longer supporting this option. </span>

### Sample Output

The default search parameters will return CUIs and their names.  If you ask for codes, sourceConcept, or sourceDescriptor as your returnIdType, you will get back source-asserted identifiers instead of CUIs.

Sample output for https://uts-ws.nlm.nih.gov/rest/search/current?string=fracture of carpal bone&apiKey=YOUR_APIKEY...

~~~~json
{

    "pageSize": 25,
    "pageNumber": 1,
    "result": 

{

    "classType": "searchResults",
    "results": 

[

{

    "ui": "C0009044",
    "rootSource": "SNOMEDCT_US",
    "uri": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/CUI/C0009044",
    "name": "Closed fracture carpal bone"

},
{

    "ui": "C0016644",
    "rootSource": "MTH",
    "uri": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/CUI/C0016644",
    "name": "Fracture of carpal bone"

},
{

    "ui": "C0159765",
    "rootSource": "MTH",
    "uri": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/CUI/C0159765",
    "name": "Open fracture of carpal bone, unspecified"

},
...
        ]
    }

}
~~~~

**Specifying returnIdType = 'code','sourceConcept',or 'sourceDescriptor' will result in output as follows:**

Sample output for https://uts-ws.nlm.nih.gov/rest/search/current?string=fracture of carpal bone&returnIdType=sourceConcept&apiKey=YOUR_APIKEY...

~~~~json
{

    "pageSize": 25,
    "pageNumber": 1,
    "result": 

{

    "classType": "searchResults",
    "results": 

[

{

    "ui": "9468002",
    "rootSource": "SNOMEDCT_US",
    "uri": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/9468002",
    "name": "Closed fracture carpal bone"

},
{

    "ui": "C34488",
    "rootSource": "NCI",
    "uri": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/NCI/C34488",
    "name": "Closed Fracture of Carpal Bone"

},
{

    "ui": "34696",
    "rootSource": "MEDCIN",
    "uri": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/MEDCIN/34696",
    "name": "closed fracture of carpal bone"

},
...
        ]
    }

}
~~~~


### Paging through results

Many times a search will return more than one page of results.  Json data returned by the /search endpoint will tell you what page number you are on,
but the current implementation does not tell you how many total pages of results there are as a result of your search.  So how do you know when you've reached the end of
your search results?   On the /search endpoint, the end of your search results will always:

*   Exist on their own unique page (not live on the same page with the rest of your search results)
*   Contain the following structure:

~~~~.json
{
    "pageSize": 25, 
    "pageNumber": 2, //your final page number may be different.  
    "result": {
        "classType": "searchResults", 
        "results": [
            {
                "ui": "NONE", 
                "name": "NO RESULTS"
            }
        ]
    }
}
~~~~

This structure will also be displayed if your original search returns null.