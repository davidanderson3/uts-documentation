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
/content/current/source/SNOMEDCT_US/9468002/relations| Retrieves relationships of the SNOMED concept


### Query Parameters

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
ticket | Y | A single-use service ticket is required for each call to the API. See [authentication](../authentication.html) for more information | n/a | n/a | n/a
pageNumber | N | Whole number that specifies which page of results to fetch. | 1,2,3, etc | 1 | n/a
pageSize | N | Whole number that specifies the number of results to include per page. | 1,2,3, etc | 25 | n/a


### Sample Output


**Calls under /relations will return a classType of 'SourceAtomCluster'.**

Sample output for /content/current/source/SNOMEDCT_US/9468002/relations?ticket=ST...

~~~~json
{
    "result": [
        {
            "classType": "SourceAtomCluster",
            "ui": "20511007",
            "suppressible": false,
            "sourceUi": "20511007",
            "obsolete": false,
            "rootSource": "SNOMEDCT_US",
            "atomCount": 6,
            "cVMemberCount": 0,
            "attributes": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/20511007/attributes",
            "atoms": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/20511007/atoms",
            "descendants": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/20511007/descendants",
            "ancestors": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/20511007/ancestors",
            "parents": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/20511007/parents",
            "children": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/20511007/children",
            "relations": "NONE",
            "definitions": "NONE",
            "memberships": "NONE",
            "name": "Fracture of hand"
        },
        {
            "classType": "SourceAtomCluster",
            "ui": "36991002",
            "suppressible": false,
            "sourceUi": "36991002",
            "obsolete": false,
            "rootSource": "SNOMEDCT_US",
            "atomCount": 5,
            "cVMemberCount": 0,
            "attributes": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/36991002/attributes",
            "atoms": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/36991002/atoms",
            "descendants": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/36991002/descendants",
            "ancestors": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/36991002/ancestors",
            "parents": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/36991002/parents",
            "children": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/36991002/children",
            "relations": "NONE",
            "definitions": "NONE",
            "memberships": "NONE",
            "name": "Closed fracture of upper limb"
        },
        {
            "classType": "SourceAtomCluster",
            "ui": "82065001",
            "suppressible": false,
            "sourceUi": "82065001",
            "obsolete": false,
            "rootSource": "SNOMEDCT_US",
            "atomCount": 7,
            "cVMemberCount": 0,
            "attributes": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/82065001/attributes",
            "atoms": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/82065001/atoms",
            "descendants": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/82065001/descendants",
            "ancestors": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/82065001/ancestors",
            "parents": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/82065001/parents",
            "children": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/82065001/children",
            "relations": "NONE",
            "definitions": "NONE",
            "memberships": "NONE",
            "name": "Fracture of carpal bone"
        }
    ],
    "pageNumber": 1,
    "pageSize": 25,
    "pageCount": 1
}
~~~~

