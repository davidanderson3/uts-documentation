title=Retrieving Content View Information
date=2016-05-09
updated=2016-07-07
type=page
status=published
category=Retrieving UMLS Data
navorder=8
~~~~~~


[URIs](#uris) | [Query Parameters](#query-parameters) | [Sample Output](#sample-output-1)

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
[/content-views/current](#sample-output-1) | Retrieves information about all subsets from the current release | ContentView
[/content-views/current/CUI/C2711988](#sample-output-2) | Retrieves information for the SNOMED CT CORE Problem List content view | ContentView
[/content-views/current/CUI/C2711988/members](#sample-output-3)  | Retrieves members of the SNOMED CT CORE Problem List content view | SourceConceptContentViewMember*
[/content-views/current/CUI/C2711988/member/238788004](#sample-output-4)  | Retrieves an individual member of the SNOMED CT CORE Problem List content view | SourceConceptContentViewMember

*Calls for members of certain content views return output with a "AtomContentViewMember" JSON Object classType*.

### Query Parameters

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
ticket | Y | A single-use service ticket is required for each call to the API. See [authentication](../authentication.html) for more information | n/a | n/a | n/a
pageNumber | N | Whole number that specifies which page of results to fetch. | 1,2,3, etc | 1 | n/a
pageSize | N | Whole number that specifies the number of results to include per page. | 1,2,3, etc | 25 | n/a

### Sample Output 1

Sample output for https://uts-ws.nlm.nih.gov/rest/content-views/current?ticket=ST...

~~~~json
{
	"pageSize" : 25,
	"pageNumber" : 1,
	"pageCount" : 1,
	"result" : [{
			"classType" : "ContentView",
			"ui" : "C1700357",
			"name" : "MetaMap NLP View",
			"cascade" : false,
			"includeObsolete" : false,
			"algorithm" : "NONE",
			"category" : "NONE",
			"code" : 0,
			"contributor" : "NONE",
			"contributorDate" : "NONE",
			"contributorURL" : "NONE",
			"contributorVersion" : "NONE",
			"description" : "This content view represents the strict model of data used by MetaMap.",
			"maintainer" : "NONE",
			"maintainerDate" : "NONE",
			"maintainerURL" : "NONE",
			"maintainerVersion" : "NONE",
			"previousMeta" : "NONE",
			"contentViewClass" : "NONE",
			"subCategory" : "NONE",
			"generated" : false,
			"attributeCount" : 0,
			"atomMemberCount" : 4478743,
			"sourceConceptMemberCount" : 0,
			"relationMemberCount" : 0,
			"conceptMemberCount" : 0,
			"uri" : "https://uts-ws.nlm.nih.gov/rest/content-views/2016AA/CUI/C1700357",
			"members" : "https://uts-ws.nlm.nih.gov/rest/content-views/2016AA/CUI/C1700357/members"
		}, {
			"classType" : "ContentView",
			"ui" : "C2711988",
			"name" : "CORE Problem List Subset of SNOMED CT",
			"cascade" : false,
			"includeObsolete" : false,
			"algorithm" : "NONE",
			"category" : "NONE",
			"code" : 0,
			"contributor" : "NONE",
			"contributorDate" : "NONE",
			"contributorURL" : "NONE",
			"contributorVersion" : "NONE",
			"description" : "This content view contains the subset of SNOMEDCT_US concepts that are most frequently used in problem lists. The subset is derived from datasets from large health care institutions. The most commonly used problem list terms are mapped to SNOMEDCT_US and the UMLS. The use of SNOMEDCT_US contents in this subset is subject to the SNOMED CT license requirements. The use of SNOMED CT is free in IHTSDO member countries (including the U.S.) and low income countries.",
			"maintainer" : "NONE",
			"maintainerDate" : "NONE",
			"maintainerURL" : "NONE",
			"maintainerVersion" : "NONE",
			"previousMeta" : "NONE",
			"contentViewClass" : "NONE",
			"subCategory" : "NONE",
			"generated" : false,
			"attributeCount" : 0,
			"atomMemberCount" : 0,
			"sourceConceptMemberCount" : 6358,
			"relationMemberCount" : 0,
			"conceptMemberCount" : 0,
			"uri" : "https://uts-ws.nlm.nih.gov/rest/content-views/2016AA/CUI/C2711988",
			"members" : "https://uts-ws.nlm.nih.gov/rest/content-views/2016AA/CUI/C2711988/members"
		}, {
			"classType" : "ContentView",
			"ui" : "C3503753",
			"name" : "Prescribable List Subset of RXNORM",
			"cascade" : false,
			"includeObsolete" : false,
			"algorithm" : "NONE",
			"category" : "NONE",
			"code" : 0,
			"contributor" : "NONE",
			"contributorDate" : "NONE",
			"contributorURL" : "NONE",
			"contributorVersion" : "NONE",
			"description" : "This content view contains the subset of RXNORM concepts that are prescribable.",
			"maintainer" : "NONE",
			"maintainerDate" : "NONE",
			"maintainerURL" : "NONE",
			"maintainerVersion" : "NONE",
			"previousMeta" : "NONE",
			"contentViewClass" : "NONE",
			"subCategory" : "NONE",
			"generated" : false,
			"attributeCount" : 0,
			"atomMemberCount" : 224133,
			"sourceConceptMemberCount" : 0,
			"relationMemberCount" : 0,
			"conceptMemberCount" : 0,
			"uri" : "https://uts-ws.nlm.nih.gov/rest/content-views/2016AA/CUI/C3503753",
			"members" : "https://uts-ws.nlm.nih.gov/rest/content-views/2016AA/CUI/C3503753/members"
		}, 
...
	]
}
~~~~

### Sample Output 2
Sample output for https://uts-ws.nlm.nih.gov/rest/content-views/current/CUI/C2711988?ticket=ST...


~~~~json
{

    "pageSize": 25,
    "pageNumber": 1,
    "pageCount": 1,
    "result": {
        "classType": "ContentView",
        "ui": "C2711988",
        "name": "CORE Problem List Subset of SNOMED CT",
        "cascade": false,
        "includeObsolete": false,
        "algorithm": "NONE",
        "category": "NONE",
        "code": 0,
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
        "attributeCount": 0,
        "atomMemberCount": 0,
        "sourceConceptMemberCount": 6358,
        "relationMemberCount": 0,
        "conceptMemberCount": 0,
        "uri": "https://uts-ws.nlm.nih.gov/rest/content-views/2016AA/CUI/C2711988",
        "members": "https://uts-ws.nlm.nih.gov/rest/content-views/2016AA/CUI/C2711988/members"
    }

}
~~~~

### Sample Output 3
Sample output for members of the SNOMED CT CORE Problem List subset, https://uts-ws.nlm.nih.gov/rest/content-views/current/CUI/C1700357/members?ticket=ST...

~~~~json
{

	"pageSize" : 25,
	"pageNumber" : 1,
	"pageCount" : 255,
	"result" : [{
			"classType" : "SourceConceptContentViewMember",
			"sourceConcept" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/813001",
			"name" : "Ankle instability",
			"contentViewMemberAttributes" : [{
					"classType" : "Attribute",
					"ui" : "AT201422859",
					"sourceUi" : "NONE",
					"rootSource" : "MTH",
					"name" : "FIRST_IN_SUBSET",
					"value" : "201408"
				}, {
					"classType" : "Attribute",
					"ui" : "AT201422860",
					"sourceUi" : "NONE",
					"rootSource" : "MTH",
					"name" : "IS_RETIRED_FROM_SUBSET",
					"value" : "False"
				}, {
					"classType" : "Attribute",
					"ui" : "AT201422861",
					"sourceUi" : "NONE",
					"rootSource" : "MTH",
					"name" : "OCCURRENCE",
					"value" : "2"
				}, {
					"classType" : "Attribute",
					"ui" : "AT201422862",
					"sourceUi" : "NONE",
					"rootSource" : "MTH",
					"name" : "USAGE",
					"value" : "0.0010"
				}
			],
			"ui" : "813001"
		}, {
			"classType" : "SourceConceptContentViewMember",
			"sourceConcept" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/271772002",
			"name" : "Unstable ankle",
			"contentViewMemberAttributes" : [{
					"classType" : "Attribute",
					"ui" : "AT153687776",
					"sourceUi" : "NONE",
					"rootSource" : "MTH",
					"name" : "FIRST_IN_SUBSET",
					"value" : "200907"
				}, {
					"classType" : "Attribute",
					"ui" : "AT201422833",
					"sourceUi" : "NONE",
					"rootSource" : "MTH",
					"name" : "IS_RETIRED_FROM_SUBSET",
					"value" : "True"
				}, {
					"classType" : "Attribute",
					"ui" : "AT201422834",
					"sourceUi" : "NONE",
					"rootSource" : "MTH",
					"name" : "REPLACED_BY_SNOMED_CID",
					"value" : "813001"
				}
			],
			"ui" : "271772002"
		}, {
			"classType" : "SourceConceptContentViewMember",
			"sourceConcept" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/409609008",
			"name" : "Radiologic infiltrate of lung",
			"contentViewMemberAttributes" : [{
					"classType" : "Attribute",
					"ui" : "AT153697462",
					"sourceUi" : "NONE",
					"rootSource" : "MTH",
					"name" : "FIRST_IN_SUBSET",
					"value" : "201002"
				}, {
					"classType" : "Attribute",
					"ui" : "AT153697463",
					"sourceUi" : "NONE",
					"rootSource" : "MTH",
					"name" : "IS_RETIRED_FROM_SUBSET",
					"value" : "False"
				}, {
					"classType" : "Attribute",
					"ui" : "AT153697464",
					"sourceUi" : "NONE",
					"rootSource" : "MTH",
					"name" : "OCCURRENCE",
					"value" : "2"
				}, {
					"classType" : "Attribute",
					"ui" : "AT153697466",
					"sourceUi" : "NONE",
					"rootSource" : "MTH",
					"name" : "USAGE",
					"value" : "0.0083"
				}
			],
			"ui" : "409609008"
		}...
	]

}

~~~~
### Sample Output 4
Sample output for one member of the SNOMED CT CORE Problem List subset, https://uts-ws.nlm.nih.gov/rest/content-views/current/CUI/C2711988/member/238788004?ticket=ST...

~~~~json
{

    "pageSize": 25,
    "pageNumber": 1,
    "pageCount": 1,
    "result": {
        "classType": "SourceConceptContentViewMember",
        "sourceConcept": "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/238788004",
        "name": "Venous stasis syndrome",
        "contentViewMemberAttributes": [
            {
                "classType": "Attribute",
                "ui": "AT153686494",
                "sourceUi": "NONE",
                "rootSource": "MTH",
                "name": "FIRST_IN_SUBSET",
                "value": "200907"
            },
            {
                "classType": "Attribute",
                "ui": "AT153686495",
                "sourceUi": "NONE",
                "rootSource": "MTH",
                "name": "IS_RETIRED_FROM_SUBSET",
                "value": "False"
            },
            {
                "classType": "Attribute",
                "ui": "AT153686496",
                "sourceUi": "NONE",
                "rootSource": "MTH",
                "name": "OCCURRENCE",
                "value": "2"
            },
            {
                "classType": "Attribute",
                "ui": "AT153686498",
                "sourceUi": "NONE",
                "rootSource": "MTH",
                "name": "USAGE",
                "value": "0.0023"
            }
        ],
        "ui": "238788004"
    }

}
~~~~