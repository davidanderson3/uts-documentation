title=Retrieving parents and children information in the UMLS
date=2015-07-06
updated=2015-07-08
type=page
status=published
~~~~~~


[URIs](#uris) | [Query Parameters](#parameters) | [Sample Output](#samples)

URIs with /parents or /children support the following use cases:

*  Retrieve the immediate parents of a known source asserted identifier.
*  Retrieve all immediate children of a known source asserted identifier.

Note that 'current' in the URI can always be used to search against the latest UMLS publication.
You may use any valid UMLS release back to 2008AA in your URI if you would like to search against a particular version of the UMLS.


<a name = "uris"></a>
### URIs

*The base URI is https://uts-ws.nlm.nih.gov/rest*

Sample URI|Description
--- | ---
/content/current/source/SNOMEDCT_US/9468002/parents| Retrieves parents of the SNOMED concept
/content/current/source/SNOMEDCT_US/9468002/children| Retrieves children of the SNOMED concept


<a name = "parameters"></a>
### Available query parameters in /parents or /children calls

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
ticket | Y | A single-use service ticket is required for each call to the API. See [authentication](../authentication.html) for more information | n/a | n/a | n/a
sabs| N | One or more source abbreviations | Any root source abbreviation in the UMLS |n/a| Use a comma between each source abbreviation to specify more than one.


<a name = "samples"></a>
### Sample Output


**The default for calls under /parents is to return the immediate parents of the concept provided.**

~~~~json
{
    "result": [
        {
            "classType": "AtomClusterAtomClusterRelation",
            "ui": "6ca734fcc6f51b5a7464d32004218005",
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
            "relatedConcept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/20511007"
        },
        {
            "classType": "AtomClusterAtomClusterRelation",
            "ui": "95b9721325649c164a488a92a89dc16a",
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
            "relatedConcept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/82065001"
        },
        {
            "classType": "AtomClusterAtomClusterRelation",
            "ui": "fefc70e0043ac9c4319de31fd7baf4ed",
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
            "relatedConcept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/36991002"
        }
    ],
    "pageNum": 0,
    "pageSize": 0
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
    "pageNum": 0,
    "pageSize": 0
}

~~~~
