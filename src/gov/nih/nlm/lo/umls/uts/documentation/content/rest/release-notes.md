title=Release Notes and Roadmap
date=2015-11-09
updated=2016-05-18
type=page
status=published
navorder=1
~~~~~~

Released: May 9, 2016

#### Features:
* **The API has been updated with data from the 2016AA UMLS release. Calls including 'current' in the URI will query the 2016AA data**.

* **New endpoint created for retrieving [Content View information](/rest/content-views/index.html)**.

* **The API key method gives users an additional [authentication](authentication.html) option when requesting a Ticket-Granting Ticket (TGT).  Rather than username/password, users can pass their API key (available in the UTS 'My Profile' area) as a parameter to this method to obtain a TGT**.

#### Change:
* **The output for source-asserted relation calls has been modified to include relatedId and relatedIdName. See the source-asserted relation [sample output](/rest/source-asserted-identifiers/relations/index.html#sample-output) for an example**.

  
#### Known issues:

See our github sample code area for a list of [known issues](https://github.com/HHS/uts-rest-api/issues) with the API.

#### Planned Updates

The following new items are planned for upcoming versions of the API.    

##### Features:

* **Add a crosswalk endpoint that allows users to find codes from one vocabulary that live in the same CUI as codes from another vocabulary.**

* **Add history mechanism so users can retrieve CUIs that are no longer in the latest UMLS release**
