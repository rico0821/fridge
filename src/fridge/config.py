# -*- coding: utf-8 -*-
"""
    fridge.config
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Configuration for fridge app.

    :copyright: (c)2020 by rico0821

"""
import os
from datetime import datetime


basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Configuration object."""

    # SQLAlchemy
    DB_URL = 'sqlite:///'
    DB_FILE_PATH = 'resource/database/fridge'
    TMP_FOLDER = 'resource/tmp/'

    # MongoDB
    MONGO_URI = 'mongodb://localhost:27017/fridge'

    # Session
    PERMANENT_SESSION_LIFETIME = 60 * 60
    SESSION_COOKIE_NAME = "fridge_session"

    # Log
    LOG_LEVEL = 'debug'
    LOG_FILE_PATH = 'resource/log/fridge.log'
    DB_LOG_FLAG = False

