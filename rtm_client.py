import os
import requests

__all__ = ['RtmClient']


def load_env_variables():
    with open(".ENV") as f:
        for line in f:
            if line[0] != '#' and '=' in line:
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()
                os.environ[key] = value


# Chargez les variables d'environnement à partir du fichier .env


class RtmClient:

    def __init__(self):
        # Load environment variables from .env file
        self.token = None
        self.code_client = None
        self.user_id = None

        # Get email and password from environment variables

        load_env_variables()
        self.EMAIL_USER = os.environ.get('EMAIL_RTM')
        self.PASSWORD_USER = os.environ.get('PASSWORD_RTM')

        # API endpoints
        self.api_url = "https://api.rtm.fr"
        self.req_url = f"{self.api_url}/MaRtm/checkUser"
        self.bills_list_url = f"{self.api_url}/MaRtm/getListeVentes"

        # HTTP headers
        self.headers_list = {
            "Accept": "*/*",
            "User-Agent": "API CLIENT ",
        }

    def login(self):
        data = {
            "email": self.EMAIL_USER,
            "password": self.PASSWORD_USER
        }

        # Payload for login request
        response = requests.request("POST", self.req_url, data=data, headers=self.headers_list)

        # Get user data from response
        user_data = response.json()

        # Check if login was successful
        if user_data["status"] == "error":
            return False

        # Get user id and token from user data
        self.user_id = user_data["data"]["user"]["id"]
        self.token = user_data["data"]["token"]
        self.code_client = user_data["data"]["user"]["code_dmz"]

        return True

    def get_all_bills(self):
        bill_list_data = {
            "userId": self.user_id,
            "token": self.token,
            "codeClient": self.code_client,
            "limit": "12",  # size of bills list
            "page": "1"
        }

        # Send request to get bills of  user
        list_vente_response = requests.request("POST", url=self.bills_list_url, data=bill_list_data,
                                               headers=self.headers_list)

        # Get data from response
        list_vente_data = list_vente_response.json()

        # parse the Json response

        return list_vente_data["data"]["list"]

    def get_bill_By_Id(self, id_bill):
        bill_url = f"https://api.rtm.fr/MaRtm/printPDF/attestations?ids={id_bill}" \
                   f"&userId={self.user_id}&token={self.token}"
        return bill_url


if __name__ == "__main__":
    rtm_client = RtmClient()
    # Connect to RTM API
    if rtm_client.login():
        # Get list of bills
        bills = rtm_client.get_all_bills()
        if len(bills) > 0:
            for bill in bills:
                bill_id = bill["PK_VENTES"]
                url = rtm_client.get_bill_By_Id(bill_id)
                print("The URL for bill with ID {} is: {}".format(bill_id, url))
        else:
            print("The bill list is empty.")

else:
    print("Error: Login failed")
