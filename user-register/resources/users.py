# REQUIRED IMPORTS
from flask_restful import Resource, reqparse
from flask import  jsonify
from models.users import UserModel
import json

# REQ PARSER
_user_parser = reqparse.RequestParser()
_user_parser.add_argument('email', type=str, required=True, help="This fiield cannot be blank")
_user_parser.add_argument('password', type=str, required=True, help="This fiield cannot be blank")
_user_parser.add_argument('conf_email', type=str, required=True, help="This fiield cannot be blank")
_user_parser.add_argument('conf_passwd', type=str, required=True, help="This fiield cannot be blank")

# CREDENTIAL LOGIC
class UserRegister(Resource):
    def post(self):
        data = _user_parser.parse_args()
        if UserModel.find_by_email(data['email']):
            return { 'message' : 'A user already has this email' }, 400
        if not UserModel.password_conf(data['conf_passwd'], data['password']):
            return { 'message' : 'Password and Conformed Password must match', 'p':data['password'], 'confp':data['conf_passwd']}, 400
        if not UserModel.email_conf(data['conf_email'], data['email']):
            return { 'message' : 'Email and Confirmed Email must match' }, 400
        
        user = UserModel(data['email'], data['password'])
        user.db_save()
        return { 'message' : 'User created successfully' }, 201
    
class User(Resource):
    @classmethod
    def get(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return { 'message' : 'User not found' }, 404
        return user.json()
    @classmethod
    def delete(cls,user_id):
        user=UserModel.find_by_id(user_id)
        if not user:
            return{ 'message':'User not found' },400
        user.delete_from_db()
        return { 'message':'User deleted successfully' },201
    
    
class Users(Resource): 
    def get(self): 
        return jsonify([user.json() for user in UserModel.get_all()])