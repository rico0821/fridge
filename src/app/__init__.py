# -*- coding: utf-8 -*-
"""
    app
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Module for initialising app package.
    -- Create a Flask application for app.

    :copyright: (c)2020 by rico0821

"""
import os

from flask import Flask
from schematics.exceptions import BaseError
from werkzeug.exceptions import HTTPException

from app.config import Config
from app.misc.logger import Log


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
    from app.extensions import jwt, main_db, mongo_db

    jwt.init_app(flask_app)
    main_db.init_app(flask_app)
    mongo_db.init_app(flask_app)


def register_controls(flask_app):
    from app.views import route

    route(flask_app)


def register_hooks(flask_app):
    from app.hooks.error import schematics_base_error_handler, broad_exception_handler, http_exception_handler
    from app.hooks.request_context import after_request

    flask_app.after_request(after_request)
    flask_app.register_error_handler(BaseError, schematics_base_error_handler)
    flask_app.register_error_handler(HTTPException, http_exception_handler)
    flask_app.register_error_handler(Exception, broad_exception_handler)


def create_app(config_filepath='resource/config.cfg'):
    """
    Create Flask application.
    :param config_filepath: configuration filepath
    :return: app
    """
    flask_app = Flask(__name__)

    # Config
    flask_app.config.from_object(Config)
    flask_app.config.from_pyfile(config_filepath, silent=True)
    print_settings(flask_app.config.items())

    # Initialise Log
    log_filepath = os.path.join(flask_app.root_path,
                                flask_app.config['LOG_FILE_PATH'])
    Log.init(log_filepath=log_filepath)

    # Registry
    register_extensions(flask_app)
    register_controls(flask_app)
    register_hooks(flask_app)

    return flask_app



