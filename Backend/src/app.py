import os
from flask import Flask, render_template, jsonify, request
from utils.project_config import (BACKEND_DIR,
                                  PROJECT_DIR,
                                  STATIC_DIR)
import logging

# logging settings
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
# Some settings
# os.environ[""]

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

if __name__ == "__main__":
    
    app.run()
