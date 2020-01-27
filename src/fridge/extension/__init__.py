# -*- coding: utf-8 -*-
"""
    fridge.extension
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Module for initialising fridge extension package.
    -- Create a MainDB instance.
    -- Create PyMongo instance.
    -- Create JWTManager instance.

    :copyright: (c)2020 by rico0821

"""
from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo

from fridge.extension.database import MainDB


jwt = JWTManager()
main_db = MainDB()
mongo_db = PyMongo()