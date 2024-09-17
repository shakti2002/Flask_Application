from flask import Flask
from flask_pymongo import PyMongo
from flask_marshmallow import Marshmallow
from app.config import Config

# Initialize extensions
mongo = PyMongo()
ma = Marshmallow()

def create_app():
    # Initialize the Flask app
    app = Flask(__name__)
    
    # Load configuration from config.py
    app.config.from_object(Config)
    
    # Initialize extensions with the app
    mongo.init_app(app)
    ma.init_app(app)
    
    # Register Blueprints (for routes)
    from app.routes import user_routes
    app.register_blueprint(user_routes.user_bp)
    
    return app
