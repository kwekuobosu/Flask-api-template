from flask import Blueprint

v1_test = Blueprint('v1_test', __name__, url_prefix='/test')

from app.controllers import test