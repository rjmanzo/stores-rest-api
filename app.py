from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_jwt import JWT
import datetime

# import the security settings for logIN
from security import authenticate, identity

# import the settings
from settings import *

# Local_settings override settings
try:
    from local_settings import *
except ImportError:
    pass

# Import others models
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = APP_KEY
api = Api(app)


@app.before_first_request
def create_table():
    db.create_all()


# JWT config
# app.config['JWT_AUTH_URL_RULE'] = AUTH_URL_PATH
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(
    seconds=EXPIRATION_TIME)

# /auth (the instance create a new endpoint)
jwt = JWT(app, authenticate, identity)

# Routes
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

# with this syntax you can run the server only with this command : python app.py
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
