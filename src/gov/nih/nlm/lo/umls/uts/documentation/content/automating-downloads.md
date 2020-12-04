title=Automating UMLS Terminology Services Downloads 
date=2020-12-02
updated=2020-12-02
type=page
status=published
navorder=1
~~~~~~

The following script will automate the download of RxNorm, UMLS, or SNOMED CT files. This script may need to be adapted for your local environment. 

<center>###[SAMPLE DOWNLOAD SCRIPT](scripts/curl-uts-download-apikey.sh)</center>
~~~~text
#!/bin/bash

#1. Add your API key from https://uts.nlm.nih.gov/uts/profile
#2. Run the script (for example: bash curl-uts-downloads-apikey.sh curl-uts-download-apikey.sh https://download.nlm.nih.gov/umls/kss/rxnorm/RxNorm_weekly_current.zip)

export apikey=
export DOWNLOAD_URL=$1

export CAS_LOGIN_URL=https://utslogin.nlm.nih.gov/cas/v1/api-key

if [ -z "$apikey" ]; then echo " Please enter you api key "
   exit
fi

if [ $# -eq 0 ]; then echo "Usage: curl-uts-downloads-apikey.sh  download_url "
                      echo "  e.g.   curl-uts-download-apikey.sh https://download.nlm.nih.gov/umls/kss/rxnorm/RxNorm_full_current.zip"
                      echo "         curl-uts-download-apikey.sh https://download.nlm.nih.gov/umls/kss/rxnorm/RxNorm_weekly_current.zip"
   exit
fi

TGT=$(curl -d "apikey="$apikey -H "Content-Type: application/x-www-form-urlencoded" -X POST https://utslogin.nlm.nih.gov/cas/v1/api-key)

TGTTICKET=$(echo $TGT | tr "=" "\n")

for TICKET in $TGTTICKET
do
    if [[ "$TICKET" == *"TGT"* ]]; then
	  SUBSTRING=$(echo $TICKET| cut -d'/' -f 7)
	  TGTVALUE=$(echo $SUBSTRING | sed 's/.$//')
	fi
done
echo $TGTVALUE
STTICKET=$(curl -d "service="$DOWNLOAD_URL -H "Content-Type: application/x-www-form-urlencoded" -X POST https://utslogin.nlm.nih.gov/cas/v1/tickets/$TGTVALUE)
echo $STTICKET

#curl $DOWNLOAD_URL?ticket=$STTICKET -O -J -Lcurl
curl -s -c cookie.txt -b cookie.txt -L -O -J $DOWNLOAD_URL?ticket=$STTICKET
rm cookie.txt
~~~~

###Detailed instructions for creating your own script to automate downloads:
<hr />
#### **Step 1**: Get your API key from your UTS profile.

* You can find the API key in the [UTS 'My Profile' area](https://uts.nlm.nih.gov) after signing in. An API key remains active as long as the associated UTS account is active.

<span style="background-color:pink;padding:10px;">**NOTE**: Use of username and password with any API that requires UTS authentication is now deprecated.</span>

<hr />
#### **Step 2**: Get a Ticket-Granting Ticket (TGT). The TGT is valid for 8 hours. **You do not need a new TGT for each REST API call.**

* NOTE: You should include the key names and key values within the url-encoded body of the form in your POST call.

Use your API key:

Type of Request|URI|Key Names|Key Values|Description
--- | --- | --
POST| https://utslogin.nlm.nih.gov/cas/v1/api-key | apikey | Your UMLS API key |Retrieves a TGT to be used repeatedly for getting Service Tickets.

curl example:

~~~~text
curl -d "apikey=USERYOUROWNAPIKEY" -H "Content-Type: application/x-www-form-urlencoded" -X POST https://utslogin.nlm.nih.gov/cas/v1/api-key
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

<hr />
#### **Step 3**: Get a Service Ticket. **A Service Ticket expires after one use or five minutes from the time of generation, whichever comes first. Each REST API call requires a new Service Ticket.**

* NOTE: You should include the key names and key values within the url-encoded body of the form in your POST call.

Getting a Service Ticket

Type of Request|URI|Key Name|Key Value|Description
--- | --- | --
POST|https://utslogin.nlm.nih.gov/cas/v1/tickets/{TGT}|service|The URL for the file you want to download, for example, https://download.nlm.nih.gov/umls/kss/rxnorm/RxNorm_full_current.zip|Retrieves a special service ticket that can be used to download the file specified in the service parameter.

curl example:

~~~~text
curl -d "service=https://download.nlm.nih.gov/umls/kss/rxnorm/RxNorm_full_current.zip" -H "Content-Type: application/x-www-form-urlencoded" -X POST https://utslogin.nlm.nih.gov/cas/v1/tickets/{TGT}
~~~~

Sample Response to a POST call for a Service Ticket:

~~~~text
ST-134-HUbXGfI765aSj0UqtdvU-cas
~~~~
<hr />
#### **Step 4** **Download the File**

* Use the service ticket as the value for the 'ticket' query parameter and request the file:

~~~~text
curl -s -c cookie.txt -b cookie.txt -L -O -J https://download.nlm.nih.gov/umls/kss/rxnorm/RxNorm_full_current.zip?ticket={service_ticket}
~~~~
