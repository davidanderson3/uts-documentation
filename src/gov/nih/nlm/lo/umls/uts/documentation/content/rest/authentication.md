title=User Authentication
date=2015-06-10
updated=2016-09-06
type=page
status=published
navorder=2
~~~~~~


The UMLS REST API requires a UMLS account for the authentication described below. If you do not have a UMLS account, you may apply for a license on the [UMLS Terminology Services (UTS) website](https://uts.nlm.nih.gov). 

Authentication involves **3 steps** and requires you to generate and submit forms using POST calls. You may find [Postman](https://www.getpostman.com/), [Hurl.it](https://www.hurl.it/), or a number of other tools useful for making these POST calls. You can also check out the [Postman sample collections](/rest/rest-api-cookbook/postman.html), or [code samples in Python, Java, and Perl on Github](https://github.com/HHS/uts-rest-api) to help you. We also offer an [authentication demo](#demo).

For help with making authentication calls using Postman, see our tutorial: [UMLS REST API: Authentication and Calling](https://www.nlm.nih.gov/research/umls/user_education/quick_tours/UTS-API/UTS_REST_API_Authentication.html). 

<a href="#demo"><input class="formButton" type="submit" value="TRY OUR AUTHENTICATION DEMO"></a>

#### Step 1: Determine whether you want to use your UMLS username and password OR your UMLS API key.

* If you choose to use an API key instead of your username and password, you can find the API key in the [UTS 'My Profile' area](https://uts.nlm.nih.gov) after signing in. An API key remains active as long as the associated UTS account is active.
* If the API key field in your UTS profile is blank, click 'Edit Profile', select the 'Generate new API Key' checkbox, then scroll down and click 'Save Profile'. Your new API key is now available for use.

#### Step 2: Get a Ticket-Granting Ticket (TGT). The TGT is valid for 8 hours. **You do not need a new TGT for each REST API call.**

* NOTE: You should include the key names and key values within the url-encoded body of the form in your POST call.

**Option 1**: Use your API key

Type of Request|URI|Key Names|Key Values|Description
--- | --- | --
POST| https://utslogin.nlm.nih.gov/cas/v1/api-key | apikey | Your UMLS API key |Retrieves a TGT to be used repeatedly for getting Service Tickets.

curl example:

~~~~text
curl -X POST https://utslogin.nlm.nih.gov/cas/v1/api-key -H 'content-type: application/x-www-form-urlencoded' -d apikey={your_api_key_here}
~~~~

**Option 2**: Use your username and password

Type of Request|URI|Key Names|Key Values|Description
--- | --- | --
POST| https://utslogin.nlm.nih.gov/cas/v1/tickets | username,password | Your UMLS username and password |Retrieves a TGT to be used repeatedly for getting Service Tickets.

curl example:

~~~~text
curl -X POST https://utslogin.nlm.nih.gov/cas/v1/tickets -H 'content-type: application/x-www-form-urlencoded' -d username={your_username_here}&password={your_password_here}
~~~~

Sample response to the POST call for getting a TGT (your TGT of course will be unique):

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


#### Step 3: Get a Service Ticket. **A Service Ticket expires after one use or five minutes from the time of generation, whichever comes first. Each REST API call requires a new Service Ticket.**

* NOTE: You should include the key names and key values within the url-encoded body of the form in your POST call.

Getting a Service Ticket

Type of Request|URI|Key Name|Key Value|Description
--- | --- | --
POST|https://utslogin.nlm.nih.gov/cas/v1/tickets/{TGT}|service|http://umlsks.nlm.nih.gov|Retrieves a single-use service ticket for the UMLS REST API.

curl example:

~~~~text
curl -X POST https://utslogin.nlm.nih.gov/cas/v1/tickets/{your_TGT_here} -H 'content-type: application/x-www-form-urlencoded' -d service=http%3A%2F%2Fumlsks.nlm.nih.gov
~~~~

Sample Response to a POST call for a Service Ticket:

~~~~text
ST-134-HUbXGfI765aSj0UqtdvU-cas
~~~~


**Making use of your Service Tickets**

* Use your service tickets as the value for the 'ticket' query parameter in GET calls to https://uts-ws.nlm.nih.gov/rest, such as this call to retrieve information about CUI:C0018787: `https://uts-ws.nlm.nih.gov/rest/content/current/CUI/C0018787?ticket=ST-134-HUbXGfI765aSj0UqtdvU-cas`


**Validating your service ticket**

* The easiest way to verify you've implemented authentication correctly is to use a browser to navigate to the following URL:  
   **https://utslogin.nlm.nih.gov/cas/serviceValidate?ticket={ST}&service=http://umlsks.nlm.nih.gov**  

* If your service ticket is valid, you'll receive a string that corresponds to either your UMLS username or API Key, depending on which option you used to generate your ticket-granting ticket.  
    * A ticket generated against the wrong service will return the following error: ```<cas:authenticationFailure code='INVALID_SERVICE'>```  
    * An invalid service ticket will return the following error: ```<cas:authenticationFailure code='INVALID_TICKET'>``` 
    
