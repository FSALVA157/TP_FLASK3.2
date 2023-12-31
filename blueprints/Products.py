from flask import Blueprint, request, jsonify
from models.ProductModel import ProductModel

products_app = Blueprint('products_app', __name__)


@products_app.route("/products/<int:prod_id>", methods=['GET'])
def produ_by_id(prod_id):
    try:
        product = ProductModel.get_product_by_id(prod_id)
        return product
    except Exception as e:
        raise e


@products_app.route("/products", methods=['GET'])
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


@products_app.route("/products/add", methods=['POST'])
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


@products_app.route("/products/update/<int:prod_id>", methods=['PUT'])
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


@products_app.route("/products/delete/<int:prod_id>", methods=['DELETE'])
def remove_product(prod_id):
    try:
        prod = ProductModel.delete_products(prod_id)
        return prod
    except Exception as e:
        raise e
