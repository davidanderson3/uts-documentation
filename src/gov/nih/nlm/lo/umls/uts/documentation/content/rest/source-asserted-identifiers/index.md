title=Retrieving Source-Asserted Information
date=2015-07-01
updated=2016-06-28
type=page
status=published
category=Retrieving Source-Asserted Data
navorder=1
~~~~~~


[URIs](#uris) | [Query Parameters](#query-parameters) | [Sample Output](#sample-output)

URIs with /source/{source}/{id} support the following use cases:

*  Retrieve information (name, attributes, term types, number of atoms, memberships etc) for a source concept, source descriptor or code from latest UMLS version or a specific release.
*  Retrieve atoms for a known source-asserted identifier.
*  Retrieve immediate parents of a known source-asserted identifier.
*  Retrieve immediate children of a known source-asserted identifier.

Note that 'current' in the URI can always be used to search against the latest UMLS publication.
You may use any valid UMLS release back to 2008AA in your URI if you would like to search against a particular version of the UMLS.

### URIs

**The base URI is https://uts-ws.nlm.nih.gov/rest**

Sample URI|Description|Returned JSON Object classType
--- | ---
/content/current/source/SNOMEDCT_US/9468002 | Retrieves Source Concept | SourceAtomCluster
/content/current/source/MSH/D015242 | Retrieves Source Descriptor | SourceAtomCluster
/content/current/source/LNC/54112-8 | Retrieves Code | SourceAtomCluster
[/content/current/source/SNOMEDCT_US/9468002/atoms](/rest/atoms/index.html)| Retrieve atoms in a source-asserted identifier | Atom
[/content/current/source/SNOMEDCT_US/9468002/parents](/rest/parents-and-children/index.html) | Retrieve immediate parents of a source-asserted identifier | SourceAtomCluster
[/content/current/source/SNOMEDCT_US/9468002/children](/rest/parents-and-children/index.html) | Retrieve immediate children of source-asserted identifier | SourceAtomCluster
[/content/current/source/SNOMEDCT_US/9468002/ancestors](/rest/ancestors-and-descendants/index.html) | Retrieve all ancestors of a source-asserted identifier | SourceAtomCluster
[/content/current/source/SNOMEDCT_US/9468002/descendants](/rest/ancestors-and-descendants/index.html) | Retrieve all descendants of source-asserted identifier | SourceAtomCluster
[/content/current/source/SNOMEDCT_US/9468002/attributes](/rest/source-asserted-identifiers/attributes/index.html) | Retrieves information about source-asserted attributes | Attribute

### Query Parameters

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
apiKey | Y | An API key is required for each call to the API. Visit [your UTS profile](https://uts.nlm.nih.gov/uts/profile) to obtain your API key. | n/a | n/a | n/a


### Sample Output

Sample output for https://uts-ws.nlm.nih.gov/rest/content/current/source/SNOMEDCT_US/9468002?apiKey=YOUR_APIKEY...

~~~~json
{
	"pageSize" : 25,
	"pageNumber" : 1,
	"pageCount" : 1,
	"result" : {
		"classType" : "SourceAtomCluster",
		"ui" : "9468002",
		"suppressible" : false,
		"obsolete" : false,
		"rootSource" : "SNOMEDCT_US",
		"atomCount" : 8,
		"cVMemberCount" : 0,
		"attributes" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/9468002/attributes",
		"atoms" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/9468002/atoms",
		"descendants" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/9468002/descendants",
		"ancestors" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/9468002/ancestors",
		"parents" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/9468002/parents",
		"children" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/9468002/children",
		"relations" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/9468002/relations",
		"definitions" : "NONE",
		"concepts" : "https://uts-ws.nlm.nih.gov/rest/search/2016AA?string=9468002&sabs=SNOMEDCT_US&searchType=exact&inputType=sourceUi",
		"defaultPreferredAtom" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/9468002/atoms/preferred",
		"name" : "Closed fracture of carpal bone"
	}
}
~~~~
