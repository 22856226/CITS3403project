from functools import wraps
from flask import Flask, flash, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
import os



app = Flask(__name__)
# Update the path to locate the file to the project root directory
app.config['SECRET_KEY'] = 'dev'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#creat a database
db = SQLAlchemy(app)
