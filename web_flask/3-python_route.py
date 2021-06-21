#!/usr/bin/python3
""" Script that starts a flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/(<text>)', strict_slashes=False)
def p_text(text="is cool"):
    return "Python {}".format(text.replace('_', ' '))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
