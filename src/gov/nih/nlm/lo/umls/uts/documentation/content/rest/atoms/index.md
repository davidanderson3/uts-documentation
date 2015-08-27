title=Retrieving UMLS Atoms
date=2015-06-12
updated=2015-08-28
type=page
status=published
category=Retrieving UMLS Concepts
navorder=2
~~~~~~


[URIs](#uris) | [Query Parameters](#query-parameters) | [Sample Output](#sample-output)

URIs with /atoms support the following use cases:

*  Retrieve atoms of a UMLS concept (CUI).
*  Retrieve atoms of a source-asserted identifier or code.
*  Retrieve atom information, such as relations to other atoms, attributes, or definitions.
*  Retrieve membership information of an atom (to which CUI, code, or content view does an atom belong).
*  Retrieve atom information such as term type, language, and restriction level

Note that 'current' in the URI can always be used to search against the latest UMLS publication.
You may use any valid UMLS release back to 2008AA in your URI if you would like to search against a particular version of the UMLS.


### URIs

**The base URI is https://uts-ws.nlm.nih.gov/rest**

Type of call|Sample URI|Description
--- | --- | ---
GET|/content/current/CUI/C0155502/atoms|Retrieves all atoms for C0155502
GET|/content/current/CUI/C0155502/atoms?language=ENG|Retrieves all English language atoms for C0155502
GET|/content/current/CUI/C0155502/atoms?sabs=SNOMEDCT_US,ICD9CM&ttys=PT | Retrieve SNOMEDCT_US and ICD9CM preferred terms in C0155502
GET|/content/current/source/SNOMEDCT_US/111541001/atoms | Retrieve atoms belonging to SNOMED CT concept 111541001


### Query Parameters

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
ticket | Y | A single-use service ticket is required for each call to the API. See [authentication](../authentication.html) for more information | n/a | n/a | n/a
sabs| N | One or more source abbreviations | Any [root source abbreviation](http://www.nlm.nih.gov/research/umls/knowledge_sources/metathesaurus/release/source_vocabularies.html) in the UMLS |n/a| Use a comma between each source abbreviation to specify more than one.
ttys | N | One or more term types | Any valid [term type](http://www.nlm.nih.gov/research/umls/knowledge_sources/metathesaurus/release/precedence_suppressibility.html) in the UMLS | n/a| Use a comma between each term type to specify more than one.
language | N | Retrieve only atoms that have a specific language | Any 3 letter language abbreviation in the UMLS, such as "ENG","FRE","SPA","GER","DUT","JPN", etc | All languages are returned by default | Currently filtering by one language is supported.
includeObsolete | N |  Include content that is obsolete according to the content provider or NLM. | true or false | false | n/a
includeSuppressible | N |  Include content that is suppressible according to NLM Editors .| true or false | false | n/a
pageNumber | N | Whole number that specifies which page of results to fetch. | 1,2,3, etc | 1 | n/a
pageSize | N | Whole number that specifies the number of results to include per page. | 1,2,3, etc | 25 | n/a


### Sample Output

**Calls under /atoms will return JSON objects of classType='Atom'.**

Sample output for /content/current/CUI/C0155502/atoms?ttys=PT&sabs=SNOMEDCT_US%2CICD9CM&ticket=ST...

~~~~json
{
    "result": [
        {
            "classType": "Atom",
            "ui": "A8345234",
            "suppressible": false,
            "obsolete": false,
            "rootSource": "ICD9CM",
            "termType": "PT",
            "memberships": {
                "code": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/ICD9CM/386.11",
                "concept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/CUI/C0155502",
                "sourceDescriptor": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/ICD9CM/386.11"
            },
            "attributes": "NONE",
            "parents": "NONE",
            "children": "NONE",
            "relations": "NONE",
            "definitions": "NONE",
            "name": "Benign paroxysmal positional vertigo",
            "language": "ENG"
        },
        {
            "classType": "Atom",
            "ui": "A2892933",
            "suppressible": false,
            "obsolete": false,
            "rootSource": "SNOMEDCT_US",
            "termType": "PT",
            "memberships": {
                "code": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/111541001",
                "concept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/CUI/C0155502",
                "sourceConcept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/111541001"
            },
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
            "ui": "A3101021",
            "suppressible": false,
            "obsolete": false,
            "rootSource": "SNOMEDCT_US",
            "termType": "PT",
            "memberships": {
                "code": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/232285008",
                "concept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/CUI/C0155502",
                "sourceConcept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/232285008"
            },
            "attributes": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/AUI/A3101021/attributes",
            "parents": "NONE",
            "children": "NONE",
            "relations": "NONE",
            "definitions": "NONE",
            "name": "Benign recurrent vertigo",
            "language": "ENG"
        }
    ],
    "pageNumber": 1,
    "pageSize": 25,
    "pageCount": 1
}
~~~~

