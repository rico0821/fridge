# -*- coding: utf-8 -*-
"""
    fridge.controller.user.account.auth
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Module for handling user account authentication.
    --

    :copyright: (c)2020 by rico0821

"""
from flask import abort
from flask_jwt_extended import create_access_token, create_refresh_token
from schematics.types import StringType
from werkzeug.security import check_password_hash

from fridge.context import context_property
from fridge.controller import BaseResource
from fridge.decorator.validation import PayLoadLocation, BaseModel, validate_with_schematics
from fridge.extension import main_db
from fridge.model.user import TblCreds


class AuthAPI(BaseResource):
    class Schema:
        class Post(BaseModel):
            username = StringType(
                serialized_name="username",
                required=True
            )

            password = StringType(
                serialized_name="password",
                required=True,
                min_length=8
            )

    @validate_with_schematics(PayLoadLocation.JSON, Schema.Post)
    def post(self):
        """Login authentication API."""

        payload = context_property.request_payload
        session = main_db.session

        creds = TblCreds.first(session, TblCreds.username == payload.username)

        if creds is None or not check_password_hash(creds.password, payload.password):
            abort(401)
        else:
            return {
                "accessToken" : create_access_token(creds.userId),
                "refreshToken" : create_refresh_token(creds.userId)
            }, 201