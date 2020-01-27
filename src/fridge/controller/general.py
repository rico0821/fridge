# -*- coding: utf-8 -*-
"""
    fridge.controller.general
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Module for general controller functions.
    -- Close db session at request teardown.
    -- Disable page cache.
    -- Define commonly used methods.

    :copyright: (c)2020 by rico0821

"""
from functools import wraps

from flask import current_app, redirect, request, session, url_for

from fridge.blueprint import fridge
from fridge.extension.database import dao
from fridge.logger import Log
from fridge.model.user import User


@fridge.after_request
def add_header(r):
    """Disable page caching to avoid back-button problems."""
    r.headers.add('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')
    return r

@fridge.teardown_request
def close_db_session(exception=None):
    """Close DB Session after each request."""
    try:
        dao.remove()
    except Exception as e:
        Log.error(str(e))

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        """Check whether user is logged in."""
        try:
            session_key = request.cookies.get(
                current_app.config['SESSION_COOKIE_NAME'])
            is_login = False
            if session.sid == session_key and session.__contains__('user_info'):
                is_login = True

            if not is_login:
                return redirect(url_for('web_frame.login', next=request.url))

            return f(*args, **kwargs)

        except Exception as e:
            Log.error('Web error: %s' % str(e))
            raise e

    return decorated_function


def get_user(username):
    """Retrieve user from DB based on username."""
    try:
        current_user = User.query.filter_by(username=username).first()
        Log.debug(current_user)
        return current_user

    except Exception as e:
        Log.error(str(e))
        raise e