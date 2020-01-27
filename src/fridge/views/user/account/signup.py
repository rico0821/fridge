# -*- coding: utf-8 -*-
"""
    fridge.views.user.account.signup
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Module for handling user account creation.
    --

    :copyright: (c)2020 by rico0821

"""
from flask import abort
from schematics.types import EmailType, StringType
from werkzeug.security import generate_password_hash

from fridge.context import context_property
from fridge.decorators.validation import PayLoadLocation, BaseModel, validate_with_schematics
from fridge.extensions import main_db
from fridge.logger import Log
from fridge.models.user import TblUsers, TblCreds
from fridge.views import BaseResource


class SignupAPI(BaseResource):
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
            email = EmailType(
                serialized_name="email",
                required=True
            )

    @validate_with_schematics(PayLoadLocation.JSON, Schema.Post)
    def post(self):
        """User signup API."""
        payload = self.Schema.Post = context_property.request_payload
        session = main_db.session

        if TblCreds.already_exists(session, payload.username, payload.email):
            abort(409)
        else:
            try:
                new_user = TblUsers()
                new_creds = TblCreds(
                         username=payload.username,
                         password=generate_password_hash(payload.password),
                         email=payload.email
                     )

                session.add_all(
                    [new_user, new_creds]
                )

                new_user.creds = new_creds

                session.commit()
                Log.info("New user %s registered." % payload.username)

                return {}, 201

            except Exception as e:
                session.rollback()
                Log.error(str(e))
                abort(500)


