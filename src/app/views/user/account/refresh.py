# -*- coding: utf-8 -*-
"""
    app.views.user.account.refresh
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Module for access token refresh.

    :copyright: (c)2020 by rico0821

"""
from flask_jwt_extended import create_access_token, jwt_refresh_token_required

from app.context import context_property
from app.misc.logger import Log
from app.views import BaseResource


class RefreshAPI(BaseResource):
    @jwt_refresh_token_required
    def get(self):
        """ Access token refresh API. """

        user = context_property.request_user
        Log.info("Refresh access token for %i" % user.id)

        return {
            "accessToken" : create_access_token(user.id)
        }, 200