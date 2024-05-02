#!/usr/bin/python3
"""
web_flask/7-states_list.py
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def state_list():
    """Prints list of all states in sorted order"""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


# Define a function to handle teardown
@app.teardown_appcontext
def teardown_appcontext(self):
    """close session context"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
