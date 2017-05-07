import logging
from logging.handlers import TimedRotatingFileHandler

from settings import LOG, DEBUG


def init():
    level_mode = logging.DEBUG if DEBUG else logging.INFO
    logging.basicConfig(level=level_mode)
    logger = logging.getLogger()
    logger_database = logging.getLogger('DATABASE')
    logger_database.setLevel(min(level_mode, logging.INFO))

    formatter = logging.Formatter(
        '%(asctime)s%(name)s:%(levelname)s:%(message)s')

    file_handler = TimedRotatingFileHandler(
        LOG + '/' + 'output.log', when='d')

    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)

    error_file_handler = TimedRotatingFileHandler(
        LOG + '/' + 'error.log', when='d')

    error_file_handler.setFormatter(formatter)
    error_file_handler.setLevel(logging.ERROR)
    logger.addHandler(error_file_handler)