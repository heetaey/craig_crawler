from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class web_crawler(object):
    def __init__(self, query, max_price):
        self.max_price = max_price
        self.query = query
        self.url = f"https://seattle.craigslist.org/search/sss?query={query}&max_price={max_price}"
        self.driver = webdriver.Chrome("/Users/heetaeyang/Documents/Project/web_crawler/chromedriver")
        self.delay = 5

        def load_page(self):
            driver = self.driver
            driver.get(self.url)



url = f"https://seattle.craigslist.org/search/sss?query=monitor&max_price=700"
query = monitor
max_price = 700
crawler = web_crawler(query, max_price)
crawler.load_page()
