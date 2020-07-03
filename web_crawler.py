from selenium import webdriver


class web_crawler(object):
    def __init__(self, query, max_price):
        self.max_price = max_price
        self.query = query
        self.url = f"https://seattle.craigslist.org/search/sss?query={query}&max_price={max_price}"
        self.driver = webdriver.Chrome(
            "/Users/PATH_TO_CHROMEDRIVER")
        self.delay = 5

    def load_page(self):
        driver = self.driver
        driver.get(self.url)
        all_data = driver.find_elements_by_class_name("result-row")
        for data in all_data:
            title = data.text.split("$")
            if title[0] == "":
                title = title[1]
            else:
                title = title[0]

            title = data.text.split("\n")
            price = title[0]
            title = title[-1]

            title = title.split(" ")
            month = title[0]
            day = title[1]
            date = month + " " + day

            title = " ".join(title[2:])
            price_idx = title.find("$")
            f_title = title[:price_idx]

            price_and_loc = title[price_idx:]
            print("Date:", date)
            print("Item:", f_title)
            print("Price and location:", price_and_loc)
            print()

    def close_web_driver(self):
        self.driver.close()
        print("\nGoodbye!")


query = "monitor"
max_price = "700"
crawler = web_crawler(query, max_price)
crawler.load_page()
crawler.close_web_driver()