#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def route1():
    """Displays an HTML with a list of all States.
    """
    state = storage.all("State")
    return render_template("9-states.html", state=state)



@app.route("/states/<id>", strict_slashes=False)
def route2(id):
    """Displays an HTML with info about <id> (only if exists)"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)


    return render_template("9-states.html")

@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
