<#include "header.ftl">

	<#include "uts-documentation-menu.ftl">
<div class="container-fluid uts-breadcrumbs">
<div class="container">
	<div id = "breadcrumb-div">
	<#include "breadcrumbs.ftl">
	</div>
	
	</div>
</div>
	<div class = "container-fluid">
	<div class = "container uts-container">
        <div id = "uts-notice">
        <p>We welcome your feedback on our <a href = "http://support.nlm.nih.gov/support/create-case/">customer service form</a>. Please use &quot;UMLS REST API feedback&quot; in your subject line.</p>
        <p>Check out the <a href = "/rest/rest-api-cookbook/postman.html">Postman sample collection</a> to help you get started using the UMLS REST API.</p>
        <p><a href="/terms-of-service.html">API Terms of Service</a></p>
        <#if (content.uri)??  && content.uri?starts_with("rest/home.html")>
        <hr>
        <h2>Change Log</h2>
        <hr>
        <h5>2023-12-19</h5>
		<p> 
		We are pleased to announce the publication of a (/automating-downloads.html)[new API endpoint for NLM terminology releases]. 
		This endpoint provides an updated list of releases for many of our terminology products. You can 
		use this endpoint to automate the download of the latest release files for RxNorm, SNOMED CT, and UMLS. 
		<hr>
        <h5>2023-07-12</h5>
		<p>We have made adjustments to the way in which the search API stems individual words.  
		The most significant impact is that queries that include plural forms of words will now find singular forms, 
		for example, a query for "lungs" will find all instances of "lung". In general, API search queries 
		and search queries in the Metathesaurus Browser will produce a higher number of results than before.</p>
		<hr>
        <h5>2023-05-09</h5>
        <p>We now offer an endpoint for validating API keys. If you have developed an application that integrates UMLS data and you need to determine whether a user is a UMLS licensee, you can use this endpoint to validate the user's API key.<br/><br/>
		Make a request that includes both your API key (validatorApiKey) and the API key of the user of your application (apiKey). For example:<br/><br/>
		<code>https://utslogin.nlm.nih.gov/validateUser?validatorApiKey=YOUR_API_KEY&apiKey=USER_API_KEY
		</code>
		<br/><br/>
		For more information see our  
        <a href="/rest/authentication.html">authentication documentation</a>.
		</p>
		<hr>
        <h5>2022-12-28</h5>
        <p><b>Search for partial matches</b>, for example: <br/><br/>
        <code>
		/search/current<br/>
		?string=Congenital Nephrogenic Diabetes Insipidus<br/>
		&partialSearch=true
		</code>
		<br/><br/>
		Adding partialSearch=true to your search query will return partial matches. If your query contains four words, it will return results that include all four words, then results that contain three of four words, then two of four words, then one of four words. 
		<br/><br/>
		For more information see our <a href="/rest/search/index.html">
        search documentation</a>.</p>
		<hr>
        <h5>2022-10-05</h5>
        <p><b>Download any RxNorm, SNOMED CT, or UMLS release using a single command</b>, for example: <br/><br/>
        <code>
		curl <br/>
		"https://uts-ws.nlm.nih.gov/download<br/>
		?url=https://download.nlm.nih.gov/<br/>
		umls/kss/rxnorm/<br/>
		RxNorm_weekly_10052022.zip<br/>
		&apiKey=YOUR_API_KEY" <br/>
		-o RxNorm_weekly_10052022.zip
		</code>
		<br/><br/>
		For more information, see our <a href="../automating-downloads.html">Automating UMLS Terminology Services Downloads page</a>.</p>
		<hr>
        <h5>2022-07-13</h5>
        <p><b>Search for a CUI, return a source-asserted code</b>: The search endpoint now supports searching for a UMLS CUI and returning a source-asserted
        code, for example:
        <br/> 
        <code>
        <br/>/search/current
        <br/>?string=C0009044
        <br/>&sabs=SNOMEDCT_US
        <br/>&returnIdType=code. 
    	</code>
    	<br/>
        <br/>For more information see our <a href="/rest/relations/index.html">
        search documentation</a>.</p>
        <hr>
        <h5>2022-06-06</h5>
        <p><b>Changes to the concept relations endpoint</b>: The <a href="/rest/relations/index.html">concept relations api endpoint</a> will return any relation associated with a
        UMLS CUI, including source-asserted relations. Previously, this endpoint only returned NLM-asserted relations. </p>
		<hr>
        <h5>2022-05-02</h5>
        <p><b>New authentication method</b>: Users can request data by simply including an API key with a data request. For more information see:
        <a href="https://www.nlm.nih.gov/pubs/techbull/mj22/mj22_umls_2022aa_release.html">2022AA release announcement</a> and 
        <a href="/rest/authentication.html">authentication documentation.</a> Ticket-granting tickets and service tickets are 
        deprecated.
        <hr>
        <h5>2022-04-12</h5>
        <p><b>Changes to API search</b>: The UMLS API started using ElasticSearch for search. Users may notice changes in search ranking.</p>
        <p><b>Changes to relation data returned</b>: Relations api requests will return additional data fields: relatedFromId and relatedFromIdName.
        These data fields indicate the subject of the relationship, which can be a code, CUI, AUI, SCUI, or SDUI. See the sample output on the 
        <a href="/rest/source-asserted-identifiers/relations/index.html">source-asserted relations documentation page</a>.</p>
        </#if>
	</div>
		
	<h1><#escape x as x?xml>${content.title}</#escape></h1>
	${content.body}
	</div>
	</div>
<#include "footer.ftl">