from flask import Blueprint

# Initialize a blueprint for user routes
user_bp = Blueprint('user_bp', __name__)

# Import the user routes (this will register the routes)
from . import user_routes
