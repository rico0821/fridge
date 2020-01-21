# -*- coding: utf-8 -*-
"""
    fridge.blueprint
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Module for fridge Flask blueprint.

    :copyright: (c)2020 by rico0821

"""
from flask import Blueprint

from fridge.logger import Log


fridge = Blueprint("fridge", __name__)