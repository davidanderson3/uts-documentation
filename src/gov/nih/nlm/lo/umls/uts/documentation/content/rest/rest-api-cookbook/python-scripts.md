title=Python Scripts
date=2022-07-12
updated=2022-07-12
type=page
status=published
category=REST API Cookbook
navorder=2
~~~~~~

Try these python scripts:



####Crosswalking Vocabularies Using CUIs

This script will crosswalk from a set of codes in one UMLS source vocabulary to a set of codes in another UMLS source vocabulary as long as the codes share a UMLS Concept. 

**Script**: [crosswalk.py](/scripts/crosswalk.py)

**Usage**: python crosswalk.py -k YOUR_API_KEY -s HPO -t SNOMEDCT_US -i hpo-codes.txt -o output.txt

**Sample Input File**: [hpo-codes.txt](/scripts/hpo-codes.txt)

**Documentation**: [Crosswalk API Endpoint](/rest/source-asserted-identifiers/crosswalk/index.html)

<hr>

####Get Codes for a List of Concepts

This script will take a list of CUIs and return the corresponding codes for a particular UMLS source vocabulary. 

**Script**: [get-codes-for-a-list-of-concepts.py](/scripts/get-codes-for-a-list-of-concepts.py)

**Usage**: python get-codes-for-a-list-of-concepts.py -k YOUR_API_KEY -i cuis.txt -o output.txt -s SNOMEDCT_US

**Documentation**: [Search API Endpoint](/rest/search/index.html)

<hr>





