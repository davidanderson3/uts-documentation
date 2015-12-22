title=Retrieving Source-Asserted Subsets
date=2015-09-30
updated=2015-12-21
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
language | N | 3-letter abbreviation for language | ENG, SPA, GER, etc | n/a | n/a

### Sample Output

Sample output for /content/current/subsets?ticket=ST...

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
            "uri": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/subsets/source/SCTSPA/900000000000534007",
            "subsetAttributes": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/subsets/source/SCTSPA/900000000000534007/attributes"
        },
...
        {
            "classType": "Subset",
            "ui": "C3853348",
            "sourceUi": "442311000124105",
            "rootSource": "SNOMEDCT_US",
            "name": "Route of administration reference set",
            "description": "Route of administration reference set",
            "attributeCount": 1,
            "atomMemberCount": 0,
            "sourceConceptMemberCount": 144,
            "relationMemberCount": 0,
            "uri": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/subsets/source/SNOMEDCT_US/442311000124105",
            "subsetAttributes": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/subsets/source/SNOMEDCT_US/442311000124105/attributes"
        },
...
        {
            "classType": "Subset",
            "ui": "C3714467",
            "sourceUi": "447562003",
            "rootSource": "SNOMEDCT_US",
            "name": "ICD-10 complex map reference set",
            "description": "ICD-10 complex map reference set",
            "attributeCount": 1,
            "atomMemberCount": 0,
            "sourceConceptMemberCount": 43041,
            "relationMemberCount": 0,
            "uri": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/subsets/source/SNOMEDCT_US/447562003",
            "subsetAttributes": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/subsets/source/SNOMEDCT_US/447562003/attributes"
        },
...
    ]
}
~~~~

Sample output for /content/current/subsets/source/SNOMEDCT_US/442311000124105/members?ticket=ST...

~~~~json
{
    "pageSize": 25,
    "pageNumber": 1,
    "pageCount": 6,
    "result": [
        {
            "classType": "SourceConceptSubsetMember",
            "name": "Suborbital route",
            "attributeCount": 0,
            "ui": "AT201016710",
            "sourceUi": "416174007",
            "rootSource": "SNOMEDCT_US",
            "sourceConcept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/416174007",
            "subsetMemberAttributes": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/subsets/source/SNOMEDCT_US/442311000124105/members/416174007/attributes"
        },
        {
            "classType": "SourceConceptSubsetMember",
            "name": "Intraocular route",
            "attributeCount": 0,
            "ui": "AT201110390",
            "sourceUi": "372468001",
            "rootSource": "SNOMEDCT_US",
            "sourceConcept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/372468001",
            "subsetMemberAttributes": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/subsets/source/SNOMEDCT_US/442311000124105/members/372468001/attributes"
        },
        {
            "classType": "SourceConceptSubsetMember",
            "name": "Intracerebral route",
            "attributeCount": 0,
            "ui": "AT200236815",
            "sourceUi": "446540005",
            "rootSource": "SNOMEDCT_US",
            "sourceConcept": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/source/SNOMEDCT_US/446540005",
            "subsetMemberAttributes": "https://uts-ws.nlm.nih.gov/rest/content/2015AA/subsets/source/SNOMEDCT_US/442311000124105/members/446540005/attributes"
        },
...
    ]
}
~~~~

Sample output for /content/current/subsets/source/SNOMEDCT_US/442311000124105/attributes?ticket=ST...

~~~~json
{
    "pageSize": 25,
    "pageNumber": 1,
    "pageCount": 1,
    "result": [
        {
            "classType": "Attribute",
            "ui": "ATM255",
            "sourceUi": "NONE",
            "rootSource": "SNOMEDCT_US",
            "name": "LANG",
            "value": "ENG"
        }
    ]
}
~~~~

Sample output for /content/current/subsets/source/SNOMEDCT_US/6011000124106/members/89361000119103/attributes?ticket=ST...

~~~~json
{
    "pageSize": 25,
    "pageNumber": 1,
    "pageCount": 1,
    "result": [
        {
            "classType": "Attribute",
            "ui": "ATM36778504",
            "sourceUi": "0c9ff6e0-ca17-5d8e-930a-0bc839769e34",
            "rootSource": "SNOMEDCT_US",
            "name": "MAPGROUP",
            "value": "1"
        },
        {
            "classType": "Attribute",
            "ui": "ATM36778505",
            "sourceUi": "0c9ff6e0-ca17-5d8e-930a-0bc839769e34",
            "rootSource": "SNOMEDCT_US",
            "name": "MAPADVICE",
            "value": "ALWAYS F80.0"
        },
        {
            "classType": "Attribute",
            "ui": "ATM36778506",
            "sourceUi": "0c9ff6e0-ca17-5d8e-930a-0bc839769e34",
            "rootSource": "SNOMEDCT_US",
            "name": "MAPTARGET",
            "value": "F80.0"
        },
...
    ]
}
~~~~