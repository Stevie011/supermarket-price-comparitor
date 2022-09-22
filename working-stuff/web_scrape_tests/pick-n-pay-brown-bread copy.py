import requests #don't think we need this
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def main():
    
    print(_scrape())

def _scrape():
    #state the url
    url = "https://www.pnp.co.za/pnpstorefront/pnp/en/search/?text=brown+bread"

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
    #results = soup.find("div", class_="item js-product-card-item product-card-grid")
    results = soup.find("div", class_="col-xs-12 product-list-wrapper")

    print(results)

    #now in that, find all divs with this class name
    # name = results.find_all("div", class_="item-name")
    # price = results.find_all
   
   

    # print(products)

    #print(products)

    # ans_list = []

    # for i in products:
    #     print(i)
    #     print("\n")
    #     #find section with name element
    #     name_element = i.find("div", class_="item-name")
    #     #find price section
    #     price_element = i.find("div", class_ = "currentPrice")
    #     if name_element:
    #         #sloppy text search to filter out specific bread
    #         if "Sandwich Bread 700" in name_element.text.strip():
    #             #use .text to extract only text from html bit
    #             #use .strip to remove whitespace
    #             ans_list.append(name_element.text.strip())
    #             ans_list.append(price_element.text.strip())
    #         # print("\n")

    # return(ans_list)


if __name__ == "__main__":
    main()


