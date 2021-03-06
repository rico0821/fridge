# -*- coding: utf-8 -*-
"""
    app.extensions.database
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Module for app database.
    -- Create SQLAlchemy database engine.
    -- Create PyMongo database engine.

    :copyright: (c)2020 by rico0821

"""
import os

from abc import abstractmethod
from flask import g, has_request_context
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from app.models import _Base
from app.models import user


class DBManager:
    """Common class for handling SQLite DB."""

    @abstractmethod
    def create_engine_kwargs(self, app):
        pass

    @property
    @abstractmethod
    def g_attribute_name(self):
        pass

    @property
    def session(self):
        """
        Get session from g.
        If there is no session, create new session.
        :return: session
        """
        session = getattr(g, self.g_attribute_name, None)

        if session is None and has_request_context():
            session = self.new_session()
            setattr(g, self.g_attribute_name, session)

        return session

    @session.setter
    def session(self, value):
        """Save session to g."""
        setattr(g, self.g_attribute_name, value)

    def __init__(self, flask_app=None):
        self.engine = None
        self.new_session = None

        if flask_app is not None:
            self.init_app(flask_app)

    def init_app(self, flask_app):
        from app.models import Base
        from app.models import user

        self.engine = create_engine(**self.create_engine_kwargs(flask_app))
        self.new_session = scoped_session(sessionmaker(autocommit=False,
                                                       autoflush=False,
                                                       bind=self.engine))

        Base.metadata.create_all(bind=self.engine)

        @flask_app.teardown_appcontext
        def remove_session(_):
            if self.session is not None:
                self.session.close()


class MainDB(DBManager):
    def create_engine_kwargs(self, app):
        db_filepath = os.path.join(app.root_path,
                                   app.config['DB_FILE_PATH'],
                                   app.config['MAIN_DB_NAME'])
        db_url = app.config['DB_URL'] + db_filepath
        return {
            "name_or_url": db_url,
            "echo": app.config['DB_LOG_FLAG']
        }

    @property
    def g_attribute_name(self):
        return "main_db_session"
