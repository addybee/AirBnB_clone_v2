#!/usr/bin/python3
"""
This module defines a Flask application for listing states.

It includes routes to display a sorted list of state objects fetched from
a storage backend. The application also handles the teardown of
the application context by closing the database connection.
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


@app.route("/cities_by_states", strict_slashes=False)
def list_state_cities():
    """
    Route to display a list of cities by states sorted by name.

    Returns:
        Rendered template with list of cities by states context.
    """
    try:
        states = storage.all(State)
        return render_template("8-cities_by_states.html", states=states)
    except Exception as e:
        return str(e), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
