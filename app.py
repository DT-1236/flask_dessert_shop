from flask import Flask, render_template
from desserts import dessert_list

app = Flask(__name__)


@app.route("/")
def home():
    """Return home page with basic info"""

    return render_template("index.html")
