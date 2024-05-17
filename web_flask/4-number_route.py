#!/usr/bin/python3
"""
This code snippet is a Flask application that defines several routes and
their corresponding route handlers.

The first route handler is for the root URL ("/") and returns a string
"Hello HBNB!".

The second route handler is for the "/hbnb" endpoint and returns
a string "HBNB".

The third route handler is for the "/c/<text>" endpoint and takes a text
parameter from the URL path. It returns a string that starts with "C "
followed by the processed value of the text parameter. The text parameter
is sanitized by replacing underscores with spaces.

The fourth route handler is for the "/python/" and "/python/<text>" endpoints.
It takes an optional text parameter from the URL path and returns a string
that says "Python" followed by the sanitized value of the text parameter.
The text parameter is sanitized by replacing underscores with spaces.

The fifth route handler is for the "/number/<n>" endpoint and takes an integer
parameter from the URL path. It returns a string indicating that the provided
value is a number.

The Flask application is run on host "0.0.0.0" and port 5000.

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
    sanitized_text = escape(text).replace("_", " ")
    return f"C {sanitized_text}"


@app.route('/python/')
@app.route("/python/<text>", strict_slashes=False)
def pythonIsCool(text: str = "is cool"):
    """
    Returns a string that says "Python" followed by the value of `text` with
    underscores replaced by spaces.

    Args:
        text (str): The value of `text` extracted from the URL path.

    Returns:
        str: A string that says "Python" followed by the sanitized value of
        `text`.
    """
    sanitized_text = escape(text).replace('_', ' ')
    return f"Python {sanitized_text}"


@app.route("/number/<int:n>", strict_slashes=False)
def isNumber(n: int):
    """
    Returns a string indicating that the provided value is a number.

    Args:
        n (int): The number provided as a parameter in the URL.

    Returns:
        str: A string indicating that the provided value is a number.
    """
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False, port=5000)
