from marshmallow import Schema, fields

class ItemSchema(Schema):
  id = fields.Str(dumps_only = True)
  item = fields.Str(required = True)
  item_id = fields.Str(required = True)

class UserSchema(Schema):
  id = fields.Str(dumps_only = True)
  username = fields.Str(required = True)
  email = fields.Str(required = True)
  password = fields.Str(required = True)
  first_name = fields.Str()
  last_name = fields.Str()

class UpdateUserSchema(Schema):
  username = fields.Str()
  email = fields.Str()
  password = fields.Str(required = True)
  new_password = fields.Str()
  first_name = fields.Str()
  last_name = fields.Str()

class DeleteUserSchema(Schema):
  username = fields.Str(required = True)
  password = fields.Str(required = True)