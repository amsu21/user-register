import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from werkzeug.middleware.proxy_fix import ProxyFix

# instantiate extensions
db = SQLAlchemy()
cors = CORS()


def create_app(script_info=None):
    """create flask application"""

    # instantiate app
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1)

    # set config
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    # setup extensions
    db.init_app(app)
    cors.init_app(app, resources={r"*": {"origins": "*"}})

    # register api
    from app.api import api
    api.init_app(app)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}
    
    return app