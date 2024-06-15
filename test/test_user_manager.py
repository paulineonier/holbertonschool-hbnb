import unittest
import json
from app_flask import app, storage, User, UserManager

class TestUserManager(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        storage.clear()

    def test_post_user(self):
        # Test case for creating a new user
        data = {
            'email': 'test@example.com',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        response = self.app.post('/users', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', json.loads(response.data))
        self.assertEqual(len(storage), 1)

    def test_post_user_missing_fields(self):
        # Test case for missing fields in user creation
        data = {
            'email': 'test@example.com',
            'first_name': 'John'
            # Missing last_name
        }
        response = self.app.post('/users', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(storage, {})  # Storage should remain empty

    # Add more test cases for UserManager as needed

if __name__ == '__main__':
    unittest.main()
