title=Retrieving UMLS Atom Ancestors and Descendants
date=2016-02-24
updated=2016-02-24
type=page
status=published
category=Retrieving UMLS Data
navorder=6
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

*Calls using codes from HL7V2.5 and HL7V3.0 return output with an "Atom" JSON Object classType.

### Query Parameters

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
ticket | Y | A single-use service ticket is required for each call to the API. See [authentication](../authentication.html) for more information | n/a | n/a | n/a
pageNumber | N | Whole number that specifies which page of results to fetch. | 1,2,3, etc | 1 | n/a
pageSize | N | Whole number that specifies the number of results to include per page. | 1,2,3, etc | 25 | n/a


### Sample Output

Sample output for /content/current/source/SNOMEDCT_US/9468002/ancestors?ticket=ST...

~~~~json
{
    "pageSize": 25,
    "pageNumber": 1,
    "pageCount": 2,
    "result": [
        {
            "classType": "SourceAtomCluster",
            "ui": "105606008",
            "suppressible": false,
            "obsolete": false,
            "rootSource": "SNOMEDCT_US",
            "atomCount": 3,
            "cVMemberCount": 0,
            "attributes": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/105606008/attributes",
            "atoms": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/105606008/atoms",
            "descendants": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/105606008/descendants",
            "ancestors": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/105606008/ancestors",
            "parents": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/105606008/parents",
            "children": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/105606008/children",
            "relations": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/105606008/relations",
            "definitions": "NONE",
            "concepts": "https://uts-ws.nlm.nih.gov/rest/search/2015AB?string=105606008&sabs=SNOMEDCT_US&searchType=exact&inputType=sourceUi",
            "defaultPreferredAtom": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/105606008/atoms/preferred",
            "name": "Injury of musculoskeletal system"
        },
        {
            "classType": "SourceAtomCluster",
            "ui": "105969002",
            "suppressible": false,
            "obsolete": false,
            "rootSource": "SNOMEDCT_US",
            "atomCount": 5,
            "cVMemberCount": 0,
            "attributes": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/105969002/attributes",
            "atoms": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/105969002/atoms",
            "descendants": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/105969002/descendants",
            "ancestors": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/105969002/ancestors",
            "parents": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/105969002/parents",
            "children": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/105969002/children",
            "relations": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/105969002/relations",
            "definitions": "NONE",
            "concepts": "https://uts-ws.nlm.nih.gov/rest/search/2015AB?string=105969002&sabs=SNOMEDCT_US&searchType=exact&inputType=sourceUi",
            "defaultPreferredAtom": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/105969002/atoms/preferred",
            "name": "Disorder of connective tissue"
        },
        {
            "classType": "SourceAtomCluster",
            "ui": "106028002",
            "suppressible": false,
            "obsolete": false,
            "rootSource": "SNOMEDCT_US",
            "atomCount": 5,
            "cVMemberCount": 0,
            "attributes": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/106028002/attributes",
            "atoms": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/106028002/atoms",
            "descendants": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/106028002/descendants",
            "ancestors": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/106028002/ancestors",
            "parents": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/106028002/parents",
            "children": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/106028002/children",
            "relations": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/106028002/relations",
            "definitions": "NONE",
            "concepts": "https://uts-ws.nlm.nih.gov/rest/search/2015AB?string=106028002&sabs=SNOMEDCT_US&searchType=exact&inputType=sourceUi",
            "defaultPreferredAtom": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/106028002/atoms/preferred",
            "name": "Musculoskeletal finding"
        },
...
    ]
}
~~~~


