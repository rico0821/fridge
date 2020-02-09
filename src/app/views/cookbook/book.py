"""
    app.views.cookbook.book
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Module for showing recipebook.

    :copyright: (c)2020 by rico0821

"""
from flask_jwt_extended import jwt_required

from app.context import context_property
from app.extensions import mongo_db
from app.views import BaseResource


class BookAPI(BaseResource):

    @jwt_required
    def get(self):
        """ Recipe book API. """

        mongo = mongo_db.db
        user = context_property.request_user

        my_recipe = mongo.recipe.find({
            "userId": user.id,
        }).toArray()

        favourites = mongo.recipe.find({
            "likes": user.id
        }).toArray()

        return {
            "data": {
                "my_recipe": my_recipe,
                "favourites": favourites
            }

        }, 200

class BookSearchAPI(BaseResource):

    @jwt_required
    def get(self, recipe_name):
        """ My recipe search API. """

        mongo = mongo_db.db
        user = context_property.request_user

        result = mongo.recipe.find({
            "userId": user.id,
            "recipeName": {"$regex": recipe_name}
        }).limit(5).toArray()

        return {
            "data": {
                result
            }
        }, 200