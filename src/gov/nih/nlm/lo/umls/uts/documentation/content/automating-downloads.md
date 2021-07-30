title=Automating UMLS Terminology Services Downloads 
date=2020-12-28
updated=2020-12-28
type=page
status=published
navorder=1
~~~~~~

<hr />

###The following instructions will allow you to automate the download of RxNorm, UMLS, or SNOMED CT files. Implementation depends on your local environment. 

<hr />
#### **Step 1**: Get your API key from your UTS profile.

* You can find the API key in the [UTS 'My Profile' area](https://uts.nlm.nih.gov/uts/) after signing in. An API key remains active as long as the associated UTS account is active.

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
curl -d "apikey={your_api_key_here}" -H "Content-Type: application/x-www-form-urlencoded" -X POST https://utslogin.nlm.nih.gov/cas/v1/api-key
~~~~

Sample response to the POST call for getting a TGT:

~~~~xml
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html>
<head>
<title>201 The request has been fulfilled and resulted in a new resource being created</title></head>
<body><h1>TGT Created</h1>
<form action="https://utslogin.nlm.nih.gov/cas/v1/tickets/{TGT}" method="POST">Service:<input type="text" name="service" value="">
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

* Download the file using a service ticket and a cookie file:

~~~~text
curl -s -c cookie.txt -b cookie.txt -L -O -J https://download.nlm.nih.gov/umls/kss/rxnorm/RxNorm_full_current.zip?ticket={service_ticket}
~~~~

<hr />

####Sample Script

This script may need to be modified depending on your local environment. 

~~~~text
#!/bin/bash

#1. Add your API key from https://uts.nlm.nih.gov/uts/profile
#2. Run the script (for example: bash curl-uts-downloads-apikey.sh https://download.nlm.nih.gov/umls/kss/rxnorm/RxNorm_weekly_current.zip)

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

curl -c cookie.txt -b cookie.txt -L -O -J $DOWNLOAD_URL?ticket=$STTICKET
rm cookie.txt
~~~~

This script for the Windows PowerShell is a user submission and may need to be modified depending on your local environment. 

~~~~text
<#
.SYNOPSIS
This script automates the download of the full RxNorm dataset.
.DESCRIPTION
This script automates the download of the full RxNorm dataset using the new authentication
protocols established by NLM in late 2020. This powershell script created using the sample
bash script and documentation provided by the NLM as a guide. The NLM documentation is
available at:  https://documentation.uts.nlm.nih.gov/automating-downloads.html
.EXAMPLE
On a powershell or cmd shell, execute the following code from the directory containing the script
powershell -ExecutionPolicy bypass -File RxNormDownload.ps1
.OUTPUTS
Log File: .\logs\RxNormDownload_YYYYMMDD.log
RxNorm Zip File: .\RxNorm_full_current.zip
.NOTES
======================================================================================================
Script Name: RxNormDownload.ps1
Version:     1.0.0
Create date: 12/16/2020
======================================================================================================
#>
 
###########################################################################################################
# ------------------------------ Initializations ------------------------------
#
# Set Error Action to Silently Continue
$ErrorActionPreference = 'SilentlyContinue'
 
# Track running time.
$StopWatch = [ordered]@{
  Total = [System.Diagnostics.Stopwatch]::StartNew()
}
 
# Set the security protocol to ensure connectivity
# Using TLS 1.2 is important
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
 
# ------------------------------ Script Variables -----------------------------
 
########################################################################
# Standard Variables
########################################################################
 
# Establish the script name
$scriptName = "RxNormDownload"
 
# Main Folder and Path Variables
$homeFolder = $PSScriptRoot
Write-Output "homeFolder = $homeFolder`n"
 
# Log File Info
$date = Get-Date -format yyyyMMdd
$logFolder = Join-Path -Path $homeFolder -ChildPath "logs"
$logFileName = $scriptName + "_" + $date + ".log"
$logFilePath = Join-Path -Path $logFolder -ChildPath $logFileName
 
# Create log folder if it does not exist
If (!(Test-Path $logFolder)) {
  Write-Output "$logFolder`nDOES NOT EXIST"
  Write-Output "Creating $logFolder`n"
  New-Item -ItemType Directory -Force -Path $logFolder
}
 
########################################################################
# User Defined Variables
########################################################################
 
# Add your API key from https://uts.nlm.nih.gov/uts/profile
# You can find the API key in the UTS ‘My Profile’ area after signing in.
# An API key remains active as long as the associated UTS account is active.
$apiKey = ""
 
# CAS login URL
$casLoginUrl = "https://utslogin.nlm.nih.gov/cas/v1/api-key"
 
# Choose your the download file you are trying to download
# Make sure to only have one like uncommented
 
$downloadUrl = "https://download.nlm.nih.gov/umls/kss/rxnorm/RxNorm_full_current.zip"
# $downloadUrl = "https://download.nlm.nih.gov/umls/kss/rxnorm/RxNorm_weekly_current.zip"
 
# Output the RxNorm Zip file download to the local folder
$downloadFilePath = Join-Path -Path $homeFolder -ChildPath "RxNorm_full_current.zip"
 
# ------------------------------- Script Logic --------------------------------
 
Try {
  If ($homeFolder -ne $PSScriptRoot) {
    Throw  'Must Execute the script from the script folder...'
  }
 
  # Start the Logging
  Start-Transcript -Path $logFilePath -Force -Append
  Write-Output "`n############################### $scriptName STARTED ###############################`n"
 
  ########################################################################
  ## Get a Ticket-Granting Ticket (TGT)
  ########################################################################
  ## The TGT is valid for 8 hours. You do not need a new TGT for each
  ## REST API call.
  ########################################################################
 
  # Track step time
  $step = "Get_Ticket_Granting_Ticket"
  Write-Output "BEGIN STEP: $step`n"
  $StopWatch.$($step) = [System.Diagnostics.Stopwatch]::StartNew()
 
  # Setup the parameters to get make the web request for your TGT
  $tgtResquestParams = @{
    "URI"     = $casLoginUrl
    "Body"    = "apikey=$apiKey"
    "Method"  = 'POST'
    "Headers" = @{
      "Content-Type" = 'application/x-www-form-urlencoded'
    }
  }
 
  Write-Output "Retrieving Ticket-Generated Ticket"
  # Make the WebRequest to obtain your TGT value
  $tgtResponse = Invoke-WebRequest @tgtResquestParams
 
  # Get the TGT value by parsing the HTML returned from the WebRequest
  # and parse to obtain the {TGT} value
  # The response returns an HTML block that looks like:
  <#
  <html>
    <head>
      <title>201 The request has been fulfilled and resulted in a new resource being created</title>
    </head>
    <body>
      <h1>TGT Created</h1>
      <form action="https://utslogin.nlm.nih.gov/cas/v1/tickets/{TGT}" method="POST">
        Service:<input type="text" name="service" value=""><br><input type="submit" value="Submit">
      </form>
    </body>
  </html>
  #>
 
  $tgtValue = (($tgtResponse.ParsedHtml.getElementsByTagName('FORM')) | `
        Select-Object -ExpandProperty action).split("/")[-1]
  Write-Output "TGT Value: $tgtValue`n"
 
  # Stop step timer.
  $StopWatch.$($step).Stop()
  Write-Output "`nEND STEP: $step"
 
  ########################################################################
  ## Get a Service Ticket
  ########################################################################
  ## A Service Ticket expires after one use or five minutes
  ## from the time of generation, whichever comes first.
  ## Each REST API call requires a new Service Ticket.
  ########################################################################
 
  # Track step time
  $step = "Get_Service_Ticket"
  Write-Output "BEGIN STEP: $step`n"
  $StopWatch.$($step) = [System.Diagnostics.Stopwatch]::StartNew()
 
  # Download Content Usint the TGT Value
  $stParams = @{
    "URI"     = "https://utslogin.nlm.nih.gov/cas/v1/tickets/$tgtValue"
    "Body"    = "service=$downloadUrl"
    "Method"  = 'POST'
    "Headers" = @{
      "Content-Type" = 'application/x-www-form-urlencoded'
    }
  }
 
  # Make the WebRequest to obtain your Service Ticket
  # Note the use of a session variable, we will reuse this session later
  # to retain the cookie from the session.
  Write-Output "Retrieving Service Ticket"
  $serviceTicket = Invoke-WebRequest @stParams -SessionVariable session
  Write-Output "serviceTicket: $serviceTicket"
 
  # Stop step timer.
  $StopWatch.$($step).Stop()
  Write-Output "`nEND STEP: $step"
  ########################################################################
  ## Download the File
  ########################################################################
  ## A Service Ticket expires after one use or five minutes
  ## from the time of generation, whichever comes first.
  ## Each REST API call requires a new Service Ticket.
  ########################################################################
 
  # Track step time
  $step = "Download_RxNorm_File"
  Write-Output "BEGIN STEP: $step`n"
  $StopWatch.$($step) = [System.Diagnostics.Stopwatch]::StartNew()
 
  # Construct your download URL using the Service Ticket
  $completeDownloadUrl = "$downloadUrl" + "?ticket=$serviceTicket"
  Write-Output "completeDownloadUrl: $completeDownloadUrl"
 
  # Remove the progress bar from the download
  # The progress bar has a massive impact on the speed of the download
  $ProgressPreference = 'SilentlyContinue'
 
  # Download the file and output to the local directory
  # Using ContetType = "application/octet-stream" speeds up the download
  Write-Output "Downloading RxNorm ZIP File"
  Invoke-WebRequest $completeDownloadUrl `
    -ContentType "application/octet-stream" `
    -WebSession $session `
    -OutFile $downloadFilePath
 
  # Reset ProgressPreference
  $ProgressPreference = 'Continue'
 
  # Stop step timer.
  $StopWatch.$($step).Stop()
  Write-Output "`nEND STEP: $step"
  Write-Output "`n############################### $scriptName ENDED ###############################`n"
 
  # Compute and display elapsed run time (Verbose stream.)
  $StopWatch.Total.Stop()
  $StepTimes = @(
    $StopWatch.Keys | Where-Object { $_ -ne 'Total' } | `
      ForEach-Object { [pscustomobject]@{ Step = $_ ; ElapsedTime = $StopWatch.Item($_).Elapsed.ToString() } }
)
$StepTimes | Out-String -Stream | Where-Object { $_ -ne "" } | Write-Verbose
Write-Verbose ""
Write-Verbose "TOTAL $($Stopwatch.Total.Elapsed.ToString())"
 
###########################################################################################################
 
}
# Error handling
Catch {
  $ErrorInfo = $Error[0]
  '='.PadRight(100, '=') | Out-Default
  [PSCustomObject]@{
    ScriptName   = $ErrorInfo.InvocationInfo.ScriptName
    ErrorMessage = $ErrorInfo.Exception.Message
    LineNumber   = $ErrorInfo.InvocationInfo.ScriptLineNumber
    ColumnNumber = $ErrorInfo.InvocationInfo.OffsetInLine
    Category     = $ErrorInfo.CategoryInfo.Category
    ErrorReason  = $ErrorInfo.CategoryInfo.Reason
    Target       = $ErrorInfo.CategoryInfo.TargetName
    StackTrace   = $ErrorInfo.Exception.StackTrace
  } | Out-Default
  '='.PadRight(100, '=') | Out-Default
  Throw
}
Finally {
  Trap { Continue } Stop-Transcript
}
~~~~

This Python script may need to be modified depending on your local environment.

~~~~text
import requests, sys

#please add apikey
apikey=''
DOWNLOAD_URL='https://download.nlm.nih.gov/umls/kss/rxnorm/RxNorm_full_current.zip'
PATH_TO_DOWNLOAD=''
if len(sys.argv) > 1:
    DOWNLOAD_URL=sys.argv[1]

print(DOWNLOAD_URL)
value = DOWNLOAD_URL.split('/')

if not apikey:
    sys.exit("Please enter you api key ")

if not DOWNLOAD_URL:
    print("Usage: curl-uts-downloads-apikey.sh  download_url ")
    print("  e.g.   curl-uts-download-apikey.sh https://download.nlm.nih.gov/umls/kss/rxnorm/RxNorm_full_current.zip")
    print("         curl-uts-download-apikey.sh https://download.nlm.nih.gov/umls/kss/rxnorm/RxNorm_weekly_current.zip")
    sys.exit("Download_url is empyt")

url = 'https://utslogin.nlm.nih.gov/cas/v1/api-key'
param = {'apikey': apikey}
headers = {'Content-type': 'application/x-www-form-urlencoded'}

TGTresponse = requests.post(url, headers=headers, data = param)
first, second = TGTresponse.text.split('api-key/')
TGTTicket, fourth = second.split('" method')

print(TGTTicket)

url = 'https://utslogin.nlm.nih.gov/cas/v1/tickets/'+TGTTicket
param = {'service': DOWNLOAD_URL}
headers = {'Content-type': 'application/x-www-form-urlencoded'}

STResponse = requests.post(url, headers=headers, data = param)

print(STResponse.text)

url = DOWNLOAD_URL+'?ticket='+STResponse.text
r = requests.get(url, allow_redirects=True)
open('RxNorm_full_current.zip', 'wb').write(r.content)

with open(PATH_TO_DOWNLOAD + value[len(value)-1], 'wb') as f:
    f.write(r.content)

#Retrieve HTTP meta-data
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)

print('completed')
~~~~
 