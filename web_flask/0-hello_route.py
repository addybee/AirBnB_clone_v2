#!/usr/bin/python3
"""
This module sets up a basic Flask application and defines a route
handler for the root URL.

The Flask application is instantiated and configured. A single route (`"/"`)
is defined, which when accessed, returns a greeting message.

Functions:
    index() -> str: Returns a greeting message when the root URL is accessed.
"""
from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    """
    This function is the route handler for the root URL ("/") in
    the Flask application.

    Returns:
        str: A string containing the message "Hello HBNB!"
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False, port=5000)
