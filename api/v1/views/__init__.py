#!/usr/bin/python3
"""initialization file for views module"""
from flask import Blueprint

<<<<<<< HEAD
app_views = Blueprint("app_views", __name__, url_prefix='/api/v1')

from api.v1.views.index import *
=======
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")
>>>>>>> c8f399eaa9ff65a9ffdfa05c49c3b8b12308bb8c
