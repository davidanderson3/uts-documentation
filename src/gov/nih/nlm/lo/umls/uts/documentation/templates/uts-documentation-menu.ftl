<#assign categories = ['Retrieving UMLS Concepts', 'Retrieving Source-Asserted Data']>
<div class = "row header">
  <div class="container-fluid col-md-12 col-sm-12 col-xs-12">
     <div class = "row">
        <div class = "col-md-6 col-sm-6 col-xs-6">
            <a href = "https://www.nlm.nih.gov"><img class= "nlm-logo img-responsive" alt="National Library of Medicine" style="margin-right:1em;" src="<#if (content.rootpath)??>${content.rootpath}<#else></#if>nlm-logo.png"></a>
        </div>
       <div class = "col-md-6 col-sm-4 col-xs-2">
           <a class = "pull-right white" style = "margin-right:1em;" href="http://apps.nlm.nih.gov/mainweb/siebel/nlm/index.cfm">Contact NLM</a>
       </div>
    </div>
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
   <div class="btn-group navbar-btn visible-lg visible-md" role="group">
    <#list published_pages?sort_by('navorder') as page>
    <#if !(page.category)?? && page.uri != "rest/home.html"><#if (content.rootpath)??><a class = "btn btn-md" role = "button" href = "${content.rootpath}${page.uri}">${page.title}</a></li><#else></#if></#if>
    </#list>
      <#list categories as cat>
      <div class="btn-group" role="group">
        <button type="button" class="btn btn-md dropdown-toggle" data-toggle="dropdown" aria-expanded="false">${cat}<span class = "caret"/></button>    
         <ul class = "dropdown-menu" role = "menu">
          <#list published_pages?sort_by('navorder') as page>
           <#if (page.category)?? && page.category = cat><li><#if (content.rootpath)??><a href = "${content.rootpath}${page.uri}">${page.title}</a></li><#else></#if></#if>
          </#list>
         </ul>
      </div><!--//btn-group-->
     </#list>
   </div>
 </div>
</div>
<br/>