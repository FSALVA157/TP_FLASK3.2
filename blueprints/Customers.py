from flask import Blueprint, request, jsonify
from models.CustomerModel import CustomerModel

customer_app = Blueprint('customer_app', __name__)


@customer_app.route('/customers/<int:customerid>', methods=['GET'])
def custom_by_id(customerid):
    try:
        customer = CustomerModel.get_customer(customerid)
        return customer
    except Exception as e:
        raise e


@customer_app.route('/customers', methods=['GET'])
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


@customer_app.route('/customers/add', methods=['POST'])
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


@customer_app.route('/customers/update/<int:customerid>', methods=['PUT'])
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


@customer_app.route("/customers/delete/<int:customerid>", methods=['DELETE'])
def delete_customer(customerid):
    try:
        customer = CustomerModel.del_customer(customerid)
        return customer
    except Exception as e:
        raise e
