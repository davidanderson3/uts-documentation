title=Automating UMLS Terminology Services Downloads 
date=2020-12-28
updated=2023-10-03
type=page
status=published
navorder=1
~~~~~~
<p>This documentation will help you to:</p>
<ol>
<li>
<p><a href="#release-api">Get the latest release files for RxNorm, SNOMED CT, and UMLS</a> <strong>(Release API)</strong></p>
</li>
<li>
<p><a href="#download-api">Download release files automatically</a> <strong>(Download API)</strong></p>
</li>
</ol>
<hr />
<h2 id="release-api"><a name="release-api"></a>Release API</h2>
<p>This API endpoint provides a list of releases for RxNorm, SNOMED CT, and UMLS. You can use this endpoint to get the latest release or to obtain past releases. </p>
<p><strong>Base URL: https://uts-ws.nlm.nih.gov/releases</strong></p>
<table class="table">
<thead>
<tr>
<th>Parameter name </th>
<th>Required? Y/N </th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>releaseType</td>
<td>N </td>
<td>You can find a list of releaseTypes here: <a href="https://uts-ws.nlm.nih.gov/releases">https://uts-ws.nlm.nih.gov/releases</a> </td>
</tr>
 <tr>
<td>current</td>
<td>N </td>
<td>Defaults to false. Set to current=true to get only the current release. </td>
</tr>
</tbody>
</table>
<h3 id="rxnorm">RxNorm</h3>
<table class="table">
<thead>
<tr>
<th>Release</th>
<th>Parameter</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://uts-ws.nlm.nih.gov/releases?releaseType=rxnorm-full-monthly-release">RxNorm Full Monthly Release</a></td>
<td>releaseType=rxnorm-full-monthly-release</td>
</tr>
<tr>
<td><a href="https://uts-ws.nlm.nih.gov/releases?releaseType=rxnorm-weekly-updates">RxNorm Weekly Updates</a></td>
<td>releaseType=rxnorm-weekly-updates</td>
</tr>
<tr>
<td><a href="https://uts-ws.nlm.nih.gov/releases?releaseType=rxnorm-prescribable-content-monthly-release">RxNorm Prescribable Content Monthly Release</a></td>
<td>releaseType=rxnorm-prescribable-content-monthly-release</td>
</tr>
<tr>
<td><a href="https://uts-ws.nlm.nih.gov/releases?releaseType=rxnorm-prescribable-content-weekly-updates">RxNorm Prescribable Content Weekly Updates</a></td>
<td>releaseType=rxnorm-prescribable-content-weekly-updates</td>
</tr>
<tr>
<td><a href="https://uts-ws.nlm.nih.gov/releases?releaseType=rxnav-in-a-box">RxNav-in-a-Box</a></td>
<td>releaseType=rxnav-in-a-box</td>
</tr>
</tbody>
</table>
<h3 id="snomed-ct">SNOMED CT</h3>
<table class="table">
<thead>
<tr>
<th>Release</th>
<th>Parameter</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://uts-ws.nlm.nih.gov/releases?releaseType=snomed-ct-us-edition">SNOMED CT US Edition</a></td>
<td>releaseType=snomed-ct-us-edition</td>
</tr>
<tr>
<td><a href="https://uts-ws.nlm.nih.gov/releases?releaseType=snomed-ct-us-edition-transitive-closure-resources">SNOMED CT US Edition Transitive Closure Resources</a></td>
<td>releaseType=snomed-ct-us-edition-transitive-closure-resources</td>
</tr>
<tr>
<td><a href="https://uts-ws.nlm.nih.gov/releases?releaseType=snomed-ct-international-edition">SNOMED CT International Edition</a></td>
<td>releaseType=snomed-ct-international-edition</td>
</tr>
<tr>
<td><a href="https://uts-ws.nlm.nih.gov/releases?releaseType=snomed-ct-core-problem-list-subset">SNOMED CT CORE Problem List Subset</a></td>
<td>releaseType=snomed-ct-core-problem-list-subset</td>
</tr>
<tr>
<td><a href="https://uts-ws.nlm.nih.gov/releases?releaseType=snomed-ct-to-icd-10-cm-mapping-resources">SNOMED CT to ICD-10-CM Mapping Resources</a></td>
<td>releaseType=snomed-ct-to-icd-10-cm-mapping-resources</td>
</tr>
<tr>
<td><a href="https://uts-ws.nlm.nih.gov/releases?releaseType=snomed-ct-spanish-edition">SNOMED CT Spanish Edition</a></td>
<td>releaseType=snomed-ct-spanish-edition</td>
</tr>
</tbody>
</table>
<h3 id="umls">UMLS</h3>
<table class="table">
<thead>
<tr>
<th>Release</th>
<th>Parameter</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://uts-ws.nlm.nih.gov/releases?releaseType=umls-metathesaurus-full-subset">UMLS Metathesaurus Full Subset</a></td>
<td>releaseType=umls-metathesaurus-full-subset</td>
</tr>
<tr>
<td><a href="https://uts-ws.nlm.nih.gov/releases?releaseType=umls-metathesaurus-mrconso-file">UMLS Metathesaurus MRCONSO File</a></td>
<td>releaseType=umls-metathesaurus-mrconso-file</td>
</tr>
<tr>
<td><a href="https://uts-ws.nlm.nih.gov/releases?releaseType=umls-full-release">UMLS Full Release</a></td>
<td>releaseType=umls-full-release</td>
</tr>
</tbody>
</table>
</ul>
<h2><a name="download-api"></a>Download API</h2>
<p>This API endpoint allows you to download RxNorm, SNOMED CT, or UMLS releases by providing the download URL and your API key.</p>
<p><strong>Base URL: https://uts-ws.nlm.nih.gov/download</strong></p>
<table class="table">
<thead>
<tr>
<th>Parameter name </th>
<th>Required? Y/N </th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>url</td>
<td>Y </td>
<td>Provide the URL for the release you wish to download. </td>
</tr>
<tr>
<td>apiKey </td>
<td>Y </td>
<td>An API key is required for each call to the API. Visit <a href="https://uts.nlm.nih.gov/uts/profile">your UTS profile</a> to obtain your API key. </td>
</tr>
</tbody>
</table>
<hr />
<h3>Examples</h3>
<h5>Download RxNorm Weekly Updates</h5>
https://uts-ws.nlm.nih.gov/download<br /><b>?url=</b>https://download.nlm.nih.gov/umls/kss/rxnorm/RxNorm_weekly_10052022.zip<br /><b>&apiKey=</b>YOUR_API_KEY
<br /><br />
<p>curl example:</p>
 curl &quot;https://uts-ws.nlm.nih.gov/download?url=https://download.nlm.nih.gov/umls/kss/rxnorm/RxNorm_weekly_10052022.zip&amp;apiKey=YOUR_API_KEY&quot; -o RxNorm_weekly_10052022.zip
<hr />

<h5>Download the US Edition of SNOMED CT</h5>
https://uts-ws.nlm.nih.gov/download<br /><b>?url=</b>https://download.nlm.nih.gov/mlb/utsauth/USExt/SnomedCT_USEditionRF2_PRODUCTION_20220901T120000Z.zip<br /><b>&apiKey=</b>YOUR_API_KEY
<br /><br />
<p>curl example:</p>
curl &quot;https://uts-ws.nlm.nih.gov/download?url=https://download.nlm.nih.gov/mlb/utsauth/USExt/SnomedCT_USEditionRF2_PRODUCTION_20220901T120000Z.zip&amp;apiKey=YOUR_API_KEY&quot; -o SnomedCT_USEditionRF2_PRODUCTION_20220901T120000Z.zip
<hr />
<h5>Download the UMLS Release</h5>
https://uts-ws.nlm.nih.gov/download<br /><b>?url=</b>https://download.nlm.nih.gov/umls/kss/2022AA/umls-2022AA-full.zip<br /><b>&apiKey=</b>YOUR_API_KEY
<br /><br />
<p>curl example:</p>
curl 
&quot;https://uts-ws.nlm.nih.gov/download?url=https://download.nlm.nih.gov/umls/kss/2022AA/umls-2022AA-full.zip&amp;apiKey=YOUR_API_KEY&quot; -o umls-2022AA-full.zip
<hr />

