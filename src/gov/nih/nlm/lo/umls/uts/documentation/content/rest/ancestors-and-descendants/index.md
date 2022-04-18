title=Retrieving Source-Asserted Ancestors and Descendants
date=2015-08-28
updated=2016-06-28
type=page
status=published
category=Retrieving Source-Asserted Data
navorder=3
~~~~~~


[URIs](#uris) | [Query Parameters](#query-parameters) | [Sample Output](#sample-output)

URIs with /ancestors or /descendants support the following use cases:

*  Retrieve all ancestors of a known source asserted identifier.
*  Retrieve all descendants of a known source asserted identifier.

Note that 'current' in the URI can always be used to search against the latest UMLS publication.
You may use any valid UMLS release back to 2008AA in your URI if you would like to search against a particular version of the UMLS.


### URIs

**The base URI is https://uts-ws.nlm.nih.gov/rest**

Sample URI|Description|Returned JSON Object classType
--- | ---
/content/current/source/SNOMEDCT_US/9468002/ancestors|Retrieves ancestors of a source-asserted identifier|SourceAtomCluster*
/content/current/source/SNOMEDCT_US/9468002/descendants|Retrieves descendants of a source-asserted identifier|SourceAtomCluster*

*Calls using codes from HL7V2.5 and HL7V3.0 return output with an "Atom" JSON Object classType*.

### Query Parameters

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
apiKey | Y | An API key is required for each call to the API. Visit [your UTS profile](https://uts.nlm.nih.gov/uts/profile) to obtain your API key. | n/a | n/a | n/a
pageNumber | N | Whole number that specifies which page of results to fetch. | 1,2,3, etc | 1 | n/a
pageSize | N | Whole number that specifies the number of results to include per page. | 1,2,3, etc | 25 | n/a


### Sample Output

Sample output for https://uts-ws.nlm.nih.gov/rest/content/current/source/SNOMEDCT_US/9468002/descendants?apiKey=YOUR_APIKEY...

~~~~.json
{
	"pageSize" : 25,
	"pageNumber" : 1,
	"pageCount" : 2,
	"result" : [{
			"classType" : "SourceAtomCluster",
			"ui" : "10934241000119100",
			"suppressible" : false,
			"obsolete" : false,
			"rootSource" : "SNOMEDCT_US",
			"atomCount" : 2,
			"cVMemberCount" : 0,
			"attributes" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/10934241000119100/attributes",
			"atoms" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/10934241000119100/atoms",
			"descendants" : "NONE",
			"ancestors" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/10934241000119100/ancestors",
			"parents" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/10934241000119100/parents",
			"children" : "NONE",
			"relations" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/10934241000119100/relations",
			"definitions" : "NONE",
			"concepts" : "https://uts-ws.nlm.nih.gov/rest/search/2016AA?string=10934241000119100&sabs=SNOMEDCT_US&searchType=exact&inputType=sourceUi",
			"defaultPreferredAtom" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/10934241000119100/atoms/preferred",
			"subsetMemberships" : [{
					"memberUri" : "https://uts-ws.nlm.nih.gov/rest/subsets/2016AA/source/SNOMEDCT_US/6011000124106/member/10934241000119100",
					"name" : "ICD-10-CM complex map reference set",
					"uri" : "https://uts-ws.nlm.nih.gov/rest/subsets/2016AA/source/SNOMEDCT_US/6011000124106"
				}
			],
			"contentViewMemberships" : [{
					"memberUri" : "https://uts-ws.nlm.nih.gov/rest/content-views/2016AA/CUI/C3812142/member/10934241000119100",
					"name" : "SNOMEDCT US Extension Subset",
					"uri" : "https://uts-ws.nlm.nih.gov/rest/content-views/2016AA/CUI/C3812142"
				}
			],
			"name" : "Closed fracture of pisiform bone of left wrist"
		}, {
			"classType" : "SourceAtomCluster",
			"ui" : "10934281000119105",
			"suppressible" : false,
			"obsolete" : false,
			"rootSource" : "SNOMEDCT_US",
			"atomCount" : 3,
			"cVMemberCount" : 0,
			"attributes" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/10934281000119105/attributes",
			"atoms" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/10934281000119105/atoms",
			"descendants" : "NONE",
			"ancestors" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/10934281000119105/ancestors",
			"parents" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/10934281000119105/parents",
			"children" : "NONE",
			"relations" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/10934281000119105/relations",
			"definitions" : "NONE",
			"concepts" : "https://uts-ws.nlm.nih.gov/rest/search/2016AA?string=10934281000119105&sabs=SNOMEDCT_US&searchType=exact&inputType=sourceUi",
			"defaultPreferredAtom" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/10934281000119105/atoms/preferred",
			"subsetMemberships" : [{
					"memberUri" : "https://uts-ws.nlm.nih.gov/rest/subsets/2016AA/source/SNOMEDCT_US/6011000124106/member/10934281000119105",
					"name" : "ICD-10-CM complex map reference set",
					"uri" : "https://uts-ws.nlm.nih.gov/rest/subsets/2016AA/source/SNOMEDCT_US/6011000124106"
				}
			],
			"contentViewMemberships" : [{
					"memberUri" : "https://uts-ws.nlm.nih.gov/rest/content-views/2016AA/CUI/C3812142/member/10934281000119105",
					"name" : "SNOMEDCT US Extension Subset",
					"uri" : "https://uts-ws.nlm.nih.gov/rest/content-views/2016AA/CUI/C3812142"
				}
			],
			"name" : "Closed fracture of capitate bone of right wrist"
		}, {
			"classType" : "SourceAtomCluster",
			"ui" : "10934321000119100",
			"suppressible" : false,
			"obsolete" : false,
			"rootSource" : "SNOMEDCT_US",
			"atomCount" : 3,
			"cVMemberCount" : 0,
			"attributes" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/10934321000119100/attributes",
			"atoms" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/10934321000119100/atoms",
			"descendants" : "NONE",
			"ancestors" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/10934321000119100/ancestors",
			"parents" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/10934321000119100/parents",
			"children" : "NONE",
			"relations" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/10934321000119100/relations",
			"definitions" : "NONE",
			"concepts" : "https://uts-ws.nlm.nih.gov/rest/search/2016AA?string=10934321000119100&sabs=SNOMEDCT_US&searchType=exact&inputType=sourceUi",
			"defaultPreferredAtom" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/10934321000119100/atoms/preferred",
			"subsetMemberships" : [{
					"memberUri" : "https://uts-ws.nlm.nih.gov/rest/subsets/2016AA/source/SNOMEDCT_US/6011000124106/member/10934321000119100",
					"name" : "ICD-10-CM complex map reference set",
					"uri" : "https://uts-ws.nlm.nih.gov/rest/subsets/2016AA/source/SNOMEDCT_US/6011000124106"
				}
			],
			"contentViewMemberships" : [{
					"memberUri" : "https://uts-ws.nlm.nih.gov/rest/content-views/2016AA/CUI/C3812142/member/10934321000119100",
					"name" : "SNOMEDCT US Extension Subset",
					"uri" : "https://uts-ws.nlm.nih.gov/rest/content-views/2016AA/CUI/C3812142"
				}
			],
			"name" : "Closed fracture of capitate bone of left wrist"
		}, 
...
	]
}
~~~~


