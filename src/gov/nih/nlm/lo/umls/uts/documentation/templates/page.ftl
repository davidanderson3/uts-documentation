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
	<div class = "container">
	<#if (content.uri)??  && content.uri?starts_with("rest/")>
        <div id = "uts-notice">
        <p>We welcome your feedback on our <a href = "http://support.nlm.nih.gov/support/create-case/">customer service form</a>. Please use &quot;UMLS REST API feedback&quot; in your subject line.</p>
        <p>Check out the <a href = "/rest/rest-api-cookbook/postman.html">Postman sample collections</a>, or <a href = "https://github.com/HHS/uts-rest-api">code samples in Python, Java, and Perl on Github</a> to help you get started using the UMLS REST API.</p>
        <p><a href="/terms-of-service.html">API Terms of Service</a></p>
	</div>
	
	</#if>
	<#if (content.uri)??  && content.uri?starts_with("soap/")>
	<br/>
          <p style="background-color:pink;font-size:3em;">
          The UMLS SOAP API was discontinued December 31, 2020. SOAP API users are encouraged to switch to the <a href="https://documentation.uts.nlm.nih.gov/rest/home.html">REST API</a>.</p>
          </p>
	</#if>
	
	<h1><#escape x as x?xml>${content.title}</#escape></h1>
	${content.body}
	<#if (content.uri)??  && content.uri?starts_with("rest/authentication.html")>
	<#include "authdemo.ftl">
	</#if>
	</div>
	</div>
<#include "footer.ftl">