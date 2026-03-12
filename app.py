# to run the server: 
# python ap.py

from flask import Flask, request, render_template, url_for, redirect
from helpers import *
from filters import *
from forms import *
import secrets


app = Flask(__name__)
app.secret_key = secrets.token_hex(32)  # Required for CSRF form protection

# setup filters to be accessible in templates
app.add_template_filter(rgb_to_hex, 'rgb_to_hex')

@app.route("/")
def index():
    color = get_one_color(5)

    name = "stranger"

    return render_template(
            'index.html', 
            color=color, 
            name = name)

@app.route("/random")
def color_random():
    color = get_random_color()

    return render_template(
            'color_random.html', 
            color=color)


if __name__ == '__main__': 
    app.run(debug=True)

    