from ScrapeData import ScrapeData
from post_data import PostData

GOOGLE_FORM = "https://forms.gle/CMhKCbymUFnqnBts6"


# --------------------- Scrape Data-----------------#
zillow_url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

headers = {
    "User-Agent": "Defined",
    "Accept-Language": "en-US,en;q=0.9",
}

rent_data = ScrapeData(url=zillow_url, headers=headers)

all_urls = rent_data.scrape_url()
all_prices = rent_data.scrape_price()
all_address = rent_data.scrape_address()

# print(len(all_urls))
# print(len(all_prices))

# print(all_prices)
# print(all_address)

# ------------------ Fill Google Form-------#

form = PostData(GOOGLE_FORM)
for index in range(len(all_urls)-1):
    form.fill_form(address=all_address[index],price=all_prices[index],url=all_urls[index])