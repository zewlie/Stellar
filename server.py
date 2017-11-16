"""Q server."""

import random

from jinja2 import StrictUndefined
from flask import Flask, Markup, render_template, redirect, request, flash, session, jsonify, url_for, abort
from flask_debugtoolbar import DebugToolbarExtension
from datetime import datetime

app = Flask(__name__)

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

    return render_template('index.html')

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True


    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()