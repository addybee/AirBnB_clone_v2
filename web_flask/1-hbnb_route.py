#!/usr/bin/python3
"""
This module is a Flask application that defines two routes: "/" and "/hbnb".

The "/" route handler returns a string message "Hello HBNB!" when accessed.

The "/hbnb" route handler returns the string "HBNB" when accessed.

The Flask application runs on host "0.0.0.0" and port 5000.

"""


from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """
    This function is the route handler for the root URL ("/") in
    the Flask application.

    Returns:
        str: A string containing the message "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def user():
    """
    This function is a route handler for the "/hbnb" endpoint.

    Parameters:
        None

    Returns:
        str: The string "HBNB"

    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False, port=5000)
