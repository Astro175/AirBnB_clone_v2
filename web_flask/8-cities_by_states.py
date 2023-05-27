#!/usr/bin/python3
"""
  Script that loads states and run them using jinja
  template with flask
"""
from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)

@app.teardown_appcontext
def close():
    storage.close()

@app.route('/cities_by_states', strict_slashes=False)
def states():
    states = storage.all(State)
    sorted_states = sorted(states.value(), key=lambda s: s.name)
    return render_template('8-cities_by_states.html', states=sorted_states)

if __main__ == '__name__':
    app.run(host='0.0.0.0', port=5000)
