<#include "header.ftl">
        
	<#include "uts-documentation-menu.ftl">
	<div class = "row">
	<div class = "container">
	<div class="page-header">
		<h1><#escape x as x?xml>${content.title}</#escape></h1>
	</div>

	<p><em>${content.date?string("dd MMMM yyyy")}</em></p>

	<p>${content.body}</p>

	</div><!--end row-->
	</div><!--end container-->
        
<#include "footer.ftl">