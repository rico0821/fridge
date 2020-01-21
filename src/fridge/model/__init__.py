# -*- coding: utf-8 -*-
"""
    fridge.model
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Module for initialising fridge model package.
    -- Create declarative base for SQLAlchemy.

    :copyright: (c)2020 by rico0821

"""
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

__all__ = ['user']