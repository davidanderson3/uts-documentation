title=Searching terms from a vocabulary
date=2016-02-26
updated=2016-03-08
type=page
status=published
category=REST API Cookbook
navorder=1
~~~~~~

Many times users want to use the UMLS search terms and retrieve identifiers from specific vocabularies such as SNOMED CT or LOINC.
For example, let's say we want look for concepts from the US Edition of SNOMED CT.   You can set up a search (using the **/search** service) for 'elevated cholesterol' with the following parameters:

+  `string=elevated cholesterol`
+  `sabs=SNOMEDCT_US`
+  `returnIdType=sourceUi`
+  `pageNumber=\<pageNumber\>`<sup><b>[1](#1)</b></sup>
+  `ticket=\<your service ticket\>` See [authentication](/rest/authentication.html) for details


Our initial `GET` call looks like this:
`https://uts-ws.nlm.nih.gov/rest/search/current?string=high cholesterol&pageNumber=1&sabs=SNOMEDCT_US&returnIdType=sourceUi&ticket=<your-ticket>`

This search returns over 30 results, not all of which may be relevant to you.  You can customize your [list of query parameters](/rest/search/index.html#query-parameters) according to your search needs.
In this example we've used the `returnIdType` parameter to ask for source-asserted concepts from SNOMED CT.  If this parameter is not included (the default setting), the API will return UMLS CUIs.

~~~~json
{
pageSize: 25,
pageNumber: 1,
result: {
classType: "searchResults",
results: [
{
ui: "13644009",
rootSource: "SNOMEDCT_US",
uri: "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/13644009",
name: "Hypercholesterolemia"
},
{
ui: "102737005",
rootSource: "SNOMEDCT_US",
uri: "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/102737005",
name: "HDL cholesterol"
},
{
ui: "370992007",
rootSource: "SNOMEDCT_US",
uri: "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/370992007",
name: "Dyslipidemia"
},
...
~~~~

If we want a more precise search, we can add the searchType parameter:

+  `searchType=exact`

This returns any source-asserted identifier containing a non-suppressible/non-obsolete exact match against the queried term:

~~~~.text
{
pageSize: 25,
pageNumber: 1,
result: {
classType: "searchResults",
results: [
{
ui: "13644009",
rootSource: "SNOMEDCT_US",
uri: "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/13644009",
name: "Hypercholesterolemia"
}
]
}
~~~~

#####1
You'll often receive more than the default 25 objects per page when querying the /search endpoint, unless you're using exact searching.
Be sure your code is set up to use the `pageNumber` parameter to make calls to each page.  See [paging through search results](/rest/search/index.html#paging-through-results) for more information.
