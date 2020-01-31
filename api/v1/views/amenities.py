#!/usr/bin/python3
"""Flask route that returns json"""

from api.v1.views import app_views
from flask import abort, jsonify, request
import models

@app_views.route('/amenities/', strict_slashes=False, methods=['GET', 'POST'])
def amenities(amenity_id=None):
    """amenities route with no ID"""
    if request.method == 'GET':
        all_amenities = storage.all('Amenity')
        all_amenities = [obj.to_json() for obj in all_amenities.values()]
        return jsonify(all_amenities)

    if request.method == 'POST':
        req_json = request.get_json()
        if req_json is None:
            abort(400, 'Not a JSON')
        if req_json.get('name') is None:
            abort(400, 'Missing name')
        Amenity = CNC.get('Amenity')
        new_object = Amenity(**req_json)
        new_object.save()
        return jsonify(new_object.to_json()), 201
