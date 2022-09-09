import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = "https://www.woolworths.co.za/cat?Ntt=brown%20bread&Dy=1"

driver = webdriver.Chrome("/Users/stevenstewart/supermarket-price-comparitor/web_scrape_tests/chromedriver")
driver.get(url)

time.sleep(5)

html = driver.page_source

#print(html)

soup = BeautifulSoup(html, "html.parser")

results = soup.find("div", class_="product-list__list")

print(results)

products = results.find_all("div", class_="product-list__item")

print(products)

for i in products:
    name_element = i.find("a", class_="range--title")
    price_element = i.find("strong", class_ = "price")
    if name_element:
        if "Sandwich Bread" in name_element.text.strip():
            print(name_element.text.strip())
            print(price_element.text.strip())
        # print("\n")






# page = requests.get(url)

# #print(page)

# soup = BeautifulSoup(page.content, "html.parser")

# print(soup)

# results = soup.find("div", class_="product-list__list")

# print(results)

# item_elements = results.find_all("div", class_="product-list__item")

# print(item_elements)