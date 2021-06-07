title=Retrieving UMLS Concept Definitions
date=2015-07-09
updated=2015-09-30
type=page
status=published
category=Retrieving UMLS Data
navorder=3
~~~~~~


[URIs](#uris) | [Query Parameters](#query-parameters) | [Sample Output](#sample-output)

URIs with /definitions support the following use cases:

*  Retrieve the source-asserted definitions for a known CUI.

Note that 'current' in the URI can always be used to search against the latest UMLS publication.
You may use any valid UMLS release back to 2008AA in your URI if you would like to search against a particular version of the UMLS.


### URIs

**The base URI is https://uts-ws.nlm.nih.gov/rest**

Sample URI|Description|Returned JSON Object classType
--- | ---
/content/current/CUI/C0155502/definitions | Retrieves definitions of the CUI | Definition


### Query Parameters

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
ticket | Y | A single-use service ticket is required for each call to the API. See [authentication](../authentication.html) for more information | n/a | n/a | n/a
sabs | N | Comma-separated list of source vocabularies to include in your search | Any root source abbreviation in the UMLS. See the "Abbreviation" column for a list of [UMLS source vocabulary abbreviations](https://www.nlm.nih.gov/research/umls/sourcereleasedocs/index.html).  | All UMLS source vocabularies | Use a comma between each source abbreviation to specify more than one.
pageNumber | N | Whole number that specifies which page of results to fetch. | 1,2,3, etc | 1 | n/a
pageSize | N | Whole number that specifies the number of results to include per page. | 1,2,3, etc | 25 | n/a


### Sample Output

Sample output for https://uts-ws.nlm.nih.gov/rest/content/current/CUI/C0155502/definitions?ticket=ST...

~~~~json
{
    "pageSize": 25,
    "pageNumber": 1,
    "pageCount": 1,
    "result": [
        {
            "classType": "Definition",
            "sourceOriginated": true,
            "rootSource": "MSH",
            "value": "Idiopathic recurrent VERTIGO associated with POSITIONAL NYSTAGMUS. It is associated with a vestibular loss without other neurological or auditory signs. Unlike in LABYRINTHITIS and VESTIBULAR NEURONITIS inflammation in the ear is not observed."
        }
    ]
}
~~~~

