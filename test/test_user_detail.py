import unittest
import json
from app_flask import app, storage, User, UserDetail

class TestUserDetail(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        # Initialize storage with a user for testing
        user = User('test@example.com', 'John', 'Doe')
        storage[user.id] = user

    def tearDown(self):
        storage.clear()

    def test_get_user(self):
        # Test case for retrieving an existing user
        user_id = list(storage.keys())[0]
        response = self.app.get(f'/users/{user_id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('email', json.loads(response.data))

    def test_get_nonexistent_user(self):
        # Test case for retrieving a non-existent user
        response = self.app.get('/users/nonexistent-id')
        self.assertEqual(response.status_code, 404)
        self.assertIn('User not found', json.loads(response.data)['message'])

    # Add more test cases for UserDetail as needed

if __name__ == '__main__':
    unittest.main()
