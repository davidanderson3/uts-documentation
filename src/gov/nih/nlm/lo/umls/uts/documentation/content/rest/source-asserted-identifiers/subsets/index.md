title=Retrieving Source-Asserted Subsets
date=2015-09-30
updated=2015-09-30
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
/content/current/subsets | Retrieves information about all subsets from the current release | Subset
/content/2015AA/subsets/source/SNOMEDCT_US/6011000124106 | Retrieves information for a SNOMED CT subset | Subset
/content/2015AA/subsets/source/SNOMEDCT_US/6011000124106/attributes | Retrieves attributes for a SNOMED CT subset | Attribute
/content/2015AA/subsets/source/SNOMEDCT_US/6011000124106/members | Retrieves members of a SNOMED CT subset | SourceConceptSubsetMember
/content/2015AA/subsets/source/SNOMEDCT_US/6011000124106/members/77147000/attributes | Retrieves attribute information for a specified member of a SNOMED CT subset | Attribute


### Query Parameters

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
ticket | Y | A single-use service ticket is required for each call to the API. See [authentication](../authentication.html) for more information | n/a | n/a | n/a
pageNumber | N | Whole number that specifies which page of results to fetch. | 1,2,3, etc | 1 | n/a
pageSize | N | Whole number that specifies the number of results to include per page. | 1,2,3, etc | 25 | n/a


### Sample Output

Sample output for /content/2015AA/subsets?ticket=ST...

~~~~json
{
    "pageSize": 25,
    "pageNumber": 1,
    "pageCount": 2,
    "result": [
        {
            "classType": "Subset",
            "ui": "C3853926",
            "sourceUi": "900000000000534007",
            "rootSource": "SCTSPA",
            "name": "conjunto de referencias de dependencia entre m\u00f3dulos",
            "description": "conjunto de referencias de dependencia entre m\u00f3dulos",
            "attributeCount": 1,
            "atomMemberCount": 0,
            "sourceConceptMemberCount": 4,
            "relationMemberCount": 0,
            "uri": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/subsets/source/SCTSPA/900000000000534007"
        },
...
        {
            "classType": "Subset",
            "ui": "C3645703",
            "sourceUi": "446608001",
            "rootSource": "SNOMEDCT_US",
            "name": "ICD-O simple map reference set",
            "description": "ICD-O simple map reference set",
            "attributeCount": 1,
            "atomMemberCount": 0,
            "sourceConceptMemberCount": 26175,
            "relationMemberCount": 0,
            "uri": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/subsets/source/SNOMEDCT_US/446608001"
        },
...
        {
            "classType": "Subset",
            "ui": "C3645570",
            "sourceUi": "900000000000509007",
            "rootSource": "SNOMEDCT_US",
            "name": "US English",
            "description": "US English",
            "attributeCount": 1,
            "atomMemberCount": 1213661,
            "sourceConceptMemberCount": 0,
            "relationMemberCount": 0,
            "uri": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/subsets/source/SNOMEDCT_US/900000000000509007"
        },
...
    ]
}

~~~~

