#!/usr/bin/python3
"""This script starts a basic flask app
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Return a simple hello message
    """
    return 'Hello HBNB'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns a simple response
    """
    return 'HBNB'
