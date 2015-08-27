title=UMLS Version Metadata
date=2015-08-21
updated=2015-08-21
type=page
status=unpublished
category=Metadata
navorder=4
~~~~~~


**Method: **getCurrentUMLSVersion(String ticket)

**Returns:** String

**Use Case:** This method allows the user to retrieve the current UMLS release, given a single use ticket.

#### Sample Input (Java):

~~~~
myarrStringMetadata = utsMetadataService.getCurrentUMLSVersion(ticket);
 System.out.println(myarrStringMetadata);
~~~~

#### Sample Input (C#):

~~~~
string myStringMetadata = utsMetadataService.getCurrentUMLSVersion(singleUseTicket);
~~~~

#### Sample Output:

~~~~
  The current UMLS Version is:  2012AB
~~~~
>

**Method: **getAllUMLSVersions(String ticket)

**Returns:** String

**Use Case:** This method allows the user to retrieve a list of all UMLS releases available, given a single use ticket.


#### Sample Input (Java):

~~~~
myarrStringMetadata = utsMetadataService.getAllUMLSVersions(ticket);
 System.out.println(myarrStringMetadata);
~~~~

#### Sample Input (C#):

~~~~
string myStringMetadata =utsMetadataService.getAllUMLSVersions(singleUseTicket);
~~~~

#### Sample Output:

~~~~
  All available UMLS Versions are:
   2012AB
   2012AA
   2011AA
   2011AB
   2010AB
   2010AA
   2009AB
   2009AA
   2008AB
   2008AA
~~~~