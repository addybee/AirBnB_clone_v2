#!/usr/bin/python3
"""
Flask web application that handles routes and teardown for a web service.

The code snippet defines a Flask web application with routes to display
states, cities, and amenities using a template. It also includes a function
to close the database connection after each request.

Example Usage:
Assuming the Flask app is running, you can access the functionality via
a web browser:
Visit http://0.0.0.0:5000/hbnb_filters to see the rendered HTML page with
states, cities, and amenities.

Inputs:
- exception: Optional. Used in the teardown function to handle exceptions
during the teardown process.

Outputs:
- HTML content rendered from the `10-hbnb_filters.html` template populated
with states, cities, and amenities data, or an error message with a 500 status
code in case of an exception.
"""


from flask import Flask, render_template
from models import storage, State, City, Amenity


app = Flask(__name__)


@app.teardown_appcontext
def do_teardown(exception=None):
    """
    Close the database connection when the application context is torn down.
    """
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filter():
    """
    Retrieve data about states, cities, and amenities from storage and
    render a template.

    Returns:
        str: Rendered HTML page with data about states, cities, and amenities.
        If an exception occurs, returns an error message with a 500 status
        code.
    """
    try:
        states = storage.all(State)
        cities = storage.all(City)
        amenities = storage.all(Amenity)
        return render_template("10-hbnb_filters.html", states=states,
                               cities=cities, amenities=amenities)
    except Exception as e:
        return str(e), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
