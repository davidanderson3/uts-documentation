<#if (content.uri)?? && content.uri?starts_with("soap/")>
<span class = "breadcrumbs">
  <#if content.uri?matches("soap/home.html")><a href = "https://www.nlm.nih.gov/research/umls">UMLS Home</a> &raquo; UMLS SOAP API Home
  <#else><a href = "https://www.nlm.nih.gov/research/umls">UMLS Home</a> &raquo; <a href="https://documentation.uts.nlm.nih.gov">UMLS API Technical Documentation Home</a> &raquo; <a href = "/soap/home.html">UMLS SOAP API Home</a> &raquo; <b>${content.title}</b>
  </#if>
</span>
</#if>
<#if (content.uri)?? && content.uri?starts_with("rest/")>
<span class = "breadcrumbs">
  <#if content.uri?matches("rest/home.html")><a href = "https://www.nlm.nih.gov/research/umls">UMLS Home</a> &raquo; UMLS REST API Home
  <#else><a href = "https://www.nlm.nih.gov/research/umls">UMLS Home</a> &raquo; <a href="https://documentation.uts.nlm.nih.gov">UMLS API Technical Documentation Home</a> &raquo; <a href = "/rest/home.html">UMLS REST API Home</a> &raquo; <b>${content.title}</b>
  </#if>
</span>
</#if>