title=Validating UMLS Licensees for Third-Party Application Developers
date=2020-02-07
updated=2024-03-01
type=page
status=published
navorder=1
~~~~~~

We offer an endpoint for validating API keys. If you have developed an application that integrates UMLS data and you need to determine whether a user is a UMLS licensee, you can use this endpoint to validate the user’s API key.

Make a request that includes both your API key (validatorApiKey) and the API key of the user of your application (apiKey). For example:

https://utslogin.nlm.nih.gov/validateUser?validatorApiKey=YOUR_API_KEY&apiKey=USER_API_KEY

If you would like to validate UMLS licensees via our sign in page (<a href="https://uts.nlm.nih.gov/uts/login">https://uts.nlm.nih.gov/uts/login</a>), please <a href="https://support.nlm.nih.gov/support/create-case/">contact us.</a>

