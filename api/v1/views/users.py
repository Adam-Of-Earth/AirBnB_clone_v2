#!/usr/bin/python3
""" Module to create a flask route """

from api.v1.views import app_views
from flask import Flask, jsonify, request
import models


@app_views.route('/users', strict_slashes=False, methods=['GET'])
def all_users():
    """ Retrieves lists """
    users_list = []
    for use in models.storage.all('User').values():
        users_list.append(use.to_dict())
    return jsonify(users_list)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def a_user(user_id):
    """ Gets  object """
    1_user = storage.get('User', user_id)
    if 1_user is None:
        abort(404)
    return jsonify(1_user.to_dict())


@app_views.route('/users/<user_id>', strict_slashes=False, methods=['DELETE'])
def rm_user(user_id):
    """ Function deletes """

    nm_user = models.storage.get('User', user_id)
    if nm_user is None:
        abort(404)
    nm_user.delete()
    models.storage.save()
    return (jsonify({}))


@app_views.route('/users/', methods=['POST'], strict_slashes=False)
def new_user():
    """ Creates a new user """

    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if 'email' not in request.get_json():
        return make_response(jsonify({'error': 'Missing email'}), 400)
    if 'password' not in request.get_json():
        return make_response(jsonify({"error": 'Missing password'}), 400)

    create_user = User(**request.get_json())
    create_user.save()
    return make_response(jsonify(create_user.to_dict()), 201)


@app_views.route('/users/<user_id>', strict_slashes=False, methods=['PUT'])
def update_user(user_id):
    """ Updates user """

    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)

    u_updater = models.storage.get("User", user_id)
    if u_updater is None:
        abort(404)

    for v, k in request.get_json().items():
        if k not in ['id', 'created_at', 'updated_at', 'email']:
            setattr(u_updater, k, v)

    u_updater.save()
    retval = jsonify(u_updater.to_dict())
    return retval
