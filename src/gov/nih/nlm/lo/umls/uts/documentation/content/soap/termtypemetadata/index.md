title=Term Type Metadata
date=2015-08-24
updated=2015-08-24
type=page
status=published
navorder=4
~~~~~~



**Method: **getTermType(String ticket,String version,String termType)

**Returns:**TermTypeDTO

**Use Case:** Given a UMLS release and a term type abbreviation (TTY), this call returns the expanded form of the term type, the abbreviation, and the obsolete field.

#### Sample Input (Java):

~~~~
myTermTyp = utsMetadataService.getTermType(ticket, umlsRelease, "MH");
 String expandedForm = myTermTyp.getExpandedForm();
 String abbreviation = myTermTyp.getAbbreviation();
~~~~

#### Sample Input (C♯):

~~~~
Metadata.termTypeDTO myTermType =utsMetadataService.getTermType(singleUseTicket, "2012AB", "MH");
 string expandedForm = myTermType.expandedForm;
 string abbreviation = myTermType.abbreviation;
~~~~

#### Sample Output:

~~~~  
   ExpandedForm:Main heading
   Abbreviation:MH
~~~~
>


**Method: **getAllTermTypes(String ticket,String version)

**Returns:**ArrayList<TermTypeDTO>

**Use Case:** Given a UMLS release, this call returns all the valid term types for that release. The details of each returned term type include its expanded form, abbreviation, and the obsolete field.


#### Sample Input (Java):

~~~~
myarrTermTyp = utsMetadataService.getAllTermTypes(ticket, umlsRelease);
 for (int i = 0; i < myarrTermTyp.size(); i++) {
 TermTypeDTO myTermTypDTO = myarrTermTyp.get(i);
 String expandedForm = myTermTypDTO.getExpandedForm();
 String abbreviation = myTermTypDTO.getAbbreviation();
 }
~~~~

#### Sample Input (C♯):

~~~~
Metadata.termTypeDTO[] myArrayTermTypeDTO = utsMetadataService.getAllTermTypes(singleUseTicket, "2012AB");
 for (int i = 0; i < myArrayTermTypeDTO.Length; i++) {
 Metadata.termTypeDTO myTermTypeDTO = myArrayTermTypeDTO[i];
 string expandedForm = myTermTypeDTO.expandedForm;
 string abbreviation = myTermTypeDTO.abbreviation;
 }
~~~~

#### Sample Output:

   Expanded Form   | Abbreviation  
   --- | ---
   Attribute type abbreviation    |AA    
    Abbreviation in any source vocabulary   | AB        
   Activities  |  AC        
Acronym   | ACR   
Adjective |   AD    
 Short form of modifier |  AM      
 Attribute type synonym    | AS       
  Attribute type    | AT         
   Authority name    | AUN    
  Fully-specified drug brand name that can be prescribed  |  BD     
   Fully-specified drug brand name that can not be prescribed  | BN                                                   |
 Branded Drug Delivery Device    |  BPCK                                      
