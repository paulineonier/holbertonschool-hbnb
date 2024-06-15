from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from uuid import uuid4
from datetime import datetime

app = Flask(__name__)
api = Api(app)

# Simulate a data storage
storage = {}

class User:
    def __init__(self, email, first_name, last_name):
        self.id = str(uuid4())
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

class UserManager(Resource):
    def post(self):
        data = request.get_json()
        email = data.get('email')
        first_name = data.get('first_name')
        last_name = data.get('last_name')

        if not email or not first_name or not last_name:
            return {'message': 'Missing fields'}, 400

        if '@' not in email:
            return {'message': 'Invalid email format'}, 400

        if email in [user.email for user in storage.values()]:
            return {'message': 'Email already exists'}, 409

        user = User(email, first_name, last_name)
        storage[user.id] = user
        return user.to_dict(), 201

    def get(self):
        return [user.to_dict() for user in storage.values()], 200

class UserDetail(Resource):
    def get(self, user_id):
        user = storage.get(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        return user.to_dict(), 200

    def put(self, user_id):
        user = storage.get(user_id)
        if not user:
            return {'message': 'User not found'}, 404

        data = request.get_json()
        email = data.get('email')
        first_name = data.get('first_name')
        last_name = data.get('last_name')

        if email:
            if '@' not in email:
                return {'message': 'Invalid email format'}, 400
            if email != user.email and email in [u.email for u in storage.values()]:
                return {'message': 'Email already exists'}, 409
            user.email = email

        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name

        user.updated_at = datetime.utcnow()
        return user.to_dict(), 200

    def delete(self, user_id):
        user = storage.pop(user_id, None)
        if not user:
            return {'message': 'User not found'}, 404
        return '', 204

api.add_resource(UserManager, '/users')
api.add_resource(UserDetail, '/users/<string:user_id>')

if __name__ == '__main__':
    app.run(debug=True)
