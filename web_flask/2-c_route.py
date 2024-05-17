#!/usr/bin/python3
"""
This module contains a Flask application that defines three routes:
"/", "/hbnb", and "/c/<text>".

The "/" route returns the string "Hello HBNB!" when accessed.

The "/hbnb" route returns the string "HBNB" when accessed.

The "/c/<text>" route takes a text parameter from the URL path,
replaces underscores with spaces, and returns a string that starts with
"C " followed by the processed value of the text parameter.

The Flask application runs on host "0.0.0.0" and port 5000 when
executed directly.
"""


from flask import Flask
from markupsafe import escape


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


@app.route("/c/<text>", strict_slashes=False)
def cIsFun(text):
    """
    This function is a route handler for the "/c/<text>" endpoint in
    a Flask web application.

    Parameters:
    - text (str): The text parameter extracted from the URL path.

    Returns:
    - str: A string that starts with "C " followed by the processed value of
    the text parameter.

    Example:
    >>> cIsFun("hello_world")
    "C hello world"
    """
    var = escape(text).replace("_", " ")
    return f"C {var}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False, port=5000)
