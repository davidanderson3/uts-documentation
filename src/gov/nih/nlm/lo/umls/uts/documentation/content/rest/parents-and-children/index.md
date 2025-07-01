title=Retrieving Source-Asserted Parents and Children
date=2015-07-06
updated=2016-06-28
type=page
status=published
category=Retrieving Source-Asserted Data
navorder=2
~~~~~~


[URIs](#uris) | [Query Parameters](#query-parameters) | [Sample Output](#sample-output)

URIs with /parents or /children support the following use cases:

*  Retrieve the immediate parents of a known source asserted identifier.
*  Retrieve all immediate children of a known source asserted identifier.

Note that 'current' in the URI can always be used to search against the latest UMLS publication.
You may use any valid UMLS release back to 2008AA in your URI if you would like to search against a particular version of the UMLS.


### URIs

**The base URI is https://uts-ws.nlm.nih.gov/rest**

Sample URI|Description|Returned JSON Object classType
--- | ---
/content/current/source/SNOMEDCT_US/9468002/parents| Retrieves parents a source-asserted identifier|SourceAtomCluster*
/content/current/source/SNOMEDCT_US/9468002/children| Retrieves children of a source-asserted identifier|SourceAtomCluster*

[Python example - Retrieve ancestors, descendants, parents, or children](/rest/rest-api-cookbook/python-scripts.html#retrieve-ancestors-descendants-parents-or-children)

*Calls using codes from HL7V2.5 and HL7V3.0 return output with an "Atom" JSON Object classType.

### Query Parameters

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
apiKey | Y | An API key is required for each call to the API. Visit [your UTS profile](https://uts.nlm.nih.gov/uts/profile) to obtain your API key. | n/a | n/a | n/a
pageNumber | N | Whole number that specifies which page of results to fetch. | 1,2,3, etc | 1 | n/a
pageSize | N | Whole number that specifies the number of results to include per page. | 1,2,3, etc | 200 | n/a


### Sample Output

Sample output for https://uts-ws.nlm.nih.gov/rest/content/current/source/SNOMEDCT_US/9468002/parents?apiKey=YOUR_APIKEY...

~~~~json
{
	"pageSize" : 200,
	"pageNumber" : 1,
	"pageCount" : 1,
	"result" : [{
			"classType" : "SourceAtomCluster",
			"ui" : "36991002",
			"suppressible" : false,
			"obsolete" : false,
			"rootSource" : "SNOMEDCT_US",
			"atomCount" : 5,
			"cVMemberCount" : 0,
			"attributes" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/36991002/attributes",
			"atoms" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/36991002/atoms",
			"descendants" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/36991002/descendants",
			"ancestors" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/36991002/ancestors",
			"parents" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/36991002/parents",
			"children" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/36991002/children",
			"relations" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/36991002/relations",
			"definitions" : "NONE",
			"concepts" : "https://uts-ws.nlm.nih.gov/rest/search/2016AA?string=36991002&sabs=SNOMEDCT_US&searchType=exact&inputType=sourceUi",
			"defaultPreferredAtom" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/36991002/atoms/preferred",
			"name" : "Closed fracture of upper limb"
		}, {
			"classType" : "SourceAtomCluster",
			"ui" : "82065001",
			"suppressible" : false,
			"obsolete" : false,
			"rootSource" : "SNOMEDCT_US",
			"atomCount" : 7,
			"cVMemberCount" : 0,
			"attributes" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/82065001/attributes",
			"atoms" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/82065001/atoms",
			"descendants" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/82065001/descendants",
			"ancestors" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/82065001/ancestors",
			"parents" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/82065001/parents",
			"children" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/82065001/children",
			"relations" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/82065001/relations",
			"definitions" : "NONE",
			"concepts" : "https://uts-ws.nlm.nih.gov/rest/search/2016AA?string=82065001&sabs=SNOMEDCT_US&searchType=exact&inputType=sourceUi",
			"defaultPreferredAtom" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/82065001/atoms/preferred",
			"name" : "Fracture of carpal bone"
		}
	]
}
~~~~


