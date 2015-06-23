<#include "header.ftl">
        
	<#include "uts-documentation-menu.ftl">
	<div class = "row">
	<div class = "container-fluid col-md-12 col-sm-8 col-xs-6">
	<h1><#escape x as x?xml>${content.title}</#escape></h1>

	${content.body}

	</div><!--end row-->
	</div><!--end container-->
        
<#include "footer.ftl">