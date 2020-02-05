# -*- coding: utf-8 -*-
"""
    fridge.views
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Module for initialising fridge views package.
    -- Define Base flask_restful Resource.
    -- Define route function.

    :copyright: (c)2020 by rico0821

"""
import arrow

from flask import Blueprint
from flask_restful import Api, Resource


class BaseResource(Resource):
    def __init__(self):
        self.utcnow = arrow.utcnow()
        self.iso8601_formatted_utcnow = self.utcnow.isoformat()


def route(flask_app):
    """
    Routing function for flask_restful structure.
    """
    from fridge.views.user.account import auth
    from fridge.views.user.account import signup
    from fridge.views.user.account import check_username
    from fridge.views.user.account import refresh
    from fridge.views.recipebook import recipe

    handle_exception_func = flask_app.handle_exception
    handle_user_exception_func = flask_app.handle_user_exception

    # Initialise blueprint and API objects
    api_blueprint = Blueprint("api", __name__)
    api_user_account = Api(api_blueprint, prefix='/user/account')
    api_recipebook = Api(api_blueprint, prefix='/recipebook')

    # Register routes
    api_user_account.add_resource(auth.AuthAPI, '/auth')
    api_user_account.add_resource(signup.SignupAPI, '/signup')
    api_user_account.add_resource(check_username.CheckUsernameAPI,
                                  '/check_username/username/<username>')
    api_user_account.add_resource(refresh.RefreshAPI, '/refresh')

    api_recipebook.add_resource(recipe.RecipeAPI, '/recipe')

    # Register blueprint
    flask_app.register_blueprint(api_blueprint)

    flask_app.handle_exception = handle_exception_func
    flask_app.handle_user_exception = handle_user_exception_func