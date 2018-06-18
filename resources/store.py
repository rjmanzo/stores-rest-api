from flask_restful import Resource, Api, reqparse
from flask_jwt import jwt_required

from models.store import StoreModel


class Store(Resource):
    # we define the request argument at top. POST & PUT need the same data
    # parser = reqparse.RequestParser()
    # parser.add_argument('name', type=str, required=True,
    #                     help='this field cannot be left blank!')

    @jwt_required()
    def get(self, name):

        store = StoreModel.find_by_name(name)

        if store:
            return store.json(), 200

        return {'message': 'the Store was not found!'}, 400

    @jwt_required()
    def post(self, name):

        if StoreModel.find_by_name(name) is not None:
            return {'message': "An Store with name '{}' already exist".format(name)}, 400

        store = StoreModel(name)

        try:
            store.save_on_db()
            return store.json(), 201
        except:
            return {'message': 'Store cannot be created. Internat problem detected'}, 500

    @jwt_required()
    def delete(self, name):

        store = StoreModel.find_by_name(name)

        if store is not None:
            # delete item
            store.delete_from_db()
            return {'message': 'the item was deleted!'}, 200

        # if the item was not found
        return {'message': 'the item was not found!'}, 400


class StoreList(Resource):

    @jwt_required()
    def get(self):
        return {"stores": [store.json() for store in StoreModel.query.all()]}
