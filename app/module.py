from __init__ import db

class User(db.Model):   #creating user data
    __tablename__= 'user data'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(128))
    is_active = db.Column(db.Boolean, default=True)
    moves_data = db.Column(db.Integer, unique=True)
    def __repr__(self):
        return 'User:%s' % self.name


