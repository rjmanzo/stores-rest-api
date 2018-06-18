
from flask_restful import Resource, Api, reqparse
from flask_jwt import jwt_required

from models.item import ItemModel


class Item(Resource):
    # we define the request argument at top. POST & PUT need the same data
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True,
                        help='this field cannot be left blank!')
    parser.add_argument('store_id', type=int, required=True,
                        help='this store cannot be left blank!')

    @jwt_required()
    def get(self, name):

        item = ItemModel.find_by_name(name)  # check if item exist

        if item is not None:
            return item.json(), 200

        # if item dont exists
        return {"message": "item not found"}, 404

    @jwt_required()
    def post(self, name):
        # verify that the name was not taken. If was return a message
        if ItemModel.find_by_name(name) is not None:
            return {'message': "An item with name '{}' already exist".format(name)}, 400

        data = Item.parser.parse_args()

        item = ItemModel(name, data['price'], data['store_id'])

        try:
            item.save_on_db()
            return item.json(), 201
        except:
            return {"message": "the item could not be inserted!"}, 500

    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)

        if item is not None:
            # delete item
            item.delete_from_db()
            return {'message': 'the item was deleted!'}, 200

        # if the item was not found
        return {'message': 'the item was not found!'}, 400

    @jwt_required()
    def put(self, name):

        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        # verify that the name was not taken. If was return a message
        if item is None:
            item = ItemModel(name, data['price'], data['store_id'])
            status_code = 201  # Insertion of new item
        else:
            item.price = data['price']
            item.store_id = data['store_id']
            status_code = 200

        item.save_on_db()
        return item.json(), status_code


class ItemList(Resource):

    @jwt_required()
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}
