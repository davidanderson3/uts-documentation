title=Retrieving UMLS Concept Relations
date=2015-07-28
updated=2015-09-30
type=page
status=published
category=Retrieving UMLS Data
navorder=4
~~~~~~


[URIs](#uris) | [Query Parameters](#query-parameters) | [Sample Output](#sample-output)

URIs with /relations support the following use cases:

*  Retrieve all relationships associated with a known CUI
*  Retrieve the NLM-asserted relationships for a known CUI.

**NLM does not assert parent or child relationships between concepts.**

Note that 'current' in the URI can always be used to search against the latest UMLS publication.
You may use any valid UMLS release back to 2008AA in your URI if you would like to search against a particular version of the UMLS.


### URIs

**The base URI is https://uts-ws.nlm.nih.gov/rest**

Sample URI|Description|Returned JSON Object classType
--- | ---
/content/current/CUI/C0009044/relations | Retrieves all relationships associated with the CUI | ConceptRelation, AtomClusterRelation, AtomRelation
/content/current/CUI/C0009044/relations?sabs=MTH | Retrieves NLM-asserted relationships of the CUI | ConceptRelation



### Query Parameters

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
apiKey | Y | An API key is required for each call to the API. Visit [your UTS profile](https://uts.nlm.nih.gov/uts/profile) to obtain your API key. | n/a | n/a | n/a
includeRelationLabels | N | One or more relation labels | Any [relation label](https://www.nlm.nih.gov/research/umls/knowledge_sources/metathesaurus/release/abbreviations.html#REL) in the UMLS |n/a| Use a comma between each relation label to specify more than one.
includeAdditionalRelationLabels | N | One or more relation attribute | Any [relation attribute](https://www.nlm.nih.gov/research/umls/knowledge_sources/metathesaurus/release/abbreviations.html#RELA) in the UMLS |n/a| Use a comma between each relation attribute to specify more than one.
includeObsolete | N |  Include content that is obsolete according to the content provider or NLM. | true or false | false | n/a
includeSuppressible | N |  Include content that is suppressible according to NLM Editors.| true or false | false | n/a
sabs | N | Comma-separated list of source vocabularies to include in your search | Any root source abbreviation in the UMLS. See the "Abbreviation" column for a list of [UMLS source vocabulary abbreviations](https://www.nlm.nih.gov/research/umls/sourcereleasedocs/).  | All UMLS source vocabularies | Use a comma between each source abbreviation to specify more than one.
pageNumber | N | Whole number that specifies which page of results to fetch. | 1,2,3, etc | 1 | n/a
pageSize | N | Whole number that specifies the number of results to include per page. | 1,2,3, etc | 25 | n/a



### Sample Output

Sample output for https://uts-ws.nlm.nih.gov/rest/content/current/CUI/C0009044/relations?apiKey=YOUR_APIKEY...

~~~~json
{
  "pageSize": 25,
  "pageNumber": 1,
  "pageCount": 10,
  "result": [
    {
      "ui": "R162928707",
      "suppressible": false,
      "sourceUi": "780251000124125",
      "obsolete": false,
      "sourceOriginated": false,
      "rootSource": "SNOMEDCT_US",
      "groupId": "0",
      "attributeCount": 0,
      "classType": "AtomClusterRelation",
      "relatedFromId": "https://uts-ws.nlm.nih.gov/rest/content/2022AA/source/SNOMEDCT_US/9468002",
      "relatedFromIdName": "Closed fracture of carpal bone",
      "relationLabel": "PAR",
      "additionalRelationLabel": "inverse_isa",
      "relatedId": "https://uts-ws.nlm.nih.gov/rest/content/2022AA/source/SNOMEDCT_US/10937761000119101",
      "relatedIdName": "Closed fracture of left wrist"
    },
    {
      "ui": "R162926601",
      "suppressible": false,
      "sourceUi": "784241000124123",
      "obsolete": false,
      "sourceOriginated": false,
      "rootSource": "SNOMEDCT_US",
      "groupId": "0",
      "attributeCount": 0,
      "classType": "AtomClusterRelation",
      "relatedFromId": "https://uts-ws.nlm.nih.gov/rest/content/2022AA/source/SNOMEDCT_US/9468002",
      "relatedFromIdName": "Closed fracture of carpal bone",
      "relationLabel": "PAR",
      "additionalRelationLabel": "inverse_isa",
      "relatedId": "https://uts-ws.nlm.nih.gov/rest/content/2022AA/source/SNOMEDCT_US/10937721000119106",
      "relatedIdName": "Closed fracture of right wrist"
    },
    {
      "ui": "R143885131",
      "suppressible": false,
      "sourceUi": "NONE",
      "obsolete": false,
      "sourceOriginated": false,
      "rootSource": "MDR",
      "groupId": "NONE",
      "attributeCount": 6,
      "classType": "AtomClusterRelation",
      "relatedFromId": "https://uts-ws.nlm.nih.gov/rest/content/2022AA/source/MDR/10009638",
      "relatedFromIdName": "Closed fractures of carpal bones",
      "relationLabel": "RO",
      "additionalRelationLabel": "member_of",
      "relatedId": "https://uts-ws.nlm.nih.gov/rest/content/2022AA/source/MDR/20000178",
      "relatedIdName": "Osteoporosis/osteopenia (SMQ)"
    },
    {
      "ui": "R144844533",
      "suppressible": false,
      "sourceUi": "NONE",
      "obsolete": false,
      "sourceOriginated": false,
      "rootSource": "MDR",
      "groupId": "NONE",
      "attributeCount": 6,
      "classType": "AtomClusterRelation",
      "relatedFromId": "https://uts-ws.nlm.nih.gov/rest/content/2022AA/source/MDR/10009529",
      "relatedFromIdName": "Closed fracture of carpal bone, unspecified",
      "relationLabel": "RO",
      "additionalRelationLabel": "member_of",
      "relatedId": "https://uts-ws.nlm.nih.gov/rest/content/2022AA/source/MDR/20000178",
      "relatedIdName": "Osteoporosis/osteopenia (SMQ)"
    },
    {
      "ui": "R143946612",
      "suppressible": false,
      "sourceUi": "NONE",
      "obsolete": false,
      "sourceOriginated": false,
      "rootSource": "MDRSPA",
      "groupId": "NONE",
      "attributeCount": 6,
      "classType": "AtomClusterRelation",
      "relatedFromId": "https://uts-ws.nlm.nih.gov/rest/content/2022AA/source/MDRSPA/10009638",
      "relatedFromIdName": "Fracturas cerradas de huesos del carpo",
      "relationLabel": "RO",
      "additionalRelationLabel": "member_of",
      "relatedId": "https://uts-ws.nlm.nih.gov/rest/content/2022AA/source/MDRSPA/20000178",
      "relatedIdName": "Osteoporosis/osteopenia (SMQ)"
    } ...
  ]
}
~~~~
