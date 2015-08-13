title=UTS Soap API Installation
date=2015-08-13
updated=2015-08-13
type=page
status=unpublished
navorder=1
~~~~~~


#### Getting Started

Installation of UTS API 2.0 involves running wsimport commands to parse
the appropriate WSDLs and generate the needed JAX-WS files.

Before you install the UTS API 2.0:

-   JDK 6 or greater must be installed on your machine
-   Your JAVA\_HOME variable must point to your JDK installation

Installation of the UTS API 2.0:

-   Create a folder in which you will compile the WSDLs
-   Within your new folder, run the wsimport statements
-   The example below demonstrates this in a UNIX environment


~~~~
mkdir utsapi2_0
cd utsapi2_0
wsimport -p gov.nih.nlm.uts.webservice.content -keep https://uts-ws.nlm.nih.gov/services/nwsContent?wsdl
wsimport -p gov.nih.nlm.uts.webservice.security -keep https://uts-ws.nlm.nih.gov/services/nwsSecurity?wsdl
wsimport -p gov.nih.nlm.uts.webservice.metadata -keep https://uts-ws.nlm.nih.gov/services/nwsMetadata?wsdl
wsimport -p gov.nih.nlm.uts.webservice.finder -keep https://uts-ws.nlm.nih.gov/services/nwsFinder?wsdl
wsimport -p gov.nih.nlm.uts.webservice.history -keep https://uts-ws.nlm.nih.gov/services/nwsHistory?wsdl
wsimport -p gov.nih.nlm.uts.webservice.semnet -keep https://uts-ws.nlm.nih.gov/services/nwsSemanticNetwork?wsdl
~~~~


After running each wsimport command, you should have six new folders.
Each new wsimport-generated folder has a name corresponding to the target packages in the wsimport commands.

The target packages contain all of the classes needed for using the UTS API 2.0.

You will need to import the packages that you just created into any client you create, as well as any additional packages needed by your application.

~~~~
import gov.nih.nlm.uts.webservice.content.*;
import gov.nih.nlm.uts.webservice.security.*;
import gov.nih.nlm.uts.webservice.metaData.*;
import gov.nih.nlm.uts.webservice.finder.*;
import gov.nih.nlm.uts.webservice.history.*;
import gov.nih.nlm.uts.webservice.semNet.*;
~~~~



#### Authentication

In general, your application will follow this sequence when making calls to the API:

1.  Obtain a Proxy Grant Ticket using the getProxyGrantTicket method described below. This is good for 8 hours and is needed for step #2
2.  Generate a Single Use Ticket (using the Proxy Grant Ticket and the string "http://umlsks.nlm.nih.gov" as parameters) with the getProxyTicket method described below.
3.  Make a call to the API, passing the Single Use Ticket as one of the parameters.


The UTS API 2.0 uses two types of "tickets" to authenticate users and calls: 

-   **Proxy Grant Ticket** (valid for 8 hours) This kind of ticket validates your UTS username and password. **It is not necessary to obtain a new Proxy Grant Ticket each time you make a call to the API. However, it is necessary to use the proxy grant ticket each time you make a call to the API to request a single-use ticket.** A Proxy Grant Ticket could be considered "the ticket that gets you a ticket."
-   **"Single-Use" Ticket** - This ticket expires after an individual call is completed. Therefore, each time you make a call to the API, you must request a new Proxy Ticket.

Please see [this very simple client example](../soap/simpleClient.html) that demonstrates using the Proxy Grant/Single-Use Tickets


##### Proxy Grant Ticket
~~~~
private String username = "foofoo";
private String password = "B@rB@z_1";

//initialize the security service
 private UtsWsSecurityController securityService = (new UtsWsSecurityControllerImplService()).getUtsWsSecurityControllerImplPort();
 private String ticketGrantingTicket = securityService.getProxyGrantTicket(username, password);
//use the ticketGrantingTicket to generate a Single Use Ticket with each call
~~~~


##### Single Use Ticket
~~~~
// set the service name, perhaps somewhere else in your code\
private String serviceName = "http://umlsks.nlm.nih.gov";

/*Do not be confused by the "serviceName" variable value above, "https://umlsks.nlm.nih.gov"
 This is simply a generic service name to access Terminology Services APIs at the National Library of Medicine, and has nothing to do with the legacy UMLSKS Knowledge Sources Server. */
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