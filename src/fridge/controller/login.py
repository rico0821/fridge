# -*- coding: utf-8 -*-
"""
    fridge.controller.login
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Module for login controller functions.
    --

    :copyright: (c)2020 by rico0821

"""
from flask import redirect, request, session, url_for
from werkzeug import check_password_hash
from wtforms import Form, TextField, PasswordField, HiddenField, validators

from fridge.blueprint import fridge
from fridge.database import dao
from fridge.logger import Log
from fridge.model.user import User
from fridge.controller.general import login_required, get_user

@fridge.route('/user/login', methods=['POST'])
def login():
    """Login controller function."""
    form = LoginForm(request.form)