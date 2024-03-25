import os
import logging
from flask import Flask, render_template, request, abort
from utils.project_config import (STATIC_DIR, SQL_USER, SQL_HOST, SQL_PASSWD)
from services.query import Query

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
def get_all_products():
    """
        retrieve all products information
    """
    res = sql.query_products()

    return res if res != 'null' else abort(404)


@app.route("/getVendor", methods=["POST"])
def get_vendors():
    """
        retrieve all vendors information
    """
    res = sql.query_vendor()

    return res if res != 'null' else abort(404)

@app.route("/getCustomer", methods=["POST"])
def get_customer():
    """
        retrieve all customers information
    """
    res = sql.query_customer()

    return res if res != 'null' else abort(404)

if __name__ == "__main__":
    
    app.run()
