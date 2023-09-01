# REQUIRED IMPORTS 
from flask import Flask
from flask_restx import Api, Namespace, Resource
from flask_cors import CORS
from structlog import get_logger