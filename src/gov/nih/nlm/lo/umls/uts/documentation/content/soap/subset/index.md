title=Retrieving UMLS Subset Information from UTS SOAP API
date=2015-08-17
updated=2015-08-17
type=page
status=published
navorder=8
~~~~~~

Interface | Method | Use Case | Object or Data type Returned 
-- | -- | -- | --
**UtsWsContentController**||||
 |[getSubsets](#getsubsets)|Retrieve information about all subsets in the UMLS|ArrayList\<SubsetDTO\>
 |[getSubset](#getsubset)|Retrieve information about one subset in the UMLS|SubsetDTO
 |[getSubsetSourceConceptMembers](#getsubsetsourceconceptmembers)|Retrieve (and perhaps store locally) all source concepts that belong to a known subset|ArrayList\<SourceConceptSubsetMemberDTO\>
 
**Each of these examples below requires an instance of the [UtsWsContentController](/soap/installation/interface-setup.html#utswscontentcontroller), [UtsWsMetadataController](/soap/installation/interface-setup.html#utswsmetadatacontroller) and [UtsWsSecurityController](/soap/installation/interface-setup.html#utswssecuritycontroller) interfaces**.


### getSubsets

**Method Signature:** ```getSubsets(String ticket,String version,PSF psf)```

#### Sample Input (Java):

~~~~java

    int pageNum = 1;
    String currentUmlsRelease = utsMetadataService.getCurrentUMLSVersion(ticket);
    List<SubsetDTO> subsets = new ArrayList<SubsetDTO>();

        do {
        //page through all the references to subsets in the UMLS
           myPsf.setPageNum(pageNum);
           subsets = utsContentService.getSubsets(ticket, currentUmlsRelease, myPsf);
           for (SubsetDTO subset:subsets) {
        	
        	  String ui = subset.getUi();
        	  String sourceUi = subset.getSourceUi();
        	  String name = subset.getName();
        	  int sourceConceptCount = subset.getSourceConceptMemberCount();
        	  int atomCount = subset.getAtomMemberCount();
        	  System.out.println(ui+"|"+sourceUi+"|"+name+"|"+atomCount+"|"+sourceConceptCount);
            }
            
        pageNum++;
        } while(subsets.size() > 0);

~~~~


#### Sample Output:

~~~~text
...
Ui|sourceUi|name|atomCount|sourceConceptCount
C4018850|6011000124106|ICD-10-CM complex map reference set|0|66488
C3714465|900000000000527005|SAME AS association reference set|0|47641
C3714470|900000000000526001|REPLACED BY association reference set|0|9813
C3645571|900000000000508004|GB English|1221637|0
C3645571|900000000000508004|GB English|1221637|0
C3693266|900000000000526001|REPLACED BY association reference set|0|0
C3693268|900000000000524003|MOVED TO association reference set|0|17001
C3669481|332501000009101|VTSL Veterinary Preferences|89374|0
C3693269|900000000000523009|POSSIBLY EQUIVALENT TO association reference set|0|18034
C3693271|900000000000489007|Concept inactivation indicator reference set|0|0
C3693270|900000000000490003|Description inactivation indicator reference set|0|0
C3693267|900000000000525002|MOVED FROM association reference set|0|0
C3693265|900000000000527005|SAME AS association reference set|0|0
~~~~


### getSubset

**Method Signature:** ```getSubset(String ticket,String version,String subsetId)```

#### Sample Input (Java):

~~~~java
String currentUmlsRelease = utsMetadataService.getCurrentUMLSVersion(ticket);
SubsetDTO subset = utsContentService.getSubset(ticket, currentUmlsRelease, "C4018850");
	    
String sourceUi = subset.getSourceUi();
String name = subset.getName();
int sourceConceptCount = subset.getSourceConceptMemberCount();
String description = subset.getDescription();
System.out.println(sourceUi+"|"+name+"|"+sourceConceptCount);
~~~~

#### Sample Output:

~~~~text
6011000124106|ICD-10-CM complex map reference set|66488
~~~~

### getSubsetSourceConceptMembers

**Method Signature:** ```getSubsetSourceConceptMembers(String ticket,String version,String subsetId, PSF psf)```


#### Sample Input (Java):

~~~~text
String currentUmlsRelease = utsMetadataService.getCurrentUMLSVersion(ticketClient.getSingleUseTicket(tgt));
List<SourceConceptSubsetMemberDTO> sctSubsetMembers = new ArrayList<SourceConceptSubsetMemberDTO>();
int pageNum = 1;
Psf myPsf = new Psf();
        	
    do {
        myPsf.setPageNum(pageNum);
        System.out.println("Fetching page "+ pageNum);
        //here we ask for the identifier for the SNOMED CT -> ICD10-CM refset, and retrieve the members and subset member attributes
        sctSubsetMembers = utsContentService.getSubsetSourceConceptMembers(ticket, currentUmlsRelease,"C4018850", myPsf);  

          for(SourceConceptSubsetMemberDTO sctSubsetMember:sctSubsetMembers) {
        	    
            //create a second psf object to handle calls to subset member attributes
            Psf psf2 = new Psf();
            String scui = sctSubsetMember.getSourceConcept().getUi();
            String subsetMemberId = sctSubsetMember.getUi();
            String name = sctSubsetMember.getSourceConcept().getDefaultPreferredName();
            System.out.println(scui+"|"+name);
            List<AttributeDTO> subsetMemberAttributes = utsContentService.getSubsetMemberAttributes(ticket, currentUmlsRelease, subsetMemberId, psf2);
        		    
        	for (AttributeDTO subsetMemberAttribute:subsetMemberAttributes){
        				
        	    String satui = subsetMemberAttribute.getSourceUi();
        	    String atn = subsetMemberAttribute.getName();
        	    String atv = subsetMemberAttribute.getValue();

                    System.out.println(    satui+"|"+atn+"|"+atv);
        	   }
        			
           }
           pageNum++;
        	
        }
        while(sctSubsetMembers.size() > 0);
~~~~

#### Sample Output:

~~~~text
92843003|Congenital abnormal fusion of carpal bone
6fffc599-d4a2-591b-bd70-f2c731df6110|CORRELATIONID|447561005
39b5ce33-e881-5cd9-bf5c-ca332236c51b|CORRELATIONID|447561005
6fffc599-d4a2-591b-bd70-f2c731df6110|MAPADVICE|ALWAYS Q79.8
39b5ce33-e881-5cd9-bf5c-ca332236c51b|MAPADVICE|IF CARPAL SYNOSTOSIS CHOOSE Q74.0 &#x7C; MAP OF SOURCE CONCEPT IS CONTEXT DEPENDENT
6fffc599-d4a2-591b-bd70-f2c731df6110|MAPCATEGORYID|447637006
39b5ce33-e881-5cd9-bf5c-ca332236c51b|MAPCATEGORYID|447639009
39b5ce33-e881-5cd9-bf5c-ca332236c51b|MAPGROUP|1
6fffc599-d4a2-591b-bd70-f2c731df6110|MAPGROUP|1
39b5ce33-e881-5cd9-bf5c-ca332236c51b|MAPPRIORITY|1
6fffc599-d4a2-591b-bd70-f2c731df6110|MAPPRIORITY|2
6fffc599-d4a2-591b-bd70-f2c731df6110|MAPRULE|OTHERWISE TRUE
39b5ce33-e881-5cd9-bf5c-ca332236c51b|MAPRULE|IFA 253930002 &#x7C; Carpal synostosis (disorder) &#x7C;
39b5ce33-e881-5cd9-bf5c-ca332236c51b|MAPTARGET|Q74.0
6fffc599-d4a2-591b-bd70-f2c731df6110|MAPTARGET|Q79.8
~~~~

