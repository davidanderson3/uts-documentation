title=UMLS API Change Log
date=2025-06-26
updated=2025-06-26
type=page
status=published
navorder=1
~~~~~~
* * *

##### 2024-01-08

We have shut down the Source-Asserted Subsets API Endpoint and the Content Views API Endpoint as of December 31, 2023. We deprecated these endpoints in May of 2022. Source-Asserted Subset information and Content View information can be retrieved from the UMLS Metathesaurus files.

* * *

##### 2023-12-19

We are pleased to announce the publication of a [new API endpoint for NLM terminology releases](/automating-downloads.html). This endpoint provides an updated list of releases for many of our terminology products. You can use this endpoint to automate the download of the latest release files for RxNorm, SNOMED CT, and UMLS.

* * *

##### 2023-07-12

We have made adjustments to the way in which the search API stems individual words. The most significant impact is that queries that include plural forms of words will now find singular forms, for example, a query for "lungs" will find all instances of "lung". In general, API search queries and search queries in the Metathesaurus Browser will produce a higher number of results than before.

* * *

##### 2023-05-09

We now offer an endpoint for validating API keys. If you have developed an application that integrates UMLS data and you need to determine whether a user is a UMLS licensee, you can use this endpoint to validate the user's API key.  
  
Make a request that includes both your API key (validatorApiKey) and the API key of the user of your application (apiKey). For example:  
  
`https://utslogin.nlm.nih.gov/validateUser?validatorApiKey=YOUR_API_KEY&apiKey=USER_API_KEY`  
  
For more information see our [authentication documentation](/rest/authentication.html).

* * *

##### 2022-12-28

**Search for partial matches**, for example:  
  
`/search/current   ?string=Congenital Nephrogenic Diabetes Insipidus   &partialSearch=true`  
  
Adding partialSearch=true to your search query will return partial matches. If your query contains four words, it will return results that include all four words, then results that contain three of four words, then two of four words, then one of four words.  
  
For more information see our [search documentation](/rest/search/index.html).

* * *

##### 2022-10-05

**Download any RxNorm, SNOMED CT, or UMLS release using a single command**, for example:  
  
`curl   "https://uts-ws.nlm.nih.gov/download   ?url=https://download.nlm.nih.gov/   umls/kss/rxnorm/   RxNorm_weekly_10052022.zip   &apiKey=YOUR_API_KEY"   -o RxNorm_weekly_10052022.zip`  
  
For more information, see our [Automating UMLS Terminology Services Downloads page](../automating-downloads.html).

* * *

##### 2022-07-13

**Search for a CUI, return a source-asserted code**: The search endpoint now supports searching for a UMLS CUI and returning a source-asserted code, for example:  
`   /search/current   ?string=C0009044   &sabs=SNOMEDCT_US   &returnIdType=code.`  
  
For more information see our [search documentation](/rest/relations/index.html).

* * *

##### 2022-06-06

**Changes to the concept relations endpoint**: The [concept relations api endpoint](/rest/relations/index.html) will return any relation associated with a UMLS CUI, including source-asserted relations. Previously, this endpoint only returned NLM-asserted relations.

* * *

##### 2022-05-02

**New authentication method**: Users can request data by simply including an API key with a data request. For more information see: [2022AA release announcement](https://www.nlm.nih.gov/pubs/techbull/mj22/mj22_umls_2022aa_release.html) and [authentication documentation.](/rest/authentication.html) Ticket-granting tickets and service tickets are deprecated.

* * *

##### 2022-04-12

**Changes to API search**: The UMLS API started using ElasticSearch for search. Users may notice changes in search ranking.

**Changes to relation data returned**: Relations api requests will return additional data fields: relatedFromId and relatedFromIdName. These data fields indicate the subject of the relationship, which can be a code, CUI, AUI, SCUI, or SDUI. See the sample output on the [source-asserted relations documentation page](/rest/source-asserted-identifiers/relations/index.html).