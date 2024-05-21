import requests

class GutHubClient:

    def __init__(self) -> None:
        pass

    def search_repos(self, repo_name):
        r = requests.get(url='https://api.github.com/search/repositories?q')