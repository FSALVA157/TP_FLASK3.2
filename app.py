from flask import Flask, jsonify, request

from models.ProductModel import ProductModel
from models.CustomerModel import CustomerModel

app = Flask(__name__)


@app.route('/')
def info():
    return jsonify({"message": "Trabajo Practico 3.2 ", "Base de datos": "Sales"})


@app.route('/customers/<int:customerid>', methods=['GET'])
def custom_by_id(customerid):
    try:
        customer = CustomerModel.get_customer(customerid)
        return customer
    except Exception as e:
        raise e


@app.route('/customers', methods=['GET'])
def get_customers():
    arg = request.args
    state = arg.get('state')

    try:
        if state is not None:
            customers = CustomerModel.customers_state(state)
            return customers
        else:
            customers = CustomerModel.get_customers()
            return customers
    except Exception as e:
        raise e


@app.route('/customers/add', methods=['POST'])
def add_customer():
    ars = request.args
    firstname = ars.get('firstname')
    lastname = ars.get('lastname')
    phone = ars.get('phone')
    email = ars.get('email')
    street = ars.get('street')
    city = ars.get('city')
    state = ars.get('state')
    zipcode = ars.get('zipcode')
    try:
        customer = CustomerModel.create_customer(firstname, lastname, phone, email, street, city, state, zipcode)
        return customer
    except Exception as e:
        raise e


@app.route('/customers/update/<int:customerid>', methods=['PUT'])
def update_customer(customerid):
    email = request.json['email']
    street = request.json['street']
    phone = request.json['phone']
    state = request.json['state']
    city = request.json['city']
    zip_code = request.json['zipcode']

    if email is None or street is None or phone is None or state is None or city is None or zip_code is None:
        response_data = {
            "Message": "Missing data"
        }
        return response_data, 400

    try:
        customer = CustomerModel.update_customer(email, phone, street, state, city, zip_code, customerid)
        return customer
    except Exception as e:
        raise e


@app.route("/customers/delete/<int:customerid>", methods=['DELETE'])
def delete_customer(customerid):
    try:
        customer = CustomerModel.del_customer(customerid)
        return customer
    except Exception as e:
        raise e


@app.route("/products/<int:prod_id>", methods=['GET'])
def produ_by_id(prod_id):
    try:
        product = ProductModel.get_product_by_id(prod_id)
        total = len(product)
        return product, total
    except Exception as e:
        raise e


@app.route("/products", methods=['GET'])
def get_products():
    brand_name = request.args.get('brand_name')

    try:
        if brand_name is None:
            products = ProductModel.get_products()
            return products
        else:
            products = ProductModel.filter_brand(brand_name)
            return products
    except Exception as e:
        raise e


@app.route("/products/add", methods=['POST'])
def add_product():
    product_name = request.json['product_name']
    brand_id = request.json['brand_id']
    category_id = request.json['category_id']
    model_year = request.json['model_year']
    list_price = request.json['list_price']

    try:
        product = ProductModel.create_product(product_name, brand_id, category_id, model_year, list_price)
        return product
    except Exception as e:
        raise e


@app.route("/products/update/<int:prod_id>", methods=['PUT'])
def update_product(prod_id):
    product_name = request.json['product_name']
    brand_id = request.json['brand_id']
    category_id = request.json['category_id']
    model_year = request.json['model_year']
    list_price = request.json['list_price']

    try:
        prod = ProductModel.mod_product_by_id(product_name, brand_id, category_id, model_year, list_price, prod_id)
        return prod
    except Exception as e:
        raise e


@app.route("/products/delete/<int:prod_id>", methods=['DELETE'])
def remove_product(prod_id):
    try:
        prod = ProductModel.delete_products(prod_id)
        return prod
    except Exception as e:
        raise e


if __name__ == '__main__':
    app.run()
