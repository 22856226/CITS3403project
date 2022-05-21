from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask
from app import db

class User(db.Model):   #creating a database model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))
    movetimes = db.Column(db.Integer)

    def set_password(self, password):   #check the password
        self.password_hash = generate_password_hash(password)
    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)

