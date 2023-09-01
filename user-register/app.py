# REQUIRED IMPORTS
from flask import Flask
from flask_restful import Api
from flask_restx import Api
from resources.users import UserRegister, Users, User
from db import db

app = Flask(__name__)

# DB URL
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./bug-tracker.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['BUNDLE_ERRORS'] = True #global setting for all the reqparsers in the app
api = Api(app)

# CRUD PATHS
api.add_resource(UserRegister, '/register')
api.add_resource(Users,'/users')
api.add_resource(User, '/users/<int:user_id>')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port = 8080, debug = True)