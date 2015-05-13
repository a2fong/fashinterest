from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
manager = APIManager(flask_sqlalchemy_db=db)
manager.init_app(app)

from app import views,models
