title=Retrieving Source-Asserted Subsets
date=2015-09-30
updated=2016-06-28
type=page
status=published
category=Retrieving Source-Asserted Data
navorder=5
~~~~~~


[URIs](#uris) | [Query Parameters](#query-parameters) | [Sample Output](#sample-output)

URIs with /subsets support the following use cases:

* Retrieve all subsets for a known UMLS Release. 
* Retrieve information (name, description, member count, etc.) for a known subset.
* Retrieve all attributes of a known subset.
* Retrieve all members of a known subset.
* Retrieve all attributes for a member of a known subset.


Note that 'current' in the URI can always be used to search against the latest UMLS publication.
You may use any valid UMLS release back to 2008AA in your URI if you would like to search against a particular version of the UMLS.


### URIs

**The base URI is https://uts-ws.nlm.nih.gov/rest**

Sample URI|Description|Returned JSON Object classType
--- | ---
/subsets/current | Retrieves information about all subsets from the current release | Subset
/subsets/current/source/SNOMEDCT_US/6011000124106 | Retrieves information for a SNOMED CT subset | Subset
/subsets/current/source/SNOMEDCT_US/6011000124106/members | Retrieves members of a SNOMED CT subset | SourceConceptSubsetMember
/subsets/current/source/SNOMEDCT_US/6011000124106/member/89361000119103 | Retrieves an individual member of a SNOMED CT subset | SourceConceptSubsetMember


### Query Parameters

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
ticket | Y | A single-use service ticket is required for each call to the API. See [authentication](../../authentication.html) for more information | n/a | n/a | n/a
pageNumber | N | Whole number that specifies which page of results to fetch. | 1,2,3, etc | 1 | n/a
pageSize | N | Whole number that specifies the number of results to include per page. | 1,2,3, etc | 25 | n/a
language | N | 3-letter abbreviation for language | ENG, SPA, GER, etc | n/a | n/a

### Sample Output

Sample output for https://uts-ws.nlm.nih.gov/rest/subsets/current?ticket=ST...

~~~~json
{
	"pageSize" : 25,
	"pageNumber" : 1,
	"pageCount" : 2,
	"result" : [{
			"classType" : "Subset",
			"ui" : "C3853926",
			"sourceUi" : "900000000000534007",
			"rootSource" : "SCTSPA",
			"name" : "conjunto de referencias de dependencia entre módulos",
			"description" : "conjunto de referencias de dependencia entre módulos",
			"attributeCount" : 1,
			"atomMemberCount" : 0,
			"sourceConceptMemberCount" : 4,
			"relationMemberCount" : 0,
			"uri" : "https://uts-ws.nlm.nih.gov/rest/subsets/2016AA/source/SCTSPA/900000000000534007",
			"subsetMembers" : "https://uts-ws.nlm.nih.gov/rest/subsets/2016AA/source/SCTSPA/900000000000534007/members",
			"subsetAttributes" : [{
					"classType" : "Attribute",
					"ui" : "ATM283",
					"sourceUi" : "NONE",
					"rootSource" : "SCTSPA",
					"name" : "LANG",
					"value" : "SPA"
				}
			]
		}, {
			"classType" : "Subset",
			"ui" : "C3853923",
			"sourceUi" : "450828004",
			"rootSource" : "SCTSPA",
			"name" : "conjunto de referencias de lenguaje castellano para América Latina",
			"description" : "conjunto de referencias de lenguaje castellano para América Latina",
			"attributeCount" : 1,
			"atomMemberCount" : 1041168,
			"sourceConceptMemberCount" : 0,
			"relationMemberCount" : 0,
			"uri" : "https://uts-ws.nlm.nih.gov/rest/subsets/2016AA/source/SCTSPA/450828004",
			"subsetMembers" : "https://uts-ws.nlm.nih.gov/rest/subsets/2016AA/source/SCTSPA/450828004/members",
			"subsetAttributes" : [{
					"classType" : "Attribute",
					"ui" : "ATM262",
					"sourceUi" : "NONE",
					"rootSource" : "SCTSPA",
					"name" : "LANG",
					"value" : "SPA"
				}
			]
		}, {
			"classType" : "Subset",
			"ui" : "C3853925",
			"sourceUi" : "900000000000456007",
			"rootSource" : "SCTSPA",
			"name" : "conjunto de referencias descriptivas de la estructura de otros conjuntos de referencias",
			"description" : "conjunto de referencias descriptivas de la estructura de otros conjuntos de referencias",
			"attributeCount" : 1,
			"atomMemberCount" : 0,
			"sourceConceptMemberCount" : 0,
			"relationMemberCount" : 0,
			"uri" : "https://uts-ws.nlm.nih.gov/rest/subsets/2016AA/source/SCTSPA/900000000000456007",
			"subsetMembers" : "https://uts-ws.nlm.nih.gov/rest/subsets/2016AA/source/SCTSPA/900000000000456007/members",
			"subsetAttributes" : [{
					"classType" : "Attribute",
					"ui" : "ATM274",
					"sourceUi" : "NONE",
					"rootSource" : "SCTSPA",
					"name" : "LANG",
					"value" : "SPA"
				}
			]
		}, 
...
	]
}
~~~~

Sample output for https://uts-ws.nlm.nih.gov/rest/subsets/current/source/SNOMEDCT_US/442311000124105/members?ticket=ST...

~~~~json
{
	"pageSize" : 25,
	"pageNumber" : 1,
	"pageCount" : 6,
	"result" : [{
			"classType" : "SourceConceptSubsetMember",
			"name" : "Intravascular route",
			"attributeCount" : 0,
			"ui" : "AT199486277",
			"sourceUi" : "445755006",
			"rootSource" : "SNOMEDCT_US",
			"sourceConcept" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/445755006",
			"obsolete" : false,
			"subsetMemberAttributes" : []
		}, {
			"classType" : "SourceConceptSubsetMember",
			"name" : "Intrabiliary route",
			"attributeCount" : 0,
			"ui" : "AT200860004",
			"sourceUi" : "404819002",
			"rootSource" : "SNOMEDCT_US",
			"sourceConcept" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/404819002",
			"obsolete" : false,
			"subsetMemberAttributes" : []
		}, {
			"classType" : "SourceConceptSubsetMember",
			"name" : "Sublingual route",
			"attributeCount" : 0,
			"ui" : "AT199923610",
			"sourceUi" : "37839007",
			"rootSource" : "SNOMEDCT_US",
			"sourceConcept" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/37839007",
			"obsolete" : false,
			"subsetMemberAttributes" : []
		}, 
...
	]
}
~~~~

Sample output for https://uts-ws.nlm.nih.gov/rest/subsets/current/source/SNOMEDCT_US/6011000124106/member/89361000119103?ticket=ST...

~~~~json
{
	"pageSize" : 25,
	"pageNumber" : 1,
	"pageCount" : 1,
	"result" : {
		"classType" : "SourceConceptSubsetMember",
		"name" : "Mild developmental articulation disorder",
		"attributeCount" : 7,
		"ui" : "AT199566985",
		"sourceUi" : "89361000119103",
		"rootSource" : "SNOMEDCT_US",
		"sourceConcept" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/89361000119103",
		"obsolete" : false,
		"subsetMemberAttributes" : [{
				"classType" : "Attribute",
				"ui" : "ATM37541478",
				"sourceUi" : "0c9ff6e0-ca17-5d8e-930a-0bc839769e34",
				"rootSource" : "SNOMEDCT_US",
				"name" : "MAPGROUP",
				"value" : "1"
			}, {
				"classType" : "Attribute",
				"ui" : "ATM37541479",
				"sourceUi" : "0c9ff6e0-ca17-5d8e-930a-0bc839769e34",
				"rootSource" : "SNOMEDCT_US",
				"name" : "MAPADVICE",
				"value" : "ALWAYS F80.0"
			}, {
				"classType" : "Attribute",
				"ui" : "ATM37541480",
				"sourceUi" : "0c9ff6e0-ca17-5d8e-930a-0bc839769e34",
				"rootSource" : "SNOMEDCT_US",
				"name" : "MAPTARGET",
				"value" : "F80.0"
			}, 
...
		]
	}
}
~~~~