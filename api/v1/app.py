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
    host = os.environ.get("HBNB_API_HOST", "0.0.0.0")
    port = int(os.environ.get("HBNB_API_PORT", 5000))

    app.run(host=host, port=port, threaded=True)
