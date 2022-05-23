from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login

class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(db.Model):
    __tablename__ = "post"
    level1 = db.Column(db.Integer)
    level2 = db.Column(db.Integer)
    level3 = db.Column(db.Integer)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    user_name = db.Column(db.String(64), primary_key=True,  nullable=False)

    def __repr__(self):
        return '<Post {}>'.format(self.user_name )
@login.user_loader
def load_user(id):
    return User.query.get(int(id))