#!/usr/bin/python3
""" Module which creates a flask route """

from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def status():
    """ Returns a JSON status """
    
    return jsonify(status="OK")

@app_views.route('/stats', strict_slashes=False)
def num_objects():
    """ Returns count of objects by type """

    new_Dict = {}
    
    classes = {
    "Amenity": "amenities",
    "City": "cities",
    "Place": "places",
    "Review": "reviews",
    "State": "states",
    "User": "users"
}

    for key, value in classes.items():
        new_Dict[value] = models.storage.count(key)
    return jsonify(new_Dict)
