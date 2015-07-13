title=Retrieving source asserted data
date=2015-07-01
updated=2015-07-06
type=page
status=published
category=Source-asserted data
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

Sample URI|Description
--- | ---
/content/current/source/SNOMEDCT_US/9468002| Retrieves Source Concept
/content/current/source/CSP/1250-9110| Retrieves Source Descriptor
/content/current/source/UMD/27-742| Retrieves Code
[/content/current/source/SNOMEDCT_US/226617008/atoms](../atoms/index.html)| Retrieve atoms in a source-asserted identifier
[/content/current/source/SNOMEDCT_US/226617008/parents](../parents-and-children/index.html) | Retrieve immediate parents of a source-asserted identifier
[/content/current/source/SNOMEDCT_US/226617008/children](../parents-and-children/index.html) | Retrieve immediate children of source-asserted identifier


### Query Parameters

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
ticket | Y | A single-use service ticket is required for each call to the API. See [authentication](../authentication.html) for more information | n/a | n/a | n/a


### Sample Output


**Calls using /source/{source}/{id} will return a JSON object with a classType of 'SourceAtomCluster'.**

~~~~json
{
    "result": {
        "classType": "SourceAtomCluster",
        "ui": "9468002",
        "suppressible": false,
        "sourceUi": "9468002",
        "obsolete": false,
        "rootSource": "SNOMEDCT_US",
        "atomCount": 6,
        "cVMemberCount": 0,
        "attributes": "https://uts-ws-qa.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/9468002/attributes",
        "atoms": "https://uts-ws-qa.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/9468002/atoms",
        "parents": "https://uts-ws-qa.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/9468002/parents",
        "children": "https://uts-ws-qa.nlm.nih.gov/rest/content/2015AA/SNOMEDCT_US/9468002/children",
        "relations": "NONE",
        "definitions": "NONE",
        "memberships": null,
        "name": "Closed fracture carpal bone"
    },
    "pageNum": 1,
    "pageSize": 25
}
~~~~
