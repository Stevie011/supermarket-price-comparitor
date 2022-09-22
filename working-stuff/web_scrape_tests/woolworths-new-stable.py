import requests #don't think we need this
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def main():
    
    print(_scrape())

def _scrape():
    #state the url
    url = "https://www.woolworths.co.za/prod/Food/Bread-Bakery-Desserts/Bread-Rolls-Wraps-Bagels/Bread/Brown-Bread/Brown-Sandwich-Bread-700-g/_/A-20067113?isFromPLP=true"
    #url = "https://www.woolworths.co.za/prod/Food/Food-Basket/Recipes/Canned-Tuna/Light-Meat-Tuna-Shredded-in-Brine-170-g/_/A-6009195372286?isFromPLP=true"

    #we use chrome web driver to render the page, specifying location of .chromedriver
    driver = webdriver.Chrome("/Users/stevenstewart/supermarket-price-comparitor/web_scrape_tests/chromedriver")
    #use this to run url instead of request
    driver.get(url)

    #wait for it to load
    time.sleep(5)

    #now get the html from here
    html = driver.page_source

    #print(html)

    #parse it with bs
    soup = BeautifulSoup(html, "html.parser")

    #look for div with that class name
    results = soup.find("div", class_="product-skus")

    name =(results.find("div", class_="prod-name")).text.strip()
    price = (results.find("span", class_="price prod--price")).text.strip()
    price = float(price[2:])

    return [name, price]


if __name__ == "__main__":
    main()


