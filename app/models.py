from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from flask import session

class User(db.Model):   #creating user data
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))
    scores = db.Column(db.Integer)
    
    def set_password(self, password):   #check the password
        self.password_hash = generate_password_hash(password)
    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)

def current(curr_player):
    for player in User:
        if player.curr_player == User.query.get(curr_player):
            return player