from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] = "PlgIqv3elU6htFRdeXVbrMYz4lHG3tkq"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///caudalie.db"


db = SQLAlchemy(app)

login_manager = LoginManager(app)
