#!/usr/bin/python3
"""Script that starts a Flask web"""
from flask import Flask, render_template
from models import storage
from api.v1.views import app_views
import os


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_route(error):
    "Close the SQLAlchemy Session"
    storage.close()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, threaded=True)
