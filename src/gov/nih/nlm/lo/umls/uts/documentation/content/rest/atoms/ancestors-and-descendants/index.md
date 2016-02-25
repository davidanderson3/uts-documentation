title=Retrieving UMLS Atom Ancestors and Descendants
date=2016-02-25
updated=2016-02-25
type=page
status=published
category=Retrieving UMLS Data
navorder=6
~~~~~~


[URIs](#uris) | [Query Parameters](#query-parameters) | [Sample Output](#sample-output)

URIs with /ancestors or /descendants support the following use cases:

*  Retrieve all ancestors of a known UMLS atom.
*  Retrieve all descendants of a known UMLS atom.

Note that 'current' in the URI can always be used to search against the latest UMLS publication.
You may use any valid UMLS release back to 2008AA in your URI if you would like to search against a particular version of the UMLS.


### URIs

**The base URI is https://uts-ws.nlm.nih.gov/rest**

Sample URI|Description|Returned JSON Object classType
--- | ---
/content/current/AUI/A10134087/ancestors|Retrieves ancestors of a UMLS atom|Atom
/content/current/AUI/A10134087/descendants|Retrieves descendants of a UMLS atom|Atom


### Query Parameters

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
ticket | Y | A single-use service ticket is required for each call to the API. See [authentication](../authentication.html) for more information | n/a | n/a | n/a
pageNumber | N | Whole number that specifies which page of results to fetch. | 1,2,3, etc | 1 | n/a
pageSize | N | Whole number that specifies the number of results to include per page. | 1,2,3, etc | 25 | n/a


### Sample Output

Sample output for /content/current/AUI/A10134087/descendants?ticket=ST...

~~~~json
{
    "pageSize": 25,
    "pageNumber": 1,
    "pageCount": 15,
    "result": [
        {
            "classType": "Atom",
            "ui": "A10133773",
            "suppressible": "false",
            "obsolete": "false",
            "rootSource": "HL7V3.0",
            "termType": "PT",
            "code": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/HL7V3.0/_IntrabursalRoute",
            "concept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/CUI/C1522205",
            "sourceConcept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/HL7V3.0/21172",
            "sourceDescriptor": "NONE",
            "attributes": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/AUI/A10133773/attributes",
            "parents": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/AUI/A10133773/parents",
            "ancestors": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/AUI/A10133773/ancestors",
            "children": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/AUI/A10133773/children",
            "descendants": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/AUI/A10133773/descendants",
            "relations": "NONE",
            "definitions": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/AUI/A10133773/definitions",
            "name": "IntrabursalRoute",
            "language": "ENG"
        },
        {
            "classType": "Atom",
            "ui": "A8317632",
            "suppressible": "false",
            "obsolete": "false",
            "rootSource": "HL7V3.0",
            "termType": "PT",
            "code": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/HL7V3.0/IBURSINJ",
            "concept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/CUI/C0848586",
            "sourceConcept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/HL7V3.0/14643",
            "sourceDescriptor": "NONE",
            "attributes": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/AUI/A8317632/attributes",
            "parents": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/AUI/A8317632/parents",
            "ancestors": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/AUI/A8317632/ancestors",
            "children": "NONE",
            "descendants": null,
            "relations": "NONE",
            "definitions": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/AUI/A8317632/definitions",
            "name": "Injection, intrabursal",
            "language": "ENG"
        },
...
    ]
}
~~~~


