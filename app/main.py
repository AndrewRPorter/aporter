from flask import Flask

from .views.main_view import main_bp

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("app.config")
    app.register_blueprint(main_bp)
    app.app_context().push()  # this is needed for application global context
    return app

application = create_app()