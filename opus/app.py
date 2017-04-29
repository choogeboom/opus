from typing import Iterable

from flask import Flask, Blueprint


ACTIVE_BLUEPRINTS = []

ACTIVE_EXTENSIONS = []


def create_app(settings_override: dict=None):
    """
    Create a flask application
    
    :param settings_override: any settings to override 
    :return: None
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)
    if settings_override:
        app.config.update(settings_override)

    register_blueprints(app)
    initialize_extensions(app)


def register_blueprints(app: Flask, blueprints: Iterable[Blueprint]=ACTIVE_BLUEPRINTS) -> None:
    """
    Register all of the specified blueprints with the app
    
    :param app: Flask app 
    :param blueprints: The blueprints to register
    :return: None
    """
    for bp in blueprints:
        app.register_blueprint(bp)


def initialize_extensions(app: Flask, extensions: Iterable=ACTIVE_EXTENSIONS) -> None:
    """
    Initialize the specified flask extensions
    
    :param app: Flask app
    :param extensions: the extensions to register
    :return: None
    """
    for extension in extensions:
        extension.init_app(app)
