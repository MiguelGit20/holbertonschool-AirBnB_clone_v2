#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""
from flask import Flask
from markupsafe import escape
from flask import render_template
from models import storage
from models.state import State
from models.city import City
from os import getenv
from sqlalchemy.orm import relationship

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_state():
    from models.state import State
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities_obj = [c for c in list(storage.all(City).values())]
        states_obj = [s for s in storage.all(State).values()]
        return render_template(
            "8-cities_by_states.html",
            states_obj=states_obj, cities_obj=cities_obj)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
