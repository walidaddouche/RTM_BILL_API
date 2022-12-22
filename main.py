import requests
import os
from dotenv import load_dotenv

load_dotenv()



EMAIL_USER = os.getenv('EMAIL_RTM')
PASSWORD_USER = os.getenv('PASSWORD_RTM')

POST = "POST"

reqUrl = "https://api.rtm.fr/MaRtm/checkUser"
urlListVente = "https://api.rtm.fr/MaRtm/getListeVentes"
last_bill = "https://api.rtm.fr/MaRtm/printPDF/attestations?ids={}&userId={}&token={}"



headersList = {
    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.com)",
    "Content-Type": "multipart/form-data; boundary=kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A"
}

payload = "--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A\r\nContent-Disposition: form-data; " \
          "name=\"email\"\r\n\r\n{}\r\n--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A\r\nContent-Disposition: " \
          "form-data; name=\"password\"\r\n\r\n{}\r\n--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A--\r\n ". \
    format(EMAIL_USER, PASSWORD_USER)

response = requests.request(POST, reqUrl, data=payload, headers=headersList)

userData = response.json()

jsonData = userData.get("data")

userId = jsonData["user"]["id"]

token = jsonData["token"]
codeClient = jsonData["user"]["code_dmz"]


payload = "--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A\r\nContent-Disposition: form-data; name=\"userId\"\r\n\r\n{}\r\n--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A\r\nContent-Disposition: form-data; " \
          "name=\"token\"\r\n\r\n{}\r\n--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A\r" \
          "\nContent-Disposition: form-data; " \
          "name=\"codeClient\"\r\n\r\n{}\r\n--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A\r\nContent" \
          "-Disposition: form-data; name=\"limit\"\r\n\r\n4\r\n--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A\r\nContent" \
          "-Disposition: form-data; name=\"page\"\r\n\r\n1\r\n--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A--\r\n"\
        .format(userId,token,codeClient)

response = requests.request(POST, urlListVente, data=payload, headers=headersList)

jsonData = response.json()

id_bill = jsonData.get("data")["list"][0]["PK_VENTES"]

last_bill = last_bill.format(id_bill, userId, token)

print(last_bill)


