title=Retrieving atoms in the UMLS
date=2015-06-12
type=page
status=published
~~~~~~


**API Version:** 0.1 alpha

[URIs](#uris) | [Query Parameters](#parameters) | [Sample Output](#samples)

URIs with /atoms support the following use cases

*  Retrieve atoms of a UMLS concept (CUI).
*  Retrieve atoms of a source-asserted identifier or code.
*  Retrieve atom information, such as relations to other atoms, attributes, or definitions.
*  Retrieve membership information of an atom (to which CUI, code, or content view does an atom belong).
*  Retrieve atom information such as term type, language, and restriction level

Note that 'current' in the URI can always be used to search against the latest UMLS publication.
You may use any valid UMLS release back to 2008AA in your URI if you would like to search against a particular version of the UMLS.


<a name = "uris"></a>
### URIs

*The base URI is https://uts-ws.nlm.nih.gov/rest*

Type of call|Sample URI|Description
--- | --- | ---
GET|/content/current/CUI/C0155502/atoms/|Retrieves all atoms for C0155502
GET|/content/current/CUI/C3853540/atoms/?sabs=SNOMEDCT_US,ICD9CM&ttys=PT | Retrieve SNOMEDCT_US and ICD9CM preferred terms in C3853540.

<a name = "parameters"></a>
### Available query parameters in /atoms

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
ticket | Y | A single-use service ticket is required for each call to the API. See [authentication](authentication.html) for more information | n/a | n/a | n/a
sabs| N | One or more source abbreviations | Any root source abbreviation in the UMLS |n/a| Use a comma between each source abbreviation to specify more than one.
ttys | N | One or more term types | Any valid term type in the UMLS | n/a| Use a comma between each [term type](http://www.nlm.nih.gov/research/umls/knowledge_sources/metathesaurus/release/precedence_suppressibility.html) to specify more than one.
-obsolete | N |  Include content that is obsolete according to the content provider | true or false | false | n/a
-suppressible | N |  Include content that is suppressible according to NLM Editors| true or false | false | n/a
page | N | Whole number that specifies which page of results to fetch. | 1,2,3, etc | 1 | n/a
pageSize | N | Whole number that specifies the number of results to include per page. | 1,2,3, etc | 25 | n/a

-not yet implemented

<a name = "samples"></a>
### Sample Output

Calls under /atoms will return JSON objects of classType='Atom'.

**The default for calls under /atom is to return Atom Information.**

~~~~json
[
    {
        "name": "Benign paroxysmal positional vertigo",
        "attributes": "NONE",
        "children": null,
        "memberships": {
            "code": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/ICD9CM/386.11",
            "concept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/CUI/C0155502/",
            "sourceDescriptor": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/ICD9CM/386.11/"
        },
        "relations": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/AUI/A8345234/relations/",
        "parents": null,
        "definitions": "NONE",
        "termType": "PT",
        "obsolete": false,
        "rootSource": "ICD9CM",
        "suppressible": false,
        "ui": "A8345234",
        "classType": "Atom"
    },
    {
        "name": "Benign paroxysmal positional vertigo",
        "attributes": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/AUI/A2892933/attributes/",
        "children": null,
        "memberships": {
            "code": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/111541001",
            "concept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/CUI/C0155502/",
            "sourceConcept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/111541001/"
        },
        "relations": "NONE",
        "parents": null,
        "definitions": "NONE",
        "termType": "PT",
        "obsolete": false,
        "rootSource": "SNOMEDCT_US",
        "suppressible": false,
        "ui": "A2892933",
        "classType": "Atom"
    },
    {
        "name": "Benign recurrent vertigo",
        "attributes": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/AUI/A3101021/attributes/",
        "children": null,
        "memberships": {
            "code": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/232285008",
            "concept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/CUI/C0155502/",
            "sourceConcept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/232285008/"
        },
        "relations": "NONE",
        "parents": null,
        "definitions": "NONE",
        "termType": "PT",
        "obsolete": false,
        "rootSource": "SNOMEDCT_US",
        "suppressible": false,
        "ui": "A3101021",
        "classType": "Atom"
    }
]
~~~~

