#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_route():
    cities_obj = [c for c in list(storage.all(City).values())]
    states_obj = [s for s in storage.all(State).values()]
    amenities_obj = [a for a in storage.all(Amenity).values()]

    return render_template(
        "10-hbnb_filters.html",
        cities_obj=cities_obj,
        states_obj=states_obj,
        amenities_obj=amenities_obj)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
