from flask import Flask
from flask_cors import CORS
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
cors = CORS(app)

from app import routes