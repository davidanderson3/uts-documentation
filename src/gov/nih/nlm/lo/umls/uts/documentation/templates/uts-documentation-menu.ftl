<#assign categories = ['UMLS Concepts','Source-asserted data']>
<div class = "row header">
  <div class="container-fluid col-md-6 col-sm-8 col-xs-12">
    <a href = "https://www.nlm.nih.gov"><img class= "nlm-logo img-responsive" alt="National Library of Medicine" style="margin-right:1em;" src="<#if (content.rootpath)??>${content.rootpath}<#else></#if>nlm-logo.png"></a>
  </div>
</div>
<div class = "row">
  <div class="container-fluid uts-nav col-md-12 col-sm-8 col-xs-6">
        <a href="${content.rootpath}rest/home.html"><img class= "img-responsive pull-left" style = "padding-top:.2em; padding-left:1em;" alt="UTS Logo" style="margin-right:1em;" src="<#if (content.rootpath)??>${content.rootpath}<#else></#if>umls-xs.gif"></a>
        <p class = "orange uts-title">UMLS REST API Technical Documentation</p>
  </div>
</div>
<div class = "row">
  <div class = "container-fluid col-md-12 col-sm-8 col-xs-6 navbar navbar-default" role = "navigation">
  <!--
     <a class = "btn" href = "${content.rootpath}rest/authentication.html">User Authentication</a> | <a class = "btn" href = "${content.rootpath}rest/search/">Searching UMLS</a>
    | <a class = "btn" href = "${content.rootpath}rest/concept/">Retrieving Concept Information</a> | <a class = "btn" href = "${content.rootpath}rest/atoms/">Retrieving Atoms</a> 
    | <a class = "btn" href = "${content.rootpath}rest/source-asserted-identifiers/">Retrieving Source Asserted Data</a> | <a class = "btn" href = "${content.rootpath}rest/parents-and-children/">Parents and Children information</a>
 -->
 
<div class="btn-group navbar-btn visible-lg visible-md" role="group">
<#list published_pages as page>
<#if !(page.category)?? && page.uri != "rest/home.html"><#if (content.rootpath)??><a class = "btn btn-md" role = "button" href = "${content.rootpath}${page.uri}">${page.title}</a></li><#else></#if></#if>

</#list>
<#list categories as cat>
<div class="btn-group" role="group">
 <button type="button" class="btn btn-md dropdown-toggle" data-toggle="dropdown" aria-expanded="false">${cat}<span class = "caret"/></button>    
   <ul class = "dropdown-menu" role = "menu">
  <#list published_pages as page>
    <#if (page.category)?? && page.category = cat><li><#if (content.rootpath)??><a href = "${content.rootpath}${page.uri}">${page.title}</a></li><#else></#if></#if>
  </#list>
  </ul>
</div><!--//btn-group-->
</#list>


</div>
 
  </div>
</div>
<br/>