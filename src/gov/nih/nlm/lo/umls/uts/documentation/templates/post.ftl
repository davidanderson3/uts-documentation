<#include "header.ftl">
	
	<#include "uts-documentation-menu.ftl">
	<h1> UMLS Use </h1>
	<p> A blog about use of the Unified Medical Language System.
	<div class="page-header">
		<h1><#escape x as x?xml>${content.title}</#escape></h1>
	</div>

	<p><em>${content.date?string("dd MMMM yyyy")}</em></p>

	<p>${content.body}</p>

	<hr />
	
<#include "footer.ftl">