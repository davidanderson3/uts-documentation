title=Python Scripts
date=2022-07-12
updated=2022-07-12
type=page
status=published
category=REST API Cookbook
navorder=2
~~~~~~

Try these python scripts:

#### Crosswalking Vocabularies Using CUIs

This script will crosswalk from a set of codes in one UMLS source vocabulary to a set of codes in another UMLS source vocabulary as long as the codes share a UMLS Concept. 

**Script**: [crosswalk.py](/scripts/crosswalk.py)

**Usage**: python crosswalk.py -k YOUR_API_KEY -s HPO -t SNOMEDCT_US -i hpo-codes.txt -o output.txt

**Sample Input File**: [hpo-codes.txt](/scripts/hpo-codes.txt)

**Documentation**: [Crosswalk API Endpoint](/rest/source-asserted-identifiers/crosswalk/index.html)

<hr>

#### Get Codes for a List of Concepts

This script will take a list of CUIs and return the corresponding codes for a particular UMLS source vocabulary. 

**Script**: [get-codes-for-a-list-of-concepts.py](/scripts/get-codes-for-a-list-of-concepts.py)

**Usage**: python get-codes-for-a-list-of-concepts.py -k YOUR_API_KEY -i cuis.txt -o output.txt -s SNOMEDCT_US

**Documentation**: [Search API Endpoint](/rest/search/index.html)

<hr>

#### Get Concepts for a List of Codes

This script will take a list of codes and return the corresponding concepts for a particular UMLS source vocabulary. 

**Script**: [get-concepts-for-a-list-of-codes.py](/scripts/get-concepts-for-a-list-of-codes.py)

**Usage**: python get-codes-for-a-list-of-concepts.py -k YOUR_API_KEY -i cuis.txt -o output.txt -s SNOMEDCT_US

**Documentation**: [Search API Endpoint](/rest/search/index.html)

<hr>

#### Get Concepts for a List of Strings

This script will take a list of strings and return the corresponding concepts for one or more UMLS source vocabularies. 

**Script**: [get-concepts-for-a-list-of-strings.py](/scripts/get-concepts-for-a-list-of-strings.py)

**Usage**: python get-concepts-for-a-list-of-strings.py -k YOUR_API_KEY -i strings.txt -o output.txt

**Documentation**: [Search API Endpoint](/rest/search/index.html)

<hr>

#### Retrieve Atoms Using a CUI or Code

This script will return atoms from a single CUI or code. If using a code, a source vocabulary must be specified.

**Script**: [retrieve-names-for-cui-or-code.py](/scripts/retrieve-names-for-cui-or-code.py)

**Usage**: python retrieve-names-for-cui-or-code.py -k YOUR_API_KEY -i C0018787

**Documentation**: [Concept API Endpoint](/rest/concept/index.html), [Source-Asserted Information API Endpoint](/rest/source-asserted-identifiers/index.html)

<hr>

#### Search for a Term 

This script will return CUIs and associated information for a search term.

**Script**: [search-terms.py](/scripts/search-terms.py)

**Usage**: python search-terms.py -k YOUR_API_KEY -s diabetic-foot

**Documentation**: [Search API Endpoint](/rest/search/index.html)

<hr>

#### Retrieve ancestors, descendants, parents, or children 

This script returns ancestors, descendants, parents, or children for a source-asserted code.

**Script**: [walk-hierarchy.py](/scripts/walk-hierarchy.py)

**Usage**: python walk-hierarchy.py -k YOUR_API_KEY -i 9468002 -s SNOMEDCT_US -o ancestors / descendants / parents / children 

**Documentation**: [Source-Asserted Information API Endpoint](/rest/source-asserted-identifiers/index.html)

<hr>

#### Get Semantic Types for a List of Strings

This script returns semantic types for concepts returned by string searches.

**Script**: [get_semantic_types_for_a_list_of_strings.py](/scripts/get_semantic_types_for_a_list_of_strings.py)

**Usage**: python get_semantic_types_for_a_list_of_strings.py -k YOUR_API_KEY -i strings.txt -o output.txt

**Documentation**: [Searching the UMLS API Endpoint](/rest/search/index.html), [Retrieving UMLS Concept Information API Endpoint](/rest/concept/index.html)

<hr>






