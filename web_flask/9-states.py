#!/usr/bin/python3
""" Script that starts a flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states/", strict_slashes=False)
def state_list():
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)

@app.route("/states/<id>", strict_slashes=False)
def state_by_id(id=None):
    states_value = storage.all(State)
    if id:
        states = states_value.get('State.{}'.format(id))
    else:
        states = states_value.values()
    return render_template('9-states.html', states=states, found=True)

@app.teardown_appcontext
def teardown(error):
    storage.close()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
