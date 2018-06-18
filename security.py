from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    # if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
    if user and user.password:
        return user


def identity(payload):
    user_id = payload['identity']
    # this method get data or return None
    return UserModel.find_by_id(user_id)
