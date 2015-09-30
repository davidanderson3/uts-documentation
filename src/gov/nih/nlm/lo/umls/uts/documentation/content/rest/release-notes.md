title=Release Notes and Roadmap
date=2015-07-10
updated=2015-09-30
type=page
status=published
navorder=1
~~~~~~

Released: September 30, 2015

##### Features:
* **Retrieving subset members**
  Retrieve all subsets, retrieve members of a specified subset.
* **Retrieving source-asserted relation data**
  Retrieve source-asserted relationship information of a source-asserted identifier.

##### Change:
* **Retrieving obsolete/suppressible terms and codes**
  Obsolete and suppressible terms and codes are no longer be retrieved by default. Users can take advantage of obsolete/suppressible parameters for some calls to include this information in the output.
* **Searching the UMLS - paging**
  The pageCount parameter has been removed from the /search endpoint. Paging is not available for /search calls.
  
### Planned Updates

The following new items are planned for upcoming versions of the API.    

##### Features:
* **Retrieving source-asserted attributes**
  Retrieve source-asserted attributes of a source-asserted identifier.
* **Retrieving content views**
  Retrieve all content views, retrieve members of a specified content views.
* **Python code samples in repository**
  Python code samples for authenticating and making other API calls will be added to the code sample repository. See the [code sample repository on GitHub](https://github.com/HHS/uts-rest-api) for details.


