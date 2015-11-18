<#include "header.ftl">
	<#include "uts-documentation-menu.ftl">
	<div class = "row">
	<div class = "container-fluid breadcrumbs-container">
	<#include "breadcrumbs.ftl">
	</div>
	</div>
	<div class = "row">
	<div class = "container-fluid">
	<#if (content.uri)??  && content.uri?starts_with("rest/")>
	<br/>
	<p class = "red"><b>API Version: ${config.restapi_version}</b></p>
        <p class = "notice">
	We welcome your feedback on our <a href = "http://apps.nlm.nih.gov/mainweb/siebel/nlm/index.cfm">customer service form</a>.
	Please use &quot;UMLS REST API feedback&quot; in your subject line.<br/>
	Check out the <a href = "https://github.com/HHS/uts-rest-api">code samples in Python, Java, and Perl on Github</a> to help you get started using the UMLS REST API.
	</p>
	
	</#if>
	
	<h1><#escape x as x?xml>${content.title}</#escape></h1>
	${content.body}
	</div><!--end row-->
	</div><!--end container--> 
<#include "footer.ftl">