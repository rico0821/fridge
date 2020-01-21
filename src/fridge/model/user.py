# -*- coding: utf-8 -*-
"""
    fridge.model
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Module for initialising fridge model package.
    -- Create declarative base for SQLAlchemy.

    :copyright: (c)2020 by rico0821

"""
from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, Float, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import func

from fridge.model import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    createdAt = Column(DateTime, server_default=func.now())
    updatedAt = Column(DateTime, onupdate=func.now())

    firstName = Column(String(50), nullable=False)
    lastName = Column(String(50), nullable=False)
    dob = Column(DateTime)
    sex = Column(Integer)

    inventory = Column(Integer, nullable=False)


