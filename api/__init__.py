from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABSE_URI"] = "sqlite:///flaskdatabase.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    CORS(app)

