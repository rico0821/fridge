# -*- coding: utf-8 -*-
"""
    fridge.views.recipebook.recipe
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Module for handling recipe.
    --

    :copyright: (c)2020 by rico0821

"""
from datetime import datetime

from flask import abort, request
from flask_jwt_extended import jwt_required
from schematics.types import DictType, IntType, ListType, StringType

from fridge.context import context_property
from fridge.decorators.validation import PayLoadLocation, BaseModel, validate_with_schematics
from fridge.extensions import mongo_db
from fridge.misc.imaging import make_filename, save_image
from fridge.misc.logger import Log
from fridge.views import BaseResource


class RecipeAPI(BaseResource):
    class Schema:
        class Post(BaseModel):
            recipe_name = StringType(
                serialized_name="recipe_name",
                required=True
            )
            description = StringType(
                serialized_name="description"
            )
            ingredients = ListType(DictType(IntType))
            steps = ListType(StringType)
            cover_filename_orig = StringType(
                serialized_name="cover_filename_orig",
            )

    @validate_with_schematics(PayLoadLocation.JSON, Schema.Post)
    @jwt_required
    def post(self):
        """ Recipe upload API. """

        payload = self.Schema.Post = context_property.request_payload
        mongo = mongo_db.db
        user = context_property.request_user
        # cover_img = request.files["cover_img"]
        # step_imgs = request.files.getlist("step_img")

        existing_recipe = mongo.recipe.find_one({
            "userId": user.id,
            "recipeName": payload.recipe_name
        })

        if existing_recipe:
            abort(409)
        else:
            cover_filename = "something"
            step_filename_list = ["a", "b", "c"]
            """
            cover_filename = make_filename(cover_img, user)
            save_image(cover_img, cover_filename, "cover")

            step_filename_list: list
            for img in step_imgs:
                step_filename = make_filename(img, user)
                save_image(img, step_filename, "step")
                step_filename_list.append(step_filename)
            """
            try:
                mongo.recipe.insert(
                    {
                        "userId": user.id,
                        "updatedAt": datetime.utcnow(),
                        "recipeName": payload.recipe_name,
                        "description": payload.description,
                        "ingredients": payload.ingredients,
                        "steps": payload.steps,
                        "coverFilenameOrig": payload.cover_filename_orig,
                        "coverFilename": cover_filename,
                        "stepFilename": step_filename_list
                    }
                )
                Log.info("New recipe %s added by %s." % (payload.recipe_name, user.id))

                return {}, 200

            except Exception as e:
                Log.error(str(e))
                abort(500)


"""
    @jwt_required
    def get(self, recipe_id):
         Recipe information API. 

        mongo = mongo_db.db

        try:
            recipe = mongo.recipe.find_one_or_404({
                "_id": recipe_id
            })

            return {"data": recipe}

        except Exception as e:
            Log.error(str(e))
            abort(500)
"""
