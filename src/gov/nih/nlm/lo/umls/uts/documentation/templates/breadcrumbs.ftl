<#if (content.uri)??  && content.uri?starts_with("soap/")>
<span class = "breadcrumbs"><a href = "/soap/home.html">SOAP API HOME</a> &gt;&gt; <#if (page.uri)??>${page.title}</#if></span>
</#if>
<#if (content.uri)??  && content.uri?starts_with("rest/")>
<span class = "breadcrumbs"><a href = "/rest/home.html">REST API HOME</a> &gt;&gt; <#if (page.uri)??>${page.title}</#if></span>
</#if>