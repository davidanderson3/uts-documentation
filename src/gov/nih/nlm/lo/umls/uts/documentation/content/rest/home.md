title=UMLS API Home
date=2015-06-10
updated=2016-07-07
type=page
status=published
navorder=1
~~~~~~


### Endpoints to search and retrieve UMLS content

Base URI|HTTP Request Type|Path|Description
--- | --- | --- | --
**https://uts-ws.nlm.nih.gov/rest**||||
 |GET | [/search/{version}](search/)| Retrieves CUIs when searching by term or code
 |GET | [/content/{version}/CUI/{CUI}](concept/) | Retrieves information about a known CUI
 |GET | [/content/{version}/CUI/{CUI}/atoms](atoms/) | Retrieves atoms and information about atoms for a known CUI
 |GET | [/content/{version}/CUI/{CUI}/definitions](definitions/) | Retrieves definitions for a known CUI
 |GET | [/content/{version}/CUI/{CUI}/relations](relations/) | Retrieves NLM-asserted relationships for a known CUI
 |GET | [/content/{version}/source/{source}/{id}](source-asserted-identifiers/) | Retrieves information about a known source-asserted identifier
 |GET | [/content/{version}/source/{source}/{id}/atoms](atoms/) | Retrieves information about atoms for a known source-asserted identifier
 |GET | [/content/{version}/source/{source}/{id}/parents](parents-and-children/) | Retrieves immediate parents of a source-asserted identifier
 |GET | [/content/{version}/source/{source}/{id}/children](parents-and-children/) | Retrieves immediate children of a source-asserted identifier
 |GET | [/content/{version}/source/{source}/{id}/ancestors](ancestors-and-descendants/) | Retrieves all ancestors of a source-asserted identifier
 |GET | [/content/{version}/source/{source}/{id}/descendants](ancestors-and-descendants/) | Retrieves all descendants of a source-asserted identifier
 |GET | [/content/{version}/source/{source}/{id}/relations](source-asserted-identifiers/relations/) | Retrieves all relationships of a source-asserted identifier
 |GET | [/content/{version}/source/{source}/{id}/attributes](source-asserted-identifiers/attributes/) | Retrieves information about source-asserted attributes
 |GET | [/semantic-network/{version}/TUI/{id}](/rest/semantic-network/) | Retrieves information for a known Semantic Type identifier (TUI)
 |GET | [/crosswalk/{version}/source/{source}/{id}](/rest/source-asserted-identifiers/crosswalk/) | Retrieves all source-asserted identifiers that share a UMLS CUI with a particular code
 
