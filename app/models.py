from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(db.Model):   #creating user data
    __tablename__= 'user data'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(128))
    is_active = db.Column(db.Boolean, default=True)
    moves_data = db.Column(db.Integer, unique=True)
    def __repr__(self):
        return 'User:%s' % self.name
        
    def set_password(self, password):   #check the password
        self.password = generate_password_hash(password)
    def validate_password(self, password):
        return check_password_hash(self.password, password)

