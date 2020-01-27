# -*- coding: utf-8 -*-
"""
    fridge.context
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Module for creating a app context property.
    -- Define _ContextProperty class.
    -- Create _ContextProperty instance.

    :copyright: (c)2020 by rico0821

"""
from flask import g
from flask_jwt_extended import get_jwt_identity

from fridge.extension import main_db
from fridge.model.user import TblUsers


class _ContextProperty:
    @property
    def request_payload(self):
        return g.request_payload

    @request_payload.setter
    def request_payload(self, value):
        g.request_payload = value

    @property
    def request_user(self):
        request_user = getattr(g, "request_user", None)

        if request_user:
            return request_user
        else:
            session = main_db.session

            user = TblUsers.first(
                session,
                TblUsers.id == get_jwt_identity(),
                code=401
            )
            g.request_user = user

            return user


context_property = _ContextProperty()