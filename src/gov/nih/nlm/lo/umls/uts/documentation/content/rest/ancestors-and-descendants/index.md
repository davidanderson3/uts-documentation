title=Retrieving Source-Asserted Ancestors and Descendants
date=2015-08-28
updated=2016-03-07
type=page
status=published
category=Retrieving Source-Asserted Data
navorder=3
~~~~~~


[URIs](#uris) | [Query Parameters](#query-parameters) | [Sample Output](#sample-output)

URIs with /ancestors or /descendants support the following use cases:

*  Retrieve all ancestors of a known source asserted identifier.
*  Retrieve all descendants of a known source asserted identifier.

Note that 'current' in the URI can always be used to search against the latest UMLS publication.
You may use any valid UMLS release back to 2008AA in your URI if you would like to search against a particular version of the UMLS.


### URIs

**The base URI is https://uts-ws.nlm.nih.gov/rest**

Sample URI|Description|Returned JSON Object classType
--- | ---
/content/current/source/SNOMEDCT_US/9468002/ancestors|Retrieves ancestors of a source-asserted identifier|SourceAtomCluster*
/content/current/source/SNOMEDCT_US/9468002/descendants|Retrieves descendants of a source-asserted identifier|SourceAtomCluster*

*Calls using codes from HL7V2.5 and HL7V3.0 return output with an "Atom" JSON Object classType*.

### Query Parameters

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
ticket | Y | A single-use service ticket is required for each call to the API. See [authentication](../authentication.html) for more information | n/a | n/a | n/a
pageNumber | N | Whole number that specifies which page of results to fetch. | 1,2,3, etc | 1 | n/a
pageSize | N | Whole number that specifies the number of results to include per page. | 1,2,3, etc | 25 | n/a


### Sample Output

Sample output for /content/current/source/SNOMEDCT_US/9468002/descendants?ticket=ST...

~~~~.json
{
    "pageSize": 25,
    "pageNumber": 1,
    "pageCount": 1,
    "result": [
        {
            "classType": "SourceAtomCluster",
            "ui": "10934241000119100",
            "suppressible": false,
            "obsolete": false,
            "rootSource": "SNOMEDCT_US",
            "atomCount": 2,
            "cVMemberCount": 0,
            "attributes": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/10934241000119100/attributes",
            "atoms": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/10934241000119100/atoms",
            "descendants": "NONE",
            "ancestors": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/10934241000119100/ancestors",
            "parents": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/10934241000119100/parents",
            "children": "NONE",
            "relations": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/10934241000119100/relations",
            "definitions": "NONE",
            "concepts": "https://uts-ws.nlm.nih.gov/rest/search/2015AB?string=10934241000119100&sabs=SNOMEDCT_US&searchType=exact&inputType=sourceUi",
            "defaultPreferredAtom": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/10934241000119100/atoms/preferred",
            "name": "Closed fracture of pisiform bone of left wrist"
        },
        {
            "classType": "SourceAtomCluster",
            "ui": "10934361000119105",
            "suppressible": false,
            "obsolete": false,
            "rootSource": "SNOMEDCT_US",
            "atomCount": 3,
            "cVMemberCount": 0,
            "attributes": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/10934361000119105/attributes",
            "atoms": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/10934361000119105/atoms",
            "descendants": "NONE",
            "ancestors": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/10934361000119105/ancestors",
            "parents": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/10934361000119105/parents",
            "children": "NONE",
            "relations": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/10934361000119105/relations",
            "definitions": "NONE",
            "concepts": "https://uts-ws.nlm.nih.gov/rest/search/2015AB?string=10934361000119105&sabs=SNOMEDCT_US&searchType=exact&inputType=sourceUi",
            "defaultPreferredAtom": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/10934361000119105/atoms/preferred",
            "name": "Closed fracture of navicular bone of right wrist"
        },
        {
            "classType": "SourceAtomCluster",
            "ui": "10934401000119101",
            "suppressible": false,
            "obsolete": false,
            "rootSource": "SNOMEDCT_US",
            "atomCount": 3,
            "cVMemberCount": 0,
            "attributes": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/10934401000119101/attributes",
            "atoms": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/10934401000119101/atoms",
            "descendants": "NONE",
            "ancestors": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/10934401000119101/ancestors",
            "parents": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/10934401000119101/parents",
            "children": "NONE",
            "relations": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/10934401000119101/relations",
            "definitions": "NONE",
            "concepts": "https://uts-ws.nlm.nih.gov/rest/search/2015AB?string=10934401000119101&sabs=SNOMEDCT_US&searchType=exact&inputType=sourceUi",
            "defaultPreferredAtom": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/10934401000119101/atoms/preferred",
            "name": "Closed fracture of navicular bone of left wrist"
        },
        {
            "classType": "SourceAtomCluster",
            "ui": "208375001",
            "suppressible": false,
            "obsolete": false,
            "rootSource": "SNOMEDCT_US",
            "atomCount": 2,
            "cVMemberCount": 0,
            "attributes": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/208375001/attributes",
            "atoms": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/208375001/atoms",
            "descendants": "NONE",
            "ancestors": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/208375001/ancestors",
            "parents": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/208375001/parents",
            "children": "NONE",
            "relations": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/208375001/relations",
            "definitions": "NONE",
            "concepts": "https://uts-ws.nlm.nih.gov/rest/search/2015AB?string=208375001&sabs=SNOMEDCT_US&searchType=exact&inputType=sourceUi",
            "defaultPreferredAtom": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/208375001/atoms/preferred",
            "name": "Closed fracture carpal bones, multiple"
        }
    ]
}
~~~~


