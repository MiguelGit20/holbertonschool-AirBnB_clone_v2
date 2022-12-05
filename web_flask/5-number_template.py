#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""

from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    new_text = text.replace('_', ' ')
    return 'C {}'.format(escape(new_text))


@app.route("/python/", defaults={'text': 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def python_route(text):
    new_text = text.replace('_', ' ')
    return 'Python {}'.format(escape(new_text))


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    return '{} is a number'.format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template_route(n):
    return render_template('5-number.html', n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
