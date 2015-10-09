title=Retrieving Source-Asserted Information
date=2015-07-01
updated=2015-10-09
type=page
status=published
category=Retrieving Source-Asserted Data
navorder=1
~~~~~~


[URIs](#uris) | [Query Parameters](#query-parameters) | [Sample Output](#sample-output)

URIs with /source/{source}/{id} support the following use cases:

*  Retrieve information (name, attributes, term types, number of atoms, memberships etc) for a source concept, source descriptor or code from latest UMLS version or a specific release.
*  Retrieve atoms for a known source-asserted identifier.
*  Retrieve immediate parents of a known source-asserted identifier.
*  Retrieve immediate children of a known source-asserted identifier.

Note that 'current' in the URI can always be used to search against the latest UMLS publication.
You may use any valid UMLS release back to 2008AA in your URI if you would like to search against a particular version of the UMLS.

### URIs

**The base URI is https://uts-ws.nlm.nih.gov/rest**

Sample URI|Description|Returned JSON Object classType
--- | ---
/content/current/source/SNOMEDCT_US/9468002 | Retrieves Source Concept | SourceAtomCluster
/content/current/source/MSH/D015242 | Retrieves Source Descriptor | SourceAtomCluster
/content/current/source/LNC/54112-8 | Retrieves Code | SourceAtomCluster
[/content/current/source/SNOMEDCT_US/9468002/atoms](../atoms/index.html)| Retrieve atoms in a source-asserted identifier | SourceAtomCluster
[/content/current/source/SNOMEDCT_US/9468002/parents](../parents-and-children/index.html) | Retrieve immediate parents of a source-asserted identifier | SourceAtomCluster
[/content/current/source/SNOMEDCT_US/9468002/children](../parents-and-children/index.html) | Retrieve immediate children of source-asserted identifier | SourceAtomCluster
[/content/current/source/SNOMEDCT_US/9468002/ancestors](../ancestors-and-descendants/index.html) | Retrieve all ancestors of a source-asserted identifier | SourceAtomCluster
[/content/current/source/SNOMEDCT_US/9468002/descendants](../ancestors-and-descendants/index.html) | Retrieve all descendants of source-asserted identifier | SourceAtomCluster


### Query Parameters

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
ticket | Y | A single-use service ticket is required for each call to the API. See [authentication](../authentication.html) for more information | n/a | n/a | n/a
pageNumber | N | Whole number that specifies which page of results to fetch. | 1,2,3, etc | 1 | n/a
pageSize | N | Whole number that specifies the number of results to include per page. | 1,2,3, etc | 25 | n/a


### Sample Output

Sample output for /content/current/source/SNOMEDCT_US/9468002?ticket=ST...

~~~~json
{
    "pageSize": 25,
    "pageNumber": 1,
    "pageCount": 1,
    "result": {
        "classType": "SourceAtomCluster",
        "ui": "9468002",
        "suppressible": false,
        "sourceUi": "9468002",
        "obsolete": false,
        "rootSource": "SNOMEDCT_US",
        "atomCount": 6,
        "cVMemberCount": 0,
        "attributes": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/9468002/attributes",
        "atoms": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/9468002/atoms",
        "descendants": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/9468002/descendants",
        "ancestors": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/9468002/ancestors",
        "parents": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/9468002/parents",
        "children": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/9468002/children",
        "relations": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/9468002/relations",
        "definitions": "NONE",
        "name": "Closed fracture carpal bone"
    }
}
~~~~
