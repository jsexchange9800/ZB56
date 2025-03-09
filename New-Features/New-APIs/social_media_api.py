import requests

class SocialMediaAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.socialmedia.com"

    def get_user_data(self, username):
        url = f"{self.base_url}/user/{username}"
        params = {'api_key': self.api_key}
        response = requests.get(url, params=params)
        return response.json()
