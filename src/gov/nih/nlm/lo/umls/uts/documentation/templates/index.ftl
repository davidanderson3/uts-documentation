<#include "header.ftl">
	
	<#include "uts-documentation-menu.ftl">
	<h1><#escape x as x?xml>UTS Technical Documentation Sitemap</#escape></h1>
         
        <div class = "row">
	<div class = "container-fluid col-md-12 col-sm-8 col-xs-6">

	<#list published_pages as page>
  		<#if (page.status == "published")>
  			<a href="${page.uri}"><h4><#escape x as x?xml>${page.title}</#escape></h4></a>
  			<p>${page.date?string("dd MMMM yyyy")}</p>
  			
  		</#if>
  	</#list>
	
	</div>
	</div>

<#include "footer.ftl">