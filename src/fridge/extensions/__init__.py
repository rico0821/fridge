# -*- coding: utf-8 -*-
"""
    fridge.extensions
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Module for initialising fridge extensions package.
    -- Create a MainDB instance.
    -- Create PyMongo instance.
    -- Create JWTManager instance.

    :copyright: (c)2020 by rico0821

"""
from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo

from fridge.extensions.database import MainDB


jwt = JWTManager()
main_db = MainDB()
mongo_db = PyMongo()