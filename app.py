# to run the server: 
# python ap.py

from flask import Flask, request, render_template, url_for, redirect
from helpers import *
from filters import *
from forms import *
import secrets

BASE_URL = "webapp"


app = Flask(__name__)
app.secret_key = secrets.token_hex(32)  # Required for CSRF form protection



@app.route(f"/{BASE_URL}/")
def index():
    return render_template('index.html')


if __name__ == '__main__': 
    app.run(debug=True, port=5000)

    