import requests

class FinancialAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.financialdata.com"

    def get_stock_data(self, ticker):
        url = f"{self.base_url}/stock/{ticker}"
        params = {'api_key': self.api_key}
        response = requests.get(url, params=params)
        return response.json()

    def get_forex_data(self, base_currency):
        url = f"{self.base_url}/forex/{base_currency}"
        params = {'api_key': self.api_key}
        response = requests.get(url, params=params)
        return response.json()
