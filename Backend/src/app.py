import os
from flask import Flask, render_template
from utils.project_config import (BACKEND_DIR,
                                  PROJECT_DIR,
                                  STATIC_DIR)


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


if __name__ == "__main__":
    
    app.run()
