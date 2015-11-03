title=Retrieving UMLS Mapping Information from UTS SOAP API
date=2015-08-18
updated=2015-08-18
type=page
status=published
navorder=9
~~~~~~


**Method: **getMapsets(String ticket,String version,PSF psf)

**Returns:** ArrayList< MapsetDTO>

**Use Case:** Given a UMLS release, this call returns the sets of mappings in the specified release. For each set of mappings, an object is returned that gives the details of the map set: the root source, the MapFrom and MapTo sources, mapping count, and other properties.

#### Sample Input (Java):

~~~~
gov.nih.nlm.uts.webservice.content.Psf myPsf = new gov.nih.nlm.uts.webservice.content.Psf();
 java.util.List<MapsetDTO> myAtoms = new ArrayList<MapsetDTO>();
 Mapsetdto = utsContentService.getMapsets(ticket, umlsRelease, myPsf);

 for (int i = 0; i < Mapsetdto.size(); i++) {
 MapsetDTO myMapset = Mapsetdto.get(i);
 String ui = myMapset.getUi();
 String name = myMapset.getName();
 String version = myMapset.getVersion();
 String frmrootsrc = myMapset.getFromRootSource();
 String frmcomplexity = myMapset.getFromComplexity();
 String torootsrc = myMapset.getToRootSource();
 String tocomplexity = myMapset.getToComplexity();
 }
~~~~

#### Sample Input (C#):

~~~~
content.psf myPsf = new content.psf();
 content.mapsetDTO[] MapsetDTO = utsContentService.getMapsets(ticket,"2011AB", myPsf);
 for (int i = 0; i < MapsetDTO.Length; i++) {
 content.mapsetDTO myMapsetDTO = MapsetDTO[i];
 string ui = myMapsetDTO.ui;
 string name = myMapsetDTO.name;
 string version = myMapsetDTO.version;
 string frmrootsrc = myMapsetDTO.fromRootSource;
 string frmcomplexity = myMapsetDTO.fromComplexity;
 string torootsrc = myMapsetDTO.toRootSource;
 string tocomplexity = myMapsetDTO.toComplexity;
~~~~

#### Sample Output:


 Concept UI |  Concept Name  | Concept Version  |    Concept FromRootSRC |  Concept FromComplexity |  Concept ToRootSRC |  Concept ToComplexity 
 --- |--- | --- | --- |--- | --- | --- 
C1541963   |  null     | 2005     | ICD9CM  |  SINGLE CODE   |   CCS |   null 
C2936849   |  null  | 2011_01 | ICD9CM   | SINGLE SDUI  |  ICD10CM |   null
C2936851   |  null   |    2011_01    |   ICD10CM   |SINGLE SDUI    |  ICD9CM   |  null
C2936850   |  null   | 2011_01     |  ICD10CM       | SINGLE SDUI  | ICD9CM    |  null  
C2963203  |  null      |     2011     |   ICD10PCS   |  SINGLE SCUI   |   ICD9CM    |  null 
>

**Method: **getMappings(String ticket,String version,String conceptId,PSF psf)

**Returns:**ArrayList< MappingDTO>

**Use Case:** Given a UMLS release and a mapset identifier (MAPSETCUI), this call returns the set of individual mappings between codes and identifiers (or expressions formed by codes and identifiers) from two different source vocabularies. Each mapping is an object that provides details of the mapping. The MapFrom and the MapTo objects include details, such as whether the mapping is source originated, the root source, ui, expression, attribute count, and type.

#### Sample Input (Java):

~~~~
myarrMapClient = utsContentService.getMappings(ticket, umlsRelease,"C3165219",myPsf);
 for (int i = 0; i < myarrMapClient.size(); i++) {
 MappingDTO myMapDTO = myarrMapClient.get(i);
 String frmExpression = myMapDTO.getMapFrom().getExpression();
 String frmRootSrc = myMapDTO.getMapFrom().getRootSource();
 String frmUi = myMapDTO.getMapFrom().getUi();
 String frmType = myMapDTO.getMapFrom().getType();
 String frmSrcUi = myMapDTO.getMapFrom().getRule();
 String toExpression = myMapDTO.getMapTo().getExpression();
 String toRootSrc = myMapDTO.getMapTo().getRootSource();
 String toUi = myMapDTO.getMapTo().getUi();
 String toType = myMapDTO.getMapTo().getType();
 String toSrcUi = myMapDTO.getMapTo().getSourceUi();
 }
~~~~

#### Sample Output:

Map From: 

Get Map From- Expression |  Get Map From-RootSource|   Get Map From-Ui  |Get Map From-Type  | Get Map From-Rule    
--- |--- | --- | --- | ---
 276586004   |  SNOMEDCT   | 276586004   |  SCUI  |   null   
93050005   |    SNOMEDCT | 93050005  |  SCUI |  null               
233907003     |    SNOMEDCT     |   233907003   |  SCUI     |   null  
250150003    |  SNOMEDCT   |   250150003  |  SCUI    |  null       
283196000  |  SNOMEDCT   | 283196000     | SCUI    | null 
400058002     |SNOMEDCT  | 400058002     | SCUI     |  null    
                       
Map to:

Get Map To- Expression  | Get Map To-RootSource  | Get Map To-Ui |  Get Map To-Type  |   Get Map To-SourceUi
--- |--- | --- | --- | ---
588.89  |   SNOMEDCT | 9549844056 | BOOLEAN_EXPRESSION_SDUI |  9549844056       
747.21   | SNOMEDCT    | 7329057    |  BOOLEAN_EXPRESSION_SDUI |  7329057      
427.1  | SNOMEDCT   | 966056 | BOOLEAN_EXPRESSION_SDUI|  966056   
null | SNOMEDCT   |  null    |   NOMAPTYPE    |  null           
880.02 AND E920.9 |   SNOMEDCT  |  9537146052    |  BOOLEAN_EXPRESSION_SDUI  | 9537146052 
198.89   |   SNOMEDCT  |4165052 | BOOLEAN_EXPRESSION_SDUI  | 4165052     

>

**Method: **getMapObjectToMapping(String ticket,String version,String UI,PSF psf)

**Returns:**ArrayList< MappingDTO>

**Use Case:** Given a UMLS release and a mapped-to identifier, this call returns the MapFrom and MapTo objects and their details. Information about the mapping includes a label describing the type of relation between the mapped codes, e.g. RQ = related and possibly synonymous. You can reference descriptions for these relation abbreviations at [Metathesaurus Release Abbreviations](http://www.nlm.nih.gov/research/umls/knowledge_sources/metathesaurus/release/abbreviations.html)

#### Sample Input (Java):

~~~~
myarrMapClient = utsContentService.getMapObjectToMapping(ticket, umlsRelease,"466.19", myPsf);
 for (int i = 0; i < myarrMapClient.size(); i++) {
 MappingDTO myMapDTO = myarrMapClient.get(i);
 String frmExpression = myMapDTO.getMapFrom().getExpression();
 String frmRootSrc = myMapDTO.getMapFrom().getRootSource();
 String frmUi = myMapDTO.getMapFrom().getUi();
 String frmType = myMapDTO.getMapFrom().getType();
 String frmSrcUi = myMapDTO.getMapFrom().getRule();
 String toExpression = myMapDTO.getMapTo().getExpression();
 String toRootSrc = myMapDTO.getMapTo().getRootSource();
 String toUi = myMapDTO.getMapTo().getUi();
 String toType = myMapDTO.getMapTo().getType();
 String toSrcUi = myMapDTO.getMapTo().getSourceUi();
 }
~~~~

#### Sample Output:

Map From: 

Get Map From- Expression |  Get Map From-RootSource|   Get Map From-Ui  |Get Map From-Type  | Get Map From-Rule    
--- |--- | --- | --- | ---       
J21.8 |  ICD10CM    | J21.8 |  SDUI  |    null     
J21.1    | ICD10CM |  J21.1   |  SDUI |  null   
J21.9  | ICD10CM      | J21.9  |  SDUI  |   null 

Map to:

Get Map To- Expression  | Get Map To-RootSource  | Get Map To-Ui |  Get Map To-Type  |   Get Map To-SourceUi
--- |--- | --- | --- | ---                  
466.19  | ICD10CM |466.19 |  SDUI  | null      
466.19  |  ICD10CM  |  466.19   | SDUI  | null  
466.19   | ICD10CM    | 466.19 |SDUI  |null      

>

**Method: **getMapObjectFromMapping(String ticket,String version,String UI,PSF psf)

**Returns:**ArrayList< MappingDTO>

**Use Case:** Given a UMLS release and a mapped-from identifier, this call returns the MapFrom and MapTo objects and their details.
Information about the mapping includes a label describing the type of relation between the mapped codes. For example, the label RQ = related and possibly synonymous. You can reference descriptions for these relation abbreviations at [Metathesaurus Release Abbreviations](http://www.nlm.nih.gov/research/umls/knowledge_sources/metathesaurus/release/abbreviations.html)

#### Sample Input (Java):

~~~~
myarrMapClient = utsContentService.getMapObjectFromMapping(ticket, umlsRelease, "718004", myPsf);
 for (int i = 0; i < myarrMapClient.size(); i++) {
 MappingDTO myMapDTO = myarrMapClient.get(i);
 String frmExpression = myMapDTO.getMapFrom().getExpression();
 String frmRootSrc = myMapDTO.getMapFrom().getRootSource();
 String frmUi = myMapDTO.getMapFrom().getUi();
 String frmType = myMapDTO.getMapFrom().getType();
 String frmSrcUi = myMapDTO.getMapFrom().getRule();
 String toExpression = myMapDTO.getMapTo().getExpression();
 String toRootSrc = myMapDTO.getMapTo().getRootSource();
 String toUi = myMapDTO.getMapTo().getUi();
 String toType = myMapDTO.getMapTo().getType();
 String toSrcUi = myMapDTO.getMapTo().getSourceUi();
 }
~~~~

#### Sample Output:

Map From: 

Get Map From- Expression |  Get Map From-RootSource|   Get Map From-Ui  |Get Map From-Type  | Get Map From-Rule    
--- |--- | --- | --- | ---       
718004|SNOMEDCT   | 718004   |SCUI    |  null   

Map to:

Get Map To- Expression  | Get Map To-RootSource  | Get Map To-Ui |  Get Map To-Type  |   Get Map To-SourceUi
--- |--- | --- | --- | ---  
466.19 | SNOMEDCT    |  5944050  |   BOOLEAN_EXPRESSION_SDUI  | 5944050   



