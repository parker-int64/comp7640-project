import os
import logging
from flask import Flask, render_template, request, abort
from utils.project_config import (STATIC_DIR, SQL_USER, SQL_HOST, SQL_PASSWD)
from services.query import Query

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
# os.environ[""]

# Init our database
sql = Query(SQL_HOST, SQL_USER, SQL_PASSWD)


app = Flask(__name__,
            static_folder=STATIC_DIR/"static",
            template_folder=STATIC_DIR,
            static_url_path="/static")

@app.route("/", defaults={
    "path": ""
})

@app.route("/<path:path>")
def index(path):
    return render_template("index.html")


@app.route("/validUser", methods=['POST'])
def validUser():
    data = request.json
    logging.info("Content %s", data)
    return "Transformed"


@app.route("/getProducts", methods=["POST"])
def get_products():
    """
        retrieve all products information
    """

    data = request.json

    # logging.info("Request body: %s", data)

    if data:
        res = sql.query_products(**data)
    else:
        res = sql.query_products()  # res contains the response

    return res


@app.route("/getVendor", methods=["POST"])
def get_vendors():
    """
        retrieve all vendors information
    """
    res = sql.query_vendor()

    return res
@app.route("/getCustomer", methods=["POST"])
def get_customer():
    """
        retrieve all customers information
    """
    res = sql.query_customer()

    return res

@app.route("/addVendor", methods=['POST'])
def add_vendor():
    """
        add a new vendor
    """
    data = request.json

    message = 'ok'

    try:
        res = sql.add_vendor(*data)
    except Exception as e:
        message = str(e)


    return {"message": message}

@app.route("/addProduct", methods=['POST'])
def add_product():
    """
        add a new product
    """
    data = request.json

    message = 'ok'

    try:
        res = sql.add_product(*data)
    except Exception as e:
        message = str(e)

    return {"message": message}

if __name__ == "__main__":
    
    app.run(port=5000, debug=True)
