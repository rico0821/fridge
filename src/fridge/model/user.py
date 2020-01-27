# -*- coding: utf-8 -*-
"""
    fridge.model.user
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Module for user database models.
    -- Create TblUsers model.

    :copyright: (c)2020 by rico0821

"""
from sqlalchemy import Column, Boolean, DateTime, Integer, ForeignKey, String, CHAR
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import func

from fridge.model import Base


class TblUsers(Base):
    __tablename__ = "tbl_users"

    id = Column(Integer, primary_key=True)
    createdAt = Column(DateTime, server_default=func.now())
    updatedAt = Column(DateTime, onupdate=func.now())

    firstName = Column(String(50), nullable=False)
    lastName = Column(String(50), nullable=False)
    dob = Column(DateTime)
    sex = Column(Integer)

    creds = relationship("TblCreds", uselist=False, backref="user")

    inventory = Column(Integer, nullable=False)


class TblCreds(Base):
    __tablename__ = "tbl_creds"

    id = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('tbl_users.id'))
    createdAt = Column(DateTime, server_default=func.now())
    updatedAt = Column(DateTime, onupdate=func.now())

    username = Column(String(50), unique=True)
    email = Column(String(100), unique=True)
    password = Column(CHAR(93))
    verified = Column(Boolean, default=False, nullable=False)




