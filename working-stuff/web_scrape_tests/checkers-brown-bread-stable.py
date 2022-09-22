import requests #don't think we need this
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def main():
    
    print(_scrape())

def _scrape():
    #state the url
    #url = "https://www.checkers.co.za/All-Departments/Food/Bakery/Bread-and-Rolls/Brown-and-Wholemeal-Bread/Albany-Superior-Sliced-Brown-Bread-700g/p/10136298EA"
    url = "https://www.checkers.co.za/All-Departments/Food/Food-Cupboard/Canned-Food/Canned-Fish-and-Seafood/Checkers-Housebrand-Light-Meat-Shredded-Tuna-In-Water-170g/p/10165121EA"

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
    results = soup.find("div", class_="pdp__details")

    name = (results.find("h1")).text.strip()
    price = (results.find("span", class_="now")).text.strip()

    price=float(price[1:])

    return [name, price]


if __name__ == "__main__":
    main()


