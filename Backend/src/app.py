import os
from flask import Flask, render_template
from pathlib import Path



# Some settings
# os.environ[""]

# cross platform path library.
# this should work on across multiple os
CURRENT_DIR = Path(__file__).parent
PROJECT_DIR =  CURRENT_DIR.parent.parent
FRONTEND_DIR = PROJECT_DIR/"Frontend/dist"


app = Flask(__name__,
            static_folder=FRONTEND_DIR/"static",
            template_folder=FRONTEND_DIR,
            static_url_path="/static")

@app.route("/", defaults={
    "path": ""
})

@app.route("/<path:path>")
def index(path):
    return render_template("index.html")


if __name__ == "__main__":
    print(f"Current directory: {CURRENT_DIR}, Project directory {PROJECT_DIR}, Frontend directory {FRONTEND_DIR}")
    app.run()
