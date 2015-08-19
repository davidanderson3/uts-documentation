title=Metadata
date=2015-08-20
updated=2015-08-20
type=page
status=unpublished
category=Metadata
navorder=4
~~~~~~


**Method: **<span class="method-name">getRootSource</span><span
class="method-parameters">(String ticket,String version,String
rootSourceAbbreviation)</span>
**Returns:** <span
class="method-return-type">RootSourceDTO </span>[<span
class="see_javadocs">(see
javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/metadata/RootSourceDTO.html)

<div class="method-description">

**Use Case:** This method returns details of a given Metathesaurus root
source abbreviation (RSAB) including content contact, license contact,
language, expanded form, preferred name, abbreviation, short name,
context type, family, and restriction level. The example below retrieves
the expanded form and restriction level for SNOMEDCT.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

RootSourceDTO myRootSource = utsMetadataService.getRootSource(ticket,
"2011AB", "SNOMEDCT");\
 String expandedForm = myRootSource.getExpandedForm();\
 int restrictionLevel = myRootSource.getRestrictionLevel();\

</div>

#### Sample Input (C♯):

<div class="input rounded-content-block">

Metadata.rootSourceDTO myRootSource =
utsMetadataService.getRootSource(ticket, "2011AB", "SNOMEDCT");\
 string expandedForm = myRootSource.expandedForm;\
 int restrictionLevel = myRootSource.restrictionLevel;\

</div>

#### Sample Output:

  -----------------------------------------------------------
  <span class="code-comment">print out the results </span>\
   Expanded Form: SNOMED Clinical Terms, 2011\_07\_31\
   Restriction Level: 9\
  -----------------------------------------------------------

</div>

<div id="getAllRootSources" class="method rounded-content-block">

**Method: **<span class="method-name">getAllRootSources</span><span
class="method-parameters">(String ticket,String version)</span>
**Returns:** <span
class="method-return-type">ArrayList&lt;RootSourceDTO&gt; </span>[<span
class="see_javadocs">(see
javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/metadata/RootSourceDTO.html)

<div class="method-description">

**Use Case:** This method returns an array list of all sources in the
UMLS for a given release. In the example below, we show only the first
and last members (rather than all 161 members) of the array list
returned for the sources in the 2011AB UMLS.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

List&lt;RootSourceDTO&gt; myRootSources = new
ArrayList&lt;RootSourceDTO&gt;();\
\
 myRootSources = utsMetadataService.getAllRootSources(ticket,
"2011AB");\
\
 for (int i = 0; i &lt; myRootSources.size(); i++) {\
 RootSourceDTO myRootSourcesDTO = myRootSources.get(i);\
 String PreferredName = myRootSourcesDTO.getPreferredName();\
 String Abbreviation = myRootSourcesDTO.getAbbreviation();\
 int RestrictionLevel = myRootSourcesDTO.getRestrictionLevel();\
 }

</div>

#### Sample Input (C♯):

<div class="input rounded-content-block">

Metadata.rootSourceDTO\[\] myRootSources =
utsMetadataService.getAllRootSources(ticket, "2011AB");\
 for (int i = 0; i &lt; myRootSources.Length; i++){\
\
 Metadata.rootSourceDTO myRootSourcesDTO = myRootSources\[i\];\
 string PreferredName = myRootSourcesDTO.preferredName;\
 string Abbreviation = myRootSourcesDTO.abbreviation;\
 int RestrictionLevel = myRootSourcesDTO.restrictionLevel;\
 }

</div>

#### Sample Output:

  -----------------------------------------------------
  Preferred Name: AI/RHEUM, 1993\
     Abbreviation: AIR\
     Restriction Level: 0\
  \
   Preferred Name: WHOART, Spanish Translation, 1997\
     Abbreviation: WHOSPA\
     Restriction Level: 2\
  \
  -----------------------------------------------------

</div>

<div id="getAllRootSourceFamilies" class="method rounded-content-block">

**Method: **<span
class="method-name">getAllRootSourceFamilies</span><span
class="method-parameters">(String ticket,String version)</span>
**Returns:** <span
class="method-return-type">ArrayList&lt;RootSourceDTO&gt; </span>[<span
class="see_javadocs">(see
javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/metadata/RootSourceDTO.html)

<div class="method-description">

**Use Case:** This method retrieves all the source families present as
per a given UMLS release. You can also retrieve the source restriction
level and the full(expanded) form of the source name.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

myArrSrc = utsMetadataService.getUpdatedSourcesByVersion(ticket,
umlsRelease);\
\
 for (int i = 0; i &lt; myArrSrc.size(); i++) {\
 RootSourceDTO myArrSrcDTO = myArrSrc.get(i);\
 String abbreviation = myArrSrcDTO.getAbbreviation();\
 int restrictionLevel = myArrSrcDTO.getRestrictionLevel();\
 String family = myArrSrcDTO.getFamily();\
 String expForm = myArrSrcDTO.getExpandedForm();\
 }\

</div>

#### Sample Output:

+--------------------------------------------------------------------------+
|   Abbreviation    Restriction Level   Family          Expanded Form      |
|   --------------- ------------------- --------------- ------------------ |
| ------------------------------------------------------------------------ |
| ------------------------------------------------------                   |
|   AIR             0                   AIR             AI/RHEUM, 1993     |
|   ALT             3                   ALT             Alternative Billin |
| g Concepts, 2009                                                         |
|   AOD             0                   AOD             Alcohol and Other  |
| Drug Thesaurus, 2000                                                     |
|   AOT             0                   AOT             Authorized Osteopa |
| thic Thesaurus, 2003                                                     |
|   BI              2                   BI              Beth Israel Vocabu |
| lary, 1.0                                                                |
|   CCC             1                   CCC             Clinical Care Clas |
| sification, 2\_5                                                         |
|   CCPSS           3                   CCPSS           Canonical Clinical |
|  Problem Statement System, 1999                                          |
|   CCS             0                   CCS             Clinical Classific |
| ations Software, 2005                                                    |
|   CHV             0                   CHV             Consumer Health Vo |
| cabulary, 2011\_02                                                       |
|   COSTAR          0                   COSTAR          COSTAR, 1989-1995  |
|   CPM             2                   CPM             Medical Entities D |
| ictionary, 2003                                                          |
|   CPT             3                   CPT             Current Procedural |
|  Terminology, 2013                                                       |
|   CSP             0                   CSP             CRISP Thesaurus, 2 |
| 006                                                                      |
|   CST             0                   CST             COSTART, 1995      |
|   DDB             3                   DDB             Diseases Database, |
|  2000                                                                    |
|   DSM3R           3                   DSM3R           DSM-III-R, 1987    |
|   DSM4            3                   DSM4            DSM-IV, 1994       |
|   DXP             0                   DXP             DXplain, 1994      |
|   FMA             0                   FMA             Foundational Model |
|  of Anatomy Ontology, 3\_1                                               |
|   GO              0                   GO              Gene Ontology, 201 |
| 2\_04\_03                                                                |
|   GS              3                   GS              Gold Standard Drug |
|  Database, 2013\_02\_01                                                  |
|   HCPCS           0                   HCPCS           Healthcare Common  |
| Procedure Coding System, 2013                                            |
|   HGNC            0                   HGNC            HUGO Gene Nomencla |
| ture Committee, 2012\_05                                                 |
|   HL7V2.5         0                   HL7V2.5         HL7 Vocabulary Ver |
| sion 2.5, 2003\_08\_30                                                   |
|   HL7V3.0         0                   HL7V3.0         HL7 Vocabulary Ver |
| sion 3.0, 2011\_03                                                       |
|   HLREL           3                   HLREL           ICPC2E-ICD10 relat |
| ionships from Dr. Henk Lamberts, 1998                                    |
|   ICD10           3                   ICD10           ICD10, 1998        |
|   ICD10AM         3                   ICD10AM         International Stat |
| istical Classification of Diseases and Related Health Problems, 10th Rev |
| ision, Australian Modification, January 2000 Release                     |
|   ICD10CM         4                   ICD10CM         International Clas |
| sification of Diseases, 10th Edition, Clinical Modification, 2013        |
|   ICD10PCS        0                   ICD10PCS        ICD-10-PCS, 2013   |
|   ICD9CM          0                   ICD9CM          International Clas |
| sification of Diseases, Ninth Revision, Clinical Modification, 2013\_201 |
| 2\_08\_06                                                                |
|   ICF             4                   ICF             International Clas |
| sification of Functioning, Disability and Health, 2008\_12\_19           |
|   ICNP            3                   ICNP            International Clas |
| sification for Nursing Practice, 2011                                    |
|   ICPC            0                   ICPC            International Clas |
| sification of Primary Care, 1993                                         |
|   ICPC2EENG       3                   ICPC2EENG       International Clas |
| sification of Primary Care 2nd Edition, Electronic, 2E, 200203           |
|   ICPC2ICD10ENG   3                   ICPC2ICD10ENG   ICPC2 - ICD10 Thes |
| aurus, 200412                                                            |
|   ICPC2P          3                   ICPC2P          ICPC-2 PLUS        |
|   JABL            1                   JABL            Online Congenital  |
| Multiple Anomaly/Mental Retardation Syndromes, 1999                      |
|   KCD5            3                   KCD5            Korean Standard Cl |
| assification of Disease Version 5, 2008                                  |
|   LCH             0                   LCH             Library of Congres |
| s Subject Headings, 1990                                                 |
|   LNC             0                   LNC             LOINC, 242         |
|   MCM             0                   MCM             McMaster Universit |
| y Epidemiology Terms, 1992                                               |
|   MDDB            3                   MDDB            Master Drug Data B |
| ase, 2013\_01\_30                                                        |
|   MDR             3                   MDR             Medical Dictionary |
|  for Regulatory Activities Terminology (MedDRA), 15.1                    |
|   MED             0                   MED             MEDLINE (2008-2013 |
| )                                                                        |
|   MEDCIN          3                   MEDCIN          MEDCIN, 3\_2012\_1 |
| 2\_14                                                                    |
|   MEDLINEPLUS     0                   MEDLINEPLUS     MedlinePlus Health |
|  Topics, 20130221                                                        |
|   MMSL            1                   MMSL            Multum MediSource  |
| Lexicon, 2013\_02\_01                                                    |
|   MMX             3                   MMX             Micromedex RED BOO |
| K, 2013\_02\_04                                                          |
|   MSH             0                   MSH             Medical Subject He |
| adings, 2013\_2013\_01\_21                                               |
|   MTH             0                   MTH             UMLS Metathesaurus |
|   MTHFDA          0                   MTHFDA          Metathesaurus FDA  |
| National Drug Code Directory, 2011\_06\_01\_13\_03\_04                   |
|   MTHMST          0                   MTHMST          Metathesaurus Vers |
| ion of Minimal Standard Terminology Digestive Endoscopy, 2001            |
|   MTHSPL          0                   MTHSPL          Metathesaurus FDA  |
| Structured Product Labels, 2013\_02\_26                                  |
|   NAN             3                   NAN             NANDA nursing diag |
| noses: definitions & classification, 2004                                |
|   NCBI            0                   NCBI            NCBI Taxonomy, 201 |
| 2\_04\_16                                                                |
|   NCI             0                   NCI             NCI Thesaurus, 201 |
| 2\_02D                                                                   |
|   NCISEER         0                   NCISEER         NCI SEER ICD Neopl |
| asm Code Mappings, 1999                                                  |
|   NDDF            3                   NDDF            FDB MedKnowledge ( |
| formerly NDDF Plus), 2013\_02\_06                                        |
|   NDFRT           0                   NDFRT           National Drug File |
| , 2013\_02\_04                                                           |
|   NEU             3                   NEU             NeuroNames, 2012\_ |
| 08\_23                                                                   |
|   NIC             3                   NIC             Nursing Interventi |
| ons Classification (NIC), 2005                                           |
|   NOC             3                   NOC             Nursing Outcomes C |
| lassification, 3rd Edition                                               |
|   OMIM            0                   OMIM            Online Mendelian I |
| nheritance in Man, 2012\_05\_02                                          |
|   OMS             1                   OMS             Omaha System, 2005 |
|   PCDS            3                   PCDS            Patient Care Data  |
| Set, 1997                                                                |
|   PDQ             0                   PDQ             Physician Data Que |
| ry, 2007\_02                                                             |
|   PNDS            3                   PNDS            Perioperative Nurs |
| ing Data Set, 3rd edition, 2011                                          |
|   PPAC            3                   PPAC            Pharmacy Practice  |
| Activity Classification, 1998                                            |
|   PSY             3                   PSY             Thesaurus of Psych |
| ological Index Terms, 2004                                               |
|   QMR             0                   QMR             Quick Medical Refe |
| rence (QMR), 1996                                                        |
|   RAM             0                   RAM             QMR clinically rel |
| ated terms from Randolph A. Miller, 1999                                 |
|   RCD             3                   RCD             Clinical Terms Ver |
| sion 3 (CTV3) (Read Codes), 1999                                         |
|   RXNORM          0                   RXNORM          RxNorm Vocabulary, |
|  12AB\_130304F                                                           |
|   SNM             9                   SNM             SNOMED-2, 2        |
|   SNMI            9                   SNMI            SNOMED Internation |
| al, 1998                                                                 |
|   SNOMEDCT        9                   SNOMEDCT        SNOMED Clinical Te |
| rms, 2013\_01\_31                                                        |
|   SOP             0                   SOP             Source of Payment  |
| Typology, 5                                                              |
|   SPN             0                   SPN             Standard Product N |
| omenclature, 2003                                                        |
|   SRC             0                   SRC             Metathesaurus Sour |
| ce Terminology Names                                                     |
|   TKMT            0                   TKMT            Traditional Korean |
|  Medical Terms, 2011                                                     |
|   ULT             3                   ULT             UltraSTAR, 1993    |
|   UMD             1                   UMD             UMDNS: product cat |
| egory thesaurus, 2013                                                    |
|   USPMG           0                   USPMG           USP Model Guidelin |
| es, 2004                                                                 |
|   UWDA            0                   UWDA            University of Wash |
| ington Digital Anatomist, 1.7.3                                          |
|   VANDF           0                   VANDF           Veterans Health Ad |
| ministration National Drug File, 2013\_01\_15                            |
|   WHO             2                   WHO             WHO Adverse Reacti |
| on Terminology, 1997                                                     |
+--------------------------------------------------------------------------+

</div>

<div id="getRootSourcesByFamily" class="method rounded-content-block">

**Method: **<span class="method-name">getRootSourcesByFamily</span><span
class="method-parameters">(String ticket,String version,String
family)</span>
**Returns:** <span
class="method-return-type">ArrayList&lt;RootSourceDTO&gt; </span>[<span
class="see_javadocs">(see
javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/metadata/RootSourceDTO.html)

<div class="method-description">

**Use Case:** This method retrieves all the root sources for a given
source family. You can also retrieve the source restriction level and
the full(expanded) form of the source name.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

myArrSrc = utsMetadataService.getRootSourcesByFamily(ticket,
umlsRelease, "SNOMEDCT");\
\
 for (int i = 0; i &lt; myArrSrc.size(); i++) {\
 RootSourceDTO myArrSrcDTO = myArrSrc.get(i);\
 String abbreviation = myArrSrcDTO.getAbbreviation();\
 int restrictionLevel = myArrSrcDTO.getRestrictionLevel();\
 String family = myArrSrcDTO.getFamily();\
 String expForm = myArrSrcDTO.getExpandedForm();\
 }\

</div>

#### Sample Output:

+--------------------------------------------------------------------------+
|   Abbreviation   Restriction Level   Family     Expanded Form            |
|   -------------- ------------------- ---------- ------------------------ |
| ---------------------------------------                                  |
|   SCTSPA         9                   SNOMEDCT   SNOMED Clinical Terms, S |
| panish Language Edition, 2012\_10\_31                                    |
|   SCTUSX         0                   SNOMEDCT   US Extension to SNOMED C |
| T(R), 2013\_03\_01                                                       |
|   SNOMEDCT       9                   SNOMEDCT   SNOMED Clinical Terms, 2 |
| 013\_01\_31                                                              |
+--------------------------------------------------------------------------+

</div>

<div id="getRootSourcesByRestrictionLevel"
class="method rounded-content-block">

**Method: **<span
class="method-name">getRootSourcesByRestrictionLevel</span><span
class="method-parameters">(String ticket,String version,int
restrictionLevel)</span>
**Returns:** <span
class="method-return-type">ArrayList&lt;RootSourceDTO&gt; </span>[<span
class="see_javadocs">(see
javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/metadata/RootSourceDTO.html)

<div class="method-description">

**Use Case:** This method retrieves all the root sources for a
particular restriction level.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

myArrSrc = utsMetadataService.getRootSourcesByRestrictionLevel(ticket,
umlsRelease, "0");\
\
 for (int i = 0; i &lt; myArrSrc.size(); i++) {\
 RootSourceDTO myArrSrcDTO = myArrSrc.get(i);\
 String abbreviation = myArrSrcDTO.getAbbreviation();\
 int restrictionLevel = myArrSrcDTO.getRestrictionLevel();\
 String family = myArrSrcDTO.getFamily();\
 String expForm = myArrSrcDTO.getExpandedForm();\
 }\

</div>

#### Sample Output:

+--------------------------------------------------------------------------+
|   Abbreviation   Restriction Level   Family        Expanded Form         |
|   -------------- ------------------- ------------- --------------------- |
| ------------------------------------------------------------------------ |
| ----------------------------------------------                           |
|   AIR            0                   AIR           AI/RHEUM, 1993        |
|   AOD            0                   AOD           Alcohol and Other Dru |
| g Thesaurus, 2000                                                        |
|   AOT            0                   AOT           Authorized Osteopathi |
| c Thesaurus, 2003                                                        |
|   CCS            0                   CCS           Clinical Classificati |
| ons Software, 2005                                                       |
|   CHV            0                   CHV           Consumer Health Vocab |
| ulary, 2011\_02                                                          |
|   COSTAR         0                   COSTAR        COSTAR, 1989-1995     |
|   CSP            0                   CSP           CRISP Thesaurus, 2006 |
|   CST            0                   CST           COSTART, 1995         |
|   DXP            0                   DXP           DXplain, 1994         |
|   FMA            0                   FMA           Foundational Model of |
|  Anatomy Ontology, 3\_1                                                  |
|   GO             0                   GO            Gene Ontology, 2012\_ |
| 04\_03                                                                   |
|   HCPCS          0                   HCPCS         Healthcare Common Pro |
| cedure Coding System, 2013                                               |
|   HGNC           0                   HGNC          HUGO Gene Nomenclatur |
| e Committee, 2012\_05                                                    |
|   HL7V2.5        0                   HL7V2.5       HL7 Vocabulary Versio |
| n 2.5, 2003\_08\_30                                                      |
|   HL7V3.0        0                   HL7V3.0       HL7 Vocabulary Versio |
| n 3.0, 2011\_03                                                          |
|   ICD10PCS       0                   ICD10PCS      ICD-10-PCS, 2013      |
|   ICD9CM         0                   ICD9CM        International Classif |
| ication of Diseases, Ninth Revision, Clinical Modification, 2013\_2012\_ |
| 08\_06                                                                   |
|   ICPC           0                   ICPC          International Classif |
| ication of Primary Care, 1993                                            |
|   ICPCBAQ        0                   ICPC          ICPC, Basque Translat |
| ion, 1993                                                                |
|   ICPCDAN        0                   ICPC          ICPC, Danish Translat |
| ion, 1993                                                                |
|   ICPCDUT        0                   ICPC          ICPC, Dutch Translati |
| on, 1993                                                                 |
|   ICPCFIN        0                   ICPC          ICPC, Finnish Transla |
| tion, 1993                                                               |
|   ICPCFRE        0                   ICPC          ICPC, French Translat |
| ion, 1993                                                                |
|   ICPCGER        0                   ICPC          ICPC, German Translat |
| ion, 1993                                                                |
|   ICPCHEB        0                   ICPC          ICPC, Hebrew Translat |
| ion, 1993                                                                |
|   ICPCHUN        0                   ICPC          ICPC, Hungarian Trans |
| lation, 1993                                                             |
|   ICPCITA        0                   ICPC          ICPC, Italian Transla |
| tion, 1993                                                               |
|   ICPCNOR        0                   ICPC          ICPC, Norwegian Trans |
| lation, 1993                                                             |
|   ICPCPOR        0                   ICPC          ICPC, Portuguese Tran |
| slation, 1993                                                            |
|   ICPCSPA        0                   ICPC          ICPC, Spanish Transla |
| tion, 1993                                                               |
|   ICPCSWE        0                   ICPC          ICPC, Swedish Transla |
| tion, 1993                                                               |
|   LCH            0                   LCH           Library of Congress S |
| ubject Headings, 1990                                                    |
|   LNC            0                   LNC           LOINC, 242            |
|   LNC\_NPUAP     0                   LNC           Pressure Ulcer Stages |
| , 242                                                                    |
|   LNC\_OPTIMAL   0                   LNC           Outpatient Physical T |
| herapy Improvement in Movement Assessment Log, 242\_2005                 |
|   MBD            0                   MED           MEDLINE (2003-2007)   |
|   MCM            0                   MCM           McMaster University E |
| pidemiology Terms, 1992                                                  |
|   MED            0                   MED           MEDLINE (2008-2013)   |
|   MEDLINEPLUS    0                   MEDLINEPLUS   MedlinePlus Health To |
| pics, 20130221                                                           |
|   MSH            0                   MSH           Medical Subject Headi |
| ngs, 2013\_2013\_01\_21                                                  |
|   MTH            0                   MTH           UMLS Metathesaurus    |
|   MTHCH          0                   CPT           Metathesaurus CPT Hie |
| rarchical Terms, 2013                                                    |
|   MTHFDA         0                   MTHFDA        Metathesaurus FDA Nat |
| ional Drug Code Directory, 2011\_06\_01\_13\_03\_04                      |
|   MTHHH          0                   HCPCS         Metathesaurus HCPCS H |
| ierarchical Terms, 2013                                                  |
|   MTHHL7V2.5     0                   HL7V2.5       HL7 Vocabulary Versio |
| n 2.5, 7-bit equivalents, 2003\_08                                       |
|   MTHICD9        0                   ICD9CM        International Classif |
| ication of Diseases, Ninth Revision, Clinical Modification, Metathesauru |
| s additional entry terms, 2013\_2012\_08\_06                             |
|   MTHMST         0                   MTHMST        Metathesaurus Version |
|  of Minimal Standard Terminology Digestive Endoscopy, 2001               |
|   MTHMSTFRE      0                   MTHMST        Metathesaurus Version |
|  of Minimal Standard Terminology Digestive Endoscopy, French Translation |
| , 2001                                                                   |
|   MTHMSTITA      0                   MTHMST        Metathesaurus Version |
|  of Minimal Standard Terminology Digestive Endoscopy, Italian Translatio |
| n, 2001                                                                  |
|   MTHSPL         0                   MTHSPL        Metathesaurus FDA Str |
| uctured Product Labels, 2013\_02\_26                                     |
|   NCBI           0                   NCBI          NCBI Taxonomy, 2012\_ |
| 04\_16                                                                   |
|   NCI            0                   NCI           NCI Thesaurus, 2012\_ |
| 02D                                                                      |
|   NCISEER        0                   NCISEER       NCI SEER ICD Neoplasm |
|  Code Mappings, 1999                                                     |
|   NDFRT          0                   NDFRT         National Drug File, 2 |
| 013\_02\_04                                                              |
|   NLM-MED        0                   MED           National Library of M |
| edicine Medline Data                                                     |
|   OMIM           0                   OMIM          Online Mendelian Inhe |
| ritance in Man, 2012\_05\_02                                             |
|   PDQ            0                   PDQ           Physician Data Query, |
|  2007\_02                                                                |
|   QMR            0                   QMR           Quick Medical Referen |
| ce (QMR), 1996                                                           |
|   RAM            0                   RAM           QMR clinically relate |
| d terms from Randolph A. Miller, 1999                                    |
|   RXNORM         0                   RXNORM        RxNorm Vocabulary, 12 |
| AB\_130304F                                                              |
|   SCTUSX         0                   SNOMEDCT      US Extension to SNOME |
| D CT(R), 2013\_03\_01                                                    |
|   SOP            0                   SOP           Source of Payment Typ |
| ology, 5                                                                 |
|   SPN            0                   SPN           Standard Product Nome |
| nclature, 2003                                                           |
|   SRC            0                   SRC           Metathesaurus Source  |
| Terminology Names                                                        |
|   TKMT           0                   TKMT          Traditional Korean Me |
| dical Terms, 2011                                                        |
|   USPMG          0                   USPMG         USP Model Guidelines, |
|  2004                                                                    |
|   UWDA           0                   UWDA          University of Washing |
| ton Digital Anatomist, 1.7.3                                             |
|   VANDF          0                   VANDF         Veterans Health Admin |
| istration National Drug File, 2013\_01\_15                               |
+--------------------------------------------------------------------------+

</div>

<div id="getVersionedSources" class="method rounded-content-block">

**Method: **<span class="method-name">getVersionedSources</span><span
class="method-parameters">(String ticket,String version,String
rootSourceAbbreviation)</span>
**Returns:** <span
class="method-return-type">ArrayList&lt;SourceDTO&gt; </span>[<span
class="see_javadocs">(see
javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/metadata/SourceDTO.html)

<div class="method-description">

**Use Case:** This method returns all versions of a given Root Source in
the Metathesaurus.

</div>

<div class="method-note rounded-content-block">

**Note:** While rare, there are certain sources that have more than one
version in the Metathesaurus. This happens occasionally when mappings
exist between 2 versions of a source. If the mapping is not updated
along with the other source content, we maintain the metadata for that
older source in the Metathesaurus.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

myArrSrc = utsMetadataService.getVersionedSources(ticket, umlsRelease,
"ICD9CM");\
 for (int i = 0; i &lt; myArrSrc.size(); i++) {\
 SourceDTO myArrSrcDTO = myArrSrc.get(i);\
 String abbreviation = myArrSrcDTO.getAbbreviation();\
 String rtSrcAbbreviation =
myArrSrcDTO.getRootSource().getAbbreviation();\
 String version = myArrSrcDTO.getVersion();\
 }

</div>

#### Sample Input (C♯):

<div class="input rounded-content-block">

Metadata.sourceDTO\[\] myArraySource =
utsMetadataService.getVersionedSources(singleUseTicket, "2012AB",
"ICD9CM");\
 for (int i = 0; i &lt; myArraySource.Length; i++)\
 {\
 Metadata.sourceDTO myArraySourceDTO = myArraySource\[i\];\
\
 string abbreviation = myArraySourceDTO.abbreviation;\
 string rootSource = myArraySourceDTO.rootSource.abbreviation;\
 string version = myArraySourceDTO.version;\
 }

</div>

#### Sample Output:

  -----------------------------------
  Abbreviation: ICD9CM\_2011\
   RootSource Abbreviation: ICD9CM\
   Version: 2011\
   Abbreviation: ICD9CM\_2005\
   RootSource Abbreviation: ICD9CM\
   Version: 2005\
   Abbreviation: ICD9CM\_1998\
   RootSource Abbreviation: ICD9CM\
   Version: 1998\
   Abbreviation: ICD9CM\_2012\
   RootSource Abbreviation: ICD9CM\
   Version: 2012\
  -----------------------------------

</div>

<div id="getCurrentVersionSource" class="method rounded-content-block">

**Method: **<span
class="method-name">getCurrentVersionSource</span><span
class="method-parameters">(String ticket,String version,String
rootSourceAbbreviation)</span>
**Returns:** <span class="method-return-type">SourceDTO </span>[<span
class="see_javadocs">(see
javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/metadata/SourceDTO.html)

<div class="method-description">

**Use Case:** Given a UMLS release and root source abbreviation (RSAB),
this call returns details of the version of the root source contained by
the given UMLS release, as well as the original version that appeared in
the UMLS.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

mySrcDTO = utsMetadataService.getCurrentVersionSource(ticket,
umlsRelease, "LNC");\
\
 String abbreviation = mySrcDTO.getAbbreviation();\
 String version = mySrcDTO.getVersion();\
 String rtSrcAbbreviation = mySrcDTO.getRootSource().getAbbreviation();\

</div>

#### Sample Input (C♯):

<div class="input rounded-content-block">

Metadata.sourceDTO mySourceDTO =
utsMetadataService.getCurrentVersionSource(singleUseTicket, "2012AB",
"LNC");\
\
 string abbreviation = mySourceDTO.abbreviation;\
 string rootSource = mySourceDTO.rootSource.abbreviation;\
 string version = mySourceDTO.version;\

</div>

#### Sample Output:

  --------------------------------
  Abbreviation: LNC215\
   Version: 215\
   RootSource Abbreviation: LNC\
  --------------------------------

</div>

<div id="getUpdatedSourcesByVersion"
class="method rounded-content-block">

**Method: **<span
class="method-name">getUpdatedSourcesByVersion</span><span
class="method-parameters">(String ticket,String version)</span>
**Returns:** <span
class="method-return-type">ArrayList&lt;SourceDTO&gt; </span>[<span
class="see_javadocs">(see
javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/metadata/SourceDTO.html)

<div class="method-description">

**Use Case:** This method retrieves all the sources that have been
updated in a given UMLS release.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

myArrSrc = utsMetadataService.getUpdatedSourcesByVersion(ticket,
umlsRelease);\
\
 for (int i = 0; i &lt; myArrSrc.size(); i++) {\
 SourceDTO myArrSrcDTO = myArrSrc.get(i);\
 String abbreviation = myArrSrcDTO.getAbbreviation();\
 String rtSrcAbbr = myArrSrcDTO.getRootSource().getAbbreviation();\
 String rtSrcExpForm = myArrSrcDTO.getRootSource().getExpandedForm();\
 String version = myArrSrcDTO.getVersion();\
 }\

</div>

#### Sample Output:

+--------------------------------------------------------------------------+
|   Abbreviation                       RootSource Abbreviation   RootSourc |
| e ExpandedForm                                                           |
|                                                            Version       |
|   ---------------------------------- ------------------------- --------- |
| ------------------------------------------------------------------------ |
| ---------------------------------------------------------- ------------- |
| -------------                                                            |
|   CPT2013                            CPT                       Current P |
| rocedural Terminology, 2013                                              |
|                                                            2013          |
|   GS\_2013\_02\_01                   GS                        Gold Stan |
| dard Drug Database, 2013\_02\_01                                         |
|                                                            2013\_02\_01  |
|   HCDT2013                           HCDT                      Current D |
| ental Terminology (CDT), 2013                                            |
|                                                            2013          |
|   HCPCS2013                          HCPCS                     Healthcar |
| e Common Procedure Coding System, 2013                                   |
|                                                            2013          |
|   HCPT2013                           HCPT                      HCPCS Ver |
| sion of Current Procedural Terminology (CPT), 2013                       |
|                                                            2013          |
|   ICD10CM\_2013                      ICD10CM                   Internati |
| onal Classification of Diseases, 10th Edition, Clinical Modification, 20 |
| 13                                                         2013          |
|   ICD10PCS\_2013                     ICD10PCS                  ICD-10-PC |
| S, 2013                                                                  |
|                                                            2013          |
|   ICD9CM\_2013\_2012\_08\_06         ICD9CM                    Internati |
| onal Classification of Diseases, Ninth Revision, Clinical Modification,  |
| 2013\_2012\_08\_06                                         2013\_2012\_0 |
| 8\_06                                                                    |
|   LNC242                             LNC                       LOINC, 24 |
| 2                                                                        |
|                                                            242           |
|   LNC242\_AD8\_2005                  LNC\_AD8                  AD8:Eight |
| -item Informant Interview to Differentiate Aging and Dementia, 242\_2005 |
|                                                            242\_2005     |
|   LNC242\_ASQ\_3\_2009               LNC\_ASQ\_3               Ages & St |
| ages Questionnaire, 242\_2009                                            |
|                                                            242\_2009     |
|   LNC242\_BRADEN\_1988               LNC\_BRADEN               Braden Sc |
| ale for Predicting Pressure Sore Risk, 242\_1988                         |
|                                                            242\_1988     |
|   LNC242\_CAM\_2003                  LNC\_CAM                  Confusion |
|  Assessment Method (CAM), 242\_2003                                      |
|                                                            242\_2003     |
|   LNC242\_FACIT                      LNC\_FACIT                Functiona |
| l Assessment of Chronic Illness Therapy (FACIT) Measurement System, 242  |
|                                                            242           |
|   LNC242\_FLACC\_1997                LNC\_FLACC                Faces, Le |
| gs, Activity, Cry and Consolability (FLACC) Scale, 242\_1997             |
|                                                            242\_1997     |
|   LNC242\_MDS20                      LNC\_MDS20                Minimum D |
| ata Set, 2.0, 242\_20                                                    |
|                                                            242\_20       |
|   LNC242\_MDS30                      LNC\_MDS30                Minimum D |
| ata Set, 3.0, 242\_30                                                    |
|                                                            242\_30       |
|   LNC242\_MLHFQ\_1986                LNC\_MLHFQ                Minnesota |
|  Living with Heart Failure Questionnaire (MLHFQ), 242\_1986              |
|                                                            242\_1986     |
|   LNC242\_NEUROQOL\_2010             LNC\_NEUROQOL             Quality o |
| f Life Outcomes in Neurological Disorders, 242\_2010                     |
|                                                            242\_2010     |
|   LNC242\_NPUAP\_2012                LNC\_NPUAP                Pressure  |
| Ulcer Stages, 242                                                        |
|                                                            242\_2012     |
|   LNC242\_OASIS\_2002                LNC\_OASIS                Outcome a |
| nd Assessment Information Set, 242\_2002                                 |
|                                                            242\_2002     |
|   LNC242\_OPTIMAL\_2005              LNC\_OPTIMAL              Outpatien |
| t Physical Therapy Improvement in Movement Assessment Log, 242\_2005     |
|                                                            242\_2005     |
|   LNC242\_PHQ\_9\_1999               LNC\_PHQ\_9               Patient H |
| ealth Questionnaire, 242\_1999                                           |
|                                                            242\_1999     |
|   LNC242\_RHO\_2008                  LNC\_RHO                  Routine H |
| ealth Outcomes Ltd. (RHO), 242\_2008                                     |
|                                                            242\_2008     |
|   LNC242\_SPERTUS\_2005              LNC\_SPERTUS              John Sper |
| tus MD MPH, 242\_2005                                                    |
|                                                            242\_2005     |
|   LNC242\_VR\_12\_2004               LNC\_VR\_12               Veterans  |
| RAND 12 Item Health Survey (VR-12), 242\_2004                            |
|                                                            242\_2004     |
|   LNC242\_WHO\_2006                  LNC\_WHO                  Patient M |
| onitoring Guidelines for HIV care and antiretroviral therapy (ART), 242\ |
| _2006                                                      242\_2006     |
|   MBD13                              MBD                       MEDLINE ( |
| 2003-2007)                                                               |
|                                                            13            |
|   MDDB\_2013\_01\_30                 MDDB                      Master Dr |
| ug Data Base, 2013\_01\_30                                               |
|                                                            2013\_01\_30  |
|   MDR15\_1                           MDR                       Medical D |
| ictionary for Regulatory Activities Terminology (MedDRA), 15.1           |
|                                                            15.1          |
|   MDRCZE15\_1                        MDRCZE                    Medical D |
| ictionary for Regulatory Activities Terminology (MedDRA), Czech Edition, |
|  15.1                                                      15.1          |
|   MDRDUT15\_1                        MDRDUT                    Medical D |
| ictionary for Regulatory Activities Terminology (MedDRA), Dutch Edition, |
|  15.1                                                      15.1          |
|   MDRFRE15\_1                        MDRFRE                    Medical D |
| ictionary for Regulatory Activities Terminology (MedDRA), French Edition |
| , 15.1                                                     15.1          |
|   MDRGER15\_1                        MDRGER                    Medical D |
| ictionary for Regulatory Activities Terminology (MedDRA), German Edition |
| , 15.1                                                     15.1          |
|   MDRHUN15\_1                        MDRHUN                    Medical D |
| ictionary for Regulatory Activities Terminology (MedDRA), Hungarian Edit |
| ion, 15.1                                                  15.1          |
|   MDRITA15\_1                        MDRITA                    Medical D |
| ictionary for Regulatory Activities Terminology (MedDRA), Italian Editio |
| n, 15.1                                                    15.1          |
|   MDRJPN15\_1                        MDRJPN                    Medical D |
| ictionary for Regulatory Activities Terminology (MedDRA), Japanese Editi |
| on, 15.1                                                   15.1          |
|   MDRPOR15\_1                        MDRPOR                    Medical D |
| ictionary for Regulatory Activities Terminology (MedDRA), Portuguese Edi |
| tion, 15.1                                                 15.1          |
|   MDRSPA15\_1                        MDRSPA                    Medical D |
| ictionary for Regulatory Activities Terminology (MedDRA), Spanish Editio |
| n, 15.1                                                    15.1          |
|   MED13                              MED                       MEDLINE ( |
| 2008-2013)                                                               |
|                                                            13            |
|   MEDCIN3\_2012\_12\_14              MEDCIN                    MEDCIN, 3 |
| \_2012\_12\_14                                                           |
|                                                            3\_2012\_12\_ |
| 14                                                                       |
|   MEDLINEPLUS\_20130221              MEDLINEPLUS               MedlinePl |
| us Health Topics, 20130221                                               |
|                                                            20130221      |
|   MMSL\_2013\_02\_01                 MMSL                      Multum Me |
| diSource Lexicon, 2013\_02\_01                                           |
|                                                            2013\_02\_01  |
|   MMX\_2013\_02\_04                  MMX                       Micromede |
| x RED BOOK, 2013\_02\_04                                                 |
|                                                            2013\_02\_04  |
|   MSH2013\_2013\_01\_21              MSH                       Medical S |
| ubject Headings, 2013\_2013\_01\_21                                      |
|                                                            2013\_2013\_0 |
| 1\_21                                                                    |
|   MSHCZE2013                         MSHCZE                    Czech tra |
| nslation of the Medical Subject Headings, 2013                           |
|                                                            2013          |
|   MSHFRE2013                         MSHFRE                    Thesaurus |
|  Biomedical Francais/Anglais (French translation of the Medical Subject  |
| Headings), 2013                                            2013          |
|   MSHGER2013                         MSHGER                    German tr |
| anslation of the Medical Subject Headings, 2013                          |
|                                                            2013          |
|   MSHITA2013                         MSHITA                    Italian t |
| ranslation of the Medical Subject Headings, 2013                         |
|                                                            2013          |
|   MSHNOR2013                         MSHNOR                    Medical S |
| ubject Headings Norwegian, 2013                                          |
|                                                            2013          |
|   MSHPOL2013                         MSHPOL                    Polish tr |
| anslation of the Medical Subject Headings, 2013                          |
|                                                            2013          |
|   MSHPOR2013                         MSHPOR                    Descritor |
| es em Ciencias da Saude (Portuguese translation of the Medical Subject H |
| eadings), 2013                                             2013          |
|   MSHRUS2013                         MSHRUS                    Russian t |
| ranslation of the Medical Subject Headings, 2013                         |
|                                                            2013          |
|   MSHSCR2013                         MSHSCR                    Croatian  |
| translation of the Medical Subject Headings, 2013                        |
|                                                            2013          |
|   MSHSPA2013                         MSHSPA                    Descritor |
| es en Ciencias de la Salud (Spanish translation of the Medical Subject H |
| eadings), 2013                                             2013          |
|   MTHCH2013                          MTHCH                     Metathesa |
| urus CPT Hierarchical Terms, 2013                                        |
|                                                            2013          |
|   MTHFDA\_2011\_06\_01\_13\_03\_04   MTHFDA                    Metathesa |
| urus FDA National Drug Code Directory, 2011\_06\_01\_13\_03\_04          |
|                                                            2011\_06\_01\ |
| _13\_03\_04                                                              |
|   MTHHH2013                          MTHHH                     Metathesa |
| urus HCPCS Hierarchical Terms, 2013                                      |
|                                                            2013          |
|   MTHICD9\_2013\_2012\_08\_06        MTHICD9                   Internati |
| onal Classification of Diseases, Ninth Revision, Clinical Modification,  |
| Metathesaurus additional entry terms, 2013\_2012\_08\_06   2013\_2012\_0 |
| 8\_06                                                                    |
|   MTHSPL\_2013\_02\_26               MTHSPL                    Metathesa |
| urus FDA Structured Product Labels, 2013\_02\_26                         |
|                                                            2013\_02\_26  |
|   NDDF\_2013\_02\_06                 NDDF                      FDB MedKn |
| owledge (formerly NDDF Plus), 2013\_02\_06                               |
|                                                            2013\_02\_06  |
|   NDFRT\_2013\_02\_04                NDFRT                     National  |
| Drug File, 2013\_02\_04                                                  |
|                                                            2013\_02\_04  |
|   NEU2012\_08\_23                    NEU                       NeuroName |
| s, 2012\_08\_23                                                          |
|                                                            2012\_08\_23  |
|   RXNORM\_12AB\_130304F              RXNORM                    RxNorm Vo |
| cabulary, 12AB\_130304F                                                  |
|                                                            12AB\_130304F |
|   SCTSPA\_2012\_10\_31               SCTSPA                    SNOMED Cl |
| inical Terms, Spanish Language Edition, 2012\_10\_31                     |
|                                                            2012\_10\_31  |
|   SCTUSX\_2013\_03\_01               SCTUSX                    US Extens |
| ion to SNOMED CT(R), 2013\_03\_01                                        |
|                                                            2013\_03\_01  |
|   SNOMEDCT\_2013\_01\_31             SNOMEDCT                  SNOMED Cl |
| inical Terms, 2013\_01\_31                                               |
|                                                            2013\_01\_31  |
|   SOP5                               SOP                       Source of |
|  Payment Typology, 5                                                     |
|                                                            5             |
|   UMD2013                            UMD                       UMDNS: pr |
| oduct category thesaurus, 2013                                           |
|                                                            2013          |
|   VANDF\_2013\_01\_15                VANDF                     Veterans  |
| Health Administration National Drug File, 2013\_01\_15                   |
|                                                            2013\_01\_15  |
+--------------------------------------------------------------------------+

</div>

<div id="getSource" class="method rounded-content-block">

**Method: **<span class="method-name">getSource</span><span
class="method-parameters">(String ticket,String version,String
versionedSourceAbbreviation)</span>
**Returns:** <span class="method-return-type">SourceDTO </span>[<span
class="see_javadocs">(see
javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/metadata/SourceDTO.html)

<div class="method-description">

**Use Case:** Given a UMLS release and versioned source abbreviation
(VSAB), this call returns details of the version of the root source.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

mySrcDTO = utsMetadataService.getSource(ticket, umlsRelease,
"ICD9CM\_1998");\
\
 String abbreviation = mySrcDTO.getAbbreviation();\
 String version = mySrcDTO.getVersion();\
 String rtSrcAbbreviation = mySrcDTO.getRootSource().getAbbreviation();\

</div>

#### Sample Input (C♯):

<div class="input rounded-content-block">

Metadata.sourceDTO mySourceDTO =
utsMetadataService.getSource(singleUseTicket, "2012AA",
"ICD9CM\_1998");\
\
 string abbreviation = mySourceDTO.abbreviation;\
 string rootSource = mySourceDTO.rootSource.abbreviation;\
 string version = mySourceDTO.version;\

</div>

#### Sample Output:

  -----------------------------------
  Abbreviation: ICD9CM\_1998\
   Version: 1998\
   RootSource Abbreviation: ICD9CM\
  -----------------------------------

</div>

<div id="getAllSources" class="method rounded-content-block">

**Method: **<span class="method-name">getAllSources</span><span
class="method-parameters">(String ticket,String version)</span>
**Returns:** <span
class="method-return-type">ArrayList&lt;SourceDTO&gt; </span>[<span
class="see_javadocs">(see
javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/metadata/SourceDTO.html)

<div class="method-description">

**Use Case:** Given a UMLS release, this call returns details of all
valid sources for the given release.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

myArrSrc = utsMetadataService.getAllSources(ticket, umlsRelease);\
\
 for (int i = 0; i &lt; myArrSrc.size(); i++) {\
 SourceDTO myArrSrcDTO = myArrSrc.get(i);\
 String abbreviation = myArrSrcDTO.getAbbreviation();\
 String rtSrcAbbreviation =
myArrSrcDTO.getRootSource().getAbbreviation();\
 String version = myArrSrcDTO.getVersion();\
 }

</div>

#### Sample Input (C♯):

<div class="input rounded-content-block">

Metadata.sourceDTO\[\] myArraySource =
utsMetadataService.getAllSources(singleUseTicket, "2012AB");\
 for (int i = 0; i &lt; myArraySource.Length; i++)\
 {\
 Metadata.sourceDTO myArraySourceDTO = myArraySource\[i\];\
\
 string abbreviation = myArraySourceDTO.abbreviation;\
 string rootSource = myArraySourceDTO.rootSource.abbreviation;\
 string version = myArraySourceDTO.version;\
 }

</div>

#### Sample Output:

+--------------------------------------------------------------------------+
|   Abbreviation             Root Source Abbreviation   Version            |
|   ------------------------ -------------------------- ------------------ |
| --                                                                       |
|   ALT2009                  ALT                        2009               |
|   AOD2000                  AOD                        2000               |
|   AOT2003                  AOT                        2003               |
|   BI98                     BI                         1.0                |
|   CCPSS99                  CCPSS                      1999               |
|   CCS2005                  CCS                        2005               |
|   CHV2010\_10              CHV                        2010\_10           |
|   COSTAR\_89-95            COSTAR                     89-95              |
|   CPM2003                  CPM                        2003               |
|   CPT01SP                  CPTSP                      2001               |
|   CPT2005                  CPT                        2005               |
|   CPT2011                  CPT                        2011               |
|   CSP2006                  CSP                        2006               |
|   CST95                    CST                        1995               |
|   DDB00                    DDB                        2000               |
|   DMDICD10\_1995           DMDICD10                   1995               |
|   DMDUMD\_1996             DMDUMD                     1996               |
|   DSM3R\_1987              DSM3R                      1987               |
|   DSM4\_1994               DSM4                       1994               |
|   DXP94                    DXP                        1994               |
|   FMA3\_1                  FMA                        3\_1               |
|   GO2011\_06\_01           GO                         2011\_06\_01       |
|   GS\_2011\_08\_02         GS                         2011\_08\_02       |
|   HCDT2011-2012            HCDT                       2011-2012          |
|   HCPCS2011                HCPCS                      2011               |
|   HCPT2011                 HCPT                       2011               |
|   HHC2003                  HHC                        2003               |
|   HL7V2.5\_2003\_08\_30    HL7V2.5                    2003\_08\_30       |
|   HL7V3.0\_2006\_05        HL7V3.0                    2006\_05           |
|   HLREL\_1998              HLREL                      1998               |
|   HUGO2011\_05             HUGO                       2011\_05           |
|   ICD10AE\_1998            ICD10AE                    1998               |
|   ICD10AMAE\_2000          ICD10AMAE                  2000               |
|   ICD10AM\_2000            ICD10AM                    2000               |
|   ICD10CM\_2011\_01        ICD10CM                    2011\_01           |
|   ICD10DUT\_200403         ICD10DUT                   200403             |
|   ICD10PCS\_2011           ICD10PCS                   2011               |
|   ICD10\_1998              ICD10                      1998               |
|   ICD9CM\_1998             ICD9CM                     1998               |
|   ICD9CM\_2005             ICD9CM                     2005               |
|   ICD9CM\_2011             ICD9CM                     2011               |
|   ICD9CM\_2012             ICD9CM                     2012               |
|   ICF-CY\_2008             ICF-CY                     2008               |
|   ICF\_2008\_12\_19        ICF                        2008\_12\_19       |
|   ICNP\_2011               ICNP                       2011               |
|   ICPC2EDUT\_200203        ICPC2EDUT                  200203             |
|   ICPC2EENG\_200203        ICPC2EENG                  200203             |
|   ICPC2ICD10DUT\_200412    ICPC2ICD10DUT              200412             |
|   ICPC2ICD10ENG\_200412    ICPC2ICD10ENG              200412             |
|   ICPC2P\_2005             ICPC2P                     2005               |
|   ICPC93                   ICPC                       1993               |
|   ICPCBAQ\_1993            ICPCBAQ                    1993               |
|   ICPCDAN\_1993            ICPCDAN                    1993               |
|   ICPCDUT\_1993            ICPCDUT                    1993               |
|   ICPCFIN\_1993            ICPCFIN                    1993               |
|   ICPCFRE\_1993            ICPCFRE                    1993               |
|   ICPCGER\_1993            ICPCGER                    1993               |
|   ICPCHEB\_1993            ICPCHEB                    1993               |
|   ICPCHUN\_1993            ICPCHUN                    1993               |
|   ICPCITA\_1993            ICPCITA                    1993               |
|   ICPCNOR\_1993            ICPCNOR                    1993               |
|   ICPCPOR\_1993            ICPCPOR                    1993               |
|   ICPCSPA\_1993            ICPCSPA                    1993               |
|   ICPCSWE\_1993            ICPCSWE                    1993               |
|   JABL99                   JABL                       1999               |
|   KCD5\_2008               KCD5                       2008               |
|   LCH90                    LCH                        1990               |
|   LNC215                   LNC                        215                |
|   LNC236                   LNC                        236                |
|   LNC236\_BRADEN\_1988     LNC\_BRADEN                236\_1988          |
|   LNC236\_CAM\_2003        LNC\_CAM                   236\_2003          |
|   LNC236\_FLACC\_1997      LNC\_FLACC                 236\_1997          |
|   LNC236\_MDS20            LNC\_MDS20                 236\_20            |
|   LNC236\_MDS30            LNC\_MDS30                 236\_30            |
|   LNC236\_OASIS\_2002      LNC\_OASIS                 236\_2002          |
|   LNC236\_PHQ\_9\_1999     LNC\_PHQ\_9                236\_1999          |
|   LNC236\_RHO\_2008        LNC\_RHO                   236\_2008          |
|   LNC236\_WHO\_2006        LNC\_WHO                   236\_2006          |
|   MBD11                    MBD                        11                 |
|   MCM92                    MCM                        1992               |
|   MDDB\_2011\_08\_03       MDDB                       2011\_08\_03       |
|   MDR14\_0                 MDR                        14.0               |
|   MDRCZE14\_0              MDRCZE                     14.0               |
|   MDRDUT14\_0              MDRDUT                     14.0               |
|   MDRFRE14\_0              MDRFRE                     14.0               |
|   MDRGER14\_0              MDRGER                     14.0               |
|   MDRHUN14\_0              MDRHUN                     14.0               |
|   MDRITA14\_0              MDRITA                     14.0               |
|   MDRJPN14\_0              MDRJPN                     14.0               |
|   MDRPOR14\_0              MDRPOR                     14.0               |
|   MDRSPA14\_0              MDRSPA                     14.0               |
|   MED11                    MED                        11                 |
|   MEDCIN3\_2011\_07\_11    MEDCIN                     3\_2011\_07\_11    |
|   MEDLINEPLUS\_20110108    MEDLINEPLUS                20110108           |
|   MMSL\_2011\_08\_01       MMSL                       2011\_08\_01       |
|   MMX\_2011\_08\_01        MMX                        2011\_08\_01       |
|   MSH2012\_2011\_09\_09    MSH                        2012\_2011\_09\_09 |
|   MSHCZE2011               MSHCZE                     2011               |
|   MSHDUT2005               MSHDUT                     2005               |
|   MSHFIN2008               MSHFIN                     2008               |
|   MSHFRE2011               MSHFRE                     2011               |
|   MSHGER2011               MSHGER                     2011               |
|   MSHITA2011               MSHITA                     2011               |
|   MSHJPN2011               MSHJPN                     2011               |
|   MSHLAV2011               MSHLAV                     2011               |
|   MSHPOL2011               MSHPOL                     2011               |
|   MSHPOR2011               MSHPOR                     2011               |
|   MSHRUS2011               MSHRUS                     2011               |
|   MSHSCR2011               MSHSCR                     2011               |
|   MSHSPA2011               MSHSPA                     2011               |
|   MSHSWE2010               MSHSWE                     2010               |
|   MTH                      MTH                        MTH                |
|   MTHCH2011                MTHCH                      2011               |
|   MTHFDA\_2011\_06\_01     MTHFDA                     2011\_06\_01       |
|   MTHHH2011                MTHHH                      2011               |
|   MTHHL7V2.5\_2003\_08     MTHHL7V2.5                 2003\_08           |
|   MTHICD9\_2012            MTHICD9                    2012               |
|   MTHICPC2EAE\_200203      MTHICPC2EAE                200203             |
|   MTHICPC2ICD107B\_0412    MTHICPC2ICD107B            0412               |
|   MTHICPC2ICD10AE\_0412    MTHICPC2ICD10AE            0412               |
|   MTHMST2001               MTHMST                     2001               |
|   MTHMSTFRE\_2001          MTHMSTFRE                  2001               |
|   MTHMSTITA\_2001          MTHMSTITA                  2001               |
|   MTHSPL\_2011\_08\_26     MTHSPL                     2011\_08\_26       |
|   NAN2004                  NAN                        2004               |
|   NCBI2011\_05\_11         NCBI                       2011\_05\_11       |
|   NCI2011\_02D             NCI                        2011\_02D          |
|   NCISEER\_1999            NCISEER                    1999               |
|   NDDF\_2011\_08\_03       NDDF                       2011\_08\_03       |
|   NDFRT\_2011\_09\_06      NDFRT                      2011\_09\_06       |
|   NEU99                    NEU                        1999               |
|   NIC2005                  NIC                        2005               |
|   NLM-MED                  NLM-MED                    NLM-MED            |
|   NOC3                     NOC                        3rd Edition        |
|   OMIM2011\_06\_08         OMIM                       2011\_06\_08       |
|   OMS2005                  OMS                        2005               |
|   PCDS97                   PCDS                       1997               |
|   PDQ2007\_02              PDQ                        2007\_02           |
|   PNDS2011                 PNDS                       2011               |
|   PPAC98                   PPAC                       1998               |
|   PSY2004                  PSY                        2004               |
|   QMR96                    QMR                        1996               |
|   RAM99                    RAM                        1999               |
|   RCD99                    RCD                        1999               |
|   RCDAE\_1999              RCDAE                      1999               |
|   RCDSA\_1999              RCDSA                      1999               |
|   RCDSY\_1999              RCDSY                      1999               |
|   RXNORM\_11AA\_110906F    RXNORM                     11AA\_110906F      |
|   SCTSPA\_2011\_04\_30     SCTSPA                     2011\_04\_30       |
|   SNM2                     SNM                        2                  |
|   SNMI98                   SNMI                       1998               |
|   SNOMEDCT\_2010\_07\_31   SNOMEDCT                   2010\_07\_31       |
|   SNOMEDCT\_2011\_01\_31   SNOMEDCT                   2011\_01\_31       |
|   SNOMEDCT\_2011\_07\_31   SNOMEDCT                   2011\_07\_31       |
|   SPN2003                  SPN                        2003               |
|   SRC                      SRC                        SRC                |
|   TKMT2011                 TKMT                       2011               |
|   ULT93                    ULT                        1993               |
|   UMD2011                  UMD                        2011               |
|   USPMG\_2004              USPMG                      2004               |
|   UWDA173                  UWDA                       1.7.3              |
|   VANDF\_2011\_07\_29      VANDF                      2011\_07\_29       |
|   WHO97                    WHO                        1997               |
|   WHOFRE\_1997             WHOFRE                     1997               |
|   WHOGER\_1997             WHOGER                     1997               |
|   WHOPOR\_1997             WHOPOR                     1997               |
|   WHOSPA\_1997             WHOSPA                     1997               |
+--------------------------------------------------------------------------+
