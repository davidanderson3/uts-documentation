title=Automating UMLS Terminology Services Downloads 
date=2020-12-28
updated=2022-11-09
type=page
status=published
navorder=1
~~~~~~
<hr />

**Download any [RxNorm](https://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html), [SNOMED CT](https://www.nlm.nih.gov/healthit/snomedct/index.html), or [UMLS](https://www.nlm.nih.gov/research/umls/licensedcontent/umlsknowledgesources.html) release using our download API.**
<hr />
#### **Step 1**: Get your API key from your UTS profile.

* You can find the API key in the [UTS 'My Profile' area](https://uts.nlm.nih.gov/uts/) after signing in. An API key remains active as long as the associated UTS account is active.

#### **Step 2**: Find the URL for the file you want to download and send a request. Examples:

<hr />
####Download RxNorm Weekly Updates####
https://uts-ws.nlm.nih.gov/download<br/><b>?url=</b>https://download.nlm.nih.gov/umls/kss/rxnorm/RxNorm_weekly_10052022.zip<br/><b>&apiKey=</b>YOUR_API_KEY 

curl example:

~~~~text
curl "https://uts-ws.nlm.nih.gov/download?url=https://download.nlm.nih.gov/umls/kss/rxnorm/RxNorm_weekly_10052022.zip&apiKey=YOUR_API_KEY" -o RxNorm_weekly_10052022.zip
~~~~
<hr />
####Download the US Edition of SNOMED CT####
https://uts-ws.nlm.nih.gov/download<br/><b>?url=</b>https://download.nlm.nih.gov/mlb/utsauth/USExt/SnomedCT_USEditionRF2_PRODUCTION_20220901T120000Z.zip<br/><b>&apiKey=</b>YOUR_API_KEY 

curl example:

~~~~text
curl "https://uts-ws.nlm.nih.gov/download?url=https://download.nlm.nih.gov/mlb/utsauth/USExt/SnomedCT_USEditionRF2_PRODUCTION_20220901T120000Z.zip&apiKey=YOUR_API_KEY" -o SnomedCT_USEditionRF2_PRODUCTION_20220901T120000Z.zip
~~~~
<hr />
####Download the UMLS Release####
https://uts-ws.nlm.nih.gov/download<br/><b>?url=</b>https://download.nlm.nih.gov/umls/kss/2022AA/umls-2022AA-full.zip<br/><b>&apiKey=</b>YOUR_API_KEY 

curl example:

~~~~text
curl "https://uts-ws.nlm.nih.gov/download?url=https://download.nlm.nih.gov/umls/kss/2022AA/umls-2022AA-full.zip&apiKey=YOUR_API_KEY" -o umls-2022AA-full.zip
~~~~
<hr />
