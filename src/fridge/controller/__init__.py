# -*- coding: utf-8 -*-
"""
    fridge.controller
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Module for initialising fridge controller package.
    -- Define Base flask_restful Resource.
    -- Define route function.

    :copyright: (c)2020 by rico0821

"""
import arrow

from flask import Blueprint, Flask
from flask_restful import Api, Resource


class BaseResource(Resource):
    def __init__(self):
        self.utcnow = arrow.utcnow()
        self.iso8601_formatted_utcnow = self.utcnow.isoformat()


def route(flask_app):
    """
    Routing function for flask_restful structure.
    """
    from fridge.controller.user.account import auth

    handle_exception_func = flask_app.handle_exception
    handle_user_exception_func = flask_app.handle_user_exception

    # Initialise blueprint and API objects
    api_blueprint = Blueprint("api", __name__)
    api_user_account = Api(api_blueprint, prefix='/user/account')

    # Register routes
    api_user_account.add_resource(auth.AuthAPI, '/auth')

    # Register blueprint
    flask_app.register_blueprint(api_blueprint)

    flask_app.handle_exception = handle_exception_func
    flask_app.handle_user_exception = handle_user_exception_func