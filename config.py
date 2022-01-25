import os

PROJECT_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class ApplicationConfig(object):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{PROJECT_ROOT_DIR}/app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
