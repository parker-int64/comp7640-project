import logging
import pymysql
import json
from flask import jsonify

# logging settings



class Query:
    """
        This is the sql query class
        host: database address
        user: database root user
        passwd: user's password
        port: default 3306
        charset: default utf-8
    """
    def __init__(self, host:str, user:str, passwd:str, db:str="estore", port:int=3306, charset:str='utf8') -> None:

        self.host = host
        self.user = user
        self.passwd = passwd
        self.port = port
        self.db = db
        self.charset = charset

        conv = pymysql.converters.conversions
        conv[246] = float
        conv[10]  = str
        conv[7]   = str
        conv[12]  = str
        conv[11]  = str

        self.conv = conv

        conn = pymysql.connect(host=self.host,
                            user=self.user,
                            passwd=self.passwd,
                            port=self.port,
                            db=self.db,
                            charset=self.charset
                            )
        cur = conn.cursor(pymysql.cursors.DictCursor)
        self.conn = conn
        self.cur  = cur

    def query_products(self, *args, **kwargs):
        """
            This query select all the products and their related information

            If query executed successfully, the corresponding data will return

            If not, it will return 405 (method not allowed) as default

            Also, 
            1. this function supports to query a single item by its product_ID
            2. Support query with key value pair. That is, you may use `name`, `tag` to find product
        """
        query_sql = "SELECT product.*, vendor.business_name, vendor.customer_feedback_score FROM product " \
                    "LEFT JOIN vendor ON product.vendor_ID = vendor.vendor_ID;"
        
        if args and len(args) == 1:
            query_sql = "SELECT product.*, vendor.business_name, vendor.customer_feedback_score FROM product " \
                    "LEFT JOIN vendor ON product.vendor_ID = vendor.vendor_ID WHERE product_ID = %s;"
            return self.select_sql(query_sql, args)

        if kwargs:
            logging.info("Kwargs %s", kwargs)
            keys_list = kwargs.keys()
            values_list = [f"%{value.lower()}%" for value in kwargs.values()] # lowercase


            query_sql = "SELECT product.*, vendor.business_name, vendor.customer_feedback_score FROM product " \
                        "LEFT JOIN vendor ON product.vendor_ID = vendor.vendor_ID " \
                        "WHERE LOWER(CONCAT(product_name, Tag1, Tag2, Tag3)) LIKE %s " \
                        "ORDER BY product_ID;"
            return self.select_sql(query_sql, values_list)

        return self.select_sql(query_sql)
    
    def query_vendor(self, *args):
        """
            This query select all the vendors and their related information

            or query a single vendor by vendor_ID

            If query executed successfully, the corresponding data will return

            If not, it will return 405 (method not allowed) as default
        """

        query_sql = "SELECT * FROM vendor"

        if args and len(args) == 1:
            query_sql = "SELECT * FROM vendor WHERE vendor_ID = %s"
        
            return self.select_sql(query_sql, args)
        
        return self.select_sql(query_sql)


    def query_customer(self, *args):
        """
            This query select all the customer and their related information (id, contact number)
        """
        query_sql = "SELECT * FROM customer"

        if args and len(args) == 1:
            query_sql = "SELECT * FROM vendor WHERE customer_ID = %s"
            return self.select_sql(query_sql, args)
        
        return self.select_sql(query_sql)
    

    def query_trans(self, *args):
        """
            by default, this method return all the transaction records
            you may also specify a `customer_ID` to view his/her transaction records 
        """
        query_sql = '''
                    SELECT t.*, p.product_name, c.customer_ID, c1.contact_number, c1.shipping_details
                    FROM transaction_include_products t1 
                    LEFT JOIN `transaction` t ON t1.transaction_ID = t.transaction_ID
                    LEFT JOIN product p ON t1.product_ID = p.product_ID
                    LEFT JOIN customer_buy_transactions c ON c.transaction_ID = t1.transaction_ID
                    LEFT JOIN customer c1 ON c.customer_ID = c1.customer_ID;
                    '''

        return self.select_sql(query_sql)

    
    

    def add_product(self, *args):
        """
            this method allow vendor to add a single product
        """
        insert_sql = "INSERT INTO product " \
                     "VALUES (null, %s, %s, %s, %s, %s, %s)"
        
        return self.insert_sql(insert_sql, *args)


    def add_vendor(self, *args):
        """
            This query add a single vendor
        """

        logging.info("Data in add_vendor %s", *args)
        

        insert_sql = "INSERT INTO vendor " \
                     "VALUES (NULL, %s, %s, %s, %s, %s)"
        
        return self.insert_sql(insert_sql, *args)

    def add_customer(self, *args):
        """
            This query add a single customer
        """

        insert_sql = "INSERT INTO customer " \
                     "VALUES (null, %s, %s, %s, %s)"
        
        self.insert_sql(insert_sql, args)


    def add_trans(self, *args):
        """
            This query add a single transaction.
        """

    def del_trans(self, *args):
        """
            This query del (cancel) a single transaction
        """


    def select_sql(self, query_sql, *args):
        """
            overall select query
        """
        data = None

        try:
            row = None
            if args:
                row = self.cur.execute(query_sql, args)
            else:
                row = self.cur.execute(query_sql)
            data = self.cur.fetchall()
            logging.info("SQL sentence: %s", query_sql)
            logging.info("[PyMysql] SQL executed successfully, rows affected: %s", row)
        except pymysql.Error as e:
            logging.error("[PyMysql] SQL executed failed: %s", e)
            raise e

        return jsonify(data)
    

    def insert_sql(self, query_sql, *args):
        """
            handle insert
        """

        logging.info("SQL sentence: %s", query_sql)

        try:
            row = None
            if args:
                row = self.cur.execute(query_sql, args)
            else:
                row = self.cur.execute(query_sql)
            
            logging.info("[PyMysql] SQL executed successfully, rows affected: %s", row)

            self.conn.commit()
        except pymysql.Error as e:
            self.conn.rollback()
            logging.error("[PyMysql] SQL executed failed: %s", e)
            raise e
    

    def del_sql(self, query_sql, *args):
        """
            handle delete, use with cautious
        """

        logging.info("SQL sentence: %s", query_sql)

        try:
            row = None
            if args:
                row = self.cur.execute(query_sql, args)
            else:
                row = self.cur.execute(query_sql)
            
            logging.info("[PyMysql] SQL executed successfully, rows affected: %s", row)

            # self.conn.commit()  # up until successfully execute the query, do not add this sentence
        except pymysql.Error as e:
            self.conn.rollback()
            logging.error("[PyMysql] SQL executed failed: %s", e)
            raise e




    def close_connection(self):
        """
            Close pymysql connection
        """
        self.cur.close()
        self.conn.close()


# For some simple test
if __name__ == "__main__":
    sql = Query("localhost", "root", "huxiaochuan")
    print(sql.query_products())
    sql.close_connection()
