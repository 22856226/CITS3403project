import unittest
from app import app, db
from app.models import User
from flask import Flask, session
'''
user = User(username='Tester', password_hash='123456789', scores='100')
db.session.add(user)
db.session.commit()

user2 = User(username='Tester2', password_hash='987654321', scores='60')
db.session.add(user2)
db.session.commit()

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
        self.runner = app.test_cli_runner()

    # Test login, logout and register
    def login(self, username, password):
        return app.post('/login', data=dict(
            username=username,
            password=password
            ), follow_redirects=True)
    def logout(self):
        return app.get('/signout', follow_redirects=True)
    def register(self, username, email, password, password2):
        return app.post('/register', data=dict(
            username=username,
            email=email,
            password=password,
            password2=password2
            ),follow_redirects=True)
    
    def test_login(self):
        response = self.client.post('/login', data=dict(   #enter correct username and password
            username='Tester',
            password='123456789'
        ), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertNotIn('Login successfully!', data)

        response = self.client.post('/login', data=dict(   #enter correct username but incorrect password
            username='Tester',
            password='123'
        ), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertNotIn('Login successfully!', data)

        response = self.client.post('/login', data=dict(   #enter incorrect username but correct password
            username='Tester2',
            password='123456789'
        ), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertNotIn('Login successfully!', data)

        response = self.client.post('/login', data=dict(   #enter incorrect username and password
            username='Tester2',
            password='123'
        ), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertNotIn('Login successfully!', data)

        response = self.client.post('/login', data=dict(   #test blank input of username
            username='',
            password='123456789'
        ), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertNotIn('Login successfully!', data)

        response = self.client.post('/login', data=dict(   #test blank input of password
            username='Tester',
            password=''
        ), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertNotIn('Login successfully!', data)
    
    def test_logout(self):   #test logout
        self.login('Tester', '123456789')
        response = self.client.get('/logout', follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertNotIn('Goodbye.', data)

    def test_register(self):
        response = self.client.post('/register', data=dict(   #test when enter incorrect confirm password 
            username='admin',
            email='admin@gmail.com',
            password='987654321',
            password2=''
        ), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertNotIn('Congratulations, you are now a registered user!', data)

        response = self.client.post('/register', data=dict(   #test when enter incorrect email 
            username='admin',
            email='',
            password='987654321',
            password2='987654321'
        ), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertNotIn('Congratulations, you are now a registered user!', data)

        response = self.client.post('/register', data=dict(   #test when enter correct format
            username='admin',
            email='admin@gmail.com',
            password='987654321',
            password2='987654321'
        ), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertNotIn('Congratulations, you are now a registered user!', data)

    def tearDown(self):   #Close the file and delete it from the file system
        db.session.remove()
        db.drop_all()
    
    def test_app_exist(self):
        self.assertIsNotNone(app)
    
    def test_app_is_testing(self):
        self.assertTrue(app.config['TESTING'])

if __name__ == '__main__':
    unittest.main()
