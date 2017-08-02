title=Retrieving Source-Asserted Attributes
date=2015-11-19
updated=2015-11-19
type=page
status=published
category=Retrieving Source-Asserted Data
navorder=6
~~~~~~


[URIs](#uris) | [Query Parameters](#query-parameters) | [Sample Output](#sample-output)

URIs with /attributes support the following use cases:

*  Retrieve the source-asserted attributes for a known source-asserted identifier.

Note that 'current' in the URI can always be used to search against the latest UMLS publication.
You may use any valid UMLS release back to 2008AA in your URI if you would like to search against a particular version of the UMLS.


### URIs

**The base URI is https://uts-ws.nlm.nih.gov/rest**

Sample URI|Description|Returned JSON Object classType
--- | ---
/content/current/source/SNOMEDCT_US/9468002/attributes| Retrieves attributes of the SNOMED CT concept | Attribute


### Query Parameters

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
ticket | Y | A single-use service ticket is required for each call to the API. See [authentication](../../authentication.html) for more information | n/a | n/a | n/a
pageNumber | N | Whole number that specifies which page of results to fetch. | 1,2,3, etc | 1 | n/a
pageSize | N | Whole number that specifies the number of results to include per page. | 1,2,3, etc | 25 | n/a
includeAttributeNames | N | One or more attribute names | Any [attribute name] (https://www.nlm.nih.gov/research/umls/knowledge_sources/metathesaurus/release/attribute_names.html) in the UMLS | n/a | Use a comma between each attribute name to specify more than one.


### Sample Output

Sample output for https://uts-ws.nlm.nih.gov/rest/content/current/source/SNOMEDCT_US/9468002/attributes?ticket=ST...

~~~~json
{
    "pageSize": 25,
    "pageNumber": 1,
    "pageCount": 1,
    "result": [
        {
            "classType": "Attribute",
            "ui": "AT176854308",
            "sourceUi": "NONE",
            "rootSource": "SNOMEDCT_US",
            "name": "ACTIVE",
            "value": "1"
        },
        {
            "classType": "Attribute",
            "ui": "AT23334589",
            "sourceUi": "NONE",
            "rootSource": "SNOMEDCT_US",
            "name": "CTV3ID",
            "value": "S240."
        },
        {
            "classType": "Attribute",
            "ui": "AT176369162",
            "sourceUi": "NONE",
            "rootSource": "SNOMEDCT_US",
            "name": "DEFINITION_STATUS_ID",
            "value": "900000000000073002"
        },
        {
            "classType": "Attribute",
            "ui": "AT200386286",
            "sourceUi": "NONE",
            "rootSource": "SNOMEDCT_US",
            "name": "EFFECTIVE_TIME",
            "value": "20020131"
        },
        {
            "classType": "Attribute",
            "ui": "AT23558435",
            "sourceUi": "NONE",
            "rootSource": "SNOMEDCT_US",
            "name": "SNOMEDID",
            "value": "DD-12410"
        }
    ]
}
~~~~

