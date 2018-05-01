<a id="demo"></a> 
<div class="container-fluid authdemo">
  <div class="row">
   <div class="col-sm-12">
    <h3>Authentication Demo
    <h4>Request a Ticket Granting Ticket (TGT)</h4>
    <p>Enter your API key. You can get your API key by visiting your profile at <a href="https://uts.nlm.nih.gov/">https://uts.nlm.nih.gov/</a>.</p>
    <form id="tgtForm" method="POST">

      <label for="apikey">API Key: </label>
      <input type="text" id="apikey" name="apikey" placeholder="API Key">

      <input class="formButton" type="submit" id="getTGTBtn" value="Get Ticket-Granting Ticket">
      <input class="formButton" type="reset" id="clearTgt" value="Clear">
    </form>
    </div>
  </div>
  <div class="row">
    <div class="col-sm-6">
      <p>
        <strong>Request:</strong>
      </p>
            <table>
      <tr>
      <td>
      Method
      </td>
      <td>POST</td>
      </tr>
      <tr>
      <td>URL</td>
      <td>https://uts-login.nlm.nih.gov/cas/v1/tickets</td>
      </tr>
      <tr>
      <td>Headers</td>
      <td>Content-Type=application/x-www-form-urlencoded</td>
      </tr>
      <tr>
      <td>Parameters</td>
      <td>username={yourusername}&password={yourpassword}</td>
      </tr>
      </table>
    </div>
    <div class="col-sm-6">
      <p>
        <strong>Response:</strong>
      </p>
      <pre id="tgtRes">           
            </pre>
    </div>
  </div>
  <div class="row">
    <div class="col-sm-12">
    <p><strong>Extracted URL with TGT for obtaining Service Tickets:</strong></p>
    <pre id="tgtVal">            
            </pre>
    <p>Your Ticket-Granting Ticket will be valid for 8 hours.</p>
    </div>
  </div>
  <img src="../images/downarrow.png" class="arrow" alt="down arrow">
  <div class="row">
   <div class="col-sm-12">
<h4>Request a Service Ticket (ST)</h4>
<p>You must request a Ticket-Granting Ticket above before requesting a service ticket.</p>
  <form id="stForm" method="POST">
    <label>Service:</label>
    <input type="text" name="service" id="service" class="apiInput" value="http://umlsks.nlm.nih.gov" />
    <input class="formButton" type="submit" id="getSTBtn" value="Get Service Ticket">
  </form>
  </div>
  </div>
  <div class="row">
    <div class="col-sm-6">
      <p>
        <strong>Request:</strong>
      </p>
      <table>
      <tr>
      <td>
      Method
      </td>
      <td>POST</td>
      </tr>
      <tr>
      <td>URL</td>
      <td><label id="stUrlLabel">https://uts-login.nlm.nih.gov/cas/v1/tickets</label></td>
      </tr>
      <tr>
      <td>Headers</td>
      <td>Content-Type=application/x-www-form-urlencoded</td>
      </tr>
      <tr>
      <td>Parameters</td>
      <td>service=http://umlsks.nlm.nih.gov</td>
      </tr>
      </table>
    </div>
    <div class="col-sm-6">
      <p>
        <strong>Response:</strong>
      </p>
  <pre id="stVal">            
            </pre>
    </div>
  </div>
     <img src="../images/downarrow.png" class="arrow" alt="down arrow">
  <div class="row">
  <div class="col-sm-12"> 
  <h4>Request Data</h4>
  <p>To request data, append your Service Ticket to your request URL. For example: https://uts-ws.nlm.nih.gov/rest/current?string=diabetes&ticket={yourServiceTicket}. Each new request requires a new Service Ticket.
  <!--
    <img src="../images/downarrow.png" class="arrow" alt="down arrow">
  <div class="row">
  <div class="col-sm-12">
<h4>Request Data</h4>

<p> Append your Service Ticket to your request. For example: https://uts-ws.nlm.nih.gov/rest/current?string={yourSearchTerm}&ticket={yourServiceTicket}</p>
  <form id="apiForm" method="POST">
    <label>Search:</label>
    <input id="searchStr" placeholder="Enter Search Term" type="text">
    <input class="formButton" type="submit" id="searchBtn" value="Search">
  </form>

  <strong>Search Results</strong>
  <pre>
        <div id="results"></div>       
        </pre>
  </div>
  </div>
  -->
</div>