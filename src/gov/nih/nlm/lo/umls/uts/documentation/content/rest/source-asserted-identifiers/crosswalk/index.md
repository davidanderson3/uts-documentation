title=Crosswalking Vocabularies Using CUIs
date=2016-06-27
updated=2016-07-07
type=page
status=published
category=Retrieving Source-Asserted Data
navorder=7
~~~~~~

[URIs](#uris) | [Query Parameters](#query-parameters) | [Sample Output](#sample-output) | [Example Python Script](/rest/rest-api-cookbook/python-scripts.html#crosswalking-vocabularies-using-cuis)

URIs with /crosswalk support the following use cases:

*  Retrieve all source-asserted identifiers that share a UMLS CUI with a particular code.
*  Retrieve all source-asserted identifiers from a particular source that share a CUI with a particular code from another source.
*  Generate a mapping between two different UMLS sources that can be used as a starting point for curating more context-specific mappings. 

A common use case of the CUIs in the UMLS is as a sort of 'bridge of synonymy' between code sets. For a given source-asserted code, the crosswalk endpoint will return codes from other sources that have UMLS-asserted synonymy. It is important to note that the synonymy asserted by the UMLS in the MRCONSO.RRF files (and the APIs derived from them) has not been rigorously tested and maintained in actual clinical care. With that disclaimer, users often have questions such as 'I have a code from vocabulary x, what is the equivalent code from vocabulary y according to UMLS synonymy?'. Although UMLS CUIs can be used as a starting point, results should be carefully reviewed for relevancy in your use case.

The following GET call will crosswalk the [Human Phenotype Ontology](https://www.nlm.nih.gov/research/umls/sourcereleasedocs/current/HPO/) (HPO) code HP:0001947, 'Renal tubular acidosis', to see if there are any SNOMEDCT codes for which the UMLS has asserted synonymy. 

`https://uts-ws.nlm.nih.gov/rest/crosswalk/current/source/HPO/HP:0001947?targetSource=SNOMEDCT_US&apiKey=<your api key>`

This call will return all SNOMED codes that share a UMLS CUI with the HPO code HP:0001947, 'Renal tubular acidosis'. 

### URIs

**The base URI is https://uts-ws.nlm.nih.gov/rest**

Sample URI|Description|Returned JSON Object classType
--- | ---
/crosswalk/current/source/HPO/HP:0001947| Retrieves all codes that share a UMLS CUI with HP:0001947 | SourceAtomCluster
/crosswalk/current/source/HPO/HP:0001947?targetSource=SNOMEDCT_US| Retrieves all SNOMEDCT_US codes that share a UMLS CUI with HP:0001947 | SourceAtomCluster

Note that 'current' in the URI can always be used to search against the latest UMLS publication.
You may use any valid UMLS release back to 2008AA in your URI if you would like to search against a particular version of the UMLS.


### Query Parameters

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
apiKey | Y | An API key is required for each call to the API. Visit [your UTS profile](https://uts.nlm.nih.gov/uts/profile) to obtain your API key. | n/a | n/a | n/a
targetSource | N | Returns codes from the specified UMLS vocabulary | Any root source abbreviation in the UMLS. See the "Abbreviation" column for a list of [UMLS source vocabulary abbreviations](https://www.nlm.nih.gov/research/umls/sourcereleasedocs/index.html).  | All UMLS source vocabularies | Use a comma between each source abbreviation to specify more than one.
includeObsolete | N | Determines whether to return obsolete codes. | true,false | false | n/a
pageNumber | N | Whole number that specifies which page of results to fetch. | 1,2,3, etc | 1 | n/a
pageSize | N | Whole number that specifies the number of results to include per page. | 1,2,3, etc | 25 | n/a


### Sample Output

Sample output for https://uts-ws.nlm.nih.gov/rest/crosswalk/current/source/HPO/HP:0001947?targetSource=SNOMEDCT_US&apiKey=YOUR_APIKEY...

~~~~json
{
	"pageSize": 25,
	"pageNumber": 1,
	"pageCount": 1,
	"result": [
	{
		"classType": "SourceAtomCluster",
		"ui": "1776003",
		"suppressible": false,
		"obsolete": false,
		"rootSource": "SNOMEDCT_US",
		"atomCount": 8,
		"cVMemberCount": 0,
		"attributes": "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/1776003/attributes",
		"atoms": "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/1776003/atoms",
		"descendants": "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/1776003/descendants",
		"ancestors": "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/1776003/ancestors",
		"parents": "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/1776003/parents",
		"children": "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/1776003/children",
		"relations": "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/1776003/relations",
		"definitions": "NONE",
		"concepts": "https://uts-ws.nlm.nih.gov/rest/search/2016AA?string=1776003&sabs=SNOMEDCT_US&searchType=exact&inputType=sourceUi",
		"defaultPreferredAtom": "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/1776003/atoms/preferred",
		"subsetMemberships": [
			{
				"memberUri": "https://uts-ws.nlm.nih.gov/rest/subsets/2016AA/source/SNOMEDCT_US/900000000000498005/member/1776003",
				"name": "SNOMED RT ID simple map",
				"uri": "https://uts-ws.nlm.nih.gov/rest/subsets/2016AA/source/SNOMEDCT_US/900000000000498005"
			},
			{
				"memberUri": "https://uts-ws.nlm.nih.gov/rest/subsets/2016AA/source/SNOMEDCT_US/900000000000497000/member/1776003",
				"name": "CTV3 simple map",
				"uri": "https://uts-ws.nlm.nih.gov/rest/subsets/2016AA/source/SNOMEDCT_US/900000000000497000"
			},
			{
				"memberUri": "https://uts-ws.nlm.nih.gov/rest/subsets/2016AA/source/SNOMEDCT_US/447562003/member/1776003",
				"name": "ICD-10 complex map reference set",
				"uri": "https://uts-ws.nlm.nih.gov/rest/subsets/2016AA/source/SNOMEDCT_US/447562003"
			},
			{
				"memberUri": "https://uts-ws.nlm.nih.gov/rest/subsets/2016AA/source/SNOMEDCT_US/6011000124106/member/1776003",
				"name": "ICD-10-CM complex map reference set",
				"uri": "https://uts-ws.nlm.nih.gov/rest/subsets/2016AA/source/SNOMEDCT_US/6011000124106"
			}
		],
		"contentViewMemberships": [
			{
				"memberUri": "https://uts-ws.nlm.nih.gov/rest/content-views/2016AA/CUI/C2711988/member/1776003",
				"name": "CORE Problem List Subset of SNOMED CT",
				"uri": "https://uts-ws.nlm.nih.gov/rest/content-views/2016AA/CUI/C2711988"
			}
		],
		"name": "Renal tubular acidosis"
	}
	]
}
~~~~

