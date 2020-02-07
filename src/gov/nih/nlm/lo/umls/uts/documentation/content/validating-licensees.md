title=Validating UMLS Licensees for Third-Party Application Developers
date=2020-02-07
updated=2020-02-07
type=page
status=published
navorder=1
~~~~~~

<p><strong>Purpose</strong></p>
Authorized content distributors can use the RESTful API to validate UMLS licensees for their applications.

<p><strong>What is an Authorized Content Distributor? </strong></p>
An authorized content distributor is a licensee who has developed applications that require their end-users to have agreed to the UMLS Metathesaurus License Agreement, <br/>and have received NLM approval to use the validation service.  

<p><strong>How to Become an Authorized Content Distributor</strong></p>
Contact the <a href="https://support.nlm.nih.gov/support/create-case/">NLM Help Desk</a> with the subject line &ldquo;UTS Content Distributor Request.&rdquo; Your request should include a summary of your application and its intended use. <br/> NLM will approve requests on a case-by-case basis.  

<p><strong>Authentication</strong></p>
UTS authentication is exposed to third party users via the following URL:<br/>
<b>https://uts-ws.nlm.nih.gov/restful/isValidUMLSUser</b>

<p> POST HTTP calls are currently supported. </p>

<p>The API expects three parameters: </p>
<table border="1" cellpadding = "5" cellspacing = "2">
<tr>
<th>Parameter</th>
<th>Description</th>
</tr>
<tr>
<td>licenseCode	</td>
<td>Valid UMLS license code of the authorized content distributor </td>
</tr>
<tr>
<td>user</td>	       
<td> Valid UTS username of end-user*</td>
</tr>
<tr>
<td>password</td>	    
<td>Valid UTS password of end-user</td>
</tr>
</table>

<p><i>Response for an valid authentication call</i>
<br/>If a valid username and password are sent, the API will return:
    <br/> &lt?xml version='1.0' encoding='UTF-8'?&gt< Result > true < /Result > </p>

<p><i>Response for an incorrect or invalid authentication call</i>
<br/>If an incorrect username and/or password are sent, the API will respond with a 400 Bad Request error. <br/> If a username is associated with an invalid account (license has expired), the API will return:
    <br/>  &lt?xml version='1.0' encoding='UTF-8'?&gt< Result > false < /Result > </p>

<p>*<b>Note to implementers:</b> The REST API converts the &quot;user&quot; parameter to lower-case before authentication is performed (e.g. &quot;USERNAME&quot; or &quot;UserName&quot; are converted to &quot;username&quot;).</p>
    
<p><strong>Best Practices for Implementation</strong></p>
<p>There are two common options for implementing the license validation service.</p>
<p><i>Scenario:</i> An authorized content distributor has one or more applications, possibly installed in many separate physical locations, which use UMLS data.   The distributor must verify that the end-users of the application(s) have valid UMLS license accounts.</p>
<p><i>Implementation Option 1:</i> The authorized content distributor hard-codes their license code into the application and the application makes the call to the RESTful API validation service. </p>
<ul>
	<li><i>Pro:</i>  The application makes the call directly to the RESTful API validation service. </li>
	<li><i>Con:</i>  If and when the authorized content distributor's license code is no longer valid AND the distributor receives a NEW license code, the authorized content distributor must update the application with the new code.  If the authorized content distributor has multiple applications, the distributor must update each application to include the new license code.</li>
</ul>
<img src="/images/validateumlsuser1.jpg" alt="Diagram of Implementation Option 1">
<p><i>Implementation Option 2:</i> The authorized content distributor deposits the license code with a middle-service.   The middle-service collects an end-user's username and password, appends the license code, and makes the call to the RESTful API validation service.</p>
<ul>
	<li><i>Pro:</i> If and when the license code is no longer valid AND the authorized content distributor receives a NEW license code, the authorized content distributor sends the new license to the middle-service for inclusion in authentication calls.  If the authorized content distributor has multiple applications that use the middle-man service, the distributor needs to replace the license code only once.</li>
    <li><i>Con:</i>  Con: The authorized content distributor must find a middle-service and implement it.  This may not be necessary for a single application.</li>
</ul>
<img src="/images/validateumlsuser2.jpg" alt="Diagram of Implementation Option 2">
<br><br>
<p><strong>Sample code in <a href="#Java">Java</a>, <a href="#Perl">Perl</a>, and <a href="#C#">C#</a></strong> </p>

<a name="Java"></a>

<h2>Java</h2>

```java

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.URL;
import java.net.URLConnection;
import java.net.URLEncoder;


public class IsValidUMLSUser {
public static void main(String[] argv) throws Exception {
if (argv.length == 1 && argv[0].equals("help")) {
System.out.println("Usage: java isValidUMLSUser <LicenseCode> <UserName> <Password>");
return ;

}

if (argv.length != 3) {
System.out.println("Incorrect Arguments!!");
System.out.println("Usage: java isValidUMLSUser <LicenseCode> <UserName> <Password>");
return ;
}

String data = URLEncoder.encode("licenseCode", "UTF-8") + "=" + URLEncoder.encode(argv[0], "UTF-8");
data += "&" + URLEncoder.encode("user", "UTF-8") + "=" + URLEncoder.encode(argv[1], "UTF-8");
data += "&" + URLEncoder.encode("password", "UTF-8") + "=" + URLEncoder.encode(argv[2], "UTF-8");


URL url = new URL("https://uts-ws.nlm.nih.gov/restful/isValidUMLSUser");
URLConnection conn = url.openConnection();
conn.setDoOutput(true);
OutputStreamWriter wr = new OutputStreamWriter(conn.getOutputStream());
wr.write(data);
wr.flush();

BufferedReader rd = new BufferedReader(new InputStreamReader(conn.getInputStream()));
String line;
while ((line = rd.readLine()) != null) {
System.out.println(line);
}
wr.close();
rd.close();
}
}

```

<a name="Perl"></a>

<h2>Perl</h2>

```perl
use HTTP::Request::Common qw(POST);
use LWP::UserAgent;
$ua = LWP::UserAgent->new;

my $req = POST 'https://uts-ws.nlm.nih.gov/restful/isValidUMLSUser',
[ licenseCode => '1', user =>'your user name',password=>'your password'];


print $ua->request($req)->as_string;
```

<a name="C#"></a>

<h2>C#</h2>

```c#
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;
using System.Net;
using System.Web;

namespace IsValidUMLSUser
{
class Program
{
static void Main(string[] args)
{
try
{
//Set the endpoint address
Uri address = new Uri("https://uts-ws.nlm.nih.gov/restful/IsValidUMLSUser");


// Create the web request
HttpWebRequest request = WebRequest.Create(address) as HttpWebRequest;

// Set request type to POST
request.Method = "POST";
request.ContentType = "application/x-www-form-urlencoded";

// Create the data to send
string licenseCode = "1";
string user = "your user name";
string password = "your password";

//build UrlEncoded parameters
StringBuilder data = new StringBuilder();
data.Append("licenseCode=" + HttpUtility.UrlEncode(licenseCode));
data.Append("&user=" + HttpUtility.UrlEncode(user));
data.Append("&password=" + HttpUtility.UrlEncode(password));

// Create a byte array of the data we want to send
byte[] byteData = UTF8Encoding.UTF8.GetBytes(data.ToString());

// Set the content length in the request headers
request.ContentLength = byteData.Length;

// Write data
using (Stream postStream = request.GetRequestStream())
{
postStream.Write(byteData, 0, byteData.Length);
}

// Get response
using (HttpWebResponse response = request.GetResponse() as HttpWebResponse)
{
// Get the response stream
StreamReader reader = new StreamReader(response.GetResponseStream());
// Console application output
Console.WriteLine(reader.ReadToEnd());


}
}
catch (WebException wex)
{
if (wex.Response != null)
{
using (HttpWebResponse errorResponse = (HttpWebResponse)wex.Response)
{
Console.WriteLine(
"The server returned '{0}' with the status code {1} ({2:d}).",
errorResponse.StatusDescription, errorResponse.StatusCode,
errorResponse.StatusCode);
}
}
}
}
}
}
```


