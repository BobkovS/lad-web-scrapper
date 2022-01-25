from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import config
from project.utils.logging.DefaultLoggingHandler import DefaultLoggingHandler

application = Flask(__name__)
application.config.from_object(config.ApplicationConfig)

default_logging_handler = DefaultLoggingHandler()
application.logger.addHandler(default_logging_handler.get_logging_handler())

application_db = SQLAlchemy(application)

from project.core import dbLayer
from project.core.webScraper import WebScraper

application_db.create_all(app=application)

web_scraper = WebScraper()
web_scraper.run_scraper()
