# run, from ./ FLASK_APP=flask_fib.py poetry run flask run
# export FLASK_APP=flask_fib
# export LC_ALL=C.UTF-8
# export LANG=C.UTF-8

from flask import Flask

app = Flask(__name__)


@app.route("/")
def print_fib():
    return "<h1>Fibonacci</h1>"


@app.route("/fib")
def list_fib():
    return "<b>1, 1, 2, 3, 5, 8, 13, 21 ...</b>"
