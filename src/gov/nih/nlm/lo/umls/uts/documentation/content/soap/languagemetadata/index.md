title=Language Metadata
date=2015-08-24
updated=2015-08-24
type=page
status=published
navorder=4
~~~~~~


**Method: **getLanguage(String ticket,String version,String language)

**Returns:** LanguageDTO

**Use Case:** Given a UMLS release and language abbreviation (LAT), this call returns the full name (expanded form) of the language along with the abbreviation.

#### Sample Input (Java):

~~~~
getLanguage(ticket, "2011AB", "DAN")
~~~~

#### Sample Input (C#):

~~~~
utsMetadataService.getLanguage(ticket, "2011AB", "SNOMEDCT");
~~~~

#### Sample Output:

~~~~
  LanguageDTO
   ClassType: Language
   Abbreviation: DAN
   ExpandedForm: Danish
~~~~
>

**Method: **getAllLanguages(String ticket,String version)

**Returns:** ArrayList< LanguageDTO>

**Use Case:** This call returns all valid languages for a given release. The language abbreviation and expanded form is given for each valid language. Below is a sample of some of the over 30 languages that exist in the UMLS as of the 2011AB release.


#### Sample Input (Java):

~~~~
getAllLanguages(ticket, "2011AB")
~~~~

#### Sample Input (C♯):

~~~~
utsMetadataService.getAllLanguages(ticket, "2011AB");\
~~~~

#### Sample Output:

~~~~
 		 1                    	   2                 	  3                 	 4                   	5                      	 6
   ClassType: Language    ClassType: Language    ClassType: Language     ClassType: Language    ClassType: Language      ClassType: Language
   Abbreviation: BAQ       Abbreviation: CZE     Abbreviation: DAN       Abbreviation: DUT      Abbreviation: ENG        Abbreviation: FIN
   ExpandedForm: Basque    ExpandedForm: Czech    ExpandedForm: Danish    ExpandedForm: Dutch    ExpandedForm: English    ExpandedForm: Finnish
~~~~
>

**Method: **getRootSourcesByLanguage(String ticket,String version,String languageAbbreviation)

**Returns:** ArrayList< RootSourceDTO>

**Use Case:** This method retrieves all the root sources that are provided in a particular language.


#### Sample Input (Java):

~~~~
myArrSrc = utsMetadataService.getRootSourcesByLanguage(ticket,umlsRelease, "GER");
 for (int i = 0; i < myArrSrc.size(); i++) {
 RootSourceDTO myArrSrcDTO = myArrSrc.get(i);
 String abbreviation = myArrSrcDTO.getAbbreviation();
 int restrictionLevel = myArrSrcDTO.getRestrictionLevel();
 String family = myArrSrcDTO.getFamily();
 String expForm = myArrSrcDTO.getExpandedForm();
 }
~~~~

#### Sample Output:

Abbreviation |  Restriction Level  | Family |  Expanded Form
--- | --- | --- | ---
DMDICD10     |  1    |ICD10  |  German translation of ICD10, 1995                       
 DMDUMD      |   1   |  UMD  |    German translation of UMDNS, 1996                          
 ICPCGER     |   0  | ICPC   |  ICPC, German Translation,1993                     
MDRGER        | 3  |MDR   |   Medical Dictionary for Regulatory Activities Terminology (MedDRA), German Edition, 15.1  
MSHGER      |   3  |  MSH     | German translation of the Medical Subject Headings, 2013        
WHOGER       |  2    |  WHO   |   WHOART, German Translation, 1997               

   