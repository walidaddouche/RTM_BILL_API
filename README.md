<h2>RTM BILL API Class Documentation</h2>
<h3>Description</h3>
<p>The RtmClient class provides methods for interacting with the RTM API to retrieve user bills.</p>
<h3>Properties</h3>
<ul>
  <li><code>token</code>: str - A token used for authenticating with the API.</li>
  <li><code>code_client</code>: str - The code of the user's client.</li>
  <li><code>user_id</code>: str - The id of the user.</li>
  <li><code>EMAIL_USER</code>: str - The email of the user, taken from the .ENV file.</li>
  <li><code>PASSWORD_USER</code>: str - The password of the user, taken from the .ENV file.</li>
  <li><code>api_url</code>: str - The base URL of the RTM API.</li>
  <li><code>req_url</code>: str - The URL for the login request.</li>
  <li><code>bills_list_url</code>: str - The URL for retrieving the list of bills.</li>
  <li><code>isLog</code>: bool - A boolean indicating whether the user is currently logged in.</li>
  <li><code>headers_list</code>: dict - A dictionary of HTTP headers to use in requests.</li>
</ul>
<h3>Methods</h3>
<h4>__init__(self)</h4>
<p>This is the constructor for the RtmClient class. It initializes the properties and loads the environment variables from the .ENV file.</p>
<h4>login(self)</h4>
<p>This method logs in the user to the RTM API. It sends a login request with the user's email and password, and retrieves the user's id, token, and client code from the response. If the login is successful, it sets the <code>isLog</code> property to <code>True</code> and returns <code>True</code>. Otherwise, it returns <code>False</code>.</p>
<h4>is_connected(self)</h4>
<p>This method returns the value of the <code>isLog</code> property.</p>
<h4>get_all_bills(self)</h4>
<p>This method retrieves the list of the user's bills from the RTM API. If the user is not logged in, it raises an exception. Otherwise, it sends a request with the user's id, token, and client code to the API, and returns the list of bills in the response.</p>
<h4>get_bill_By_Id(self, id_bill)</h4>
<p>This method retrieves the URL of a specific bill with the given id. If the user is not logged in, it raises an exception. Otherwise, it returns the URL as a string.</p>
<h3>Example</h3>
<pre>
<code>
from rtm_client import *

client = RtmClient()
if client.login():
    bills = client.get_all_bills()
    for bill in bills:
        print(client.get_bill_By_Id(bill["PK_VENTES"]))

</code>
</pre>
<div>
This example creates an instance of the RtmClient class, logs in to the RTM API, and retrieves the list of the user's bills. For each bill in the list, the URL of the bill is displayed.
</div>