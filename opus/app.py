from typing import Iterable, Callable

from flask import Flask, Blueprint

from lib.jinja import join_attribute
from opus.blueprints.page import page

ACTIVE_BLUEPRINTS = [page]

ACTIVE_EXTENSIONS = []

CUSTOM_FILTERS = [join_attribute]


def create_app(settings_override: dict = None):
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
    register_custom_filters(app)
    initialize_extensions(app)

    return app


def register_blueprints(
        app: Flask,
        blueprints: Iterable[Blueprint] = ACTIVE_BLUEPRINTS) -> None:
    """
    Register all of the specified blueprints with the app

    :param app: Flask app
    :param blueprints: The blueprints to register
    :return: None
    """
    for bp in blueprints:
        app.register_blueprint(bp)


def register_custom_filters(
        app: Flask,
        filters: Iterable[Callable] = CUSTOM_FILTERS) -> None:
    """
    Register all of the specified custom filters with the Jinja environment

    :param app: Flask app
    :param filters: sequence of pairs filters
    :return:
    """
    for f in filters:
        app.jinja_env.filters[f.__name__] = f


def initialize_extensions(app: Flask,
                          extensions: Iterable = ACTIVE_EXTENSIONS) -> None:
    """
    Initialize the specified flask extensions

    :param app: Flask app
    :param extensions: the extensions to register
    :return: None
    """
    for extension in extensions:
        extension.init_app(app)
