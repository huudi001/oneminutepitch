import os

class Config:
    '''
    general configuration
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
    '''
    production configuration child class
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    '''
    development configuration child class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://khalid:pythonista@localhost/oneminutepitch'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
