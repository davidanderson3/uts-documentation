<p>
  <#if content.uri?matches("rest/home.html")><a href = "https://www.nlm.nih.gov/research/umls">UMLS Home</a> &raquo; UMLS REST API 
  <#else><a href = "https://www.nlm.nih.gov/research/umls">UMLS Home</a> &raquo; <a href = "/rest/home.html">UMLS REST API </a> &raquo; <b>${content.title}</b>
  </#if>
</p>
