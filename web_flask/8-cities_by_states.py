#!/usr/bin/python3
"""
web_flask/7-states_list.py
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Prints list of all states in sorted order"""
    states = storage.all(State)
    cities = storage.all(City)
    city_by_state = {
        state: [city for city in cities.values() if city.state_id == state.id]
        for state in states.values()
    }
    # print(city_by_state)
    return render_template("8-cities_by_states.html", states=city_by_state)


# Define a function to handle teardown
@app.teardown_appcontext
def teardown_appcontext(self):
    """close session context"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
