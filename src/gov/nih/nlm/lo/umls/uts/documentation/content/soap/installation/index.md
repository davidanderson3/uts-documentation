title=UMLS SOAP API Installation
date=2015-08-13
updated=2015-08-13
type=page
status=unpublished
navorder=1
~~~~~~


#### Getting Started

Installation of UTS API 2.0 involves running wsimport commands to parse the appropriate WSDLs and generate the needed JAX-WS files.

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

####Here are steps on how to create the reference variables for each web service:

[Content](../installation/content.html)
[Metadata](../installation/metadata.html)
[Semantic Network](../installation/semanticnetwork.html)
[Concept History](../installation/concepthistory.html)
[Finder](../installation/finder.html)
[Paging, Sorting, Filtering](../installation/psf.html)
>
