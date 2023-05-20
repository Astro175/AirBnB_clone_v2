#!/usr/bin/python3
"""
   Script that uses flask to route with variables
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Function that displays Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """Function that diplayes HBNB"""
    return "HBNB!"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Function that displays C is text variable"""
    text = text.replace("_", " ")
    return "C {}".format(text)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
