#!/usr/bin/python3
""" Module for status of API """

import os
from flask import Flask, make_response, jsonify
from models import storage
from flask_cors import CORS
from api.v1.views import app_views
import models


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, origins='0.0.0.0')


@app.teardown_appcontext
def teardown(self):
    """ This closes storage """
    models.storage.close()


@app.errorhandler(404)
def not_found(error):
    """ Return a 404 error message """
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST") or '0.0.0.0'
    port = os.getenv("HBNB_API_PORT") or '5000'
    app.run(host=host, port=port, threaded=True)
