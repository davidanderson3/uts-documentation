<#assign categories=['Retrieving UMLS Data', 'Retrieving Source-Asserted Data' , 'REST API Cookbook' ]>
  <div class="container-fluid bg-primary">
    <div class="container">
      <div id="barbranding">
        <h3><span style="color: white;">UMLS API Technical Documentation</span></h3>
        <div class="breadcrumb-brand umls-div">
          <ul>
            <li><a href="//support.nlm.nih.gov/support/create-case/" title="Provide Feedback" id="anch_33"><strong>Provide Feedback</strong></a></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
  <#if (content.uri)?? && content.uri?starts_with("rest/")>
    <div class="container-fluid bg-secondary">
      <div class="container pl-0 pl-lg-3">
        <nav class="navbar navbar-expand-lg navbar-light">
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation"> <span class="navbar-toggler-icon"></span> </button>
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
                    <a class="nav-link dropdown-toggle" href="#" id="products_services" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">${cat}</a>
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