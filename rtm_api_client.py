import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get email and password from environment variables
EMAIL_USER = os.getenv('EMAIL_RTM')
PASSWORD_USER = os.getenv('PASSWORD_RTM')

# API endpoints
req_url = "https://api.rtm.fr/MaRtm/checkUser"
url_list_vente = "https://api.rtm.fr/MaRtm/getListeVentes"

# HTTP headers
headers_list = {
    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.com)",
    "Content-Type": "multipart/form-data; boundary=kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A"
}

# Payload for login request
payload = f"--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A\r\nContent-Disposition: form-data; " \
          f"name=\"email\"\r\n\r\n{EMAIL_USER}\r\n--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A\r\nContent-Disposition: " \
          f"form-data; name=\"password\"\r\n\r\n{PASSWORD_USER}\r\n--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A--\r\n"

# Send login request
response = requests.request("POST", req_url, data=payload, headers=headers_list)

# Get user data from response
user_data = response.json()

# Get user id and token from user data
user_id = user_data["data"]["user"]["id"]
token = user_data["data"]["token"]
code_client = user_data["data"]["user"]["code_dmz"]

# Payload for list vente request
payload = f"--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A\r\nContent-Disposition: form-data; name=\"userId\"\r\n\r\n{user_id}\r\n--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A\r\nContent-Disposition: form-data; " \
          f"name=\"token\"\r\n\r\n{token}\r\n--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A\r" \
          f"\nContent-Disposition: form-data; " \
          f"name=\"codeClient\"\r\n\r\n{code_client}\r\n--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A\r\nContent" \
          f"-Disposition: form-data; name=\"limit\"\r\n\r\n4\r\n--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A\r\nContent" \
          f"-Disposition: form-data; name=\"page\"\r\n\r\n1\r\n--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A--\r\n"

# Send list vente request
response = requests.request("POST", url_list_vente, data=payload, headers=headers_list)

# Get data from response
json_data = response.json()

# Get id of first bill from list
id_bill = json_data["data"]["list"][0]["PK_VENTES"]

# Construct URL for last bill request
last_bill_url = f"https://api.rtm.fr/MaRtm/printPDF/attestations?ids={id_bill}&userId={user_id}&token={token}"

# Send last bill request
response = requests.request("GET", last_bill_url)

