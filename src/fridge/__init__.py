# -*- coding: utf-8 -*-
"""
    fridge
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Module for initialising fridge package.
    -- Create a Flask application for fridge.
    -- Initilaise config, blueprint, session, DB.

    :copyright: (c)2020 by rico0821

"""
import os
from datetime import datetime

from flask import Flask, render_template, url_for

from fridge.config import Config
from fridge.logger import Log
from fridge.database import DBManager, dao, mongo
from fridge.blueprint import fridge
from fridge.cache_session import SimpleCacheSessionInterface


def print_settings(config):
    """
    Print settings on console.
    :param config: configuration dictionary
    :return: none
    """
    print("----------------------------------------")
    print("SETTINGS")
    print("----------------------------------------")
    for key, value in config:
        print("%s=%s" % (key, value))
    print("----------------------------------------")

def create_app(config_filepath='resource/config.cfg'):
    """
    Create Flask application for fridge.
    :param config_filepath: configuration filepath
    :return: fridge app
    """
    app = Flask(__name__)

    # Config
    app.config.from_object(Config)
    app.config.from_pyfile(config_filepath, silent=True)
    print_settings(app.config.items())

    # Initialise Log
    log_filepath = os.path.join(app.root_path,
                                app.config['LOG_FILE_PATH'])
    Log.init(log_filepath=log_filepath)

    # Load SQLAlchemy DB
    db_filepath = os.path.join(app.root_path,
                               app.config['DB_FILE_PATH'])
    db_url = app.config['DB_URL'] + db_filepath
    DBManager.init(db_url, app.config['DB_LOG_FLAG'])
    DBManager.init_db()

    # Load MongoDB
    mongo.init_app(app)

    # Register blueprint
    app.register_blueprint(fridge)

    # Register SessionInterface
    app.session_interface = SimpleCacheSessionInterface()

    return app



