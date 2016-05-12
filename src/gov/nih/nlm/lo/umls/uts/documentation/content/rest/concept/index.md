title=Retrieving UMLS Concept Information
date=2015-06-12
updated=2015-12-21
type=page
status=published
category=Retrieving UMLS Data
navorder=1
~~~~~~


[URIs](#uris) | [Query Parameters](#query-parameters) | [Sample Output](#sample-output)

URIs with /CUI support the following use cases:

*  Retrieve information (name, semantic types, number of atoms, etc) for a known CUI from latest UMLS version or a specific release.
*  Retrieve atoms for a known CUI.
*  Retrieve all definitions of a known CUI.
*  Retrieve relationships to other CUIs (broader/narrower).

Note that 'current' in the URI can always be used to search against the latest UMLS publication.
You may use any valid UMLS release back to 2008AA in your URI if you would like to search against a particular version of the UMLS.


### URIs

**The base URI is https://uts-ws.nlm.nih.gov/rest**

Sample URI|Description|Returned JSON Object classType
--- | ---
[/content/current/CUI/C0009044](#sample-output)| Retrieves CUI | Concept
[/content/current/CUI/C0009044/atoms](../atoms/index.html) | Retrieve atoms in a CUI | Atom
[/content/current/CUI/C0009044/definitions](../definitions/index.html) | Retrieve CUI definitions | Definition
[/content/current/CUI/C0009044/relations](../relations/index.html) | Retrieve CUI relations | ConceptRelation

### Query Parameters

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
ticket | Y | A single-use service ticket is required for each call to the API. See [authentication](../authentication.html) for more information | n/a | n/a | n/a

### Sample Output

**The default for calls under /CUI/{CUI} is to return UMLS CUIs.**

Sample output for /content/current/CUI/C0009044?ticket=ST...

~~~~json
{
    "pageSize": 25,
    "pageNumber": 1,
    "pageCount": 1,
    "result": {
        "classType": "Concept",
        "ui": "C0009044",
        "suppressible": false,
        "dateAdded": "09-30-1990",
        "majorRevisionDate": "08-18-2015",
        "status": "R",
        "semanticTypes": [
            {
                "name": "Injury or Poisoning",
                "uri": "https://uts-ws.nlm.nih.gov/rest/semantic-network/2015AB/TUI/T037"
            }
        ],
        "atomCount": 63,
        "attributeCount": 0,
        "cvMemberCount": 0,
        "atoms": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/CUI/C0009044/atoms",
        "definitions": "NONE",
        "relations": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/CUI/C0009044/relations",
        "defaultPreferredAtom": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/CUI/C0009044/atoms/preferred",
        "relationCount": 5,
        "name": "Closed fracture carpal bone"
    }
}
~~~~
