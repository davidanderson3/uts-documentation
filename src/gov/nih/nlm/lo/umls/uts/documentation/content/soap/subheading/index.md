title=Subheading Metadata
date=2015-08-21
updated=2015-08-21
type=page
status=published
navorder=4
~~~~~~


**Method: **getSubheading(String ticket,String version,String subheading)

**Returns:** SubheadingDTO

**Use Case:** Given a UMLS release and a MeSH subheading abbreviation, this call returns the expanded form of the MeSH subheading name, together with the supplied MeSH subheading abbreviation.

#### Sample Input (Java):

~~~~
mySubheading = utsMetadataService.getSubheading(ticket, umlsRelease,"AE");
 String expandedForm = mySubheading.getExpandedForm();
 String abbreviation = mySubheading.getAbbreviation();
~~~~

#### Sample Input (C#):

~~~~
Metadata.subheadingDTO mySubheading =utsMetadataService.getSubheading(singleUseTicket, "2012AB", "AE");
 string expandedForm = mySubheading.expandedForm;
~~~~

#### Sample Output:

~~~~
  ExpandedForm:adverse effects
   Abbreviation:AE
~~~~
>

**Method: **getAllSubheadings(String ticket,String version)

**Returns:** ArrayList< SubheadingDTO>

**Use Case:** Given a UMLS release, this call returns all of the valid MeSH subheadings, their expanded forms and abbreviations, for the given release.


#### Sample Input (Java):

~~~~
myarrSubheading = utsMetadataService.getAllSubheadings(ticket,umlsRelease);
 for (int i = 0; i < myarrSubheading.size(); i++) {
 SubheadingDTO mySubheadingDTO = myarrSubheading.get(i);
 String expandedForm = mySubheadingDTO.getExpandedForm();
 String abbreviation = mySubheadingDTO.getAbbreviation();
 }
~~~~

#### Sample Input (C#):

~~~~
Metadata.subheadingDTO[] mySubheadings =utsMetadataService.getAllSubheadings(singleUseTicket, "2012AB");
 for (int i = 0; i < mySubheadings.Length; i++) {
 Metadata.subheadingDTO mySubheadingDTO = mySubheadings[i];
 string expandedForm = mySubheadingDTO.expandedForm;
 string abbreviation = mySubheadingDTO.abbreviation;
 }
~~~~

#### Sample Output:

~~~~
   ExpandedForm:No MeSH subheading (qualifier)
   Abbreviation:<>
   ExpandedForm:analogs & derivatives
   Abbreviation:AA
   ExpandedForm:abnormalities
   Abbreviation:AB
   ExpandedForm:administration & dosage
   Abbreviation:AD
   ExpandedForm:adverse effects
   Abbreviation:AE
   ExpandedForm:agonists
   Abbreviation:AG
   ExpandedForm:anatomy & histology
   Abbreviation:AH
   ExpandedForm:antagonists & inhibitors
   Abbreviation:AI
   ExpandedForm:analysis
   Abbreviation:AN
   ExpandedForm:biosynthesis
   Abbreviation:BI
   ExpandedForm:blood
   Abbreviation:BL
   ExpandedForm:blood supply
   Abbreviation:BS
   ExpandedForm:cerebrospinal fluid
   Abbreviation:CF
   ExpandedForm:chemistry
   Abbreviation:CH
   ExpandedForm:chemically induced
   Abbreviation:CI
~~~~
   