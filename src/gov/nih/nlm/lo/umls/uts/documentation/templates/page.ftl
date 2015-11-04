<#include "header.ftl">
	<#include "uts-documentation-menu.ftl">
	<div class = "row">
	<div class = "container-fluid breadcrumbs-container">
	<#include "breadcrumbs.ftl">
	</div>
	</div>
	<div class = "row">
	<div class = "container-fluid main-content-container">
	<#if (content.uri)??  && content.uri?starts_with("rest/")>
	<br/>
	<p class = "red"><b>API Version: ${config.restapi_version}</b></p>
        <p class = "notice"><span class = "red">The UMLS REST API is currently in beta mode and is ready for you to try out!</span><br/>
	We welcome your feedback on our <a href = "http://apps.nlm.nih.gov/mainweb/siebel/nlm/index.cfm">customer service form</a>.
	Please use &quot;UMLS REST API feedback&quot; in your subject line.</p>
	</#if>
	
	<h1><#escape x as x?xml>${content.title}</#escape></h1>
	${content.body}
	</div><!--end row-->
	</div><!--end container--> 
<#include "footer.ftl">
</div>