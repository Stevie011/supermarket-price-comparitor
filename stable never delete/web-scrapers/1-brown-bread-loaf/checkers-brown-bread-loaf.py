import requests #don't think we need this
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
    url = "https://www.checkers.co.za/All-Departments/Food/Bakery/Bread-and-Rolls/Brown-and-Wholemeal-Bread/Albany-Superior-Sliced-Brown-Bread-700g/p/10136298EA"
    #url = "https://www.checkers.co.za/All-Departments/Food/Food-Cupboard/Canned-Food/Canned-Fish-and-Seafood/Checkers-Housebrand-Light-Meat-Shredded-Tuna-In-Water-170g/p/10165121EA"

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

def update_db(_price):
    print("db update start")
    dbname="Stevie011/grocery-store-prices" 
    user="Stevie011" 
    password="v2_3tvSA_AGU7ZGKNAVS3XDW3DfUM4Vc"

    # Connect to bit.io
    b = bitdotio.bitdotio("v2_3tvSA_AGU7ZGKNAVS3XDW3DfUM4Vc")

    conn = b.get_connection("Stevie011/grocery-store-prices")
    cur = conn.cursor()
    cur.execute("UPDATE groceries SET checkers_price = (%s) WHERE itemname = 'Brown Bread (loaf)';", (_price,))
    conn.commit()



if __name__ == "__main__":
    main()


