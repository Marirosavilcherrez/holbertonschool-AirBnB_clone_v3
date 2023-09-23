#!/usr/bin/python3
"""Script that starts a Flask web"""
from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_route(error):
    "Close the SQLAlchemy Session"
    storage.close()


if __name__ == '__main__':
<<<<<<< HEAD
    port = int(os.environ.get('HBNB_API_PORT', 5000))
    app.run(host='localhost', port=port, threaded=True)
=======
    host = getenv("HBNB_API_HOST") if getenv("HBNB_API_HOST") else "0.0.0.0"
    port = getenv("HBNB_API_PORT") if getenv("HBNB_API_PORT") else 5000
    app.run(host=host, port=port, threaded=True)
>>>>>>> c8f399eaa9ff65a9ffdfa05c49c3b8b12308bb8c
