title=Retrieving concept information in the UMLS
date=2015-06-12
updated=2015-06-25
type=page
status=published
~~~~~~


**API Version:** 0.1 alpha

[URIs](#uris) | [Query Parameters](#parameters) | [Sample Output](#samples)

URIs with /concept/{CUI} support the following use cases:

*  Retrieve information (name, semantic types, number of atoms, etc) for a known CUI from latest UMLS version or a specific release.
*  Retrieve atoms for a known CUI.
*  Retrieve all definitions of a known CUI.
*  Retrieve relationships to other CUIs (broader/narrower).

Note that 'current' in the URI can always be used to search against the latest UMLS publication.
You may use any valid UMLS release back to 2008AA in your URI if you would like to search against a particular version of the UMLS.


<a name = "uris"></a>
### URIs

*The base URI is https://uts-ws.nlm.nih.gov/rest*

Sample URI|Description
--- | ---
[/content/current/CUI/C0009044](#samples.html)| Retrieves CUI
[/content/current/CUI/C0009044/atoms](../atoms/index.html) | Retrieve atoms in a CUI
/content/current/CUI/C0009044/definitions | Retrieve CUI definitions
/content/current/CUI/C0009044/relations | Retrieve CUI relations


<a name = "parameters"></a>
### Available query parameters in /concept/{CUI}

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
ticket | Y | A single-use service ticket is required for each call to the API. See [authentication](../authentication.html) for more information | n/a | n/a | n/a
page | N | Whole number that specifies which page of results to fetch. | 1,2,3, etc | 1 | n/a
pageSize | N | Whole number that specifies the number of results to include per page. | 1,2,3, etc | 25 | n/a

<a name = "samples"></a>
### Sample Output


**The default for calls under /concept/{CUI} is to return UMLS CUIs.**

~~~~json
{
    "result": {
        "classType": "Concept",
        "ui": "C0009044",
        "suppressible": false,
        "dateAdded": "09-30-1990",
        "majorRevisionDate": "07-04-2012",
        "status": "R",
        "semanticTypes": [
            "T037"
        ],
        "atomCount": 63,
        "attributeCount": 0,
        "cvMemberCount": 0,
        "atoms": "https://uts-ws-qa.nlm.nih.gov/rest/content/2015AA/CUI/C0009044/atoms",
        "definitions": "NONE",
        "relations": "https://uts-ws-qa.nlm.nih.gov/rest/content/2015AACUI/C0009044/relations",
        "relationCount": 5,
        "name": "Closed fracture carpal bone"
    },
    "pageNum": 0,
    "pageSize": 0
}
~~~~
