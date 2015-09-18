title=Retrieving Source-Asserted Relations
date=2015-09-15
updated=2015-09-15
type=page
status=draft
category=Retrieving Source-Asserted Data
navorder=4
~~~~~~


[URIs](#uris) | [Query Parameters](#query-parameters) | [Sample Output](#sample-output)

URIs with /relations support the following use cases:

*  Retrieve the sources-asserted relationships for a known source-asserted identifier.

Note that 'current' in the URI can always be used to search against the latest UMLS publication.
You may use any valid UMLS release back to 2008AA in your URI if you would like to search against a particular version of the UMLS.


### URIs

**The base URI is https://uts-ws.nlm.nih.gov/rest**

Sample URI|Description
--- | ---
/content/current/source/SNOMEDCT_US/77147000/relations| Retrieves relationships of the SNOMED concept


### Query Parameters

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
ticket | Y | A single-use service ticket is required for each call to the API. See [authentication](../authentication.html) for more information | n/a | n/a | n/a
pageNumber | N | Whole number that specifies which page of results to fetch. | 1,2,3, etc | 1 | n/a
pageSize | N | Whole number that specifies the number of results to include per page. | 1,2,3, etc | 25 | n/a


### Sample Output


**Calls under /relations will return a classType of 'AtomClusterAtomClusterRelation'.**

Sample output for /content/2015AA/source/SNOMEDCT_US/77147000/relations?ticket=ST...

~~~~json
{
    "result": [
        {
            "classType": "AtomClusterAtomClusterRelation",
            "ui": "R84490076",
            "suppressible": false,
            "sourceUi": "NONE",
            "obsolete": false,
            "sourceOriginated": true,
            "rootSource": "SNOMEDCT_US",
            "relationLabel": "RN",
            "additionalRelationLabel": "mapped_to",
            "groupId": "NONE",
            "attributeCount": 0,
            "relatedAtom": "NONE",
            "relatedConcept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/579.9"
        },
        {
            "classType": "AtomClusterAtomClusterRelation",
            "ui": "R19807467",
            "suppressible": false,
            "sourceUi": "273426023",
            "obsolete": false,
            "sourceOriginated": true,
            "rootSource": "SNOMEDCT_US",
            "relationLabel": "CHD",
            "additionalRelationLabel": "isa",
            "groupId": "NONE",
            "attributeCount": 0,
            "relatedAtom": "NONE",
            "relatedConcept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/32230006"
        },
        {
            "classType": "AtomClusterAtomClusterRelation",
            "ui": "R20059020",
            "suppressible": false,
            "sourceUi": "2042729024",
            "obsolete": false,
            "sourceOriginated": true,
            "rootSource": "SNOMEDCT_US",
            "relationLabel": "CHD",
            "additionalRelationLabel": "isa",
            "groupId": "NONE",
            "attributeCount": 0,
            "relatedAtom": "NONE",
            "relatedConcept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/85919009"
        },
        {
            "classType": "AtomClusterAtomClusterRelation",
            "ui": "R13983646",
            "suppressible": false,
            "sourceUi": "2042730025",
            "obsolete": false,
            "sourceOriginated": true,
            "rootSource": "SNOMEDCT_US",
            "relationLabel": "RO",
            "additionalRelationLabel": "has_finding_site",
            "groupId": "0",
            "attributeCount": 0,
            "relatedAtom": "NONE",
            "relatedConcept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/113276009"
        }
    ],
    "pageNumber": 1,
    "pageSize": 25,
    "pageCount": 1
}
~~~~

