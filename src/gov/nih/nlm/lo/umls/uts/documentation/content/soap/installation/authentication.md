title=UMLS SOAP API Authentication Interface
date=2015-08-13
updated=2015-08-13
type=page
status=published
navorder=1
~~~~~~

Interface | Method | Use Case | Object or Data type Returned | Guidance
-- | -- | -- | --
**UtsWsSecurityControllerController**|||||
 |[getProxyGrantTicket](#getproxygrantticket)|Retrieve a proxy grant ticket (also known as a ticket granting ticket).|String|Generate one time, normally when your application starts up. A ticket granting ticket is good for 8 hours, and is needed for the getProxyTicket() method below.  **You do not need to generate a new ticket granting ticket for each call to the API**.
 |[getProxyTicket](#getproxyticket)|Retrieve a **single-use** service ticket to make calls to the API.|String|Use these service tickets when making calls to the content, history, metadata, etc interfaces.  These tickets are good for one use or 5 minutes, whichever comes first. 
 |[validateProxyTicket](#validateproxyticket)|Validate a single-use service ticket.|String| Returns the username of the person who requested the service ticket.  This is useful if you are hosting UMLS content and want to validate that your users are UMLS licensees|

 **Below is an example of how to create an instance of the UtsWsSecurityInterface**
 
### Authentication

In general, your application will follow this sequence when making calls to the API:

1.  Obtain a Proxy Grant Ticket using the getProxyGrantTicket method described below. This is good for 8 hours and is needed for step #2
2.  Generate a Single Use Ticket (using the Proxy Grant Ticket and the string "http://umlsks.nlm.nih.gov" as parameters) with the getProxyTicket method described below.
3.  Make a call to the API, passing the Single Use Ticket as one of the parameters.
4.  Repeat steps 2 and 3 while your application is in use.

### getProxyGrantTicket

**Method Signature**: getProxyGrantTicket(String username, String password)

~~~~java
//use your UMLS username and password
private String username = "InformaticsResearcher";
private String password = "C0des@reCool";

private String ticketGrantingTicket = securityService.getProxyGrantTicket(username, password);
~~~~


### getProxyTicket

**Method Signature**: getProxyTicket(String ticketGrantingTicket, String targetService)

~~~~java
private String serviceName = "http://umlsks.nlm.nih.gov";

private String getProxyTicket() {
 try {
 return securityService.getProxyTicket(ticketGrantingTicket, serviceName);
 }
 catch (Exception e) {
 return "";
 }
}

//Pass the Single-Use ticket as a parameter with each call to the API. 
~~~~