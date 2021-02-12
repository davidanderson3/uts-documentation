title=UMLS REST API Home Page
date=2015-06-10
updated=2016-07-07
type=page
status=published
navorder=1
~~~~~~


### Authentication Service Endpoint
The authentication service provides methods for retrieving a ticket granting ticket as well as single-use service tickets.
Service tickets are needed each time you search or retrieve content from the UMLS REST API. 
For help with making authentication calls using Postman, see our tutorial: [UMLS REST API: Authentication and Calling](https://www.nlm.nih.gov/research/umls/user_education/quick_tours/UTS-API/UTS_REST_API_Authentication.html).

Base URI|Method Type|Path|Description
--- | --- | --- | --
**https://utslogin.nlm.nih.gov**||||
 |POST|[/cas/v1/api-key](authentication.html) | Retrieves a Ticket Granting Ticket (TGT)
 |POST|[/cas/v1/tickets/{TGT}](authentication.html) | Retrieves a single-use Service Ticket

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
 |GET | [/subsets/{version}/](source-asserted-identifiers/subsets/) | Retrieves all available source-asserted subsets
 |GET | [/subsets/{version}/source/{source}/{id}](source-asserted-identifiers/subsets/) | Retrieves information about a specific source-asserted subset
 |GET | [/subsets/{version}/source/{source}/{id}/members](source-asserted-identifiers/subsets/) | Retrieves members of a specific source-asserted subset
 |GET | [/subsets/{version}/source/{source}/{id}/member/{id}](source-asserted-identifiers/subsets/) | Retrieves an individual member of a specific source-asserted subset
 |GET | [/content/{version}/source/{source}/{id}/attributes](source-asserted-identifiers/attributes/) | Retrieves information about source-asserted attributes
 |GET | [/semantic-network/{version}/TUI/{id}](/rest/semantic-network/) | Retrieves information for a known Semantic Type identifier (TUI)
 |GET | [/content-views/{version}](/rest/content-views/) | Retrieve all available [content views](https://www.nlm.nih.gov/research/umls/knowledge_sources/metathesaurus/release/content_views.html) in the UMLS
 |GET | [/content-views/{version}/CUI/{CUI}](/rest/content-views/) | Retrieve information about a specific content view
 |GET | [/content-views/{version}/CUI/{CUI}/members](/rest/content-views/) | Retrieve members of a specific content view
 |GET | [/content-views/{version}/CUI/{CUI}/member/{id}](/rest/content-views/) | Retrieves an individual member of a specific content view
 |GET | [/crosswalk/{version}/source/{source}/{id}](/rest/source-asserted-identifiers/crosswalk/) | Retrieves all source-asserted identifiers that share a UMLS CUI with a particular code
 