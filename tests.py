import unittest
from app import app, db, User

user = User(name='Grey Li')

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