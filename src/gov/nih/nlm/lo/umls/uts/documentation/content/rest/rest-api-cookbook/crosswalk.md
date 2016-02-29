title=Code Crosswalk
date=2016-02-26
updated=2016-02-26
type=page
status=published
category=REST API Cookbook
navorder=1
~~~~~~

###Crosswalking codes using UMLS CUIs

A common use case of the CUIs in the UMLS is as a bridge of synonymy between code sets.  Users often have questions such as 'I have a code from vocabulary x, what
is the equivalent code from vocabulary according to UMLS synonymy?'. Although UMLS CUIs can be used as a starting point, results should be carefully reviewed for relevancy in your use case.  In this example, we'll use the API to crosswalk the [Human Phenotype Ontology](https://www.nlm.nih.gov/research/umls/sourcereleasedocs/current/HPO/) (HPO) code HP:0001947,
'Renal tubular acidosis', to see if there are any SNOMEDCT codes available.  The algorithm is as follows:

+ Query the /search endpoint for HPO concept HP:0001947 with the following parameters:
    - string=HP:0001947
    - searchType=exact
    - inputType=sourceUi
    - sabs=SNOMEDCT_US
    - ticket=\<your service ticket\>.  See [authentication](/rest/authentication.html) for details
+ Parse the concept object (CUI) returned and ask for atoms (preferred terms or synonyms) from the US Edition of SNOMED CT
+ Query the URI of the SNOMED CT concept returned to retrieve complete information about the SNOMED CT concept


Your initial `GET` call should look like this:
`https://uts-ws.nlm.nih.gov/rest/search/current?string=HP:0001947&searchType=exact&inputType=sourceUi&sabs=HPO&ticket=<your-ticket>`


You'll receive a list of searchResult objects back in your Json payload.  Most of the time it will contain only one CUI.  Sometimes you may receive more than one
depending on how NLM editors have interpreted the meaning of a source-asserted concept.  In this example, your search result will look as follows:

~~~~.json
{
pageSize: 25,
pageNumber: 1,
result: {
   classType: "searchResults",
   results: [
              {
                ui: "C0001126",
                rootSource: "MTH",
                uri: "https://uts-ws.nlm.nih.gov/rest/content/2015AB/CUI/C0001126",
                name: "Renal tubular acidosis"
               }
            ]   
        }
}
~~~~

Now that we have the CUI, we can use a linked data approach to make one more `GET` call to the [/atoms](/rest/atoms/index.html) endpoint of the CUI in question.
This will give us back a list of Atom objects that have all the terms that NLM editors have determined to be synonymous with 'Renal tubular acidosis'.
We can ask the API to include only atoms from the US Edition of SNOMED CT, and further ask for only preferred terms and synonyms.  Normally you'll only receive one atom back using
this algorithm.  Occasionally NLM Editors may merge more than one SNOMED CT concept into the same UMLS CUI if they determine the meaning is the same.
For example, HP:0001596 'Alopecia', maps to SNOMED CT concepts 278040002 'Loss of Hair', and 56317004 'Alopecia'.  There are also instances where synonyms asserted by SNOMED CT
have been split out from their preferred terms.  An example is HP:0000787, 'Nephrolithiasis', which maps to a CUI containing what SNOMED CT refers to as a synonym, 'Nephrolithiasis', but not the preferred term of 'Kidney Stone'.

`https://uts-ws.nlm.nih.gov/rest/content/2015AB/CUI/C0001126/atoms?sabs=SNOMEDCT_US&ttys=PT,SY&ticket=<your-ticket>`

In this example we receive the following Atom object:

~~~~.json
{
pageSize: 25,
pageNumber: 1,
pageCount: 1,
result: [
  {
   classType: "Atom",
   ui: "A2872556",
   suppressible: "false",
   obsolete: "false",
   rootSource: "SNOMEDCT_US",
   termType: "PT",
   code: "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/1776003",
   concept: "https://uts-ws.nlm.nih.gov/rest/content/2015AB/CUI/C0001126",
   sourceConcept: "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/1776003",
   sourceDescriptor: "NONE",
   attributes: "https://uts-ws.nlm.nih.gov/rest/content/2015AB/AUI/A2872556/attributes",
   parents: "NONE",
   ancestors: null,
   children: "NONE",
   descendants: null,
   relations: "NONE",
   definitions: "NONE",
   name: "Renal tubular acidosis",
   language: "ENG"
  }
]
}

~~~~

Finally, make one additional `GET` call to the SNOMED CT sourceConcept URI - `https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/1776003?ticket=<your-ticket>`
This exposes complete information about the SNOMED CT concept, such as links to additional properties (attributes), parents, children, descendants, etc.

~~~~.json
{
pageSize: 25,
pageNumber: 1,
pageCount: 1,
   result: {
   classType: "SourceAtomCluster",
   ui: "1776003",
   suppressible: false,
   obsolete: false,
   rootSource: "SNOMEDCT_US",
   atomCount: 8,
   cVMemberCount: 0,
   attributes: "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/1776003/attributes",
   atoms: "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/1776003/atoms",
   descendants: "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/1776003/descendants",
   ancestors: "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/1776003/ancestors",
   parents: "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/1776003/parents",
   children: "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/1776003/children",
   relations: "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/1776003/relations",
   definitions: "NONE",
   concepts: "https://uts-ws.nlm.nih.gov/rest/search/2015AB?string=1776003&sabs=SNOMEDCT_US&searchType=exact&inputType=sourceUi",
   defaultPreferredAtom: "https://uts-ws.nlm.nih.gov/rest/content/2015AB/source/SNOMEDCT_US/1776003/atoms/preferred",
   name: "Renal tubular acidosis"
   }
}
~~~~