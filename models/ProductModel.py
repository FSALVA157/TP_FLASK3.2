from models.entity.Products import Product
from utils.connProd import Conexion


class ProductModel:
    @classmethod
    def get_product_by_id(cls, prod_id):
        conn = Conexion()
        try:
            sql = """SELECT 
                    p.product_id,
                    p.product_name,
                    p.model_year,
                    p.list_price,
                    bd.brand_id, 
                    bd.brand_name,
                    ca.category_id, 
                    ca.category_name from products p
                    inner join brands bd on p.brand_id = bd.brand_id
                    inner join categories ca on p.category_id = ca.category_id
                    where product_id = %s """
            conn.execute(sql, (prod_id,))
            products = conn.fetchall()
            if products is not None:
                prod_list = []
                for produc in products:
                    items = Product(produc[0], produc[1], produc[2], produc[3], produc[4], produc[5], produc[6],
                                    produc[7])
                    prod_list.append(items.to_json())
                return prod_list, 200
            else:
                response_data = {
                    "message": "Product not found"
                }
                return response_data, 404
        except Exception as e:
            raise e

    @classmethod
    def filter_brand(cls, brand_name):
        conn = Conexion()
        try:
            sql = """SELECT product_id,
               product_name,
               model_year,
               list_price,
               b.brand_id,
               b.brand_name,
               c.category_id,
               c.category_name
            from products
                     inner join production.brands b on products.brand_id = b.brand_id
                     inner join categories c on products.category_id = c.category_id
            where b.brand_name = %s"""
            conn.execute(sql, (brand_name,))
            products = conn.fetchall()
            if products is not None:
                product_list = []
                for product in products:
                    items = Product(product[0], product[1], product[2], product[3], product[4], product[5], product[6],
                                    product[7])
                    product_list.append(items.to_json())
                return product_list, 200
            else:
                response_data = {
                    "Message": "Products not found",
                    "Products": products
                }
                return response_data, 404
        except Exception as e:
            raise e

    @classmethod
    def get_products(cls):
        conn = Conexion()
        try:
            sql = """SELECT * from products"""
            conn.execute(sql)
            products = conn.fetchall()
            if products is not None:
                product_list = []
                for product in products:
                    items = {
                        "Products": {
                            "Products_id": product[0],
                            "Products_name": product[1],
                            "Brand_id": product[2],
                            "Category_Id": product[3],
                            "Products_year": product[4],
                            "Products_price": product[5],
                        }
                    }
                    product_list.append(items)
                return product_list, 200
            else:
                response_data = {
                    "message": "Products not found"
                }
                return response_data, 404
        except Exception as e:
            raise e

    @classmethod
    def create_product(cls, product_name, brand_id, category_id, model_year, list_price):
        conn = Conexion()
        try:
            sql = """INSERT INTO products (product_name, brand_id, category_id, model_year, list_price) 
                        VALUES (%s, %s, %s, %s, %s)"""
            conn.execute(sql, (product_name, brand_id, category_id, model_year, list_price))
            if conn.rowcount() > 0:
                response_data = {
                    "message": "Product registered successfully"
                }
                return response_data, 201
            else:
                response_data = {
                    "message": "Product not registered"
                }
                return response_data, 400
        except Exception as e:
            raise e

    @classmethod
    def mod_product_by_id(cls, product_name, brand_id, category_id, model_year, list_price, prod_id):
        conn = Conexion()
        try:
            sql = """UPDATE products SET product_name = %s, brand_id = %s, category_id = %s, model_year = %s, 
            list_price = %s
            WHERE product_id = %s"""
            conn.execute(sql, (product_name, brand_id, category_id, model_year, list_price, prod_id,))
            if conn.rowcount() > 0:
                response_data = {
                    "message": "Product updated successfully"
                }
                return response_data, 201
            else:
                response_data = {
                    "message": "Product not updated"
                }
                return response_data, 400
        except Exception as e:
            raise e

    @classmethod
    def delete_products(cls, prod_id):
        conn = Conexion()
        try:
            sql = """DELETE FROM products WHERE product_id = %s"""
            conn.execute(sql, (prod_id,))
            if conn.rowcount() > 0:
                response_data = {
                    "message": "Product deleted successfully"
                }
                return response_data, 200
            else:
                response_data = {
                    "message": "Product not deleted"
                }
                return response_data, 400
        except Exception as e:
            raise e
