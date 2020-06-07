from flask import Flask
from flask_mongoengine import MongoEngine
from app.config import MONGODB_DB, MONGODB_HOST, MONGODB_PORT

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': MONGODB_DB,
    'host': MONGODB_HOST,
    'port': MONGODB_PORT
}

db = MongoEngine(app)

from app.controllers import v1_test
app.register_blueprint(v1_test)