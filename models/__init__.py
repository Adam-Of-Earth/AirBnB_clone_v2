#!/usr/bin/python3
"""
initialize the models package
"""

from os import getenv
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.state import State


storage_t = getenv("HBNB_TYPE_STORAGE")

if storage_t == "db":
    from models.engine.db_storage import DBStorage
    CNC = db_storage.DBStorage.CNC
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    CNC = file_storage.FileStorage.CNC
    storage = FileStorage()
storage.reload()
