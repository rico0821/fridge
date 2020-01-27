# -*- coding: utf-8 -*-
"""
    fridge.views.user.account.refresh
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Module for access token refresh.

    :copyright: (c)2020 by rico0821

"""
from flask_jwt_extended import jwt_refresh_token_required, create_access_token

from fridge.context import context_property
from fridge.logger import Log
from fridge.views import BaseResource


class RefreshAPI(BaseResource):
    @jwt_refresh_token_required
    def get(self):
        """Access token refresh API."""

        user = context_property.request_user
        Log.info("Refresh access token for %i" % user.id)

        return {
            "accessToken" : create_access_token(user.id)
        }, 200