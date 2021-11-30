from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys

from time import sleep


class PostData:

    def __init__(self, form) -> None:
        s = Service('/home/voidarchive/chromedriver_linux64/chromedriver')
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=s, options=chrome_options)
        self.driver.get(form)

    def fill_form(self, address, price, url):
        sleep(1)
        # Fill address
        self.driver.find_element(
            by="xpath", value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(address)

        # Fill price
        self.driver.find_element(
            by="xpath", value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(price)

        # Fill Url
        self.driver.find_element(
            by="xpath", value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(url)

        # Click Sumbit
        self.driver.find_element(
            by="xpath", value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()

        # Refill Form
        self.driver.find_element(
            by="xpath", value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()

