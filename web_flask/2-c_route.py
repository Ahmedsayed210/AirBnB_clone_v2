#!/usr/bin/python3
"""Scripts that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C_is_fun(text):
    return "C" + text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
