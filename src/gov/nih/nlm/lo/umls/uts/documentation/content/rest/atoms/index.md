title=Retrieving UMLS Atoms
date=2015-06-12
updated=2021-07-29
type=page
status=published
category=Retrieving UMLS Data
navorder=4
~~~~~~


[URIs](#uris) | [Query Parameters](#query-parameters) | [Sample Output](#sample-output)

URIs with /atoms support the following use cases:

*  Retrieve all atoms of a UMLS concept (CUI) or source-asserted identifier.
*  Retrieve the default preferred atom of a UMLS CUI or source-asserted identifier.
*  Retrieve information about an individual atom (AUI).
*  Retrieve atom information, such as relations to other atoms, attributes, or definitions.
*  Retrieve membership information of an atom (to which CUI, code, or content view does an atom belong).
*  Retrieve atom information such as name,term type, language, and suppressibility/obsolescence.

Note that 'current' in the URI can always be used to search against the latest UMLS publication.
You may use any valid UMLS release back to 2008AA in your URI if you would like to search against a particular version of the UMLS.


### URIs
 
**The base URI is https://uts-ws.nlm.nih.gov/rest**

Sample URI|Description|Returned JSON Object classType
--- | --- | ---
/content/current/CUI/C0155502/atoms|Retrieves all atoms for C0155502 | Atom
/content/current/CUI/C0155502/atoms/preferred|Retrieves the default preferred atom of C0155502 | Atom
/content/current/CUI/C0155502/atoms?language=ENG|Retrieves all English language atoms for C0155502| Atom
/content/current/CUI/C0155502/atoms?sabs=SNOMEDCT_US,ICD9CM&ttys=PT | Retrieve SNOMEDCT_US and ICD9CM preferred terms in C0155502| Atom
/content/current/source/SNOMEDCT_US/111541001/atoms | Retrieve atoms belonging to SNOMED CT concept 111541001| Atom
/content/current/source/SNOMEDCT_US/111541001/atoms/preferred | Retrieve the default preferred atom belonging to SNOMED CT concept 111541001| Atom
/content/current/AUI/A8345234 | Retrieve information about AUI A8345234| Atom
[/content/current/AUI/A8345234/ancestors](../atoms/ancestors-and-descendants/index.html)|Retrieve ancestors of a UMLS atom|Atom
[/content/current/AUI/A8345234/descendants](../atoms/ancestors-and-descendants/index.html)|Retrieve descendants of a UMLS atom|Atom
[/content/current/AUI/A8345234/parents](../atoms/parents-and-children/index.html)|Retrieve parents of a UMLS atom|Atom
[/content/current/AUI/A8345234/children](../atoms/parents-and-children/index.html)|Retrieve children of a UMLS atom|Atom

### Query Parameters

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
apiKey | Y | An API key is required for each call to the API. Visit [your UTS profile](https://uts.nlm.nih.gov/uts/profile) to obtain your API key. | n/a | n/a | n/a
sabs| N | Comma-separated list of source vocabularies to include in your search | Any root source abbreviation in the UMLS. See the "Abbreviation" column for a list of [UMLS source vocabulary abbreviations](https://www.nlm.nih.gov/research/umls/sourcereleasedocs/index.html).  | All UMLS source vocabularies | Use a comma between each source abbreviation to specify more than one.
ttys | N | One or more term types | Any valid [term type](https://www.nlm.nih.gov/research/umls/knowledge_sources/metathesaurus/release/abbreviations.html#TTYC) in the UMLS | All term types | Use a comma between each term type to specify more than one.
language | N | Retrieve only atoms that have a specific language | Any 3 letter language abbreviation in the UMLS, such as "ENG","FRE","SPA","GER","DUT","JPN", etc | All languages are returned by default | Currently filtering by one language is supported.
includeObsolete | N |  Include content that is obsolete according to the content provider or NLM. | true or false | false (except for atoms/preferred, which defaults to true) | n/a
includeSuppressible | N |  Include content that is suppressible according to NLM Editors.| true or false | false (except for atoms/preferred, which defaults to true) | n/a
pageNumber | N | Whole number that specifies which page of results to fetch. | 1,2,3, etc | 1 | n/a
pageSize | N | Whole number that specifies the number of results to include per page. | 1,2,3, etc | 25 | n/a


### Sample Output

Sample output for https://uts-ws.nlm.nih.gov/rest/content/current/CUI/C0155502/atoms?ttys=PT&sabs=SNOMEDCT_US%2CICD9CM&apiKey=YOUR_APIKEY...

~~~~json
{
	"pageSize" : 25,
	"pageNumber" : 1,
	"pageCount" : 1,
	"result" : [{
			"classType" : "Atom",
			"ui" : "A8345234",
			"suppressible" : "false",
			"obsolete" : "false",
			"rootSource" : "ICD9CM",
			"termType" : "PT",
			"code" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/ICD9CM/386.11",
			"concept" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/CUI/C0155502",
			"sourceConcept" : "NONE",
			"sourceDescriptor" : "NONE",
			"attributes" : "NONE",
			"parents" : "NONE",
			"ancestors" : null,
			"children" : "NONE",
			"descendants" : null,
			"relations" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/AUI/A8345234/relations",
			"name" : "Benign paroxysmal positional vertigo",
			"language" : "ENG",
			"contentViewMemberships" : [{
					"memberUri" : "https://uts-ws.nlm.nih.gov/rest/content-views/2016AA/CUI/C1700357/member/A8345234",
					"uri" : "https://uts-ws.nlm.nih.gov/rest/content-views/2016AA/CUI/C1700357",
					"name" : "MetaMap NLP View"
				}
			]
		}, {
			"classType" : "Atom",
			"ui" : "A2892933",
			"suppressible" : "false",
			"obsolete" : "false",
			"rootSource" : "SNOMEDCT_US",
			"termType" : "PT",
			"code" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/111541001",
			"concept" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/CUI/C0155502",
			"sourceConcept" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/111541001",
			"sourceDescriptor" : "NONE",
			"attributes" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/AUI/A2892933/attributes",
			"parents" : "NONE",
			"ancestors" : null,
			"children" : "NONE",
			"descendants" : null,
			"relations" : "NONE",
			"name" : "Benign paroxysmal positional vertigo",
			"language" : "ENG",
			"contentViewMemberships" : [{
					"memberUri" : "https://uts-ws.nlm.nih.gov/rest/content-views/2016AA/CUI/C1700357/member/A2892933",
					"uri" : "https://uts-ws.nlm.nih.gov/rest/content-views/2016AA/CUI/C1700357",
					"name" : "MetaMap NLP View"
				}
			]
		}, {
			"classType" : "Atom",
			"ui" : "A3101021",
			"suppressible" : "false",
			"obsolete" : "false",
			"rootSource" : "SNOMEDCT_US",
			"termType" : "PT",
			"code" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/232285008",
			"concept" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/CUI/C0155502",
			"sourceConcept" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/source/SNOMEDCT_US/232285008",
			"sourceDescriptor" : "NONE",
			"attributes" : "https://uts-ws.nlm.nih.gov/rest/content/2016AA/AUI/A3101021/attributes",
			"parents" : "NONE",
			"ancestors" : null,
			"children" : "NONE",
			"descendants" : null,
			"relations" : "NONE",
			"name" : "Benign recurrent vertigo",
			"language" : "ENG",
			"contentViewMemberships" : [{
					"memberUri" : "https://uts-ws.nlm.nih.gov/rest/content-views/2016AA/CUI/C1700357/member/A3101021",
					"uri" : "https://uts-ws.nlm.nih.gov/rest/content-views/2016AA/CUI/C1700357",
					"name" : "MetaMap NLP View"
				}
			]
		}
	]
}
~~~~

