<#if (content.uri)?? && content.uri?starts_with("soap/")>
<p>
  <#if content.uri?matches("soap/home.html")><a href = "https://www.nlm.nih.gov/research/umls">UMLS Home</a> &raquo; <a href="/">API Technical Documentation</a> &raquo; SOAP API
  <#else><a href = "https://www.nlm.nih.gov/research/umls">UMLS Home</a> &raquo; <a href="/">API Technical Documentation</a> &raquo; <a href = "/soap/home.html">SOAP API</a> &raquo; <b>${content.title}</b>
  </#if>
</p>
</#if>
<#if (content.uri)?? && content.uri?starts_with("rest/")>
<p>
  <#if content.uri?matches("rest/home.html")><a href = "https://www.nlm.nih.gov/research/umls">UMLS Home</a> &raquo; <a href="/">API Technical Documentation</a> &raquo; REST API 
  <#else><a href = "https://www.nlm.nih.gov/research/umls">UMLS Home</a> &raquo; <a href="/">API Technical Documentation</a> &raquo; <a href = "/rest/home.html">REST API </a> &raquo; <b>${content.title}</b>
  </#if>
</p>
</#if>