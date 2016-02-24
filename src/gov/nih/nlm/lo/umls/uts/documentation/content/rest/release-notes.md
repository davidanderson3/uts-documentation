title=Release Notes and Roadmap
date=2015-11-09
updated=2016-02-24
type=page
status=published
navorder=1
~~~~~~

Released: February 24, 2016

#### Features:
* **Retrieving parents/children of UMLS atoms**
  Retrieve all parents/children of UMLS atoms. See [Retrieving UMLS Atom Parents and Children](/rest/atoms/parents-and-children/) for details.
* **Retrieving ancestors/descendants of UMLS atoms**
  Retrieve all ancestors/descendants of UMLS atoms.  See [Retrieving UMLS Atom Ancestors and Descendants](/rest/atoms/ancestors-and-descendants/) for details.
  
#### Change:
* **Added sourceUi parameter to /search calls**
  The ```sourceUi``` parameter has been added to [/search](/rest/search/index.html) calls.
  
* **Expired service ticket handling**
  When a call is submitted with an expired service ticket, the API now returns a 404 status.

#### Known issues:

See our github sample code area for a list of [known issues](https://github.com/HHS/uts-rest-api/issues) with the API.

#### Planned Updates

The following new items are planned for upcoming versions of the API.    

##### Features:
* **Retrieving content views**
  Retrieve all content views, retrieve members of a specified content views.
* **Add history mechanism so users can retrieve CUIs that are no longer in the latest UMLS release**
