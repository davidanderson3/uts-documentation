title=Retrieving parents and children from the UMLS SOAP API
date=2015-10-22
updated=2015-10-22
type=page
status=published
navorder=3
~~~~~~

Interface | Method | Use Case | Object or Data type Returned
-- | -- | -- | --
**UtsWsContentController**||||
 |[getSourceConceptTreePositionChildren](#getsourceconcepttreepositionchildren)|Retrieve immediate children for a known source-asserted concept |ArrayList\<SourceAtomClusterTreePositionDTO\>
 |[getSourceConceptTreePositionPathsToRoot](#getsourceconceptreepositionpathstoroot)|Retrieve ancestors for a known source-asserted concept | ArrayList\<SourceAtomClusterTreePositionPathDTO\>, ArrayList\<SourceAtomClusterTreePositionDTO\>
 |[getSourceConceptTreePositionSiblings](#getsourceconcepttreepositionsiblings)|Retrieve siblings for a known source-asserted concept | ArrayList\<SourceAtomClusterTreePositionDTO\>
 |[getSourceDescriptorTreePositionChildren](#getsourcedescriptortreepositionchildren)|Retrieve immediate children for a known source-asserted descriptor |ArrayList\<SourceAtomClusterTreePositionDTO\>
 |[getSourceDescriptorTreePositionPathsToRoot](#getsourcedescriptortreepositionpathstoroot)|Retrieve ancestors for a known source-asserted descriptor | ArrayList\<SourceAtomClusterTreePositionPathDTO\>, ArrayList\<SourceAtomClusterTreePositionDTO\>
 |[getSourceDescriptorTreePositionSiblings](#getsourcedescriptortreepositionsiblings)|Retrieve siblings for a known source-asserted descriptor | ArrayList\<SourceAtomClusterTreePositionDTO\>

**Each of these examples below requires an instance of the [UtsWsContentController](/soap/installation/interface-setup.html#utswscontentcontroller), [UtsWsMetadataController](/soap/installation/interface-setup.html#utswsmetadatacontroller) and [UtsWsSecurityController](/soap/installation/interface-setup.html#utswssecuritycontroller) interfaces**.

When obtaining parents or children via the SOAP API, you must first obtain the tree position(s) of the source-asserted identifier in question, as detailed in the
code samples below.


### getSourceConceptTreePositionChildren

**Method Signature**: ``` getSourceConceptTreePositionChildren(String ticket, String version,String scuiPosId,PSF psf)```

~~~~java

List<SourceAtomClusterTreePositionDTO> treePositions = new ArrayList<SourceAtomClusterTreePositionDTO>();
String currentUmlsRelease = utsMetadataService.getCurrentUMLSVersion(ticket);
//retrieve children of SNOMED CT concept 362969004, "Disorder of endocrine system"
treePositions = utsContentService
	.getSourceConceptTreePositions(ticket,currentUmlsRelease,"362969004","SNOMEDCT_US",myPsf);
		
for (SourceAtomClusterTreePositionDTO treePosition:treePositions) {
			
    List<SourceAtomClusterTreePositionDTO> children = new ArrayList<SourceAtomClusterTreePositionDTO>();
    int pageNum = 1;
    //some codes contain more than 25 children, so we page through all the results		
	do{
	  myPsf.setPageNum(pageNum);
	  children = utsContentService
	    .getSourceConceptTreePositionChildren(ticket,currentUmlsRelease, treePosition.getUi(), myPsf);
		
		for (SourceAtomClusterTreePositionDTO child:children) {
		    	
		    String ui = child.getCluster().getUi();
		    String name = child.getCluster().getDefaultPreferredName();
		    System.out.println(ui +"|" + name);
		    	
		    	   
		}pageNum++;
		        
	}while(children.size() > 0);
		      
}

~~~~

#### Sample Output

~~~~text
sct concept|name
73211009|Diabetes mellitus
81682002|Functional disease of the CNS with neuroendocrine disturbance
363104002|Hereditary disorder of endocrine system
79268002|POEMS syndrome
127009005|Disorder of endocrine receptor
54539003|Endocrine alopecia
363128000|Fetal endocrine disorder
26572003|Polyglandular dysfunction AND/OR related disorders
129632001|General adaptation syndrome
128470003|Pineal gland disorder
253030004|Glomus vagale tumor
363103008|Endocrine system complication of procedure
237822008|Autoimmune endocrine disease
253031000|Glomus tympanicum tumor
7651000119100|Mineralocorticoid deficiency
17346000|Disorder of endocrine pancreas
237597000|Disorder of glucose regulation
284000008|Endocrine injury
22063003|Isolated deficiency of hormone other than HGH
237594007|Abnormality of serotonin secretion
387927001|Neoplasm of endocrine system
14304000|Disorder of thyroid gland
127345001|Disorder of endocrine gonad
73132005|Disorder of parathyroid gland
286566006|Foreign body of endocrine structure
442498002|Endocrine axis dysfunction
4184009|Congenital anomaly of endocrine gland
30171000|Disorder of adrenal gland
237658004|Pseudohypoparathyroidism and pseudopseudohypoparathyroidism
312426003|Endocrine infection
399244003|Disorder of pituitary gland

~~~~

### getSourceConceptTreePositionPathsToRoot

**Method Signature**: ```getSourceConceptTreePositionPathsToRoot(String ticket, String version,String scuiPosId,PSF psf)```

### getSourceDescriptorTreePositionPathsToRoot

**Method Signature**: ```getSourceDescriptorTreePositionPathsToRoot(String ticket, String version,String scuiPosId,PSF psf)```

~~~~java

List<SourceAtomClusterTreePositionDTO> treePositions = new ArrayList<SourceAtomClusterTreePositionDTO>();
String currentUmlsRelease = utsMetadataService.getCurrentUMLSVersion(ticket);
treePositions = utsContentService
		.getSourceDescriptorTreePositions(ticket,currentUmlsRelease,"O24.4",rsab,myPsf);
		
    for (SourceAtomClusterTreePositionDTO treePosition:treePositions) {
			
	List<SourceAtomClusterTreePositionPathDTO> ancestors = new ArrayList<SourceAtomClusterTreePositionPathDTO>();
	ancestors = utsContentService
                    .getSourceDescriptorTreePositionPathsToRoot(ticket,currentUmlsRelease, treePosition.getUi(), myPsf);
			        
		    for (SourceAtomClusterTreePositionPathDTO parent:ancestors) {
		    	
		    	List<SourceAtomClusterTreePositionDTO> parentTreePositions = new ArrayList<SourceAtomClusterTreePositionDTO>();
		    	parentTreePositions = parent.getTreePositions();
                        //we reverse the array list to sort the collection from the tree-top downwards
		    	Collections.reverse(parentTreePositions);
		    	for (SourceAtomClusterTreePositionDTO parentTreePosition:parentTreePositions) {
		    		
		    	    String ui = parentTreePosition.getCluster().getSourceUi();
		    	    String name = parentTreePosition.getCluster().getDefaultPreferredName();
		    	    System.out.println(ui +"|" + name );
		    	}
		    }
    }

~~~~


#### Sample Output

~~~~text
ICD-10-CM|ICD-10-CM TABULAR LIST of DISEASES and INJURIES
O00-O9A|Pregnancy, childbirth and the puerperium (O00-O9A)
O20-O29|Other maternal disorders predominantly related to pregnancy (O20-O29)
O24|Diabetes mellitus in pregnancy, childbirth, and the puerperium
~~~~

### getSourceConceptTreePositionSiblings

**Method Signature**: ``` getSourceConceptTreePositionChildren(String ticket, String version,String scuiPosId,PSF psf)```

~~~~java
List<SourceAtomClusterTreePositionDTO> treePositions = new ArrayList<SourceAtomClusterTreePositionDTO>();
String currentUmlsRelease = utsMetadataService.getCurrentUMLSVersion(ticket);
treePositions = utsContentService
    .getSourceConceptTreePositions(ticket,currentUmlsRelease,identifier,rsab,myPsf);
		
	for (SourceAtomClusterTreePositionDTO treePosition:treePositions) {
	  
	  List<SourceAtomClusterTreePositionDTO> siblings = new ArrayList<SourceAtomClusterTreePositionDTO>();
          int pageNum = 1;
	    do {
	    myPsf.setPageNum(pageNum);
            //retrieve siblings of SNOMED CT concept 362969004, "Disorder of endocrine system"
	    siblings = utsContentService
		       .getSourceConceptTreePositionSiblings(ticket,currentUmlsRelease, treePosition.getUi(), myPsf);
					        
		for (SourceAtomClusterTreePositionDTO sibling:siblings) {
	
		    String ui = sibling.getCluster().getSourceUi();
		    String name = sibling.getCluster().getDefaultPreferredName();
		    System.out.println(ui +"|" + name );
		}
			  
		pageNum++;
	    }while(siblings.size() > 0);
		    
        }
~~~~

#### Sample Output

~~~~text
79604008|Disorder of breast
363171009|Inflammation of specific body systems
402816008|Squamous cell carcinoma of anogenital area
414027002|Disorder of hematopoietic structure
118940003|Disorder of nervous system
414030009|Disorder of immune structure
188498009|Lymphosarcoma
928000|Disorder of musculoskeletal system
42030000|Disorder of the genitourinary system
280129003|Disorder of soft tissue of thoracic cavity
363296001|Sequelae of disorders classified by disorder-system
400072006|Fixed drug reaction
240659008|Chagas' mega disease
95351003|Disorder of mucous membrane
95194004|Nodular lymphoma of extranodal AND/OR solid organ site
49601007|Disorder of cardiovascular system
128598002|Disorder of integument
362966006|Disorder of auditory system
128127008|Visual system disorder
402811003|Squamous neoplasm of surface epithelium
283985007|Lymphoreticular injury
417237009|Blister
363137000|Hereditary disorder by system
428100006|Malignant neoplasm of thoracic cavity structure
362971004|Disorder of lymphatic system
240844004|Loa loa lymphadenopathy
53619000|Disorder of digestive system
284006002|Injury of thoracic cavity
427617000|Aphthous ulceration of skin and/or mucous membrane
404147001|Follicular center B-cell lymphoma (nodal/systemic with skin involvement)
49483002|Disorder of mediastinum
255142009|Carcinoma in situ of respiratory and intrathoracic organ
38292009|Red blood cell disorder
50043002|Disorder of respiratory system
~~~~

### getSourceDescriptorTreePositionChildren

**Method Signature**: ``` getSourceDescriptorTreePositionChildren(String ticket, String version,String sduiPosId,PSF psf)```

~~~~java

List<SourceAtomClusterTreePositionDTO> treePositions = new ArrayList<SourceAtomClusterTreePositionDTO>();
String currentUmlsRelease = utsMetadataService.getCurrentUMLSVersion(ticket);
//retrieve children of ICD-10-CM code O24.4, 'Gestational Diabetes'
treePositions = utsContentService
	.getSourceDescriptorTreePositions(ticket,currentUmlsRelease,"O24.4","ICD10CM",myPsf);
		
for (SourceAtomClusterTreePositionDTO treePosition:treePositions) {
			
    List<SourceAtomClusterTreePositionDTO> children = new ArrayList<SourceAtomClusterTreePositionDTO>();
    int pageNum = 1;
    //some codes contain more than 25 children, so we page through all the results		
	do{
	  myPsf.setPageNum(pageNum);
	  children = utsContentService
	    .getSourceDescriptorTreePositionChildren(ticket,currentUmlsRelease, treePosition.getUi(), myPsf);
		
		for (SourceAtomClusterTreePositionDTO child:children) {
		    	
		    String ui = child.getCluster().getUi();
		    String name = child.getCluster().getDefaultPreferredName();
		    System.out.println(ui +"|" + name);
		    	
		    	   
		}pageNum++;
		        
	}while(children.size() > 0);
		      
}

~~~~

#### Sample Output

~~~~text
icd-10-cm code|name
O24.41|Gestational diabetes mellitus in pregnancy
O24.43|Gestational diabetes mellitus in the puerperium
O24.42|Gestational diabetes mellitus in childbirth
~~~~


### getSourceDescriptorTreePositionSiblings

**Method Signature**: ``` getSourceDescriptorTreePositionSiblings(String ticket, String version,String sduiPosId,PSF psf)```

~~~~java
List<SourceAtomClusterTreePositionDTO> treePositions = new ArrayList<SourceAtomClusterTreePositionDTO>();
String currentUmlsRelease = utsMetadataService.getCurrentUMLSVersion(ticket);
treePositions = utsContentService
    .getSourceDescriptorTreePositions(ticket,currentUmlsRelease,identifier,rsab,myPsf);
		
	for (SourceAtomClusterTreePositionDTO treePosition:treePositions) {
	  
	  List<SourceAtomClusterTreePositionDTO> siblings = new ArrayList<SourceAtomClusterTreePositionDTO>();
          int pageNum = 1;
	    do {
	    myPsf.setPageNum(pageNum);
            //retrieve siblings of ICD-10-CM concept O24.4, "Gestational Diabetes"
	    siblings = utsContentService
		       .getSourceDescriptorTreePositionSiblings(ticket,currentUmlsRelease, treePosition.getUi(), myPsf);
					        
		for (SourceAtomClusterTreePositionDTO sibling:siblings) {
	
		    String ui = sibling.getCluster().getSourceUi();
		    String name = sibling.getCluster().getDefaultPreferredName();
		    System.out.println(ui +"|" + name );
		}
			  
		pageNum++;
	    }while(siblings.size() > 0);
		    
        }
~~~~

#### Sample Output

~~~~text
icd-10-cm code | name
O24.0|Pre-existing diabetes mellitus, type 1, in pregnancy, childbirth and the puerperium
O24.8|Other pre-existing diabetes mellitus in pregnancy, childbirth, and the puerperium
O24.3|Unspecified pre-existing diabetes mellitus in pregnancy, childbirth and the puerperium
O24.9|Unspecified diabetes mellitus in pregnancy, childbirth and the puerperium
O24.1|Pre-existing diabetes mellitus, type 2, in pregnancy, childbirth and the puerperium
~~~~
