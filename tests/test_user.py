import unittest
from app import create_app, mongo
from flask import json

class UserTestCase(unittest.TestCase):

    def setUp(self):
        # Set up the test app
        self.app = create_app()
        self.client = self.app.test_client()

        # Initialize some test data
        self.test_user = {
            "id": "123",
            "name": "John Doe",
            "email": "johndoe@example.com",
            "password": "password123"
        }
        
        self.updated_user = {
            "name": "Jane Doe",
            "email": "janedoe@example.com",
            "password": "newpassword456"
        }
        
        # Clean up database before each test
        with self.app.app_context():
            mongo.db.users.delete_many({})

    def test_get_users(self):
        # Initially, there should be no users
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])

    def test_create_user(self):
        # Test creating a user
        response = self.client.post('/users/', json=self.test_user)
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data['name'], self.test_user['name'])
        self.assertEqual(data['email'], self.test_user['email'])

        # Verify the user was added to the database
        response = self.client.get('/users/')
        self.assertEqual(len(response.get_json()), 1)

    def test_get_user_by_id(self):
        # First create a user
        self.client.post('/users/', json=self.test_user)

        # Fetch the user by ID
        response = self.client.get(f'/users/{self.test_user["id"]}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['name'], self.test_user['name'])
        self.assertEqual(data['email'], self.test_user['email'])

    def test_update_user(self):
        # First create a user
        self.client.post('/users/', json=self.test_user)

        # Update the user
        response = self.client.put(f'/users/{self.test_user["id"]}', json=self.updated_user)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['name'], self.updated_user['name'])
        self.assertEqual(data['email'], self.updated_user['email'])

    def test_delete_user(self):
        # First create a user
        self.client.post('/users/', json=self.test_user)

        # Delete the user
        response = self.client.delete(f'/users/{self.test_user["id"]}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'User deleted successfully')

        # Verify the user no longer exists
        response = self.client.get(f'/users/{self.test_user["id"]}')
        self.assertEqual(response.status_code, 404)

    def tearDown(self):
        # Clean up after each test
        with self.app.app_context():
            mongo.db.users.delete_many({})

if __name__ == "__main__":
    unittest.main()
