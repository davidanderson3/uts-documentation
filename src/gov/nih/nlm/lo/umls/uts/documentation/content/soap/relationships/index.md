title=Retrieving UMLS Relationship Information from UTS SOAP API
date=2015-08-18
updated=2015-08-18
type=page
status=published
navorder=10
~~~~~~

Interface | Method | Use Case | Object or Data type Returned 
-- | -- | -- | --
**UtsWsContentController**||||
 |[getSourceConceptSourceConceptRelations](#getsourceconceptsourceconceptrelations)|Retrieve relations for a known source-asserted concept|ArrayList\<SourceAtomClusterRelationDTO\>
 |[getSourceDescriptorSourceDescriptorRelations](#getsourcedescriptorsourcedescriptorrelations)|Retrieve relations for a known source-asserted concept|ArrayList\<SourceAtomClusterRelationDTO\>
 |[getCodeCodeRelations](#getcodecoderelations)|Retrieve relations for a known source-asserted code|ArrayList\<SourceAtomClusterRelationDTO\>
 |[getConceptConceptRelations](#getconceptrelations)|Retrieve relations for a known UMLS CUI|ArrayList\<ConceptRelationDTO\>
 |[getAtomAtomRelations](#getatomatomrelations)|Retrieve relations for a known UMLS AUI|ArrayList\<AtomRelationDTO\>

**Each of these examples below requires an instance of the [UtsWsContentController](/soap/installation/content.html) and [UtsWsSecurityController](/soap/installation/authentication.html) interfaces**.

### getSourceConceptSourceConceptRelations

**Method Signature**: ```getSourceConceptSourceConceptRelations(String ticket,String version,String sourceConceptId,String rootSourceAbbreviation, PSF psf)```

#### Sample Input

~~~~java
//find has_finding_site relations for 9468002, 'Closed fracture carpal bone'
int pageNumber=1;
String currentUmlsRelease = utsMetadataService.getCurrentUMLSVersion(ticket);
List<AtomClusterRelationDTO> relations = new ArrayList<AtomClusterRelationDTO>();
        
        do {
        myPsf.setPageNum(pageNumber);
        myPsf.setIncludeObsolete(false);
        myPsf.getIncludedAdditionalRelationLabels().add("has_finding_site");
	relations = utsContentService.getSourceConceptSourceConceptRelations(ticket,currentUmlsRelease, "9468002", "SNOMEDCT_US", myPsf);		
	     
	for (AtomClusterRelationDTO relation:relations) {
			
		System.out.println(relation.getRelationLabel()+"|"+relation
		.getAdditionalRelationLabel()+"|"+relation
		.getRelatedAtomCluster().getUi()+"|"+relation.getRelatedAtomCluster()
		.getDefaultPreferredName());
                
	}
	pageNumber++;
        } while(relations.isEmpty() == false);

~~~~

#### Sample output

~~~~text
RO|has_finding_site|83936004|Bone structure of carpus
RO|has_finding_site|24097009|Bone structure of hand
~~~~

### getSourceDescriptorSourceDescriptorRelations

**Method Signature**: ```getSourceDescriptorSourceDescriptorRelations(String ticket,String version,String sourceDescriptorId,String rootSourceAbbreviation, PSF psf)```

#### Sample Input

~~~~java
//Retrieve qualifiers for MeSH D015242, 'Ofloxacin'
int pageNumber=1;
String currentUmlsRelease = utsMetadataService.getCurrentUMLSVersion(ticket);
List<AtomClusterRelationDTO> relations = new ArrayList<AtomClusterRelationDTO>();
        
        do {
        myPsf.setPageNum(pageNumber);
        myPsf.setIncludeObsolete(false);
        myPsf.getIncludedRelationLabels().add("QB");
	relations = utsContentService.getSourceDescriptorSourceDescriptorRelations(ticket,currentUmlsRelease, "D015242", MSH, myPsf);		
	     
		   for (AtomClusterRelationDTO relation:relations) {
			
			  System.out.println(relation.getRelationLabel()+"|"+relation
			    .getRelatedAtomCluster().getUi()+"|"+relation.getRelatedAtomCluster()
			    .getDefaultPreferredName());
		    }
		  pageNumber++;
        } while(relations.isEmpty() == false);

~~~~

#### Sample Output

~~~~text
QB|Q000627|therapeutic use
QB|Q000633|toxicity
QB|Q000145|classification
QB|Q000737|chemistry
QB|Q000032|analysis
QB|Q000037|antagonists & inhibitors
QB|Q000009|adverse effects
QB|Q000494|pharmacology
QB|Q000134|cerebrospinal fluid
QB|Q000191|economics
QB|Q000138|chemical synthesis
QB|Q000592|standards
QB|Q000528|radiation effects
QB|Q000819|agonists
QB|Q000493|pharmacokinetics
QB|Q000031|analogs & derivatives
QB|Q000506|poisoning
QB|Q000302|isolation & purification
QB|Q000097|blood
QB|Q000276|immunology
QB|Q000652|urine
QB|Q000266|history
QB|Q000008|administration & dosage
QB|Q000378|metabolism
QB|Q000744|contraindications
QB|Q000600|supply & distribution
~~~~

### getCodeCodeRelations

**Method Signature**: ```getCodeCodeRelations(String ticket,String version,String codeId,String rootSourceAbbreviation, PSF psf)```

#### Sample Input

~~~~java
//Retrieve panel members for LNC 72171-2, 'Glucose tolerance 2 hours panel - Serum or Plasma'
int pageNumber=1;
String currentUmlsRelease = utsMetadataService.getCurrentUMLSVersion(ticket);
List<AtomClusterRelationDTO> relations = new ArrayList<AtomClusterRelationDTO>();
        
        do {
        myPsf.setPageNum(pageNumber);
        myPsf.setIncludeObsolete(false);
        myPsf.getIncludedAdditionalRelationLabels().add("has_member");
	relations = utsContentService.getCodeCodeRelations(ticket,currentUmlsRelease, "72171-2", "LNC", myPsf);		
	     
	    for (AtomClusterRelationDTO relation:relations) {
			
		System.out.println(relation.getRelationLabel()+"|"+relation
		.getAdditionalRelationLabel()+"|"+relation
		.getRelatedAtomCluster().getUi()+"|"+relation.getRelatedAtomCluster()
		.getDefaultPreferredName());
	    }
            
	    pageNumber++;
        } while(relations.isEmpty() == false);

~~~~

#### Sample Output

~~~~text
RB|has_member|25665-1|Glucose^1H post XXX challenge:SCnc:Pt:Ser/Plas:Qn
RB|has_member|25668-5|Glucose^2H post XXX challenge:SCnc:Pt:Ser/Plas:Qn
RB|has_member|25679-2|Glucose^1.5H post XXX challenge:SCnc:Pt:Ser/Plas:Qn
RB|has_member|14771-0|Glucose^post CFst:SCnc:Pt:Ser/Plas:Qn
~~~~

### getConceptConceptRelations

**Method Signature**: ```getConceptConceptRelations(String ticket, String version, String conceptId, PSF psf)```

#### Sample Input

~~~~java
//retrieve relations for C0014591, 'Epistaxis'
int pageNumber=1;
String currentUmlsRelease = utsMetadataService.getCurrentUMLSVersion(ticket);
List<ConceptRelationDTO> relations = new ArrayList<ConceptRelationDTO>();
        
        do {
        myPsf.setPageNum(pageNumber);
		relations = utsContentService.getConceptConceptRelations(ticket,currentUmlsRelease, "C0014591",myPsf);		
		System.out.println(relations.size());
		   for (ConceptRelationDTO relation:relations) {
			
			  System.out.println(relation.getRelatedConcept().getUi()+"|"+relation
				.getRelationLabel()+"|"+relation
				.getAdditionalRelationLabel()+"|"+relation
                                .getRelatedConcept().getDefaultPreferredName());
		    }
		  pageNumber++;
        } while(relations.isEmpty() == false);

~~~~


#### Sample Output

~~~~text
C0188972|RO||Epistaxis control
C0189015|RO||Control of epistaxis by packing of posterior and anterior nose
C0189064|RO||Control of epistaxis by cauterization and packing
C2228238|RO||Epistaxis on exam
C1963103|RO||Nose Hemorrhage Adverse Event
C0179204|RO||Nasal balloon
C0240549|RO||nose discharge bloody
C0344367|RO||Has nosebleeds - epistaxis
C0176350|RO||Control of epistaxis by anterior nasal packing
C0176354|RO||Control of epistaxis by ligation of the external carotid artery
C0176355|RO||Control of epistaxis by excision of nasal mucosa and skin grafting of septum and lateral nasal wall
C0176356|RO||Control of epistaxis by other means
C0189040|RO||Control of epistaxis by ligation of ethmoidal arteries
C0189041|RO||Control of epistaxis by (transantral) ligation of the maxillary artery
~~~~

### getAtomAtomRelations

**Method Signature**: ```getAtomAtomRelations(String ticket, String version, String atomId, PSF psf)```

#### Sample Input

~~~~java

//retrieve relations for which HL7V3.0 code 'MaritalStatus' is a parent
int pageNumber=1;
String currentUmlsRelease = utsMetadataService.getCurrentUMLSVersion(ticket);
List<AtomRelationDTO> relations = new ArrayList<AtomRelationDTO>();
AtomDTO atom = utsContentService.getDefaultPreferredAtom(ticket, currentUmlsRelease, identifier, rsab);
        
        do {
        myPsf.setPageNum(pageNumber);
        myPsf.getIncludedRelationLabels().add("PAR");
		relations = utsContentService.getAtomAtomRelations(ticket,currentUmlsRelease, atom.getUi(),myPsf);		
		assertFalse(relations.isEmpty());
		System.out.println(relations.size());
		   for (AtomRelationDTO relation:relations) {
			
			  System.out.println(relation.getRelatedAtom().getUi()+"|"+relation
			    .getRelationLabel()+"|"+relation
			    .getAdditionalRelationLabel()+"|"+relation.getRelatedAtom()
			    .getTermString().getDefaultPreferredName());
		    }
		  pageNumber++;
        } while(relations.isEmpty() == false);

~~~~

#### Sample Output

~~~~text
A8318072|PAR||Interlocutory
A8318166|PAR||Annulled
A8317988|PAR||Domestic partner
A8317267|PAR||Married
A8316726|PAR||Never Married
A24155777|PAR||unmarried
A8318084|PAR||Legally Separated
A8317438|PAR||Polygamous
A8317017|PAR||Widowed
A8316586|PAR||Divorced
~~~~
