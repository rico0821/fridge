# -*- coding: utf-8 -*-
"""
    app.views
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Module for initialising app views package.
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
    from app.views.user.account import auth
    from app.views.user.account import signup
    from app.views.user.account import check_username
    from app.views.user.account import refresh
    from app.views.cookbook import recipe
    from app.views.cookbook import book
    from app.views.fridge import search_ingredient

    handle_exception_func = flask_app.handle_exception
    handle_user_exception_func = flask_app.handle_user_exception

    # Initialise blueprint and API objects
    api_blueprint = Blueprint("api", __name__)
    api_user_account = Api(api_blueprint, prefix='/user/account')
    api_cookbook = Api(api_blueprint, prefix='/cookbook')
    api_fridge = Api(api_blueprint, prefix='/fridge')

    # Register routes
    api_user_account.add_resource(auth.AuthAPI, '/auth')
    api_user_account.add_resource(signup.SignupAPI, '/signup')
    api_user_account.add_resource(check_username.CheckUsernameAPI,
                                  '/check_username/username/<username>')
    api_user_account.add_resource(refresh.RefreshAPI, '/refresh')

    api_cookbook.add_resource(book.BookAPI, '/')
    api_cookbook.add_resource(recipe.UploadRecipeAPI, '/recipe/upload')
    api_cookbook.add_resource(recipe.RecipeAPI, '/recipe/<recipe_id>')
    api_cookbook.add_resource(book.BookSearchAPI, '/search/<recipe_name>')

    # Register blueprint
    flask_app.register_blueprint(api_blueprint)

    flask_app.handle_exception = handle_exception_func
    flask_app.handle_user_exception = handle_user_exception_func