title=Release Notes and Roadmap
date=2015-11-09
updated=2015-11-24
type=page
status=published
navorder=1
~~~~~~

Released: November 20, 2015

#### Features:
* **Retrieving [source-asserted attributes](/rest/source-asserted-identifiers/attributes/index.html) of a source-asserted identifier, such as ```EFFECTIVE_TIME``` of a SNOMEDCT concept**
* **Add links to SourceAtomCluster objects to discover CUIs**
  The ```concepts``` link in the output of SourceAtomCluster objects allows users to easily discover the UMLS CUI(s) associated with a source-asserted code, concept, or descriptor.

#### Change:
* **sourceUi**
  The ```sourceUi``` data element has been added to [Source-Asserted Subsets Member Attributes output](/rest/source-asserted-identifiers/subsets/#sample-output).

#### Known issues:

There are no known issues at this time.

#### Planned Updates

The following new items are planned for upcoming versions of the API.    

##### Features:
* **Retrieving content views**
  Retrieve all content views, retrieve members of a specified content views.
* **Add history mechanism so users can retrieve CUIs that are no longer in the latest UMLS release**
