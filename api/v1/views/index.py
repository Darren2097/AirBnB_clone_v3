#!/usr/bin/python3
"""Routing Functions"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def show_status():
    """Shows the OK status"""

    return jsonify({'status': 'OK'})
