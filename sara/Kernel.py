import os
import logging
import logging.config

from dynaconf import FlaskDynaconf
from flask import Flask
from flask_migrate import Migrate

import sara.Console
import sara.Entity


class Kernel():
    def __init__(self, app=None):
        if app:
            self.app = app
        else:
            self.app = Flask(__name__)
        self.configure()
        self.load_extensions()
        self.load_blueprints()
        self.load_socketio()
        self.load_celery()
        self.load_console()
        self.finalize()

    def configure(self):
        """
        Configure app settings
        """
        FlaskDynaconf(self.app)
        # we should load initial logging at this point
        if 'LOG_SETTINGS_FILE' in self.app.config and os.path.exists(self.app.config.LOG_SETTINGS_FILE):
            logging.config.fileConfig(self.app.config.LOG_SETTINGS_FILE)

    def load_extensions(self):
        """
        Initialize Flask Extensions
        """
        sara.Entity.db.init_app(self.app)
        if self.app.config.ENV != 'testing':
            Migrate(self.app, sara.Entity.db)
        else:
            with self.app.app_context():
                sara.Entity.db.create_all()
                # @TODO load all the settings from the database

    def load_blueprints(self):
        pass

    def load_socketio(self):
        pass

    def load_celery(self):
        pass

    def load_console(self):
        """
        Load console commands
        """
        for cmd in sara.Console.commands:
            self.app.cli.add_command(cmd)

    def finalize(self):
        """
        Post initializations
        """
        pass
