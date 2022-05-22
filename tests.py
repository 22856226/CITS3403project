import unittest
from app import app, db
from app.models import User
from flask import session
'''
user = User(username='Tester', password_hash='123456789', scores='100')
db.session.add(user)
db.session.commit()


user2 = User(username='Tester2', password_hash='987654321', scores='60')
db.session.add(user2)
db.session.commit()

player = User.query.filter_by(username=session('Tester')).first()
db.session.commit()
print(player.scores)

user.scores = user.scores + int(50)
db.session.commit()

print(user.scores)
'''

class GameTestCase(unittest.TestCase):
    def setUp(self): # A new test client is created and a new database is initialized
        app.config.update(
            TESTING=True,
            SQLALCHEMY_DATABASE_URI='sqlite:///:memory:'
        )
        db.create_all()
        self.client = app.test_client()

    # Test login, logout and register
    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
            ), follow_redirects=True)
    def logout(self):
        return self.app.get('/signout', follow_redirects=True)
    def register(self, username, password):
        return self.app.post('/register', data=dict(
            username=username,
            password=password
            ),follow_redirects=True)

    def test_login_logout(self):
        rv = self.login('Tester', '123456789')   #enter username and password correctly
        assert 'Login successfully!' in rv.data
        rv = self.logout()   # test logout
        assert 'You were logged out. Goodbye!' in rv.data
        rv = self.login('wrong', '123456789')   #enter incorrect username but correct password
        assert 'Incorrect username or password!' in rv.data
        rv = self.login('Tester', '1234567')   #enter correct username but incorrect password
        assert 'Incorrect username or password!' in rv.data

    def test_register(self):
        rv = self.register(username='Tester2', password='88888888')   # test register a account
        assert 'Invalid input!' not in rv.data
        assert 'New player is created.' in rv.data
        rv = self.register(username='', password='88888888')   # test blank input of username or password
        assert 'Invalid input!' in rv.data
        rv = self.register(username='Tester2', password='')
        assert 'Invalid input!' in rv.data
    
    def tearDown(self):   #Close the file and delete it from the file system
        db.session.remove()
        db.drop_all()

if __name__ == '__main__':
    unittest.main()

