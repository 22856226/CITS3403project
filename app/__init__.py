from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
import os
import sys

app = Flask(__name__)
# Update the path to locate the file to the project root directory
app.config['SECRET_KEY'] = 'dev'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)   #initialize the extension and pass in the app instance
# migrate = Migrate(app, db)

from app import routes, models

db.create_all()   # Creating a database
