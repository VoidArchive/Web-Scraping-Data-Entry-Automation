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
    
    def scrape_price(self):
        all_price = self.soup.find_all(name="div", class_="list-card-price")
        price_list = [price.getText().split("/")[0] for price in all_price]
        return price_list

    def scrape_address(self):
        all_address = self.soup.find_all(name="address",class_="list-card-addr")
        address_list = [address.getText() for address in all_address]
        return address_list