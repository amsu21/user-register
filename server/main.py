# REQUIRED IMPORTS 
from flask import Flask
from flask_restx import Api, Namespace, Resource
from flask_cors import CORS
from structlog import get_logger
from werkzeug.middleware.proxy_fix import ProxyFix

# INITILIAZE THE APP 
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1)