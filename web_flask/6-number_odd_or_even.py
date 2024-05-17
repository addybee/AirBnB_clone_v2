#!/usr/bin/python3
"""
This module contains a Flask application that defines several routes and their
corresponding route handlers.

The routes are as follows:

1. Route: "/"
2. Route: "/hbnb"
3. Route: "/c/<text>"
4. Route: "/python/" and "/python/<text>"
5. Route: "/number/<int:n>"
6. Route: "/number_template/<int:n>"
7. Route: "/number_odd_or_even/<int:n>"

The Flask application runs on host "0.0.0.0" and port 5000.

"""

from flask import Flask, render_template
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


@app.route("/number_template/<int:n>")
def numberTemplate(n: int):
    """
    Renders the template '5-number.html' with the value of 'n' passed
    as a variable.

    Args:
        n (int): The integer parameter passed from the URL.

    Returns:
        str: The rendered template as a response to the client.
    """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>")
def oddOrEven(n: int):
    """
    Renders a template called '6-number_odd_or_even.html' with the input
    parameter passed to it.

    Args:
        n (int): The input parameter passed to the route.

    Returns:
        str: The rendered template '6-number_odd_or_even.html' with the
        input parameter passed as a variable 'n'.
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False, port=5000)
