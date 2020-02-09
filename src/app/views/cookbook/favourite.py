"""
    app.views.cookbook.favourite.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Module for handling recipe likes.

    :copyright: (c)2020 by rico0821

"""
from flask import abort

from app.context import context_property
from app.extensions import main_db
from app.views import BaseResource



# do not allow like if my own