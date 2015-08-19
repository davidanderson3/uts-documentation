title=Metadata
date=2015-08-20
updated=2015-08-20
type=page
status=unpublished
category=Metadata
navorder=4
~~~~~~


The UtsWsMetadataController object allows access to UMLS Metadata. This
can be very useful for answering questions such as:

-   What kind of term types, attributes or relationships are associated
    with a given source?
-   What foreign languages are in this version (or previous version) of
    the UMLS Metathesaurus?
-   What are all the sources associated with a given UMLS Metathesaurus
    release?
-   What are the expanded forms (human readable) of term type and
    attribute abbreviations?

In order to make calls on Metathesaurus Metadata, you must create
reference variables, and instantiate them, for the
UtsWsMetadataController and UtsWsSecurityController objects somewhere in
your code.
<div class="code rounded-content-block">

<span class="code-comment">//create the reference variables</span>\
 private UtsWsMetadataController utsMetadataService;\
 private UtsWsSecurityController utsSecurityService;\
\
<span class="code-comment">//instantiate and handshake</span>\
 try {\
 utsMetadataService = (new UtsWsMetadataControllerImplService())\
 .getUtsWsMetadataControllerImplPort();\
\
 utsSecurityService = (new UtsWsSecurityControllerImplService())\
 .getUtsWsSecurityControllerImplPort();\
 }\
\
 catch (Exception e) {\
 System.out.println("Error!!!" + e.getMessage());\
 }\

</div>

\
 All the methods below are called on the utsMetadataService object
created in the code sample above.
\
### UMLS Version Metadata <span class="nav">[return to top of page](#metadata)</span>

<div class="group rounded-content-block">

<div id="getCurrentUMLSVersion" class="method rounded-content-block">

**Method: **<span class="method-name">getCurrentUMLSVersion</span><span
class="method-parameters">(String ticket)</span>
**Returns:** <span class="method-return-type">String </span>

<div class="method-description">

**Use Case:** This method allows the user to retrieve the current UMLS
release, given a single use ticket.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

myarrStringMetadata = utsMetadataService.getCurrentUMLSVersion(ticket);\
 System.out.println(myarrStringMetadata);\

</div>

#### Sample Input (C♯):

<div class="input rounded-content-block">

string myStringMetadata =
utsMetadataService.getCurrentUMLSVersion(singleUseTicket);

</div>

#### Sample Output:

  -------------------------------
  The current UMLS Version is:\
   2012AB\
  -------------------------------

</div>

<div id="getAllUMLSVersions" class="method rounded-content-block">

**Method: **<span class="method-name">getAllUMLSVersions</span><span
class="method-parameters">(String ticket)</span>
**Returns:** <span class="method-return-type">String </span>

<div class="method-description">

**Use Case:** This method allows the user to retrieve a list of all UMLS
releases available, given a single use ticket.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

myarrStringMetadata = utsMetadataService.getAllUMLSVersions(ticket);\
 System.out.println(myarrStringMetadata);\

</div>

#### Sample Input (C♯):

<div class="input rounded-content-block">

string myStringMetadata =
utsMetadataService.getAllUMLSVersions(singleUseTicket);\

</div>

#### Sample Output:

  -----------------------------------
  All available UMLS Versions are:\
   2012AB\
   2012AA\
   2011AA\
   2011AB\
   2010AB\
   2010AA\
   2009AB\
   2009AA\
   2008AB\
   2008AA\
  -----------------------------------

</div>

</div>

\

### Characterset Metadata <span class="nav">[return to top of page](#metadata)</span>

<div class="group rounded-content-block">

</div>

\
### Co-occurrenceType Metadata <span class="nav">[return to top of page](#metadata)</span>

<div class="group rounded-content-block">

<div id="getCooccurrenceType" class="method rounded-content-block">

**Method: **<span class="method-name">getCooccurrenceType</span><span
class="method-parameters">(String ticket,String version,String
cooccurrenceType)</span>
**Returns:** <span
class="method-return-type">CooccurrenceTypeDTO </span>[<span
class="see_javadocs">(see
javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/metadata/CooccurrenceTypeDTO.html)

<div class="method-description">

**Use Case:** Given a UMLS release and co-occurrence type abbreviation
(COT), this call returns the expanded form of the co-occurrence type as
well as the co-occurrence type abbreviation.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

myCoocTyp = utsMetadataService.getCooccurrenceType(ticket, serviceName),
umlsRelease, "LQ");\
\
 String abbreviation = myCoocTyp.getAbbreviation();\
 String expandedForm = myCoocTyp.getExpandedForm();\

</div>

#### Sample Output:

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Abbreviation:LQ\
   ExpandedForm:second concept occurs as a MeSH topical qualifier of the first in citations to the published literature. Where CUI2 is not present, the count of citations of CUI1 with no MeSH qualifiers is reported.\
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

</div>

<div id="getAllCooccurrenceTypes" class="method rounded-content-block">

**Method: **<span
class="method-name">getAllCooccurrenceTypes</span><span
class="method-parameters">(String ticket,String version)</span>
**Returns:** <span
class="method-return-type">ArrayList&lt;CooccurrenceTypeDTO&gt; </span>[<span
class="see_javadocs">(see
javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/metadata/CooccurrenceTypeDTO.html)

<div class="method-description">

**Use Case:** Given a UMLS release, this call returns the set of all
valid co-occurrence types in the release. Each valid co-occurrence type
is returned as an object that gives its abbreviation and expanded form.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

myarrCoocTyp = utsMetadataService.getAllCooccurrenceTypes(ticket,
serviceName), umlsRelease);\
\
 for (int i = 0; i &lt; myarrCoocTyp.size(); i++) {\
 String abbreviation = myCoocTyp.getAbbreviation();\
 String expandedForm = myCoocTyp.getExpandedForm();\
 }

</div>

#### Sample Output:

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Abbreviation:KN\
   expandedForm:negative association in Knowledge Base, e.g., a finding that is inconsistent with a disease.\
   Abbreviation:KP\
   expandedForm:positive association in Knowledge Base\
   Abbreviation:L\
   expandedForm:Co-occurrence of primary or main subject headings in citations to the published literature\
   Abbreviation:LQ\
   expandedForm:second concept occurs as a MeSH topical qualifier of the first in citations to the published literature. Where CUI2 is not present, the count of citations of CUI1 with no MeSH qualifiers is reported.\
   Abbreviation:LQB\
   expandedForm:second concept is qualified by the first (a MeSH topical qualifier) in citations to the published literature\
   Abbreviation:MP\
   expandedForm:Co-occurrence of modifier and problem within a patient record\
   Abbreviation:PP\
   expandedForm:Co-occurrence of two problems within a patient record\
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

</div>

</div>

\
### General Entry Metadata <span class="nav">[return to top of page](#metadata)</span>

<div class="group rounded-content-block">

</div>

\
### IdentifierType Metadata <span class="nav">[return to top of page](#metadata)</span>

<div class="group rounded-content-block">

<div id="getIdentifierType" class="method rounded-content-block">

**Method: **<span class="method-name">getIdentifierType</span><span
class="method-parameters">(String ticket,String version,String
identifier)</span>
**Returns:** <span
class="method-return-type">IdentifierTypeDTO </span>[<span
class="see_javadocs">(see
javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/metadata/IdentifierTypeDTO.html)

<div class="method-description">

**Use Case:** Given a UMLS release and identifier type abbreviation (for
example: CUI, AUI, SCUI), this call returns the expanded form of the
identifier type, along with the abbreviation.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

myIdentifierTypeDTO = utsMetadataService.getIdentifierType(ticket,
umlsRelease, "SCUI");\
 String abbreviation = myIdentifierTypeDTO.getAbbreviation();\
 String expandedForm = myIdentifierTypeDTO.getExpandedForm();\

</div>

#### Sample Input (C♯):

<div class="input rounded-content-block">

Metadata.identifierTypeDTO myIdentifierTypeDTO =
utsMetadataService.getIdentifierType(singleUseTicket, "2012AB ", "SCUI
");\
\
 string abbreviation = myIdentifierTypeDTO.abbreviation;\
 string expandedForm = myIdentifierTypeDTO.expandedForm;\

</div>

#### Sample Output:

  ----------------------------------------------------------
  Abbreviation:SCUI\
   ExpandedForm:Source asserted concept unique identifier\
  ----------------------------------------------------------

</div>

</div>

\
### Language Metadata <span class="nav">[return to top of page](#metadata)</span>

<div class="group rounded-content-block">

<div id="getLanguage" class="method rounded-content-block">

**Method: **<span class="method-name">getLanguage</span><span
class="method-parameters">(String ticket,String version,String
language)</span>
**Returns:** <span class="method-return-type">LanguageDTO </span>[<span
class="see_javadocs">(see
javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/metadata/LanguageDTO.html)

<div class="method-description">

**Use Case:** Given a UMLS release and language abbreviation (LAT), this
call returns the full name (expanded form) of the language along with
the abbreviation.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

getLanguage(ticket, "2011AB", "DAN")

</div>

#### Sample Input (C♯):

<div class="input rounded-content-block">

utsMetadataService.getLanguage(ticket, "2011AB", "SNOMEDCT");\

</div>

#### Sample Output:

  ------------------------
  LanguageDTO\
   ClassType: Language\
   Abbreviation: DAN\
   ExpandedForm: Danish\
  ------------------------

</div>

<div id="getAllLanguages" class="method rounded-content-block">

**Method: **<span class="method-name">getAllLanguages</span><span
class="method-parameters">(String ticket,String version)</span>
**Returns:** <span
class="method-return-type">ArrayList&lt;LanguageDTO&gt; </span>[<span
class="see_javadocs">(see
javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/metadata/LanguageDTO.html)

<div class="method-description">

**Use Case:** This call returns all valid languages for a given release.
The language abbreviation and expanded form is given for each valid
language. Below is a sample of some of the over 30 languages that exist
in the UMLS as of the 2011AB release.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

getAllLanguages(ticket, "2011AB")

</div>

#### Sample Input (C♯):

<div class="input rounded-content-block">

utsMetadataService.getAllLanguages(ticket, "2011AB");\

</div>

#### Sample Output:

  ------------------------ ----------------------- ------------------------ ----------------------- ------------------------- -------------------------
  1\                       2\                      3\                       4\                      5\                        6\
   ClassType: Language\     ClassType: Language\    ClassType: Language\     ClassType: Language\    ClassType: Language\      ClassType: Language\
   Abbreviation: BAQ\       Abbreviation: CZE\      Abbreviation: DAN\       Abbreviation: DUT\      Abbreviation: ENG\        Abbreviation: FIN\
   ExpandedForm: Basque\    ExpandedForm: Czech\    ExpandedForm: Danish\    ExpandedForm: Dutch\    ExpandedForm: English\    ExpandedForm: Finnish\
                                                                                                                              
  ------------------------ ----------------------- ------------------------ ----------------------- ------------------------- -------------------------

</div>

<div id="getRootSourcesByLanguage" class="method rounded-content-block">

**Method: **<span
class="method-name">getRootSourcesByLanguage</span><span
class="method-parameters">(String ticket,String version,String
languageAbbreviation)</span>
**Returns:** <span
class="method-return-type">ArrayList&lt;RootSourceDTO&gt; </span>[<span
class="see_javadocs">(see
javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/metadata/RootSourceDTO.html)

<div class="method-description">

**Use Case:** This method retrieves all the root sources that are
provided in a particular language.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

myArrSrc = utsMetadataService.getRootSourcesByLanguage(ticket,
umlsRelease, "GER");\
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
|   Abbreviation   Restriction Level   Family   Expanded Form              |
|   -------------- ------------------- -------- -------------------------- |
| ---------------------------------------------------------------          |
|   DMDICD10       1                   ICD10    German translation of ICD1 |
| 0, 1995                                                                  |
|   DMDUMD         1                   UMD      German translation of UMDN |
| S, 1996                                                                  |
|   ICPCGER        0                   ICPC     ICPC, German Translation,  |
| 1993                                                                     |
|   MDRGER         3                   MDR      Medical Dictionary for Reg |
| ulatory Activities Terminology (MedDRA), German Edition, 15.1            |
|   MSHGER         3                   MSH      German translation of the  |
| Medical Subject Headings, 2013                                           |
|   WHOGER         2                   WHO      WHOART, German Translation |
| , 1997                                                                   |
+--------------------------------------------------------------------------+

</div>

</div>

\
### SynonymousNames Metadata <span class="nav">[return to top of page](#metadata)</span>

<div class="group rounded-content-block">

</div>

\
### Source Citation Metadata <span class="nav">[return to top of page](#metadata)</span>

<div class="group rounded-content-block">

<div id="getAllSourceCitations" class="method rounded-content-block">

**Method: **<span class="method-name">getAllSourceCitations</span><span
class="method-parameters">(String ticket,String version)</span>
**Returns:** <span
class="method-return-type">ArrayList&lt;SourceCitationDTO&gt; </span>[<span
class="see_javadocs">(see
javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/metadata/SourceCitationDTO.html)

<div class="method-description">

**Use Case:** This call returns a list of all valid source citations for
a given release. The output is a list of SourceCitationDTOs. Each
SourceCitationDTO contains a full citation and a handle.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

myarrSrcCitationDTO = utsMetadataService.getAllSourceCitations(ticket,
umlsRelease);\
\
 for (int i = 0; i &lt; myarrSrcCitationDTO.size(); i++) {\
 SourceCitationDTO mySrcCitDTO = myarrSrcCitationDTO.get(i);\
 String value = mySrcCitDTO.getValue();\
 }\

</div>

#### Sample Input (C♯):

<div class="input rounded-content-block">

Metadata.sourceCitationDTO\[\] myArraySourceCitationDTO =
utsMetadataService.getAllSourceCitations(singleUseTicket, "2012AB");\
 for (int i = 0; i &lt; myArraySourceCitationDTO.Length; i++) {\
\
 Metadata.sourceCitationDTO mySourceCitationDTO =
myArraySourceCitationDTO\[i\];\
\
 string value = mySourceCitationDTO.value;\
 }

</div>

#### Sample Output:

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Health Level Seven Vocabulary (HL7). Ann Arbor (MI): Health Level Seven, 1998-2002. Contact: Mark McDougall, Executive Director, Health Level Seven; 3300 Washtenaw Avenue, Suite 227, Ann Arbor, MI 48104-4250; Phone: (734)677-7777; Fax: (734)677-6622; Email: HQ@HL7.ORG ; Web site: www.HL7.ORG.\
  \
   HL7 Vocabulary Version 2.5, 7-bit equivalents created by the National Library of Medicine. Bethesda (MD): August 30, 2003\
  \
   United States Pharmacopeia (USP). Medicare Prescription Drug Benefit Model Guidelines: Drug Categories and Classes in Part D, 2004. http://www.usp.org/pdf/EN/mmg/comprehensiveDrugListing2004-12-31.pdf\
  \
   ICPC-2 PLUS. Sydney: Family Medicine Research Centre, University of Sydney, December 2005.\
  \
   Computer Retrieval of Information on Scientific Projects (CRISP). Bethesda (MD): National Institutes of Health, Division of Research Grants, Research Documentation Section, 2006.\
  \
   Authorized Osteopathic Thesaurus. Educational Council of Osteopathic Principles of the American Association of Colleges of Osteopathic Medicine: Chevy Chase MD, 2004;http://www.aacom.org/InfoFor/educators/Pages/thesaurus.aspx;ENG\
  \
   Nursing Interventions Classification (NIC)\
  \
   Moorhead, Sue, Johnson, Marion, Maas, Meridean, editors. Nursing Outcomes Classification (NOC): Iowa Outcomes Project. St. Louis (MO): Mosby, Inc., 2004.\
  \
   PDQ. Bethesda (MD): National Cancer Institute, February 2007.\
  \
   Martin, Karen S., Scheet, Nancy J.;The Omaha System;2005\
  \
   Finnish Translations of Medical Subject Headings (MeSH);Finnish Medical Society Duodecim;2008;Helsinki, Finland;FIN\
  \
  \
   ABC Codes and Terminology;9th;Albuquerque, NM;ABC Coding Solutions - Alternative Link;2009;ENG\
  \
   World Health Organization;International Classification of Functioning, Disability and Health;Geneva, Switzerland;World Health Organization;2008;12/19/2008;http://www.who.int/classification/icf\
  \
   World Health Organization;International Classification of Functioning, Disability and Health for Children and Youth;Geneva, Switzerland;World Health Organization;2008;http://www.who.int/classification/icf\
  \
   Korean Standard Classification of Disease Version 5;2008;Seoul, Korea;KOR\
  \
   Swedish Translation of Medical Subject Headings (MeSH);Karolinska Institutet;2010;Stockholm\
  \
   AORN;Carol Petersen;Perioperative nursing data set : the perioperative nursing vocabulary;3rd edition;Denver, CO;AORN, Inc.;2011\
  \
   Cornelius Rosse MD DSc, Jose L.V. Mejino Jr. MD\
  \
   MEDLINE Current Files (2007-2012). Bethesda (MD): National Library of Medicine. Contact: http://www.nlm.nih.gov.\
  \
   MEDLINE Backfiles (2002-2006). Bethesda (MD): National Library of Medicine. Contact: http://www.nlm.nih.gov.\
  \
   Metathesaurus Forms of FDA National Drug Code Directory;2011\_06\_01;Bethesda, MD;National Library of Medicine\
  \
   International Classification for Nursing Practice (ICNP);2011;Geneva, Switzerland;International Council of Nurses;2011\
  \
   Igaku-Chuo-Zasshi.;NPO Japan Medical Abstracts Society (JAMAS);JAMAS Japanese Medical Thesaurus (JJMT);Tokyo, Japan;2011;Japanese\
  \
   Traditional Korean Medical Terms;2011;Korea;KOR\
  \
   The Universal Medical Device Nomenclature System;ECRI;Plymouth Meeting;2012\
  \
   Health Level Seven Vocabulary (HL7). Ann Arbor (MI): Health Level Seven, 1998-2011. Contact: Mark McDougall, Executive Director, Health Level Seven; 3300 Washtenaw Avenue, Suite 227, Ann Arbor, MI 48104-4250;www.HL7.ORG.\
  \
   Consumer Health Vocabulary;2011;USA;ENG\
  \
   Centers for Medicare and Medicaid Services;ICD-10-PCS;Baltimore, MD;2012\
  \
   Current Procedural Terminology (CPT);American Medical Association;2012;Chicago (IL)\
  \
   National Library of Medicine;Metathesaurus CPT Hierarchical Terms;National Library of Medicine;2012;Bethesda, MD\
  \
   Thesaurus Biomedical Francais/Anglais \[French translation of the Medical Subject Headings\];Institut National de la Sante et Recherche Medicale;2012;Paris (France)\
  \
   BIREME/PAHO/WHO;Descritores em Ciencias da Saude \[Portuguese translation of Medical Subject Headings\];Centro Latino-Americano e do Caribe de Informaco em Ciencias da Saude;2012;Sao Paulo (Brasil)\
  \
   Russian Translation of the Medical Subject Headings;State Central Scientific Medical Library;2012;Moscow\
  \
   HCPCS Version of Current Dental Terminology 2011-2012 (CDT8);8th edition;Chicago, IL;American Dental Association;2008\
  \
   Healthcare Common Procedure Coding System (HCPCS);Baltimore, MD;Centers for Medicare & Medicaid Services;2012\
  \
   Version of Physicians' Current Procedural Terminology (CPT) included in the Healthcare Common Procedure Coding System (HCPCS);Baltimore, MD;Centers for Medicare & Medicaid Services;2012\
  \
   Metathesaurus Hierarchical HCPCS Terms;Bethesda, MD;National Library of Medicine;2012\
  \
   BIREME/PAHO/WHO;Descritores en Ciencias de la Salud \[Spanish translation of the Medical Subject Headings\];Centro Latino-Americano e do Caribe de Informacao em Ciencias da Saude;2012;Sao Paulo (Brasil)\
  \
   MedlinePlus Health Topics;National Library of Medicine;December 28, 2011;Bethesda, MD\
  \
   Dept. of Bibliography, National Library of Medicine;Czech translation of the Medical Subject Headings;Prague,Czech Republic;2012\
  \
   SabaCare,Inc.;Clinical Care Classification (CCC) System;2.5;2011;ENG\
  \
   Department of Medical Bibliography;Polish Translation of the Medical Subject Headings;Central Medical Library;2012;Warsaw, Poland\
  \
   U.S. Department of Health and Human Services, Centers for Medicare & Medicaid Services;ICD-10-CM \[computer file\]: International Classification of Diseases, Tenth Revision, Clinical Modification;December 1, 2011;Hyattsville, MD;provided for public viewing only, and not valid for use prior to October 1, 2013.\
  \
   Latvian translation of the Medical Subject Headings;Medical Library of Latvia;2012;Riga (Latvia)\
  \
   Croatian translation of the Medical Subject Headings (MeSH);Zagreb, Croatia;University of Zagreb School of Medicine - Central Medical Library;2012\
  \
   Italian translation of Medical Subject Headings;Istituto Superiore di Sanita, Settore Documentazione;2012;Rome(Itlay)\
  \
   German translation of Medical Subject Headings (MeSH);Deutsches Institut fur Medizinische Dokumentation und Information;2012;Cologne(Germany)\
  \
   Norwegian translation of the Medical Subject Headings (MeSH);2012;Oslo,Norway\
  \
   National Library of Medicine;US Extension to SNOMED CT (R);September 1, 2012;Bethesda, MD;National Library of Medicine;September 1, 2012\
  \
   UMLS Metathesaurus. Bethesda, MD: National Library of Medicine.\
  \
   UMLS Metathesaurus Source Terminologies. Bethesda, MD: National Library of Medicine.\
  \
   Medical Subject Headings (MeSH);National Library of Medicine;2011;Bethesda, MD\
  \
   Logical Observation Identifier Names and Codes (LOINC). Version 2.15. Indianapolis (IN): The Regenstrief Institute, June 6, 2005\
  \
   ICD-9-CM \[computer file\]: international classification of diseases, ninth revision, clinical modification. Version 22. Baltimore, MD: U.S. Department of Health and Human Services, Centers for Medicare & Medicaid Services, effective October 1, 2004.\
  \
   U.S. Department of Health and Human Services, Centers for Medicare & Medicaid Services;ICD-9-CM \[computer file\]: International Classification of Diseases, Ninth Revision, Clinical Modification;October 1, 2011;Baltimore, MD\
  \
   Current Procedural Terminology (CPT), 4th ed. Chicago (IL): American Medical Association, 2004. http://www.ama-assn.org\
  \
   National Library of Medicine (NLM) Medline Data. Bethesda (MD): National Library of Medicine. Contact: http://www.nlm.nih.gov.\
  \
   International Health Terminology Standards Development Organization;SNOMED Clinical Terms;July 31, 2011;Copenhagen,Denmark;International Health Terminology Standards Development Organisation (IHTSDO)\
  \
   International Health Terminology Standards Development Organization;SNOMED Clinical Terms;January 31, 2012;Copenhagen,Denmark;International Health Terminology Standards Development Organisation (IHTSDO)\
  \
   MedDRA MSSO;MedDRA \[electronic resource\] : Medical Dictionary for Regulatory Activities Terminology;Version 15.0;Chantilly, VA;March, 2012\
  \
   Medical Dictionary for Regulatory Activities Terminology (MedDRA) Version 15.0, Czech Edition;MedDRA MSSO;March, 2012\
  \
   The Gene Ontology;The Gene Ontology Consortium;April 3, 2012\
  \
   Medical Dictionary for Regulatory Activities Terminology (MedDRA) Version 15.0, Dutch Edition;MedDRA MSSO;March,2012\
  \
   National Cancer Institute, National Institutes of Health;NCI Thesaurus;National Cancer Institute;February 2012, Protege version;Rockville, MD\
  \
   Medical Dictionary for Regulatory Activities Terminology (MedDRA) Version 15.0, French Edition;MedDRA MSSO;March, 2012\
  \
   McKusick-Nathans Institute of Genetic Medicine, Johns Hopkins University (Baltimore, MD);Online Mendelian Inheritance in Man, OMIM.;McKusick-Nathans Institute for Genetic Medicine,Johns Hopkins University;May 2, 2012\
  \
   Medical Dictionary for Regulatory Activities Terminology (MedDRA) Version 15.0, German Edition;MedDRA MSSO;March, 2012\
  \
   Medical Dictionary for Regulatory Activities Terminology (MedDRA) Version 15.0, Hungarian Edition;MedDRA MSSO;March, 2012\
  \
   Medical Dictionary for Regulatory Activities Terminology (MedDRA) Version 15.0, Italian Edition;MedDRA MSSO;March, 2012\
  \
   U.S. Department of Health and Human Services;NCBI Taxonomy;National Institutes of Health, National Library of Medicine, National Center for Biotechnology Information;April 16, 2012;Bethesda, MD\
  \
   Medical Dictionary for Regulatory Activities Terminology (MedDRA) Version 15.0, Spanish Edition;MedDRA MSSO;March, 2012\
  \
   Medical Dictionary for Regulatory Activities Terminology (MedDRA) Version 15.0, Japanese Edition;MedDRA MSSO;March, 2012\
  \
   Medical Dictionary for Regulatory Activities Terminology (MedDRA) Version 15.0, Portuguese Edition;MedDRA MSSO;March, 2012\
  \
   International Health Terminology Standards Development Organisation (IHTSDO);SNOMED Terminos Clinicos (SNOMED CT), Edicion en Espanol;Spanish Language Edition;Copenhagen, Denmark;April 30, 2012\
  \
   Medicomp Systems;MEDCIN;\[terminology files\];Chantilly VA;Medicomp Systems;2012;July 16, 2012;Chantilly VA\
  \
   Eyre TA, Ducluzeau F, Sneddon TP, Povey S, Bruford EA and Lush MJ;HGNC Database;The HUGO Gene Nomenclature Database;European Bioinformatics Institute Wellcome Trust Genome Campus;May 2012;United Kingdom\
  \
   International Health Terminology Standards Development Organization;SNOMED Clinical Terms;July 31, 2012;Copenhagen,Denmark;International Health Terminology Standards Development Organisation (IHTSDO)\
  \
   The Regenstrief Institute;Logical Observation Identifier Names and Codes (LOINC);Version 2.38.;December, 2011;Indianapolis (IN)\
  \
   Institute of Gerontology;Minimum Data Set;2.0;University of Michigan;Ann Arbor, Michigan\
  \
   Institute of Gerontology;Minimum Data Set;3.0;University of Michigan;Ann Arbor, Michigan\
  \
   Pfizer Inc.;Patient Health Questionnaire (PHQ-9);1999\
  \
   The Outcome and Assessment Information Set (OASIS);Center for Health Services Research, UCHSC;2002;Denver, CO\
  \
   Barbara Braden and Nancy Bergstrom;The Braden Scale for Predicting Pressure Sore Risk;Prevention Plus;1988\
  \
   SI Merkel, T. Voepel-Lewis, J.R. Shayevitz, S. Malviya; Department of Anesthesiology, University of Michigan Medical School and Health Systems;The FLACC: A behavioral scale for scoring postoperative pain in young children;Pediatric Nursing;1997\
  \
   Patient Monitoring Guidelines for HIV care and antiretroviral therapy (ART);Geneva, Switzerland;WHO Press;2006\
  \
   Routine Health Outcomes Ltd.;Berkshire, UK;2008\
  \
   Inouye SK, VanDyck CH, Alessi CA, Balkin S, Siegal AP, Horwitz RI;Sharon K. Inouye, M.D., MPH;Clarifying confusion: The Confusion Assessment Method;113: 941-948;Ann Intern Med.;1990;Copyright 2003;Confusion Assessment Method: Training Manual and Coding Guide- A new method for detection of delirium\
  \
   American Physical Therapy Association;Outpatient Physical Therapy Improvement in Movement Assessment Log (OPTIMAL);Version 2.38.;(c)2005;Alexandria,VA\
   David Cella, PhD. Used with permission. All of these Neuro-QOL instruments can be used at no charge. We do ask, however, that you contact Neuro-QOL project manager, Vitali Ustsinovich, at v-ustsinovich@northwestern.edu and let him know that you intend to use Neuro-QOL.;Indianapolis (IN)\
  \
   David Cella, Ph.D. Questionnaires and all related\
  \
   Washington University, St. Louis, Missouri. (All Rights Reserved. Reprinted with permission.);The Eight-item Informant Interview to Differentiate Aging and Dementia;Missouri;Washington University;Copyright 2005\
   Rector, Thomas;Regents of the University of Minnesota;Living With Heart Failure;Minnesota;1986\
  \
   John Spertus,MD,MPH,FACC;Kansas City Cardiomyopathy Questionnaire;Copyright 1996-2005\
  \
   U.S. Department of Health and Human Services, Centers for Medicare & Medicaid Services;ICD-9-CM \[computer file\]: International Classification of Diseases, Ninth Revision, Clinical Modification;October 1, 2012;Baltimore, MD\
  \
   Metathesaurus additional entry terms for ICD-9-CM \[computer file\]: International Classification of Diseases, Ninth Revision, Clinical Modification;National Library of Medicine;October 1, 2012;Bethesda, MD\
  \
   Gold Standard Drug Database;302 Knights Run Ave, Suite 800, Tampa, FL 33602;Gold Standard\
  \
   Master Drug Data Base;July 04, 2012\
  \
   Medisource Lexicon;August 01, 2012;Denver, CO;Multum Information Services, Inc.\
  \
   Veterans Health Administration National Drug File;June 27, 2012;Washington, DC;U.S. Department of Veterans Affairs\
  \
   Metathesaurus Forms of the FDA Structured Product Labels;2012\_08\_28;Bethesda, MD;National Library of Medicine\
  \
   FDB MedKnowledge (formerly NDDF Plus);August 01, 2012;South San Francisco, CA;First Databank\
  \
   RxNorm;META2012AA Full Update 2012\_09\_04;Bethesda, MD;National Library of Medicine\
  \
   Micromedex RED BOOK;July 30, 2012\
  \
   National Drug File - Reference Terminology;2012\_09\_04;Washington, DC;U.S. Department Of Veterans Affairs, Veterans Health Administration\
  \
   Medical Subject Headings (MeSH);National Library of Medicine;2012;Bethesda, MD\
  \
   AI/RHEUM. Bethesda, (MD) : National Library of Medicine, Lister Hill Center, 1993.\
  \
   Coding Symbols for Thesaurus of Adverse Reaction Terms (COSTART). 5th ed. Rockville (MD): U.S. Food and Drug Administration, Center for Drug Evaluation and Research, 1995.\
  \
   DXplain (An expert diagnosis program). Boston (MA): Massachusetts General Hospital, 1994.\
  \
   Library of Congress Subject Headings. 12th ed. Washington (DC): Library of Congress, 1989.\
  \
   Glossary of Methodologic Terms for Clinical Epidemiologic Studies of Human Disorders. Canada: McMaster University, 1992.\
  \
   Cote, Roger A., editor. Systematized Nomenclature of Medicine. 2nd ed. Skokie (IL): College of American Pathologists, 1979. SNOMED update, 1982. Skokie (IL): College of American Pathologists, 1982.\
  \
   Cote, Roger A., editor. Systematized Nomenclature of Human and Veterinary Medicine: SNOMED International. Northfield (IL): College of American Pathologists; Schaumburg (IL): American Veterinary Medical Association, Version 3.5, 1998.\
  \
   WHO Adverse Drug Reaction Terminology (WHOART). Uppsala (Sweden): WHO Collaborating Centre for International Drug Monitoring, 1997.\
  \
   Bell, Douglas. Ultrasound Structured Attribute Reporting (UltraSTAR). Boston (MA): Brigham & Womens Hospital, 1993.\
  \
   Bowden, Douglas M., Martin, Richard F., Dubach, Joev G. Neuronames Brain Hierarchy. Seattle (WA): University of Washington, Primate Information Center, 1999. http://rprcsgi.rprc.washington.edu/neuronames/\
  \
   International Statistical Classification of Diseases and Related Health Problems (ICD-10). 10th rev. Geneva (Switzerland): World Health Organization, 1998.\
  \
   The International Classification of Primary Care (ICPC). Denmark: World Organisation of Family Doctors, 1993.\
  \
   Quick Medical Reference (QMR). San Bruno (CA): First DataBank, 1997.\
  \
   Clinical Terms Version 3 (CTV3) (Read Codes) (Q199): National Health Service National Coding and Classification Centre; March, 1999.\
  \
   Pharmacy Practice Activity Classification (PPAC). Version 1. Washington (DC): American Pharmaceutical Association, 1998.\
  \
   Diagnostic and Statistical Manual of Mental Disorders (DSM-III-R). 3rd ed. rev. Washington (DC): American Psychiatric Association, 1987.\
  \
   Diagnostic and Statistical Manual of Mental Disorders (DSM-IV). 4th ed. Washington (DC): American Psychiatric Association, 1994.\
  \
   Alcohol and Other Drug Thesaurus: A Guide to Concepts and Terminology in Substance Abuse and Addiction. 3rd. ed. \[4 Volumes.\] Bethesda, MD: National Institute on Alcohol Abuse and Alcoholism (NIAAA) and Center for Substance Abuse Prevention (CSAP), 2000;ENG\
  \
   Beth Israel OMR Clinical Problem List Vocabulary. Version 1.0. Boston (MA): Beth Israel Deaconess Medical Center, 1999. Contact: Howard Goldberg, MD.;http://clinquery.bidmc.harvard.edu.;ENG\
  \
   American English equivalent of the Clinical Terms Version 3 (Q1, 1999), produced by NLM. Bethesda (MD): National Library of Medicine, UMLS project, 1999.\
  \
   American English equivalent of synthesized terms from the Clinical Terms Version 3 (Q1, 1999), produced by NLM. Bethesda (MD): National Library of Medicine, UMLS project, 1999.\
  \
   Synthesized Read terms (without initial bracketed letters) of the Clinical Terms Version 3 (Q1, 1999), produced by NLM. Bethesda (MD): National Library of Medicine, UMLS project, 1999.\
  \
   International Statistical Classification of Diseases and Related Health Problems (ICD-10): Americanized Version. 10th rev. Geneva (Switzerland): World Health Organization, 1998.\
  \
   Internationale Klassifikation der Krankheiten 10 \[German translation of ICD10\]. Germany: Deutsches Institut fuer Medizinische Dokumentation und Information, 1998.\
  \
   Die Nomenklatur fuer Medizinprodukte UMDNS \[German translation of UMDNS\]. Germany: Deutsches Institut fuer Medizinische Dokumentation und Information, 1996.\
  \
   The International Classification of Primary Care (ICPC). Danish Translation. Denmark: World Organisation of Family Doctors, 1993.\
  \
   The International Classification of Primary Care (ICPC). Dutch Translation. Denmark: World Organisation of Family Doctors, 1993.\
  \
   The International Classification of Primary Care (ICPC). Finnish Translation. Denmark: World Organisation of Family Doctors, 1993.\
  \
   The International Classification of Primary Care (ICPC). French Translation. Denmark: World Organisation of Family Doctors, 1993.\
  \
   And so on...\
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

</div>

<div id="getSourceCitation" class="method rounded-content-block">

**Method: **<span class="method-name">getSourceCitation</span><span
class="method-parameters">(String ticket,String version,String
handle)</span>
**Returns:** <span
class="method-return-type">SourceCitationDTO </span>[<span
class="see_javadocs">(see
javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/metadata/SourceCitationDTO.html)

<div class="method-description">

**Use Case:** Given a UMLS release and a source citation handle, this
call returns a full citation for the supplied handle. You can retrieve a
source citation handle from the getAllSourceCitations call.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

mySrcCitationDTO = utsMetadataService.getSourceCitation(ticket,
umlsRelease, "37");\
 String value = mySrcCitationDTO.getValue();\

</div>

#### Sample Input (C♯):

<div class="input rounded-content-block">

Metadata.sourceCitationDTO mySourceCitation =
utsMetadataService.getSourceCitation(singleUseTicket, "012AB", "37");\
\
 string value = mySourceCitationDTO.value;\

</div>

#### Sample Output:

  --------------------------------------------------------------------------------------------------------------------------------------------------------------
  WHO Adverse Drug Reaction Terminology (WHOART). Portuguese Translation. Uppsala (Sweden): WHO Collaborating Centre for International Drug Monitoring, 1997.\
  --------------------------------------------------------------------------------------------------------------------------------------------------------------

</div>

</div>

\
### TermType Metadata <span class="nav">[return to top of page](#metadata)</span>

<div class="group rounded-content-block">

<div id="getTermType" class="method rounded-content-block">

**Method: **<span class="method-name">getTermType</span><span
class="method-parameters">(String ticket,String version,String
termType)</span>
**Returns:** <span class="method-return-type">TermTypeDTO </span>[<span
class="see_javadocs">(see
javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/metadata/TermTypeDTO.html)

<div class="method-description">

**Use Case:** Given a UMLS release and a term type abbreviation (TTY),
this call returns the expanded form of the term type, the abbreviation,
and the obsolete field.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

myTermTyp = utsMetadataService.getTermType(ticket, umlsRelease, "MH");\
\
 String expandedForm = myTermTyp.getExpandedForm();\
 String abbreviation = myTermTyp.getAbbreviation();\

</div>

#### Sample Input (C♯):

<div class="input rounded-content-block">

Metadata.termTypeDTO myTermType =
utsMetadataService.getTermType(singleUseTicket, "2012AB", "MH");\
\
 string expandedForm = myTermType.expandedForm;\
 string abbreviation = myTermType.abbreviation;\

</div>

#### Sample Output:

  ----------------------------
  ExpandedForm:Main heading\
   Abbreviation:MH\
  ----------------------------

</div>

<div id="getAllTermTypes" class="method rounded-content-block">

**Method: **<span class="method-name">getAllTermTypes</span><span
class="method-parameters">(String ticket,String version)</span>
**Returns:** <span
class="method-return-type">ArrayList&lt;TermTypeDTO&gt; </span>[<span
class="see_javadocs">(see
javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/metadata/TermTypeDTO.html)

<div class="method-description">

**Use Case:** Given a UMLS release, this call returns all the valid term
types for that release. The details of each returned term type include
its expanded form, abbreviation, and the obsolete field.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

myarrTermTyp = utsMetadataService.getAllTermTypes(ticket, umlsRelease);\
\
 for (int i = 0; i &lt; myarrTermTyp.size(); i++) {\
 TermTypeDTO myTermTypDTO = myarrTermTyp.get(i);\
 String expandedForm = myTermTypDTO.getExpandedForm();\
 String abbreviation = myTermTypDTO.getAbbreviation();\
 }\

</div>

#### Sample Input (C♯):

<div class="input rounded-content-block">

Metadata.termTypeDTO\[\] myArrayTermTypeDTO =
utsMetadataService.getAllTermTypes(singleUseTicket, "2012AB");\
 for (int i = 0; i &lt; myArrayTermTypeDTO.Length; i++) {\
\
 Metadata.termTypeDTO myTermTypeDTO = myArrayTermTypeDTO\[i\];\
\
 string expandedForm = myTermTypeDTO.expandedForm;\
 string abbreviation = myTermTypeDTO.abbreviation;\
 }

</div>

#### Sample Output:

+--------------------------------------------------------------------------+
|   Expanded Form                                                          |
|                                                                          |
|                     Abbreviation                                         |
|   ---------------------------------------------------------------------- |
| ------------------------------------------------------------------------ |
| ------------------- ---------------                                      |
|   Attribute type abbreviation                                            |
|                                                                          |
|                     AA                                                   |
|   Abbreviation in any source vocabulary                                  |
|                                                                          |
|                     AB                                                   |
|   Activities                                                             |
|                                                                          |
|                     AC                                                   |
|   Acronym                                                                |
|                                                                          |
|                     ACR                                                  |
|   Adjective                                                              |
|                                                                          |
|                     AD                                                   |
|   Short form of modifier                                                 |
|                                                                          |
|                     AM                                                   |
|   Attribute type synonym                                                 |
|                                                                          |
|                     AS                                                   |
|   Attribute type                                                         |
|                                                                          |
|                     AT                                                   |
|   Authority name                                                         |
|                                                                          |
|                     AUN                                                  |
|   Fully-specified drug brand name that can be prescribed                 |
|                                                                          |
|                     BD                                                   |
|   Fully-specified drug brand name that can not be prescribed             |
|                                                                          |
|                     BN                                                   |
|   Branded Drug Delivery Device                                           |
|                                                                          |
|                     BPCK                                                 |
|   Biomedical Research Integrated Domain Group Model PT                   |
|                                                                          |
|                     BRIDGPT                                              |
|   BioCarta online maps of molecular pathways, adapted for NCI use PT     |
|                                                                          |
|                     BioCPT                                               |
|   BioCarta online maps of molecular pathways, adapted for NCI use SY     |
|                                                                          |
|                     BioCSY                                               |
|   ISO 3166-1 standard country code in alpha-2 (two-letter) format        |
|                                                                          |
|                     CA2                                                  |
|   ISO 3166-1 standard country code in alpha-3 (three-letter) format      |
|                                                                          |
|                     CA3                                                  |
|   Trimmed ICPC component process                                         |
|                                                                          |
|                     CC                                                   |
|   Chemical code name                                                     |
|                                                                          |
|                     CCN                                                  |
|   FIPS 10-4 country code                                                 |
|                                                                          |
|                     CCS                                                  |
|   Clinical Drug                                                          |
|                                                                          |
|                     CD                                                   |
|   Clinical drug name in abbreviated format                               |
|                                                                          |
|                     CDA                                                  |
|   Clinical drug name in concatenated format (NDDF), Clinical drug name ( |
| NDFRT)                                                                   |
|                     CDC                                                  |
|   U.S. Centers for Disease Control and Prevention PT                     |
|                                                                          |
|                     CDCPT                                                |
|   Clinical drug name in delimited format                                 |
|                                                                          |
|                     CDD                                                  |
|   Clinical Data Interchange Standards Consortium PT                      |
|                                                                          |
|                     CDISCPT                                              |
|   Clinical Data Interchange Standards Consortium SY                      |
|                                                                          |
|                     CDISCSY                                              |
|   Entry term for a Supplementary Concept                                 |
|                                                                          |
|                     CE                                                   |
|   Chemical structure name                                                |
|                                                                          |
|                     CHN                                                  |
|   Class                                                                  |
|                                                                          |
|                     CL                                                   |
|   Common name                                                            |
|                                                                          |
|                     CMN                                                  |
|   LOINC official component name                                          |
|                                                                          |
|                     CN                                                   |
|   Component name (these are hierarchical terms, as opposed to the LOINC  |
| component names which are analytes)                                      |
|                     CO                                                   |
|   ICPC component process (in original form)                              |
|                                                                          |
|                     CP                                                   |
|   Cancer Research Center of Hawaii PT                                    |
|                                                                          |
|                     CRCHPT                                               |
|   Cancer Research Center of Hawaii SY                                    |
|                                                                          |
|                     CRCHSY                                               |
|   Short component process in ICPC, i.e. include some abbreviations       |
|                                                                          |
|                     CS                                                   |
|   Chemical Structure Name                                                |
|                                                                          |
|                     CSN                                                  |
|   Common Terminology Criteria for Adverse Events PT                      |
|                                                                          |
|                     CTCAEPT                                              |
|   Common usage                                                           |
|                                                                          |
|                     CU                                                   |
|   Content view                                                           |
|                                                                          |
|                     CV                                                   |
|   Component, with abbreviations expanded.                                |
|                                                                          |
|                     CX                                                   |
|   NCI Division of Cancer Prevention Program PT                           |
|                                                                          |
|                     DCPPT                                                |
|   NCI Division of Cancer Prevention Program SY                           |
|                                                                          |
|                     DCPSY                                                |
|   Descriptor                                                             |
|                                                                          |
|                     DE                                                   |
|   Deactivated entry term                                                 |
|                                                                          |
|                     DET                                                  |
|   Descriptor entry version                                               |
|                                                                          |
|                     DEV                                                  |
|   Dose Form                                                              |
|                                                                          |
|                     DF                                                   |
|   Disease name                                                           |
|                                                                          |
|                     DI                                                   |
|   Digital Imaging Communications in Medicine PT                          |
|                                                                          |
|                     DICOMPT                                              |
|   Display Name                                                           |
|                                                                          |
|                     DN                                                   |
|   Domain                                                                 |
|                                                                          |
|                     DO                                                   |
|   Drug Product                                                           |
|                                                                          |
|                     DP                                                   |
|   Short form of descriptor                                               |
|                                                                          |
|                     DS                                                   |
|   Descriptor sort version                                                |
|                                                                          |
|                     DSV                                                  |
|   Definitional term, present in the Metathesaurus because of its connect |
| ion to a Dorland's definition or to a definition created especially for  |
| the Metathesaurus   DT                                                   |
|   NCI Developmental Therapeutics Program PT                              |
|                                                                          |
|                     DTPPT                                                |
|   NCI Developmental Therapeutics Program SY                              |
|                                                                          |
|                     DTPSY                                                |
|   Diagnosis                                                              |
|                                                                          |
|                     DX                                                   |
|   Non-print entry term                                                   |
|                                                                          |
|                     EN                                                   |
|   Print entry term                                                       |
|                                                                          |
|                     EP                                                   |
|   Equivalent name                                                        |
|                                                                          |
|                     EQ                                                   |
|   Short form of entry term                                               |
|                                                                          |
|                     ES                                                   |
|   Entry term                                                             |
|                                                                          |
|                     ET                                                   |
|   Entry Term Allelic Variant                                             |
|                                                                          |
|                     ETAV                                                 |
|   Expanded form of entry term                                            |
|                                                                          |
|                     EX                                                   |
|   Foreign brand name                                                     |
|                                                                          |
|                     FBD                                                  |
|   U.S. Food and Drug Administration AB                                   |
|                                                                          |
|                     FDAAB                                                |
|   U.S. Food and Drug Administration PT                                   |
|                                                                          |
|                     FDAPT                                                |
|   U.S. Food and Drug Administration SY                                   |
|                                                                          |
|                     FDASY                                                |
|   Finding name                                                           |
|                                                                          |
|                     FI                                                   |
|   Full form of descriptor                                                |
|                                                                          |
|                     FN                                                   |
|   Generic drug name                                                      |
|                                                                          |
|                     GN                                                   |
|   Goal                                                                   |
|                                                                          |
|                     GO                                                   |
|   Generic Drug Delivery Device                                           |
|                                                                          |
|                     GPCK                                                 |
|   Glossary term                                                          |
|                                                                          |
|                     GT                                                   |
|   Hierarchical class                                                     |
|                                                                          |
|                     HC                                                   |
|   Hierarchical descriptor                                                |
|                                                                          |
|                     HD                                                   |
|   High Level Group Term                                                  |
|                                                                          |
|                     HG                                                   |
|   Japanese High Level Group Term (kana)                                  |
|                                                                          |
|                     HGJKN                                                |
|   Japanese High Level Group Term (kana1)                                 |
|                                                                          |
|                     HGJKN1                                               |
|   Short or alternate version of hierarchical term                        |
|                                                                          |
|                     HS                                                   |
|   Hierarchical term                                                      |
|                                                                          |
|                     HT                                                   |
|   Japanese Hierarchical term (kana)                                      |
|                                                                          |
|                     HTJKN                                                |
|   Japanese Hierarchical term (kana1)                                     |
|                                                                          |
|                     HTJKN1                                               |
|   HL7 Table Name                                                         |
|                                                                          |
|                     HTN                                                  |
|   Expanded version of short hierarchical term                            |
|                                                                          |
|                     HX                                                   |
|   International Conference on Harmonization AB                           |
|                                                                          |
|                     ICHAB                                                |
|   International Conference on Harmonization PT                           |
|                                                                          |
|                     ICHPT                                                |
|   International Conference on Harmonization SY                           |
|                                                                          |
|                     ICHSY                                                |
|   Nursing indicator                                                      |
|                                                                          |
|                     ID                                                   |
|   Name for an ingredient                                                 |
|                                                                          |
|                     IN                                                   |
|   Obsolete Synonym                                                       |
|                                                                          |
|                     IS                                                   |
|   Index term                                                             |
|                                                                          |
|                     IT                                                   |
|   Intervention                                                           |
|                                                                          |
|                     IV                                                   |
|   Intervention categories                                                |
|                                                                          |
|                     IVC                                                  |
|   Jackson Laboratories Mouse Terminology, adapted for NCI use PT         |
|                                                                          |
|                     JAXPT                                                |
|   Jackson Laboratories Mouse Terminology, adapted for NCI use SY         |
|                                                                          |
|                     JAXSY                                                |
|   Kyoto Encyclopedia of Genes and Genomes (KEGG), KEGG Pathway Database, |
|  adapted for NCI use AB                                                  |
|                     KEGGAB                                               |
|   Kyoto Encyclopedia of Genes and Genomes (KEGG), KEGG Pathway Database, |
|  adapted for NCI use PT                                                  |
|                     KEGGPT                                               |
|   Kyoto Encyclopedia of Genes and Genomes (KEGG), KEGG Pathway Database, |
|  adapted for NCI use SY                                                  |
|                     KEGGSY                                               |
|   Long common name                                                       |
|                                                                          |
|                     LC                                                   |
|   LOINC official fully specified name                                    |
|                                                                          |
|                     LN                                                   |
|   Obsolete official fully specified name                                 |
|                                                                          |
|                     LO                                                   |
|   LOINC parts display name                                               |
|                                                                          |
|                     LPDN                                                 |
|   LOINC parts name                                                       |
|                                                                          |
|                     LPN                                                  |
|   Expanded system/sample type (The expanded version was created for the  |
| Metathesaurus and includes the full name of some abbreviations.)         |
|                     LS                                                   |
|   Lower Level Term                                                       |
|                                                                          |
|                     LT                                                   |
|   Japanese Lower Level Term (kana)                                       |
|                                                                          |
|                     LTJKN                                                |
|   Japanese Lower Level Term (kana1)                                      |
|                                                                          |
|                     LTJKN1                                               |
|   Lexical variant                                                        |
|                                                                          |
|                     LV                                                   |
|   CCS multi-level diagnosis categories                                   |
|                                                                          |
|                     MD                                                   |
|   Main heading                                                           |
|                                                                          |
|                     MH                                                   |
|   name for a multi-ingredient                                            |
|                                                                          |
|                     MIN                                                  |
|   Preferred names of modifiers                                           |
|                                                                          |
|                     MP                                                   |
|   Multum names of branded and generic supplies or supplements            |
|                                                                          |
|                     MS                                                   |
|   MTH abbreviation                                                       |
|                                                                          |
|                     MTH\_AB                                              |
|   MTH acronym                                                            |
|                                                                          |
|                     MTH\_ACR                                             |
|   MTH fully-specified drug brand name that can be prescribed             |
|                                                                          |
|                     MTH\_BD                                              |
|   MTH chemical structure name                                            |
|                                                                          |
|                     MTH\_CHN                                             |
|   MTH Component, with abbreviations expanded.                            |
|                                                                          |
|                     MTH\_CN                                              |
|   MTH print entry term                                                   |
|                                                                          |
|                     MTH\_EP                                              |
|   Metathesaurus entry term                                               |
|                                                                          |
|                     MTH\_ET                                              |
|   MTH Full form of descriptor                                            |
|                                                                          |
|                     MTH\_FN                                              |
|   MTH High Level Group Term                                              |
|                                                                          |
|                     MTH\_HG                                              |
|   MTH Hierarchical term                                                  |
|                                                                          |
|                     MTH\_HT                                              |
|   Metathesaurus expanded form of nursing indicator                       |
|                                                                          |
|                     MTH\_ID                                              |
|   Metathesaurus-supplied form of obsolete synonym                        |
|                                                                          |
|                     MTH\_IS                                              |
|   MTH Official fully specified name with expanded abbreviations          |
|                                                                          |
|                     MTH\_LN                                              |
|   MTH Expanded LOINC obsolete fully specified name                       |
|                                                                          |
|                     MTH\_LO                                              |
|   MTH Lower Level Term                                                   |
|                                                                          |
|                     MTH\_LT                                              |
|   MTH lexical variant                                                    |
|                                                                          |
|                     MTH\_LV                                              |
|   MTH main heading                                                       |
|                                                                          |
|                     MTH\_MH                                              |
|   MTH non-preferred for language term                                    |
|                                                                          |
|                     MTH\_NPT                                             |
|   Metathesaurus-supplied form of obsolete fully specified name           |
|                                                                          |
|                     MTH\_OF                                              |
|   MTH Non-current Lower Level Term                                       |
|                                                                          |
|                     MTH\_OL                                              |
|   Metathesaurus obsolete preferred term                                  |
|                                                                          |
|                     MTH\_OP                                              |
|   Metathesaurus obsolete preferred term, natural language form           |
|                                                                          |
|                     MTH\_OPN                                             |
|   MTH System-organ class                                                 |
|                                                                          |
|                     MTH\_OS                                              |
|   MTH preferred entry term                                               |
|                                                                          |
|                     MTH\_PEP                                             |
|   Metathesaurus preferred term                                           |
|                                                                          |
|                     MTH\_PT                                              |
|   Metathesaurus-supplied form of British preferred term                  |
|                                                                          |
|                     MTH\_PTGB                                            |
|   Metathesaurus preferred term, natural language form                    |
|                                                                          |
|                     MTH\_PTN                                             |
|   MTH Preferred qualifier term                                           |
|                                                                          |
|                     MTH\_PXQ                                             |
|   RxNorm Created BD                                                      |
|                                                                          |
|                     MTH\_RXN\_BD                                         |
|   RxNorm Created CD                                                      |
|                                                                          |
|                     MTH\_RXN\_CD                                         |
|   RxNorm Created CDC                                                     |
|                                                                          |
|                     MTH\_RXN\_CDC                                        |
|   RxNorm Created DP                                                      |
|                                                                          |
|                     MTH\_RXN\_DP                                         |
|   RxNorm Created reference hierarchy term                                |
|                                                                          |
|                     MTH\_RXN\_RHT                                        |
|   MTH Sign or symptom of                                                 |
|                                                                          |
|                     MTH\_SI                                              |
|   Metathesaurus version of Standardised MedDRA Query                     |
|                                                                          |
|                     MTH\_SMQ                                             |
|   SN Mixed-case component synonym with expanded abbreviations            |
|                                                                          |
|                     MTH\_SN                                              |
|   MTH Designated synonym                                                 |
|                                                                          |
|                     MTH\_SY                                              |
|   Metathesaurus-supplied form of British synonym                         |
|                                                                          |
|                     MTH\_SYGB                                            |
|   MTH Topical qualifier                                                  |
|                                                                          |
|                     MTH\_TQ                                              |
|   MTH Alternate name for a qualifier                                     |
|                                                                          |
|                     MTH\_XQ                                              |
|   Multi-level procedure category                                         |
|                                                                          |
|                     MV                                                   |
|   Chemical Abstracts Service Type 1 name of a chemical                   |
|                                                                          |
|                     N1                                                   |
|   Name aliases                                                           |
|                                                                          |
|                     NA                                                   |
|   NCI Dictionary of Cancer Terms OP                                      |
|                                                                          |
|                     NCI-GLOSSOP                                          |
|   NCI Dictionary of Cancer Terms PT                                      |
|                                                                          |
|                     NCI-GLOSSPT                                          |
|   NCI Dictionary of Cancer Terms SY                                      |
|                                                                          |
|                     NCI-GLOSSSY                                          |
|   NCI Health Level 7, AB                                                 |
|                                                                          |
|                     NCI-HL7AB                                            |
|   NCI Health Level 7, PT                                                 |
|                                                                          |
|                     NCI-HL7PT                                            |
|   NCI Health Level 7, SY                                                 |
|                                                                          |
|                     NCI-HL7SY                                            |
|   National Council for Prescription Drug Programs PT                     |
|                                                                          |
|                     NCPDPPT                                              |
|   National Institute of Child Health and Human Development PT            |
|                                                                          |
|                     NICHDPT                                              |
|   National Institute of Child Health and Human Development SY            |
|                                                                          |
|                     NICHDSY                                              |
|   Name of Supplementary Concept                                          |
|                                                                          |
|                     NM                                                   |
|   Non-preferred term                                                     |
|                                                                          |
|                     NP                                                   |
|   HL7 non-preferred for language term                                    |
|                                                                          |
|                     NPT                                                  |
|   Short form of non-preferred term                                       |
|                                                                          |
|                     NS                                                   |
|   Expanded form of non-preferred term                                    |
|                                                                          |
|                     NX                                                   |
|   Obsolete abbreviation                                                  |
|                                                                          |
|                     OA                                                   |
|   Obsolete Modifier Abbreviation                                         |
|                                                                          |
|                     OAM                                                  |
|   Obsolete term                                                          |
|                                                                          |
|                     OB                                                   |
|   Nursing outcomes                                                       |
|                                                                          |
|                     OC                                                   |
|   Obsolete clinical drug                                                 |
|                                                                          |
|                     OCD                                                  |
|   Obsolete entry term                                                    |
|                                                                          |
|                     OET                                                  |
|   Obsolete fully specified name                                          |
|                                                                          |
|                     OF                                                   |
|   Non-current Lower Level Term                                           |
|                                                                          |
|                     OL                                                   |
|   Obsolete Long common name                                              |
|                                                                          |
|                     OLC                                                  |
|   Japanese Non-current Lower Level Term (kana)                           |
|                                                                          |
|                     OLJKN                                                |
|   Japanese Non-current Lower Level Term (kana1)                          |
|                                                                          |
|                     OLJKN1                                               |
|   Obsolete modifiers in HCPCS                                            |
|                                                                          |
|                     OM                                                   |
|   Obsolete non-preferred for language term                               |
|                                                                          |
|                     ONP                                                  |
|   Obsolete official short name                                           |
|                                                                          |
|                     OOSN                                                 |
|   Obsolete preferred name                                                |
|                                                                          |
|                     OP                                                   |
|   Obsolete preferred term, natural language form                         |
|                                                                          |
|                     OPN                                                  |
|   Orders                                                                 |
|                                                                          |
|                     OR                                                   |
|   System-organ class                                                     |
|                                                                          |
|                     OS                                                   |
|   Japanese System-organ class in the WHO Adverse Reaction Terminology (k |
| ana)                                                                     |
|                     OSJKN                                                |
|   Japanese System-organ class in the WHO Adverse Reaction Terminology (k |
| ana1)                                                                    |
|                     OSJKN1                                               |
|   Official short name                                                    |
|                                                                          |
|                     OSN                                                  |
|   Preferred "trimmed term" in ICPC                                       |
|                                                                          |
|                     PC                                                   |
|   Preferred entry term for Supplementary Concept                         |
|                                                                          |
|                     PCE                                                  |
|   Preferred non-print entry term                                         |
|                                                                          |
|                     PEN                                                  |
|   Preferred entry term                                                   |
|                                                                          |
|                     PEP                                                  |
|   National Cancer Institute Nature Pathway Interaction Database PT       |
|                                                                          |
|                     PIDPT                                                |
|   Name from a precise ingredient                                         |
|                                                                          |
|                     PIN                                                  |
|   Machine permutation                                                    |
|                                                                          |
|                     PM                                                   |
|   Metathesaurus preferred name                                           |
|                                                                          |
|                     PN                                                   |
|   Qualifier for a problem                                                |
|                                                                          |
|                     PQ                                                   |
|   Name of a problem                                                      |
|                                                                          |
|                     PR                                                   |
|   Short forms that needed full specification                             |
|                                                                          |
|                     PS                                                   |
|   Protocol selection criteria                                            |
|                                                                          |
|                     PSC                                                  |
|   Designated preferred name                                              |
|                                                                          |
|                     PT                                                   |
|   Preferred Allelic Variant                                              |
|                                                                          |
|                     PTAV                                                 |
|   Preferred Clinical Synopsis                                            |
|                                                                          |
|                     PTCS                                                 |
|   British preferred term                                                 |
|                                                                          |
|                     PTGB                                                 |
|   Japanese Designated preferred name (kana)                              |
|                                                                          |
|                     PTJKN                                                |
|   Japanese Designated preferred name (kana1)                             |
|                                                                          |
|                     PTJKN1                                               |
|   Preferred term, natural language form                                  |
|                                                                          |
|                     PTN                                                  |
|   Expanded preferred terms (pair with PS)                                |
|                                                                          |
|                     PX                                                   |
|   Preferred qualifier term                                               |
|                                                                          |
|                     PXQ                                                  |
|   Qualifier abbreviation                                                 |
|                                                                          |
|                     QAB                                                  |
|   Qualifier entry version                                                |
|                                                                          |
|                     QEV                                                  |
|   Qualifier sort version                                                 |
|                                                                          |
|                     QSV                                                  |
|   Root abbreviation                                                      |
|                                                                          |
|                     RAB                                                  |
|   Registry Nomenclature Information Display Name                         |
|                                                                          |
|                     RENIDN                                               |
|   Root hierarchical term                                                 |
|                                                                          |
|                     RHT                                                  |
|   Root preferred term                                                    |
|                                                                          |
|                     RPT                                                  |
|   Extracted related names in SNOMED2                                     |
|                                                                          |
|                     RS                                                   |
|   Root synonym                                                           |
|                                                                          |
|                     RSY                                                  |
|   Designated related term                                                |
|                                                                          |
|                     RT                                                   |
|   Named subset of a source                                               |
|                                                                          |
|                     SB                                                   |
|   Semantic branded drug                                                  |
|                                                                          |
|                     SBD                                                  |
|   Semantic Branded Drug Component                                        |
|                                                                          |
|                     SBDC                                                 |
|   Semantic branded drug and form                                         |
|                                                                          |
|                     SBDF                                                 |
|   Special Category term                                                  |
|                                                                          |
|                     SC                                                   |
|   Scale                                                                  |
|                                                                          |
|                     SCALE                                                |
|   Semantic Clinical Drug                                                 |
|                                                                          |
|                     SCD                                                  |
|   Semantic Drug Component                                                |
|                                                                          |
|                     SCDC                                                 |
|   Semantic clinical drug and form                                        |
|                                                                          |
|                     SCDF                                                 |
|   Scientific name                                                        |
|                                                                          |
|                     SCN                                                  |
|   CCS single-level diagnosis categories                                  |
|                                                                          |
|                     SD                                                   |
|   Name of a sign or symptom of a problem                                 |
|                                                                          |
|                     SI                                                   |
|   Standardised MedDRA Query                                              |
|                                                                          |
|                     SMQ                                                  |
|   Official component synonym in LOINC                                    |
|                                                                          |
|                     SN                                                   |
|   CCS single-level procedure categories                                  |
|                                                                          |
|                     SP                                                   |
|   Synonymous "short" forms                                               |
|                                                                          |
|                     SS                                                   |
|   Source short name, used in the UMLS Knowledge Source Server            |
|                                                                          |
|                     SSN                                                  |
|   Step                                                                   |
|                                                                          |
|                     ST                                                   |
|   Active Substance                                                       |
|                                                                          |
|                     SU                                                   |
|   Mixed-case component synonym with expanded abbreviations               |
|                                                                          |
|                     SX                                                   |
|   Designated synonym                                                     |
|                                                                          |
|                     SY                                                   |
|   British synonym                                                        |
|                                                                          |
|                     SYGB                                                 |
|   Designated alias                                                       |
|                                                                          |
|                     SYN                                                  |
|   Task                                                                   |
|                                                                          |
|                     TA                                                   |
|   Term class                                                             |
|                                                                          |
|                     TC                                                   |
|   Name of the target of an intervention                                  |
|                                                                          |
|                     TG                                                   |
|   Tall Man synonym                                                       |
|                                                                          |
|                     TMSY                                                 |
|   Topical qualifier                                                      |
|                                                                          |
|                     TQ                                                   |
|   CCPSS synthesized problems for TC termgroup                            |
|                                                                          |
|                     TX                                                   |
|   Unique authority name                                                  |
|                                                                          |
|                     UAUN                                                 |
|   Unique common name                                                     |
|                                                                          |
|                     UCN                                                  |
|   Unified Code for Units of Measure AB                                   |
|                                                                          |
|                     UCUMAB                                               |
|   Unified Code for Units of Measure PT                                   |
|                                                                          |
|                     UCUMPT                                               |
|   Unified Code for Units of Measure SY                                   |
|                                                                          |
|                     UCUMSY                                               |
|   Unique equivalent name                                                 |
|                                                                          |
|                     UE                                                   |
|   Unique scientific name                                                 |
|                                                                          |
|                     USN                                                  |
|   Unique synonym                                                         |
|                                                                          |
|                     USY                                                  |
|   Versioned abbreviation                                                 |
|                                                                          |
|                     VAB                                                  |
|   Versioned preferred term                                               |
|                                                                          |
|                     VPT                                                  |
|   Versioned synonym                                                      |
|                                                                          |
|                     VSY                                                  |
|   Expanded descriptor in AOD                                             |
|                                                                          |
|                     XD                                                   |
|   Cross mapping set                                                      |
|                                                                          |
|                     XM                                                   |
|   Alternate name for a qualifier                                         |
|                                                                          |
|                     XQ                                                   |
|   Expanded string                                                        |
|                                                                          |
|                     XX                                                   |
|   Zebrafish Model Organism Database PT                                   |
|                                                                          |
|                     ZFINPT                                               |
|   Zebrafish Model Organism Database SY                                   |
|                                                                          |
|                     ZFINSY                                               |
+--------------------------------------------------------------------------+

</div>

</div>

\
### Subheading Metadata <span class="nav">[return to top of page](#metadata)</span>

<div class="group rounded-content-block">

<div id="getSubheading" class="method rounded-content-block">

**Method: **<span class="method-name">getSubheading</span><span
class="method-parameters">(String ticket,String version,String
subheading)</span>
**Returns:** <span
class="method-return-type">SubheadingDTO </span>[<span
class="see_javadocs">(see
javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/metadata/SubheadingDTO.html)

<div class="method-description">

**Use Case:** Given a UMLS release and a MeSH subheading abbreviation,
this call returns the expanded form of the MeSH subheading name,
together with the supplied MeSH subheading abbreviation.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

mySubheading = utsMetadataService.getSubheading(ticket, umlsRelease,
"AE");\
 String expandedForm = mySubheading.getExpandedForm();\
 String abbreviation = mySubheading.getAbbreviation();\

</div>

#### Sample Input (C♯):

<div class="input rounded-content-block">

Metadata.subheadingDTO mySubheading =
utsMetadataService.getSubheading(singleUseTicket, "2012AB", "AE");\
\
 string expandedForm = mySubheading.expandedForm;\
 string abbreviation = mySubheading.abbreviation;\

</div>

#### Sample Output:

  -------------------------------
  ExpandedForm:adverse effects\
   Abbreviation:AE\
  -------------------------------

</div>

<div id="getAllSubheadings" class="method rounded-content-block">

**Method: **<span class="method-name">getAllSubheadings</span><span
class="method-parameters">(String ticket,String version)</span>
**Returns:** <span
class="method-return-type">ArrayList&lt;SubheadingDTO&gt; </span>[<span
class="see_javadocs">(see
javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/metadata/SubheadingDTO.html)

<div class="method-description">

**Use Case:** Given a UMLS release, this call returns all of the valid
MeSH subheadings, their expanded forms and abbreviations, for the given
release.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

myarrSubheading = utsMetadataService.getAllSubheadings(ticket,
umlsRelease);\
\
 for (int i = 0; i &lt; myarrSubheading.size(); i++) {\
 SubheadingDTO mySubheadingDTO = myarrSubheading.get(i);\
 String expandedForm = mySubheadingDTO.getExpandedForm();\
 String abbreviation = mySubheadingDTO.getAbbreviation();\
 }\

</div>

#### Sample Input (C♯):

<div class="input rounded-content-block">

Metadata.subheadingDTO\[\] mySubheadings =
utsMetadataService.getAllSubheadings(singleUseTicket, "2012AB");\
 for (int i = 0; i &lt; mySubheadings.Length; i++) {\
\
 Metadata.subheadingDTO mySubheadingDTO = mySubheadings\[i\];\
\
 string expandedForm = mySubheadingDTO.expandedForm;\
 string abbreviation = mySubheadingDTO.abbreviation;\
 }\

</div>

#### Sample Output:

  ----------------------------------------------
  ExpandedForm:No MeSH subheading (qualifier)\
   Abbreviation:&lt;&gt;\
   ExpandedForm:analogs & derivatives\
   Abbreviation:AA\
   ExpandedForm:abnormalities\
   Abbreviation:AB\
   ExpandedForm:administration & dosage\
   Abbreviation:AD\
   ExpandedForm:adverse effects\
   Abbreviation:AE\
   ExpandedForm:agonists\
   Abbreviation:AG\
   ExpandedForm:anatomy & histology\
   Abbreviation:AH\
   ExpandedForm:antagonists & inhibitors\
   Abbreviation:AI\
   ExpandedForm:analysis\
   Abbreviation:AN\
   ExpandedForm:biosynthesis\
   Abbreviation:BI\
   ExpandedForm:blood\
   Abbreviation:BL\
   ExpandedForm:blood supply\
   Abbreviation:BS\
   ExpandedForm:cerebrospinal fluid\
   Abbreviation:CF\
   ExpandedForm:chemistry\
   Abbreviation:CH\
   ExpandedForm:chemically induced\
   Abbreviation:CI\
   ExpandedForm:classification\
   Abbreviation:CL\
   ExpandedForm:congenital\
   Abbreviation:CN\
   ExpandedForm:complications\
   Abbreviation:CO\
   ExpandedForm:chemical synthesis\
   Abbreviation:CS\
   ExpandedForm:contraindications\
   Abbreviation:CT\
   ExpandedForm:cytology\
   Abbreviation:CY\
   ExpandedForm:drug effects\
   Abbreviation:DE\
   ExpandedForm:deficiency\
   Abbreviation:DF\
   ExpandedForm:diet therapy\
   Abbreviation:DH\
   ExpandedForm:diagnosis\
   Abbreviation:DI\
   ExpandedForm:drug therapy\
   Abbreviation:DT\
   ExpandedForm:diagnostic use\
   Abbreviation:DU\
   ExpandedForm:economics\
   Abbreviation:EC\
   ExpandedForm:education\
   Abbreviation:ED\
   ExpandedForm:ethnology\
   Abbreviation:EH\
   ExpandedForm:embryology\
   Abbreviation:EM\
   ExpandedForm:enzymology\
   Abbreviation:EN\
   ExpandedForm:epidemiology\
   Abbreviation:EP\
   ExpandedForm:ethics\
   Abbreviation:ES\
   ExpandedForm:etiology\
   Abbreviation:ET\
   ExpandedForm:growth & development\
   Abbreviation:GD\
   ExpandedForm:genetics\
   Abbreviation:GE\
   ExpandedForm:history\
   Abbreviation:HI\
   ExpandedForm:immunology\
   Abbreviation:IM\
   ExpandedForm:injuries\
   Abbreviation:IN\
   ExpandedForm:isolation & purification\
   Abbreviation:IP\
   ExpandedForm:innervation\
   Abbreviation:IR\
   ExpandedForm:instrumentation\
   Abbreviation:IS\
   ExpandedForm:legislation & jurisprudence\
   Abbreviation:LJ\
   ExpandedForm:manpower\
   Abbreviation:MA\
   ExpandedForm:metabolism\
   Abbreviation:ME\
   ExpandedForm:microbiology\
   Abbreviation:MI\
   ExpandedForm:mortality\
   Abbreviation:MO\
   ExpandedForm:methods\
   Abbreviation:MT\
   ExpandedForm:nursing\
   Abbreviation:NU\
   ExpandedForm:organization & administration\
   Abbreviation:OG\
   ExpandedForm:pathology\
   Abbreviation:PA\
   ExpandedForm:prevention & control\
   Abbreviation:PC\
   ExpandedForm:pharmacology\
   Abbreviation:PD\
   ExpandedForm:physiology\
   Abbreviation:PH\
   ExpandedForm:pharmacokinetics\
   Abbreviation:PK\
   ExpandedForm:poisoning\
   Abbreviation:PO\
   ExpandedForm:physiopathology\
   Abbreviation:PP\
   ExpandedForm:parasitology\
   Abbreviation:PS\
   ExpandedForm:psychology\
   Abbreviation:PX\
   ExpandedForm:pathogenicity\
   Abbreviation:PY\
   ExpandedForm:radiography\
   Abbreviation:RA\
   ExpandedForm:radiation effects\
   Abbreviation:RE\
   ExpandedForm:rehabilitation\
   Abbreviation:RH\
   ExpandedForm:radionuclide imaging\
   Abbreviation:RI\
   ExpandedForm:radiotherapy\
   Abbreviation:RT\
   ExpandedForm:secondary\
   Abbreviation:SC\
   ExpandedForm:supply & distribution\
   Abbreviation:SD\
   ExpandedForm:secretion\
   Abbreviation:SE\
   ExpandedForm:statistics & numerical data\
   Abbreviation:SN\
   ExpandedForm:standards\
   Abbreviation:ST\
   ExpandedForm:surgery\
   Abbreviation:SU\
   ExpandedForm:trends\
   Abbreviation:TD\
   ExpandedForm:therapy\
   Abbreviation:TH\
   ExpandedForm:transmission\
   Abbreviation:TM\
   ExpandedForm:toxicity\
   Abbreviation:TO\
   ExpandedForm:transplantation\
   Abbreviation:TR\
   ExpandedForm:therapeutic use\
   Abbreviation:TU\
   ExpandedForm:ultrastructure\
   Abbreviation:UL\
   ExpandedForm:urine\
   Abbreviation:UR\
   ExpandedForm:ultrasonography\
   Abbreviation:US\
   ExpandedForm:utilization\
   Abbreviation:UT\
   ExpandedForm:veterinary\
   Abbreviation:VE\
   ExpandedForm:virology\
   Abbreviation:VI\
  ----------------------------------------------

</div>

</div>

\
### Relation Metadata <span class="nav">[return to top of page](#metadata)</span>

<div class="group rounded-content-block">

<div id="getRelationLabel" class="method rounded-content-block">

**Method: **<span class="method-name">getRelationLabel</span><span
class="method-parameters">(String ticket,String version,String
relationLabel)</span>
**Returns:** <span
class="method-return-type">RelationLabelDTO </span>[<span
class="see_javadocs">(see
javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/metadata/RelationLabelDTO.html)

<div class="method-description">

**Use Case:** Given a UMLS release and abbreviated form of a relation
label (REL), this call returns the expanded form of the relation label
as well as the abbreviation.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

myRelationLabel = utsMetadataService.getRelationLabel(ticket,
umlsRelease, "RN");\
 String abbreviation = myRelationLabel.getAbbreviation();\
 String expandedForm = myRelationLabel.getExpandedForm();\
 String inverseAbbr = myRelationLabel.getInverse().getAbbreviation();\
 String inverseExpandedForm =
myRelationLabel.getInverse().getExpandedForm();\

</div>

#### Sample Input (C♯):

<div class="input rounded-content-block">

Metadata.relationLabelDTO myRelationLabel =
utsMetadataService.getRelationLabel(singleUseTicket, "2012AB", "RN");\
\
 string abbreviation = myRelationLabel.abbreviation;\
 string expandedForm = myRelationLabel.expandedForm;\
 string inverseAbbreviation = myRelationLabel.inverse.abbreviation;\
 string inverseExpandedForm = myRelationLabel.inverse.expandedForm;\

</div>

#### Sample Output:

  --------------------------------------------------
  Abbreviation:RN\
   ExpandedForm:has a narrower relationship\
   inverseAbbr:RB\
   inverseExpandedForm:has a broader relationship\
  --------------------------------------------------

</div>

<div id="getAllRelationLabels" class="method rounded-content-block">

**Method: **<span class="method-name">getAllRelationLabels</span><span
class="method-parameters">(String ticket,String version)</span>
**Returns:** <span
class="method-return-type">ArrayList&lt;RelationLabelDTO&gt; </span>[<span
class="see_javadocs">(see
javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/metadata/RelationLabelDTO.html)

<div class="method-description">

**Use Case:** Given a UMLS release, this call returns all the valid
relation labels (REL) for the release. Each relation label is returned
with its expanded form and its abbreviation.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

myarrRelationLabel = utsMetadataService.getAllRelationLabels(ticket,
umlsRelease);\
\
 for (int i = 0; i &lt; myarrRelationLabel.size(); i++) {\
 RelationLabelDTO myRelationLabelDTO = myarrRelationLabel.get(i);\
 String expandedForm = myRelationLabelDTO.getAbbreviation();\
 String abbreviation = myRelationLabelDTO.getExpandedForm();\
 }\

</div>

#### Sample Input (C♯):

<div class="input rounded-content-block">

Metadata.relationLabelDTO\[\] myRelationLabels =
utsMetadataService.getAllRelationLabels(singleUseTicket, "2012AB");\
 for (int i = 0; i &lt; myRelationLabels.Length; i++)\
 {\
 Metadata.relationLabelDTO myRelationLabelDTO = myRelationLabels\[i\];\
\
 string expandedForm = myRelationLabelDTO.expandedForm;\
 string abbreviation = myRelationLabelDTO.abbreviation;\
 }

</div>

#### Sample Output:

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Abbreviation:Allowed qualifier\
   ExpandedForm:AQ\
   Abbreviation:has child relationship in a Metathesaurus source vocabulary\
   ExpandedForm:CHD\
   Abbreviation:Deleted concept\
   ExpandedForm:DEL\
   Abbreviation:has parent relationship in a Metathesaurus source vocabulary\
   ExpandedForm:PAR\
   Abbreviation:can be qualified by.\
   ExpandedForm:QB\
   Abbreviation:has a broader relationship\
   ExpandedForm:RB\
   Abbreviation:the relationship is similar or "alike". the two concepts are similar or "alike". In the current edition of the Metathesaurus, most relationships with this attribute are mappings provided by a source, named in SAB and SL; hence concepts linked by this relationship may be synonymous, i.e. self-referential: CUI1 = CUI2. In previous releases, some MeSH Supplementary Concept relationships were represented in this way.\
   ExpandedForm:RL\
   Abbreviation:has a narrower relationship\
   ExpandedForm:RN\
   Abbreviation:has relationship other than synonymous, narrower, or broader\
   ExpandedForm:RO\
   Abbreviation:related and possibly synonymous.\
   ExpandedForm:RQ\
   Abbreviation:Related, unspecified\
   ExpandedForm:RU\
   Abbreviation:has sibling relationship in a Metathesaurus source vocabulary.\
   ExpandedForm:SIB\
   Abbreviation:source asserted synonymy.\
   ExpandedForm:SY\
   Abbreviation:Not related, no mapping\
   ExpandedForm:XR\
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

</div>

<div id="getAdditionalRelationLabel"
class="method rounded-content-block">

**Method: **<span
class="method-name">getAdditionalRelationLabel</span><span
class="method-parameters">(String ticket,String version,String
additionalrelationLabel)</span>
**Returns:** <span
class="method-return-type">AdditionalRelationLabelDTO </span>[<span
class="see_javadocs">(see
javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/metadata/AdditionalRelationLabelDTO.html)

<div class="method-description">

**Use Case:** Given a UMLS release and an abbreviation for an additional
relation (RELA), this call returns the expanded name of the additional
relation as well as the supplied abbreviation. Additional relations are
asserted by the source vocabulary and not all terms have an additional
relation. The abbreviations are very similar to the expanded forms for
most additional relations with slight differences in capitalization or
word-delimiting (e.g., spaces versus underlines).

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

myAdditionalRelationLabel =
utsMetadataService.getAdditionalRelationLabel(ticket, umlsRelease,
"origin\_of");\
\
 String expandedForm = myAdditionalRelationLabel.getExpandedForm();\
 String abbreviation = myAdditionalRelationLabel.getAbbreviation();\
 String inverseExpForm =
myAdditionalRelationLabel.getInverse().getExpandedForm();\
 String inverseExpForm =
myAdditionalRelationLabel.getInverse().getAbbreviation();\

</div>

#### Sample Input (C♯):

<div class="input rounded-content-block">

Metadata.additionalRelationLabelDTO myAdditionalRelationLabel =
utsMetadataService.getAdditionalRelationLabel(singleUseTicket, "2012AB",
"origin\_of");\
\
 string expandedForm = myAdditionalRelationLabel.expandedForm;\
 string abbreviation = myAdditionalRelationLabel.abbreviation;\
 string inverseExpandedForm =
myAdditionalRelationLabel.inverse.expandedForm;\
 string inverseAbbreviation =
myAdditionalRelationLabel.inverse.abbreviation;\

</div>

#### Sample Output:

  --------------------------------------
  ExpandedForm:Origin of\
   Abbreviation:origin\_of\
   InverseExpandedForm:Has origin\
   InverseAbbreviationForm:Has origin\
  --------------------------------------

</div>

<div id="getAllAdditionalRelationLabels"
class="method rounded-content-block">

**Method: **<span
class="method-name">getAllAdditionalRelationLabels</span><span
class="method-parameters">(String ticket,String version)</span>
**Returns:** <span
class="method-return-type">ArrayList&lt;AdditionalRelationLabelDTO&gt; </span>[<span
class="see_javadocs">(see
javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/metadata/AdditionalRelationLabelDTO.html)

<div class="method-description">

**Use Case:** Given a UMLS release, this call returns all the valid
additional relations (RELA) for the release. Additional relations are
asserted by the source vocabulary and not all terms have an additional
relation. The abbreviations are very similar to the expanded forms for
most additional relations with slight differences in capitalization or
word-delimiting (e.g., spaces versus underlines).

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

myarrAdditionalRelationLabel =
utsMetadataService.getAllAdditionalRelationLabels(ticket, umlsRelease);\
\
 for (int i = 0; i &lt; myarrAdditionalRelationLabel.size(); i++) {\
 String expandedForm = myarrAdditionalRelationLabel.getExpandedForm();\
 String abbreviation = myarrAdditionalRelationLabel.getAbbreviation();\
 String inverseExpForm =
myarrAdditionalRelationLabel.getInverse().getExpandedForm();\
 String inverseExpForm =
myarrAdditionalRelationLabel.getInverse().getAbbreviation();\
 }\

</div>

#### Sample Input (C♯):

<div class="input rounded-content-block">

Metadata.additionalRelationLabelDTO\[\] myAdditionalRelationLabelDTO =
utsMetadataService.getAllAdditionalRelationLabels(singleUseTicket,
"2012AB");\
 for (int i = 0; i &lt; myAdditionalRelationLabelDTO.Length; i++) {\
\
 Metadata.additionalRelationLabelDTO myArrayAdditionalRelationLabel =
myAdditionalRelationLabelDTO\[i\];\
\
 string expandedForm = myArrayAdditionalRelationLabel.expandedForm;\
 string abbreviation = myArrayAdditionalRelationLabel.abbreviation;\
 string inverseExpandedForm =
myArrayAdditionalRelationLabel.inverse.expandedForm;\
 string inverseAbbreviation =
myArrayAdditionalRelationLabel.inverse.abbreviation;\

</div>

#### Sample Output:

  --------------------------------------------------------------------
  ExpandedForm:abnormal cell affected by chemical or drug\
   Abbreviation:abnormal\_cell\_affected\_by\_chemical\_or\_drug\
   Inverse ExpandedForm:chemical or drug affects abnormal cell\
   Inverse Abbreviation:chemical\_or\_drug\_affects\_abnormal\_cell\
   ExpandedForm:abnormality associated with allele\
   Abbreviation:abnormality\_associated\_with\_allele\
   Inverse ExpandedForm:allele has abnormality\
   Inverse Abbreviation:allele\_has\_abnormality\
   ExpandedForm:Access device used by\
   Abbreviation:access\_device\_used\_by\
   Inverse ExpandedForm:Uses access device\
   Inverse Abbreviation:uses\_access\_device\
   ExpandedForm:Access of\
   Abbreviation:access\_of\
   Inverse ExpandedForm:Has access\
   Inverse Abbreviation:has\_access\
   ExpandedForm:Active ingredient of\
   Abbreviation:active\_ingredient\_of\
   Inverse ExpandedForm:Has active ingredient\
   Inverse Abbreviation:has\_active\_ingredient\
   and so on..\
  --------------------------------------------------------------------

</div>

</div>

\
### Attribute Metadata <span class="nav">[return to top of page](#metadata)</span>

<div class="group rounded-content-block">

<div id="getAttributeName" class="method rounded-content-block">

**Method: **<span class="method-name">getAttributeName</span><span
class="method-parameters">(String ticket,String version,String
attributeName)</span>
**Returns:** <span
class="method-return-type">AttributeNameDTO </span>[<span
class="see_javadocs">(see
javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/metadata/AttributeNameDTO.html)

<div class="method-description">

**Use Case:** Given a UMLS release and an attribute name abbreviation
(ATN), this call returns the expanded form of the attribute name.

</div>

<div class="sample content-block">

</div>

#### Sample Input (Java):

<div class="input rounded-content-block">

myAttributeName = utsMetadataService.getAttributeName(ticket,
umlsRelease, "TH");\
\
 String abbreviation = myAttributeName.getAbbreviation();\
 String expandedForm = myAttributeName.getExpandedForm();\

</div>

#### Sample Input (C♯):

<div class="input rounded-content-block">

Metadata.attributeNameDTO myAttributeName =
utsMetadataService.getAttributeName(singleUseTicket, "2012AB", "TH");\
 string abbreviation = myAttributeName.abbreviation;\
 string expandedForm = myAttributeName.expandedForm;\

</div>

#### Sample Output:

  ----------------------------------------------------------------------------------------------------------------------------------
  Abbreviation:TH\
   ExpandedForm:MeSH Thesaurus ID - identifies thesauri other than MeSH in which the MeSH heading or cross-reference is included.\
  ----------------------------------------------------------------------------------------------------------------------------------

</div>



**Method: **<span class="method-name">getAllAttributeNames</span><span
class="method-parameters">(String ticket,String version)</span>
**Returns:** <span
class="method-return-type">ArrayList&lt;AttributeNameDTO&gt; </span>[<span
class="see_javadocs">(see
javadocs)</span>](javadocs/gov/nih/nlm/umls/dto/metadata/AttributeNameDTO.html)



**Use Case:** Given a UMLS release, this call returns all attribute
names for the release. Each attribute is returned in abbreviated form
and expanded form.



#### Sample Input (Java):

myarrAttributeName = utsMetadataService.getAllAttributeNames(ticket,
umlsRelease);\
\
 for (int i = 0; i &lt; myarrAttributeName.size(); i++) {\
 AttributeNameDTO myarrAttributeNameDTO = myarrAttributeName.get(i);\
 String abbreviation = myarrAttributeNameDTO.getAbbreviation();\
 String expandedForm = myarrAttributeNameDTO.getExpandedForm();\
 }\



#### Sample Input (C♯):

Metadata.attributeNameDTO\[\] myAttributeNameDTO =
utsMetadataService.getAllAttributeNames(singleUseTicket, "2012AB");\
 for (int i = 0; i &lt; myAttributeNameDTO.Length; i++) {\
\
 Metadata.attributeNameDTO myArrayAttributeNameDTO =
myAttributeNameDTO\[i\];\
\
 string abbreviation = myArrayAttributeNameDTO.abbreviation;\
 string expandedForm = myArrayAttributeNameDTO.expandedForm;\



#### Sample Output:

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Abbreviation:AAL\_TERM\
   ExpandedForm:AAL term\
   Abbreviation:ACCEPTED\_THERAPEUTIC\_USE\_FOR\
   ExpandedForm:Accepted therapeutic use for\
   Abbreviation:ACCESSION\_NO\
   ExpandedForm:Accession number\
   Abbreviation:ADJACENT\
   ExpandedForm:Adjacent\
   Abbreviation:ALT\_SORT\_CODE\
   ExpandedForm:Alt sort code\
   Abbreviation:AMBIGUITY\_FLAG\
   ExpandedForm:Source atom ambiguity flag\
   Abbreviation:AMT\
   ExpandedForm:AOT uses MeSH term\
   Abbreviation:AN\
   ExpandedForm:MeSH Annotation - an informative MeSH note written primarily for indexers or catalogers that may also be useful in explaining the use of a MeSH term to online searchers.\
   Abbreviation:ANADA\
   ExpandedForm:Abbreviated New Animal Drug application number for the generic drug for MTHSPL\
   Abbreviation:ANATOMICAL\_COORDINATE\
   ExpandedForm:Anatomical coordinate\
   Abbreviation:ANATOMICAL\_OR\_ARBITRARY\
   ExpandedForm:Anatomical or Arbitrary\
   Abbreviation:ANDA\
   ExpandedForm:Abbreviated New (Generic) Drug application number for the MTHSPL drug\
   Abbreviation:AQ\
   ExpandedForm:SNOMED CT "allowable qualifier" attribute for representing certain relationships (those having a characteristic type of "Qualifier" and a refinability of "Mandatory") which indicate one of several allowable types of qualifiers, such as laterality or severity, that a concept may have\
   Abbreviation:AQL\
   ExpandedForm:MeSH Allowable Qualifier - list of allowable qualifier abbreviations for MeSH main headings (e.g. AA, CL, CS, DF, DU, IM, I,P ME, PK)\
   Abbreviation:BIOCARTA\_ID\
   ExpandedForm:BioCarta online maps of molecular pathways, adapted for NCI use ID\
   Abbreviation:BLA\
   ExpandedForm:Therapeutic Biologic Applications number for the MTHSPL drug\
   Abbreviation:BLOCK\
   ExpandedForm:Block code\
   Abbreviation:CAS\_REGISTRY\
   ExpandedForm:CAS Registry\
   Abbreviation:CCDS\_ID\
   ExpandedForm:CCDS ID\
   Abbreviation:CCF\
   ExpandedForm:Canonical Clinical Problem Statement System (CCPSS) frequency - the number of times a CCPSS term appears in a patient record.\
   Abbreviation:CCI\
   ExpandedForm:ICD-9-CM code(s) clusters in a Clinical Classifications Software (CCS) category - individual ICD-9-CM codes (or ranges of such codes) classified into CCS categories.\
   Abbreviation:CELL\_APPENDAGE\_TYPE\
   ExpandedForm:Cell appendage type\
   Abbreviation:CELL\_LAYER\
   ExpandedForm:Cell layer\
   Abbreviation:CFR\
   ExpandedForm:Code of Federal Regulation Number (e.g. 862.3220, 892.1610)\
   Abbreviation:CHANGE\_REASON\_PUBLIC\
   ExpandedForm:Detailed explanation about special changes to the term over time.\
   Abbreviation:CHAPTER\
   ExpandedForm:Chapter code\
   Abbreviation:CHAPTER\_NOTE\
   ExpandedForm:Chapter note\
   Abbreviation:CHARACTERISTICTYPE\
   ExpandedForm:SNOMED CT indication of whether a relationship specifies a defining characteristic of the source concept or a possible qualification of that Concept.\
   Abbreviation:CHEMICAL\_FORMULA\
   ExpandedForm:Chemical Formula\
   Abbreviation:CHROMOSOME\
   ExpandedForm:Chromosome\
   Abbreviation:CHROMOSOME\_PAIRS\_PER\_NUCLEUS\
   ExpandedForm:Chromosome pairs per nucleus\
   Abbreviation:CITE\
   ExpandedForm:Citation or edition information\
   Abbreviation:CNU\
   ExpandedForm:ISO 3166-1 standard country code in numeric (three-digit) format\
   Abbreviation:COATING\
   ExpandedForm:FDA Structured Product Label imprint attribute for coating\
   Abbreviation:CODE\
   ExpandedForm:Code\
   Abbreviation:CODE\_ALSO\
   ExpandedForm:Instructs that 2 codes may be required to fully describe a condition but the sequencing of the two codes is discretionary, depending on the severity of the conditions and the reason for the encounter.\
   Abbreviation:CODE\_FIRST\
   ExpandedForm:Certain conditions have both an underlying etiology and multiple body system manifestations due to the underlying etiology. ICD-10-CM has a coding convention that requires the underlying condition be sequenced first followed by the manifestation. Wherever such a combination exists there is a "code first" note at the manifestation code. These instructional notes indicate the proper sequencing order of the codes, etiology followed by manifestation. In most cases the manifestation codes will have in the code title, "in diseases classified elsewhere." Codes with this title are a component of the etiology/manifestation convention. The code title indicates that it is a manifestation code. "In diseases classified elsewhere" codes are never permitted to be used as first listed or principle diagnosis codes. They must be used in conjunction with an underlying condition code and they must be listed following the underlying condition.\
   Abbreviation:COLOR\
   ExpandedForm:FDA Structured Product Label imprint attribute for color\
   Abbreviation:COLORTEXT\
   ExpandedForm:FDA Structured Product Label imprint attribute for color text\
   Abbreviation:COMBO\_SCORE\
   ExpandedForm:Combo Score\
   Abbreviation:COMBO\_SCORE\_NO\_TOP\_WORDS\
   ExpandedForm:Combo Score that has no top words\
   Abbreviation:COMMON\_TEST\_RANK\
   ExpandedForm:Numeric ranking of approximately 2,000 common tests performed by hospitals\
   Abbreviation:CONCEPTSTATUS\
   ExpandedForm:SNOMED CT status which indicates whether a concept is in active use and, if not, indicates the reason it is inactive.\
   Abbreviation:CONNECTED\_TO\
   ExpandedForm:Connected to\
   Abbreviation:CONNECTION\_TYPE\
   ExpandedForm:Connection type\
   Abbreviation:CONSIDER\
   ExpandedForm:Codes to consider before definitive diagnosis\
   Abbreviation:CONSUMER\_NAME\
   ExpandedForm:An experimental (beta) consumer friendly name\
   Abbreviation:CONTACT\_TYPE\
   ExpandedForm:Contact type\
   Abbreviation:CONTEXT\_SCORE\
   ExpandedForm:Context Score\
   Abbreviation:CONTRIBUTING\_SOURCE\
   ExpandedForm:Contributing Source\
   Abbreviation:COPYRIGHT\
   ExpandedForm:Copyright\
   Abbreviation:CPF\
   ExpandedForm:CPT Full Description - complete text of the CPT full description, in cases where the CPT term in the "STR" field of MRCON has been trimmed from its original form.\
   Abbreviation:CTV3ID\
   ExpandedForm:The Read Code for a SNOMED CT concept taken from the United Kingdom?s Clinical Terms Version 3 terminology.\
   Abbreviation:CUI\_SCORE\
   ExpandedForm:CUI Score\
   Abbreviation:CURATED\_RANGE\_AND\_UNITS\
   ExpandedForm:Curated Range and Units\
   Abbreviation:CV\_ALGORITHM\
   ExpandedForm:Content view algorithm\
   Abbreviation:CV\_CATEGORY\
   ExpandedForm:Content view category\
   Abbreviation:CV\_CLASS\
   ExpandedForm:Content view class\
   Abbreviation:CV\_CODE\
   ExpandedForm:Content view code\
   Abbreviation:CV\_CONTRIBUTOR\
   ExpandedForm:Content view contributor\
   Abbreviation:CV\_CONTRIBUTOR\_DATE\
   ExpandedForm:Date corresponding to the contributor version of this concept view\
   Abbreviation:CV\_CONTRIBUTOR\_URL\
   ExpandedForm:URL corresponding to the contributor version of this concept view\
   Abbreviation:CV\_CONTRIBUTOR\_VERSION\
   ExpandedForm:Version of this content view submitted by the contributor\
   Abbreviation:CV\_DESCRIPTION\
   ExpandedForm:Content view description\
   Abbreviation:CV\_INCLUDE\_OBSOLETE\
   ExpandedForm:Content view includes obsolete data: YN\
   Abbreviation:CV\_IS\_GENERATED\
   ExpandedForm:Content view generated: Y/N\
   Abbreviation:CV\_MAINTAINER\
   ExpandedForm:Content view maintainer\
   Abbreviation:CV\_MAINTAINER\_DATE\
   ExpandedForm:Date corresponding to the maintainer version of this concept view\
   Abbreviation:CV\_MAINTAINER\_URL\
   ExpandedForm:URL corresponding to the maintainer version of this concept view\
   Abbreviation:CV\_MAINTAINER\_VERSION\
   ExpandedForm:Version of this content view submitted by the maintainer\
   Abbreviation:CV\_MEMBER\
   ExpandedForm:Describes the membership for an atom belonging to a particular content view. The value for this attribute is a tilde-delimited microsyntax. The first field is the content view bitflag (e.g. 2048), followed by field name-value pairs describing the member.\
   Abbreviation:CV\_PREVIOUS\_META\
   ExpandedForm:Previous UMLS Metathesaurus version used to generate content view. A null value means the content view is generated based on current UMLS Metathesaurus version.\
   Abbreviation:CX\
   ExpandedForm:MeSH Consider Also Note - other word roots or prefixes that should be consulted for concepts related to this MeSH concept, e.g., the value for "Heart" is "consider also terms at cardi- and myocardi-".\
   Abbreviation:DA\
   ExpandedForm:Metathesaurus Date of entry - YYYYMMDD, e.g., 19920830 - date of entry of the concept into the Metathesaurus.\
   Abbreviation:DATE\_CREATED\
   ExpandedForm:Date created\
   Abbreviation:DATE\_FIRST\_PUBLISHED\
   ExpandedForm:Date first published\
   Abbreviation:DATE\_LAST\_MODIFIED\
   ExpandedForm:Date last modified\
   Abbreviation:DATE\_NAME\_CHANGED\
   ExpandedForm:Date name changed\
   Abbreviation:DATE\_SYMBOL\_CHANGED\
   ExpandedForm:Date symbol changed\
   Abbreviation:DB\_XR\
   ExpandedForm:Database cross-reference\
   Abbreviation:DB\_XR\_ID\
   ExpandedForm:Database cross-reference ID\
   Abbreviation:DC\
   ExpandedForm:MeSH Descriptor class - type of MeSH term the concept name represents.\
   Abbreviation:DCSA\
   ExpandedForm:Controlled Substance Act designation code (e.g. 0,2,3n)\
   Abbreviation:DDF\
   ExpandedForm:Drug Doseform (e.g. chewable tablet)\
   Abbreviation:DDFA\
   ExpandedForm:Drug Doseform Abbreviation (e.g. SOLN)\
   Abbreviation:DEFCHARACTERISTICS\
   ExpandedForm:Defining characteristics\
   Abbreviation:DEFINITION\
   ExpandedForm:Definition\
   Abbreviation:DEFINITION\_DESCRIPTION\_HELP\
   ExpandedForm:Definition Description Help\
   Abbreviation:DESCRIPTIONSTATUS\
   ExpandedForm:SNOMED CT description status which indicates whether a description (concept name) is in active use and, if not, the reason it is inactive.\
   Abbreviation:DESCRIPTIONTYPE\
   ExpandedForm:SNOMED CT term type, indicating whether the term is the Preferred Term, Synonym or the Fully Specified Name for the associated concept.\
   Abbreviation:DESIGN\_NOTE\
   ExpandedForm:Design note.\
   Abbreviation:DESI\_DESC\
   ExpandedForm:Source drug efficacy study implementation indicator\
   Abbreviation:DEVTYPE\
   ExpandedForm:Device Type\
   Abbreviation:DHJC\
   ExpandedForm:Multum HCPCS J-code Multum clinical drugs linked to HCPCS J-codes where applicable (e.g. J7507)\
   Abbreviation:DID\
   ExpandedForm:Descriptor Identifier\
   Abbreviation:DIMENSION\
   ExpandedForm:Dimension code\
   Abbreviation:DISJOINT\_FROM\
   ExpandedForm:Disjoint from\
   Abbreviation:DISPARAGED\
   ExpandedForm:Disparaged\
   Abbreviation:DIV\
   ExpandedForm:NCBI Division/Phyla (e.g. DIV\[NCBI\]Viruses)\
   Abbreviation:DM\_SPL\_ID\
   ExpandedForm:DailyMed internal identifier for MTHSPL atom\
   Abbreviation:DOCUMENT\_SECTION\
   ExpandedForm:Classification of whether this LOINC code can be used a full document, a section of a document, or both.\
   ExpandedForm:Medline citation counts from articles dated 1944.\
   Abbreviation:MED1945\
   ExpandedForm:Medline citation counts from articles dated 1945.\
   Abbreviation:MED1946\
   ExpandedForm:Medline citation counts from articles dated 1946.\
   Abbreviation:MED1947\
   ExpandedForm:Medline citation counts from articles dated 1947.\
   Abbreviation:MED1948\
   ExpandedForm:Medline citation counts from articles dated 1948.\
   Abbreviation:MED1949\
   ExpandedForm:Medline citation counts from articles dated 1949.\
   Abbreviation:MED1950\
   ExpandedForm:Medline citation counts from articles dated 1950.\
   Abbreviation:MED1951\
   ExpandedForm:Medline citation counts from articles dated 1951.\
   Abbreviation:MED1952\
   ExpandedForm:Medline citation counts from articles dated 1952.\
   Abbreviation:MED1953\
   ExpandedForm:Medline citation counts from articles dated 1953.\
   Abbreviation:MED1954\
   ExpandedForm:Medline citation counts from articles dated 1954.\
   Abbreviation:MED1955\
   ExpandedForm:Medline citation counts from articles dated 1955.\
   Abbreviation:MED1956\
   ExpandedForm:Medline citation counts from articles dated 1956.\
   Abbreviation:MED1957\
   ExpandedForm:Medline citation counts from articles dated 1957.\
   Abbreviation:MED1958\
   ExpandedForm:Medline citation counts from articles dated 1958.\
   Abbreviation:MED1959\
   ExpandedForm:Medline citation counts from articles dated 1959.\
   Abbreviation:MED1960\
   ExpandedForm:Medline citation counts from articles dated 1960.\
   Abbreviation:MED1961\
   ExpandedForm:Medline citation counts from articles dated 1961.\
   Abbreviation:MED1962\
   ExpandedForm:Medline citation counts from articles dated 1962.\
   Abbreviation:MED1963\
   ExpandedForm:Medline citation counts from articles dated 1963.\
   Abbreviation:MED1964\
   ExpandedForm:Medline citation counts from articles dated 1964.\
   Abbreviation:MED1965\
   ExpandedForm:Medline citation counts from articles dated 1965.\
   Abbreviation:MED1966\
   ExpandedForm:Medline citation counts from articles dated 1966.\
   Abbreviation:MED1967\
   ExpandedForm:Medline citation counts from articles dated 1967.\
   Abbreviation:MED1968\
   ExpandedForm:Medline citation counts from articles dated 1968.\
   Abbreviation:MED1969\
   ExpandedForm:Medline citation counts from articles dated 1969.\
   Abbreviation:MED1970\
   ExpandedForm:Medline citation counts from articles dated 1970.\
   Abbreviation:MED1971\
   ExpandedForm:Medline citation counts from articles dated 1971.\
   Abbreviation:MED1972\
   ExpandedForm:Medline citation counts from articles dated 1972.\
   Abbreviation:MED1973\
   ExpandedForm:Medline citation counts from articles dated 1973.\
   Abbreviation:MED1974\
   ExpandedForm:Medline citation counts from articles dated 1974.\
   Abbreviation:MED1975\
   ExpandedForm:Medline citation counts from articles dated 1975.\
   Abbreviation:MED1976\
   ExpandedForm:Medline citation counts from articles dated 1976.\
   Abbreviation:MED1977\
   ExpandedForm:Medline citation counts from articles dated 1977.\
   Abbreviation:MED1978\
   ExpandedForm:Medline citation counts from articles dated 1978.\
   Abbreviation:MED1979\
   ExpandedForm:Medline citation counts from articles dated 1979.\
   Abbreviation:MED1980\
   ExpandedForm:Medline citation counts from articles dated 1980.\
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

