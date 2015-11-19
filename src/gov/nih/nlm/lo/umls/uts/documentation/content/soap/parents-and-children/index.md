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
 |[getSourceConceptTreePositionChildren](#getsourceconceptreepositionchildren)|Retrieve children for a known source-asserted concept. |ArrayList\<SourceAtomClusterTreePositionDTO\>
 |[getSourceConceptTreePositionPathsToRoot](#getsourceconceptreepositionpathstoroot)|Retrieve ancestors for a known source-asserted concept. | ArrayList\<SourceAtomClusterTreePositionPathDTO\>
 |[getSourceDescriptorTreePositionChildren](#getsourcedescriptortreepositionchildren)|Retrieve children for a known source-asserted descriptor. |ArrayList\<SourceAtomClusterTreePositionDTO\>
 |[getSourceDescriptorTreePositionPathsToRoot](#getsourcedescriptortreepositionpathstoroot)|Retrieve ancestors for a known source-asserted descriptor. | ArrayList\<SourceAtomClusterTreePositionPathDTO\>

**Each of these examples below requires an instance of the [UtsWsContentController](/soap/installation/content.html) and [UtsWsSecurityController](/soap/installation/authentication.html) interfaces**.

When obtaining parents or children via the SOAP API, you must first obtain the tree position(s) of the source-asserted identifier in question, as detailed in the
code samples below.


### getSourceConceptTreePositionChildren

**Method Signature**: ``` getSourceConceptTreePositionChildren(String ticket, String version,String scuiPosId,PSF psf)```

~~~~java

List<SourceAtomClusterTreePositionDTO> treePositions = new ArrayList<SourceAtomClusterTreePositionDTO>();
String currentUmlsRelease = utsMetadataService.getCurrentUMLSVersion(ticket);
treePositions = utsContentService.getSourceConceptTreePositions(ticket,currentUmlsRelease,"9468002","SNOMEDCT_US",myPsf);
		
    for (SourceAtomClusterTreePositionDTO treePosition:treePositions) {
			
	List<SourceAtomClusterTreePositionDTO> children = new ArrayList<SourceAtomClusterTreePositionDTO>();
	children = utsContentService
                   .getSourceConceptTreePositionChildren(ticketClient.getSingleUseTicket(tgt),currentUmlsRelease, treePosition.getUi(), myPsf);
		
	    for (SourceAtomClusterTreePositionDTO child:children) {
		    	
		String ui = child.getCluster().getUi();
		String name = child.getCluster().getDefaultPreferredName();
		System.out.println(ui +  "|" + name);
		    	
	    }
    }

~~~~

#### Sample Output

~~~~text
ui | name
10934361000119105|Closed fracture of navicular bone of right wrist
10934241000119100|Closed fracture of pisiform bone of left wrist
208375001|Closed fracture carpal bones, multiple
10934401000119101|Closed fracture of navicular bone of left wrist

~~~~
