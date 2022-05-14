from flask import Flask
from app.store_pwd import db
import os
import sys

app = Flask(__name__)
# Update the path to locate the file to the project root directory
app.config['SECRET_KEY'] = 'dev'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from app import routes

db.create_all()   # Creating a database
