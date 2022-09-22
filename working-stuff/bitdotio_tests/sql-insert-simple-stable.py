import bitdotio



dbname="Stevie011/grocery-store-prices" 
user="Stevie011" 
password="v2_3tvSA_AGU7ZGKNAVS3XDW3DfUM4Vc"

# Connect to bit.io
b = bitdotio.bitdotio("v2_3tvSA_AGU7ZGKNAVS3XDW3DfUM4Vc")

conn = b.get_connection("Stevie011/grocery-store-prices")
cur = conn.cursor()


cur.execute("INSERT INTO groceries (id, itemname, checkers_price, woolworths_price, pnp_price) VALUES (12, 'Apples 1kg', 14.99, 19.99, 16.99) RETURNING *;")
conn.commit()

#better format but don't know how to include returning
#
#from psycopg2 import sql

# cur.execute(
#     sql.SQL("INSERT INTO {} VALUES (%s, %s, %s, %s, %s)")
#         .format(sql.Identifier('groceries')),
#     [12, 'Apples 1kg', 14.99, 19.99, 16.99])

# conn.commit()