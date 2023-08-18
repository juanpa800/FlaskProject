import os

class Config:
    SECRET_KEY = os.urandom(24).hex()

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig 
}