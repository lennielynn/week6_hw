from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from Config import Config 
app = Flask(__name__)
app.config.from_object(Config) 

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

from resources.users import bp as user_bp
api.register_blueprint(user_bp)
from resources.store import bp as post_bp
api.register_blueprint(post_bp)

from resources.users import routes
from resources.store import routes

from resources.users.UserModel import UserModel
