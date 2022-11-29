<#assign categories=['Retrieving UMLS Data', 'Retrieving Source-Asserted Data' , 'REST API Cookbook' ]>

<div id="barbranding">
<div class="container">
<div class="row text-white pt-3 pb-2">
<div class="col breadcrumb-brand">
<div class="floating-s">
<h4 class="text-white">UMLS API Technical Documentation</h4>
</div>
<div class="floating-e">
<ul class="ps-0">


   
<li class="list-inline-item"><a class="text-white" href="//uts.nlm.nih.gov/uts/profile" title="Get Your API Key"><strong>Get Your API Key</strong></a>&nbsp;&nbsp;|</li>

   
   
<li class="list-inline-item"><a class="text-white" href="//support.nlm.nih.gov/support/create-case/" title="Unified Medical Language System Support" id="anch_31"><strong>Customer Support</strong></a>&nbsp;&nbsp;</li>

   
   
</ul></div> <!-- 1 --> 


 </div> <!-- 2 -->
  

</div> <!-- 3 --></div></div></div>
  <#if (content.uri)?? && content.uri?starts_with("rest/")>
    <div class="container-fluid bg-secondary">
      <div class="container pl-0 pl-lg-3">
        <nav class="navbar navbar-expand-lg navbar-light">
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation"> <span class="navbar-toggler-icon"></span> </button>
          <div class="collapse navbar-collapse" id="navbarNavDropdown">
            <ul class="navbar-nav">
              <#list published_pages?sort_by('navorder') as page>
                <#if !(page.category)?? && (page.uri?starts_with("rest/"))>
                  <#if (content.rootpath)??>
                    <li class="navitem">
                      <a class="nav-link" href="${content.rootpath}${page.uri}">${page.title}</a>
                    </li>
                    <#else>
                  </#if>
                </#if>
              </#list>
              <#list categories as cat>
                <li>
                <div class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="products_services" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">${cat}</a>
                    <div class="dropdown-menu dropdown-menu-right ml-xl-5">
                      <#list published_pages?sort_by('navorder') as page>
                        <#if (page.category)?? && page.category=cat>
                          <#if (content.rootpath)??>
                            <a class="dropdown-item" href="${content.rootpath}${page.uri}">${page.title}</a>
                            <#else>
                          </#if>
                        </#if>
                      </#list>
                    </div>  
            	</div>
                </li>
              </#list>
            </ul>
          </div>
        </nav>
      </div>
    </div>
  </#if>