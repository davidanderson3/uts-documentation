title=Retrieving UMLS Content View Information from UMLS SOAP API
date=2015-08-17
updated=2015-08-17
type=page
status=published
navorder=7
~~~~~~

Interface | Method | Use Case | Object or Data type Returned 
-- | -- | -- | --
**UtsWsContentController**||||
 |[getContentViews](#getcontentviews)|Retrieve a list of all content views available in the UMLS|ArrayList\<ContentViewDTO\>
 |[getContentView](#getcontentview)|Retrieve information about a particular content view given its identifier|ContentViewDTO
 |[getContentViewSourceConceptMembers](#getcontentviewsourceconceptmembers)|Retrieve all source concepts (and perhaps store them locally) that belong to a particular content view|ArrayList\<SourceConceptContentViewMemberDTO\>
 |[getContentViewAtomMembers](#getcontentviewatommembers)|Retrieve all atoms (and perhaps store them locally) that belong to a particular content view|ArrayList\<AtomContentViewMemberDTO\>

**Each of these examples below requires an instance of the [UtsWsContentController](/soap/installation/interface-setup.html#utswscontentcontroller), [UtsWsMetadataController](/soap/installation/interface-setup.html#utswsmetadatacontroller) and [UtsWsSecurityController](/soap/installation/interface-setup.html#utswssecuritycontroller) interfaces**.

### getContentViews
 
**Method Signature:** ```getContentViews(String ticket,String version,PSF psf)```

#### Sample Input (Java):

~~~~
List<ContentViewDTO> contentViews = new ArrayList<ContentViewDTO>();
String currentUmlsRelease = utsMetadataService.getCurrentUMLSVersion(ticket);
contentViews = utsContentService.getContentViews(ticket, currentUmlsRelease, myPsf);
		
    for (ContentViewDTO contentView:contentViews) {
			
	String ui = contentView.getUi();
	String name = contentView.getName();
	int numberOfScuis = contentView.getSourceConceptMemberCount();
	int numberOfAtoms = contentView.getAtomMemberCount();
	String algorithm = contentView.getAlgorithm();

    }
~~~~

#### Sample Output

~~~~text
ui:C1700357
name:MetaMap NLP View
# sourceConcepts: 0
# atoms: 4231900
algorithm: This content view is built from mrconso.filtered.strict (a subset of RRF MRCONSO) and converted into an AUI list based on 2015AA. This view is not algorithmically generated during Metathesaurus construction.
--------
ui:C1964027
name:UMLS enhanced VA/KP Problem List Subset of SNOMED (Level 0+SNOMED)
# sourceConcepts: 0
# atoms: 212274
algorithm: This content view includes UMLS atoms sharing a UMLS CUI with a SNOMEDCT_US atom having a SCUI value on the VA/KP Problem List Subset which is marked active.  Only atoms from the SNOMED family and level 0 sources with LAT=ENG and SUPPRESS=N are included.
--------
ui:C1964028
name:UMLS enhanced VA/KP Problem List Subset of SNOMED (Level 0+SNOMED+MDR)
# sourceConcepts: 0
# atoms: 234633
algorithm: This content view includes UMLS atoms sharing a UMLS CUI with a SNOMEDCT atom having a SCUI value on the VA/KP Problem List Subset which is marked active.  Only atoms from the SNOMED family, MDR and level 0 sources with LAT=ENG and SUPPRESS=N are included.
--------
ui:C2711988
name:CORE Problem List Subset of SNOMED CT
# sourceConcepts: 6347
# atoms: 0
algorithm: The creation of this content view is based on the list of SNOMED CT concept IDs in the latest release of the CORE Problem List Subset of SNOMED CT, excluding those that are retired from the Subset. It contains all atoms linked to that SNOMED CT concept with LAT=ENG and SUPPRESS=N.
--------
ui:C3503753
name:Prescribable List Subset of RXNORM
# sourceConcepts: 0
# atoms: 220464
algorithm: The creation of this content view is based on the set of RXNORM concepts marked as prescribable in the RXNCONSO.RRF file.
--------
ui:C3812142
name:SNOMEDCT US Extension Subset
# sourceConcepts: 4627
# atoms: 0
algorithm: AUIs with module_id of SNOMEDCT US Extension, '731000124108'
--------
~~~~

### getContentView

**Method Signature:** ```getContentView(String ticket,String version,String conceptId)```

#### Sample Input (Java):

~~~~java
String currentUmlsRelease = utsMetadataService.getCurrentUMLSVersion(ticket);
ContentViewDTO myContentView = new ContentViewDTO();
myContentView = utsContentService.getContentView(ticket, currentUmlsRelease, "C2711988");
String name = myContentView.getName();
int numberOfScuis = myContentView.getSourceConceptMemberCount();
String algorithm = myContentView.getAlgorithm();
String contributorurl = myContentView.getContributorURL();
~~~~


#### Sample Output:

~~~~text
ui:C2711988
name:CORE Problem List Subset of SNOMED CT
# sourceConcepts: 6347
# atoms: 0
algorithm: The creation of this content view is based on the list of SNOMED CT concept IDs in the latest release of the CORE Problem List Subset of SNOMED CT, excluding those that are retired from the Subset. It contains all atoms linked to that SNOMED CT concept with LAT=ENG and SUPPRESS=N.
url: http://www.nlm.nih.gov/research/umls/Snomed/core_subset.html
--------        
~~~~


### getContentViewAtomMembers

**Method Signature:** ```getContentViewAtomMembers(String ticket,String version,String conceptId,PSF psf)```

#### Sample Input (Java):

~~~~java
//retrieve members MetaMap NLP View content view
int pageNum = 1;
List<AtomContentViewMemberDTO> members = new ArrayList<AtomContentViewMemberDTO>();
String currentUmlsRelease = utsMetadataService.getCurrentUMLSVersion(ticket);
		
    do {
	myPsf.setPageNum(pageNum);
	members = utsContentService.getContentViewAtomMembers(ticket, currentUmlsRelease, "C1700357", myPsf);
	for (AtomContentViewMemberDTO member:members) {
            	
	    String ui = member.getAtom().getUi();
	    String name = member.getAtom().getTermString().getDefaultPreferredName();
            String tty = member.getAtom().getTermType();
            String rsab = member.getAtom().getRootSource();
            System.out.println(ui+"|"+tty+"|"+rsab+"|"+name);
            	
        }pageNum++;
			 
    } while(members.size() > 0);
~~~~


#### Sample Output:

~~~~text
...
A23780681|PTCS|OMIM|Chronic thrombotic microangiopathy
A23789255|PTCS|OMIM|Skin blistering, intermittent
A23786614|PTCS|OMIM|Residual slightly atrophic scarring
A23782656|PTCS|OMIM|Acanthosis, mild
A23788588|PTCS|OMIM|Basement membrane keratinocyte disruption within lower epidermis
A23782658|PTCS|OMIM|Aggregated intermediate filaments
A23786615|PTCS|OMIM|Increased number of perinuclear vesicles
A23780012|PTCS|OMIM|Central apnea, episodic
A23787281|PTCS|OMIM|Abnormal lipid peak on brain MRS
A23784679|PTCS|OMIM|Dystonic posturing of the upper limb
A23781991|PTCS|OMIM|Laryngeal tremor
A23787282|PTCS|OMIM|Arthrogryposis of the small joints
A23780014|PT|OMIM|EPISODIC PAIN SYNDROME, FAMILIAL, 1
A23788592|ACR|OMIM|FEPS1
A23788593|PTCS|OMIM|Pain, episodic
A21307920|SCN|NCBI|bacterium ENA08R
A21307921|SCN|NCBI|Bacillus sp. ENA08F
A21389116|SCN|NCBI|Luetzelburgia sp. DC-2012b
A21372830|SCN|NCBI|Dyckia distachya
A21324097|SCN|NCBI|Synodus bondi
A21340193|SCN|NCBI|Ypthima similis
A21356392|SCN|NCBI|Pseudovidalia
A21275800|SCN|NCBI|Pseudovidalia furialis
...
~~~~

### getContentViewSourceConceptMembers

**Method Signature:** ```getContentViewSourceConceptMembers(String ticket,String version,String conceptId,PSF psf)```

#### Sample Input (Java):

~~~~

//retrieve members of the SNOMED CT CORE Problem List content view, along with attributes of each member
int pageNum = 1;
List<SourceConceptContentViewMemberDTO> members = new ArrayList<SourceConceptContentViewMemberDTO>();
String currentUmlsRelease = utsMetadataService.getCurrentUMLSVersion(ticket);
		
    do {
	myPsf.setPageNum(pageNum);
	members = utsContentService.getContentViewSourceConceptMembers(ticket, currentUmlsRelease, "C2711988", myPsf);
	for (SourceConceptContentViewMemberDTO member:members) {
            	
	    String ui = member.getSourceConcept().getUi();
	    String name = member.getSourceConcept().getDefaultPreferredName();
            int attributeCount = member.getAttributeCount();
                
            System.out.println(ui+"|"+name);
            //check for attribute of each content view member
            if (attributeCount > 0) {
                  
            Psf psf2 = new Psf();
            //only include IS_RETIRED_FROM_SUBSET attributes
            psf2.getIncludedAttributeNames().add("IS_RETIRED_FROM_SUBSET");
            List<AttributeDTO> attributes = utsContentService.getContentViewMemberAttributes(ticket, currentUmlsRelease, member.getUi(), psf2);
                  
            for (AttributeDTO attribute:attributes) {
            		
            	System.out.println("---"+attribute.getName()+"|"+attribute.getValue());
            	  
            }
            	
        }pageNum++;
			 
    } while(members.size() > 0);
~~~~

#### Sample Output:

~~~~text
...
18165001|Jaundice
---IS_RETIRED_FROM_SUBSET|False
36222008|Carcinoid heart disease
---IS_RETIRED_FROM_SUBSET|False
189607006|Carcinoid tumor - morphology
---IS_RETIRED_FROM_SUBSET|True
443492008|Carcinoid tumor
---IS_RETIRED_FROM_SUBSET|False
60853003|Disorder of magnesium metabolism
---IS_RETIRED_FROM_SUBSET|False
165816005|HIV positive
---IS_RETIRED_FROM_SUBSET|False
54319003|Disruptive behavior disorder
---IS_RETIRED_FROM_SUBSET|False
308546005|Dissection of aorta
---IS_RETIRED_FROM_SUBSET|False
74390002|Wolff-Parkinson-White pattern
---IS_RETIRED_FROM_SUBSET|False
76844004|Local infection of wound
---IS_RETIRED_FROM_SUBSET|False
312608009|Laceration - injury
---IS_RETIRED_FROM_SUBSET|False
7484005|Double outlet right ventricle
---IS_RETIRED_FROM_SUBSET|False
...
~~~~
