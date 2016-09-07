title=UMLS SOAP API Authentication Interface
date=2015-08-13
updated=2016-05-05
type=page
status=published
navorder=1
~~~~~~

**New**: The [getProxyGrantTicketWithApiKey](#getproxygrantticketwithapikey) method gives users an additional authentication option when requesting a
ticket-granting ticket (or Proxy Grant Ticket).  Rather than username/password, users can pass their api key (available in the UTS 'My Profile' area) as a parameter to
this method to obtain a ticket-granting ticket.   If your API Key appears blank in your profile, perform the following steps:
*  Click 'Edit Profile'
*  Click 'Generate New API Key'
*  Click 'Save Profile'

Your new API Key is now available for use.


Interface | Method | Use Case | Object or Data type Returned | Guidance
-- | -- | -- | --
**UtsWsSecurityControllerController**|||||
 |[getProxyGrantTicket](#getproxygrantticket)|Retrieve a proxy grant ticket (also known as a ticket-granting ticket).|String|Generate one time, normally when your application starts up. A ticket granting ticket is good for 8 hours, and is needed for the getProxyTicket() method below.  **You do not need to generate a new ticket granting ticket for each call to the API**.
 |[getProxyGrantTicketWithApiKey](#getproxygrantticketwithapikey)|Retrieve a proxy grant ticket (also known as a ticket-granting ticket).|String|Generate one time, normally when your application starts up. A ticket granting ticket is good for 8 hours, and is needed for the getProxyTicket() method below. **You do not need to generate a new ticket granting ticket for each call to the API**.
 |[getProxyTicket](#getproxyticket)|Retrieve a **single-use** service ticket to make calls to the API.|String|Use these service tickets when making calls to the content, history, metadata, etc interfaces.  These tickets are good for one use or 5 minutes, whichever comes first. **You may also use these service tickets for the AccessGUDID API (when retrieving SNOMED CT information).**
 |[validateProxyTicket](#validateproxyticket)|Validate a single-use service ticket.|String| Returns the username of the person who requested the service ticket.  This is useful if you are hosting UMLS content and want to validate that your users are UMLS licensees|

**The examples below requires an instance of the [UtsWsSecurityController](/soap/installation/interface-setup.html#utswssecuritycontroller) interface**.



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

private String ticketGrantingTicket = utsSecurityService.getProxyGrantTicket(username, password);

//returns a ticket-granting ticket, such as TGT-296-vRJn4UOsEBNugGUVCHTHkbZjvSa43lzdmeT3b6S7HihrWyXC0-cas
~~~~


### getProxyGrantTicketWithApiKey
**Method Signature**: getProxyGrantTicketWithApiKey(String apikey)


~~~~java
//use your UMLS API key from the 'My Profile' area of your UTS account

private String apikey = "123456abcdef-g";
private String ticketGrantingTicket = utsSecurityService.getProxyGrantTicketWithApiKey(apikey);

//returns a ticket-granting ticket, such as TGT-296-vRJn4UOsEBNugGUVCHTHkbZjvSa43lzdmeT3b6S7HihrWyXC0-cas
~~~~

### getProxyTicket

**Method Signature**: getProxyTicket(String ticketGrantingTicket, String targetService)

~~~~java
private String serviceName = "http://umlsks.nlm.nih.gov";

private String getProxyTicket() {
 try {
 return utsSecurityService.getProxyTicket(ticketGrantingTicket, serviceName);
 }
 catch (Exception e) {
 return "";
 }
}

~~~~

### validateProxyTicket

**Method Signature**: ```validateProxyTicket(String serviceTicket, String targetService)```

~~~~java
private String serviceName = "http://umlsks.nlm.nih.gov";

//below is a SAMPLE service ticket
String user = utsSecurityService.validateProxyTicket("ST-890427-tH2kLYxbuOMSKWUOcbH5-cas", "http://umlsks.nlm.nih.gov")
~~~~

If you obtained your ticket-granting ticket by authenticating with your UMLS username and password,
the validateProxyTicket method returns the UMLS username who requested the ticket, such as ```JoeCoolResearcher```.

If you obtained your ticket-granting ticket by authenticating with your UMLS API Key,
the validateProxyTicket method returns the user's API key, such as ```123456abcdef-g```.