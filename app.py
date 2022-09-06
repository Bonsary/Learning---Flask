from flask import Flask, jsonify, request
from products import products

app = Flask(__name__)


@app.route("/ping", methods=['GET']) #optional 'cause I'm using GET
def ping():
    return jsonify({"message": "pong!"})

@app.route('/products')
def getProducts():
    return jsonify(products)

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if len(productFound) > 0:
        return jsonify(productFound)
    return jsonify({"message": "product {} not found...".format(product_name)})

@app.route('/products', methods=['POST'])
def addProduct():
    new_product = request.json
    products.append(new_product)
    print(products)
    return "received"

@app.route('/product/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    filteredProducts =  list(filter(lambda product: product['name'] != product_name, products))
    print(filteredProducts)
    return jsonify(filteredProducts)

if __name__ == '__main__':
    app.run(debug=True, port=4000) 