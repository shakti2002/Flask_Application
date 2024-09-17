import os

class Config:
    MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://mongo:27017/mydatabase')
    SECRET_KEY = os.environ.get('SECRET_KEY', 'supersecretkey')
