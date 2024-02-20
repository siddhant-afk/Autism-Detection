from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.app_context().push()
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///results.db'
db = SQLAlchemy(app)