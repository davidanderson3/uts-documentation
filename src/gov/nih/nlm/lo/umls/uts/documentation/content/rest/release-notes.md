title=Release Notes
date=2015-07-06
updated=2015-07-06
type=page
status=unpublished
~~~~~~

**API Version:** 0.2 alpha
Released: July 10, 2015

_Change to URL request structure_
Users no longer need to include a trailing forward slash at the end of their REST calls. For example, _/CUI/C0018787/atoms_ - without a forward slash following the word 'atoms' - is a valid call in Version 0.2 alpha. The JSON output from the REST API no longer includes trailing forward slashes either.

_Retrieving atoms for source asserted identifiers_
Users can retrieve all of the atoms associated with a source asserted identifier. The REST call must include the root source abbreviation (sab) and the source asserted identifier, as in _/content/2015AA/SNOMEDCT&#95;US/226617008/atoms_. The resulting output in this example is all of the atoms associated with SNOMEDCT&#95;US ConceptID 226617008:

* A24131514/Hot cereal 
* A3186248/Porridge 
* A3638864/Porridge (substance) 

_Searches returning no results_
For searches returning no results, users will no longer receive a results:null JSON object, as was the case in Version 0.1 alpha. To prevent users from having to perform null checks for _/search_ calls, a search with no results returns the following:

    {"result":{"classType":"searchResults","results":[{"ui":null,"name":"NO RESULTS"}]},"pageNum":1,"pageSize":25}

