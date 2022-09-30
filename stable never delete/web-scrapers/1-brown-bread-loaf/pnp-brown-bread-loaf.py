#import requests #don't think we need this
from bs4 import BeautifulSoup
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import time
import bitdotio

#pnpstorefront/pnp/en/All-Products/Bakery/Bread/Brown-Bread/Blue-Ribbon-Classic-Brown-Sliced-Bread-700g/p/000000000000249519_EA

def main():
    
    price = _scrape()[1]
    print(price)
    update_db(price)

def _scrape():
    #state the url
    url = "https://www.pnp.co.za/pnpstorefront/pnp/en/All-Products/Bakery/Bread/Brown-Bread/Albany-Superior-Sliced-Brown-Bread-700g/p/000000000000251231_EA"
    #url = "https://www.pnp.co.za/pnpstorefront/pnp/en/All-Products/Food-Cupboard/Canned-Foods-%26-Packets/Canned-Fish/Tuna/No-Name-Shredded-Tuna-In-Salt-Water-170g/p/000000000000206934_EA"


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
    results = soup.find("div", class_="col-xs-12 fed-pdp-col-sm-r fed-pdp-col-md-r fed-pdp-product-details")

    #print(results)

    name = (results.find("h1")).text.strip()

    price = (results.find("div", class_= "normalPrice")).text.strip()

    price = price[1:]
    price = float(price[:2]+"."+price[2:])

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
    cur.execute("UPDATE groceries SET pnp_price = (%s) WHERE itemname = 'Brown Bread (loaf)';", (_price,))
    conn.commit()   


if __name__ == "__main__":
    main()


