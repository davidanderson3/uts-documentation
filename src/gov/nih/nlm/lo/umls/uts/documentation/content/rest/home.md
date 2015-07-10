title=UTS REST API Home Page
date=2015-06-10
updated=2015-07-09
type=page
status=published
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
GET | /content/{version}/CUI/{CUI}/relations | Retrieves relationships for a known CUI
GET | [/content/{version}/source/{source}/{id}](source-asserted-identifiers/) | Retrieves information about a known source-asserted identifier
GET | [/content/{version}/source/{source}/{id}/atoms](atoms/) | Retrieves information about atoms for a known source-asserted identifier
GET | [/content/{version}/source/{source}/{id}/parents](parents-and-children/) | Retrieves immediate parents of a source-asserted identifier
GET | [/content/{version}/source/{source}/{id}/children](parents-and-children/) | Retrieves immediate children of a source-asserted identifier
