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

from flask import Flask
from schematics.exceptions import BaseError
from werkzeug.exceptions import HTTPException

from fridge.config import Config
from fridge.logger import Log


def print_settings(config):
    """
    Print settings on console.
    :param config: configuration dictionary
    """
    print("----------------------------------------")
    print("SETTINGS")
    print("----------------------------------------")
    for key, value in config:
        print("%s=%s" % (key, value))
    print("----------------------------------------")


def register_extensions(flask_app):
    from fridge.extension import jwt, main_db, mongo_db

    jwt.init_app(flask_app)
    main_db.init_app(flask_app)
    mongo_db.init_app(flask_app)


def register_controls(flask_app):
    from fridge.controller import route

    route(flask_app)


def register_hooks(flask_app):
    from fridge.hook.error import schematics_base_error_handler, broad_exception_handler, http_exception_handler
    from fridge.hook.request_context import after_request

    flask_app.after_request(after_request)
    flask_app.register_error_handler(BaseError, schematics_base_error_handler)
    flask_app.register_error_handler(HTTPException, http_exception_handler)
    flask_app.register_error_handler(Exception, broad_exception_handler)


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

    # Registry
    register_extensions(app)
    register_controls(app)
    register_hooks(app)

    return app



