import logging

from flask.logging import default_handler


class DefaultLoggingHandler:
    def __init__(self):
        self._logging_formatter = None
        self._logging_handler = None

    def _initialize_logging_formatter(self):
        self._logging_formatter = logging.Formatter(
            '[%(levelname)s][%(asctime)s] in %(module)s/%(funcName)s: %(message)s')

    def _initialize_logging_handler(self):
        self._logging_handler = default_handler

    def get_logging_handler(self):
        self._initialize_logging_handler()
        self._initialize_logging_formatter()
        self._logging_handler.setFormatter(self._logging_formatter)
        return self._logging_handler
