import unittest
from app import app, db
from app.models import User

user = User(username='Tester', password_hash='123456789')
db.session.add(user)
db.session.commit()

class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_one(self):
        rv = one()
        self.assertEqual(rv, 'admin')

if __name__ == '__main__':
    unittest.main()