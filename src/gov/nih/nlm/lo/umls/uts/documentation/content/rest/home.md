title=UTS REST API Home Page
date=2015-06-10
updated=2015-06-30
type=page
status=published
~~~~~~

**API Version:** 0.1 alpha

### Authentication Service URIs
Method Type|URI|Description
--- | --- | ---
POST | [https://utslogin.nlm.nih.gov/cas/v1/tickets](authentication.html) | Retrieves a Ticket Granting Ticket (TGT)
POST | [https://utslogin.nlm.nih.gov/cas/v1/tickets/{TGT}](authentication.html) | Retrieves a single-use Service Ticket

### Webservice URIs (Base URI - https://uts-ws.nlm.nih.gov)
Method Type|Sample URI|Description
--- | --- | ---
GET | [/rest/{version}/search](search/)| Retrieves CUIs when searching by term or code.
GET | [/rest/content/{version}/CUI/{CUI}](concept/) | Retrieves concepts and information about concepts.
GET | [/rest/content/{version}/CUI/{CUI}/atoms/](atoms/) | Retrieves atoms and information about atoms.
