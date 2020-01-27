# -*- coding: utf-8 -*-
"""
    fridge.hook.error
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Module for defining error handlers.

    :copyright: (c)2020 by rico0821

"""
from flask import jsonify


def schematics_base_error_handler(e):
    return jsonify({
        "msg" : e.to_primitive()
    }), 400


def http_exception_handler(e):
    return jsonify({
        "msg" : e.description
    }), e.code


def broad_exception_handler(e):
    return "", 500