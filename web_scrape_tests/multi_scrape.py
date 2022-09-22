from bs4 import BeautifulSoup
from selenium import webdriver
import time
import bitdotio

checkers_url = "https://www.checkers.co.za/All-Departments/Food/Bakery/Bread-and-Rolls/Brown-and-Wholemeal-Bread/Albany-Superior-Sliced-Brown-Bread-700g/p/10136298EA"
pnp_url = "https://www.pnp.co.za/pnpstorefront/pnp/en/All-Products/Bakery/Bread/Brown-Bread/Albany-Superior-Sliced-Brown-Bread-700g/p/000000000000251231_EA"
woolworths_url = "https://www.woolworths.co.za/prod/Food/Bread-Bakery-Desserts/Bread-Rolls-Wraps-Bagels/Bread/Brown-Bread/Brown-Sandwich-Bread-700-g/_/A-20067113?isFromPLP=true"
item_id = 1


def main_brown_bread():
    
    checkers_price = checkers_scrape()[1]
    pnp_price = pnp_scrape()[1]
    woolworths_price = woolworths_scrape()[1]

    update_db(checkers_price, pnp_price, woolworths_price, item_id)

def checkers_scrape():
    try:
        url = checkers_url
        driver = webdriver.Chrome("/Users/stevenstewart/supermarket-price-comparitor/web_scrape_tests/chromedriver")
        driver.get(url)
        time.sleep(5)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        results = soup.find("div", class_="pdp__details")
        name = (results.find("h1")).text.strip()
        price = (results.find("span", class_="now")).text.strip()
        price=float(price[1:])
        return [name, price]
    except:
        print("Checkers error at url :", checkers_url)



def pnp_scrape():
    try:
        url = pnp_url
        driver = webdriver.Chrome("/Users/stevenstewart/supermarket-price-comparitor/web_scrape_tests/chromedriver")
        driver.get(url)
        time.sleep(5)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        results = soup.find("div", class_="col-xs-12 fed-pdp-col-sm-r fed-pdp-col-md-r fed-pdp-product-details")
        name = (results.find("h1")).text.strip()
        price = (results.find("div", class_= "normalPrice")).text.strip()
        price = price[1:]
        price = float(price[:2]+"."+price[2:])
        return [name, price]
    except:
        print("Pnp error at url :", pnp_url)

def woolworths_scrape():
    try:
        url = woolworths_url
        driver = webdriver.Chrome("/Users/stevenstewart/supermarket-price-comparitor/web_scrape_tests/chromedriver")
        driver.get(url)
        time.sleep(5)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        results = soup.find("div", class_="product-skus")
        name =(results.find("div", class_="prod-name")).text.strip()
        price = (results.find("span", class_="price prod--price")).text.strip()
        price = float(price[2:])
        return [name, price]
    except:
        print("Woolworths error at url :", woolworths_url)

def update_db(ch, pnp, ww, _id):
    try:
        print("db update start")
        dbname="Stevie011/grocery-store-prices" 
        user="Stevie011" 
        password="v2_3tvSA_AGU7ZGKNAVS3XDW3DfUM4Vc"

        b = bitdotio.bitdotio("v2_3tvSA_AGU7ZGKNAVS3XDW3DfUM4Vc")

        conn = b.get_connection("Stevie011/grocery-store-prices")
        cur = conn.cursor()
        cur.execute("UPDATE groceries SET checkers_price = (%s) WHERE id=(%s);", (ch, _id,))
        cur.execute("UPDATE groceries SET pnp_price = (%s) WHERE id=(%s);", (pnp, _id,))
        cur.execute("UPDATE groceries SET woolworths_price = (%s) WHERE id=(%s);", (ww, _id,))
        #how to insert item id too?
        conn.commit()
    except:
        print("DB update error")



if __name__ == "__main__":
    main_brown_bread()