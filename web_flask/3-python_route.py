#!/usr/bin/python3
"""This script starts a basic flask app
"""
from flask import Flask


app = Flask(__name__)


defaults = {'text': 'is cool'}


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'
    """
    return 'HBNB'


@app.route('/c/', defaults=defaults, strict_slashes=False)
@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text):
    """Displays C followed by text content
    """
    return f'C {text.replace("_", " ")}'


@app.route('/python/', defaults=defaults, strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_text(text='is cool'):
    """Displays Python followed by text content
    """
    return f'Python {text.replace("_", " ")}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
