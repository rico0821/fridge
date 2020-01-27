# -*- coding: utf-8 -*-
"""
    fridge.decorator.validation
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Module for defining validation decorator.
    -- Define schematics validation decorator.

    :copyright: (c)2020 by rico0821

"""
from abc import abstractmethod
from enum import Enum
from functools import wraps

from flask import request
from schematics import Model

from fridge.context import context_property


class PayLoadLocation(Enum):
    ARGS = "args"
    JSON = "json"


class BaseModel(Model):
    @abstractmethod
    def validate_additional(self):
        pass


def validate_with_schematics(validation_target, model):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            instance = model(getattr(request, validation_target.value))
            instance.validate()
            getattr(instance, "validate_additional", lambda: ...)()

            context_property.request_payload = instance

            return f(*args, **kwargs)
        return wrapper
    return decorator