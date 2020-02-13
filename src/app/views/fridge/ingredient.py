# -*- coding: utf-8 -*-
"""
    app.views.search.ingredient
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Module for searching ingredient.

    :copyright: (c)2020 by rico0821

"""
from flask_jwt_extended import jwt_required

from app.extensions import mongo_db
from app.views import BaseResource


class SearchIngredientAPI(BaseResource):

    @jwt_required
    def get(self, ingredient_name):
        """ Ingredient search API. """

        mongo = mongo_db.db

        result = mongo.ingredient.find({
            "ingredientName": {"$regex": ingredient_name}
        }).limit(5).toArray()

        return {
            "data": {
                result
            }
        }, 200