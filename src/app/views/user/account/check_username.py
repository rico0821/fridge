# -*- coding: utf-8 -*-
"""
    app.views.user.account.check_username
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Module for checking duplicate username.

    :copyright: (c)2020 by rico0821

"""
from flask import abort

from app.extensions import main_db
from app.models.user import TblCreds
from app.views import BaseResource


class CheckUsernameAPI(BaseResource):
    def get(self, username):
        """ Username check API. """

        session = main_db.session

        if TblCreds.already_exists(session, username):
            abort(409)
        else:
            return {}, 200

