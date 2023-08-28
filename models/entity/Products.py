class Product:

    def __init__(self, prod_id, prod_name, prod_year, prod_price, brand_id, brand_name, category_id, category_name):
        self.prod_id = prod_id
        self.prod_name = prod_name
        self.prod_year = prod_year
        self.prod_price = prod_price
        self.brand_id = brand_id
        self.brand_name = brand_name
        self.category_id = category_id
        self.category_name = category_name

    def to_json(self):
        response_data = {
            "Product": {
                "product_id": self.prod_id,
                "product_name": self.prod_name,
                "product_year": self.prod_year,
                "product_price": self.prod_price,
            },
            "Brand": {
                "brand_id": self.brand_id,
                "brand_name": self.brand_name
            },
            "Category": {
                "category_id": self.category_id,
                "category_name": self.category_name
            }
        }
        return response_data

    def json_(self):
        response_data = {
            "Products": {
                "Products_name": self.prod_name,
                "Products_id": self.prod_id,
                "Products_year": self.prod_year,
                "Products_price": self.prod_price,
                "Brand_id": self.brand_id,
                "Brand_name": self.brand_name,
                "Category_id": self.category_id,
                "Category_name": self.category_name
            }
        }
        return response_data


class ProductBrand:

    def __init__(self, brand_id, brand_name):
        self.brand_id = brand_id
        self.brand_name = brand_name

    def to_json(self):
        response_data = {
            "Brand": {
                "brand_id": self.brand_id,
                "brand_name": self.brand_name
            }
        }
        return response_data
