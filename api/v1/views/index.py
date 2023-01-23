#!/usr/bin/python3
"""Routing Functions"""

<<<<<<< HEAD
from api.v1.views import app_views
=======
from api.v1.views import app.views
>>>>>>> storage_get_count
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def show_status():
    """Shows the OK status"""

    return jsonify({'status': 'OK'})
<<<<<<< HEAD


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def get_stats():
    """Gets stats for models"""

    stats_dict = {
            "amenities": storage.count("Amenity"),
            "cities": storage.count("City"),
            "places": storage.count("Place"),
            "reviews": storage.count("Review"),
            "states": storage.count("State"),
            "users": storage.count("User")
            }

    return jsonify(stats_dict)
=======
>>>>>>> storage_get_count
