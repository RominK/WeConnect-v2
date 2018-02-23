from flask import Flask, jsonify, Blueprint

from flask_restful import Resource, abort, Api, reqparse

from models import User


Users = {
    1: User('user1', 'rom1', 'kay1', 'user1@wecon.com', 'pass1').__dict__,
    2: User('user2', 'rom2', 'kay2', 'user2@wecon.com', 'pass2').__dict__,
    3: User('user3', 'rom3', 'kay3', 'user3@wecon.com', 'pass3').__dict__

}


class User(Resource):
    """
    register user
    get one user
    """

    def post(self):
        # register user
        args = self.reqparse.parse_args()
        user_id = int(max(Users.keys())+1)
        Users[id] = User(**args)
        return jsonify(Users[user_id]), 201

    def put(self, user_id):
        # reset password
        args = self.reqparse.parse_args()
        if user_id in Users.keys():
            Users[user_id] = User(**args)
        return jsonify(Users[user_id]), 201


class Login(Resource):
    """
    Login user 
    Logout user
    """
    
    def post(self, user_id):
        args = self.reqparse.parse_args()
        password = args['password']
        username = args['username']
        if user_id in Users.keys():
            if Users[user_id].password == password and Users[user_id].username == username:
                Users[user_id].is_auth=True
                return {'login': 'Successful'}

        return {'login': 'Failed'}


class Logout(Resource):

    def post(self, user_id):
        Users[user_id].is_auth=False
        return {'logout': 'Successful'}


auth_api = Blueprint('resources.users', __name__)
api = Api(auth_api)


api.add_resource(User, '/register' )

api.add_resource(Login, '/login')

api.add_resource(Logout, '/logout')

api.add_resource(User, '/reset_password')
