#!/usr/bin/python3
"""
   Script that uses flask to route with variables
"""

from flask import Flask
from flask import render_template
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


@app.route('/python/', defaults={'text': 'is cool'},
           strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """
       Function that displays Python is text
       variable
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
       Function that displays n, if it is a number
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>',
           strict_slashes=False)
def number_template(n):
    """
      Function that displays html page of n
      if it is a number
    """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
