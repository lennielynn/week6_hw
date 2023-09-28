from flask_smorest import Blueprint

#any route ("/") with the bp prefix will use the url listed
bp = Blueprint('store', __name__, url_prefix='/store')

from . import routes