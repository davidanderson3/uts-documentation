title=Retrieving Source-Asserted Relations
date=2015-09-30
updated=2015-09-30
type=page
status=published
category=Retrieving Source-Asserted Data
navorder=4
~~~~~~


[URIs](#uris) | [Query Parameters](#query-parameters) | [Sample Output](#sample-output)

URIs with /relations support the following use cases:

*  Retrieve the sources-asserted relationships for a known source-asserted identifier.

Note that 'current' in the URI can always be used to search against the latest UMLS publication.
You may use any valid UMLS release back to 2008AA in your URI if you would like to search against a particular version of the UMLS.


### URIs

**The base URI is https://uts-ws.nlm.nih.gov/rest**

Sample URI|Description
--- | ---
/content/current/source/SNOMEDCT_US/9468002/relations| Retrieves relationships of the SNOMED concept


### Query Parameters

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
ticket | Y | A single-use service ticket is required for each call to the API. See [authentication](../authentication.html) for more information | n/a | n/a | n/a
includeRelationLabels | N | One or more relation labels | Any [relation label](https://www.nlm.nih.gov/research/umls/knowledge_sources/metathesaurus/release/abbreviations.html#mrdoc_REL) in the UMLS |n/a| Use a comma between each relation label to specify more than one.
includeAdditionalRelationLabels | N | One or more relation attribute | Any [relation attribute](https://www.nlm.nih.gov/research/umls/knowledge_sources/metathesaurus/release/abbreviations.html#mrdoc_RELA) in the UMLS |n/a| Use a comma between each relation attribute to specify more than one.
pageNumber | N | Whole number that specifies which page of results to fetch. | 1,2,3, etc | 1 | n/a
pageSize | N | Whole number that specifies the number of results to include per page. | 1,2,3, etc | 25 | n/a


### Sample Output


**Calls under /relations will return a JSON object of classType 'AtomClusterAtomClusterRelation'.**

Sample output for /content/2015AA/source/SNOMEDCT_US/9468002/relations?ticket=ST...

~~~~json
{
    "pageSize": 25,
    "pageNumber": 1,
    "pageCount": 2,
    "result": [
        {
            "classType": "AtomClusterAtomClusterRelation",
            "ui": "R88901452",
            "suppressible": false,
            "sourceUi": "NONE",
            "obsolete": false,
            "sourceOriginated": true,
            "rootSource": "MEDCIN",
            "relationLabel": "SY",
            "additionalRelationLabel": "same_as",
            "groupId": "NONE",
            "attributeCount": 0,
            "relatedAtom": "NONE",
            "relatedConcept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/MEDCIN/34696"
        },
        {
            "classType": "AtomClusterAtomClusterRelation",
            "ui": "R88701069",
            "suppressible": false,
            "sourceUi": "NONE",
            "obsolete": false,
            "sourceOriginated": true,
            "rootSource": "MEDCIN",
            "relationLabel": "RB",
            "additionalRelationLabel": "inverse_isa",
            "groupId": "NONE",
            "attributeCount": 0,
            "relatedAtom": "NONE",
            "relatedConcept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/MEDCIN/91573"
        },
        {
            "classType": "AtomClusterAtomClusterRelation",
            "ui": "R88980836",
            "suppressible": false,
            "sourceUi": "NONE",
            "obsolete": false,
            "sourceOriginated": true,
            "rootSource": "MEDCIN",
            "relationLabel": "RB",
            "additionalRelationLabel": "inverse_isa",
            "groupId": "NONE",
            "attributeCount": 0,
            "relatedAtom": "NONE",
            "relatedConcept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/MEDCIN/91574"
        },
...
    ]
}
~~~~

