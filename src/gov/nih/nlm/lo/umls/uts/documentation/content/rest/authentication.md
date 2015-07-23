title=User Authentication
date=2015-06-10
updated=2015-06-25
type=page
status=published
navorder=2
~~~~~~


**Each call to https://uts-ws.nlm.nih.gov/rest requires a Service Ticket as a query parameter.
A service ticket is good for one call and will expire after 5 minutes if not used.**

The UTS REST authentication involves 2 steps:

*  Getting a Ticket Granting Ticket (TGT) using UMLS credentials. The TGT is valid for 8 hours. **You do not need a new TGT for each call to the REST API.**
*  Getting a Service Ticket using the Ticket Granting Ticket. A  Service Ticket expires in five minutes from the time of generation or after one use, which ever comes first. Each REST call requires a new Service Ticket. 

Use your service tickets the value for the 'ticket' query parameter in GET calls to https://uts-ws.nlm.nih.gov/rest, such as:

~~~~xml
https://uts-ws.nlm.nih.gov/rest/content/current/CUI/C0018787?ticket=ST-134-HUbXGfI765aSj0UqtdvU-cas
~~~~


### URIs

**The base URI for authentication is https://utslogin.nlm.nih.gov**

Call # | Type of Request|URI|Required Parameters| Parameter values |Description
--- | --- | --
1|POST|https://utslogin.nlm.nih.gov/cas/v1/tickets | username,password | Your UMLS username and password |Retrieves a Ticket Granting Ticket (TGT) to be used repeatedly in call #2.
2|POST| https://utslogin.nlm.nih.gov/cas/v1/tickets/{TGT}| service | http://umlsks.nlm.nih.gov | Retrieves a single-use Service Ticket

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

**Sample Response to a POST call for a service ticket:**

~~~~tex
ST-134-HUbXGfI765aSj0UqtdvU-cas
~~~~