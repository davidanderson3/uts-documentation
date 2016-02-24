<#include "header.ftl">
	<#include "uts-documentation-menu.ftl">
	<h1><#escape x as x?xml>UMLS API Technical Documentation</#escape></h1>
         
        <div class = "row">
	<div class = "container-fluid col-md-12 col-sm-8 col-xs-6">

	Welcome to the UMLS API Technical Documentation.  There are 2 implementations of the UMLS API available for use:
	<ol>
	  <li><a href = "/rest/home.html">UMLS REST API</a> - a set of convenient URI patterns and Json output that offer links for important UMLS entities such as CUIs, atoms, and subsets such as the SNOMED CT-> ICD-10-CM map.
	  Code samples are available in the documentation as well as on <a href = "https://github.com/HHS/uts-rest-api" target = "_blank">github</a>.</li>
	  <li><a href = "/soap/home.html">UMLS SOAP API</a> - install all the classes for the SOAP API using Maven as described in the installation documentation. Code samples within the documentation
	  are available, mainly in Java.</li>
	</div>
	</div>

<#include "footer.ftl">