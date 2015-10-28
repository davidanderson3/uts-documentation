<#include "header.ftl">
	<#include "uts-documentation-menu.ftl">
	<div class = "row">
	<div class = "container-fluid">
	<#if (content.uri)??  && content.uri?starts_with("rest/")>
	<p class = "red"><b>API Version: ${config.restapi_version}</b></p>
        <p class = "notice"><span class = "red">The UMLS REST API is currently in beta mode.</span><br/>
	We welcome your feedback on our <a href = "http://apps.nlm.nih.gov/mainweb/siebel/nlm/index.cfm">customer service form</a>.
	Please use &quot;UMLS REST API feedback&quot; in your subject line.</p>
	</#if>
	
	<h1><#escape x as x?xml>${content.title}</#escape></h1>
	${content.body}
	</div><!--end row-->
	</div><!--end container--> 
<#include "footer.ftl">