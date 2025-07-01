title=Retrieving Source-Asserted Relations
date=2015-09-30
updated=2016-05-09
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
apiKey | Y | An API key is required for each call to the API. Visit [your UTS profile](https://uts.nlm.nih.gov/uts/profile) to obtain your API key. | n/a | n/a | n/a
includeRelationLabels | N | One or more relation labels | Any [relation label](https://www.nlm.nih.gov/research/umls/knowledge_sources/metathesaurus/release/abbreviations.html#REL) in the UMLS |n/a| Use a comma between each relation label to specify more than one.
includeAdditionalRelationLabels | N | One or more relation attribute | Any [relation attribute](https://www.nlm.nih.gov/research/umls/knowledge_sources/metathesaurus/release/abbreviations.html#RELA) in the UMLS |n/a| Use a comma between each relation attribute to specify more than one.
includeObsolete | N |  Include content that is obsolete according to the content provider or NLM. | true or false | false | n/a
includeSuppressible | N |  Include content that is suppressible according to NLM Editors.| true or false | false | n/a
pageNumber | N | Whole number that specifies which page of results to fetch. | 1,2,3, etc | 1 | n/a
pageSize | N | Whole number that specifies the number of results to include per page. | 1,2,3, etc | 25 | n/a


### Sample Output

Sample output for https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/LNC/44255-8/relations?includeAdditionalRelationLabels=has_answer&apiKey=YOUR_APIKEY...

~~~~json

{
  "pageSize": 25,
  "pageNumber": 1,
  "pageCount": 1,
  "result": [
    {
      "ui": "R150349583",
      "suppressible": false,
      "sourceUi": "NONE",
      "obsolete": false,
      "sourceOriginated": false,
      "rootSource": "LNC",
      "groupId": "NONE",
      "attributeCount": 1,
      "classType": "AtomClusterRelation",
      "relatedFromId": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/LNC/44255-8",
      "relatedFromIdName": "Feeling down, depressed, or hopeless in last 2W:Find:Pt:^Patient:Ord:Reported.PHQ",
      "relationLabel": "RO",
      "additionalRelationLabel": "has_answer",
      "relatedId": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/LNC/LA6570-1",
      "relatedIdName": "More than half the days"
    },
    {
      "ui": "R150379228",
      "suppressible": false,
      "sourceUi": "NONE",
      "obsolete": false,
      "sourceOriginated": false,
      "rootSource": "LNC",
      "groupId": "NONE",
      "attributeCount": 1,
      "classType": "AtomClusterRelation",
      "relatedFromId": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/LNC/44255-8",
      "relatedFromIdName": "Feeling down, depressed, or hopeless in last 2W:Find:Pt:^Patient:Ord:Reported.PHQ",
      "relationLabel": "RO",
      "additionalRelationLabel": "has_answer",
      "relatedId": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/LNC/LA6571-9",
      "relatedIdName": "Nearly every day"
    },
    {
      "ui": "R150401508",
      "suppressible": false,
      "sourceUi": "NONE",
      "obsolete": false,
      "sourceOriginated": false,
      "rootSource": "LNC",
      "groupId": "NONE",
      "attributeCount": 1,
      "classType": "AtomClusterRelation",
      "relatedFromId": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/LNC/44255-8",
      "relatedFromIdName": "Feeling down, depressed, or hopeless in last 2W:Find:Pt:^Patient:Ord:Reported.PHQ",
      "relationLabel": "RO",
      "additionalRelationLabel": "has_answer",
      "relatedId": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/LNC/LA6569-3",
      "relatedIdName": "Several days"
    },
    {
      "ui": "R150334726",
      "suppressible": false,
      "sourceUi": "NONE",
      "obsolete": false,
      "sourceOriginated": false,
      "rootSource": "LNC",
      "groupId": "NONE",
      "attributeCount": 1,
      "classType": "AtomClusterRelation",
      "relatedFromId": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/LNC/44255-8",
      "relatedFromIdName": "Feeling down, depressed, or hopeless in last 2W:Find:Pt:^Patient:Ord:Reported.PHQ",
      "relationLabel": "RO",
      "additionalRelationLabel": "has_answer",
      "relatedId": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/LNC/LA6568-5",
      "relatedIdName": "Not at all"
    }
  ]
}
~~~~

