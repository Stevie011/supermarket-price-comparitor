#import requests #don't think we need this
from bs4 import BeautifulSoup
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import time
import bitdotio

def main():
    
    price = _scrape()[1]
    print(price)
    update_db(price)


def _scrape():
    #state the url
    url = "https://www.woolworths.co.za/prod/Food/Food-Basket/Recipes/Canned-Tuna/Light-Meat-Tuna-Shredded-in-Brine-170-g/_/A-6009195372286?isFromPLP=true"
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

def update_db(_price):
    print("db update start")
    dbname="Stevie011/grocery-store-prices" 
    user="Stevie011" 
    password="v2_3tvSA_AGU7ZGKNAVS3XDW3DfUM4Vc"

    # Connect to bit.io
    b = bitdotio.bitdotio("v2_3tvSA_AGU7ZGKNAVS3XDW3DfUM4Vc")

    conn = b.get_connection("Stevie011/grocery-store-prices")
    cur = conn.cursor()
    cur.execute("UPDATE groceries SET woolworths_price = (%s) WHERE id=3;", (_price,))
    conn.commit()


if __name__ == "__main__":
    main()


