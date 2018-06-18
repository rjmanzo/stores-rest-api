from flask_restful import Resource, reqparse

# import models
from models.user import UserModel


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True,
                        help='this field cannot be left blank!')
    parser.add_argument('password', type=str, required=True,
                        help='this field cannot be left blank!')

    def post(self):
        # check incomming data for valid register
        data = UserRegister.parser.parse_args()

        # check if username already exist
        if UserModel.find_by_username(data['username']):
            return {"message": "This username already exist"}, 400

        # save new user to db
        user = UserModel(data['username'], data['password'])
        user.save_to_db()

        return {"message": "Your New user was created!"}, 201
