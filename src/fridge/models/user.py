# -*- coding: utf-8 -*-
"""
    fridge.models.user
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Module for user database models.
    -- Create TblUsers model.
    -- Create TblCreds model.

    :copyright: (c)2020 by rico0821

"""
from sqlalchemy import Column, Boolean, DateTime, Integer, ForeignKey, String, CHAR
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import func

from fridge.models import Base


class TblUsers(Base):
    __tablename__ = "tbl_users"

    id = Column(Integer, primary_key=True)
    createdAt = Column(DateTime, server_default=func.now())
    updatedAt = Column(DateTime, server_default=func.now(), onupdate=func.now())

    firstName = Column(String(50), default=None)
    lastName = Column(String(50), default=None)
    dob = Column(DateTime, default=None)
    sex = Column(Integer, default=None)

    creds = relationship("TblCreds", uselist=False, backref="user")

    def __init__(self):
        pass


class TblCreds(Base):
    __tablename__ = "tbl_creds"

    id = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('tbl_users.id'))
    createdAt = Column(DateTime, server_default=func.now())
    updatedAt = Column(DateTime, server_default=func.now(), onupdate=func.now())

    username = Column(String(50), unique=True)
    email = Column(String(100), unique=True)
    password = Column(CHAR(93))
    verified = Column(Boolean, default=False, nullable=False)

    @classmethod
    def already_exists(cls, session, username, email=None):
        username_check = cls.first(session, cls.username == username) is not None
        email_check = cls.first(session, cls.email == email) is not None
        return username_check or email_check

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password