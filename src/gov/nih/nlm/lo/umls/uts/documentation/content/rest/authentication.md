title=UTS REST API Authentication
date=2015-06-10
type=page
status=published
~~~~~~


**API Version:** 0.1 alpha

## User Authentication

**Each call to https://uts-ws.nlm.nih.gov/rest requires a Service Ticket as a query parmeter.
A service ticket is good for one call and will expire after 5 minutes if not used.**

The UTS REST authentication involves 2 steps:

*  Getting a Ticket Granting Ticket (TGT) using UMLS credentials. The TGT is valid for 8 hours. **You do not need a new TGT for each call to the REST API.**
*  Getting a Service Ticket using the Ticket Granting Ticket. A  Service Ticket expires in five minutes from the time of generation or after one use, which ever comes first. Each REST call requires a new Service Ticket. 

Use your service tickets the value for the 'ticket' query parameter in GET calls to https://uts-ws.nlm.nih.gov/rest, such as:

```
https://uts-ws.nlm.nih.gov/rest/content/current/CUI/C0018787?ticket=ST-134-HUbXGfI765aSj0UqtdvU-cas
```


### URIs

*The base URI for authentication is https://utslogin.nlm.nih.gov*

Call # | Type of Request|URI|Required Parameters| Parameter values |Description
--- | --- | --
1|POST|https://utslogin.nlm.nih.gov/cas/v1/tickets | username,password | Your UMLS username and password |Retrieves a Ticket Granting Ticket (TGT) to be used repeatedly in call #2.
2|POST| https://utslogin.nlm.nih.gov/cas/v1/tickets/{TGT}| service | http://umlsks.nlm.nih.gov | Retrieves a single-use Service Ticket

###Sample Output:

**The response to the POST call for getting a TGT (your TGT of course will be unique)**

<pre>
&lt;!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN"&gt;&lt;html&gt;
&lt;head&gt;
&lt;title&gt;201 The request has been fulfilled and resulted in a new resource being created&lt;/title&gt;&lt;/head&gt;
&lt;body&gt;&lt;h1&gt;TGT Created&lt;/h1&gt;
&lt;form action="https://utslogin.nlm.nih.gov/cas/v1/tickets/TGT-36471-aYqNLN2rFIJPXKzxwdTNC5ZT7z3B3cTAKfSc5ndHQcUxeaDOLN-cas" method="POST"&gt;Service:&lt;input type="text" name="service" value=""&gt;
&lt;br&gt;&lt;input type="submit" value="Submit"&gt;&lt;/form&gt;
&lt;/body&gt;&lt;/html&gt;

take the 'action' attribute of the form element and re-use it as your URI to get a service ticket as in call #2 above.

</pre>


**Service Ticket**
```
ST-134-HUbXGfI765aSj0UqtdvU-cas
```