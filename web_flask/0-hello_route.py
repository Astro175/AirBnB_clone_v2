#!/usr/bin/python3
"""Module that uses flask to run simple hello HBNB"""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Function that returns a string"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
