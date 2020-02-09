# -*- coding: utf-8 -*-
"""
    app.models
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Module for initialising app models package.
    -- Create declarative base for SQLAlchemy.
    -- Define Base model class.

    :copyright: (c)2020 by rico0821

"""
from flask import abort
from sqlalchemy.ext.declarative import declarative_base


_Base = declarative_base()


class Base(_Base):
    """ Abstract base class for main DB models using SQLAlchemy. """
    __abstract__ = True

    @classmethod
    def _build_query(cls, session, where=None, order_by=None):
        query = session.query(cls)

        if where is not None:
            query = query.filter(where)

        if order_by is not None:
            query = query.order_by(order_by)

        return query

    @classmethod
    def get_all(cls, session, where=None, order_by=None):
        """
        Perform query.all() based on parameters.
        :param session: SQLAlchemy session(scoped)
        :param where: where clause
        :param order_by: order_by clause
        :return: query result
        """
        query = cls._build_query(session, where, order_by)

        return query.all()

    @classmethod
    def first(cls, session, where=True, order_by=None):
        """
        Return .first() regardless of None.
        :param session: SQLAlchemy session(scoped)
        :param where: where clause
        :param order_by: order_by clause
        :return: query result
        """
        query = cls._build_query(session, where, order_by)

        return query.first()

    @classmethod
    def first_or_abort(
            cls, session, where=True, order_by=None, code=404, msg=None
    ):
        """
        Return .first() or abort according to parameters if None.
        :param session: SQLAlchemy session(scoped)
        :param where: where clause
        :param order_by: order_by clause
        :param code: abort code if query result is None
        :param msg: abort message if query result in None
        :return: query result or abort
        """
        result = cls.first(session, where, order_by)

        if result is None:
            abort(code, msg)
        else:
            return result

    @classmethod
    def delete(cls, session, where=True):
        """
        Delete all results based on query.
        :param session: SQLAlchemy session(scoped)
        :param where: where clause
        """
        session.query(cls).filter(where).delete()