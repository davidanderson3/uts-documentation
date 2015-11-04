title=Release Notes and Roadmap
date=2015-07-10
updated=2015-11-02
type=page
status=published
navorder=1
~~~~~~

Released: September 30, 2015

#### Features:
* **Retrieving subset members**
  Retrieve all subsets, retrieve members of a specified subset.
* **Retrieving source-asserted relation data**
  Retrieve source-asserted relationship information of a source-asserted identifier.

#### Change:
* **Retrieving obsolete/suppressible terms and codes**
  Obsolete and suppressible terms and codes are no longer be retrieved by default. Users can take advantage of obsolete/suppressible parameters for some calls to include this information in the output.
* **Searching the UMLS - paging**
  The pageCount parameter has been removed from the /search endpoint.  See our notes about [paging through results](/rest/search/index.html#paging-through-results) on the /search endpoint for more details.
* **Change in output for semanticTypes**
  For convenience, semantic type names (in addition to the semantic type identifier) are now included in Concept classes when retrieving UMLS CUIs on the /rest/content/CUI/{CUI} endpoint, such as ```"T037: Injury or Poisoning"```

#### Deprecation notice:
* **sourceUi**
  The ```sourceUi``` data element returned in [SourceAtomCluster objects](/rest/source-asserted-identifiers/#sample-output) is deprecated.  Please use ```ui``` instead.

#### Known issues:

Item | Issue | Resolution
-- | -- | --
1|The /subset endpoint does not return results when version is defined as 'current' in the URI|Users can specify a specific UMLS publication, such as '2015AA' a workaround.  The issue will be resolved in the next deployment the week of November 9, 2015

### Planned Updates

The following new items are planned for upcoming versions of the API.    

#### Features:
* **Retrieving source-asserted attributes**
  Retrieve source-asserted attributes of a source-asserted identifier.
* **Retrieving content views**
  Retrieve all content views, retrieve members of a specified content views.
* **Python code samples in repository**
  Python code samples for authenticating and making other API calls are in the code sample repository. See the [code sample repository on GitHub](https://github.com/HHS/uts-rest-api) for details.


