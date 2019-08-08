from flask import Flask, redirect

from .views.api_view import api_bp
from .views.main_view import main_bp


def page_not_found(e):
    """Custom error handling for 404"""
    return redirect("/")


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("app.config")
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp)
    app.app_context().push()  # this is needed for application global context
    app.register_error_handler(404, page_not_found)
    return app


application = create_app()
