title=Retrieving UMLS Atom Parents and Children
date=2016-02-25
updated=2016-06-28
type=page
status=published
category=Retrieving UMLS Data
navorder=5
~~~~~~


[URIs](#uris) | [Query Parameters](#query-parameters) | [Sample Output](#sample-output)

URIs with /parents or /children support the following use cases:

*  Retrieve the immediate parents of a known UMLS atom.
*  Retrieve the immediate children of a known UMLS atom.

Note that 'current' in the URI can always be used to search against the latest UMLS publication.
You may use any valid UMLS release back to 2008AA in your URI if you would like to search against a particular version of the UMLS.


### URIs

**The base URI is https://uts-ws.nlm.nih.gov/rest**

Sample URI|Description|Returned JSON Object classType
--- | ---
/content/current/AUI/A10134087/parents|Retrieves parents of a UMLS atom|Atom
/content/current/AUI/A10134087/children|Retrieves children of a UMLS atom|Atom


### Query Parameters

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
ticket | Y | A single-use service ticket is required for each call to the API. See [authentication](../authentication.html) for more information | n/a | n/a | n/a
pageNumber | N | Whole number that specifies which page of results to fetch. | 1,2,3, etc | 1 | n/a
pageSize | N | Whole number that specifies the number of results to include per page. | 1,2,3, etc | 25 | n/a


### Sample Output

Sample output for https://uts-ws.nlm.nih.gov/rest/content/current/AUI/A10134087/parents?ticket=ST...

~~~~json
{
	"pageSize" : 25,
	"pageNumber" : 1,
	"pageCount" : 1,
	"result" : [{
			"classType" : "Atom",
			"ui" : "A19720766",
			"suppressible" : "false",
			"obsolete" : "false",
			"rootSource" : "HL7V3.0",
			"termType" : "CSY",
			"code" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/HL7V3.0/RouteOfAdministration",
			"concept" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/CUI/C0013153",
			"sourceConcept" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/HL7V3.0/2.16.840.1.113883.5.112",
			"sourceDescriptor" : "NONE",
			"attributes" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/AUI/A19720766/attributes",
			"parents" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/AUI/A19720766/parents",
			"ancestors" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/AUI/A19720766/ancestors",
			"children" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/AUI/A19720766/children",
			"descendants" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/AUI/A19720766/descendants",
			"relations" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/AUI/A19720766/relations",
			"definitions" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/AUI/A19720766/definitions",
			"name" : "RouteOfAdministration",
			"language" : "ENG",
			"contentViewMemberships" : []
		}
	]
}
~~~~


