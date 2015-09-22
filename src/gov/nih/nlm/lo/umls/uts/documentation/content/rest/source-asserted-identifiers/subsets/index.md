title=Retrieving Source-Asserted Subsets
date=2015-09-22
updated=2015-09-22
type=page
status=draft
category=Retrieving Source-Asserted Subsets
navorder=5
~~~~~~


[URIs](#uris) | [Query Parameters](#query-parameters) | [Sample Output](#sample-output)

URIs with /subsets support the following use cases:

* Retrieve all subsets for a known UMLS Release. 
* Retrieve information (name, description, member count, etc.) for a known subset.
* Retrieve all members of a known subset.
* Retrieve attributes for a member of a known subset.

Note that 'current' in the URI can always be used to search against the latest UMLS publication.
You may use any valid UMLS release back to 2008AA in your URI if you would like to search against a particular version of the UMLS.


### URIs

**The base URI is https://uts-ws.nlm.nih.gov/rest**

Sample URI|Description
--- | ---
/content/current/subsets | Retrieve information about all subsets from latest UMLS version or a specific release.
/content/2015AA/subsets/source/SNOMEDCT_US/6011000124106 | Retrieves information for a known subset.
/content/2015AA/subsets/source/SNOMEDCT_US/6011000124106/members | Retrieves all members of a known subset
/content/2015AA/subsets/source/SNOMEDCT_US/6011000124106/members/77147000/attributes | Retrieve attribute information for a specified member of a known subset


### Query Parameters

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
ticket | Y | A single-use service ticket is required for each call to the API. See [authentication](../authentication.html) for more information | n/a | n/a | n/a
pageNumber | N | Whole number that specifies which page of results to fetch. | 1,2,3, etc | 1 | n/a
pageSize | N | Whole number that specifies the number of results to include per page. | 1,2,3, etc | 25 | n/a


### Sample Output


* **Calls under /{version}/subsets and /{version}/subsets/source/{source}/{subset identifier} will return a classType of 'Subset'.** 
* **Calls under /{version}/subsets/source/{source}/{subset identifier}/members will return a classType of 'SourceConceptSubsetMember'.** 
* **Calls under /{version}/subsets/source/{source}/{subset identifier}/members/{subset member identifier}/attributes will return a classType of 'Attribute'.**

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
            "uri": "https://uts-ws-qa.nlm.nih.gov/rest/content/2015AA/subsets/source/SCTSPA/900000000000534007"
        },
        {
            "classType": "Subset",
            "ui": "C3853923",
            "sourceUi": "450828004",
            "rootSource": "SCTSPA",
            "name": "conjunto de referencias de lenguaje castellano para Am\u00e9rica Latina",
            "description": "conjunto de referencias de lenguaje castellano para Am\u00e9rica Latina",
            "attributeCount": 1,
            "atomMemberCount": 1000011,
            "sourceConceptMemberCount": 0,
            "relationMemberCount": 0,
            "uri": "https://uts-ws-qa.nlm.nih.gov/rest/content/2015AA/subsets/source/SCTSPA/450828004"
        },
        {
            "classType": "Subset",
            "ui": "C3853925",
            "sourceUi": "900000000000456007",
            "rootSource": "SCTSPA",
            "name": "conjunto de referencias descriptivas de la estructura de otros conjuntos de referencias",
            "description": "conjunto de referencias descriptivas de la estructura de otros conjuntos de referencias",
            "attributeCount": 1,
            "atomMemberCount": 0,
            "sourceConceptMemberCount": 0,
            "relationMemberCount": 0,
            "uri": "https://uts-ws-qa.nlm.nih.gov/rest/content/2015AA/subsets/source/SCTSPA/900000000000456007"
        },
        {
            "classType": "Subset",
            "ui": "C3692150",
            "sourceUi": "900000000000490003",
            "rootSource": "SCTSPA",
            "name": "conjunto de referencias atributo-valor de motivo de inactivaci\u00f3n de descripciones",
            "description": "conjunto de referencias atributo-valor de motivo de inactivaci\u00f3n de descripciones",
            "attributeCount": 1,
            "atomMemberCount": 471721,
            "sourceConceptMemberCount": 0,
            "relationMemberCount": 0,
            "uri": "https://uts-ws-qa.nlm.nih.gov/rest/content/2015AA/subsets/source/SCTSPA/900000000000490003"
        },
        {
            "classType": "Subset",
            "ui": "C3645685",
            "sourceUi": "447565001",
            "rootSource": "SNOMEDCT_US",
            "name": "Virtual therapeutic moiety simple reference set",
            "description": "Virtual therapeutic moiety simple reference set",
            "attributeCount": 1,
            "atomMemberCount": 0,
            "sourceConceptMemberCount": 3566,
            "relationMemberCount": 0,
            "uri": "https://uts-ws-qa.nlm.nih.gov/rest/content/2015AA/subsets/source/SNOMEDCT_US/447565001"
        },
        {
            "classType": "Subset",
            "ui": "C3683780",
            "sourceUi": "900000000000490003",
            "rootSource": "SNOMEDCT_US",
            "name": "Description inactivation indicator reference set",
            "description": "Description inactivation indicator reference set",
            "attributeCount": 1,
            "atomMemberCount": 0,
            "sourceConceptMemberCount": 0,
            "relationMemberCount": 0,
            "uri": "https://uts-ws-qa.nlm.nih.gov/rest/content/2015AA/subsets/source/SNOMEDCT_US/900000000000490003"
        },
        {
            "classType": "Subset",
            "ui": "C3645684",
            "sourceUi": "447566000",
            "rootSource": "SNOMEDCT_US",
            "name": "Virtual medicinal product simple reference set",
            "description": "Virtual medicinal product simple reference set",
            "attributeCount": 1,
            "atomMemberCount": 0,
            "sourceConceptMemberCount": 10803,
            "relationMemberCount": 0,
            "uri": "https://uts-ws-qa.nlm.nih.gov/rest/content/2015AA/subsets/source/SNOMEDCT_US/447566000"
        },
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
            "uri": "https://uts-ws-qa.nlm.nih.gov/rest/content/2015AA/subsets/source/SNOMEDCT_US/447562003"
        },
        {
            "classType": "Subset",
            "ui": "C3669743",
            "sourceUi": "900000000000534007",
            "rootSource": "SNOMEDCT_US",
            "name": "Module dependency",
            "description": "Module dependency",
            "attributeCount": 1,
            "atomMemberCount": 0,
            "sourceConceptMemberCount": 0,
            "relationMemberCount": 0,
            "uri": "https://uts-ws-qa.nlm.nih.gov/rest/content/2015AA/subsets/source/SNOMEDCT_US/900000000000534007"
        },
        {
            "classType": "Subset",
            "ui": "C3714471",
            "sourceUi": "900000000000524003",
            "rootSource": "SNOMEDCT_US",
            "name": "MOVED TO association reference set",
            "description": "MOVED TO association reference set",
            "attributeCount": 1,
            "atomMemberCount": 0,
            "sourceConceptMemberCount": 0,
            "relationMemberCount": 0,
            "uri": "https://uts-ws-qa.nlm.nih.gov/rest/content/2015AA/subsets/source/SNOMEDCT_US/900000000000524003"
        },
        {
            "classType": "Subset",
            "ui": "C3539934",
            "sourceUi": "900000000000538005",
            "rootSource": "SNOMEDCT_US",
            "name": "Description format",
            "description": "Description format",
            "attributeCount": 1,
            "atomMemberCount": 0,
            "sourceConceptMemberCount": 3,
            "relationMemberCount": 0,
            "uri": "https://uts-ws-qa.nlm.nih.gov/rest/content/2015AA/subsets/source/SNOMEDCT_US/900000000000538005"
        },
        {
            "classType": "Subset",
            "ui": "C3714473",
            "sourceUi": "447563008",
            "rootSource": "SNOMEDCT_US",
            "name": "ICD-9-CM equivalence complex map reference set",
            "description": "ICD-9-CM equivalence complex map reference set",
            "attributeCount": 1,
            "atomMemberCount": 0,
            "sourceConceptMemberCount": 121098,
            "relationMemberCount": 0,
            "uri": "https://uts-ws-qa.nlm.nih.gov/rest/content/2015AA/subsets/source/SNOMEDCT_US/447563008"
        },
        {
            "classType": "Subset",
            "ui": "C3683520",
            "sourceUi": "900000000000489007",
            "rootSource": "SNOMEDCT_US",
            "name": "Concept inactivation indicator reference set",
            "description": "Concept inactivation indicator reference set",
            "attributeCount": 1,
            "atomMemberCount": 1193,
            "sourceConceptMemberCount": 99329,
            "relationMemberCount": 0,
            "uri": "https://uts-ws-qa.nlm.nih.gov/rest/content/2015AA/subsets/source/SNOMEDCT_US/900000000000489007"
        },
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
            "uri": "https://uts-ws-qa.nlm.nih.gov/rest/content/2015AA/subsets/source/SNOMEDCT_US/446608001"
        },
        {
            "classType": "Subset",
            "ui": "C3645553",
            "sourceUi": "900000000000531004",
            "rootSource": "SNOMEDCT_US",
            "name": "REFERS TO concept association reference set",
            "description": "REFERS TO concept association reference set",
            "attributeCount": 1,
            "atomMemberCount": 865,
            "sourceConceptMemberCount": 0,
            "relationMemberCount": 0,
            "uri": "https://uts-ws-qa.nlm.nih.gov/rest/content/2015AA/subsets/source/SNOMEDCT_US/900000000000531004"
        },
        {
            "classType": "Subset",
            "ui": "C3645556",
            "sourceUi": "900000000000528000",
            "rootSource": "SNOMEDCT_US",
            "name": "WAS A association reference set",
            "description": "WAS A association reference set",
            "attributeCount": 1,
            "atomMemberCount": 0,
            "sourceConceptMemberCount": 20998,
            "relationMemberCount": 0,
            "uri": "https://uts-ws-qa.nlm.nih.gov/rest/content/2015AA/subsets/source/SNOMEDCT_US/900000000000528000"
        },
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
            "uri": "https://uts-ws-qa.nlm.nih.gov/rest/content/2015AA/subsets/source/SNOMEDCT_US/900000000000509007"
        },
        {
            "classType": "Subset",
            "ui": "C3645554",
            "sourceUi": "900000000000530003",
            "rootSource": "SNOMEDCT_US",
            "name": "ALTERNATIVE association reference set",
            "description": "ALTERNATIVE association reference set",
            "attributeCount": 1,
            "atomMemberCount": 0,
            "sourceConceptMemberCount": 165,
            "relationMemberCount": 0,
            "uri": "https://uts-ws-qa.nlm.nih.gov/rest/content/2015AA/subsets/source/SNOMEDCT_US/900000000000530003"
        },
        {
            "classType": "Subset",
            "ui": "C3669402",
            "sourceUi": "900000000000456007",
            "rootSource": "SNOMEDCT_US",
            "name": "Reference set descriptor",
            "description": "Reference set descriptor",
            "attributeCount": 1,
            "atomMemberCount": 0,
            "sourceConceptMemberCount": 31,
            "relationMemberCount": 0,
            "uri": "https://uts-ws-qa.nlm.nih.gov/rest/content/2015AA/subsets/source/SNOMEDCT_US/900000000000456007"
        },
        {
            "classType": "Subset",
            "ui": "C3645581",
            "sourceUi": "900000000000497000",
            "rootSource": "SNOMEDCT_US",
            "name": "CTV3 simple map",
            "description": "CTV3 simple map",
            "attributeCount": 1,
            "atomMemberCount": 0,
            "sourceConceptMemberCount": 417209,
            "relationMemberCount": 0,
            "uri": "https://uts-ws-qa.nlm.nih.gov/rest/content/2015AA/subsets/source/SNOMEDCT_US/900000000000497000"
        },
        {
            "classType": "Subset",
            "ui": "C3882623",
            "sourceUi": "6011000124106",
            "rootSource": "SNOMEDCT_US",
            "name": "ICD-10-CM complex map reference set",
            "description": "ICD-10-CM complex map reference set",
            "attributeCount": 1,
            "atomMemberCount": 0,
            "sourceConceptMemberCount": 54262,
            "relationMemberCount": 0,
            "uri": "https://uts-ws-qa.nlm.nih.gov/rest/content/2015AA/subsets/source/SNOMEDCT_US/6011000124106"
        },
        {
            "classType": "Subset",
            "ui": "C3714465",
            "sourceUi": "900000000000527005",
            "rootSource": "SNOMEDCT_US",
            "name": "SAME AS association reference set",
            "description": "SAME AS association reference set",
            "attributeCount": 1,
            "atomMemberCount": 0,
            "sourceConceptMemberCount": 47524,
            "relationMemberCount": 0,
            "uri": "https://uts-ws-qa.nlm.nih.gov/rest/content/2015AA/subsets/source/SNOMEDCT_US/900000000000527005"
        },
        {
            "classType": "Subset",
            "ui": "C3714470",
            "sourceUi": "900000000000526001",
            "rootSource": "SNOMEDCT_US",
            "name": "REPLACED BY association reference set",
            "description": "REPLACED BY association reference set",
            "attributeCount": 1,
            "atomMemberCount": 0,
            "sourceConceptMemberCount": 9715,
            "relationMemberCount": 0,
            "uri": "https://uts-ws-qa.nlm.nih.gov/rest/content/2015AA/subsets/source/SNOMEDCT_US/900000000000526001"
        },
        {
            "classType": "Subset",
            "ui": "C3645571",
            "sourceUi": "900000000000508004",
            "rootSource": "SNOMEDCT_US",
            "name": "GB English",
            "description": "GB English",
            "attributeCount": 1,
            "atomMemberCount": 1205756,
            "sourceConceptMemberCount": 0,
            "relationMemberCount": 0,
            "uri": "https://uts-ws-qa.nlm.nih.gov/rest/content/2015AA/subsets/source/SNOMEDCT_US/900000000000508004"
        },
        {
            "classType": "Subset",
            "ui": "C3714472",
            "sourceUi": "900000000000525002",
            "rootSource": "SNOMEDCT_US",
            "name": "MOVED FROM association reference set",
            "description": "MOVED FROM association reference set",
            "attributeCount": 1,
            "atomMemberCount": 0,
            "sourceConceptMemberCount": 5,
            "relationMemberCount": 0,
            "uri": "https://uts-ws-qa.nlm.nih.gov/rest/content/2015AA/subsets/source/SNOMEDCT_US/900000000000525002"
        }
    ]
}

~~~~

