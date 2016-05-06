title=Retrieving Content View Information
date=2016-05-09
updated=2016-05-09
type=page
status=published
category=Retrieving UMLS Data
navorder=8
~~~~~~


[URIs](#uris) | [Query Parameters](#query-parameters) | [Sample Output](#sample-output)

URIs with /content-views support the following use cases:

* Retrieve all content views for a known UMLS Release. 
* Retrieve information (name, description, member count, etc.) for a known content views.
* Retrieve all members of a known content view.

Note that 'current' in the URI can always be used to search against the latest UMLS publication.
You may use any valid UMLS release back to 2008AA in your URI if you would like to search against a particular version of the UMLS.


### URIs

**The base URI is https://uts-ws.nlm.nih.gov/rest**

Sample URI|Description|Returned JSON Object classType
--- | ---
/content-views/current/ | Retrieves information about all subsets from the current release | ContentView
/content-views/current/CUI/C1700357 | Retrieves information for the MetaMap NLP View content view | ContentView
/content-views/current/CUI/C1700357/members | Retrieves members of the MetaMap NLP View content view | AtomContentViewMember*

*Calls for members of certain content views return output with a "SourceConceptContentViewMember" JSON Object classType*.

### Query Parameters

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
ticket | Y | A single-use service ticket is required for each call to the API. See [authentication](../authentication.html) for more information | n/a | n/a | n/a

### Sample Output

Sample output for /content-views/2015AB?ticket=ST-...

~~~~json
{

    "pageSize": 25,
    "pageNumber": 1,
    "pageCount": 1,
    "result": 

[

{

    "classType": "ContentView",
    "ui": "C1700357",
    "name": "MetaMap NLP View",
    "cascade": false,
    "includeObsolete": false,
    "algorithm": "NONE",
    "category": "NONE",
    "code": 0,
    "contributor": "NONE",
    "contributorDate": "NONE",
    "contributorURL": "NONE",
    "contributorVersion": "NONE",
    "description": "This content view represents the strict model of data used by MetaMap.",
    "maintainer": "NONE",
    "maintainerDate": "NONE",
    "maintainerURL": "NONE",
    "maintainerVersion": "NONE",
    "previousMeta": "NONE",
    "contentViewClass": "NONE",
    "subCategory": "NONE",
    "generated": false,
    "attributeCount": 0,
    "atomMemberCount": 4231900,
    "sourceConceptMemberCount": 0,
    "relationMemberCount": 0,
    "conceptMemberCount": 0,
    "uri": "https://uts-ws.nlm.nih.gov/rest/content-views/2015AB/CUI/C1700357",
    "memberUri": "https://uts-ws.nlm.nih.gov/rest/content-views/2015AB/CUI/C1700357/members"

},
{

    "classType": "ContentView",
    "ui": "C1964027",
    "name": "UMLS enhanced VA/KP Problem List Subset of SNOMED (Level 0+SNOMED)",
    "cascade": false,
    "includeObsolete": false,
    "algorithm": "NONE",
    "category": "NONE",
    "code": 0,
    "contributor": "NONE",
    "contributorDate": "NONE",
    "contributorURL": "NONE",
    "contributorVersion": "NONE",
    "description": "This content view provides an UMLS-enhanced view of the Veterans Health Administration and Kaiser Permanente (VA/KP) Problem List Subset of SNOMED, which is one of the controlled terminologies used for Structured Product Labeling (SPL). SPL is a document markup standard approved by Health Level Seven (HL7) and adopted by FDA as a mechanism for exchanging medication information. This set of SNOMED terms and codes is freely reusable worldwide without licensing or intellectual property restrictions. This content view consists of all UMLS concepts containing the active SNOMED concepts in the Problem List Subset. It includes contents from SNOMED and other source vocabularies with no additional licensing restrictions. All non-English, obsolete and suppressible contents are excluded.",
    "maintainer": "NONE",
    "maintainerDate": "NONE",
    "maintainerURL": "NONE",
    "maintainerVersion": "NONE",
    "previousMeta": "NONE",
    "contentViewClass": "NONE",
    "subCategory": "NONE",
    "generated": false,
    "attributeCount": 0,
    "atomMemberCount": 212274,
    "sourceConceptMemberCount": 0,
    "relationMemberCount": 0,
    "conceptMemberCount": 0,
    "uri": "https://uts-ws.nlm.nih.gov/rest/content-views/2015AB/CUI/C1964027",
    "memberUri": "https://uts-ws.nlm.nih.gov/rest/content-views/2015AB/CUI/C1964027/members"

},
{

    "classType": "ContentView",
    "ui": "C1964028",
    "name": "UMLS enhanced VA/KP Problem List Subset of SNOMED (Level 0+SNOMED+MDR)",
    "cascade": false,
    "includeObsolete": false,
    "algorithm": "NONE",
    "category": "NONE",
    "code": 0,
    "contributor": "NONE",
    "contributorDate": "NONE",
    "contributorURL": "NONE",
    "contributorVersion": "NONE",
    "description": "This content view provides an UMLS-enhanced view of the Veterans Health Administration and Kaiser Permanente (VA/KP) Problem List Subset of SNOMED, which is one of the controlled terminologies used for Structured Product Labeling (SPL). SPL is a document markup standard approved by Health Level Seven (HL7) and adopted by FDA as a mechanism for exchanging medication information. This set of SNOMED terms and codes is freely reusable worldwide without licensing or intellectual property restrictions. This content view consists of all UMLS concepts containing the active SNOMED concepts in the Problem List Subset. It includes contents from SNOMED, MedDRA and other source vocabularies with no additional licensing restrictions. All non-English, obsolete and suppressible contents are excluded.",
    "maintainer": "NONE",
    "maintainerDate": "NONE",
    "maintainerURL": "NONE",
    "maintainerVersion": "NONE",
    "previousMeta": "NONE",
    "contentViewClass": "NONE",
    "subCategory": "NONE",
    "generated": false,
    "attributeCount": 0,
    "atomMemberCount": 234633,
    "sourceConceptMemberCount": 0,
    "relationMemberCount": 0,
    "conceptMemberCount": 0,
    "uri": "https://uts-ws.nlm.nih.gov/rest/content-views/2015AB/CUI/C1964028",
    "memberUri": "https://uts-ws.nlm.nih.gov/rest/content-views/2015AB/CUI/C1964028/members"

},
...

}
~~~~

Sample output for /content-views/2015AB/CUI/C1700357?ticket=ST-...

~~~~json
{

    "pageSize": 25,
    "pageNumber": 1,
    "pageCount": 1,
    "result": 

    {
        "classType": "ContentView",
        "ui": "C1700357",
        "name": "MetaMap NLP View",
        "cascade": false,
        "includeObsolete": false,
        "algorithm": "NONE",
        "category": "NONE",
        "code": 0,
        "contributor": "NONE",
        "contributorDate": "NONE",
        "contributorURL": "NONE",
        "contributorVersion": "NONE",
        "description": "This content view represents the strict model of data used by MetaMap.",
        "maintainer": "NONE",
        "maintainerDate": "NONE",
        "maintainerURL": "NONE",
        "maintainerVersion": "NONE",
        "previousMeta": "NONE",
        "contentViewClass": "NONE",
        "subCategory": "NONE",
        "generated": false,
        "attributeCount": 0,
        "atomMemberCount": 4231900,
        "sourceConceptMemberCount": 0,
        "relationMemberCount": 0,
        "conceptMemberCount": 0,
        "uri": "https://uts-ws.nlm.nih.gov/rest/content-views/2015AB/CUI/C1700357",
        "memberUri": "https://uts-ws.nlm.nih.gov/rest/content-views/2015AB/CUI/C1700357/members"
    }

}
~~~~

Sample output for /content-views/2015AB/CUI/C1700357/members?ticket=ST-...

~~~~json
{

    "pageSize": 25,
    "pageNumber": 1,
    "pageCount": 1,
    "result": 

[

{

    "classType": "AtomContentViewMember",
    "ui": "A19582446",
    "uri": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/AUI/A19582446",
    "name": "KPNA6 protein, mouse",
    "contentViewMemberAttributes": [ ]

},
{

    "classType": "AtomContentViewMember",
    "ui": "A19580305",
    "uri": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/AUI/A19580305",
    "name": "importin alpha7 protein, mouse",
    "contentViewMemberAttributes": [ ]

},
{

    "classType": "AtomContentViewMember",
    "ui": "A19592982",
    "uri": "https://uts-ws.nlm.nih.gov/rest/content/2015AB/AUI/A19592982",
    "name": "FBXL2 protein, mouse",
    "contentViewMemberAttributes": [ ]

},
...

}
~~~~