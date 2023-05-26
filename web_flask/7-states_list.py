#!/usr/bin/python3
"""
  Script that sets up states unordered list
  using flask
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name_)

@app.teardown_appcontext
def close():
    storage.close()

@app.route('/states_list', strict_slashes=False)
def states():
    states = storagee.all("States")
    sorted_states = sorted(states.values(), key=lambda s: s.name)
    return render_template('7-states_list', states=sorted_states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
