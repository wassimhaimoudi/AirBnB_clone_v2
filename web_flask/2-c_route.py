#!/usr/bin/python3
"""This script starts a basic flask web app
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Returns a simple hello message
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns a simple message
    """
    return 'HBNB'


@app.route('/c/<string:text>')
def c_text(text):
    """displays “C ” followed by the value of the text variable
    """
    t = str.maketrans("_", " ")
    new_text = text.translate(t)
    return f'C {new_text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
