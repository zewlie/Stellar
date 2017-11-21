"""Stellar server."""

import random

from jinja2 import StrictUndefined
from flask import Flask, Markup, render_template, redirect, request, flash, session, jsonify, url_for, abort
from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.login import LoginManager, login_required, login_user, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from models import db, connect_to_db
from models import User, Square

app = Flask(__name__)

# Flask Login
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.init_app(app)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined

# Global variables

BACK_TO_ROOT = "../../"

# Functions not associated with particular routes
#################################################################################

#################################################################################

# TODO: Use Flask Login

@app.route('/')
def index():
    """Homepage."""

    squares_dict = {}
    for x in range(0,26):
        squares_dict[x] = {}

    squares = db.session.query(Square).all()
    for square in squares:
        squares_dict[square.x][square.y] = square.fill


    return render_template('index.html', squares_dict=squares_dict)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()