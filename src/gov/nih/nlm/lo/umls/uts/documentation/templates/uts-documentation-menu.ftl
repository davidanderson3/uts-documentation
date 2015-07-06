<div class = "row header">
  <div class="container-fluid col-md-6 col-sm-8 col-xs-12">
    <a href = "https://www.nlm.nih.gov"><img class= "nlm-logo img-responsive" alt="National Library of Medicine" style="margin-right:1em;" src="<#if (content.rootpath)??>${content.rootpath}<#else></#if>nlm-logo.png"></a>
  </div>
</div>
<div class = "row">
  <div class="container-fluid uts-nav navbar navbar-default col-md-12 col-sm-8 col-xs-6" role="navigation">
        <a href="${content.rootpath}rest/home.html"><img class= "img-responsive pull-left" style = "padding-top:.2em; padding-left:1em;" alt="UTS Logo" style="margin-right:1em;" src="<#if (content.rootpath)??>${content.rootpath}<#else></#if>umls-xs.gif"></a>
        <p class = "orange uts-title">UMLS REST API Technical Documentation</p>
     <div class = "row">
      <div class = "col-md-12 col-sm-8 col-xs-6">
          <a class = "btn" href = "${content.rootpath}rest/authentication.html">User Authentication</a> | <a class = "btn" href = "${content.rootpath}rest/search/">Searching UMLS</a>
    | <a class = "btn" href = "${content.rootpath}rest/concept/">Retrieving Concept Information</a> | <a class = "btn" href = "${content.rootpath}rest/atoms/">Retrieving Atoms</a> 
    | <a class = "btn" href = "${content.rootpath}rest/source-asserted-identifiers/">Retrieving Source Asserted Data</a>
      </div>
    </div>
  </div>
</div>
<br/>