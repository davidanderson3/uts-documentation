title=Release Notes
date=2015-11-09
updated=2018-10-04
type=page
status=published
navorder=1
~~~~~~

Released: June 28, 2016

#### Features:
* **New endpoint created for using UMLS CUIs for [Crosswalking Source-Asserted Identifiers](/rest/source-asserted-identifiers/crosswalk/index.html). This endpoint simplifies the multi-step crosswalk process previously outlined in the REST API Cookbook.**

* **New endpoint created for [individual content view members](/rest/content-views/index.html#uris).**

* **New endpoint created for [individual subset members](/rest/source-asserted-identifiers/subsets/index.html#uris).**


#### Change:
* **The URI pattern for the [Source-Asserted Subset endpoint](/rest/source-asserted-identifiers/subsets/index.html#uris) has been simplified from '/content/current/subsets' to '/subsets/current'.**

* **Subset objects now have attributes embedded and include a link to the endpoint for members of the subset. See the [sample output](/rest/source-asserted-identifiers/subsets/index.html#sample-output) for an example.**

* **SourceConceptSubsetMember objects, which are the output of subset members calls, now have attributes embedded, and the subset member attributes endpoint has been removed. See the [sample output](/rest/source-asserted-identifiers/subsets/index.html#sample-output) for an example.**

* **SourceAtomCluster objects and Atom objects now have subset and content view membership information embedded.**
  
#### Known issues:

See our github sample code area for a list of [known issues](https://github.com/HHS/uts-rest-api/issues) with the API.

