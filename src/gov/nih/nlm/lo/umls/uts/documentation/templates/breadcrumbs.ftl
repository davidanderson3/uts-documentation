<#if (content.uri)?? && content.uri?starts_with("soap/")>
<span class = "breadcrumbs">
  <#if content.uri?matches("soap/home.html")>UMLS SOAP API Home
  <#else><a href = "/soap/home.html">UMLS SOAP API Home</a> &raquo; <b>${content.title}</b>
  </#if>
</span>
</#if>
<#if (content.uri)?? && content.uri?starts_with("rest/")>
<span class = "breadcrumbs">
  <#if content.uri?matches("rest/home.html")>UMLS REST API Home
  <#else><a href = "/rest/home.html">UMLS REST API Home</a> &raquo; <b>${content.title}</b>
  </#if>
</span>
</#if>