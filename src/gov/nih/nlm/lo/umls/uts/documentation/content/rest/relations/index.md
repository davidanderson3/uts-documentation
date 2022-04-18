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

*  Retrieve the NLM-asserted relationships for a known CUI.

**NLM does not assert parent or child relationships between concepts.**

Note that 'current' in the URI can always be used to search against the latest UMLS publication.
You may use any valid UMLS release back to 2008AA in your URI if you would like to search against a particular version of the UMLS.


### URIs

**The base URI is https://uts-ws.nlm.nih.gov/rest**

Sample URI|Description|Returned JSON Object classType
--- | ---
/content/current/CUI/C0009044/relations | Retrieves NLM-asserted relationships of the CUI | ConceptRelation



### Query Parameters

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
apiKey | Y | An API key is required for each call to the API. Visit [your UTS profile](https://uts.nlm.nih.gov/uts/profile) to obtain your API key. | n/a | n/a | n/a
pageNumber | N | Whole number that specifies which page of results to fetch. | 1,2,3, etc | 1 | n/a
pageSize | N | Whole number that specifies the number of results to include per page. | 1,2,3, etc | 25 | n/a



### Sample Output

Sample output for https://uts-ws.nlm.nih.gov/rest/content/current/CUI/C0009044/relations?apiKey=YOUR_APIKEY...

~~~~json
{
    "pageSize": 25,
    "pageNumber": 1,
    "pageCount": 1,
    "result": [
        {
            "classType": "ConceptRelation",
            "ui": "R02986047",
            "suppressible": false,
            "sourceUi": "NONE",
            "obsolete": false,
            "sourceOriginated": false,
            "rootSource": "MTH",
            "relationLabel": "RN",
            "additionalRelationLabel": "",
            "groupId": "NONE",
            "attributeCount": 0,
            "relatedId": "https://uts-ws.nlm.nih.gov/rest/content/2016AA/CUI/C0029509",
            "relatedIdName": "Unspecified site injury"
        },
        {
            "classType": "ConceptRelation",
            "ui": "R13333743",
            "suppressible": false,
            "sourceUi": "NONE",
            "obsolete": false,
            "sourceOriginated": false,
            "rootSource": "MTH",
            "relationLabel": "RO",
            "additionalRelationLabel": "",
            "groupId": "NONE",
            "attributeCount": 0,
            "relatedId": "https://uts-ws.nlm.nih.gov/rest/content/2016AA/CUI/C0007285",
            "relatedIdName": "Bone structure of carpus"
        },
        {
            "classType": "ConceptRelation",
            "ui": "R03033072",
            "suppressible": false,
            "sourceUi": "NONE",
            "obsolete": false,
            "sourceOriginated": false,
            "rootSource": "MTH",
            "relationLabel": "RO",
            "additionalRelationLabel": "",
            "groupId": "NONE",
            "attributeCount": 0,
            "relatedId": "https://uts-ws.nlm.nih.gov/rest/content/2016AA/CUI/C0009353",
            "relatedIdName": "Colles' Fracture"
        },
        {
            "classType": "ConceptRelation",
            "ui": "R18927471",
            "suppressible": false,
            "sourceUi": "NONE",
            "obsolete": false,
            "sourceOriginated": false,
            "rootSource": "MTH",
            "relationLabel": "RO",
            "additionalRelationLabel": "",
            "groupId": "NONE",
            "attributeCount": 0,
            "relatedId": "https://uts-ws.nlm.nih.gov/rest/content/2016AA/CUI/C0159738",
            "relatedIdName": "Closed fracture of lower end of radius AND ulna"
        },
        {
            "classType": "ConceptRelation",
            "ui": "R03164258",
            "suppressible": false,
            "sourceUi": "NONE",
            "obsolete": false,
            "sourceOriginated": false,
            "rootSource": "MTH",
            "relationLabel": "RO",
            "additionalRelationLabel": "",
            "groupId": "NONE",
            "attributeCount": 0,
            "relatedId": "https://uts-ws.nlm.nih.gov/rest/content/2016AA/CUI/C0347757",
            "relatedIdName": "Closed fracture dislocation of wrist"
        }
    ]
}
~~~~
