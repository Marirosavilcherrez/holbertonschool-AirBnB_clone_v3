#!/usr/bin/python3
"""Script that starts a Flask web"""
from api.v1.views import app_views
from flask import Flask, jsonify, make_response
from flask_cors import CORS
from models import storage
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, origins="0.0.0.0")


@app.teardown_appcontext
def close_route(error):
    "Close the SQLAlchemy Session"
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    host = getenv("HBNB_API_HOST") if getenv("HBNB_API_HOST") else "0.0.0.0"
    port = getenv("HBNB_API_PORT") if getenv("HBNB_API_PORT") else 5000
    app.run(host=host, port=port, threaded=True)
