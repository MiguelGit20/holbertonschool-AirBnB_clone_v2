#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City
from os import getenv

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_route():
    states_obj = [s for s in storage.all(State).values()]
    return render_template("9-states.html", states_obj=states_obj)


@app.route('/states/<id>', strict_slashes=False)
def states_id_route(id):
    cities_obj = [c for c in list(storage.all(City).values())]
    states_obj = [s for s in storage.all(State).values()]
    states_ids = [s.id for s in storage.all(State).values()]
    state_name = [s.name for s in storage.all(State).values() if s.id == id]
    s_name = ''
    if len(state_name) >= 1:
        for i in state_name:
            s_name += i
    else:
        s_name = ''
    return render_template(
        "9-states.html", id=id,
        cities_obj=cities_obj,
        states_obj=states_obj,
        s_name=s_name,
        states_ids=states_ids)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
