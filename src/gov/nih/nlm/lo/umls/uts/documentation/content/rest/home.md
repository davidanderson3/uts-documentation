title=UTS REST API Home Page
date=2015-06-10
type=page
status=published
~~~~~~

## UTS REST API home page

**API Version:** 0.1 alpha

### Authentication Service URIs
Method Type|URI|Description
--- | --- | ---
POST | [https://utslogin.nlm.nih.gov/cas/v1/tickets](authentication.html) | Retrieves a Ticket Granting Ticket (TGT)
POST | [https://utslogin.nlm.nih.gov/cas/v1/tickets/{TGT}](authentication.html) | Retrieves a single-use Service Ticket

###Webservice URIs
Method Type|Sample URI|Description
--- | --- | ---
GET | [https://uts-ws.nlm.nih.gov/rest/search](/search/index.html)| Retrieves CUIs for specific strings
GET | [https://uts-ws.nlm.nih.gov/rest/content/{version}/CUI/{CUI}](/concepts/index.html) | Retrieves concepts and information about concepts
GET | [https://uts-ws.nlm.nih.gov/rest/content/{version}/CUI/{CUI}/atoms/](/atoms/index.html) | Retrieves atoms and information about atoms
GET | [https://uts-ws.nlm.nih.gov/rest/content/{version}/CUI/{CUI}/definitions/](/definitions/index.html) | Retrieve definitions and information about definitions
GET | [https://uts-ws.nlm.nih.gov/rest/content/{version}/CUI/{CUI}/relationships/](/relationships/index.html) | Retrieve relationships and information about relationships
