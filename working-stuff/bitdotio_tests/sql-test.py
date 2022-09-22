import bitdotio
#from psycopg2 import sql


dbname="Stevie011/grocery-store-prices" 
user="Stevie011" 
password="v2_3tvSA_AGU7ZGKNAVS3XDW3DfUM4Vc"

# Connect to bit.io
b = bitdotio.bitdotio("v2_3tvSA_AGU7ZGKNAVS3XDW3DfUM4Vc")

conn = b.get_connection("Stevie011/grocery-store-prices")
cur = conn.cursor()
cur.execute("UPDATE groceries SET checkers_price = 45.33 WHERE itemname = 'Brown Bread (loaf)';")
conn.commit()
#cur.execute('SELECT * FROM groceries;')
#cur.execute("INSERT INTO groceries (itemname, checkers_price, woolworths_price, pnp_price) VALUES ('Apples 1kg', 14.99, 19.99, 16.99);")
#table_name = 'groceries'

#from psycopg2 import sql

# cur.execute("INSERT INTO groceries (id, itemname, checkers_price, woolworths_price, pnp_price) VALUES (12, 'Apples 1kg', 14.99, 19.99, 16.99) RETURNING *;")
# conn.commit()


