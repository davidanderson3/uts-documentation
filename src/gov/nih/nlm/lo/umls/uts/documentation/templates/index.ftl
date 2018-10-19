<#include "header.ftl">
  <#include "uts-documentation-menu.ftl">
    <h1>
      <#escape x as x?xml>UMLS API Technical Documentation</#escape>
    </h1>

    

      <div class="container-fluid">
      <div class="row">
        <p>Welcome to the UMLS API Technical Documentation. There are 2 implementations of the UMLS API available for use:</p>
        </div>
        <div class="row">
        <div class="col-sm uts-rest-description">
          <h2><a href="/rest/home.html">UMLS REST API</a></h2>
          <p>A set of convenient URI patterns and Json output that offer links for important UMLS entities such as CUIs, atoms, and subsets such as the SNOMED CT-> ICD-10-CM map. Code samples are available in
          the documentation as well as on <a href="https://github.com/HHS/uts-rest-api" target="_blank">github</a>.</p>
        </div>
        <div class="col-sm uts-soap-description">
        
          <h2><a href="/soap/home.html">UMLS SOAP API</a></h2> <p>
          Install all the classes for the SOAP API using Maven as described in the installation documentation. Code samples within the documentation are available, mainly in Java.
          </p>
        </div>
      </div>
    </div>

    <#include "footer.ftl">