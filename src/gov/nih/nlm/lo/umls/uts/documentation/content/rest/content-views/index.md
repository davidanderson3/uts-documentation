title=Retrieving Content View Information
date=2016-05-09
updated=2016-06-28
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
/content-views/current/ | Retrieves information about all subsets from the current release | ContentView
/content-views/current/CUI/C1700357 | Retrieves information for the MetaMap NLP View content view | ContentView
/content-views/current/CUI/C1700357/members | Retrieves members of the MetaMap NLP View content view | AtomContentViewMember*
/content-views/current/CUI/C1700357/member/A21290378 | Retrieves an individual member of the MetaMap NLP View content view | AtomContentViewMember

*Calls for members of certain content views return output with a "SourceConceptContentViewMember" JSON Object classType*.

### Query Parameters

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
ticket | Y | A single-use service ticket is required for each call to the API. See [authentication](../authentication.html) for more information | n/a | n/a | n/a

### Sample Output

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

Sample output for https://uts-ws.nlm.nih.gov/rest/content-views/current/CUI/C1700357?ticket=ST...

~~~~json
{
	"pageSize" : 25,
	"pageNumber" : 1,
	"pageCount" : 1,
	"result" : {
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
	}
}
~~~~

Sample output for https://uts-ws.nlm.nih.gov/rest/content-views/current/CUI/C1700357/members?ticket=ST...

~~~~json
{
	"pageSize" : 25,
	"pageNumber" : 1,
	"pageCount" : 179150,
	"result" : [{
			"classType" : "AtomContentViewMember",
			"atom" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/AUI/A21290378",
			"name" : "Herbertia tigridioides",
			"contentViewMemberAttributes" : [],
			"ui" : "A21290378"
		}, {
			"classType" : "AtomContentViewMember",
			"atom" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/AUI/A21290379",
			"name" : "Herbertia zebrina",
			"contentViewMemberAttributes" : [],
			"ui" : "A21290379"
		}, {
			"classType" : "AtomContentViewMember",
			"atom" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/AUI/A21274417",
			"name" : "Libertia chilensis",
			"contentViewMemberAttributes" : [],
			"ui" : "A21274417"
		}, 
...
	]
}
~~~~

Sample output for https://uts-ws.nlm.nih.gov/rest/content-views/current/CUI/C1700357/member/A21290378?ticket=ST...

~~~~json
{
	"pageSize" : 25,
	"pageNumber" : 1,
	"pageCount" : 1,
	"result" : {
		"classType" : "AtomContentViewMember",
		"atom" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/AUI/A21290378",
		"name" : "Herbertia tigridioides",
		"contentViewMemberAttributes" : [],
		"ui" : "A21290378"
	}
}
~~~~