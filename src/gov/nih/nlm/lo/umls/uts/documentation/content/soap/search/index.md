title=Searching the SOAP API in UMLS
date=2015-08-14
updated=2015-08-14
type=page
status=unpublished
navorder=2
~~~~~~


**Method:**findConcepts(String ticket,String version,String target,String str, String searchType,PSF psf)

**Returns:**ArrayList< UiLabel> 


**Use Case:**You want to see a list of UMLS CUIs and their associated preferred names. You have a search string "lou gehrig disease" and want to return a list of CUIs having at least one atom that contains all of those words.
 ***It's important to note that the preferred names of the concepts returned may not match your search string.***

~~~~
**Note:**The "target" parameter indicates what kind of cluster on which you're basing a search. In findConcepts, the following values can be passed for target:
-   aui
-   atom (this is used for string searching)
-   code
-   concept
-   sourceConcept
-   sourceDescriptor


 The following values can be used for searchType in all of the finder service calls
-   exact
-   approximate
-   leftTruncation
-   rightTruncation
-   words
-   normalizedWords
-   normalizedString
~~~~


#### Sample Input (Java):
~~~~
UtsMetathesaurusFinder.Psf myPsf = new UtsMetathesaurusFinder.Psf();
 myPsf.setPageLn(50);
 List<UiLabel> myUiLabels = new ArrayList<UiLabel>();

 myUiLabels = UtsFinderService.findConcepts(ticket, 2011AB, "atom", "lou gehrig disease", "words", myPsf);

 for (int i = 0; i < myUiLabels.size(); i++) {
 UiLabel myUiLabel = myUiLabels.get(i);
 String ui = myUiLabel.getUi();
 String label = myUiLabel.getLabel();

 }
~~~~


#### Sample Input (C♯):
~~~~
Finder.psf myPsf = new Finder.psf();
 Finder.uiLabel[] myUiLabels = utsFinderService.findConcepts(ticket,"2011AB", "atom", "lou gehrig disease", "words", myPsf);

 myPsf.pageLn = 50 ;
 for (int i = 0; i < myUiLabels.Length; i++){

 Finder.uiLabel myUiLabel = myUiLabels[i];
 string ui = myUiLabel.ui;
 string label = myUiLabel.label;
 }
~~~~


#### Sample Output:

~~~~
//print out the results 
   UI: C0002736
   Name: Amyotrophic Lateral Sclerosis
 
   UI: C2317803
   Name: acquired amyotrophic lateral sclerosis
  
   UI: C2317805
   Name: multifactorial amyotrophic lateral sclerosis
  
   UI: C1862939
   Name: AMYOTROPHIC LATERAL SCLEROSIS 1
  
   UI: C1862940
   Name: AMYOTROPHIC LATERAL SCLEROSIS, AUTOSOMAL RECESSIVE
  
   UI: C2317804
   Name: X-linked amyotrophic lateral sclerosis
  
   UI: C2956919
   Name: Lou Gehrig's Disease Gene Mutation Reagents
~~~~

>


**Method:**findAtoms(String ticket,String version,String target,String str,String searchType,PSF psf)

**Returns:**�ArrayList< UiLabel>

**Use Case:** Given a UMLS release, a searchType, and the string or code you would like to search, this call returns a set of atom unique identifiers (AUI) each with its corresponding atom name (Label), that meet your search criteria.

~~~~
**Note:**  In findAtoms, the following values can be used for the "target" parameter:
-   aui
-   atom
-   code
-   sourceConcept
-   sourceDescriptor


 The following values can be used for searchType in all of the finder service calls
-   exact
-   approximate
-   leftTruncation
-   rightTruncation
-   words
-   normalizedWords
-   normalizedString
~~~~

#### Sample Input (Java):
~~~~
UtsMetathesaurusFinder.Psf myPsf = new UtsMetathesaurusFinder.Psf();
 myPsf.setPageLn(50);
 List<UiLabel> myUiLabels = new ArrayList<UiLabel>();
 myUiLabels = UtsFinderService.findAtoms(ticket, 2011AB, "atom", "lou gehrig disease", "exact", myPsf);

 for (int i = 0; i < myUiLabels.size(); i++) {
 UiLabel myUiLabel = myUiLabels.get(i);
 String ui = myUiLabel.getUi();
 String label = myUiLabel.getLabel();
 }
~~~~

#### Sample Input (C♯):
~~~~
Finder.psf myPsf = new Finder.psf();
 Finder.uiLabel[] myUiLabels = utsFinderService.findAtoms(ticket,"2011AB", "atom", "lou gehrig disease", "exact", myPsf);
 myPsf.pageLn = 50; 
 
 for (int i = 0; i < myUiLabels.Length; i++){

 Finder.uiLabel myUiLabel = myUiLabels[i];
 string ui = myUiLabel.ui;
 string label = myUiLabel.label;
 }
~~~~

#### Sample Output:

~~~~
 //print out the results
   UI: A17970785
   Name: Lou Gehrig Disease
  
   UI: A7571806
   Name: Lou Gehrig Disease
  
   UI: A0081037
   Name: Lou Gehrig Disease
  
   UI: A0428150
   Name: LOU GEHRIG DISEASE
  
   UI: A18552743
   Name: lou gehrig disease
~~~~
>

**Method:**findCodes(String ticket,String version,String target,String str,String searchType,PSF psf)

**Returns:**ArrayList< UiLabelRootSource> 


**Use Case:** Starting with an atom, source concept, source descriptor, or aui, you want to find codes, their preferred names, and the source vocabularies that provide them.


**Note:**  You should consider excluding **code = "NOCODE"** results from your result set. Some atoms from source vocabularies are assigned "NOCODE" during source processing, and will not be useful in the context of most finder search results.

~~~~
**Note:**  In findCodes, the following values can be used for the "target" parameter:
-   aui
-   atom
-   sourceConcept
-   sourceDescriptor


 The following values can be used for searchType in all of the finder service calls
-   exact
-   approximate
-   leftTruncation
-   rightTruncation
-   words
-   normalizedWords
-   normalizedString
~~~~

#### Sample Input (Java):
~~~~
UtsMetathesaurusFinder.Psf myPsf = new UtsMetathesaurusFinder.Psf();
 myPsf.setPageLn(50);
 List<UiLabelRootSource> myUiLabelsRootSource = new ArrayList<UiLabelRootSource>();
 myUiLabelsRootSource = UtsFinderService.findCodes(ticket, 2011AB, "atom", "diabetic foot", "exact", myPsf);

 for (int i = 0; i < myUiLabelsRootSource.size(); i++) {
 UiLabelRootSource myUiLabelRootSource = myUiLabelsRootSource.get(i);
 String ui = myUiLabelRootSource.getUi();
 String label = myUiLabelRootSource.getLabel();
 String source = myUiLabelRootSource.getRootSource();
 }
~~~~


#### Sample Input (C♯):
~~~~
Finder.psf myPsf = new Finder.psf();
 myPsf.pageLn = 50;
 Finder.uiLabelRootSource[] myUiLabelsRootSource = utsFinderService.findCodes(ticket, "2011AB", "atom", "diabetic foot", "exact", myPsf);

 for (int i = 0; i < myUiLabelsRootSource.Length; i++){

 Finder.uiLabelRootSource myUiLabelRootSource = myUiLabelsRootSource[i];
 string ui = myUiLabelRootSource.ui;
 string label = myUiLabelRootSource.label;
 string source = myUiLabelRootSource.rootSource
 }
~~~~

#### Sample Output:

~~~~
//print out the results
   UI: D017719
   Name: Diabetic Foot
   Source: MSH
  
   UI: T1341
   Name: Diabetic Foot
   Source: MEDLINEPLUS
  
   UI: N0000003630
   Name: Diabetic Foot [Disease/Finding]
   Source: NDFRT
  
   UI: NOCODE
   Name: Diabetic foot
   Source: RCD
  
   UI: 10060734
   Name: Diabetic foot
   Source: MDR
  
   UI: 280137006
   Name: Diabetic foot
   Source: SNOMEDCT
  
   UI: 0000020837
   Name: diabetic foot
   Source: CHV
  
   UI: 1002126
   Name: DIABETIC FOOT
   Source: CCPSS
~~~~
>


**Method:**findSourceConcepts(String ticket,String version,String target,String str,String searchType,PSF psf);

**Returns:**ArrayList< UiLabelRootSource>

**Use Case:**Starting with an atom, code, source descriptor, or aui, you want to find source concepts, their preferred names, and the source vocabularies that provide them.

~~~~
**Note:**  In findSourceConcepts, the following values can be used for the "target" parameter:
-   aui
-   atom
-   code
-   sourceDescriptor


 The following values can be used for searchType in all of the finder service calls
-   exact
-   approximate
-   leftTruncation
-   rightTruncation
-   words
-   normalizedWords
-   normalizedString
~~~~


#### Sample Input (Java):
~~~~
UtsMetathesaurusFinder.Psf myPsf = new UtsMetathesaurusFinder.Psf();
 myPsf.setPageLn(50);
 List<UiLabelRootSource> myUiLabelsRootSource = new ArrayList<UiLabelRootSource>();
 myUiLabelsRootSource = UtsFinderService.findSourceConcepts(ticket, 2011AB, "atom", "myocardial infarction", "words", myPsf);

 for (int i = 0; i < myUiLabelsRootSource.size(); i++) {
 UiLabelRootSource myUiLabelRootSource = myUiLabelsRootSource.get(i);
 String ui = myUiLabelRootSource.getUi();
 String label = myUiLabelRootSource.getLabel();
 String source = myUiLabelRootSource.getRootSource();
 }
~~~~


#### Sample Input (C♯):
~~~~
Finder.psf myPsf = new Finder.psf();
 myPsf.pageLn = 50;
 Finder.uiLabelRootSource[] myUiLabelsRootSource = utsFinderService.findSourceConcepts(ticket, "2011AB", "atom","myocardial infarction", "words", myPsf);

 for (int i = 0; i < myUiLabelsRootSource.Length; i++){

 Finder.uiLabelRootSource myUiLabelRootSource = myUiLabelsRootSource[i];
 string ui = myUiLabelRootSource.ui;
 string label = myUiLabelRootSource.label;
 string source = myUiLabelRootSource.rootSource
 }
~~~~


#### Sample Output:

~~~~
 //print out the results
   UI: M0014340
   Name: Myocardial Infarction
   Source: MSH
  
   UI: N0000002085
   Name: Myocardial Infarction [Disease/Finding]
   Source: NDFRT
  
   UI: C27996
   Name: Myocardial Infarction
   Source: NCI
  
   UI: LP98884-7
   Name: Myocardial infarction
   Source: LNC
  
   UI: 66514008
   Name: Coronary artery thrombosis
   Source: SNOMEDCT
  
   UI: 233824008
   Name: Myocardial infarction
   Source: SNOMEDCT
~~~~
>


**Method:**findSourceDescriptors(String ticket,String version,String target,String str,String searchType,PSF psf)

**Returns:**ArrayList< UiLabelRootSource>;

**Use Case:**Given a UMLS release, a searchType, the string or code you would like to search, and a root source abbreviation (RSAB), this call returns a set of source descriptor identifiers (SDUI) each with its corresponding name (Label), for the specified RSAB.

~~~~
**Note:**In findSourceDescriptors, the following values can be used for the "target" parameter:
-   aui
-   atom
-   code
-   sourceConcept


 The following values can be used for searchType in all of the finder service calls
-   exact
-   approximate
-   leftTruncation
-   rightTruncation
-   words
-   normalizedWords
-   normalizedString
~~~~


#### Sample Input (Java):
~~~~
UtsMetathesaurusFinder.Psf myPsf = new UtsMetathesaurusFinder.Psf();
myPsf.setPageLn(50);
 List<UiLabelRootSource>; myUiLabelsRootSource = new ArrayList<UiLabelRootSource>();
 myUiLabelsRootSource = UtsFinderService.findSourceDescriptors(ticket, 2011AB, "atom", "trophy", "leftTruncation", myPsf);

 for (int i = 0; i < myUiLabelsRootSources.size(); i++) {
 UiLabelRootSource myUiLabelRootSource = myUiLabelsRootSource.get(i);
 String ui = myUiLabelRootSource.getUi();
 String label = myUiLabelRootSource.getLabel();
 String source = myUiLabelRootSource.getRootSource();
 }
~~~~


#### Sample Input (C♯):
~~~~
Finder.psf myPsf = new Finder.psf();
 myPsf.pageLn = 50;
 Finder.uiLabelRootSource[] myUiLabelsRootSource = utsFinderService.findSourceDescriptors(ticket, "2011AB", "atom","trophy", "leftTruncation", myPsf);

 for (int i = 0; i < myUiLabelsRootSource.Length; i++){

 Finder.uiLabelRootSource myUiLabelRootSource = myUiLabelsRootSource[i];
 string ui = myUiLabelRootSource.ui;
 string label = myUiLabelRootSource.label;
 string source = myUiLabelRootSource.rootSource;
 }
~~~~

#### Sample Output:

~~~~
  //print out the results
   UI: D047508
   Name: Massive Hepatic Necrosis 
   Source: MSH
  
   UI: 570
   Name: Parenchymatous degeneration of liver
   Source: MTHICD9
  
   UI: 10070815
   Name: Acute yellow liver atrophy
   Source: MDR
  
   UI: D016301
   Name: Alveolar Bone Loss
   Source: MSH
  
   UI: 10004446
   Name: Benign prostatic hyperplasia
   Source: MDR
  
   UI: 600.0
   Name: Benign prostatic hypertrophy
   Source: MTHICD9
~~~~

