title=Installing the UMLS SOAP API with Maven
date=2015-12-08
date=2015-12-08
type=page
status=published
navorder=3
~~~~~~

You can install the UMLS SOAP API by using Maven by following the steps below.  The current version of the UMLS SOAP API is always discoverable on our public ftp server:
<ftp://ftp.nlm.nih.gov/nlmdata/tools_repo/public_html/gov/nih/nlm/umls/umls-uts-ws-client-classes/>

#####Step 1: Modify your settings.xml file to include the ftp server that NLM uses to distribute the maven artifact.
Your settings.xml file is normally located in the .m2 directory of the $HOME account of your machine.  (C:\Users\\<user\>\\.m2 on Windows, and ~/.m2 Linux or Macintosh).

~~~~.xml
<settings>
  <servers>
    <server>
      <id>FTP-SERVER</id>
      <username>anonymous</username>
      <password></password>
    </server> 
  </servers>
</settings>
~~~~

#####Step 2: Modify your pom.xml file - add or modify the following areas:

~~~~.xml
...
<properties>
    <umls.soap.api.version>1.3.0.RELEASE</umls.soap.api.version>
</properties>
...
<repositories>
...
  <repository>
    <id>FTP-SERVER</id>
    <url>ftp://ftp.nlm.nih.gov/nlmdata/tools_repo/public_html/</url>
  </repository>
</repositories>
...
<dependencies>
  <dependency>
     <groupId>gov.nih.nlm.umls</groupId>
     <artifactId>umls-uts-ws-client-classes</artifactId>
     <version>${umls.soap.api.version}</version>
  </dependency>
  <dependency>
     <groupId>org.apache.maven.wagon</groupId>
     <artifactId>wagon-ftp</artifactId>
     <version>2.10</version>      
  </dependency>
</dependencies>
<build>
    <extensions>
        <extension>
           <groupId>org.apache.maven.wagon</groupId>
           <artifactId>wagon-ftp</artifactId>
           <version>1.0-beta-5</version>
        </extension>
    </extensions>
</build>
...
~~~~

#####Step 3 - Complete the installation:
Install the API classes.  In Eclipse, for example, right click on your pom.xml file and click ```'Run As' -> 'Maven install'```
The UMLS SOAP API classes will download into your .m2/repository directory into a package named ```gov.nih.nlm.uts.webservice```.