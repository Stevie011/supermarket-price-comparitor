from flask import Flask
from flask_restful import Resource, Api

import bitdotio

dbname="Stevie011/grocery-store-prices" 
user="Stevie011" 
password="v2_3tvSA_AGU7ZGKNAVS3XDW3DfUM4Vc"

# Connect to bit.io
b = bitdotio.bitdotio("v2_3tvSA_AGU7ZGKNAVS3XDW3DfUM4Vc")

app = Flask(__name__)
api = Api(app)

class Count(Resource):
    def get(self):
        conn = b.get_connection("Stevie011/grocery-store-prices")
        cur = conn.cursor()
        #cur.execute('SELECT itemname, checkers, woolworths FROM "price-table.xlsx - Sheet1";')
        cur.execute('SELECT itemname FROM "groceries.xlsx - Sheet1";')
        return cur.fetchmany()

api.add_resource(Count, '/count')

if __name__ == '__main__':
    app.run(debug=True)