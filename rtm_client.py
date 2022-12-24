import os
import requests

from dotenv import load_dotenv

__all__ = ['RtmClient']


class RtmClient:
    """
    A client for interacting with the RTM API.
    """

    def __init__(self):
        """
        Initialize the client with environment variables from the .env file.
        """
        # Load environment variables from .env file
        self.token = None
        self.code_client = None
        self.user_id = None

        # Chargez les variables d'environnement à partir du fichier .env
        load_dotenv(".ENV")

        # Get email and password from environment variables
        self.EMAIL_USER = os.environ.get('EMAIL_RTM')
        self.PASSWORD_USER = os.environ.get('PASSWORD_RTM')

        # API endpoints
        self.api_url = "https://api.rtm.fr"
        self.req_url = f"{self.api_url}/MaRtm/checkUser"
        self.bills_list_url = f"{self.api_url}/MaRtm/getListeVentes"

        self.isLog = False

        # HTTP headers
        self.headers_list = {
            "Accept": "*/*",
            "User-Agent": "API CLIENT ",
        }

    def login(self) -> bool:
        """
        Login to the RTM API using the email and password stored in the environment variables.
        Returns:
            bool: True if login was successful, False otherwise.
        """
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

        self.isLog = True

        return True

    def is_connected(self) -> bool:
        """
        Check if the client is currently logged in to the RTM API.
        Returns:
            bool: True if the client is logged in, False otherwise.
        """
        return self.isLog

    def get_all_bills(self) -> list:
        """
        Get a list of all bills for the logged-in user.

        Returns:
            A list of dictionaries, where each dictionary contains information about a single bill.

        Raises:
            Exception: If the user is not logged in.
        """
        if not self.is_connected():
            raise Exception("Error: not connected")
        else:
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

    def get_bill_By_Id(self, id_bill: int) -> str:
        """
        Get the URL of a bill by its ID.

        Parameters:
            id_bill (int): The ID of the bill.

        Returns:
            str: The URL of the bill.

        Raises:
            Exception: If the user is not connected to the RTM API.
        """
        if not self.is_connected():
            raise Exception("Error: not connected")
        else:
            bill_url = f"{self.api_url}/MaRtm/printPDF/attestations?ids={id_bill}" \
                       f"&userId={self.user_id}&token={self.token}"
            return bill_url
