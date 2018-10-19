<#include "header.ftl">
	<#include "uts-documentation-menu.ftl">
	<div id = "breadcrumb-div">
	<#include "breadcrumbs.ftl">
	</div>
	<div class = "row">
	<div class = "container-fluid">
	<#if (content.uri)??  && content.uri?starts_with("rest/")>
	<br/>
	<!-- <p class = "red"><b>Current REST API Version: ${config.restapi_version}</b></p> -->
        <div id = "uts-notice">
        <p>We welcome your feedback on our <a href = "http://support.nlm.nih.gov/support/create-case/">customer service form</a>. Please use &quot;UMLS REST API feedback&quot; in your subject line.</p>
        <p>Check out the <a href = "/rest/rest-api-cookbook/postman.html">Postman sample collections</a>, or <a href = "https://github.com/HHS/uts-rest-api">code samples in Python, Java, and Perl on Github</a> to help you get started using the UMLS REST API.</p>
        <p><a href="/terms-of-service.html">API Terms of Service</a></p>
	</div>
	
	</#if>
	<#if (content.uri)??  && content.uri?starts_with("soap/")>
	<br/>
	<p class = "red"><b>Current SOAP API Version: ${config.soap_api_version}</b></p>
	</#if>
	
	<h1><#escape x as x?xml>${content.title}</#escape></h1>
	${content.body}
	<#if (content.uri)??  && content.uri?starts_with("rest/authentication.html")>
	<#include "authdemo.ftl">
	</#if>
	</div><!--end row-->
	</div><!--end container--> 
<#include "footer.ftl">