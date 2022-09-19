import bitdotio

def update_db(_price):
    dbname="Stevie011/grocery-store-prices" 
    user="Stevie011" 
    password="v2_3tvSA_AGU7ZGKNAVS3XDW3DfUM4Vc"

    # Connect to bit.io
    b = bitdotio.bitdotio("v2_3tvSA_AGU7ZGKNAVS3XDW3DfUM4Vc")

    conn = b.get_connection("Stevie011/grocery-store-prices")
    cur = conn.cursor()
    cur.execute("UPDATE groceries SET checkers_price = (%s) WHERE itemname = 'Brown Bread (loaf)';", (_price,))
    conn.commit()

update_db(16.99)