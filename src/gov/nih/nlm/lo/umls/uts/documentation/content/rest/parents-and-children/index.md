title=Retrieving Parents and Children
date=2015-07-06
updated=2015-07-08
type=page
status=published
category=Retrieving Source-Asserted Data
navorder=2
~~~~~~


[URIs](#uris) | [Query Parameters](#query-parameters) | [Sample Output](#sample-output)

URIs with /parents or /children support the following use cases:

*  Retrieve the immediate parents of a known source asserted identifier.
*  Retrieve all immediate children of a known source asserted identifier.

Note that 'current' in the URI can always be used to search against the latest UMLS publication.
You may use any valid UMLS release back to 2008AA in your URI if you would like to search against a particular version of the UMLS.


### URIs

**The base URI is https://uts-ws.nlm.nih.gov/rest**

Sample URI|Description
--- | ---
/content/current/source/SNOMEDCT_US/9468002/parents| Retrieves parents of the SNOMED concept
/content/current/source/SNOMEDCT_US/9468002/children| Retrieves children of the SNOMED concept


### Query Parameters

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
ticket | Y | A single-use service ticket is required for each call to the API. See [authentication](../authentication.html) for more information |  |  | 
page | N | Whole number that specifies which page of results to fetch. | 1,2,3, etc | 1 | 
pageSize | N | Whole number that specifies the number of results to include per page. | 1,2,3, etc | 25 | 


### Sample Output


*Calls under /parents or /children will return a classType of 'AtomClusterAtomClusterRelation'*

~~~~json
{
    "result": [
        {
            "classType": "AtomClusterAtomClusterRelation",
            "ui": "e50f3647a92e85415e8b8c5cde3e5f4c",
            "suppressible": false,
            "sourceUi": null,
            "obsolete": false,
            "sourceOriginated": true,
            "rootSource": "SNOMEDCT_US",
            "relationLabel": "PAR",
            "additionalRelationLabel": "isa",
            "groupId": null,
            "attributeCount": 0,
            "relatedAtom": "",
            "relatedConcept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/226598007"
        }
    ],
    "pageNum": 1,
    "pageSize": 25
}


~~~~


**The default for calls under /children is to return the immediate children of the concept provided.**

~~~~json

{
    "result": [
        {
            "classType": "AtomClusterAtomClusterRelation",
            "ui": "3044515a9559e835bc8ed5bf7099fddc",
            "suppressible": false,
            "sourceUi": null,
            "obsolete": false,
            "sourceOriginated": true,
            "rootSource": "SNOMEDCT_US",
            "relationLabel": "CHD",
            "additionalRelationLabel": "isa",
            "groupId": null,
            "attributeCount": 0,
            "relatedAtom": "",
            "relatedConcept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/10934401000119101"
        },
        {
            "classType": "AtomClusterAtomClusterRelation",
            "ui": "5a14b35f8b85af14f2f5e39b1e7408a6",
            "suppressible": false,
            "sourceUi": null,
            "obsolete": false,
            "sourceOriginated": true,
            "rootSource": "SNOMEDCT_US",
            "relationLabel": "CHD",
            "additionalRelationLabel": "isa",
            "groupId": null,
            "attributeCount": 0,
            "relatedAtom": "",
            "relatedConcept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/208375001"
        },
        {
            "classType": "AtomClusterAtomClusterRelation",
            "ui": "f22c54b32695c7bcb4d96c5620d6987f",
            "suppressible": false,
            "sourceUi": null,
            "obsolete": false,
            "sourceOriginated": true,
            "rootSource": "SNOMEDCT_US",
            "relationLabel": "CHD",
            "additionalRelationLabel": "isa",
            "groupId": null,
            "attributeCount": 0,
            "relatedAtom": "",
            "relatedConcept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/10934361000119105"
        }
    ],
    "pageNum": 1,
    "pageSize": 25
}

~~~~
