import requests

class ScientificAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.scientificdata.com"

    def get_research_papers(self, topic):
        url = f"{self.base_url}/papers"
        params = {'api_key': self.api_key, 'topic': topic}
        response = requests.get(url, params=params)
        return response.json()
