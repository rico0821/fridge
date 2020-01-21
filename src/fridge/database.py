# -*- coding: utf-8 -*-
"""
    fridge.database
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Module for fridge app database.
    -- Create SQLAlchemy database engine.
    -- Create PyMongo database engine.

    :copyright: (c)2020 by rico0821

"""
from flask_pymongo import PyMongo
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from fridge.model import Base
from fridge.model import user

# Create PyMongo instance
mongo = PyMongo()

class DBManager:
    """Common class for handling SQLite DB."""

    __engine = None
    __session = None

    @staticmethod
    def init(db_url, db_log_flag=True):
        DBManager.__engine = create_engine(db_url, echo=db_log_flag)
        DBManager.__session = scoped_session(sessionmaker(autocommit=False,
                                                          autoflush=False,
                                                          bind=DBManager.__engine))
        global dao
        dao = DBManager.__session

    @staticmethod
    def init_db():
        Base.metadata.create_all(bind=DBManager.__engine)

dao = None