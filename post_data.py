from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class PostData:

    def __init__(self, form) -> None:
        s = Service('/home/voidarchive/chromedriver_linux64/chromedriver')
        self.driver = webdriver.Chrome(service=s)
        self.driver.get(url=form)
