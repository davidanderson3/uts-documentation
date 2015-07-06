title=Retrieving source asserted information in the UMLS
date=2015-07-01
updated=2015-07-06
type=page
status=published
~~~~~~


**API Version:** 0.2 alpha

[URIs](#uris) | [Query Parameters](#parameters) | [Sample Output](#samples)

URIs with /Source Asserted Identifier support the following use cases:

*  Retrieve information (name, attributes, term types, number of atoms, memberships etc) for a known 'Source Asserted Identifier' like source concept, source descriptor or code from latest UMLS version or a specific release.
*  Retrieve atoms for a known source asserted identifier.
*  Retrieve all parents of a known source asserted identifier.
*  Retrieve all children of a known source asserted identifier.

Note that 'current' in the URI can always be used to search against the latest UMLS publication.
You may use any valid UMLS release back to 2008AA in your URI if you would like to search against a particular version of the UMLS.


<a name = "uris"></a>
### URIs

*The base URI is https://uts-ws.nlm.nih.gov/rest*

Sample URI|Description
--- | ---
/content/current/source/SNOMEDCT_US/9468002| Retrieves Source Concept
/content/current/source/CSP/1250-9110| Retrieves Source Descriptor
/content/current/source/UMD/27-742| Retrieves Code
[/content/current/source/SNOMEDCT_US/226617008/atoms](../atoms/index.html)| Retrieve atoms in a CUI
[/content/current/source/SNOMEDCT_US/226617008/parents](../parents-and-children/index.html) | Retrieve Source Asserted Identifier parents
[/content/current/source/SNOMEDCT_US/226617008/children](../parents-and-children/index.html) | Retrieve Source Asserted Identifier children


<a name = "parameters"></a>
### Available query parameters in /Source Asserted Identifier

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
ticket | Y | A single-use service ticket is required for each call to the API. See [authentication](../authentication.html) for more information | n/a | n/a | n/a
sabs| N | One or more source abbreviations | Any root source abbreviation in the UMLS |n/a| Use a comma between each source abbreviation to specify more than one.


<a name = "samples"></a>
### Sample Output


**The default for calls under /source/{Source Asserted Identifier} is to return information on the Source Asserted Identifier.**

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
        "defintions": "NONE",
        "memberships": null,
        "name": "Closed fracture carpal bone"
    },
    "pageNum": 0,
    "pageSize": 0

}
~~~~
