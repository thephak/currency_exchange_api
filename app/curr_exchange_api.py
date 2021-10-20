import requests
import os

API_TOKEN = os.getenv("API_TOKEN")
API_HOST = os.getenv("API_HOST")
API_URL = os.getenv("API_URL")
LIST_CURRENCY_RAW = os.getenv("LIST_CURRENCY")

LIST_CURRENCY = LIST_CURRENCY_RAW.split(',')

class CurrencyExchangeAPI:
    def __init__(
        self
    ):  
        self.headers = {
            "X-Rapidapi-Key": API_TOKEN,
            "X-Rapidapi-Host": API_HOST
        }

    def get_exchange (
        self,
        source: str,
        destination: str
    ):  
        """
        Get Currency Exchange by specifying the quotes of source and destination.

        :param source: Source currency. 
        :param destination: Destination currency.
        :return: Response from Currency Exchange API. If success it will return float number for the currency exchange rate.
        """

        if not validate_currency(source):
            r = requests.Response()
            r.status_code = 403 
            r._content = bytes("Invalid currency: " + source, encoding='utf8')
            return r

        if not validate_currency(destination):
            r = requests.Response()
            r.status_code = 403 
            r._content = bytes("Invalid currency: " + destination, encoding='utf8')
            return r
        
        url = API_URL + "?from=" + source + "&to=" + destination
        print("Sending request to Currency Exchange API: " + url)
        response = requests.get(url, headers=self.headers)

        return response

def validate_currency (
    currency: str 
):
    """
    Validate text if it is a currency on the currecy list allowed to use this API.

    :param currency: A text to be checked as valid currency. 
    :return: True if a text is a currency on the list, otherwise return False.
    """

    if currency not in LIST_CURRENCY:
        return False
    return True