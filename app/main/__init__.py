from flask import Blueprint

# create blue print object
bp = Blueprint('main', __name__)

# import routes
from app.main import routes
