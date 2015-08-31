title=Retrieving Parents and Children
date=2015-07-06
updated=2015-08-31
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
ticket | Y | A single-use service ticket is required for each call to the API. See [authentication](../authentication.html) for more information | n/a | n/a | n/a
pageNumber | N | Whole number that specifies which page of results to fetch. | 1,2,3, etc | 1 | n/a
pageSize | N | Whole number that specifies the number of results to include per page. | 1,2,3, etc | 25 | n/a


### Sample Output


**Calls under /parents or /children will return a classType of 'SourceAtomCluster'.**

Sample output for /content/current/source/SNOMEDCT_US/9468002/parents?ticket=ST...

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


**The default for calls under /children is to return the immediate children of the concept provided.**

Sample output for /content/current/source/SNOMEDCT_US/9468002/children?ticket=ST...

~~~~json


{
    "result": [
        {
            "classType": "SourceAtomCluster",
            "ui": "10934361000119105",
            "suppressible": false,
            "sourceUi": "10934361000119105",
            "obsolete": false,
            "rootSource": "SNOMEDCT_US",
            "atomCount": 3,
            "cVMemberCount": 0,
            "attributes": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/10934361000119105/attributes",
            "atoms": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/10934361000119105/atoms",
            "descendants": "NONE",
            "ancestors": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/10934361000119105/ancestors",
            "parents": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/10934361000119105/parents",
            "children": "NONE",
            "relations": "NONE",
            "definitions": "NONE",
            "memberships": "NONE",
            "name": "Closed fracture of navicular bone of right wrist"
        },
        {
            "classType": "SourceAtomCluster",
            "ui": "10934401000119101",
            "suppressible": false,
            "sourceUi": "10934401000119101",
            "obsolete": false,
            "rootSource": "SNOMEDCT_US",
            "atomCount": 3,
            "cVMemberCount": 0,
            "attributes": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/10934401000119101/attributes",
            "atoms": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/10934401000119101/atoms",
            "descendants": "NONE",
            "ancestors": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/10934401000119101/ancestors",
            "parents": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/10934401000119101/parents",
            "children": "NONE",
            "relations": "NONE",
            "definitions": "NONE",
            "memberships": "NONE",
            "name": "Closed fracture of navicular bone of left wrist"
        },
        {
            "classType": "SourceAtomCluster",
            "ui": "208375001",
            "suppressible": false,
            "sourceUi": "208375001",
            "obsolete": false,
            "rootSource": "SNOMEDCT_US",
            "atomCount": 2,
            "cVMemberCount": 0,
            "attributes": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/208375001/attributes",
            "atoms": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/208375001/atoms",
            "descendants": "NONE",
            "ancestors": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/208375001/ancestors",
            "parents": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/208375001/parents",
            "children": "NONE",
            "relations": "NONE",
            "definitions": "NONE",
            "memberships": "NONE",
            "name": "Closed fracture carpal bones, multiple"
        }
    ],
    "pageNumber": 1,
    "pageSize": 25,
    "pageCount": 1
}


~~~~
