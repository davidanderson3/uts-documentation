<!DOCTYPE html>  
<html lang="en">
  <head>
    <meta charset="utf-8"/>
    <title><#if (content.title)??><#escape x as x?xml>${content.title}</#escape><#else>JBake</#if></title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">
    <meta name="keywords" content="">
    <meta name="generator" content="JBake">
    <meta http-equiv="X-UA-Compatible" content="IE=9" />

    <!-- Le styles -->
    <link href="<#if (content.rootpath)??>${content.rootpath}<#else></#if>css/bootstrap.min.css" rel="stylesheet">
    <link href="<#if (content.rootpath)??>${content.rootpath}<#else></#if>css/asciidoctor.css" rel="stylesheet">
    <link href="<#if (content.rootpath)??>${content.rootpath}<#else></#if>css/prettify.css" rel="stylesheet">
    <link href="<#if (content.rootpath)??>${content.rootpath}<#else></#if>css/uts-docs.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/8.6/styles/default.min.css">

    <script src="//code.jquery.com/jquery-1.11.3.min.js"></script>
    <script src="//code.jquery.com/jquery-migrate-1.2.1.min.js"></script>
    <script src="<#if (content.rootpath)??>${content.rootpath}<#else></#if>js/bootstrap.min.js"></script>
    <script src="<#if (content.rootpath)??>${content.rootpath}<#else></#if>js/prettify.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/8.6/highlight.min.js"></script>
    
    <!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
      <script src="<#if (content.rootpath)??>${content.rootpath}<#else></#if>js/html5shiv.min.js"></script>
    <![endif]-->
    <link rel="shortcut icon" href="<#if (content.rootpath)??>${content.rootpath}<#else></#if>favicon.ico">
    
    <script type = "text/javascript">
      $(document).ready(function() {
        
       $("th").attr("scope","col");
      
      });
    </script>
  </head>
  <body onload="prettyPrint();hljs.initHighlighting();">
     <div class="container-fluid">
      <!--header to hold banner + top navigation area -->
      <!-- responsive design header using bootstrap css framework -->
   