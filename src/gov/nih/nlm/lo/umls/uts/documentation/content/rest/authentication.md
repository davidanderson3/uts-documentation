title=User Authentication
date=2015-06-10
updated=2021-03-01
type=page
status=published
navorder=2
~~~~~~

The UMLS REST API requires a UMLS account for the authentication described below. If you do not have a UMLS account, you may apply for a license on the [UMLS Terminology Services (UTS) website](https://uts.nlm.nih.gov). 

#### **Step 1**: Get your API key from your UTS profile.

* You can find the API key in the [UTS 'My Profile' area](https://uts.nlm.nih.gov/uts/profile) after signing in. An API key remains active as long as the associated UTS account is active.
* To generate a new API key, click 'Edit Profile', select the 'Generate new API Key' checkbox, then scroll down and click 'Save Profile'. Your new API key is now available for use.

#### **Step 2**: Append your API key to a data request.

For example, https://uts-ws.nlm.nih.gov/rest/content/current/CUI/C0009044?apiKey={{YOUR_API_KEY}}

<hr />

####<span style="color:red;"><b>Note</b>: AccessGUDID users can now use the [API Key authentication method](https://accessgudid.nlm.nih.gov/news). For AccessGUDID users that have previously implemented Ticket-Granting Tickets and Service Tickets for authentication, please refer to this documentation:</span>

[Ticket-Granting Ticket and Service Ticket Documentation](/authentication-deprecated.html)

