# -*- coding: utf-8 -*-
"""
    app.config
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Configuration for app.

    :copyright: (c)2020 by rico0821

"""
import datetime
import os


class Config:
    """Configuration object."""

    # Security
    SECRET_KEY = os.getenv('SECRET_KEY', '85c145a16bd6f6e1f3e104ca78c6a102')

    # SQLite DB
    DB_URL = 'sqlite:///'
    DB_FILE_PATH = 'resource/database/'
    TMP_FOLDER = 'resource/tmp/'
    DB_LOG_FLAG = False

    MAIN_DB_NAME = "main_db"

    # MongoDB
    MONGO_URI = 'mongodb://localhost:27017/app'

    # Upload
    UPLOAD_FOLDER = 'resource/recipe/'

    # Token
    TOKEN_EXPIRES = datetime.timedelta(days=365)

    # Log
    LOG_LEVEL = 'debug'
    LOG_FILE_PATH = 'resource/log/app.log'

