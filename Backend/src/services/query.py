import logging
import pymysql
import json


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
        cur = conn.cursor()
        self.conn = conn
        self.cur  = cur     

    def query_products(self):
        """
            This query select all the products and their related information

            If query executed successfully, the corresponding data will return

            If not, it will return 'null' as default
        """
        query_sql = "SELECT product.*, vendor.business_name, vendor.customer_feedback_score FROM product " \
                    "LEFT JOIN vendor ON product.vendor_ID = vendor.vendor_ID;"

        data = None

        try:
            row = self.cur.execute(query_sql)
            data = self.cur.fetchall()
            logging.debug("SQL sentence: %s", query_sql)
            logging.info("[PyMysql] SQL executed successfully, rows affected: %s", row)
        except pymysql.Error as e:
            logging.error("[PyMysql] SQL executed failed: %s", e)

        return json.dumps(data)
    
    def query_vendor(self):
        """
            This query select all the vendors and their related information

            If query executed successfully, the corresponding data will return

            If not, it will return 'null' as default
        """
        query_sql = "select * from `vendor`"

        data = None

        try:
            row = self.cur.execute(query_sql)
            data = self.cur.fetchall()
            logging.debug("SQL sentence: %s", query_sql)
            logging.info("[PyMysql] SQL executed successfully, rows affected: %s", row)
        except pymysql.Error as e:
            logging.error("[PyMysql] SQL executed failed: %s", e)


        return json.dumps(data)

    def query_customer(self):
        """
            This query select all the vendors and their related information
        """
        query_sql = "select * from `customer`"

        data = None

        try:
            row = self.cur.execute(query_sql)
            data = self.cur.fetchall()
            logging.debug("SQL sentence: %s", query_sql)
            logging.info("[PyMysql] SQL executed successfully, rows affected: %s", row)
        except pymysql.Error as e:
            logging.error("[PyMysql] SQL executed failed: %s", e)

        return json.dumps(data)


    def add_vendor(self):
        """
            This query add a single vendor
        """

    def add_customer(self):
        """
            This query add a single customer
        """


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
