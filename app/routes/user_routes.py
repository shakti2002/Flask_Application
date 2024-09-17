from flask import Blueprint, request, jsonify
from app.services.user_service import UserService

# Define a blueprint for user-related routes
user_bp = Blueprint('users', __name__, url_prefix='/users')

# Initialize the user service
user_service = UserService()

@user_bp.route('/', methods=['GET'])
def get_users():
    users = user_service.get_all_users()
    return jsonify(users), 200

@user_bp.route('/<id>', methods=['GET'])
def get_user(id):
    user = user_service.get_user_by_id(id)
    return jsonify(user), 200

@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    user = user_service.create_user(data)
    return jsonify(user), 201

@user_bp.route('/<id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = user_service.update_user(id, data)
    return jsonify(user), 200

@user_bp.route('/<id>', methods=['DELETE'])
def delete_user(id):
    user_service.delete_user(id)
    return jsonify({"message": "User deleted successfully"}), 200
