title=Retrieving UMLS Atom Ancestors and Descendants
date=2016-02-25
updated=2016-06-28
type=page
status=published
category=Retrieving UMLS Data
navorder=6
~~~~~~


[URIs](#uris) | [Query Parameters](#query-parameters) | [Sample Output](#sample-output)

URIs with /ancestors or /descendants support the following use cases:

*  Retrieve all ancestors of a known UMLS atom.
*  Retrieve all descendants of a known UMLS atom.

Note that 'current' in the URI can always be used to search against the latest UMLS publication.
You may use any valid UMLS release back to 2008AA in your URI if you would like to search against a particular version of the UMLS.


### URIs

**The base URI is https://uts-ws.nlm.nih.gov/rest**

Sample URI|Description|Returned JSON Object classType
--- | ---
/content/current/AUI/A10134087/ancestors|Retrieves ancestors of a UMLS atom|Atom
/content/current/AUI/A10134087/descendants|Retrieves descendants of a UMLS atom|Atom


### Query Parameters

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
apiKey | Y | An API key is required for each call to the API. Visit [your UTS profile](https://uts.nlm.nih.gov/uts/profile) to obtain your API key. | n/a | n/a | n/a
pageNumber | N | Whole number that specifies which page of results to fetch. | 1,2,3, etc | 1 | n/a
pageSize | N | Whole number that specifies the number of results to include per page. | 1,2,3, etc | 25 | n/a


### Sample Output

Sample output for https://uts-ws.nlm.nih.gov/rest/content/current/AUI/A10134087/descendants?apiKey=YOUR_APIKEY...

~~~~json
{
	"pageSize" : 25,
	"pageNumber" : 1,
	"pageCount" : 15,
	"result" : [{
			"classType" : "Atom",
			"ui" : "A10133773",
			"suppressible" : "false",
			"obsolete" : "false",
			"rootSource" : "HL7V3.0",
			"termType" : "PT",
			"code" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/HL7V3.0/_IntrabursalRoute",
			"concept" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/CUI/C1522205",
			"sourceConcept" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/HL7V3.0/21172",
			"sourceDescriptor" : "NONE",
			"attributes" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/AUI/A10133773/attributes",
			"parents" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/AUI/A10133773/parents",
			"ancestors" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/AUI/A10133773/ancestors",
			"children" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/AUI/A10133773/children",
			"descendants" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/AUI/A10133773/descendants",
			"relations" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/AUI/A10133773/relations",
			"name" : "IntrabursalRoute",
			"language" : "ENG",
			"contentViewMemberships" : []
		}, {
			"classType" : "Atom",
			"ui" : "A8317632",
			"suppressible" : "false",
			"obsolete" : "false",
			"rootSource" : "HL7V3.0",
			"termType" : "PT",
			"code" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/HL7V3.0/IBURSINJ",
			"concept" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/CUI/C0848586",
			"sourceConcept" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/HL7V3.0/14643",
			"sourceDescriptor" : "NONE",
			"attributes" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/AUI/A8317632/attributes",
			"parents" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/AUI/A8317632/parents",
			"ancestors" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/AUI/A8317632/ancestors",
			"children" : "NONE",
			"descendants" : null,
			"relations" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/AUI/A8317632/relations",
			"name" : "Injection, intrabursal",
			"language" : "ENG",
			"contentViewMemberships" : []
		}, {
			"classType" : "Atom",
			"ui" : "A10133791",
			"suppressible" : "false",
			"obsolete" : "false",
			"rootSource" : "HL7V3.0",
			"termType" : "PT",
			"code" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/HL7V3.0/_IntraepidermalRoute",
			"concept" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/CUI/C1512941",
			"sourceConcept" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/HL7V3.0/21190",
			"sourceDescriptor" : "NONE",
			"attributes" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/AUI/A10133791/attributes",
			"parents" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/AUI/A10133791/parents",
			"ancestors" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/AUI/A10133791/ancestors",
			"children" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/AUI/A10133791/children",
			"descendants" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/AUI/A10133791/descendants",
			"relations" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/AUI/A10133791/relations",
			"name" : "IntraepidermalRoute",
			"language" : "ENG",
			"contentViewMemberships" : []
		}, 
...
	]
}
~~~~


