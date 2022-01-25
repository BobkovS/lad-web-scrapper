from contextlib import contextmanager

from project.core import application


@contextmanager
def ignore_errors_wrapper():
    try:
        yield
    except Exception as e:
        application.logger.error(e.__str__())
