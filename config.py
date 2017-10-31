

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://khalid:pythonista@localhost/oneminutepitch'




class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
