<#include "header.ftl">
    <#include "uts-documentation-menu.ftl">
        <div class="container-fluid uts-breadcrumbs">
            <div class="container">
                <div id="breadcrumb-div">
                    <#include "breadcrumbs.ftl">
                </div>
            </div>
        </div>
        <div class="container">
            <h1>
                <#escape x as x?xml>${content.title}</#escape>
            </h1>
            ${content.body}
        </div>
        <div class="container uts-container">
            <div id="uts-notice">
                <p>We welcome your feedback on our <a href="http://support.nlm.nih.gov/support/create-case/">customer
                        service
                        form</a>. Please use &quot;UMLS REST API feedback&quot; in your subject
                    line.</p>
                <p>Check out the <a href="/rest/rest-api-cookbook/postman.html">Postman sample
                        collection</a> to help you get started using the UMLS REST API.</p>
                <p><a href="/terms-of-service.html">API Terms of Service</a></p>
                <p><a href="/change-log.html">Change Log</a></p>
            </div>
        </div>
        <#include "footer.ftl">