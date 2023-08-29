from flask import Flask, jsonify

from blueprints.Customers import customer_app
from blueprints.Products import products_app

app = Flask(__name__)
app.register_blueprint(customer_app)
app.register_blueprint(products_app)


@app.route('/')
def info():
    return jsonify({"message": "Trabajo Practico 3.2 ", "Base de datos": "Sales y Productions"})


if __name__ == '__main__':
    app.run()
