#!/usr/bin/python3
""" This Python module uses Flask to manage state information via a web
    application. It interacts with a data storage system from the models
    package to handle state data. The module features routes for listing
    states or a specific state by ID and includes a function to close the
    database connection post-request.
"""


from flask import Flask, render_template
from models import storage, State


app = Flask(__name__)


@app.teardown_appcontext
def do_teardown(exception=None):
    """
    Close the database connection when the application context is torn down.
    """
    storage.close()


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states(id=None):
    """
    Handle web requests to the "/states" and "/states/<id>" URLs.

    Args:
        id (str, optional): A specific state ID to filter states,
        passed as part of the URL.

    Returns:
        str : content rendered by the "9-states.html" template if successful,
                or error message and a 500 status code if an exception occurs.
    """
    try:
        states = storage.all(State)
        return render_template("9-states.html", states=states, id=id)
    except Exception as e:
        return str(e), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
