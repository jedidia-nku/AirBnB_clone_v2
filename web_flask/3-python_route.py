#!/usr/bin/python3
"""
AirBnB_clone_v2/web_flask/0-hello_route.py
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """Returns page"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns page"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Returns page"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False, defaults={'text': 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """Returns page"""
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    print("Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)")
    app.run(host='0.0.0.0', port=5000)
