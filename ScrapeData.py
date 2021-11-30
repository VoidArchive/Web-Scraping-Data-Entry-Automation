from bs4 import BeautifulSoup
import requests

class ScrapeData:

    def __init__(self, url, headers) -> None:
        self.url = url
        self.headers = headers
        self.response = requests.get(url = self.url, headers=self.headers)
        self.soup = BeautifulSoup(self.response.content, "html.parser")

    def scrape_url(self):
        all_url = self.soup.find_all(name="a", class_= "list-card-link")
        link_list = [link.get("href") for link in all_url]
        return list(set(link_list))