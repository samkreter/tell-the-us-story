from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os




app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

print(os.environ['APP_SETTINGS'])

db = SQLAlchemy(app)

from app import views, models

