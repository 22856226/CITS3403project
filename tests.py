import unittest
from app import app, db
from app.models import User
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

if __name__ == '__main__':
    unittest.main()