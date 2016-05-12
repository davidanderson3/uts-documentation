title=Retrieving Content View Information
date=2016-05-09
updated=2016-05-09
type=page
status=published
category=Retrieving UMLS Data
navorder=8
~~~~~~


[URIs](#uris) | [Query Parameters](#query-parameters) | [Sample Output](#sample-output)

URIs with /content-views support the following use cases:

* Retrieve all content views for a known UMLS Release. 
* Retrieve information (name, description, member count, etc.) for a known content view.
* Retrieve all members of a known content view.

Note that 'current' in the URI can always be used to search against the latest UMLS publication.
You may use any valid UMLS release back to 2008AA in your URI if you would like to search against a particular version of the UMLS.


### URIs

**The base URI is https://uts-ws.nlm.nih.gov/rest**

Sample URI|Description|Returned JSON Object classType
--- | ---
/content-views/current/ | Retrieves information about all content views from the current release | ContentView
/content-views/current/CUI/C2711988 | Retrieves information for the 'CORE Problem List Subset of SNOMED CT' content view | ContentView
[/content-views/current/CUI/C2711988/members](#sourceconceptcontentviewmember-sample-output) | Retrieves members of the 'CORE Problem List Subset of SNOMED CT' content view| SourceConceptContentViewMember
[/content-views/current/CUI/C1700357/members](#atomcontentviewmember-sample-output) | Retrieves members of the 'MetaMap NLP View' content view | AtomContentViewMember

Content view members that do not contain attributes will return an empty contentViewMemberAttributes array with each content view member object.

### Query Parameters

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
ticket | Y | A single-use service ticket is required for each call to the API. See [authentication](../authentication.html) for more information | n/a | n/a | n/a
pageNumber | N | Whole number that specifies which page of results to fetch.  | 1,2,3, etc. | 1  | Most content views contain several thousand members. When retrieving members of a content view, use paging to retrieve the complete set.
pageSize | N | Whole number that specifies the number of results to include per page. | 1,2,3, etc | 25 | n/a 

### Sample Output

Sample output for /content-views/current?ticket=ST-...

~~~~json
{
    "pageSize": 25,
    "pageNumber": 1,
    "pageCount": 1,
    "result": 
[
...
{

    "classType": "ContentView",
    "ui": "C2711988",
    "name": "CORE Problem List Subset of SNOMED CT",
    "cascade": false,
    "includeObsolete": false,
    "algorithm": "NONE",
    "category": "NONE",
    "code": ​0,
    "contributor": "NONE",
    "contributorDate": "NONE",
    "contributorURL": "NONE",
    "contributorVersion": "NONE",
    "description": "This content view contains the subset of SNOMEDCT_US concepts that are most frequently used in problem lists. The subset is derived from datasets from large health care institutions. The most commonly used problem list terms are mapped to SNOMEDCT_US and the UMLS. The use of SNOMEDCT_US contents in this subset is subject to the SNOMED CT license requirements. The use of SNOMED CT is free in IHTSDO member countries (including the U.S.) and low income countries.",
    "maintainer": "NONE",
    "maintainerDate": "NONE",
    "maintainerURL": "NONE",
    "maintainerVersion": "NONE",
    "previousMeta": "NONE",
    "contentViewClass": "NONE",
    "subCategory": "NONE",
    "generated": false,
    "attributeCount": ​0,
    "atomMemberCount": ​0,
    "sourceConceptMemberCount": ​6358,
    "relationMemberCount": ​0,
    "conceptMemberCount": ​0,
    "uri": "https://uts-ws.nlm.nih.gov/rest/content-views/2016AA/CUI/C2711988",
    "members": "https://uts-ws.nlm.nih.gov/rest/content-views/2016AA/CUI/C2711988/members"

},
{

    "classType": "ContentView",
    "ui": "C3503753",
    "name": "Prescribable List Subset of RXNORM",
    "cascade": false,
    "includeObsolete": false,
    "algorithm": "NONE",
    "category": "NONE",
    "code": ​0,
    "contributor": "NONE",
    "contributorDate": "NONE",
    "contributorURL": "NONE",
    "contributorVersion": "NONE",
    "description": "This content view contains the subset of RXNORM concepts that are prescribable.",
    "maintainer": "NONE",
    "maintainerDate": "NONE",
    "maintainerURL": "NONE",
    "maintainerVersion": "NONE",
    "previousMeta": "NONE",
    "contentViewClass": "NONE",
    "subCategory": "NONE",
    "generated": false,
    "attributeCount": ​0,
    "atomMemberCount": ​224133,
    "sourceConceptMemberCount": ​0,
    "relationMemberCount": ​0,
    "conceptMemberCount": ​0,
    "uri": "https://uts-ws.nlm.nih.gov/rest/content-views/2016AA/CUI/C3503753",
    "members": "https://uts-ws.nlm.nih.gov/rest/content-views/2016AA/CUI/C3503753/members"

},
{

    "classType": "ContentView",
    "ui": "C3812142",
    "name": "SNOMEDCT US Extension Subset",
    "cascade": false,
    "includeObsolete": false,
    "algorithm": "NONE",
    "category": "NONE",
    "code": ​0,
    "contributor": "NONE",
    "contributorDate": "NONE",
    "contributorURL": "NONE",
    "contributorVersion": "NONE",
    "description": "This content view allows users to easily identify atoms in the UMLS that come from the US Extension to SNOMED CT and carry the NLM Module ID of '731000124108'.",
    "maintainer": "NONE",
    "maintainerDate": "NONE",
    "maintainerURL": "NONE",
    "maintainerVersion": "NONE",
    "previousMeta": "NONE",
    "contentViewClass": "NONE",
    "subCategory": "NONE",
    "generated": false,
    "attributeCount": ​0,
    "atomMemberCount": ​0,
    "sourceConceptMemberCount": ​5358,
    "relationMemberCount": ​0,
    "conceptMemberCount": ​0,
    "uri": "https://uts-ws.nlm.nih.gov/rest/content-views/2016AA/CUI/C3812142",
    "members": "https://uts-ws.nlm.nih.gov/rest/content-views/2016AA/CUI/C3812142/members"

},
{

    "classType": "ContentView",
    "ui": "C4048847",
    "name": "LOINC Top 300+ Lab Orders",
    "cascade": false,
    "includeObsolete": false,
    "algorithm": "NONE",
    "category": "NONE",
    "code": ​0,
    "contributor": "NONE",
    "contributorDate": "NONE",
    "contributorURL": "NONE",
    "contributorVersion": "NONE",
    "description": "The Universal Lab Order Codes Value Set from LOINC is a collection of the most frequent lab orders. It was created for use by developers of provider order entry systems that would deliver them in HL7 messages to laboratories where they could be understood and fulfilled.",
    "maintainer": "NONE",
    "maintainerDate": "NONE",
    "maintainerURL": "NONE",
    "maintainerVersion": "NONE",
    "previousMeta": "NONE",
    "contentViewClass": "NONE",
    "subCategory": "NONE",
    "generated": false,
    "attributeCount": ​0,
    "atomMemberCount": ​0,
    "sourceConceptMemberCount": ​330,
    "relationMemberCount": ​0,
    "conceptMemberCount": ​0,
    "uri": "https://uts-ws.nlm.nih.gov/rest/content-views/2016AA/CUI/C4048847",
    "members": "https://uts-ws.nlm.nih.gov/rest/content-views/2016AA/CUI/C4048847/members"

},

...
}
~~~~

Sample output for /content-views/current/CUI/C2711988?ticket=ST-...

~~~~json
{

   "pageSize": 25,
   "pageNumber": 1,
   "pageCount": 1,
   "result": 

   {

    "classType": "ContentView",
    "ui": "C2711988",
    "name": "CORE Problem List Subset of SNOMED CT",
    "cascade": false,
    "includeObsolete": false,
    "algorithm": "NONE",
    "category": "NONE",
    "code": ​0,
    "contributor": "NONE",
    "contributorDate": "NONE",
    "contributorURL": "NONE",
    "contributorVersion": "NONE",
    "description": "This content view contains the subset of SNOMEDCT_US concepts that are most frequently used in problem lists. The subset is derived from datasets from large health care institutions. The most commonly used problem list terms are mapped to SNOMEDCT_US and the UMLS. The use of SNOMEDCT_US contents in this subset is subject to the SNOMED CT license requirements. The use of SNOMED CT is free in IHTSDO member countries (including the U.S.) and low income countries.",
    "maintainer": "NONE",
    "maintainerDate": "NONE",
    "maintainerURL": "NONE",
    "maintainerVersion": "NONE",
    "previousMeta": "NONE",
    "contentViewClass": "NONE",
    "subCategory": "NONE",
    "generated": false,
    "attributeCount": ​0,
    "atomMemberCount": ​0,
    "sourceConceptMemberCount": ​6358,
    "relationMemberCount": ​0,
    "conceptMemberCount": ​0,
    "uri": "https://uts-ws.nlm.nih.gov/rest/content-views/2016AA/CUI/C2711988",
    "members": "https://uts-ws.nlm.nih.gov/rest/content-views/2016AA/CUI/C2711988/members"

   }
}
~~~~

####SourceConceptContentViewMember Sample Output
Sample output for /content-views/current/CUI/C2711988/members?ticket=ST-...

~~~~json
{
    "pageSize": 25,
    "pageNumber": 1,
    "pageCount": 1,
    "result": [
        {
            "classType": "SourceConceptContentViewMember",
            "ui": "813001",
            "uri": "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/813001",
            "name": "Ankle instability",
            "contentViewMemberAttributes": [
                {
                    "classType": "Attribute",
                    "ui": "AT201422859",
                    "sourceUi": "NONE",
                    "rootSource": "MTH",
                    "name": "FIRST_IN_SUBSET",
                    "value": "201408"
                },
                {
                    "classType": "Attribute",
                    "ui": "AT201422860",
                    "sourceUi": "NONE",
                    "rootSource": "MTH",
                    "name": "IS_RETIRED_FROM_SUBSET",
                    "value": "False"
                },
                {
                    "classType": "Attribute",
                    "ui": "AT201422861",
                    "sourceUi": "NONE",
                    "rootSource": "MTH",
                    "name": "OCCURRENCE",
                    "value": "2"
                },
                {
                    "classType": "Attribute",
                    "ui": "AT201422862",
                    "sourceUi": "NONE",
                    "rootSource": "MTH",
                    "name": "USAGE",
                    "value": "0.0010"
                }
            ]
        },
        {
            "classType": "SourceConceptContentViewMember",
            "ui": "271772002",
            "uri": "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/271772002",
            "name": "Unstable ankle",
            "contentViewMemberAttributes": [
                {
                    "classType": "Attribute",
                    "ui": "AT153687776",
                    "sourceUi": "NONE",
                    "rootSource": "MTH",
                    "name": "FIRST_IN_SUBSET",
                    "value": "200907"
                },
                {
                    "classType": "Attribute",
                    "ui": "AT201422833",
                    "sourceUi": "NONE",
                    "rootSource": "MTH",
                    "name": "IS_RETIRED_FROM_SUBSET",
                    "value": "True"
                },
                {
                    "classType": "Attribute",
                    "ui": "AT201422834",
                    "sourceUi": "NONE",
                    "rootSource": "MTH",
                    "name": "REPLACED_BY_SNOMED_CID",
                    "value": "813001"
                }
            ]
        },
        {
            "classType": "SourceConceptContentViewMember",
            "ui": "409609008",
            "uri": "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/409609008",
            "name": "Radiologic infiltrate of lung",
            "contentViewMemberAttributes": [
                {
                    "classType": "Attribute",
                    "ui": "AT153697462",
                    "sourceUi": "NONE",
                    "rootSource": "MTH",
                    "name": "FIRST_IN_SUBSET",
                    "value": "201002"
                },
                {
                    "classType": "Attribute",
                    "ui": "AT153697463",
                    "sourceUi": "NONE",
                    "rootSource": "MTH",
                    "name": "IS_RETIRED_FROM_SUBSET",
                    "value": "False"
                },
                {
                    "classType": "Attribute",
                    "ui": "AT153697464",
                    "sourceUi": "NONE",
                    "rootSource": "MTH",
                    "name": "OCCURRENCE",
                    "value": "2"
                },
                {
                    "classType": "Attribute",
                    "ui": "AT153697466",
                    "sourceUi": "NONE",
                    "rootSource": "MTH",
                    "name": "USAGE",
                    "value": "0.0083"
                }
            ]
        },
...

}
~~~~


####AtomContentViewMember Sample Output

~~~~json
{
    "pageSize": 25,
    "pageNumber": 1,
    "pageCount": 1,
    "result": [
        {
            "classType": "AtomContentViewMember",
            "ui": "A21290378",
            "uri": "https://uts-ws.nlm.nih.gov/rest/content/2016AA/AUI/A21290378",
            "name": "Herbertia tigridioides",
            "contentViewMemberAttributes": [
                
            ]
        },
        {
            "classType": "AtomContentViewMember",
            "ui": "A21290379",
            "uri": "https://uts-ws.nlm.nih.gov/rest/content/2016AA/AUI/A21290379",
            "name": "Herbertia zebrina",
            "contentViewMemberAttributes": [
                
            ]
        },
        {
            "classType": "AtomContentViewMember",
            "ui": "A21274417",
            "uri": "https://uts-ws.nlm.nih.gov/rest/content/2016AA/AUI/A21274417",
            "name": "Libertia chilensis",
            "contentViewMemberAttributes": [
                
            ]
        },
        {
            "classType": "AtomContentViewMember",
            "ui": "A21371390",
            "uri": "https://uts-ws.nlm.nih.gov/rest/content/2016AA/AUI/A21371390",
            "name": "Libertia sessiliflora",
            "contentViewMemberAttributes": [
                
            ]
        },
        {
            "classType": "AtomContentViewMember",
            "ui": "A21371391",
            "uri": "https://uts-ws.nlm.nih.gov/rest/content/2016AA/AUI/A21371391",
            "name": "Mastigostyla sp. 01",
            "contentViewMemberAttributes": [
                
            ]
        },
        {
            "classType": "AtomContentViewMember",
            "ui": "A21290380",
            "uri": "https://uts-ws.nlm.nih.gov/rest/content/2016AA/AUI/A21290380",
            "name": "Nemastylis geminiflora",
            "contentViewMemberAttributes": [
                
            ]
        },
        
...
}
~~~~
