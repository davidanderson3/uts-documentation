title=Retrieving UMLS Atom Parents and Children
date=2016-02-24
updated=2016-02-24
type=page
status=published
category=Retrieving UMLS Data
navorder=5
~~~~~~


[URIs](#uris) | [Query Parameters](#query-parameters) | [Sample Output](#sample-output)

URIs with /parents or /children support the following use cases:

*  Retrieve the immediate parents of a known source asserted identifier.
*  Retrieve all immediate children of a known source asserted identifier.

Note that 'current' in the URI can always be used to search against the latest UMLS publication.
You may use any valid UMLS release back to 2008AA in your URI if you would like to search against a particular version of the UMLS.


### URIs

**The base URI is https://uts-ws.nlm.nih.gov/rest**

Sample URI|Description|Returned JSON Object classType
--- | ---
/content/current/source/SNOMEDCT_US/9468002/parents| Retrieves parents a source-asserted identifier|SourceAtomCluster*
/content/current/source/SNOMEDCT_US/9468002/children| Retrieves children of a source-asserted identifier|SourceAtomCluster*

*Calls using codes from HL7V2.5 and HL7V3.0 return output with an "Atom" JSON Object classType.

### Query Parameters

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
ticket | Y | A single-use service ticket is required for each call to the API. See [authentication](../authentication.html) for more information | n/a | n/a | n/a
pageNumber | N | Whole number that specifies which page of results to fetch. | 1,2,3, etc | 1 | n/a
pageSize | N | Whole number that specifies the number of results to include per page. | 1,2,3, etc | 25 | n/a


### Sample Output

Sample output for /content/current/source/SNOMEDCT_US/9468002/parents?ticket=ST...

~~~~json
{
    "pageSize": 25,
    "pageNumber": 1,
    "pageCount": 1,
    "result": [
        {
            "classType": "SourceAtomCluster",
            "ui": "20511007",
            "suppressible": false,
            "obsolete": false,
            "rootSource": "SNOMEDCT_US",
            "atomCount": 6,
            "cVMemberCount": 0,
            "attributes": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/20511007/attributes",
            "atoms": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/20511007/atoms",
            "descendants": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/20511007/descendants",
            "ancestors": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/20511007/ancestors",
            "parents": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/20511007/parents",
            "children": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/20511007/children",
            "relations": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/20511007/relations",
            "definitions": "NONE",
            "concepts": "https://uts-ws.nlm.nih.gov/rest/search/2015AB?string=20511007&sabs=SNOMEDCT_US&searchType=exact&inputType=sourceUi",
            "defaultPreferredAtom": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/20511007/atoms/preferred",
            "name": "Fracture of hand"
        },
        {
            "classType": "SourceAtomCluster",
            "ui": "36991002",
            "suppressible": false,
            "obsolete": false,
            "rootSource": "SNOMEDCT_US",
            "atomCount": 5,
            "cVMemberCount": 0,
            "attributes": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/36991002/attributes",
            "atoms": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/36991002/atoms",
            "descendants": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/36991002/descendants",
            "ancestors": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/36991002/ancestors",
            "parents": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/36991002/parents",
            "children": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/36991002/children",
            "relations": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/36991002/relations",
            "definitions": "NONE",
            "concepts": "https://uts-ws.nlm.nih.gov/rest/search/2015AB?string=36991002&sabs=SNOMEDCT_US&searchType=exact&inputType=sourceUi",
            "defaultPreferredAtom": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/36991002/atoms/preferred",
            "name": "Closed fracture of upper limb"
        },
        {
            "classType": "SourceAtomCluster",
            "ui": "82065001",
            "suppressible": false,
            "obsolete": false,
            "rootSource": "SNOMEDCT_US",
            "atomCount": 7,
            "cVMemberCount": 0,
            "attributes": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/82065001/attributes",
            "atoms": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/82065001/atoms",
            "descendants": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/82065001/descendants",
            "ancestors": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/82065001/ancestors",
            "parents": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/82065001/parents",
            "children": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/82065001/children",
            "relations": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/82065001/relations",
            "definitions": "NONE",
            "concepts": "https://uts-ws.nlm.nih.gov/rest/search/2015AB?string=82065001&sabs=SNOMEDCT_US&searchType=exact&inputType=sourceUi",
            "defaultPreferredAtom": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/82065001/atoms/preferred",
            "name": "Fracture of carpal bone"
        }
    ]
}
~~~~


