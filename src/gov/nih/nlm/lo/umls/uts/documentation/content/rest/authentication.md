title=User Authentication
date=2015-06-10
updated=2016-05-09
type=page
status=published
navorder=2
~~~~~~


The UMLS REST API requires a UMLS username and password or a UMLS API key for the authentication described below. If you do not have a UMLS account, you may apply for a license on the [UMLS Terminology Services (UTS) website](https://uts.nlm.nih.gov). 

The UTS REST authentication involves 3 steps:

1. Determining whether you want to use your UMLS username and password OR a UMLS API key to authenticate that you have an active UTS account.
	+ If you choose to use an API key instead of your username and password, you can find the API key in the [UTS 'My Profile' area](https://uts.nlm.nih.gov) after signing in. An API key remains active as long as the associated UTS account is active.
2. Getting a Ticket-Granting Ticket (TGT) using UMLS credentials. The TGT is valid for 8 hours. **You do not need a new TGT for each call to the REST API.**
3. Getting a Service Ticket using the Ticket Granting Ticket. **A  Service Ticket expires five minutes from the time of generation or after one use, which ever comes first. Each REST call requires a new Service Ticket.** 
    + You can also [validate a service ticket](#ticket-validation) if you want to make sure you've implemented the authentication service correctly. Once validated, the service ticket can no longer be used.

Use your service tickets as the value for the 'ticket' query parameter in GET calls to https://uts-ws.nlm.nih.gov/rest, such as:

~~~~xml
https://uts-ws.nlm.nih.gov/rest/content/current/CUI/C0018787?ticket=ST-134-HUbXGfI765aSj0UqtdvU-cas
~~~~


### URIs

**The base URI for authentication is https://utslogin.nlm.nih.gov/cas/v1**

---------------------------------------

**Choose ONE of the following methods for getting a Ticket-Granting Ticket (TGT):**

**Option 1:** Getting a Ticket-Granting Ticket (TGT) with your username and password

Type of Request|URI|Key Names| Key Values|Description
--- | --- | --
POST| /tickets | username,password | Your UMLS username and password |Retrieves a Ticket Granting Ticket (TGT) to be used repeatedly for getting Service Tickets.

**Option 2:** Getting a Ticket-Granting Ticket (TGT) with your API key

Type of Request|URI|Key Names| Key Values|Description
--- | --- | --
POST| /api-key | apikey | Your UMLS API key |Retrieves a Ticket Granting Ticket (TGT) to be used repeatedly for getting Service Tickets.

---------------------------------------

**Once you have a TGT, use the TGT to generate Service Tickets:** 

Getting a Service Ticket (ST)

Type of Request|URI|Key Names| Key Values|Description
--- | --- | --
POST| /tickets/{TGT}| service | http://umlsks.nlm.nih.gov | Retrieves a single-use Service Ticket for the UMLS REST API. **You may also use these Service Tickets for the AccessGUDID API (when retrieving SNOMED CT information), or the VSAC API.**

###Sample Output:

**Sample response to the POST call for getting a TGT (your TGT of course will be unique):**

~~~~xml
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html>
<head>
<title>201 The request has been fulfilled and resulted in a new resource being created</title></head>
<body><h1>TGT Created</h1>
<form action="https://utslogin.nlm.nih.gov/cas/v1/tickets/TGT-36471-aYqNLN2rFIJPXKzxwdTNC5ZT7z3B3cTAKfSc5ndHQcUxeaDOLN-cas" method="POST">Service:<input type="text" name="service" value="">
<br><input type="submit" value="Submit"></form>
</body>
</html>

<!--take the 'action' attribute of the form element and re-use it as your URI to get a service ticket as in call #2 above.-->
~~~~

**Sample Response to a POST call for a Service Ticket:**

~~~~text
ST-134-HUbXGfI765aSj0UqtdvU-cas
~~~~

#### Ticket validation

We provide an endpoint that validates a service ticket.  This allows you to verify that you've implemented the authentication service correctly.
The easiest way to verify you've implemented authentication correctly is to use a browser to navigate to the URL below.

**http://utslogin.nlm.nih.gov/cas/serviceValidate?ticket={ST}&service=http://umlsks.nlm.nih.gov**

If your service ticket is valid, you'll receive a string that corresponds to either your UMLS username or API Key (depending on how you generated your ticket granting ticket), such as ```InformaticsUser```.
A ticket generated against the wrong service will return a ```<cas:authenticationFailure code='INVALID_SERVICE'>``` error in the response.
An invalid service ticket will return a ```<cas:authenticationFailure code='INVALID_TICKET'>``` error in the response.