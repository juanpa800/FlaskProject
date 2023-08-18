import os

class Config:
    SECRET_KEY = os.urandom(24).hex()

class DevelopmentConfig(Config):
    DEBUG = True

db ={
    'SQLSERVER_SERVER': '(localdb)\LocalFlaskP1',  # Your server name
    'SQLSERVER_DATABASE': 'DBPruebaDatabase',
    'u': '',  # Your login
    'p':''  # Your login password
}

config = {
    'development': DevelopmentConfig 
}