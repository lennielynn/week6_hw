from flask import request
from uuid import uuid4
from flask.views import MethodView
from flask_smorest import abort
#^^^^imports function abort from smorest library (abort is used when an error code is responded)

from schemas import ItemSchema
from . import bp
#^^^^^^imports blueprint from __init__
from db import store

@bp.route('/')
class StoreFront(MethodView):
  def get(self):
    return {'store': store}

  @bp.arguments(ItemSchema)
  def post(self, store_data):
    store[uuid4().hex] = store_data
    return store_data, 201



@bp.route('/<item_id>')
class SellerItems(MethodView):
  
  def get(self, item_id):
    try:
      item = store[item_id]
      return item, 200
    except KeyError:
      abort(404, message='Item not Found')
      #func, stat code, specified message^^
      # return {'message': 'post not found'}, 400

  @bp.arguments(ItemSchema)
  def put(self, store_data, item_id):
    if item_id in store:
      item = store[item_id]
      if store_data['item_id'] != store['item_id']:
        abort(400, message='Cannot edit other users items')
      #func, stat code, specified message^^
      store['item'] = store_data['item']
      return item, 200
    abort(404, message='Item not Found')
    #func, stat code, specified message^^

  def delete(self, item_id):
    try:
      deleted_item = store.pop(item_id)
      return {'message':f'{deleted_item["body"]} deleted'}, 202
    except KeyError:
      abort(404, message='Item not found')
     #func, stat code, specified message^^