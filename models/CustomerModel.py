from utils.connSales import Conexion


class CustomerModel:

    @classmethod
    def get_customer(cls, customerid):
        conn = Conexion()
        try:
            sql = """SELECT * FROM customers WHERE customer_id = %s"""
            params = (customerid,)
            conn.execute(sql, params)
            customer = conn.fetchall()
            if customer is not None:
                response_data = {
                    "CustomerID": customer[0][0],
                    "FirstName": customer[0][1],
                    "LastName": customer[0][2],
                    "Phone": customer[0][3],
                    "Email": customer[0][4],
                    "Street": customer[0][5],
                    "City": customer[0][6],
                    "State": customer[0][7],
                    "ZipCode": customer[0][8],
                }
                return response_data, 200
            else:
                response_data = {
                    "Message": "Customer not found"
                }
                return response_data, 404
        except Exception as e:
            raise e

    @classmethod
    def customers_state(cls, state):
        conn = Conexion()
        try:
            sql = """SELECT * FROM customers WHERE state = %s"""
            params = (state,)
            conn.execute(sql, params)
            customers = conn.fetchall()
            if customers is not None:
                response_data = []
                for customer in customers:
                    response_data.append({
                        "CustomerID": customer[0],
                        "FirstName": customer[1],
                        "LastName": customer[2],
                        "Phone": customer[3],
                        "Email": customer[4],
                        "Street": customer[5],
                        "City": customer[6],
                        "State": customer[7],
                        "ZipCode": customer[8],
                    })
                return response_data, 200
            else:
                response_data = {
                    "Message": "Customers not found"
                }
                return response_data, 404
        except Exception as e:
            raise e

    @classmethod
    def get_customers(cls):
        conn = Conexion()
        try:
            sql = """SELECT * FROM customers"""
            conn.execute(sql)
            customers = conn.fetchall()
            if customers is not None:
                response_data = []
                for customer in customers:
                    response_data.append({
                        "CustomerID": customer[0],
                        "FirstName": customer[1],
                        "LastName": customer[2],
                        "Phone": customer[3],
                        "Email": customer[4],
                        "Street": customer[5],
                        "City": customer[6],
                        "State": customer[7],
                        "ZipCode": customer[8],
                    })
                return response_data, 200
            else:
                response_data = {
                    "Message": "Customers not found"
                }
                return response_data, 404
        except Exception as e:
            raise e

    @classmethod
    def create_customer(cls, firstname, lastname, phone, email, street, city, state, zipcode):
        conn = Conexion()
        try:
            sql = """INSERT INTO customers (first_name, last_name, phone, email, street, city, state, zip_code) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
            params = (firstname, lastname, phone, email, street,
                      city, state, zipcode)
            conn.execute(sql, params)
            conn.commit()
            if conn.rowcount() > 0:
                response_data = {
                    "Message": "Customer created successfully"
                }
                return response_data, 201
            else:
                response_data = {
                    "Message": "Customer not created"
                }
                return response_data, 400
        except Exception as e:
            raise e

    @classmethod
    def update_customer(cls, email, phone, street, state, city, zip_code, customerid):
        conn = Conexion()
        try:
            sql = """UPDATE customers SET email = %s, phone = %s, street = %s, state = %s, city = %s, zip_code = %s 
            WHERE customer_id = %s"""
            conn.execute(sql, (email, phone, street, state, city, zip_code, customerid,))
            conn.commit()
            if conn.rowcount() > 0:
                response_data = {
                    "Message": "Customer updated successfully"
                }
                return response_data, 200
            else:
                response_data = {
                    "Message": "Customer not updated"
                }
                return response_data, 400
        except Exception as e:
            raise e

    @classmethod
    def del_customer(cls, customerid):
        conn = Conexion()
        try:
            sql = """DELETE FROM customers WHERE customer_id = %s"""
            conn.execute(sql, (customerid,))
            conn.commit()
            if conn.rowcount() > 0:
                response_data = {
                    "Message": "Customer deleted successfully"
                }
                return response_data, 200
            else:
                response_data = {
                    "Message": "Customer not deleted"
                }
                return response_data, 400
        except Exception as e:
            raise e