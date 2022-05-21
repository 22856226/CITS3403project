import unittest
from app import app, db
from app.models import User
import tempfile
import os
''''
user = User(username='Tester', password_hash='123456789', movetimes='100')
db.session.add(user)
db.session.commit()

user2 = User(username='Tester2', password_hash='987654321', movetimes='60')
db.session.add(user2)
db.session.commit()
'''
user = User.query.get(1)
user.movetimes = user.movetimes + int(50)
db.session.commit()
print(user.movetimes)


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def setUp(self): # A new test client is created and a new database is initialized
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        self.app = app.test_client()
        app.init_db()

    def tearDown(self):   #Close the file and delete it from the file system
        os.close(self.db_fd)
        os.unlink(app.DATABASE)

    def test_empty_db(self):
        rv = self.app.get('/')
        assert 'No entries here so far' in rv.data
    
    # Test login, logout and register
    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
            ), follow_redirects=True)
    def logout(self):
        return self.app.get('/logout', follow_redirects=True)
    def test_login_logout(self):
        rv = self.login('Tester', '123456789')
        assert 'You were logged in' in rv.data
        rv = self.logout()
        assert 'You were logged out' in rv.data
        rv = self.login('wrong', '123456789')
        assert 'Invalid username' in rv.data
        rv = self.login('Tester', '1234567')
        assert 'Invalid password' in rv.data
    def test_register(self):
        self.login('admin', '88888888')
        rv = self.app.post('/add', data=dict(
        username='admin',
        password_hash='88888888'
        ), follow_redirects=True)
        assert 'No entries here so far' not in rv.data
        assert 'admin' in rv.data
        assert '88888888' in rv.data

if __name__ == '__main__':
    unittest.main()