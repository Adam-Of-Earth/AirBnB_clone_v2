#!/usr/bin/python3
"""init file to set up flask"""
from flask import Blueprint



app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

<<<<<<< HEAD

=======
<<<<<<< HEAD
from api.v1.views.states import *
>>>>>>> parent of 4c3d1eb... update
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
=======
from api.v1.views.index import *


>>>>>>> 4ef47d88179195c5e0758e9b91ea001fbd458b59
