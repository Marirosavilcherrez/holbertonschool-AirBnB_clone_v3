#!/usr/bin/python3
"""Script that starts a Flask web"""
from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage
import os
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_route(error):
    "Close the SQLAlchemy Session"
    storage.close()


if __name__ == '__main__':

    port = int(os.environ.get('HBNB_API_PORT', 5000))
    cors = CORS(app, origins="0.0.0.0")
    app.run(host='localhost', port=port, threaded=True)
