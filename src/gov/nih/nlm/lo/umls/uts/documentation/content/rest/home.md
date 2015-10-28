title=UMLS REST API Home Page
date=2015-06-10
updated=2015-09-30
type=page
status=published
navorder=1
~~~~~~


### Authentication Service URIs

Method Type|URI|Description
--- | --- | ---
POST | [https://utslogin.nlm.nih.gov/cas/v1/tickets](authentication.html) | Retrieves a Ticket Granting Ticket (TGT)
POST | [https://utslogin.nlm.nih.gov/cas/v1/tickets/{TGT}](authentication.html) | Retrieves a single-use Service Ticket

### Webservice URIs (Base URI - https://uts-ws.nlm.nih.gov/rest)

Method Type|Sample URI|Description
--- | --- | ---
GET | [/search/{version}](search/)| Retrieves CUIs when searching by term or code
GET | [/content/{version}/CUI/{CUI}](concept/) | Retrieves information about a known CUI
GET | [/content/{version}/CUI/{CUI}/atoms](atoms/) | Retrieves atoms and information about atoms for a known CUI
GET | [/content/{version}/CUI/{CUI}/definitions](definitions/) | Retrieves definitions for a known CUI
GET | [/content/{version}/CUI/{CUI}/relations](relations/) | Retrieves NLM-asserted relationships for a known CUI
GET | [/content/{version}/source/{source}/{id}](source-asserted-identifiers/) | Retrieves information about a known source-asserted identifier
GET | [/content/{version}/source/{source}/{id}/atoms](atoms/) | Retrieves information about atoms for a known source-asserted identifier
GET | [/content/{version}/source/{source}/{id}/parents](parents-and-children/) | Retrieves immediate parents of a source-asserted identifier
GET | [/content/{version}/source/{source}/{id}/children](parents-and-children/) | Retrieves immediate children of a source-asserted identifier
GET | [/content/{version}/source/{source}/{id}/ancestors](ancestors-and-descendants/) | Retrieves all ancestors of a source-asserted identifier
GET | [/content/{version}/source/{source}/{id}/descendants](ancestors-and-descendants/) | Retrieves all descendants of a source-asserted identifier
GET | [/content/{version}/source/{source}/{id}/relations](source-asserted-identifiers/relations/) | Retrieves all relationships of a source-asserted identifier
GET | [/content/{version}/source/{source}/{id}/subsets](source-asserted-identifiers/subsets/) | Retrieves information about source-asserted subsets

### Code Sample Repository
The [Code Sample Repository on GitHub](https://github.com/HHS/uts-rest-api) features code samples in various languages that show how to use the UMLS REST API. The repository currently includes code samples in Java, Perl, and Python.