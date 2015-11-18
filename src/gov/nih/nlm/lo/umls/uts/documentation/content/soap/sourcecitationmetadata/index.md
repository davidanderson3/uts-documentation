title=Source Citation Metadata
date=2015-08-25
updated=2015-08-25
type=page
status=published
navorder=4
~~~~~~



**Method: **getAllSourceCitations(String ticket,String version)

**Returns:**ArrayList<SourceCitationDTO>

**Use Case:** This call returns a list of all valid source citations for a given release. The output is a list of SourceCitationDTOs. Each SourceCitationDTO contains a full citation and a handle.


#### Sample Input (Java):

~~~~
myarrSrcCitationDTO = utsMetadataService.getAllSourceCitations(ticket,umlsRelease);
 for (int i = 0; i < myarrSrcCitationDTO.size(); i++) {
 SourceCitationDTO mySrcCitDTO = myarrSrcCitationDTO.get(i);
 String value = mySrcCitDTO.getValue();
 }
~~~~

#### Sample Input (C♯):

~~~~
Metadata.sourceCitationDTO\[\] myArraySourceCitationDTO =utsMetadataService.getAllSourceCitations(singleUseTicket, "2012AB");
 for (int i = 0; i < myArraySourceCitationDTO.Length; i++) {
 Metadata.sourceCitationDTO mySourceCitationDTO =myArraySourceCitationDTO\[i\];
 string value = mySourceCitationDTO.value;
 }
~~~~

#### Sample Output:

~~~~
  Health Level Seven Vocabulary (HL7). Ann Arbor (MI): Health Level Seven, 1998-2002. Contact: Mark McDougall, Executive Director, Health Level Seven; 3300 Washtenaw Avenue, Suite 227, Ann Arbor, MI 48104-4250; Phone: (734)677-7777; Fax: (734)677-6622; Email: HQ@HL7.ORG ; Web site: www.HL7.ORG.
  
   HL7 Vocabulary Version 2.5, 7-bit equivalents created by the National Library of Medicine. Bethesda (MD): August 30, 2003
  
   United States Pharmacopeia (USP). Medicare Prescription Drug Benefit Model Guidelines: Drug Categories and Classes in Part D, 2004. http://www.usp.org/pdf/EN/mmg/comprehensiveDrugListing2004-12-31.pdf
  
   ICPC-2 PLUS. Sydney: Family Medicine Research Centre, University of Sydney, December 2005.
  
   Computer Retrieval of Information on Scientific Projects (CRISP). Bethesda (MD): National Institutes of Health, Division of Research Grants, Research Documentation Section, 2006.
  
   Authorized Osteopathic Thesaurus. Educational Council of Osteopathic Principles of the American Association of Colleges of Osteopathic Medicine: Chevy Chase MD, 2004;http://www.aacom.org/InfoFor/educators/Pages/thesaurus.aspx;ENG
  
   Nursing Interventions Classification (NIC)
  
   Moorhead, Sue, Johnson, Marion, Maas, Meridean, editors. Nursing Outcomes Classification (NOC): Iowa Outcomes Project. St. Louis (MO): Mosby, Inc., 2004.
  
   PDQ. Bethesda (MD): National Cancer Institute, February 2007.
  
   Martin, Karen S., Scheet, Nancy J.;The Omaha System;2005
  
   Finnish Translations of Medical Subject Headings (MeSH);Finnish Medical Society Duodecim;2008;Helsinki, Finland;FIN
  
  
   ABC Codes and Terminology;9th;Albuquerque, NM;ABC Coding Solutions - Alternative Link;2009;ENG
  
   World Health Organization;International Classification of Functioning, Disability and Health;Geneva, Switzerland;World Health Organization;2008;12/19/2008;http://www.who.int/classification/icf
   And so on...\
~~~~
>

**Method: **getSourceCitation(String ticket,String version,String handle)

**Returns:**SourceCitationDTO

**Use Case:** Given a UMLS release and a source citation handle, this call returns a full citation for the supplied handle. You can retrieve a source citation handle from the getAllSourceCitations call.

#### Sample Input (Java):

~~~~
mySrcCitationDTO = utsMetadataService.getSourceCitation(ticket, umlsRelease, "37");
 String value = mySrcCitationDTO.getValue();
~~~~>

#### Sample Input (C♯):

~~~~
Metadata.sourceCitationDTO mySourceCitation =utsMetadataService.getSourceCitation(singleUseTicket, "012AB", "37");
 string value = mySourceCitationDTO.value;
~~~~

#### Sample Output:

~~~~
  WHO Adverse Drug Reaction Terminology (WHOART). Portuguese Translation. Uppsala (Sweden): WHO Collaborating Centre for International Drug Monitoring, 1997.\
~~~~
