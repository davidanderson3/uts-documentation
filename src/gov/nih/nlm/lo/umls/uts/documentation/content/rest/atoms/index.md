title=Retrieving UMLS Atoms
date=2015-06-12
updated=2016-01-08
type=page
status=published
category=Retrieving UMLS Data
navorder=4
~~~~~~


[URIs](#uris) | [Query Parameters](#query-parameters) | [Sample Output](#sample-output)

URIs with /atoms support the following use cases:

*  Retrieve all atoms of a UMLS concept (CUI) or source-asserted identifier.
*  Retrieve the default preferred atom of a UMLS CUI or source-asserted identifier.
*  Retrieve information about an individual atom (AUI).
*  Retrieve atom information, such as relations to other atoms, attributes, or definitions.
*  Retrieve membership information of an atom (to which CUI, code, or content view does an atom belong).
*  Retrieve atom information such as name,term type, language, and suppressibility/obsolescence.

Note that 'current' in the URI can always be used to search against the latest UMLS publication.
You may use any valid UMLS release back to 2008AA in your URI if you would like to search against a particular version of the UMLS.


### URIs

**The base URI is https://uts-ws.nlm.nih.gov/rest**

Type of call|Sample URI|Description|Returned JSON Object classType
--- | --- | ---
GET|/content/current/CUI/C0155502/atoms|Retrieves all atoms for C0155502 | Atom
GET|/content/current/CUI/C0155502/atoms/preferred|Retrieves the default preferred atom of C0155502 | Atom
GET|/content/current/CUI/C0155502/atoms?language=ENG|Retrieves all English language atoms for C0155502| Atom
GET|/content/current/CUI/C0155502/atoms?sabs=SNOMEDCT_US,ICD9CM&ttys=PT | Retrieve SNOMEDCT_US and ICD9CM preferred terms in C0155502| Atom
GET|/content/current/source/SNOMEDCT_US/111541001/atoms | Retrieve atoms belonging to SNOMED CT concept 111541001| Atom
GET|/content/current/source/SNOMEDCT_US/111541001/atoms/preferred | Retrieve the default preferred atom belonging to SNOMED CT concept 111541001| Atom
GET|/content/current/AUI/A8345234 | Retrieve information about AUI A8345234| Atom


### Query Parameters

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
ticket | Y | A single-use service ticket is required for each call to the API. See [authentication](../authentication.html) for more information | n/a | n/a | n/a
sabs| N | One or more source abbreviations | Any [root source abbreviation](https://www.nlm.nih.gov/research/umls/sourcereleasedocs/index.html) in the UMLS |n/a| Use a comma between each source abbreviation to specify more than one.
ttys | N | One or more term types | Any valid [term type](https://www.nlm.nih.gov/research/umls/knowledge_sources/metathesaurus/release/abbreviations.html#TTYC) in the UMLS | n/a| Use a comma between each term type to specify more than one.
language | N | Retrieve only atoms that have a specific language | Any 3 letter language abbreviation in the UMLS, such as "ENG","FRE","SPA","GER","DUT","JPN", etc | All languages are returned by default | Currently filtering by one language is supported.
includeObsolete | N |  Include content that is obsolete according to the content provider or NLM. | true or false | false | n/a
includeSuppressible | N |  Include content that is suppressible according to NLM Editors .| true or false | false | n/a
pageNumber | N | Whole number that specifies which page of results to fetch. | 1,2,3, etc | 1 | n/a
pageSize | N | Whole number that specifies the number of results to include per page. | 1,2,3, etc | 25 | n/a


### Sample Output

Sample output for /content/current/CUI/C0155502/atoms?ttys=PT&sabs=SNOMEDCT_US%2CICD9CM&ticket=ST...

~~~~json
{
    "pageSize": 25,
    "pageNumber": 1,
    "pageCount": 1,
    "result": [
        {
            "classType": "Atom",
            "ui": "A2994854",
            "suppressible": "false",
            "obsolete": "false",
            "rootSource": "SNOMEDCT_US",
            "termType": "SY",
            "code": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/111541001",
            "concept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/CUI/C0155502",
            "sourceConcept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/111541001",
            "sourceDescriptor": "NONE",
            "attributes": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/AUI/A2994854/attributes",
            "parents": "NONE",
            "children": "NONE",
            "relations": "NONE",
            "definitions": "NONE",
            "name": "BPPV - Benign paroxysmal positional vertigo",
            "language": "ENG"
        },
        {
            "classType": "Atom",
            "ui": "A2955676",
            "suppressible": "false",
            "obsolete": "false",
            "rootSource": "SNOMEDCT_US",
            "termType": "SY",
            "code": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/111541001",
            "concept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/CUI/C0155502",
            "sourceConcept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/111541001",
            "sourceDescriptor": "NONE",
            "attributes": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/AUI/A2955676/attributes",
            "parents": "NONE",
            "children": "NONE",
            "relations": "NONE",
            "definitions": "NONE",
            "name": "Benign paroxysmal positional nystagmus",
            "language": "ENG"
        },
        {
            "classType": "Atom",
            "ui": "A2892933",
            "suppressible": "false",
            "obsolete": "false",
            "rootSource": "SNOMEDCT_US",
            "termType": "PT",
            "code": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/111541001",
            "concept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/CUI/C0155502",
            "sourceConcept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/111541001",
            "sourceDescriptor": "NONE",
            "attributes": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/AUI/A2892933/attributes",
            "parents": "NONE",
            "children": "NONE",
            "relations": "NONE",
            "definitions": "NONE",
            "name": "Benign paroxysmal positional vertigo",
            "language": "ENG"
        },
        {
            "classType": "Atom",
            "ui": "A3808177",
            "suppressible": "false",
            "obsolete": "false",
            "rootSource": "SNOMEDCT_US",
            "termType": "FN",
            "code": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/111541001",
            "concept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/CUI/C0155502",
            "sourceConcept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/111541001",
            "sourceDescriptor": "NONE",
            "attributes": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/AUI/A3808177/attributes",
            "parents": "NONE",
            "children": "NONE",
            "relations": "NONE",
            "definitions": "NONE",
            "name": "Benign paroxysmal positional vertigo (disorder)",
            "language": "ENG"
        },
        {
            "classType": "Atom",
            "ui": "A3101021",
            "suppressible": "false",
            "obsolete": "false",
            "rootSource": "SNOMEDCT_US",
            "termType": "PT",
            "code": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/232285008",
            "concept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/CUI/C0155502",
            "sourceConcept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/232285008",
            "sourceDescriptor": "NONE",
            "attributes": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/AUI/A3101021/attributes",
            "parents": "NONE",
            "children": "NONE",
            "relations": "NONE",
            "definitions": "NONE",
            "name": "Benign recurrent vertigo",
            "language": "ENG"
        },
        {
            "classType": "Atom",
            "ui": "A3808204",
            "suppressible": "false",
            "obsolete": "false",
            "rootSource": "SNOMEDCT_US",
            "termType": "FN",
            "code": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/232285008",
            "concept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/CUI/C0155502",
            "sourceConcept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/232285008",
            "sourceDescriptor": "NONE",
            "attributes": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/AUI/A3808204/attributes",
            "parents": "NONE",
            "children": "NONE",
            "relations": "NONE",
            "definitions": "NONE",
            "name": "Benign recurrent vertigo (disorder)",
            "language": "ENG"
        }
    ]
}
~~~~

