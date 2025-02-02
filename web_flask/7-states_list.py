#!/usr/bin/python3
""" Script that starts a flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list/", strict_slashes=False)
def s_list():
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(error):
    storage.close()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
