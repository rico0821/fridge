# -*- coding: utf-8 -*-
"""
    fridge.logger
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Module for fridge app server logging.

    :copyright: (c)2020 by rico0821

"""
import logging
from logging import getLogger, handlers, Formatter


class Log:
    """Log engine class."""

    __log_level_dict = {
        'debug' : logging.DEBUG,
        'info' : logging.INFO,
        'warn' : logging.WARN,
        'error' : logging.ERROR,
        'critical' : logging.CRITICAL
    }

    _my_logger = None

    @staticmethod
    def init(logger_name="Fridge_Log",
             log_level='debug',
             log_filepath='fridge/resource/fridge.log'):
        Log.__logger = getLogger(logger_name)
        Log.__logger.setLevel(Log.__log_level_dict.get(log_level, 'warn'))

        formatter = Formatter("%(asctime)s - %(levelname)s - %(message)s")

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        Log.__logger.addHandler(console_handler)

        file_handler = handlers.TimedRotatingFileHandler(log_filepath,
                                                         when='D',
                                                         interval=1)
        file_handler.setFormatter(formatter)

        Log.__logger.addHandler(file_handler)

    @staticmethod
    def debug(msg):
        Log.__logger.debug(msg)

    @staticmethod
    def info(msg):
        Log.__logger.info(msg)

    @staticmethod
    def warn(msg):
        Log.__logger.warn(msg)

    @staticmethod
    def error(msg):
        Log.__logger.error(msg)

    @staticmethod
    def critical(msg):
        Log.__logger.critical(msg)
