title=Release Notes
date=2015-07-10
updated=2015-09-15
type=page
status=published
category=Release Information
navorder=1
~~~~~~

Released: August 28, 2015

#### New Features: 
* **Retrieving ancestors of source-asserted identifiers**
  Users can now retrieve ancestors of source-asserted identifiers. See [Retrieving ancestors](/rest/ancestors-and-descendants/) for details.
* **Retrieving descendants of source-asserted identifiers**
  Users can now retrieve descendants of source-asserted identifiers.  See [Retrieving descendants](/rest/ancestors-and-descendants/) for details.
* **Retrieving relations for UMLS concepts**
  Users can now retrieve NLM-asserted relationship information for UMLS concepts.  See [Retrieving concept relations](/rest/relations/) for details.
* **Code sample repository on GitHub**
  Users can access code samples for authenticating and making other API calls in Perl and Java with more programming languages and samples to follow. See the [code sample repository on GitHub](https://github.com/HHS/uts-rest-api) for details.

#### Change: 
* **Pagination fields**
  A 'pageCount' field has been added to the Json output, which is populated with a whole number that specifies the number of pages of results, and the 'pageNum' query parameter has been relabeled 'pageNumber'.
  
### Planned Updates

The following new items are planned for upcoming versions of the API.    

#### Features:
* **Paging for /search results**
  View the total number of results pages, the current page, and the current page size for /search calls.
* **Python code samples in repository**
  Python code samples for authenticating and making other API calls will be added to the code sample repository. See the [code sample repository on GitHub](https://github.com/HHS/uts-rest-api) for details.

#### Methods:
* **Retrieving subset members**
  Retrieve all subsets, retrieve members of a specified subset.
* **Retrieving source-asserted relation data**
  Retrieve source-asserted relationship information for a source-asserted identifier.