#!/usr/bin/python3
"""Script that import app_views"""
import app_views from api.v1.views
from flask import jsonify

@app_views.route("/status", methods=["GET"], strict_slashes=False)
def api_tatus():
    """a function to return api status"""
    return jsonify({"status": "OK"})
