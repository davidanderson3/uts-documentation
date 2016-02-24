title=Retrieving Source-Asserted Relations
date=2015-09-30
updated=2016-02-09
type=page
status=published
category=Retrieving Source-Asserted Data
navorder=4
~~~~~~


[URIs](#uris) | [Query Parameters](#query-parameters) | [Sample Output](#sample-output)

URIs with /relations support the following use cases:

*  Retrieve the source-asserted relationships for a known source-asserted identifier.

Note that 'current' in the URI can always be used to search against the latest UMLS publication.
You may use any valid UMLS release back to 2008AA in your URI if you would like to search against a particular version of the UMLS.


### URIs

**The base URI is https://uts-ws.nlm.nih.gov/rest**

Sample URI|Description|Returned JSON Object classType
--- | ---
/content/current/source/LNC/44255-8/relations| Retrieves relationships of LOINC code 44255-8 | AtomClusterRelation


### Query Parameters

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
ticket | Y | A single-use service ticket is required for each call to the API. See [authentication](../../authentication.html) for more information | n/a | n/a | n/a
includeRelationLabels | N | One or more relation labels | Any [relation label](https://www.nlm.nih.gov/research/umls/knowledge_sources/metathesaurus/release/abbreviations.html#REL) in the UMLS |n/a| Use a comma between each relation label to specify more than one.
includeAdditionalRelationLabels | N | One or more relation attribute | Any [relation attribute](https://www.nlm.nih.gov/research/umls/knowledge_sources/metathesaurus/release/abbreviations.html#RELA) in the UMLS |n/a| Use a comma between each relation attribute to specify more than one.
pageNumber | N | Whole number that specifies which page of results to fetch. | 1,2,3, etc | 1 | n/a
pageSize | N | Whole number that specifies the number of results to include per page. | 1,2,3, etc | 25 | n/a


### Sample Output

Sample output for /content/2015AA/source/LNC/44255-8/relations?includeAdditionalRelationLabels=has_answer&ticket=ST...

~~~~json
{
    "pageSize": 25,
    "pageNumber": 1,
    "pageCount": 1,
    "result": [
        {
            "classType": "AtomClusterRelation",
            "ui": "R150334726",
            "suppressible": false,
            "sourceUi": "NONE",
            "obsolete": false,
            "sourceOriginated": false,
            "rootSource": "LNC",
            "relationLabel": "RO",
            "additionalRelationLabel": "has_answer",
            "groupId": "NONE",
            "attributeCount": 1,
            "relatedAtom": "",
            "relatedConcept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/LNC/LA6568-5",
            "relatedConceptName": "Not at all"
        },
        {
            "classType": "AtomClusterRelation",
            "ui": "R150349583",
            "suppressible": false,
            "sourceUi": "NONE",
            "obsolete": false,
            "sourceOriginated": false,
            "rootSource": "LNC",
            "relationLabel": "RO",
            "additionalRelationLabel": "has_answer",
            "groupId": "NONE",
            "attributeCount": 1,
            "relatedAtom": "",
            "relatedConcept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/LNC/LA6570-1",
            "relatedConceptName": "More than half the days"
        },
        {
            "classType": "AtomClusterRelation",
            "ui": "R150379228",
            "suppressible": false,
            "sourceUi": "NONE",
            "obsolete": false,
            "sourceOriginated": false,
            "rootSource": "LNC",
            "relationLabel": "RO",
            "additionalRelationLabel": "has_answer",
            "groupId": "NONE",
            "attributeCount": 1,
            "relatedAtom": "",
            "relatedConcept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/LNC/LA6571-9",
            "relatedConceptName": "Nearly every day"
        },
        {
            "classType": "AtomClusterRelation",
            "ui": "R150401508",
            "suppressible": false,
            "sourceUi": "NONE",
            "obsolete": false,
            "sourceOriginated": false,
            "rootSource": "LNC",
            "relationLabel": "RO",
            "additionalRelationLabel": "has_answer",
            "groupId": "NONE",
            "attributeCount": 1,
            "relatedAtom": "",
            "relatedConcept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/LNC/LA6569-3",
            "relatedConceptName": "Several days"
        }
    ]
}
~~~~

