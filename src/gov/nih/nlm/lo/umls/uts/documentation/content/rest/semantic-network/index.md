title=Retrieving Semantic Type Information
date=2016-03-05
updated=2016-03-05
type=page
status=published
category=Retrieving UMLS Data
navorder=7
~~~~~~

The /semantic-network endpoint supports the retrieval of semantic type information by identifier.
UMLS CUIs are assigned semantic types.  When you make a call to the /CUI/{CUI} service, you will receive back semantic type
information as part of your [Concept](/rest/concept/index.html) object.

Use **https://uts-ws.nlm.nih.gov/rest/semantic-network** as your base URI.

Sample URI|Description|Returned JSON Object classType
--- | ---
[/semantic-network/current/TUI/T109](#sample-output)| Retrieves TUI | SemanticType

### Query Parameters

Parameter name | Required? Y/N | Description|  Valid Values | Default value | Usage Note
--- | ---
apiKey | Y | An API key is required for each call to the API. Visit [your UTS profile](https://uts.nlm.nih.gov/uts/profile) to obtain your API key. | n/a | n/a | n/a

Sample output for https://uts-ws.nlm.nih.gov/rest/semantic-network/2015AB/TUI/T109?apiKey=YOUR_APIKEY-...

### Sample Output

~~~~.json
{
   pageSize: 25,
   pageNumber: 1,
   pageCount: 1,
   result: {
        classType: "SemanticType",
        abbreviation: "orch",
        ui: "T109",
        definition: "The general class of carbon-containing compounds, usually based on carbon chains or rings, and also containing hydrogen (hydrocarbons), with or without nitrogen, oxygen, or other elements in which the bonding between elements is generally covalent.",
        example: "NONE",
        nonHuman: "NONE",
        usageNote: "Salts of organic chemicals (such as Calcium Acetate) would be considered organic chemicals and should not also receive the type 'Inorganic Chemical'.",
        treeNumber: "A1.4.1.2.1",
        semanticTypeGroup: {
            classType: "SemanticGroup",
            abbreviation: "CHEM",
            expandedForm: "Chemicals & Drugs",
            semanticTypeCount: 20
            },
        childCount: 2,
        name: "Organic Chemical"
    }
}
~~~~
