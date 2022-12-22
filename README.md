<!DOCTYPE html>
<html>
  <head>
    <title>RTM API Client</title>
  </head>
  <body>
    <h1>RTM API Client</h1>
    <p>
      This is a Python script that demonstrates how to use the RTM API to authenticate a user and retrieve a list of their bills. The RTM API is a REST API that allows you to access information about a user's account and perform actions on their behalf.
    </p>
    <h2>Prerequisites</h2>
    <p>
      Before running the script, make sure you have the following:
    </p>
    <ul>
      <li>
        Python 3.6 or higher installed on your system. You can check the version of Python you have installed by running <code>python --version</code> in a terminal.
      </li>
      <li>
        The <code>requests</code> and <code>dotenv</code> modules installed. These modules are used to send HTTP requests and load environment variables, respectively. You can install them by running the following command:
        <pre>pip install requests dotenv</pre>
      </li>
      <li>
        An RTM account with a valid email and password. You can sign up for an RTM account at <a href="https://www.rtm.fr/">https://www.rtm.fr/</a>.
      </li>
      <li>
        A <        <li><code>EMAIL_RTM</code>: the email address of the user's RTM account</li>
        <li><code>PASSWORD_RTM</code>: the password of the user's RTM account</li>
      </ul>
      The <code>.env</code> file should be placed in the same directory as the script.
    </li>
  </ul>
  <h2>Usage</h2>
  <p>
    To use the script, follow these steps:
  </p>
  <ol>
    <li>
      Replace the placeholders in the <code>.env</code> file with the email and password of the user's RTM account.
    </li>
    <li>
      Open a terminal, navigate to the directory where the script and <code>.env</code> file are located, and run the script using the following command:
      <pre>python3 rtm_api_client.py</pre>
    </li>
    <li>
      The script will output the URL of the user's last bill. You can use this URL to download the bill as a PDF file.
    </li>
  </ol>
  <h2>Notes</h2>
  <ul>
    <li>
      The script uses the following API endpoints:
      <ul>
        <li>
          <code>https://api.rtm.fr/MaRtm/checkUser</code>: This endpoint is used to authenticate the user. It accepts a POST request with a payload containing the user's email and password, and returns a JSON object containing the user's data and a token that can be used to access the other endpoints.
        </li>
        <li>
          <code>https://api.rtm.fr/MaRtm/getListeVentes</code>
          <code>https://api.rtm.fr/MaRtm/printPDF/attestations</code>: This endpoint is used to retrieve the PDF of a specific bill. It accepts a GET request with query parameters containing the id of the bill, the user's id, and the token, and returns the PDF file.
        </li>
      </ul>
    </li>
    <li>
      The script sends requests with a specific set of HTTP headers and payloads. Make sure to use the correct headers and payloads when interacting with the RTM API.
    </li>
    <li>
      The script retrieves the URL of the user's last bill by getting the first bill in the list of bills returned by the API. You may want to modify the script to retrieve a different bill, for example by sorting the list of bills by date or by selecting a bill based on its id.
    </li>
    <li>
      The RTM API may have rate limits and/or require an API key. Make sure to respect these limits and use the appropriate API key when making requests to the API.
    </li>
  </ul>
</body>
</html>

